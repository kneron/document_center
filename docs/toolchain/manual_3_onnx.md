# 3. Floating-Point Model Preparation

Our toolchain utilities take ONNX files as inputs. The ONNX workflow is mainly about convert models from other platforms to ONNX and prepare the onnx for the quantization and compilation. There are three main steps: conversion, evaluation and testing.

## 3.1. Model Conversion and Optimization

The onnx converter part currently support Keras, TFLite, a subset of Tensorflow, Caffe and Pytorch. Here, we will only briefly introduce some common usage of the python API. This part of python API is based on our converter and optimizer open-source project which can be found on Github <https://github.com/kneron/ONNX_Convertor>. We have both Python API and script usage. In this document, we only introduce the Python API. The detailed usage of those converter scripts usage can be found in [ONNX Converter](appendix/converters.md). The Tensorflow ktc api is not introduced here. We recommend export the tensorflow model to tflite and convert the tflite model. If you really want to try convert a pb file, please check the onnx converter project.

The example models used in the following converter command are not included in the docker by default. They can be found on Github <https://github.com/kneron/ConvertorExamples>. You can download them through these terminal commands:

```bash
git clone https://github.com/kneron/ConvertorExamples.git
cd ConvertorExamples && git lfs pull
```

### 3.1.1. Keras to ONNX

