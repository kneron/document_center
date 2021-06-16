# Introduction

**Kneron PLUS** stands for *Platform Library Unified Software* which is a framework comprising new software(SW) and firmware(FW) design for KL520 (and alpha for KL720).  

In order to run the inference of models on Kneron AI dongles, there are three parts of AI application development are required:

- **model development**
- **software development**
- **firmware development**

Below diagram depicts three parts of development in a big picture.

![](../imgs/KL520_develop_flow.png)

However, this document only focuses on the **software development** and the **firmware development**. For the **model development**, please refer to the **Toolchain Docker** part.

In comparison with the previous SW/FW framework, this aims to simplify the design flow for AI applications development.

Below gives some definitions regarding the Kneron PLUS:

- **PLUS** is a software library developed by Kneron and it allows users to manipulate the AI dongle through sophisticated C/C++/Python API.

- **KP** API is part of the PLUS written in C and it provides simplied functions and examples to help users develop their software applications. For the complete list of KP API, please refer to another document.

- **NEF** represents for **NPU Executable Format** which may comprise one or multiple models and it can only work on Kneron's SoC. The host_lib comes with some NEFs for demonstration purposes. We will use the **Tiny Yolo v3** NEF as the model input in our inference examples.

- **Firmware** is the code responsible for driving Kneron SoC and make it work with the software library. The KDP2 firmware can work with the PLUS and it has prebuilt images included in the PLUS.


The features which PLUS Supported are listed below:

Index   | Category          | Supported Item
------- | :---------------- | :---------------
1       | Image Format      | RGBA8888 , RAW8 , YUYV422 , RGB565
2       | System            | Firmware In Flash
3       |                   | Runtime Upload Firmware
4       |                   | Runtime Upload Model
5       |                   | Software Reset
6       |                   | Scan Devices
7       |                   | Device Log via USB
8       | Device Connection | All Dongles , Specified Dongle(s)
9       | Inference         | Sync / Async Mode Inference
10      |                   | Multiple Dongle Auto Dispatch
11      |                   | Enable / Disable Pre-process on Device
12      |                   | Enable / Disable Post-process on Device
13      |                   | Output Floating Point Result
14      | Utility           | Get CRC
15      |                   | Get KN Number
16      |                   | Get Model Info
17      |                   | Get NEF Model Meta Data
18      | Application API   | Tiny Yolo v3
19      |                   | Generic Inference
20      |                   | Customized Inference
21      | Example           | Tiny Yolo v3
22      |                   | Generic Inference (Tiny Yolo v3)
23      |                   | Customized Inference with Single Model (Tiny Yolo v3)
24      |                   | Customized Inference with Multiple Models (Face Detect + Landmark)


The following components are contained in Kneron PLUS:

- KP API
- PLUS examples code
- KDP2 firmware code
- Pre-build firmware binary files
- Some demonstrative NEF files

    ![](../imgs/KL520_develop_flow_sw.png)
