# 3. Floating-Point Model Preparation

Our toolchain utilities take ONNX files as inputs. The ONNX workflow is mainly about convert models from other platforms to ONNX and prepare the onnx for the quantization and compilation. There are three main steps: conversion, evaluation and testing.

## 3.1. Model Conversion and Optimization

The conversion tools are different for different onnx versions. The environment is managed by miniconda. Current default environment is `onnx1.13`. It supports ONNX opset up to 18.

There is also a `base` environment which is the default environment for the toolchain before v0.25.0. This `base` environment supports opset 8 to 12. It is not recommended to use this environment for new models. But if you have a model using those opsets, you can still use this environment. The following documents are all based on the `onnx1.13` environment. If you are using the `base` environment, please check the [ONNX Converters](appendix/converters.md) for the API usage.

### 3.1.1. Convert models to ONNX

We do not provide model conversion tools from other frameworks to ONNX in the `onnx1.13` environment due to the huge efforts needed to keep up with the updates of various frameworks. Instead, we highly recommend you to use the official conversion tools from the framework you are using or other mature open source tools. For example, if you are using Pytorch, you can use the `torch.onnx.export` API to convert your model to ONNX. If you are using Tensorflow, you can use the `tf2onnx` tool to convert your model to ONNX.

### 3.1.2. ONNX Optimization

We provide a general ONNX optimize API. We strongly recommend that all ONNX models, including the onnx generated from other conversion tools, should pass this API before going into the next section. This general onnx optimization API would modify the onnx graph to fit the toolchain and Kneron hardware specification. The optimization includes: inferencing internal value_info shapes, fusing consecutive operators, eliminating do-nothing operators, replacing high-cost operators with low-cost operators, etc..

> This ONNX optimizer is for the default `onnx1.13` environment. If you are using the `base` environment, please check [ONNX Converter](appendix/converters.md).

Here is the detailed ONNX optimization API:

```python
#[API]
kneronnxopt.optimize(
    model,
    duplicate_shared_weights=1,
    skip_check=False,
    overwrite_input_shapes=None,
    skipped_optimizers=None,
    skip_fuse_qkv=False,
    clear_descriptions=False,
    opt_matmul=False,
):
```

Return the optimized model. Optimize the onnx model.

Args:

* model (ModelProto): the input onnx ModelProto
* duplicate_shared_weights (int, optional): by what level, duplicate shared weight. 0-no duplication, 1-duplicate shared weights only when kneron compiler not support, 2-duplicate shared weights always. Default is 1.
* skip_check (bool): skip the final check or not.
* overwrite_input_shapes (List\[str\]): overwrite the input shape. The format is "input_name:dim0,dim1,...,dimN" or simply "dim0,dim1,...,dimN" when there is only one input, for example, "data:1,3,224,224" or "1,3,224,224". Note: you might want to use some visualization tools like netron to make sure what the input name and dimension ordering (NCHW or NHWC) is.
* skipped_optimizers (list): skip the onnx optimizers. Check onnx document for details. Default is None.
* skip_fuse_qkv (bool): skip the fuse_qkv optimization or not. By default, fuse_qkv is enabled.
* clear_descriptions (bool): clear all descriptions in the graph. By default, descriptions are not cleared.
* opt_matmul (bool): optimize matmul operators for specific kneron compiler. By default, this option is not set.

Suppose we have a onnx object, here is the example python code:

```python
import kneronnxopt
optimized_m = kneronnxopt.optimize(input_m, skip_fuse_qkv=True)
```

In this line of python code, `kneronnxopt.optimize` is the function that takes an onnx object and optimize it. The return value `result_m` is the converted onnx object.

The previous `onnx2onnx_flow` API is also available in the `onnx1.13` environment. It is a wrapper of the `kneronnxopt.optimize` API. But not all the previous options are available in the `onnx1.13` environment. We recommend you to use the `kneronnxopt.optimize` API instead of the `onnx2onnx_flow` API.

```python
#[API]
ktc.onnx_optimizer.onnx2onnx_flow(m, opt_matmul=False, duplicate_shared_weights=False)
```

Return the optimized model. Optimize the onnx model.

Args:

* m (ModelProto): the input onnx ModelProto
* opt_matmul (bool, optional): optimize the MatMul layers according to the NPU limit. Defaults to False.
* duplicate_shared_weights(bool, optional): duplicate shared weights. Defaults to False.

By the way, to save the model, you can use the following function from the onnx package.

```python
# Save the onnx object optimized_m to path /data1/optimized.onnx.
onnx.save(optimized_m, '/data1/optimized.onnx')
```

### 3.1.3. ONNX Editing

KL520/KL720/KL530 NPU supports most of the compute extensive OPs, such as Conv, BatchNormalization, Fully Connect/GEMM, in order to speed up the model inference run time. On the other hand, there are some OPs that KL520 NPU cannot support well, such as `Softmax` or `Sigmod`. However, these OPs usually are not compute extensive and they are better to execute in CPU.

Therefore, we recommend users move certain OPs to preprocess or postprocess. We recommend using the ONNX utils api `onnx.utils.extract_model` for ONNX editing. For details, please refer to the [onnx.utils.extract_model](https://onnx.ai/onnx/api/utils.html).

**Please run the optimzier again after modify the model.**

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
* weight_bandwidth: weight bandwidth in gbps. Defaults to None to use the default value for the specific hardware. This only affect the evaluation result.
* dma_bandwidth: dma bandwidth in gbps. Defaults to None to use the default value for the specific hardware. This only affect the evaluation result.

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
