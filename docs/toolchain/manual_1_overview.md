<div align="center">
<img src="../imgs/manual/kneron_log.png">
</div>

# 1. Toolchain Overview

**2022 Nov**
**Toolchain v0.20.0**

## 1.1. Introduction

KDP toolchain is a set of software which provide inputs and simulate the operation in the hardware KDP 520, 720, 530 and 730(preview).
For better environment compatibility, we provide a docker which include all the dependencies as well as the toolchain software.

In this document, you'll learn:

1. What tools are in the toolchain.
2. How to deploy the latest toolchain.
3. How to utilize the tools through Python API.

**Major changes of the current version**

* **[v0.20.0]**
    * Support text procssing models.
    * Set flatbuffer as the default 720 compiling mode.
    * Refactor compiler and analyser inner structure.
    * Refactor toolchain manual.
    * Bug fixes.

## 1.2. Workflow Overview

In the following parts of this page, you can go through the basic toolchain working process to get familiar with the toolchain.

Below is a breif diagram showing the workflow of how to generate the binary from a floating-point model using the toolchain.

<div align="center">
<img src="../imgs/manual/Manual_Flow_Chart.png">
<p><span style="font-weight: bold;">Figure 1.</span> Diagram of working flow</p>
</div>

To keep the diagram as clear as possible, some details are omitted. But it is enough to show the general structure. There are three main sections:

1. Floating-point model preparation. Convert the model from different platforms to onnx and optimize the onnx file. Evaluate the onnx the model to check the operator support and the estimate performance. Then, test the onnx model and compare the result with the source.
2. Fixed-point model generation. Quantize the floating-point model and generate bie file. Test the bie file and compare the result with the previous step.
3. Compilation. Batch compile multiple bie models into a nef format binary file. Test the nef file and compare the result with the previous step.

In the following parts, we will use LittleNet as the example. Details will be explained later in other sections.
And all the code below in this section can be found inside the docker at `/workspace/examples/test_python_api.py`.

### 1.3. Toolchain Docker Deployment

We provide docker images for ease of deployment. Below are command for downloading and running the latest docker image.

```bash
# Pull the latest toolchain docker image.
docker pull kneron/toolchain:latest

# Login to the docker and mount host machine /mnt/docker into the docker at /docker_mount.
docker run --rm -it -v /mnt/docker:/docker_mount kneron/toolchain:latest
```

To learn more about the docker installation, docker image version management, docker usage and environment inside the docker,
please check [2. Toolchain Deployment](manual_2_deploy.md).

## 1.4. Floating-Point Model Preparation

Our toolchain utilities take ONNX files as inputs. This part of workflow is mainly about convert models from other platforms to ONNX and prepare the onnx for the quantization and compilation. There are three main steps: conversion, evaluation and testing.

For more details about the model conversion and optimization, please check [3. Floating-Point Model Preparation](manual_3_onnx.md).

### 1.4.1. Model Conversion And Optimization

Before we start, we need to import our python package. The package name is `ktc`. You can simply start by having `import ktc` in the script.
In the following sections, we'll introduce the API and their usage. You can also find the usage using the python `help()` function.

**Note that this package is only available in the docker due to the dependency issue.**

Here the LittleNet model is already in ONNX format. So, we only need to optimize the ONNX model to fix our toolchain.
The following model optimization code is in Python since we are using the Python API.

```python
import onnx
# Import the ktc package which is our Python API.
import ktc

# Load the model.
original_m = onnx.load("/workspace/examples/LittleNet/LittleNet.onnx")
# Optimize the model using optimizer for onnx model.
optimized_m = ktc.onnx_optimizer.onnx2onnx_flow(original_m)
# Save the onnx object optimized_m to path /data1/optimized.onnx.
onnx.save(optimized_m, '/data1/optimized.onnx')
```

### 1.4.2. Model Evaluation

Before we start quantizing the model and try simulating the model, we need to test if the model can be taken by the toolchain structure and estimate the performance.
IP evaluator is such a tool which can estimate the performance of your model and check if there is any operator or structure not supported by our toolchain.

```python
# Create a ModelConfig object. For details about this class, please check Appendix Python API.
# Here we set the model ID to 32769, the version to 0001 and the target platform to 520
# The `optimized_m` is from the previous code block.
km = ktc.ModelConfig(32769, "0001", "520", onnx_model=optimized_m)

# Evaluate the model. The evaluation result is saved as string into `eval_result`.
eval_result = km.evaluate()
```

The evaluation result will be returned as string. User can also find the evaluation result under /data1/compiler/.
But the report file names are different for different platforms.

* 520: ip_eval_prof.txt
* Other hardware: ProfileResult.txt

### 1.4.3. Floating-Point Model Inference

Before going into the next section of quantization, we need to ensure the optimized onnx file can produce the same result as the originally designed model.
Here we introduce the E2E simulator which is the abbreviation for end to end simulator. It can inference a model and simulate the calculation of the hardware.
We are using the onnx as the input model now. But it also can take other file formats which would be introduced later.

```python
# Import necessary libraries for image processing.
from PIL import Image
import numpy as np

# A very simple preprocess function. Note that the image is transposed into channel last format.
def preprocess(input_file):
    image = Image.open(input_file)
    image = image.convert("RGB")
    img_data = np.array(image.resize((112, 96), Image.BILINEAR)) / 255
    img_data = np.transpose(img_data, (1, 0, 2))
    return img_data

# Use the previous function to preprocess an example image as the input.
input_data = [preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0001.png")]

# The `onnx_file` is generated and saved in the previous code block.
# The `input_names` are the input names of the model.
# The `input_data` order should be kept corresponding to the input names.
# The inference result will be save as a list of array.
floating_point_inf_results = ktc.kneron_inference(input_data, onnx_file='/data1/optimized.onnx', input_names=["data_out"])
```

