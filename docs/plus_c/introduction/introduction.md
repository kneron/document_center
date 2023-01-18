# Introduction

## Basic Features

**Kneron PLUS** stands for *Platform Library Unified Software* which is a framework comprising new software(SW) and firmware(FW) design for KL520, and KL720 (and alpha for KL630).

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

Index   | Category              | Supported Item                                                            | Min Version (KL520/KL720) | Min Version (KL630) [***1***] | KL520 | KL720 | KL630
------- | :-------------------- | :------------------------------------------------------------------------ | :------------------------ | :---------------------------- | :---: | :---: | :---:
1       | Image Format          | RGBA8888 , RAW8 , Packed YCbCr422 (YUYV422) , RGB565                      |                           |                               |       |       |
2       |                       | Planar YUV420                                                             |                           |                               | X     | X     |
3       | System                | Firmware In Flash                                                         |                           |                               |       |       |
4       |                       | Model In Flash                                                            |                           |                               |       |       |
5       |                       | Runtime Upload Firmware                                                   |                           |                               |       | X     |
6       |                       | Runtime Upload Model                                                      |                           |                               |       |       |
7       |                       | Software Reset                                                            |                           |                               |       |       |
8       |                       | Software Shutdown (Developing Broad Only)                                 |                           |                               |       | X     | X
9       |                       | Software Reboot                                                           |                           |                               |       |       |
10      |                       | Scan Devices                                                              |                           |                               |       |       |
11      |                       | Device Log via USB                                                        |                           |                               |       |       |
12      |                       | Device Connection : All Devices, Specified Device(s)                      |                           |                               |       |       |
13      | Inference             | Flexible Send / Receive Inference                                         |                           |                               |       |       |
14      |                       | Multiple Device Auto Dispatch                                             |                           |                               |       |       |
15      |                       | Enable / Disable Pre-process on Device                                    |                           |                               |       |       |
16      |                       | Enable / Disable Post-process on Device                                   |                           |                               |       |       |
17      |                       | Output Floating Point / Fixed Point Result                                |                           |                               |       |       |
18      |                       | Enable / Disable Debug Checkpoints                                        | v1.3.0                    |                               |       |       |
19      |                       | Enable / Disable Execution Time Profiling                                 | v1.3.0                    |                               |       |       |
20      | System / Model Info   | Get Firmware Version                                                      |                           |                               |       |       |
21      |                       | Get KN Number                                                             |                           |                               |       |       |
22      |                       | Get Model CRC                                                             |                           |                               |       |       |
23      |                       | Get Model Info                                                            |                           |                               |       |       |
24      |                       | Install Device Driver for Windows                                         | v1.3.0                    |                               |       |       |
25      | Application API       | Generic Image Inference                                                   | v2.0.0                    |                               |       |       |
26      |                       | Generic Data Inference                                                    | v2.0.0                    |                               |       |       |
27      |                       | Customized Inference (C code only)                                        |                           |                               |       |       |
28      |                       | User Define API (C code only)                                             |                           |                               |       |       |
29      | System Examples       | Get Firmware Info                                                         |                           |                               |       |       |
30      |                       | Get Model Info                                                            |                           |                               |       |       |
31      |                       | Reboot Device                                                             |                           |                               |       |       |
32      |                       | Shutdown Device                                                           |                           |                               |       | X     | X
33      |                       | Device FIFO Queue Config Example                                          | v2.0.0                    |                               |       |       |
34      | Inference Examples    | Generic Image Inference (Raw Output)                                      | v2.0.0                    |                               |       |       |
35      |                       | Generic Image Inference (with Crop)                                       | v2.0.0                    |                               |       |       |
36      |                       | Generic Image Inference (with Post Process on Host Side)                  | v2.0.0                    |                               |       |       |
37      |                       | Generic Image Inference (Multiple Threads)                                | v2.0.0                    |                               |       |       |
38      |                       | Generic Image Inference (Model in Flash)                                  | v2.0.0                    |                               |       |       |
39      |                       | Generic Image Inference (Web Cam with Drop Frame)                         | v2.0.0                    |                               |       |       |
40      |                       | Generic Data Inference (with Pre Process on Host Side)                    | v2.0.0                    |                               |       |       |
41      |                       | User Define API Inference (Yolo with Config Post Process) (C code only)   | v1.3.0                    |                               |       |       |
42      |                       | Customized Inference with Single Model (C code only)                      | v2.0.0 for KL720          |                               |       |       |
43      |                       | Customized Inference with Multiple Models (C code only)                   | v2.0.0 for KL720          |                               |       |       |
44      | Debug Examples        | Debug Checkpoints Example                                                 | v1.3.0                    |                               |       | X     | X
45      |                       | Execution Time Profiling Example                                          | v1.3.0                    |                               |       | X     | X
46      | Model Zoo Examples    | Simple examples for pre-trained models                                    |                           |                               |       |       | X

**Note**:
- [1] If the minimum version is not written, this feature is supported from v2.1.1.


The following components are contained in Kneron PLUS:

- KP API
- PLUS examples code
- KDP2 firmware code (KL520 and KL720 only)
- Pre-build firmware binary files
- Some demonstrative NEF files

    ![](../imgs/KL520_develop_flow_sw.png)

---

## Advanced Features for Enterprise Version

Besides the basic features, there are few advanced features provided in Kneron PLUS Enterprise:

**Note**: Most of the advanced features and examples are C code only. Only **Update Kdp2 to Kdp2 Flash Boot** has the python version example.

Index   | Category              | Supported Item                                            | Min Version (KL520/KL720) | Min Version (KL630)   | KL520 | KL720 | KL630
------- | :-------------------- | :-------------------------------------------------------- | :------------------------ | :-------------------- | :---: | :---: | :---:
1       | System                | Runtime Upload Firmware via UART                          |                           |                       |       | X     | X
2       |                       | Hico Mode (MIPI image input, Companion Result Output)     |                           | v2.1.1                |   X   |       |
2       | Examples              | Update Kdp to Kdp2 Usb Boot                               |                           |                       |       | X     | X
3       |                       | Update Kdp2 to Kdp2 Usb Boot                              |                           | v2.1.1                |       | X     |
4       |                       | Update Kdp to Kdp2 Flash Boot                             |                           |                       |       |       | X
5       |                       | Update Kdp2 to Kdp2 Flash Boot                            |                           | v2.1.1                |       |       |
6       |                       | Update Model to Flash                                     |                           | v2.1.1                |       |       |
7       |                       | Upload Firmware via UART                                  |                           |                       |       | X     | X
8       |                       | Upload Firmware via Usb for No-Flash Device               | v2.0.0                    |                       |   X   |       | X
9       |                       | Read / Write Device Memory                                |                           |                       |       |       | X
10      |                       | Access Firmware Log via USB                               |                           |                       |   X   |       | X
11      |                       | Hico Cam Inference [***1***] [***2***]                    |                           | v2.1.1                |   X   |       |
12      |                       | Hico ToF Inference (Kneron ToF module is required)        | v1.3.0                    |                       |   X   |       | X

**Note**:

- [1] For Hico Mipi on KL720, Kneron LW 3D module is required.
- [2] For Hico Mipi on KL630, Vatics CIS-OS05A10-EVM-1.0.0 module is required.
