<div align="center">
<img src="../imgs/manual/kneron_log.png">
</div>

# Kneron Linux Toolchain Manual

**2021 Jun**
**Toolchain v0.15.0**

[PDF Downloads](manual.pdf)

## 0. Overview

KDP toolchain is a set of software which provide inputs and simulate the operation in the hardware KDP 520 and KDP 720. For better
environment compatibility, we provide a docker which include all the dependencies as well as the toolchain software.

**This document is compatible with `kneron/toolchain:v0.15.0`.**

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.3         | 158 ms         |        No        |
| Inception v4         | 299x299 |    0.48        | 2068 ms        |        No        |
| Mobilenet v1         | 224x224 |    60.7        | 16.5 ms        |        No        |
| Mobilenet v2         | 224x224 |    61.3        | 16.3 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    30.4        | 32.9 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    7.02        | 142.4 ms       |        No        |
| OpenPose             | 256x256 |    0.61        | 1639 ms        |        No        |
| SRCNN                | 384x384 |    7.04        | 142 ms         |        No        |
| Tiny yolo v3         | 416x416 |    22.8        | 43.8 ms        |        Yes       |
| Yolo v3              | 416x416 |    1.5         | 666.7 ms       |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    80.9        | 12.4 ms        |        No        |
| Inception v4         | 299x299 |    19.9        | 50.2 ms        |        No        |
| Mobilenet v1         | 224x224 |    404         | 2.48 ms        |        No        |
| Mobilenet v2         | 224x224 |    624         | 1.60 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    283         | 3.54 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    52.3        | 19.1 ms        |        No        |
| OpenPose             | 256x256 |    5.3         | 189 ms         |        No        |
| SRCNN                | 384x384 |    127         | 7.87 ms        |        No        |
| Tiny yolo v3         | 416x416 |    148         | 6.75 ms        |        No        |
| Yolo v3              | 416x416 |    10.5        | 95.3 ms        |        No        |
| Centernet res101     | 512x512 |    3.02        | 331 ms         |        No        |
| Unet                 | 384x384 |    2.83        | 354 ms         |        No        |

In this document, you'll learn:

1. How to install and use the toolchain docker.
2. What tools are in the toolchain.
3. How to use utilize the tools through Python API.

** Major changes of past versions**