After getting the `floating_point_inf_results` and post-process it, you may want to compare the result with the one generated by the source model.
Since we want to keep this flow as clear as possible in this walk through, we do not provide any postprocess and skip the step of comparing the inference result for this example.

## 1.5. Fixed-Point Model Generation

In this chapter, we would go through fixed-point model generation and verification. In our toolchain, the fixed-point
model is generated by quantization and saved in bie format. It is encrpyted and not available for visuanlization.
The details about the fixed-point model generation are under [4. Fixed-Point Model Generation](manual_4_bie.md).

### 1.5.1. Quantization

Quantization is the step where the floating-point weight are quantized into fixed-point to reduce the size and the calculation complexity.
The Python API for this step is called `analysis`. It is also a class function of `ktc.ModelConfig`.

This is a very simple example usage. There are many more parameters for fine-tuning. Please check [4. Fixed-Point Model Generation](manual_4_bie.md).

```python
# Preprocess images as the quantization inputs. The preprocess function is defined in the previous section.
input_images = [
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0001.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0002.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0003.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0004.png"),
]

# We need to prepare a dictionary, which mapping the input name to a list of preprocessed arrays.
input_mapping = {"data_out": input_images}

# Quantization the model. `km` is the ModelConfig object defined in the previous section.
# The quantized model is saved as a bie file. The path to the bie file is returned as a string.
bie_path = km.analysis(input_mapping, threads = 4)
```

### 1.5.2. Fixed-Point Model Inference

Before going into the next section of compilation, we need to ensure the quantized model do not lose too much precision.
We would use `ktc.kneron_inference` here, too. But here we are using the generated bie file as the input.

The python code would be like:

```python
# Use the previous function to preprocess an example image as the input.
# Here the input image is the same as in section 1.4.3.
input_data = [preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0001.png")]

# Inference with a bie file. `bie_path` is defined in section 1.5.1.
fixed_point_inf_results = ktc.kneron_inference(input_data, bie_file=bie_path, input_names=["data_out"])

# Compare `fixed_point_inf_results` and `floating_point_inf_results` to check the precision loss.
```

As mentioned above, we do not provide any postprocess. In reality, you may want to have your own postprocess function in Python, too.

After getting the `fixed_point_inf_results` and post-process it, you may want to compare the result with the `floating_point_inf_results`
which is generated in section 1.4.3 to see if the precision lose too much. We skip this step to keep this quick start as simple as possible.

## 1.6. Compilation

Finally, we can compiling models into the binary files which are in nef format. In fact, our compiler can compile multiple
models into just one nef file, that's why it is called 'batch compile'. However in this simple example, we would not go
that deep. If you are willing to learn more, please check [5. Compilation](manual_5_nef.md).

### 1.6.1. Batch Compile

Batch compile turns multiple models into a single binary file. But, we would use the single model we just generated for now.

```python
# `compile` function takes a list of ModelConfig object.
# The `km` here is first defined in section 3 and quantized in section 4.
# The compiled binary file is saved in nef format. The path is returned as a `str` object.
nef_path = ktc.compile([km])
```

### 1.6.2. Hardware Simulation

After compilation, we need to check if the nef can work as expected.
We would use `ktc.kneron_inference` here again. And we are using the generated nef file this time.

```python
# `nef_path` is defined in section 1.6.1.
binary_inf_results = ktc.kneron_inference(input_data, nef_file=nef_path)

# Compare binary_inf_results and fixed_point_inf_results. They should be almost the same.
```

After getting the `binary_inf_results` and post-process it, you may want to compare the result with the `fixed_point_inf_results` which is generated in section 1.5.2 to see if the results match. Once the results match, then you can deploy your model onto the chip. Congratulations.

## 1.7 What's Next

This overview section only provides a simplified version of the workflow. The aim of this section is to get your an idea
of how our toolchain shall be utilized. There are much more details which help you deploy your own model and may greatly
improve your model performance on-chip waiting in other section. Please check.

* [2. Toolchain Deployment](manual_2_deploy.md)
* [3. Floating-Point Model Preparation](manual_3_onnx.md)
* [4. Fixed-Point Model Generation](manual_4_bie.md)
* [5. Compilation](manual_5_nef.md)

There are also other useful tools and informations:

* [End to End Simulator](appendix/app_flow_manual.md): manual for the E2E simualtor.
* [Hardware Performance](appendix/performance.md): common model performance table for Kneron hardwares and the supported operator list.
* [Hardware Supported Operators](appendix/operators.md): operators supported by the hardware.
* [ONNX Converters](appendix/converters.md): manual for the script usage of our converter tools.
* [Script Tools](appendix/command_line.md): manual for deprecated command line tools. Kept for compatibility of toolchain before v0.15.0)
* [Toolchain History](appendix/history.md): manuals for history version of toolchain and the change log.
* [Web GUI](appendix/toolchain_webgui.md): a simple web interface for the toolchain docker image.
* [YOLO Example](appendix/yolo_example.md): a step-by-step walk through using YOLOv3 as the example.
* [Yolo Example (With In-Model Preprocess)](appendix/yolo_example_InModelPreproc_trick.md): a step-by-step walk through using YOLOv3 with in-model preprocess as the example.


