# Getting Started

**Note**: We built and run the examples below under OS Ubuntu 18.04.5 LTS with cmake version 3.10.2.

## 1. Introduction

In this document, we will introduce **Kneron PLUS** (*Platform Library Unified Software*) framework to demostrate the usage of Kneron AI dongle from host software. When referring to a complete AI application development, actually three parts are involved:

- **model development**
- **software development**
- **firmware development**

This **Getting Started** document only focuses on host software usage with the AI dongle to perform following functionality.

- **How to upgrade the AI dongle to KDP2 firmware loader.**
- **How to build the software package**
- **How to run the APP Yolo inference example.**

For **model development**, please refer the **Toolchain Docker** part.

For **firmware development**, please refer the documents in Customized API folder.

## 2. Update AI Dongle to KDP2 Firmware Loader

Before running PLUS examples, users need to make the AI dongle running with the KDP2 firmware loader.

Download the *KneronDFUT_ubuntu.zip* into Ubuntu in from https://www.kneron.com/tw/support/developers/. It is located at **Kneron PLUS** section.

```bash
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

1. Use GUI to Update AI Dongle

    ```bash
    $ sudo ./KneronDFUT
    ```

    Select the AI dongle to be update to KDP2 firmware, and push **Run** button.

    ![](./imgs/dfut_upgrade_firmware_loader.png)

2. Use Command Line to Update AI Dongle

    ```bash
    $ sudo ./KneronDFUT --help

        [Display help message]
            --help                : [no argument]         help message

        [Scan and list all information]
            --list                : [no argument]         list all dongles information

        [Update dongles to usb loader] (Only works for KL520)
            --usb                 : [no argument]         choose update to Usb Loader
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Update firmware file to flash memory in dongles
            --type                : [argument required]   type of firmware ("KL520" or "KL720")
            --scpu                : [argument required]   self pointed scpu firmware file path (.bin)
            --ncpu                : [argument required]   selp pointed ncpu firmware file path (.bin)
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Enable Graphic User Interface]
            --gui                 : [no argument]         display GUI
    ```

    ```bash
    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        517
        Kn Number:      0x270A265C
        Device Type:    KL520
        FW Type:        KDP
        Connectable:    true
        ===========================================
    ```

    ```bash
    $ sudo ./KneronDFUT --port 517 --usb

        Start Update Device with Port Id 517 to USB Loader

        ==== Update of Device with Port Id: 517 Succeeded ====
    ```


## 3. Build PLUS

**Note**: we use Ubuntu 18.04.5 LTS with cmake version 3.10.2

Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

Before building code, some build tools and packages must be set up for the first time.

Install **CMake**, **libusb-1.0.0-dev** and **build-essential**.

```bash
$ sudo apt install cmake
$ sudo apt install libusb-1.0-0-dev
$ sudo apt install build-essential
```

Decompress the **kneron_plus_vXXX.zip**.

```bash
$ unzip kneron_plus_vX.X.X.zip
```

Build code.

```bash
$ cd kneron_plus/
$ mkdir build
$ cd build/
$ cmake ..
$ make -j
```

Once build is done, the **libkplus.so** will be in **build/src/**

Example executables will be in **build/bin/**

Check if PLUS examples are built successfully.

```bash
$ ls bin/

    kl520_demo_app_yolo_inference
    kl520_demo_app_yolo_inference_multithread
    kl520_demo_customize_inf_multiple_models
    kl520_demo_customize_inf_single_model
    kl520_demo_generic_inference
    ...
```

## 4. Run App Yolo Inference

```bash
$ sudo ./kl520_demo_app_yolo_inference

    connect device ... OK
    upload firmware ... OK
    upload model ... OK
    read image ... OK

    starting inference loop 100 times:
    .......................................
    class count : 80
    box count : 5
    Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
    Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
    Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
    Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
    Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2

    output bounding boxes on 'output_bike_cars_street_224x224.bmp'

```

Besides output results in the screen console, it also draws detected objects in a new-created **output_bike_cars_street_224x224.bmp**.

![](./imgs/ex_kdp2_tiny_yolo_v3.bmp)
