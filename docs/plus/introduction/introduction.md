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

- **KP** API is part of the PLUS written in C/Python and it provides simplied functions and examples to help users develop their software applications. For the complete list of KP API, please refer to another document.

- **NEF** represents for **NPU Executable Format** which may comprise one or multiple models and it can only work on Kneron's SoC. This package comes with some NEFs for demonstration purposes. We will use the **Tiny Yolo v3** NEF as the model input on KL520 in our inference examples.

- **Firmware** is the code responsible for driving Kneron SoC and make it work with the software library. The KDP2 firmware can work with the PLUS and it has prebuilt images included in the PLUS.


The features which PLUS Supported are listed below:

Index   | Category              | Supported Item                                            | KL520 | KL720
------- | :-------------------- | :-------------------------------------------------------- | :---: | :---:
1       | Image Format          | RGBA8888 , RAW8 , YUYV422 , RGB565                        |       |
2       | System                | Firmware In Flash                                         |       |
3       |                       | Model In Flash                                            |       |
4       |                       | Runtime Upload Firmware                                   |       | X
5       |                       | Runtime Upload Model                                      |       |
6       |                       | Software Reset                                            |       |
7       |                       | Scan Devices                                              |       |
8       |                       | Device Log via USB                                        |       |
9       | Device Connection     | All Dongles, Specified Dongle(s)                          |       |
10      | Inference             | Sync / Async Mode Inference                               |       |
11      |                       | Multiple Dongle Auto Dispatch                             |       |
12      |                       | Enable / Disable Pre-process on Device                    |       |
13      |                       | Enable / Disable Post-process on Device                   |       |
14      |                       | Output Floating Point Result                              |       |
15      | System / Model Info   | Get Firmware Version                                      |       |
16      |                       | Get KN Number                                             |       |
17      |                       | Get Model CRC                                             |       |
18      |                       | Get Model Info                                            |       |
19      | Application API       | App Yolo Inference                                        |       |
20      |                       | Generic Inference                                         |       |
21      |                       | Customized Inference (C code only)                        |       |
22      | Inference Examples    | App Yolo Inference (Single Thread)                        |       |
23      |                       | App Yolo Inference (Multiple Threads)                     |       |
24      |                       | App Yolo Inference (Model in Flash)                       |       |
25      |                       | App Yolo Inference (Web Cam)                              |       |
26      |                       | App Yolo Inference (Web Cam with Drop Frame)              |       |
27      |                       | Generic Inference (Raw Output)                            |       |
28      |                       | Generic Inference (with Crop)                             |       |
29      |                       | Generic Inference (with Post Process on Host Side)        |       |
30      |                       | Customized Inference with Single Model (C code only)      |       |
31      |                       | Customized Inference with Multiple Models (C code only)   |       | X
31      | Model Zoo Examples    | Simple examples for pre-trained models                    |       | 


The following components are contained in Kneron PLUS:

- KP API
- PLUS examples code
- KDP2 firmware code (KL520 only)
- Pre-build firmware binary files
- Some demonstrative NEF files

    ![](../imgs/KL520_develop_flow_sw.png)
