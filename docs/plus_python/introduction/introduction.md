# Introduction

## Basic Features

**Kneron PLUS** stands for *Platform Library Unified Software* which is a framework comprising new software(SW) and firmware(FW) design for KL520, KL720, KL630 and KL730.

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

Index   | Category              | Supported Item                                                            | Min Version (KL520/KL720) | Min Version (KL630) [***1***] | Min Version (KL730) [***2***][***3***] | KL520 | KL720 | KL630 | KL730
------- | :-------------------- | :------------------------------------------------------------------------ | :------------------------ | :---------------------------- | :------------------------------------- | :---: | :---: | :---: | :---:
1       | Image Format          | RGBA8888 , RAW8 , Packed YCbCr422 (YUYV422) , RGB565                      |                           | | |       |       |       |
2       |                       | Planar YUV420                                                             |                           | | | X     | X     |       |
3       | System                | Firmware In Flash                                                         |                           | | |       |       |       |
4       |                       | Model In Flash                                                            |                           | | |       |       |       |
5       |                       | Runtime Upload Firmware                                                   |                           | | |       | X     |       |
6       |                       | Runtime Upload Model                                                      |                           | | |       |       |       |
7       |                       | Software Reset                                                            |                           | | |       |       |       |
8       |                       | Software Shutdown (Developing Broad Only)                                 |                           | | |       | X     | X     | X
9       |                       | Software Reboot                                                           |                           | | |       |       |       |
10      |                       | Scan Devices                                                              |                           | | |       |       |       |
11      |                       | Device Log via USB                                                        |                           | | | X     |       | X     | X
12      |                       | Device Connection : All Devices, Specified Device(s)                      |                           | | |       |       |       |
13      | Inference             | Flexible Send / Receive Inference                                         |                           | | |       |       |       |
14      |                       | Multiple Device Auto Dispatch                                             |                           | | |       |       |       |
15      |                       | Enable / Disable Pre-process on Device                                    |                           | | |       |       |       |
16      |                       | Enable / Disable Post-process on Device                                   |                           | | |       |       |       |
17      |                       | Output Floating Point / Fixed Point Result                                |                           | | |       |       |       |
20      | System / Model Info   | Get Firmware Version                                                      |                           | | |       |       |       |
21      |                       | Get KN Number                                                             |                           | | |       |       |       |
22      |                       | Get Model CRC                                                             |                           | | |       |       |       |
23      |                       | Get Model Info                                                            |                           | | |       |       |       |
24      |                       | Install Device Driver for Windows                                         | v1.3.0                    | | |       |       |       |
25      | Application API       | Generic Image Inference                                                   | v2.0.0                    | | |       |       |       |
26      |                       | Generic Data Inference                                                    | v2.0.0                    | | |       |       |       |
29      | System Examples       | Get Firmware Info                                                         |                           | | |       |       |       |
30      |                       | Get Model Info                                                            |                           | | |       |       |       |
31      |                       | Reboot Device                                                             |                           | | |       |       |       |
32      |                       | Shutdown Device                                                           |                           | | |       | X     | X     | X
33      |                       | Device FIFO Queue Config Example                                          | v2.0.0                    | | |       |       |       |
34      | Inference Examples    | Generic Image Inference (Raw Output)                                      | v2.0.0                    | | |       |       |       |
35      |                       | Generic Image Inference (with Crop)                                       | v2.0.0                    | | |       |       |       |
36      |                       | Generic Image Inference (with Post Process on Host Side)                  | v2.0.0                    | | |       |       |       |
37      |                       | Generic Image Inference (Multiple Threads)                                | v2.0.0                    | | |       |       |       |
38      |                       | Generic Image Inference (Model in Flash)                                  | v2.0.0                    | | |       |       |       |
39      |                       | Generic Image Inference (Web Cam with Drop Frame)                         | v2.0.0                    | | |       |       |       |
40      |                       | Generic Data Inference (with Pre Process on Host Side)                    | v2.0.0                    | | |       |       |       |
46      | Model Zoo Examples    | Simple examples for pre-trained models                                    |                           | | |       |       | X     | X

**Note**:
- [1] If the minimum version is not written, this feature is supported from v2.1.1.
- [2] If the minimum version is not written, this feature is supported from v2.3.0.
- [3] The official support for KL730 starts on v3.0.0, and only support KL730 model under toolchain version 0.25.0


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

Index   | Category              | Supported Item                                            | Min Version (KL520/KL720) | Min Version (KL630) | Min Version (KL730) | KL520 | KL720 | KL630 | KL730
------- | :-------------------- | :-------------------------------------------------------- | :------------------------ | :------------------ | :------------------ | :---: | :---: | :---: | :---:
1       | Examples              | Update Kdp to Kdp2 Usb Boot                               |                           |                     |                     |       | X     | X     | X
2       |                       | Update Kdp2 to Kdp2 Usb Boot                              |                           | v2.1.1              | v2.3.0              |       | X     |       |
3       |                       | Update Kdp to Kdp2 Flash Boot                             |                           |                     |                     |       |       | X     | X
4       |                       | Update Kdp2 to Kdp2 Flash Boot                            |                           | v2.1.1              | v2.3.0              |       |       |       |
5       |                       | Update Model to Flash                                     |                           | v2.1.1              | v2.3.0              |       |       |       |