For Keras, our converter support models from Keras 2.2.4. **Note that `tf.keras` and Keras 2.3 is not supported.** You may
need to export the model as tflite model and see [section 3.1.4](#314-tf-lite-to-onnx) for TF Lite model conversion.

Here is the API:

```python
#[API]
ktc.onnx_optimizer.keras2onnx_flow(keras_model_path, optimize, input_shape)
```

Return the converted onnx object. Convert keras model to onnx object.

Args:

* keras_model_path (str): the input hdf5/h5 model path.
* optimize (int, optional): optimization level. Defaults to 0.
* input_shape (List, optional): change the input shape if set. Only single input model is supported. Defaults to None.

Suppose there is an onet hdf5 model exported By Keras, you need to convert it to onnx by the following python code:

```python
#[Note] You need to download the model first
result_m = ktc.onnx_optimizer.keras2onnx_flow('/data1/ConvertorExamples/keras_example/onet-0.417197.hdf5')
```

In this line of python code, `ktc.onnx_optimizer.keras2onnx_flow` is the function that takes an hdf5 file path and convert the hdf5 into an onnx object. The return value `result_m` is the converted onnx object. It need to take one more optimization step (section 3.1.5) before going into the next section.

There might be some warning log printed out by the Tensorflow backend, but we can ignore it since we do not actually run it. You can check whether the conversion succeed by whether there is any exception raised.


### 3.1.2. Pytorch to ONNX

Our Python API do not actually convert the python model. It only takes Pytorch exported onnx object as the input and optimize it. Pleace checkout the tips below on how to export an onnx with Pytorch.

The Pytorch inside the docker is version 1.7.1. We currently only support models exported by Pytorch version >=1.0.0, <=1.7.1. Other versions are not tested.

> TIPS on export onnx using `torch.onnx`:
>
> You can use `torch.onnx` to export your model into onnx object. Here is the [Pytorch to ONNX document](https://pytorch.org/docs/stable/onnx.html#example-alexnet-from-pytorch-to-onnx) for `onnx.torch`. An example code for exporting the model is:

```python
#[Note] Please modify input dimension according to your need.
import torch.onnx
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, 'output.onnx', opset_version=12)
```

> In the example, `(1, 3, 224, 224)` are batch size, input channel, input height and input width.
> `model` is the pytorch model object you want to export. `output.onnx` is the output onnx file path.


Pytorch exported onnx needs to pass through a special optimization designed for pytorch exported models first.

The following is the Python API:

```python
#[API]
ktc.onnx_optimizer.torch_exported_onnx_flow(m, disable_fuse_bn=False):
```

Return the optimized model. Optimize the Pytorch exported onnx. Note that onnx2onnx_flow is still needed after
running this optimizaiton.

Args:

* m (ModelProto): the input onnx model
* disable_fuse_bn (bool, optional): do not fuse BN into Conv. Defaults to False.

Suppose the input file is loaded into a onnx object `exported_m`, here is the python code for pytorch exported onnx optimization:

```python
#[API]
result_m = ktc.onnx_optimizer.torch_exported_onnx_flow(exported_m)
```

In this line of python code, `ktc.onnx_optimizer.torch_exported_onnx_flow` is the function that takes an onnx object and optimize it. The return value `result_m` is the optimized onnx object. It need to take one more general onnx optimization step (section 3.1.5) before going into the next section.

For the example in ConvertorExamples project, the whole process would be:

```python
#[Note] You need to download the model first
import torch
import torch.onnx

# Load the pth saved model
pth_model = torch.load("/data1/ConvertorExamples/pytorch_example/resnet34.pth", map_location='cpu')
# Export the model
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(pth_model, dummy_input, '/data1/resnet34.onnx', opset_version=11)
# Load the exported onnx model as an onnx object
exported_m = onnx.load('/data1/resnet34.onnx')
# Optimize the exported onnx object
result_m = ktc.onnx_optimizer.torch_exported_onnx_flow(exported_m)
```

There might be some warning log printed out by the Pytorch because our example model is a little old. But we can ignore it since we do not actually run it. You can check whether the conversion succeed by whether there is any exception raised.

*__Crash due to name conflict__*

If you meet the errors related to `node not found` or `invalid input`, this might be caused by a bug in the onnx library.
Please try set `disable_fuse_bn` to `True`. The code would be:

```python
#[API]
result_m = ktc.onnx_optimizer.torch_exported_onnx_flow(exported_m, disable_fuse_bn=True)
```


### 3.1.3. Caffe to ONNX

For caffe, we only support model which can be loaded by [Intel Caffe 1.0](https://github.com/intel/caffe).

The following is the Python API:

```python
#[API]
ktc.onnx_optimizer.caffe2onnx_flow(caffe_model_path, caffe_weight_path)
```

Return the converted onnx object. Convert caffe model to onnx object.

Args:

* caffe_model_path (str): the input model definition (.prototxt).
* caffe_weight_path (str): the input weight file (.caffemodel).

Here we will use the example from ConvertorExamples. You can find two files for the caffe model: the model structure definition file `mobilenetv2.prototxt` and the model weight file `mobilenetv2.caffemodel`. Here is the example python code for model conversion:

```python
#[Note] You need to download the model first
result_m = ktc.onnx_optimizer.caffe2onnx_flow('/data1/ConvertorExamples/caffe_example/mobilenetv2.prototxt', '/data1/ConvertorExamples/caffe_example/mobilenetv2.caffemodel')
```

In this line of python code, `ktc.onnx_optimizer.caffe2onnx_flow` is the function that takes caffe model file paths and convert the them into an onnx object. The return value `result_m` is the converted onnx object. It need to take one more optimization step (section 3.1.5) before going into the next section.


### 3.1.4. TF Lite to ONNX

We only support unquantized TF Lite models for now. Also tensorflow 2 is not supported yet. If our converter cannot process your model correctly, please use the open-source [tf2onnx](https://github.com/onnx/tensorflow-onnx). And use `torch_exported_onnx_flow` API for optimization after that.

The following is our TFLite to ONNX API:

```python
#[API]
ktc.onnx_optimizer.tflite2onnx_flow(tflite_path, release_mode, bottom_nodes)
```

Return the converted onnx object. Convert tflite model to onnx object.

Args:

* tflite_path (str): the input tflite model path.
* release_mode (bool, optional): whether eliminate the transpose for channel first. Defaults to True.
* bottom_nodes (List, optional): nodes name in tflite model which is the bottom node of sub-graph. Defaults to [].

Suppose we are using the tflite file `model_unquant.tflite` from the ConvertorExamples, here is the example python code:

```python
#[Note] You need to download the model first
result_m = ktc.onnx_optimizer.tflite2onnx_flow('/data1/ConvertorExamples/tflite_example/model_unquant.tflite')
```

In this line of python code, `ktc.onnx_optimizer.tflite2onnx_flow` is the function that takes an tflite file path and convert the tflite into an onnx object. The return value `result_m` is the converted onnx object. It need to take one more optimization step (section 3.1.5) before going into the next section.

There might be some warning log printed out by the Tensorflow backend, but we can ignore it since we do not actually run it. You can check whether the conversion succeed by whether there is any exception raised.

This function has more parameters for fine-tuning. Please check [Toolchain Python API](http://doc.kneron.com/docs/toolchain/python_api/) if needed.


### 3.1.5. ONNX Optimization

We provide a general onnx optimize API. We strongly recommend that all the onnx, including the onnx generated from the previous subsections, shall pass this API before going into the next section. This general onnx optimization API would modify the onnx graph to fit the toolchain and Kneron hardware specification. The optimization includes: inference internal value_info shapes, fuse consecutive operators, eliminate do-nothing operators, replace high-cost operators with low-cost operators, etc..

Here is the detailed ONNX optimization API:

```python
#[API]
ktc.onnx_optimizer.onnx2onnx_flow(m, disable_fuse_bn=False, bgr=False, norm=False, rgba2yynn=False, eliminate_tail=False, opt_matmul=False, opt_720=False, duplicate_shared_weights=True)
```

Return the optimized model. Optimize the onnx model.

Args:

* m (ModelProto): the input onnx ModelProto
* disable_fuse_bn (bool, optional): do not fuse BN into Conv. Defaults to False.
* bgr (bool, optional): add an Conv layer to convert rgb input to bgr. Defaults to False.
* norm (bool, optional): add an Conv layer to add 0.5 tp the input. Defaults to False.
* rgba2yynn (bool, optional): add an Conv layer to convert rgb input to yynn . Defaults to False.
* eliminate_tail (bool, optional): remove the trailing NPU unsupported nodes. Defaults to False.
* opt_matmul (bool, optional): optimize the MatMul layers according to the NPU limit. Defaults to False.
* opt_720 (bool, optional): optimize the model for the kneron hardware kdp720. Defaults to False.
* duplicate_shared_weights(bool, optional): duplicate shared weights. Defaults to False.

Suppose we have a onnx object, here is the example python code:

```python
optimized_m = ktc.onnx_optimizer.onnx2onnx_flow(result_m, eliminate_tail=True, opt_matmul=False)
```

In this line of python code, `ktc.onnx_optimizer.onnx2onnx_flow` is the function that takes an onnx object and optimize it. The return value `result_m` is the converted onnx object.

**Note** that for hardware usage, `eliminate_tail` should be set to true as in the example. This option eliminate the no calculation operators and the npu unsupported operators (Reshape, Transpose, ...) at the last of the graph. However, since this changes the graph structure, you may need to check the model yourself and add the related functions into post-process to keep the algorithm consistent. If you only want to use onnx model for software testing, the `eliminate_tail` can be set to false to keep the model same as the input from the mathematics perspective. `opt_matmul` is also for hardware usage which optimize the MatMul nodes according to the NPU limit. By default, it is set to False. You only need to enable this flag if there are MatMul nodes with inputs more than 2D.

By the way, to save the model, you can use the following function from the onnx package.

```python
# Save the onnx object optimized_m to path /data1/optimized.onnx.
onnx.save(optimized_m, '/data1/optimized.onnx')
```

*__Crash due to name conflict__*

If you meet the errors related to `node not found` or `invalid input`, this might be caused by a bug in the onnx library.
Please try set `disable_fuse_bn` to `True`. The code would be:

```python
#[API]
optimized_m = ktc.onnx_optimizer.onnx2onnx_flow(result_m, eliminate_tail=True, disable_fuse_bn=True)
```

*__Error due to the opset version__*

If you have met errors which are related to the opset version or the ir version. Please check section 3.1.6 to update your model first.


### 3.1.6. ONNX Opset Upgrade

From toolchain version 0.14.0, ONNX in the docker has been updated from 1.4.1 to 1.6. And the default opset that converters support is changed from opset 9 into opset 11. IR version is updated from 4 to 6. Thus, if you have a onnx model with opset 9 or IR version 4, you may need to update it with the following Python API. Actually, the current ONNX version inside the docker is upgraded to 1.7.0. ONNX 1.7.0 do not have many changes compared to ONNX 1.6.*. Thus, the following API is still in use.

Here is the API:

```python
#[API]
ktc.onnx_optimizer.onnx1_4to1_6(model)
```

Return the updated onnx model. Update model ir_version from 4 to 6 and update opset from 9 to 11.

Args:

* model (onnx.ModelProto): input onnx model.

Here is an example usage.

```python
#[Note] old_m is the opset 9 onnx model object.
new_m = ktc.onnx_optimizer.onnx1_4to1_6(old_m)
```

In this line of python code, `ktc.onnx_optimizer.onnx1_4to1_6` is the function that takes an old version onnx object and upgrade it. The return value `new_m` is the converted onnx object. It need to take one more optimization step (section 3.1.5) before going into the next section. Even if you have already passed optimizar before, we still recommend you do it again after this upgrade.


### 3.1.7. ONNX Editor

KL520/KL720/KL530 NPU supports most of the compute extensive OPs, such as Conv, BatchNormalization, Fully Connect/GEMM, in order to speed up the model inference run time. On the other hand, there are some OPs that KL520 NPU cannot support well, such as `Softmax` or `Sigmod`. However, these OPs usually are not compute extensive and they are better to execute in CPU.
Therefore, Kneron provides python APIs which help user modify the model so that KL520 NPU can run the model more efficiently.

Following are the Python APIs we provide.

#### Delete specific nodes

```python
#[API]
ktc.onnx_optimizer.delete_nodes(model, node_names)
```

Return the result onnx model. Delete nodes with the given names.

Args:

* model (onnx.ModelProto): the input onnx model.
* node_names (List[str]): a list of node names.

#### Delete specific inputs

```python
#[API]
ktc.onnx_optimizer.delete_inputs(model, value_names)
```

Return the result onnx model. Delete specific inputs

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): inputs to delete.

#### Delete specific outputs

```python
#[API]
ktc.onnx_optimizer.delete_outputs(model, value_names)
```

Return the result onnx model. Delete specific outputs

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): outputs to delete.

#### Cut the graph from the given node.

```python
#[API]
ktc.onnx_optimizer.cut_graph_from_nodes(model, node_names)
```

Return the result onnx model. Cut the graph from the given node. The difference between this function and the
`delete_node` is that this function also delete all the following nodes after the specific nodes.

Args:

* model (onnx.ModelProto): the input onnx model.
* node_names (List[str]): a list of node names.

#### Cut the graph from the given operator type.

```python
#[API]
ktc.onnx_optimizer.remove_nodes_with_types(model, type_names)
```

Return the result onnx model. Cut the graph from the nodes with specific operation types. Similar behaviour to
`cut_graph_from_nodes`.

Args:

* model (onnx.ModelProto): the input onnx model.
* type_names (List[str]): operator types to cut from.

#### Change input/output shapes

```python
#[API]
ktc.onnx_optimizer.change_input_output_shapes(model, input_shape_mapping=None, output_shape_mapping=None)
```

Return the result onnx model. Change input shapes and output shapes.

Args:

* model (onnx.ModelProto): input onnx model.
* input_shape_mapping (Dict, optional): mapping from input names to the shapes to change. Defaults to None.
* output_shape_mapping (Dict, optional): mapping from output names to the shapes to change. Defaults to None.

#### Add do-nothing Conv nodes after specific values

```python
#[API]
ktc.onnx_optimizer.add_conv_after(model, value_names)
```

Return the result onnx model. Add a do-nothing Conv node after the specific value.

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): values after which we add Conv.

#### Add do-nothing BN nodes after specific values

```python
#[API]
ktc.onnx_optimizer.add_bn_after(model, value_names)
```

Return the result onnx model. Add a do-nothing BN node after the specific value.

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): values after which we add BN.

#### Rename an output

```python
#[API]
ktc.onnx_optimizer.rename_output(model, old_name, new_name)
```

Return the result onnx model. Rename the specific output

Args:

* model (onnx.ModelProto): input onnx model.
* old_name (str): old output name.
* new_name (str): new output name.

#### Input pixel shift

```python
#[API]
ktc.onnx_optimizer.pixel_modify(model, scale, bias)
```

Return the result onnx model. Add a special BN node to adjust the input range. Currently only support single input model.

Args:

* model (onnx.ModelProto): input onnx model.
* scale (List[float]): the scale of the BN node.
* bias (List[float]): the bias of the BN node


## 3.2. IP Evaluation

Before we start quantizing the model and try simulating the model, we need to test if the model can be taken by the toolchain structure and estimate the performance.
IP evaluator is such a tool which can estimate the performance of your model and check if there is any operator or structure not supported by our toolchain.

We need to create a `ktc.ModelConfig` object. The `ktc.ModelConfig` is the class which contains the basic needed information of a model. You can initilize it through the API below.

```python
#[API]
class ktc.ModelConfig(self, id, version, platform, onnx_model=None, onnx_path=None, bie_path=None)
```

Create an Kneron model config object. One of these three parameters is required: onnx_model, onnx_path, bie_path.

Args:

* id (int): model ID
* version (str): version number which should be a four digit hex, e.g. "0a2f"
* platform (str): hardware platform, should be one of "520", "720", "530", "630", "730"
* onnx_model (ModelProto, optional): loaded onnx model object. Defaults to None.
* onnx_path (str, optional): onnx file path. Defaults to None.
* bie_path (str, optional): bie file path. Defaults to None.
* radix_json_path (str, optional): radix json path. Defaults to None.
* compiler_config_path (str, optional): compiler config json path. Defaults to None.
* debug (bool, optional): keep the debug output files. Defaults to False.

Note that for `onnx_model`, `onnx_path` and `bie_path`, user should provide one of those three parameter and only one.
The bie file is the file generated by the kneron toolchain after quantization, which is introduced in the section 4.

`radix_json_path` is used to specify the radix configuration for batch compiling. Models with this json file may compile without
bie file path. This configuration currently is only for advanced users. Please leave it to `None`.

`compiler_config_path` is used to specify the configuration for batch compiling. This configuration currently is only for
advanced users. Please leave it to `None`.

For this example, we create the MobileNet V2 ModelConfig with the following python code:

```python
km = ktc.ModelConfig(32769, "8b28", "720", onnx_model=optimized_m)
```

`evaluate` is class function of the `ktc.ModelConfig`.

```python
#[API]
classmethod evaluate(output_dir: str = "/data1/kneron_flow")
```

Args:

* output_dir (str, optional): output directory. Defaults to "/data1/kneron_flow".
* datapath_bitwidth_mode: choose from "int8"/"int16"/"mix balance"/"mix light". ("int16" is not supported in kdp520. "mix balance" and "mix light" are combines of int8 and int16 mode. "mix balance" prefers int16 while "mix light" prefers int8.)
* weight_bitwidth_mode: choose from "int8"/"int16"/"int4"/"mix balance"/"mix light". ("int16" is not supported in kdp520. "int4" is not supported in kdp720. "mix balance" and "mix light" are combines of int8 and int16 mode. "mix balance" prefers int16 while "mix light" prefers int8.)
* model_in_bitwidth_mode: choose from "int8"/"int16". ("int16" is not supported in kdp520.)
* model_out_bitwidth_mode: choose from "int8"/"int16". ("int16" is not supported in kdp520.)
* cpu_node_bitwidth_mode: choose from "int8"/"int16". ("int16" is not supported in kdp520.)

Return the evaluation result as `str`. The IP evaluator gives an estimation of the model running performance. It can run
with either onnx or bie. Below is an example usage.

```python
eval_result = km.evaluate()
```

The evaluation result will be returned as string. User can also find the evaluation result under `output_dir`.
The report is in html format: `model_fx_report.html`. You can check the report in command line with:

```bash
w3m model_fx_report.html
```

If the model is not supported, there would be warning messages or exceptions. Please modify the model structure referring to the message.
Please check the report to see if the performance meets your expectation. Please consider redesign the network structure. Also note that the evaluator report only considers the performance of NPU. Thus, if the model contains many operators that are not supported by NPU but by CPU, the actual performance would be even worse.

> TIPS:
> You can find the profiling configuration under `/workspace/scripts/res`. The configuration files are named like `ip_config_<platform>.json`. You can change the
> bandwidth according to your scenario .

## 3.3. E2E Simulator Check (Floating Point)

Before going into the next section of quantization, we need to ensure the optimized onnx file can produce the same result as the originally designed model.

Here we introduce the E2E simulator which is the abbreviation for end to end simulator. It can inference a model and simulate the calculation of the hardware.
The inference function of the E2E simulator is called `ktc.kneron_inference`.
Here we are using the onnx as the input model. But it also can take bie file and nef file which would be introduced later.

The python code would be like:

```python
inf_results = ktc.kneron_inference(input_data, onnx_file="/workspace/examples/mobilenetv2/mobilenetv2_zeroq.origin.onnx", input_names=["images"])
```

In the code above, `inf_results` is a list of result data. `onnx_file` is the path to the input onnx. `input_data` is a list of input data after preprocess. It should be the same shape as in the onnx. The `input_names` is a list of string mapping the input data to specific input on the graph using the sequence. **Note that the input should have the same shape as in the onnx (usually NCHW for image inputs).**

Here we provide a very simple preprocess function which only do the resize and normalization. Then, the full code of this section would be:

```python
from PIL import Image
import numpy as np

def preprocess(input_file):
    image = Image.open(input_file)
    image = image.convert("RGB")
    img_data = np.array(image.resize((224, 224), Image.BILINEAR)) / 255
    img_data = np.transpose(img_data, (2, 0, 1))
    img_data = np.expand_dims(img_data, 0)
    return img_data

input_data = [preprocess("/workspace/examples/mobilenetv2/images/000007.jpg")]
inf_results = ktc.kneron_inference(input_data, onnx_file="/workspace/examples/mobilenetv2/mobilenetv2_zeroq.origin.onnx", input_names=["images"])
```

Since we want to focus on the toolchain usage here, we do not provide any postprocess. In reality, you may want to have your own postprocess function in Python, too.

After getting the `inf_results` and post-process it, you may want to compare the result with the one generated by the source model.
For example, if the source model is from pytorch, you may want to try inference the source model using Pytorch with the same input image to see if the results match. If the result mismatch, please check FAQ 1 for possible solution.

Since we do not actually has any source model here for the simplicity of example, we would skip the step of comparing result.

## 3.4. FAQ

### 3.4.1. What if the E2E simulator results from the original model and the optimized onnx mismatch?

Please double check if the final layers are cut due to unsupported by NPU.
If so, please add the deleted operator as part of the E2E simulater post process and test again.
Otherwise, please search on forum <https://www.kneron.com/forum/categories/ai-model-migration>. You can also contact us through the forum if no match issue found. The technical support would reply directly to your post.

### 3.4.2 What if I get "RuntimeError: Inferred shape and existing shape differ in rank: (0) vs (3)'?

**Causes**:

Inside the converter, we are using `onnx.shape_inference.infer_shapes` from the official onnx repository to do the shape inference. It inferences the shapes of the nodes' input and output one by one. If any existing shape written in the graph is different from the already existed shape, this error is raise. Thus, there might be two main reasons for this error:

1. The input shape and the output shape of this model is invalid.
2. The onnx shape inferencer cannot inference the shape correctly.

**Solution**:

1. Please double check the model see if there is any wrong input/output shape.
2. Check if there is any large blocks of Reshape or Transpose. Those blocks are not friendly for the shape inferencer. Please consider replace those structures.

### 3.4.3 How to convert previous channel last input into channel first?

We provide a simple Python API to help you convert the input data from channel last to channel first. The API is called `ktc.convert_channel_last_to_first(image)`.
The input parameter `image` is a numpy array with shape (H, W, C) or (N, H, W, C), where N is the batch size, C is the channel size, H and W represent height and width.
The return value is also a numpy array with shape (N, C, H, W).

**Note this API is only for 2D image input.**

For example:

```python
import ktc
from PIL import Image
import numpy as np

image = Image.open("/workspace/examples/mobilenetv2/images/000007.jpg")
image = image.convert("RGB")
# Here the image is in channel last format, which is (224, 224, 3)
img_data = np.array(image.resize((224, 224), Image.BILINEAR)) / 255
ASSERT img_data.shape == (224, 224, 3)

# Now we use the API to convert the image into channel first format, which is (1, 3, 224, 224)
new_img_data = ktc.convert_channel_last_to_first(img_data)
ASSERT new_img_data.shape == (1, 3, 224, 224)
```
