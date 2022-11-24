# ONNX Converter

ONNX_Convertor is an open-source project on [Github](https://github.com/kneron/ONNX_Convertor). If there is any bugs in
the ONNX_Convertor project inside the docker, don't hesitate to try `git pull` under the project folder to get the
latest update. And if the problem persists, you can raise an issue there. We also welcome contributions to the project.

The general process for model conversion is as following:

1. Convert the model from other platforms to onnx using the specific converters. See section 1 - 5.
2. Optimize the onnx for Kneron toolchain using `onnx2onnx.py`. See [section 6](#6-onnx-to-onnx-onnx-optimization).
3. Check the model and do further customization using `editor.py` (optional). See [section 7](#7-model-editor)

> TIPS:
>
> ONNX exported by Pytorch **cannot** skip step 1 and directly go into step 2. Please check
> [section 2](#2-pytorch-to-onnx) for details.

**If you're still confused reading the manual, please try our examples from <https://github.com/kneron/ConvertorExamples>**

Table 1.2 shows supported operators conversion mapping table for every platform.

*Table 1.2 Operators conversion table for every platform*

| type                   | keras                   | caffe                | tflite                                    | onnx(Opset 11)              |
|------------------------|-------------------------|----------------------|-------------------------------------------|-----------------------------|
| add                    | Add                     | Eltwise              | ADD                                       | Add                         |
| average pooling        | AveragePooling2D        | Pooling              | AVERAGE_POOL_2D                           | AveragePool                 |
| batchnormalization     | BatchNormalization      | BatchNorm            |                                           | BatchNormalization          |
| concatenate            | Concatenate             | Concat               | CONCATENATION                             | Concat                      |
| convolution            | Conv2D                  | Convolution          | CONV_2D                                   | Conv                        |
| crop                   | Cropping2D / Cropping1D |                      |                                           | Slice                       |
| deconvolution          | Conv2DTranspose         | Deconvolution        | TRANSPOSE_CONV                            | ConvTranspose               |
| dense                  | Dense                   | InnerProduct         | FULLY_CONNECTED                           | Gemm                        |
| depthwise convolution  | DepthwiseConv2D         | DepthwiseConvolution | DEPTHWISE_CONV_2D                         | Conv (with group attribute) |
| flatten                | Flatten                 | Flatten              |                                           | Flatten                     |
| global average pooling | GlobalAveragePooling2D  | Pooling              | MEAN                                      | GlobalAveragePool           |
| global max pooling     | GlobalMaxPooling2D      | Pooling              |                                           | GlobalMaxPool               |
| leaky relu             | LeakyReLU               |                      | LEAKY_RELU                                | LeakyRelu                   |
| max pooling            | MaxPooling2D            | Pooling              | MAX_POOL_2D                               | MaxPool                     |
| multiply               | Multiply                | Eltwise              | MUL                                       | Mul                         |
| padding                | ZeroPadding2D           |                      | PAD                                       | Pad                         |
| prelu                  | PReLU                   | PReLU                | PRELU                                     | Prelu                       |
| relu                   | ReLU                    | ReLU                 | RELU                                      | Relu                        |
| relu6                  | ReLU                    |                      | RELU6                                     | Clip                        |
| separable conv2d       | SeparableConv2D         |                      |                                           | Conv                        |
| sigmoid                | Sigmoid                 | Sigmoid              | LOGISTIC                                  | Sigmoid                     |
| squeeze                |                         |                      | SQUEEZE                                   | Squeeze                     |
| tanh                   | Tanh                    |                      |                                           | Tanh                        |
| resize                 | UpSampling2D            |                      | RESIZE_BILINEAR / RESIZE_NEAREST_NEIGHBOR | Resize                      |
| roi pooling            |                         | ROIPooling           |                                           | MaxRoiPool                  |
 
1.  our tensorflow conversion tool is based on opensource "tf2onnx", please check "https://github.com/onnx/tensorflow-onnx/blob/r1.6/support_status.md" for the supported op information  
2. our pytorch conversion tool is based on onnx exporting api in torch.onnx, please check "https://pytorch.org/docs/stable/onnx.html#supported-operators" for the supported op information  
3. some operators could be replaced by onnx2onnx.py in order to fit the KL520/KL720 spec.   



## 1 Keras to ONNX

For Keras, our converter support models from Keras 2.2.4. **Note that `tf.keras` and Keras 2.3 is not supported.** You may
need to export the model as tflite model and see [section 5](#5-tf-lite-to-onnx) for TF Lite model conversion.

Suppose there is an hdf5 model exported By Keras, you need to convert it to onnx by the following command:

```bash
python /workspace/libs/ONNX_Convertor/keras-onnx/generate_onnx.py -o absolute_path_of_output_model_file -O --duplicate-shared-weights absolute_path_of_input_model_file 
```

For example, if the model is `/docker_mount/onet.hdf5`, and you want to convert it to `/docker_mount/onet.onnx`, the
detailed command is:

```bash
python /workspace/libs/ONNX_Convertor/keras-onnx/generate_onnx.py -o /docker_mount/onet.onnx  -O --duplicate-shared-weights /docker_mount/onet.hdf5
```

There might be some warning log printed out by the TensorFlow backend, but we can ignore it since we do not actually run
it. You can check whether the conversion succeed by checking whether the onnx file is generated.

You need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization) after this step.

*__Input shape change__(optional)*

If there’s customized input shape for the model file, you need to use `-I` flag in the command. Here is an example:

```bash
python /workspace/libs/ONNX_Convertor/keras-onnx/generate_onnx.py abs_path_of_input_model -o abs_path_of_output_model -I 1 model_input_width model_input_height num_of_channel -O --duplicate-shared-weights
```

*__Add RGBN to YYNN layer for Keras model__(optional)*

Some of the models might take gray scale images instead of RGB images as the input. Here is a small script to add an
extra layer to let the model take RGB input.

```bash
cd /workspace/libs/ONNX_Convertor/keras-onnx && python rgba2yynn.py input_hdf5_file output_hdf5_file
```

## 2 Pytorch to ONNX

The `pytorch2onnx.py` script not only takes `pth` file as the input. It also takes Pytorch exported `onnx` as the input.
In fact, we recommend using the Pytorch exported `onnx` file instead of the `pth` file, since the Pytorch do not has a
very good model save and load API. You can check TIPS below on how to export models to onnx.

We currently only support models exported by Pytorch version >=1.0.0, <=1.7.1, no matter it is a `pth` file or an `onnx`
file exported by `torch.onnx`. The PyTorch version in the toolchain docker is 1.7.1.

> TIPS
>
> You can use `torch.onnx` to export your model into onnx format. Here is the
> [Pytorch 1.7.1 version document](https://pytorch.org/docs/1.7.1/onnx.html) for `onnx.torch`. An example code for
> exporting the model is:

```python
import torch.onnx
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, 'output.onnx', opset_version=11)
```

> In the example, `(1, 3, 224, 224)` are batch size, input channel, input height and input width. `model` is the model
> object you want to export. `output.onnx` is the output file.

*__Run pytorch2onnx with pth file__*

Suppose the input file is called `/docker_mount/resnet34.pth` and you want to save the onnx as
`/docker_mount/resnet34.onnx`. The input channel, height, width for the model are (3, 224, 224). Here is the example
command:

```bash
python /workspace/libs/ONNX_Convertor/optimizer_scripts/pytorch2onnx.py /docker_mount/resnet34.pth /docker_mount/resnet34.onnx --input-size 3 224 224 
```

You need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization) after this step.

*__Run pytorch_exported_onnx_preprocess with onnx file__*

Suppose the input file is called `/docker_mount/resnet34.onnx` and you want to save the optimized onnx as
`/docker_mount/resnet34.opt.onnx`. Here is the example
command:

```bash
python /workspace/libs/ONNX_Convertor/optimizer_scripts/pytorch_exported_onnx_preprocess.py /docker_mount/resnet34.onnx /docker_mount/resnet34.opt.onnx
```

You need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization) after this step.

*__Crash due to name conflict__*

If you meet the errors related to `node not found` or `invalid input`, this might be caused by a bug in the onnx
library. Please try using `--no-bn-fusion` flag.


## 3 Caffe to ONNX

For caffe, we only support model which can be loaded by [Intel Caffe 1.0](https://github.com/intel/caffe).

Suppose you have model structure definition file `/docker_mount/mobilenetv2.prototxt` and model weight file
`/docker_mount/mobilenetv2.caffemodel` and you want to output the result as `/docker_mount/mobilenetv2.onnx`, Here is
the example command:

```bash
python /workspace/libs/ONNX_Convertor/caffe-onnx/generate_onnx.py -o /docker_mount/mobilenetv2.onnx -w /docker_mount/mobilenetv2.caffemodel -n /docker_mount/mobilenetv2.prototxt
```

You need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization) after this step.

## 4 Tensorflow to ONNX

Tensorflow to onnx script only support Tensorflow 1.x and the operator support is very limited. If it cannot work on
your model, please try to export the model as tflite and convert it using [section 5](#5-tf-lite-to-onnx).

Suppose you want to convert the model `/docker_mount/mnist.pb` to `/docker_mount/mnist.onnx`, here is the example
command:

```bash
python /workspace/libs/ONNX_Convertor/optimizer_scripts/tensorflow2onnx.py /docker_mount/mnist.pb /docker_mount/mnist.onnx
```

You need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization) after this step.

## 5 TF Lite to ONNX

```bash
python /workspace/libs/ONNX_Convertor/tflite-onnx/onnx_tflite/tflite2onnx.py -tflite path_of_input_tflite_model -save_path path_of_output_onnx_file -release_mode True
```

For the provided example model: `model_unquant.tflite`

```bash
python /workspace/libs/ONNX_Convertor/tflite-onnx/onnx_tflite/tflite2onnx.py -tflite /data1/tflite/model/model_unquant.tflite -save_path /data1/tflite/model/model_unquant.tflite.onnx -release_mode True
```

Then need to run the command in [section 6](#6-onnx-to-onnx-onnx-optimization).

*__TF Lite quant models:__*

If the tflite model provided is a quantized model, use the same command above to convert it into onnx. A user_config.json will be generated in the same path as -save_path provided. This file could be moved to the model input folder as one of the knerex input to do better quantization.

## 6 ONNX to ONNX (ONNX optimization)

After converting models from other frameworks to onnx format, you need to run the following command to optimize the 
model for Kneron hardware, suppose your model is `input.onnx` and the output model is called `output.onnx`:

```bash
python /workspace/libs/ONNX_Convertor/optimizer_scripts/onnx2onnx.py input.onnx -o output.onnx --add-bn -t
```

*__Crash due to name conflict__*

If you meet the errors related to `node not found` or `invalid input`, this might be caused by a bug in the onnx
library. Please try using `--no-bn-fusion` flag.

*__MatMul optimization for kneron hardware__*

If your model has MatMul nodes with inputs of 3D instead of 2D and you want to deploy your model using Kneron hardware,
please use `--opt-matmul` flag to optimize the model. This flag allows the optimizer to split the input due to current
hardware input without affecting the correctness of calculation.

## 7 Model Editor

KL720 NPU supports most of the compute extensive OPs, such as Conv, BatchNormalization, Fully Connect/GEMM, in order to
speed up the model inference run time. On the other hand, there are some OPs that KL720 NPU cannot support well, such as
`Softmax` or `Sigmod`. However, these OPs usually are not compute extensive and they are better to execute in CPU.
Therefore, Kneron provides a model editor which is `editor.py` to help user modify the model so that KL720 NPU can run
the model more efficiently.

*__General Editor Guideline__*

Here are some general guideline to edit a model to take full advantage of KL720 NPU MAC efficiency:

**Step 1:** Start from each output node of the model, we should trace back to an operator that has significant compute
workload, such as `GlobalAveragePool`, `Gemm`(fully connect), or `Conv`. Then, we could cut to the output of that OP.
For example, there is a model looks Figure 4, and it has two output nodes: `350` and `349`. From output node `349`, we
can trace back to the `Gemm` above the red line because the `Div`, `Clip`, `Add` and `Mul` only have 1x5 dimension, and
these OPs are not very heavy computation. Since `Mul` and `Div` are not support in NPU, so it is recommend to cut the
rest of the OPs and let the model finish at the output of the `Gemm` (red line). For the other output node `350`, since
it is the output of a `Gemm`, there is no need to do any more edition.

**Step 2:** If both input nodes and output nodes are channel last, and there is a `Transpose` after the input and before
the output, then the model is transposed into channel first. We can use the model editor to safely remove the
`Transpose`.

**Step 3:** If the input shape is not availble or invalid, we can usethe editor to give it a valid shape.

**Step 4:** The model need to pass `onnx2onnx.py` again after running the editor.  See
[section 6](#6-onnx-to-onnx-onnx-optimization).

<div align="center">
<img src="../../imgs/manual/fig4_pre_edited_model.png">
<p><span style="font-weight: bold;">Figure 4.</span> Pre-edited model </p>
</div>

_**Feature**_
The script called `editor.py` is under the folder `/workspace/libs/ONNX_Convertor/optimizer_scripts`. It is a simple
ONNX editor which achieves the following functions:

1. Add nop `BN` or `Conv` nodes.
2. Delete specific nodes or inputs.
3. Cut the graph from certain node (Delete all the nodes following the node).
4. Reshape inputs and outputs
5. Rename the output.

*__Usage__*

```
editor.py [-h] [-c CUT_NODE [CUT_NODE ...]]
             [--cut-type CUT_TYPE [CUT_TYPE ...]]
             [-d DELETE_NODE [DELETE_NODE ...]]
             [--delete-input DELETE_INPUT [DELETE_INPUT ...]]
             [-i INPUT_CHANGE [INPUT_CHANGE ...]]
             [-o OUTPUT_CHANGE [OUTPUT_CHANGE ...]]
             [--add-conv ADD_CONV [ADD_CONV ...]]
             [--add-bn ADD_BN [ADD_BN ...]]
             in_file out_file

Edit an ONNX model. The processing sequense is 'delete nodes/values' -> 'add nodes' -> 'change shapes' -> 'cut node'.
Cutting is not recommended to be done with other operations together.

positional arguments:

in_file   input ONNX FILE
out_file  ouput ONNX FILE

optional arguments:

        -h, --help            show this help message and exit
        -c CUT_NODE [CUT_NODE ...], --cut CUT_NODE [CUT_NODE ...]
        remove nodes from the given nodes(inclusive)

        --cut-type CUT_TYPE [CUT_TYPE ...]
        remove nodes by type from the given nodes(inclusive)

        -d DELETE_NODE [DELETE_NODE ...], --delete DELETE_NODE [DELETE_NODE ...]
        delete nodes by names and only those nodes

        --delete-input DELETE_INPUT [DELETE_INPUT ...]
        delete inputs by names

        -i INPUT_CHANGE [INPUT_CHANGE ...], --input INPUT_CHANGE [INPUT_CHANGE ...]
        change input shape (e.g. -i 'input_0 1 3 224 224')

        -o OUTPUT_CHANGE [OUTPUT_CHANGE ...], --output OUTPUT_CHANGE [OUTPUT_CHANGE ...]
        change output shape (e.g. -o 'input_0 1 3 224 224')

        --add-conv ADD_CONV [ADD_CONV ...]
        add nop conv using specific input

        --add-bn ADD_BN [ADD_BN ...]
        add nop bn using specific input
```

## 8 ONNX Updater

For existed onnx models with the previous version of the opset, we provide the following scripts to update your model.
Note that after running any of the following scripts, you may still need to run `onnx2onnx.py`.

```bash
# For ONNX 1.3 to 1.4 (opset 7/8 to opset 9):
python /workspace/libs/ONNX_Convertor/optimizer_scripts/onnx1_3to1_4.py input.onnx output.onnx

# For ONNX 1.4 to 1.6 (opset 9 to opset 11):
python /workspace/libs/ONNX_Convertor/optimizer_scripts/onnx1_4to1_6.py input.onnx output.onnx
```
