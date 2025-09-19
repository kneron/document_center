# YOLOv3 with In-Model-Preprocess trick Step by Step

In this document, we provide a step by step example on how to utilize our tools to compile and test with a newly downloaded YOLOv3 model. We found data normalization is quite disturbing when doing model quantization and porting, so we also provide a trick to let user port their models without worrying about this.

>  The major difference between Yolo Example and this example:
> 1. Step 2: Convert and optimize the pretrain model.
> 2. Step 4: Check ONNX model and preprocess and postprocess are good.

> This document is writen for toolchain v0.22.0. If any description is not consistent with the latest toolchain, please refer to the main toolchain manual.

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
wget https://data.pjreddie.com/files/yolov3.weights
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

Now, in order to make model porting easier, we do In-Model-Preprocess trick. We add a Batchnormalization layer at model front, this Batchnormalization layer will do the following things:
1. divide 255 for every pixel (data normalization required by this model)
2. add 0.5 (hardware require -128 to 127 input but source data is 0 to 255, so we will substract 128 for source data due to hardware requirement, and add back at model's front)


```python
# add pixel modify node:
#   1. scaling 1/255 for every channel due to original normalize method,
#   2. shift 0.5 to change input range from 0~255 to -128 to 127
ktc.onnx_optimizer.pixel_modify(m, [1/255, 1/255, 1/255], [0.5, 0.5, 0.5])

# do onnx2onnx again to calculate "pixel_modify" BN node's output shape
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
```

Now, we have optimized onnx model in variable "m", which input data is in range -128 to 127.
Here, we save the onnx model 'm' to disk at `/data1/yolo.opt.onnx` for further verification (like Netron or onnxruntime) in step 4.

```python
onnx.save(m, 'yolo.opt.onnx')
```

## Step 3: IP Evaluation

To make sure the onnx model is as expected, we should check the onnx model's performance and see if there are any unsupprted operators (or CPU nodes).

```python
# npu (only) performance simulation
km = ktc.ModelConfig(32768, "0001", "530", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))
```

The estimated FPS (NPU only) report on your terminal should look similar to this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```
Npu performance evaluation result:
=========================
===== Configuration =====
=========================
Frequency = 500 Mhz
Bit width = 8
MAC# = 512
Batch size = 1
4 bit mode is off
RDMA_bandwidth_GBPs = 8 GB/s
WDMA_bandwidth_GBPs = 8 GB/s
GETW_bandwidth_GBPs = 8 GB/s
Effective model compression rate = 1

=========================
===== Output result =====
=========================
output_fps = 64.9343
output_total_cycle = 7.7001e+06
output_total_time = 15.4002 ms

output_total_time_no_Sync = 15.6146 ms

===== Data move =====
output_total_data_move_time = 0.723726 ms
output_total_data_move_amount = 0.00578981 GB
output_avg_data_bw = 0.375957 GB/s

===== Weight loading =====
output_total_weight_size = 9837.86 KB
output_avg_weight_bw = 0.638814 GB/s

===== Dram =====
output_avg_dram_bw = 1.01477 GB/s
```

</div>



## Step 4: Check ONNX model and preprocess and postprocess are good

If we can get correct detection result from the ONNX and provided preprocess and postprocess functions, everything should be correct.

First, we need to check the preprocess and postprocess methods. [Here](<https://github.com/qqwweee/keras-yolo3/blob/master/yolo.py>) is the relevant code.

The following is the extracted preprocess:

```python
from yolo3.utils import letterbox_image

def preprocess(pil_img):
    model_input_size = (416, 416)  # to match our model input size when converting
    boxed_image = letterbox_image(pil_img, model_input_size)
    np_data = np.array(boxed_image, dtype='float32')

    np_data /= 255.
    return np_data
```

But we need to modify this preprocess function due to the In-Model-Preprocess trick in previous step.

```python
from yolo3.utils import letterbox_image

def preprocess(pil_img):
    model_input_size = (416, 416)  # to match our model input size when converting
    boxed_image = letterbox_image(pil_img, model_input_size)
    np_data = np.array(boxed_image, dtype='float32')

    # change normalization method due to we add "pixel_modify" BN node at model's front
    #np_data /= 255.
    np_data -= 128

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

Now, we can check the ONNX inference result with api `ktc.kneron_inference`.

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
(array([[258.89148, 470.26517, 297.0268 , 524.3218 ],
       [233.60538, 218.1825 , 306.83316, 381.80402]], dtype=float32), array([0.9251515, 0.7872135], dtype=float32), array([2, 7], dtype=int32))
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
2. You need to provide the radix value, which can be obtained by `ktc.get_radix` with input images as the parameter.
3. If the platform is not 530, you need to modify parameter: `platform`, e.g. `platform=720`.

```python
## bie model check
input_image = Image.open('/data1/000000350003.jpg')

# resize and normalize input data
in_data = preprocess(input_image)

# check nef radix from quantization data
radix = ktc.get_radix(img_list)

# bie inference
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"], radix=radix, platform=530)

# bie output data processing
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)
```

The result will be displayed on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```bash
(array([[260.75397, 471.40704, 295.34024, 522.4468 ],
       [233.62381, 216.45245, 308.01544, 393.66284]], dtype=float32), array([0.87260216, 0.6417989 ], dtype=float32), array([2, 7], dtype=int32))
```

</div>

This is slightly different from the result in Step 3: we lost one bounding box after quantization. Note that this loss is acceptable after quantization.


## Step 7: Compile

The final step is compile the BIE model into an NEF model.

```python
# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")
```

You can find the NEF file under `/data1/batch_compile/models_530.nef`. `models_530.nef` is the final compiled model.


## (optional) Step 8. Check NEF model

Toolchain api `ktc.inference` does support NEF model inference. The usage of `ktc.kneron_inference` is similar to the steps in Step 4 and Step 6, with minor differences.

1. The 2nd parameter is changed from to nef_model.
2. You need to provide the radix value, which can be obtained by `ktc.get_radix` with input images as the parameter.
3. If the platform is not 530, you need to provide an extra parameter: `platform`, e.g. `platform=720`.

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

The result will be displayed on your terminal like this:

<div style="background-color: rgb(80, 80, 80); font-size: 11px; font-style: italic;" >

```bash
(array([[260.75397, 471.40704, 295.34024, 522.4468 ],
       [233.62381, 216.45245, 308.01544, 393.66284]], dtype=float32), array([0.87260216, 0.6417989 ], dtype=float32), array([2, 7], dtype=int32))
```

</div>

> Note: the NEF model results should be exactly the same as the BIE model results.



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

    # change normalization method due to we add "pixel_modify" BN node at model's front
    #np_data /= 255.
    np_data -= 128

    # Insert batch dimension and transpose to match model's input.
    np_data = np.expand_dims(np_data, 0)
    np_data = np.transpose(np_data, (0, 3, 1, 2))
    return np_data


# convert h5 model to onnx
m = ktc.onnx_optimizer.keras2onnx_flow("/data1/yolo.h5", input_shape = [1,416,416,3])
m = ktc.onnx_optimizer.onnx2onnx_flow(m)

# add pixel modify node:
#   1. scaling 1/255 for every channel due to original normalize method,
#   2. shift 0.5 to change input range from 0~255 to -128 to 127
ktc.onnx_optimizer.pixel_modify(m,[1/255,1/255,1/255],[0.5,0.5,0.5])

# do onnx2onnx again to calculate "pixel_modify" BN node's output shape
m = ktc.onnx_optimizer.onnx2onnx_flow(m)

onnx.save(m,'yolo.opt.onnx')


# setup ktc config
km = ktc.ModelConfig(32769, "0001", "530", onnx_model=m)

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
radix = ktc.get_radix(img_list)
out_data = ktc.kneron_inference([in_data], bie_file=bie_model_path, input_names=["input_1_o0"], radix=radix, platform=530)
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)


# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")

# nef model check
input_image = Image.open('/data1/000000350003.jpg')
in_data = preprocess(input_image)
radix = ktc.get_radix(img_list)
out_data = ktc.kneron_inference([in_data], nef_file=nef_model_path, radix=radix, platform=530)
det_res = postprocess(out_data, [input_image.size[1], input_image.size[0]])
print(det_res)
```