* **[v0.15.0]**
    * Document now is written for Python API. The original script document can be found in [Command Line Script Tools](http://doc.kneron.com/docs/toolchain/command_line/).
* **[v0.14.0]**
    * ONNX is updated to 1.6.0
    * Pytorch is updated to 1.7.1
    * Introduce toolchain Python API.
* **[v0.13.0]**
    * 520 toolchain and 720 toolchain now is combined into one. But the scripts names and paths are the same as before. You don't need to learn it again.
    * E2E simulator has been updated to a new version. Usage changed. Please check its document.
* **[v0.12.0]** Introduce `convert_model.py` which simplify the conversion process.
* **[v0.11.0]** Batch compile now generate `.nef` files to simplify the output.
* **[v0.10.0]**
    * `input_params.json` and `batch_input_params.json` have been simplified a lot. Please check the document for details.
    * `simulator.sh`, `emulator.sh` and draw yolo image scripts are no longer available from `/workspace/scripts`. They have been moved to E2E simulator. Please check its document.
* **[v0.9.0]** In the example, the mount folder `/docker_mount` is separated from the interactive folder `/data1` to avoid
unexpected file changes. Users need to copy data between the mount folder and the interactive folder. Of course you can
still mount on `/data1`. But please be careful that the results folder under `/data1` may be overwritten.

## 1. Installation

**Review the system requirements below before start installing and using the toolchain.**

### 1.1 System requirements

1. **Hardware**: Minimum quad-core CPU, 4GB RAM and 6GB free disk space.
2. **Operating system**: Window 10 x64 version 1903 or higher with build 18362 or higher. Ubuntu 16.04 x64 or higher.
Other OS which can run docker later than 19.03 may also work. But they are not tested. Please take the risk yourself.
3. **Docker**: Docker Desktop later than 19.03. Here is a [link](https://www.docker.com/products/docker-desktop) to
download Docker Desktop.

> **TIPS:**
>
> For Windows 10 users, we recommend using docker with wsl2, which is Windows subsystem Linux provided by Microsoft.
> Here is [how to install wsl2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and
> [how to install and run docker with wsl2](https://docs.docker.com/docker-for-windows/wsl/)

Please double-check whether the docker is successfully installed and callable from the console before going on to the
next section. If there is any problem about the docker installation, please search online or go to the docker community
for further support. The questions about the docker is beyond the reach of this document.

### 1.2 Pull the latest toolchain image

All the following steps are on the command line. Please make sure you have the access to it.

> TIPS:
>
> You may need `sudo` to run the docker commands, which depends on your system configuration.


You can use the following command to pull the latest toolchain docker.

```bash
docker pull kneron/toolchain:latest
```

Note that this document is compatible with toolchain v0.14.2. You can find the version of the toolchain in
`/workspace/version.txt` inside the docker. If you find your toolchain is later than v0.14.2, you may need to find the
latest document from the [online document center](http://doc.kneron.com/docs).

## 2. Toolchain Docker Overview

After pulling the desired toolchain, now we can start walking through the process. In all the following sections, we use
`kneron/toolchain:latest` as the docker image. Before we actually start the docker, we'd better provide a folder
which contains the model files you want to test in our docker, for example, `/mnt/docker`. Then, we can use the
following command to start the docker and work in the docker environment:

```bash
docker run --rm -it -v /mnt/docker:/docker_mount kneron/toolchain:latest
```

> TIPS:
>
> The mount folder path here is recommended to be an absolute path.

Here are the brief explanations for the flags. For detailed explanations, please visit [docker documents](https://docs.docker.com/engine/reference/run/).

* `--rm`: the container will be removed after it exists. Each time we use `docker run`, we create a new docker
container. Thus, without this flag, the docker will consumes more and more disk space.
* `-it`: enter the interactive mode so we can use the bash.
* `-v`: mount a folder into the docker container. Thus, we can visit the desired files from the host and save the result
from the container.

### 2.1 Folder structure

After logging into the container, you are under `/workspace`, where all the tools are. Here is the folder structure and
their usage:

```
/workspace
|-- E2E_Simulator       # End to end simulator
|-- ai_training         # AI training project.
|-- cmake               # Environment
|-- examples            # Example for the workflow, will be used later.
|-- libs                # The libraries
|   |-- ONNX_Convertor  # ONNX Converters and optimizer scripts, will be discussed in section 3.
|   |-- compiler        # Compiler for the hardware and the IP evaluator to infer the performance.
|   |-- dynasty         # Simulator which only simulates the calculation.
|   |-- fpAnalyser      # Analyze the model and provide fixed point information.
|   `-- hw_c_sim        # Hardware simulator which simulate all the hardware behaviours.
|-- miniconda           # Environment
|-- scripts             # Scripts to run the tools, will be discussed in section 3.
`-- version.txt
```

### 2.2 Work flow

Before we start actually introducing the usage, let us go through the general work flow.

<div align="center">
<img src="../imgs/manual/Manual_Flow_Chart.png">
<p><span style="font-weight: bold;">Figure 1.</span> Diagram of working flow</p>
</div>

To keep the diagram as clear as possible, some details are omitted. But it is enough to show the general steps. There are three main sections:

1. ONNX section. Convert the model from different platforms to onnx and optimize the onnx file. Evaluate the onnx the model to check the operator support and the estimate performance. Then, test the onnx model and compare the result with the source.
2. Bie section. Quantize the model and generate bie file. Test the bie file and compare the result with the previous step.
3. Nef section. Batch compile multiple bie models into a bie binary file. Test the nef file and compare the result with the previous step.

> The workflow has been changed a lot since v0.15.0. We recommend Python API instead of the original scritps for a more smooth workflow. But this doesn't means the scripts used before are abandoned. They are still available and the document can be found in [Command Line Script Tools](http://doc.kneron.com/docs/toolchain/command_line/). The detailed document of the Python API can be found in [Toolchain Python API](http://doc.kneron.com/docs/toolchain/python_api/)

### 2.3 Supported operators

Table 1.1 shows the list of functions KDP520 supports base on ONNX 1.6.1.

*Table 1.1 The functions KDP520 NPU supports*

| Type             | Operarots                     | Applicable Subset | Spec.                 |
| ---------------- | ----------------------------- | ----------------- | --------------------- |
| Convolution      | Conv                          | Kernel dimension  | 1x1 up to 11x11       |
|                  |                               | Strides           | 1,2,4                 |
|                  | Pad                           |                   | 0-15                  |
|                  | Depthwise Conv                |                   | Yes                   |
|                  | Deconvolution                 |                   | Use Upsampling + Conv |
| Pooling          | MaxPool                       | 3x3               | stride 1,2,3          |
|                  | MaxPool                       | 2x2               | stride 1,2            |
|                  | AveragePool                   | 3x3               | stride 1,2,3          |
|                  | AveragePool                   | 2x2               | stride 1,2            |
|                  | GlobalAveragePool             |                   | support               |
|                  | GlobalMaxPool                 |                   | support               |
| Activation       | Relu                          |                   | support               |
|                  | LeakyRelu                     |                   | support               |
|                  | PRelu                         |                   | support               |
| Other processing | BatchNormalization            |                   | support               |
|                  | Add                           |                   | support               |
|                  | Concat                        |                   | axis = 1              |
|                  | Gemm or Dense/Fully Connected |                   | support               |
|                  | Flatten                       |                   | support               |
|                  | Clip                          |                   | min = 0               |

Table 1.2 shows the list of functions KDP720 supports base on ONNX 1.6.1.

*Table 1.2 The functions KDP720 NPU supports*

| Node               | Applicable Subset    | Spec.                           |
| ------------------ | -------------------- | ------------------------------- |
| Relu               |                      | support                         |
| PRelu              |                      | support                         |
| LeakyRelu          |                      | support                         |
| Sigmoid            |                      | support                         |
| Clip               |                      | min = 0                         |
| Tanh               |                      | support                         |
| BatchNormalization | up to 4D input       | support                         |
| Conv               |                      | strides < [4, 16]               |
| Pad                |                      | spacial dimension only          |
| ConvTranspose      |                      | strides = [1, 1], [2, 2]        |
| Upsample           |                      | support                         |
| Gemm               | 2D input             | support                         |
| Flatten            | Before Gemm          | support                         |
| Add                |                      | support                         |
| Concat             |                      | axis = 1                        |
| Mul                |                      | support                         |
| MaxPool            |                      | kernel = [1, 1], [2, 2], [3, 3] |
| AveragePool        | 3x3                  | kernel = [1, 1], [2, 2], [3, 3] |
| GlobalAveragePool  | 4D input             | support                         |
| GlobalMaxPool      |                      | support                         |
| MaxRoiPool         |                      | support                         |
| Slice              | input dimension <= 4 | support                         |

## 3 ONNX Workflow

Our toolchain utilities take ONNX files as inputs. The ONNX workflow is mainly about convert models from other platforms to ONNX and prepare the onnx for the quantization and compilation. There are three main steps: conversion, evaluation and testing.

### 3.1 Model Conversion and Optimization

The onnx converter part currently support Keras, TFLite, a subset of Tensorflow, Caffe and Pytorch. Here, we will only briefly introduce some common usage of the python API. This part of python API is based on our converter and optimizer open-source project which can be found on Github <https://github.com/kneron/ONNX_Convertor>. The detailed usage of those converter scripts can be found in [ONNX Converter](http://doc.kneron.com/docs/toolchain/converters/).

The example models used in the following converter command are not included in the docker by default. They can be found on Github <https://github.com/kneron/ConvertorExamples>. You can download them through these commands:

```bash
git clone https://github.com/kneron/ConvertorExamples.git
cd ConvertorExamples && git lfs pull
```

### 3.1.1 Keras to ONNX

### 3.1.2 Caffe to ONNX

### 3.1.3 TFLite to ONNX

### 3.1.4 Pytorch to ONNX

### 3.1.5 ONNX Optimization

### 3.1.6 ONNX Opset Upgrade

### 3.1.7 ONNX Editor

### 3.2 IP Evaluation

### 3.3 E2E Simulator Check (Floating Point)

## 4 BIE Workflow

### 4.1 Quantization

### 4.2 E2E Simulator Check (Fixed Point)

## 5 NEF Workflow

### 5.1 Batch Compile (One Model)

### 5.2 Batch Compiler (Multiple Models)

### 5.2 E2E Simulator Check (Hardware)

## 6 What's Next

## FAQ

1. 