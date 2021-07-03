# YOLOv3 Step by Step

In this document, we provide a step by step example on how to utilize our tools to compile and test with a newly downloaded YOLOv3 model.

## Step 0: Prepare environment and data

We need to download the latest toolchain docker image which contains all the tools we need.

```bash
docker pull kneron/toolchain:latest
```

Start the docker with a local folder mounted into the docker.

```
docker run --rm -it -v /your/folder/path/for/docker_mount:/data1 kneron/toolchain:latest
```

go to our mounted folder and download a public keras based YOLOv3 model from Github <https://github.com/qqwweee/keras-yolo3>

```bash
cd /data1 && git clone https://github.com/qqwweee/keras-yolo3.git keras_yolo3
```
follow the model's document to save the pretrain model as an `h5` model:

```bash
cd keras-yolo3
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights /data1/yolo.h5
```

We now have `yolo.h5` under our mounted folder `/data1`.

We also need to preprare some images under the mounted folder. We have provided some example input images at <http://doc.kneron.com/docs/toolchain/res/test_image10.zip>.

Here is how you can get it:
```bash
cd /data1
wget http://doc.kneron.com/docs/toolchain/res/test_image10.zip
unzip test_image10.zip
```
Now we have images in folder `test_image10/` at `/data1`, this is for quantization.

We also need some extra images for accuracy testing. But considering the complexity of document, we use only one image in toolchain docker for testing. 

```bash
cd /data1
cp /workspace/E2E_Simulator/app/test_image_folder/yolo/000000350003.jpg ./.
```
Now we have images `000000350003.jpg` at `/data1`, this is for testing.

## Step 1: Import KTC and required lib in python shell
Now, we go through all toolchain flow by KTC(Kneron Toolchain) python api in python shell.
* run "python" to open to python shell:
<div align="center">
<img src="../imgs/yolo_example/python_shell.png">
<p><span style="font-weight: bold;">Figure 1.</span> python shell</p>
</div>
and then, 

* import KTC and others necessary libs

```python
import ktc
import os
import onnx
from PIL import Image
import numpy as np
```

## Step 2: Convert and optimize the pretrain model

