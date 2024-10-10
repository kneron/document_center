# YOLOv3 Step by Step

In this document, we provide a step by step example on how to utilize our tools to compile and test with a newly downloaded YOLOv3 model.

> This document is writen for toolchain v0.25.1. If any description is not consistent with the latest toolchain, please refer to the main toolchain manual.

## Step 0: Prepare environment and data

We need to download the latest toolchain docker image which contains all the tools we need.

```bash
docker pull kneron/toolchain:latest
```

Start the docker with a local folder mounted into the docker.

```bash
docker run --rm -it -v /your/folder/path/for/docker_mount:/data1 kneron/toolchain:latest
```

Go to our mounted folder and download a public keras based YOLOv3 model from Github <https://github.com/qqwweee/keras-yolo3>

```bash
cd /data1 && git clone https://github.com/qqwweee/keras-yolo3.git keras_yolo3
```

Switch to the base conda environment.

```bash
conda activate base
```

Follow the model's document to save the pretrained model as an `h5` file:

```bash
cd keras_yolo3
wget https://pjreddie.com/media/files/yolov3-tiny.weights
python convert.py yolov3-tiny.cfg yolov3-tiny.weights /data1/yolo.h5
```

We now have `yolo.h5` under our mounted folder `/data1`.

We also need to preprare some images under the mounted folder. We have provided some example input images at <http://doc.kneron.com/docs/toolchain/res/test_image10.zip>.

Here is how you can get it:

```bash
cd /data1
wget http://doc.kneron.com/docs/toolchain/res/test_image10.zip
unzip test_image10.zip
```

Now we have images in folder `test_image10/` at `/data1`; these are needed for quantization.

We also need some extra images for accuracy testing. But considering the complexity of document, we use only one image in toolchain docker for testing.

```bash
cd /data1
cp /workspace/E2E_Simulator/app/test_image_folder/yolo/000000350003.jpg ./.
```

Now we have image `000000350003.jpg` at `/data1` for testing.

## Step 1: Import KTC and required lib in python shell

Now, we go through all toolchain flow by KTC (Kneron Toolchain) using the Python API in the Python shell.

* Run "python" to open to Python shell:

<div align="center">
<img src="../../imgs/yolo_example/python_shell.png">
<p><span style="font-weight: bold;">Figure 1.</span> python shell</p>
</div>

* Import KTC and other necessary modules

```python
import ktc
import numpy as np
import os
import onnx
from PIL import Image
import numpy as np
```

## Step 2: Convert and optimize the pretrain model

