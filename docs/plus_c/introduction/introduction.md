# Introduction

## Basic Features

**Kneron PLUS** stands for *Platform Library Unified Software* which is a framework comprising new software(SW) and firmware(FW) design for KL520 (and alpha for KL720).

In order to run the inference of models on Kneron AI devices, there are three parts of AI application development are required:

- **model development**
- **software development**
- **firmware development**

Below diagram depicts three parts of development in a big picture.

![](../imgs/KL520_develop_flow.png)

However, this document only focuses on the **software development** and the **firmware development**. For the **model development**, please refer to the [Toolchain Docker](../../toolchain/manual_1_overview.md) part.

In comparison with the previous SW/FW framework, this aims to simplify the design flow for AI applications development.

Below gives some definitions regarding the Kneron PLUS:

- **PLUS** is a software library developed by Kneron and it allows users to manipulate the AI device through sophisticated C/C++/Python API.

- **KP** API is part of the PLUS written in C/Python and it provides simplified functions and examples to help users develop their software applications. For the complete list of KP API, please refer to another document.

- **NEF** represents for **NPU Executable Format** which may comprise one or multiple models and it can only work on Kneron's SoC. This package comes with some NEFs for demonstration purposes. We will use the **Tiny Yolo v3** NEF as the model input on KL520 in our inference examples.

- **Firmware** is the code responsible for driving Kneron SoC and make it work with the software library. The KDP2 firmware can work with the PLUS and it has prebuilt images included in the PLUS.


The features which PLUS Supported are listed below:

Index   | Category              | Supported Item                                                            | Minimum Version   | KL520 | KL720
------- | :-------------------- | :------------------------------------------------------------------------ | :---------------- | :---: | :---:
1       | Image Format          | RGBA8888 , RAW8 , YCbCr422 (YUYV422) , RGB565                             |                   |       |
2       | System                | Firmware In Flash                                                         |                   |       |
3       |                       | Model In Flash                                                            |                   |       |
4       |                       | Runtime Upload Firmware                                                   |                   |       | X
5       |                       | Runtime Upload Model                                                      |                   |       |
6       |                       | Software Reset                                                            |                   |       |
7       |                       | Software Shutdown (Developing Broad Only)                                 |                   |       | X
8       |                       | Software Reboot                                                           |                   |       |
9       |                       | Scan Devices                                                              |                   |       |
10      |                       | Device Log via USB                                                        |                   |       |
11      |                       | Device Connection : All Devices, Specified Device(s)                      |                   |       |
12      | Inference             | Flexible Send / Receive Inference                                         |                   |       |
13      |                       | Multiple Device Auto Dispatch                                             |                   |       |
14      |                       | Enable / Disable Pre-process on Device                                    |                   |       |
15      |                       | Enable / Disable Post-process on Device                                   |                   |       |
16      |                       | Output Floating Point / Fixed Point Result                                |                   |       |
17      |                       | Enable / Disable Debug Checkpoints                                        | v1.3.0            |       |
18      |                       | Enable / Disable Execution Time Profiling                                 | v1.3.0            |       |
19      | System / Model Info   | Get Firmware Version                                                      |                   |       |
20      |                       | Get KN Number                                                             |                   |       |
21      |                       | Get Model CRC                                                             |                   |       |
22      |                       | Get Model Info                                                            |                   |       |
23      |                       | Install Device Driver for Windows                                         | v1.3.0            |       |
24      | Application API       | Generic Image Inference                                                   | v2.0.0            |       |
25      |                       | Generic Data Inference                                                    | v2.0.0            |       |
26      |                       | Customized Inference (C code only)                                        |                   |       |
27      |                       | User Define API (C code only)                                             |                   |       |
28      | System Examples       | Get Firmware Info                                                         |                   |       |
29      |                       | Get Model Info                                                            |                   |       |
30      |                       | Reboot Device                                                             |                   |       |
31      |                       | Shutdown Device                                                           |                   |       | X
32      |                       | Device FIFO Queue Config Example                                          | v2.0.0            |       |
33      | Inference Examples    | Generic Image Inference (Raw Output)                                      | v2.0.0            |       |
34      |                       | Generic Image Inference (with Crop)                                       | v2.0.0            |       |
35      |                       | Generic Image Inference (with Post Process on Host Side)                  | v2.0.0            |       |
36      |                       | Generic Image Inference (Multiple Threads)                                | v2.0.0            |       |
37      |                       | Generic Image Inference (Model in Flash)                                  | v2.0.0            |       |
38      |                       | Generic Image Inference (Web Cam with Drop Frame)                         | v2.0.0            |       |
39      |                       | Generic Data Inference (with Pre Process on Host Side)                    | v2.0.0            |       |
40      |                       | User Define API Inference (Yolo with Config Post Process) (C code only)   | v1.3.0            |       |
41      |                       | Customized Inference with Single Model (C code only)                      | v2.0.0 for KL720  |       |
42      |                       | Customized Inference with Multiple Models (C code only)                   | v2.0.0 for KL720  |       |
43      | Debug Examples        | Debug Checkpoints Example                                                 | v1.3.0            |       | X
44      |                       | Execution Time Profiling Example                                          | v1.3.0            |       | X
45      | Model Zoo Examples    | Simple examples for pre-trained models                                    |                   |       |


The following components are contained in Kneron PLUS:

- KP API
- PLUS examples code
- KDP2 firmware code (KL520 only)
- Pre-build firmware binary files
- Some demonstrative NEF files

    ![](../imgs/KL520_develop_flow_sw.png)

---

## Advanced Features for Enterprise Version

Besides the basic features, there are few advanced features provided in Kneron PLUS Enterprise:

**Note**: Most of the advanced features and examples are C code only. Only **Update Kdp2 to Kdp2 Flash Boot** has the python version example.

Index   | Category              | Supported Item                                            | Minimum Version   | KL520 | KL720
------- | :-------------------- | :-------------------------------------------------------- | :---------------- | :---: | :---:
1       | System                | Runtime Upload Firmware via UART                          |                   |       | X
2       |                       | Hico Mode (MIPI image input, Companion Result Output)     |                   |   X   |
2       | Examples              | Update Kdp to Kdp2 Usb Boot                               |                   |       | X
3       |                       | Update Kdp2 to Kdp2 Usb Boot                              |                   |       | X
4       |                       | Update Kdp to Kdp2 Flash Boot                             |                   |       |
5       |                       | Update Kdp2 to Kdp2 Flash Boot                            |                   |       |
6       |                       | Update Model to Flash                                     |                   |       |
7       |                       | Upload Firmware via UART                                  |                   |       | X
8       |                       | Upload Firmware via Usb for No-Flash Device               | v2.0.0            |   X   |
9       |                       | Read / Write Device Memory                                |                   |       |
10      |                       | Access Firmware Log via USB                               |                   |   X   |
11      |                       | Hico Cam Inference (Kneron LW 3D module is required)      |                   |   X   |
12      |                       | Hico ToF Inference (Kneron ToF module is required)        | v1.3.0            |   X   |