You can check model architecture with [Netron](https://netron.app/).

We could find this model has no input shape, it's illegal for our toolchain. We need to specify the input shape while doing the conversion. 

```python
# convert h5 model to onnx
m = ktc.onnx_optimizer.keras2onnx_flow("/data1/yolo.h5", input_shape = [1,416,416,3])
```

Not only conversion, we also need to optimize it to make it compatible and efficient for our hardware.

```python
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
```

Now, we have optimized onnx model in variable "m".
We can save the onnx model 'm' to disk for further check (like Netron or onnxruntime).

```python
onnx.save(m,'yolo.opt.onnx')
```
Here we save it to `/data1/yolo.opt.onnx` for further verification in Step 4.

## Step 3: IP Evaluation
To make sure the onnx model is expected, we had better check the onnx model's performance and if there is any unsuppoorted operator (or cpu node) inside.



```python
# npu(only) performance simulation
km = ktc.ModelConfig(1001, "0001", "520", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))
```



you can see the estimated fps (npu only) report shown on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
    Npu performance evaluation result:
    ***** Warning: this model has 1 CPU ops which may cause that the report's fps is different from the actual fps *****
    ***** Warning: CPU ops types: KneronResize.

    [Evaluation Result]
    estimate FPS float = 1.39266
    total time = 718.052 ms
    total theoretical covolution time = 213.788 ms
    average DRAM bandwidth = 0.341753 GB/s
    MAC efficiency to total time = 29.7734 %
    MAC idle time = 153.815 ms
    MAC running time = 564.237 ms
    
```

</div>

two things we have to emphasize on this report:
* 1 op type will run as cpu node in our model, which type is KneronResize
* the estimated FPS is 1.39266, the report is for NPU only

at the same time, a folder "compiler" will be generated in your docker mounted folder(/data1), the evaluation result could be found in that folder. One important thing is to check the 'ioinfo.csv' in /data1/compiler, it looks like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
    i,0,input_1_o0,3,416,416
    c,0,up_sampling2d_1_o0_kn,256,26,26
    c,1,up_sampling2d_2_o0_kn,128,52,52
    o,0,conv2d_59_o0,255,13,13
    o,1,conv2d_67_o0,255,26,26
    o,2,conv2d_75_o0,255,52,52
```

</div>


this file show us some special node in onnx.
each line shows the information of each node, and the first element of a line shows the type of the special node.
>type explaination:
>* i : input node
>* o : output node
>* c : cpu node

so under kl520, there are two cpu node in our onnx model, the node name are 'up_sampling2d_1_o0_kn' and 'up_sampling2d_2_o0_kn'

## Step 4: Check ONNX model and Pre&Post process are good 
If we can get correct detection result from onnx and given pre post process, everything should be good.

At first, we need to check the pre and post process method. we can find the information at following code <https://github.com/qqwweee/keras-yolo3/blob/master/yolo.py>.

here is the extracted pre process:
``` python
from yolo3.utils import letterbox_image

def preprocess(pil_img):
    model_input_size = (416, 416)  # to match our model input size when converting
    boxed_image = letterbox_image(pil_img, model_input_size)
    np_data = np.array(boxed_image, dtype='float32')

    np_data /= 255.
    return np_data
```

and post process:
``` python
import tensorflow as tf
import pathlib
import sys
sys.path.append(str(pathlib.Path("keras_yolo3").resolve()))
from yolo3.model import yolo_eval

def postprocess(inf_results, ori_image_shape):
    tensor_data = [tf.convert_to_tensor(data, dtype=tf.float32) for data in inf_results]

    # get anchor info
    anchors_path = "/data1/keras_yolo3/model_data/yolo_anchors.txt"
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    anchors = np.array(anchors).reshape(-1, 2)

    # post process
    num_classes = 80
    boxes, scores, classes = yolo_eval(tensor_data, anchors, num_classes, ori_image_shape)
    with tf.Session() as sess:
        boxes = boxes.eval()
        scores = scores.eval()
        classes = classes.eval()

    return boxes, scores, classes
```
Now, we can check the ONNX inference result with api 'ktc.kneron_inference'.

```python
## onnx model check

input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# onnx inference 
out_data = ktc.kneron_inference([in_data], onnx_file="/data1/yolo.opt.onnx", input_names=["input_1_o0"])

# onnx output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])

print(det_res)
```
you can see the result on your terminal like this:
<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
(array([[251.099  , 535.6055 , 298.40985, 551.92285],
       [256.12146, 408.87692, 295.4361 , 424.1309 ],
       [259.28464, 474.59253, 298.83353, 525.9219 ],
       [238.99045, 233.12668, 309.90186, 364.7603 ]], dtype=float32), array([0.9018596 , 0.88071007, 0.99525476, 0.87767243], dtype=float32), array([0, 0, 2, 7], dtype=int32))
```

</div>
looks good.

*Note that we only use one image as example. Use more data to check accuracy is a good idea.

## Step 5: Quantization
We found the preprocess method at Step 4.

do the same things on our quantization data and put it in a list:

```bash
# load and normalize all image data from folder
img_list = []
for (dir_path, _, file_names) in os.walk("/data1/test_image10"):
    for f_n in file_names:
        fullpath = os.path.join(dir_path, f_n)
        print("processing image: " + fullpath)
        
        image = Image.open(fullpath)
        img_data = preprocess(image)
        img_list.append(img_data)
```

then do quantization:

```python
# fix point analysis
bie_model_path = km.analysis({"input_1_o0": img_list})
print("\nFix point analysis done. Save bie model to '" + str(bie_model_path) + "'")
```

the bie model will be generated at `/data1/output.bie`.

## Step 6: Check BIE model accuracy is good enough
After quantization, the model accuracy slightly drop is expected. We had better check the accuracy is good enough to use. 

Toolchain api 'ktc.kneron_inference' can help us to check. The usage of 'ktc.kneron_inference' is similar to Step 4, only one different is at the 2nd parameter, changed from onnx_file to bie_file:

```python
## bie model check

input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# bie inference 
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"])

# bie output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])

print(det_res)
```

you can see the result on your terminal like this:
<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
(array([[252.5644 , 409.62875, 298.71826, 422.9387 ],
       [251.66833, 534.666  , 297.8222 , 552.76654],
       [261.4086 , 474.91138, 296.7932 , 525.6806 ],
       [239.97507, 229.75151, 309.20587, 369.74634]], dtype=float32), array([0.8616499 , 0.82176036, 0.9962568 , 0.82386315], dtype=float32), array([0, 0, 2, 7], dtype=int32))
```

</div>
slightly different from the Step 3, but looks good enough.

*Note that we only use one image as example. Use more data to check accuracy is a good idea.

## Step 7: Compile

The final step is compile the bie model to nef model. 

```python
# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")
```

You can find the `nef` file under `/data1/batch_compile/models_520.nef`.
The 'models_520.nef' is the final compiled model.

To learn the usage of generated NEF model on KL520, please check the document in following link:
http://doc.kneron.com/docs/#520_1.5.0.0/getting_start/


## (optional) Step 8. Check NEF model 
Toolchain api 'ktc.inference' does support doing NEF model inference. The usage of 'ktc.kneron_inference' is similar to Step 4 and Step 6, only two things are different
* the 2nd parameter of 'ktc.kneron_inference' is 'nef_model'
* need to check 'radix' (see the toolchain mannual to learn more)

the code looks like this:

```python
# nef model check

input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# check nef radix from quantization data
radix = ktc.get_radix(img_list)
# nef inference
out_data = ktc.kneron_inference([in_data], nef_file=nef_model_path, radix=radix)

# nef output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])

print(det_res)
```
you can see the result on your terminal like this:
<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
(array([[251.66833, 534.666  , 297.8222 , 552.76654],
       [252.5644 , 409.62875, 298.71826, 422.9387 ],
       [262.0151 , 474.91138, 297.39972, 525.6806 ],
       [239.97507, 229.75151, 309.20587, 369.74634]], dtype=float32), array([0.86275786, 0.86213624, 0.99394107, 0.8687069 ], dtype=float32), array([0, 0, 2, 7], dtype=int32))
```

</div>

the NEF model should be exactly the same as the BIE model results. However, in this case, the differences are due to precision loss when converting the preprocessed input into fixed point values.


## Appendix
The whole model conversion process from onnx to nef(step 1 ~ 6) could be written into one python script:

```python
import ktc
import os
import onnx
from PIL import Image
import numpy as np


###  post process function  ###
import tensorflow as tf
import pathlib
import sys
sys.path.append(str(pathlib.Path("keras_yolo3").resolve()))
from yolo3.model import yolo_eval

def postprocess(inf_results, ori_image_shape):
    tensor_data = [tf.convert_to_tensor(data, dtype=tf.float32) for data in inf_results]

    # get anchor info
    anchors_path = "/data1/keras_yolo3/model_data/yolo_anchors.txt"
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    anchors = np.array(anchors).reshape(-1, 2)

    # post process
    num_classes = 80
    boxes, scores, classes = yolo_eval(tensor_data, anchors, num_classes, ori_image_shape)
    with tf.Session() as sess:
        boxes = boxes.eval()
        scores = scores.eval()
        classes = classes.eval()

    return boxes, scores, classes



###  pre process function  ###
from yolo3.utils import letterbox_image

def preprocess(pil_img):
    model_input_size = (416, 416)  # to match our model input size when converting
    boxed_image = letterbox_image(pil_img, model_input_size)
    np_data = np.array(boxed_image, dtype='float32')

    np_data /= 255.
    return np_data




# convert h5 model to onnx
m = ktc.onnx_optimizer.keras2onnx_flow("/data1/yolo.h5", input_shape = [1,416,416,3])
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
onnx.save(m,'yolo.opt.onnx')


# npu(only) performance simulation
km = ktc.ModelConfig(1001, "0001", "520", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))



## onnx model check
input_image = Image.open('/data1/000000350003.jpg')
in_data = preprocess(input_image)
out_data = ktc.kneron_inference([in_data], onnx_file="/data1/yolo.opt.onnx", input_names=["input_1_o0"])
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)

# load and normalize all image data from folder
img_list = []
for (dir_path, _, file_names) in os.walk("/data1/test_image10"):
    for f_n in file_names:
        fullpath = os.path.join(dir_path, f_n)
        print("processing image: " + fullpath)
        
        image = Image.open(fullpath)
        img_data = preprocess(image)
        img_list.append(img_data)


# fix point analysis
bie_model_path = km.analysis({"input_1_o0": img_list})
print("\nFix point analysis done. Save bie model to '" + str(bie_model_path) + "'")


# bie model check
input_image = Image.open('/data1/000000350003.jpg')
in_data = preprocess(input_image)
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"])
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)


# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")

# nef model check
input_image = Image.open('/data1/000000350003.jpg')
in_data = preprocess(input_image)
out_data = ktc.kneron_inference([in_data], nef_file=nef_model_path, radix=7)
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)

```