You can check the model architecture with [Netron](https://netron.app/).

We find this model has no input shape, so it will be unable to run in our toolchain. We need to specify the input shape while doing the conversion.

```python
# convert h5 model to onnx
m = ktc.onnx_optimizer.keras2onnx_flow("/data1/yolo.h5", input_shape = [1, 416, 416, 3])
```

Not only do we need to do conversion, but we also need to optimize it to make it efficient and compatible with our hardware.

```python
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
```

Now, we have optimized onnx model in variable "m".
Here, we save the onnx model 'm' to disk at `/data1/yolo.opt.onnx` for further verification (like Netron or onnxruntime) in step 4.

```python
onnx.save(m,'yolo.opt.onnx')
```

## Step 3: IP Evaluation

To make sure the onnx model is as expected, we should check the onnx model's performance and see if there are any unsupprted operators (or CPU nodes).

```python
# npu (only) performance simulation
km = ktc.ModelConfig(33, "0001", "720", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))
```

The estimated FPS (NPU only) report on your terminal should look similar to this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
    ***** Warning: this model has 1 CPU ops which may cause that the report's fps is different from the actual fps *****
    ***** Warning: CPU ops types: KneronResize.

    [Evaluation Result]
    estimate FPS float = 22.5861
    total time = 44.2751 ms
    total theoretical covolution time = 16.7271 ms
    average DRAM bandwidth = 0.279219 GB/s
    MAC efficiency to total time = 37.7799 %
    MAC idle time = 3.85105 ms
    MAC running time = 40.424 ms
```

</div>

There are two things to take note of in this report:

* Found one CPU node 'KneronResize' in our model
  Tthe estimated FPS is 22.5861, the report is for NPU only

At the same time, a folder called `compiler` will be generated in your docker mounted folder (`/data1`); the evaluation result will be found in this folder. One important thing is to check the 'ioinfo.csv' in `/data1/compiler`, which looks like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
    i,0,input_1_o0,3,416,416
    c,0,up_sampling2d_1_o0_kn,128,26,26
    o,0,conv2d_10_o0,255,13,13
    o,1,conv2d_13_o0,255,26,26
```

</div>

This file gives information about the special nodes in the ONNX. Each line shows the information of each node, and the first element shows the type of the special node.
>type explanation:
>
>* i: input node
>* o: output node
>* c: cpu node

We can see, under KL720, one CPU node called `up_sampling2d_1_o0_kn1` in our ONNX model.

## Step 4: Check ONNX model and preprocess and postprocess are good

If we can get correct detection result from the ONNX and provided preprocess and postprocess functions, everything should be correct.

First, we need to check the preprocess and postprocess methods. [Here](<https://github.com/qqwweee/keras-yolo3/blob/master/yolo.py>) is the relevant code.
We need to move under the `keras_yolo3` before we start in order to import the preprocess and postprocess functions.

The following is the extracted preprocess:

```python
from yolo3.utils import letterbox_image

def preprocess(pil_img):
    model_input_size = (416, 416)  # to match our model input size when converting
    boxed_image = letterbox_image(pil_img, model_input_size)
    np_data = np.array(boxed_image, dtype='float32')

    np_data /= 255.
    # Insert batch dimension and transpose to match model's input.
    np_data = np.expand_dims(np_data, 0)
    np_data = np.transpose(np_data, (0, 3, 1, 2))
    return np_data
```

This is the extracted postprocess:

```python
import tensorflow as tf
import pathlib
import sys
sys.path.append(str(pathlib.Path("keras_yolo3").resolve()))
from yolo3.model import yolo_eval

def postprocess(inf_results, ori_image_shape):
    tensor_data = [tf.convert_to_tensor(data, dtype=tf.float32) for data in inf_results]
    tensor_data = [tf.transpose(data, perm=[0, 2, 3, 1]) for data in tensor_data]   # expects bhwc data

    # get anchor info
    anchors_path = "/data1/keras_yolo3/model_data/tiny_yolo_anchors.txt"
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

The result will be displayed on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```bash
(array([[258.8878 , 470.29474, 297.01447, 524.3069 ],
       [233.62653, 218.19923, 306.79245, 381.78162]], dtype=float32), array([0.9248918, 0.786504 ], dtype=float32), array([2, 7], dtype=int32))
```

</div>

This result looks good.

> Note that we only use one image as example. Using more data to check accuracy is a good idea.

## Step 5: Quantization

Let us use the same preprocess on our quantization data and put it in a list:

```python
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

Then, perform quantization. The BIE model will be generated at `/data1/output.bie`.

```python
# fix point analysis
bie_model_path = km.analysis({"input_1_o0": img_list})
print("\nFix point analysis done. Save bie model to '" + str(bie_model_path) + "'")
```

## Step 6: Check if BIE model accuracy is good enough

After quantization, the slight drop in model accuracy is expected. We should check if this accuracy is good enough to use.

Toolchain API `ktc.kneron_inference` can help us to check. The usage of 'ktc.kneron_inference' is similar to Step 4, but there are several differences:

1. The 2nd parameter is changed from onnx_file to bie_file.

```python
## bie model check
input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# bie inference
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"], platform=720)

# bie output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)
```

The result will be displayed on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```bash
(array([[258.51468, 467.71683, 293.07394, 529.15967]], dtype=float32), array([0.8253723], dtype=float32), array([2], dtype=int32))
```

</div>

This is slightly different from the result in Step 3: we lost one bounding box after quantization. Note that this loss is acceptable after quantization.

*If you are running the example using 720 as the hardware platform, there might be one extra bounding box. This is normal.*

## Step 7: Compile

The final step is compile the BIE model into an NEF model.

```python
# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")
```

You can find the NEF file under `/data1/batch_compile/models_720.nef`. `models_720.nef` is the final compiled model.


## (optional) Step 8. Check NEF model

Toolchain api `ktc.inference` does support NEF model inference. The usage of `ktc.kneron_inference` is similar to the steps in Step 4 and Step 6, with minor differences.

1. The 2nd parameter is changed from to nef_model.

```python
# nef model check
input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# nef inference
out_data = ktc.kneron_inference([in_data], nef_file=nef_model_path, input_names=["input_1_o0"], platform=720)

# nef output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)
```

The result will be displayed on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```bash
(array([[258.51468, 467.71683, 293.07394, 529.15967]], dtype=float32), array([0.8253723], dtype=float32), array([2], dtype=int32))
```

</div>

> Note: the NEF model results should be exactly the same as the BIE model results.

## Step 9. Prepare Kneron PLUS (Don't do it in toolchain docker)

To run NEF on KL720, we need help from [Kneron PLUS](http://doc.kneron.com/docs/#plus/getting_started/):

1. Connect KL720 USB dongle to your computer
2. Follow the instruction in document([Kneron PLUS](http://doc.kneron.com/docs/#plus/getting_started/)) to setup the environment (Note: python usage document is at "kneron_plus/python/README.md" in Kneron PLUS folder)

## Step 10. Run our yolo NEF on KL720 with Kneron PLUS

We leverage the provided the example code in Kneron PLUS to run our YOLO NEF.

1. Replace `kneron_plus/res/models/KL720/tiny_yolo_v3/models_720.nef` with our YOLO NEF.
2. Modify `kneron_plus/python/example/KL720DemoGenericInferencePostYolo.py` line 20. Change input image from "bike_cars_street_224x224.bmp" to "bike_cars_street_416x416.bmp"

<div align="center">
<img src="../../imgs/yolo_example/kplus_modify_input_img.png">
<p><span style="font-weight: bold;">Figure 2.</span> modify input image in example </p>
</div>

3. Modify line 105. change normaization method in preprocess config from "Kneron" mode to "Yolo" mode

<div align="center">
<img src="../../imgs/yolo_example/preprocess_from_KnMod_to_YoloMod.png">
<p><span style="font-weight: bold;">Figure 3.</span> modify normalization method in example </p>
</div>

4. Run example `KL720DemoGenericInferencePostYolo.py`

```bash
    cd kneron_plus/python/example
    python KL720DemoGenericInferencePostYolo.py
```

Then, you should see the YOLO NEF detection result is saved to "./output_bike_cars_street_416x416.bmp" :

<div align="center">
<img src="../../imgs/yolo_example/detection_res.png">
<p><span style="font-weight: bold;">Figure 4.</span> detection result </p>
</div>

## Appendix

The whole model conversion process from ONNX to NEF (Steps 1-6) can be combined into one Python script:

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
    tensor_data = [tf.transpose(data, perm=[0, 2, 3, 1]) for data in tensor_data]   # expects bhwc data

    # get anchor info
    anchors_path = "/data1/keras_yolo3/model_data/tiny_yolo_anchors.txt"
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
    # Insert batch dimension and transpose to match model's input.
    np_data = np.expand_dims(np_data, 0)
    np_data = np.transpose(np_data, (0, 3, 1, 2))
    return np_data


# convert h5 model to onnx
m = ktc.onnx_optimizer.keras2onnx_flow("/data1/yolo.h5", input_shape = [1,416,416,3])
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
onnx.save(m,'yolo.opt.onnx')


# setup ktc config
km = ktc.ModelConfig(33, "0001", "720", onnx_model=m)

# npu(only) performance simulation
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
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"], platform=720)
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)


# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")

# nef model check
input_image = Image.open('/data1/000000350003.jpg')
in_data = preprocess(input_image)
out_data = ktc.kneron_inference([in_data], nef_file=nef_model_path, input_names=["input_1_o0"],  platform=720)
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)
```
