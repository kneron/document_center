## 1. Introduction

In this document, we will introduce the **PLUS** architecture comprising new software(SW) and firmware(FW) design for KL520 (and alpha for KL720).

In comparison with the previous SW/FW architecture, this aims to simplify the design flow for AI applications development.

When referring to a complete AI application development, actually three parts are involved:

- **model development**
- **software development**
- **firmware development**

Below diagram depicts three parts of development in a big picture.

![](./imgs/getting_start_imgs_520_PLUS/KL520_develop_flow.png)

This **Getting Started** document only focuses on host software usage with the AI dongle to perform following functionality.

- **How to build the host software.**
- **How to update the AI dongle to KDP2 firmware loader.**
- **How to list all AI dongles.**
- **How to run the APP inference example.**
- **How to run the generic inference example.**



For **model development**, please refer to the **Toolchain Docker** part.

For **firmware development**, it is more advanced, please contact Kneron.




Below gives some definitions regarding the Kneron PLUS:

- **PLUS** is a software library developed by Kneron and it allows users to manipulate the AI dongle through sophisticated C/C++/Python API.
- **KP** API is part of the PLUS written in C and it provides simplied functions and examples to help users develop their software applications.
- **NEF** represents for **NPU Executable Format** which may comprise one or multiple models and it can only work on Kneron's SoC. The host_lib comes with some NEFs for demonstration purposes. We will use the **Tiny Yolo v3** NEF as the model input in our inference examples.
- **Firmware** is the code responsible for driving Kneron SoC and make it work with the PLUS. The KDP2 firmware can work with the PLUS and it has prebuilt images included in the PLUS.



PLUS contains KP API software code and examples, prebuilt KDP2 firmware and some demonstrative NEF files; and with the AI dongle it can give some edge AI examples.

Here we will demonstrate below diagram scenario with followings:

- A host running Ubuntu
- One Kneron AI dongle.
- The PLUS package.

![](./imgs/getting_start_imgs_520_PLUS/KL520_develop_flow_sw.png)



## 2. Build PLUS

***Note**: here we use Linux-based OS Ubuntu.

Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>, it is located at **KNEO Stem (USB Dongle)/kneron_plus/**.

Before building code, some build tools and packages must be set up for the first time.

Install **CMake**, **libusb-1.0.0-dev** and **build-essential**.
```
$ sudo apt install cmake
$ sudo apt install libusb-1.0-0-dev
$ sudo apt install build-essential
```

Decompress the **kneron_plus_vXXX.zip**.
```
$ unzip kneron_plus_v1.0.0.zip
```

Build code.
```
$ cd kneron_plus/
$ mkdir build ; cd build/
$ cmake ..
$ make -j
```

Once build is done, the **libkplus.so** will be in **build/src/**

Example executables will be in **build/bin/**

Check if PLUS examples are built successfully.
```
$ ls bin/

demo_customize_inf_multiple_models
demo_customize_inf_single_model
generic_inference
scan_device
...
```



## 3. Update AI Dongle to KDP2 Firmware Loader

Before running PLUS examples, users need to make the AI dongle running with the KDP2 firmware loader.

Plug the AI dongle in the Ubuntu host and confirm it with the **'lsusb'** command.

```
$ lsusb
...
Bus 001 Device 002: ID 3231:0100
...

```

If not seeing "3231:0100" (represents KL520 device); "3231:0200"|"3231"0720"(represents KL720 device), it may have a connectivity problem or some device failures.


Download the *KneronDFUT_ubuntu.zip* into Ubuntu from https://www.kneron.com/tw/support/developers/.

```
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

1. Use GUI to Update AI Dongle

    ```
    $ sudo ./KneronDFUT
    ```
    Select the AI dongle to be update to KDP2 firmware, and push **Run** button.

    ![](./imgs/getting_start_imgs_520_PLUS/KneronDFUT.png)

2. Use Command Line to Update AI Dongle

    ```
    $ sudo ./KneronDFUT --help

        [Display help message]
            --help              : help message

        [Scan and list all information]
            --list              : list all dongles' information

        [Upgrade dongles to PLUS]
        If scpu and ncpu firmwares are NOT provided, this process will auto upgrade dongles to KneronPLUS
            --port              : port id set ("all", "auto" or specified multiple port ids "13,537")
            --scpu (optional)   : self pointed scpu firmware file path (.bin)
            --ncpu (optional)   : selp pointed ncpu firmware file path (.bin)

        [Enable Graphic User Interface]
            --gui               : display GUI

    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        517
        Kn Number:      0x270A265C
        Device Type:    KL520
        Connectable:    true
        ===========================================

    $ sudo ./KneronDFUT --port 517

        flash target is 'KDP2 FW Loader'
        it is running KDP FW ...
        updating to K2FL ...
        updating K2FL ... done, try to re-connect it ..
        updating K2FL ... re-connect done
        need helper FW to update OTA configs, uploading ...
        uploading helper FW for OTA config ... done

        ==== Upgrading of Port Id: 517 Succeeded ====

    ```



## 4. List Device Info

While one or multiple AI dongles are plugged into the host, they can be scanned to get some basic device information.

```
$ sudo ./scan_devices

scanning kneron devices ...
number of Kneron devices found: 2

listing devices infomation as follows:

[0] scan_index: '0'
[0] port ID: '517'
[0] product_id: '0x100' (KL520)
[0] USB link speed: 'High-Speed'
[0] USB port path: '1-1-4'
[0] kn_number: '0x270A265C'
[0] Connectable: 'True'
[0] Firmware: 'KDP2 Loader'

[1] scan_index: '1'
[1] port ID: '38'
[1] product_id: '0x100' (KL520)
[1] USB link speed: 'High-Speed'
[1] USB port path: '1-1-5'
[1] kn_number: '0x63252C53'
[1] Connectable: 'True'
[1] Firmware: 'KDP2 Loader'

```

Above shows that it founds two KL520 devices, a brief descript listed below.

- **scan_index** : An index number represents the device in the scanned order, can be used by KP API to establish USB connection.
- **port ID** : An unique number represents the device on the certain usb port, can be used by KP API to establish USB connection.
- **product_id** : The product ID.
- **USB link speed** : USB link speed, High-Speed is fastest speed for USB2.0.
- **USB port path** : This means the physical USB port path on the host.
- **kn_number** : Kneron's serial number for the device.
- **Connectable** : It tells if this device is connectable; one device can only be connected by one program at the same time.
- **Firmware** : This shows which firmware the AI dongle is using, KDP or KDP2 Loader.



## 5. Run Inference Examples

The PLUS provides three categories of API set for model inference.

1. **APP inference** category, providing some decent functions for specific applications with specified NEF models and it is designed to be used in a easy way.

2. **Customized inference** category, providing some decent functions for user to customize their own applications with customized NEF models.

3. **Generic inference** category which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code.

Below will demonstrate only usage in two examples for **APP inference** and **Generic inference**.

### 5.1  App Inference Example

The **'app_yolo_inference'** example utilizes the **APP inference API** and the **Tiny Yolo V3 model** to perform object detection.

When no parameters, it takes **res/models/KL520/tiny_yolo_v3/models_520.nef** as the inference model, **res/images/bike_cars_street_224x224.bmp** as the input image in BMP format and repeats 20 loops to calculate performance then prints inference results.

```
$ sudo ./app_yolo_inference

-h     : help
-target: [target platform] (KL520, KL720) = KL520
-sidx  : [scan index set] = all (all, auto or specified scan index set, can also be "0,1,2" for multiple devices)
-port  : [port id set] = auto (all, auto or specified port id set, can also be "13,537" for multiple devices)
         Notice that scan index has higher priority than port id
-model : [model file path] (.nef) = ../../res/models/KL520/tiny_yolo_v3/models_520.nef
-mid   : [model ID] = auto
-img   : [image file path] = ../../res/images/bike_cars_street_224x224.bmp
-ifmt  : [image file format] = BMP (BMP, RGB565, RGBA8888, YUYV, RAW8)
-iw    : [image width] = auto (only for BMP file)
-ih    : [image height] = auto (only for BMP file)
-loop  : [test loops] = 50

connect target: index '0', port ID '517'

connect 1 device(s) ... OK

upload firmware ... OK
time spent: 0.44 secs

upload model ... OK
time spent: 0.38 secs

this NEF contains 1 model(s):
[1] model ID = 19
[1] model raw input width = 224
[1] model raw input height = 224
[1] model input channel = 3
[1] model raw image format = RGBA8888
[1] model raw output size = 85752


image resolution 224x224

starting doing inference, loop = 50
..................................................

total inference 50 images
time spent: 1.05 secs, FPS = 47.8

class count : 80
box count : 5
Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'

disconnecting device ...

```

Besides output results in the screen console, it also draws detected objects in a new-created **output_bike_cars_street_224x224.bmp**.

![](./imgs/getting_start_imgs_520_PLUS/ex_kdp2_tiny_yolo_v3.bmp)

The key features of APP inference are listed below:
- Specified model NEF.
- Normally post-process is done in SoC.
- Simplfied function parameters.

### 5.2  Generic Inference Example

**Generic inference** API is intended for users who have their own models and applications.

It needs more complex input parameters and normally the post-process is implemented by users in host side.

The **'generic_inference'** is an example for showing how it work.

By default, it runs with a Tiny Yolo v3 model NEF and takes an BMP image as input and does post-process in host side.

Below shortly explains the key input parameters:

- **model file path** : NEF file path, it can be changed to user's own NEF.
- **image file path** : An image file path in BMP format. The actual input format for now supported is RGB565 or RGBA8888.
- **inference model ID** : The model ID of one model in the NEF. Each model should have a unique ID.
- **image format** : This indicates what image format preferred to be converted, the example converts BMP to RGB565 or RGBA888.
- **normalize mode** : Normalize mode depends how data is normalized when training the model.
- **post process** : In PLUS we provide a few post-processing functions, if choosing 'yolo_v3' it use an internal post-processing function for processing yolo_v3 and outputs bounding boxes. For other models, users can use 'none' to diretly get floating point values of each output node.

```

$ sudo ./generic_inference

-h     : help
-target: [target platform] (KL520, KL720) = KL520
-sidx  : [scan index set] = all (all, auto or specified scan index set, can also be "0,1,2" for multiple devices)
-port  : [port id set] = auto (all, auto or specified port id set, can also be "13,537" for multiple devices)
         Notice that scan index has higher priority than port id
-model : [model file path] (.nef) = ../../res/models/KL520/tiny_yolo_v3/models_520.nef
-mid   : [inference model ID] = 19
-img   : [image file path] = ../../res/images/one_bike_many_cars_224x224.bmp
-ifmt  : [image file format] = BMP (BMP, RGB565, RGBA8888, YUYV, RAW8)
-iw    : [image width] = auto (only for BMP file)
-ih    : [image height] = auto (only for BMP file)
-norm  : [normalize mode] (kneron, tensorflow, yolo, customized) = kneron
-pre   : [pre process] (auto, none) = auto
-post  : [post process] (none, yolo_v3, yolo_v5) = yolo_v3
-crop  : [crop boxes] = none
                     (format: (x_left_top, y_left_top, width, height), please quote it with "")
                     (none if crop mechanism is not needed)
-loop  : [test loops] = 50

connect target: index '0', port ID '517'

connect 1 device(s) ... OK

upload firmware ... OK
time spent: 0.91 secs

upload model ... OK
time spent: 0.28 secs

this NEF contains 1 model(s):
[1] model ID = 19
[1] model raw input width = 224
[1] model raw input height = 224
[1] model input channel = 3
[1] model raw image format = RGBA8888
[1] model raw output size = 85752


image resolution 224x224
target inference model ID : 19
allocate memory 85752 bytes for RAW output

starting doing inference, loop = 50
..................................................

total inference 50 images
time spent: 1.04 secs, FPS = 47.9

================== [Post Process] 'yolo_v3' =========================

class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 104.0, 78.0, 141.0, 217.0, 0.949131, 0
Box 1 (x1, y1, x2, y2, score, class) = 106.0, 145.0, 137.0, 214.0, 0.253075, 1
Box 2 (x1, y1, x2, y2, score, class) = 35.0, 49.0, 131.0, 118.0, 0.989020, 2
Box 3 (x1, y1, x2, y2, score, class) = 199.0, 48.0, 221.0, 131.0, 0.916225, 2
Box 4 (x1, y1, x2, y2, score, class) = 129.0, 46.0, 197.0, 95.0, 0.887819, 2
Box 5 (x1, y1, x2, y2, score, class) = 12.0, 30.0, 64.0, 79.0, 0.618796, 2

ouptut bouning boxes on 'output_one_bike_many_cars_224x224.bmp'

===============================================================

disconnecting device ...

```

From the console output, it can be observed that the information of models in the NEF is printed, including model ID, raw resolution, intput channel, raw image format and raw output size.

**Raw output** size indicates that a buffer of the size should be prepared to receive the output directly from the AI dongle, and it cannot be used until converting the raw output to well-structed floating point values.

If [post process] is set to 'yolo_v3', it draws detected objects in a new-created **output_one_bike_many_cars_224x224.bmp**.

![](./imgs/getting_start_imgs_520_PLUS/ex_kdp2_generic_inference_raw.bmp)


Otherwise if [post process] is set to 'none', the example dumps floating point values into **.txt** files for each output node.

```
$ sudo ./generic_inference -post none

-h     : help
-target: [target platform] (KL520, KL720) = KL520
-sidx  : [scan index set] = all (all, auto or specified scan index set, can also be "0,1,2" for multiple devices)
-port  : [port id set] = auto (all, auto or specified port id set, can also be "13,537" for multiple devices)
         Notice that scan index has higher priority than port id
-model : [model file path] (.nef) = ../../res/models/KL520/tiny_yolo_v3/models_520.nef
-mid   : [inference model ID] = 19
-img   : [image file path] = ../../res/images/one_bike_many_cars_224x224.bmp
-ifmt  : [image file format] = BMP (BMP, RGB565, RGBA8888, YUYV, RAW8)
-iw    : [image width] = auto (only for BMP file)
-ih    : [image height] = auto (only for BMP file)
-norm  : [normalize mode] (kneron, tensorflow, yolo, customized) = kneron
-pre   : [pre process] (auto, none) = auto
-post  : [post process] (none, yolo_v3, yolo_v5) = none
-crop  : [crop boxes] = none
                     (format: (x_left_top, y_left_top, width, height), please quote it with "")
                     (none if crop mechanism is not needed)
-loop  : [test loops] = 50

connect target: index '0', port ID '517'

connect 1 device(s) ... OK

upload firmware ... OK
time spent: 0.91 secs

upload model ... OK
time spent: 0.28 secs

this NEF contains 1 model(s):
[1] model ID = 19
[1] model raw input width = 224
[1] model raw input height = 224
[1] model input channel = 3
[1] model raw image format = RGBA8888
[1] model raw output size = 85752


image resolution 224x224
target inference model ID : 19
allocate memory 85752 bytes for RAW output

starting doing inference, loop = 50
..................................................

total inference 50 images
time spent: 1.05 secs, FPS = 47.8

================== [Post Process] 'none' =========================

number of output node : 2

node 0:
width: 7:
height: 7:
channel: 255:
number of data (float): 12495:
first 20 data:
    1.699, 0.340, -0.170, -0.340, -0.340, -0.340,
    -1.019, 1.189, 1.189, 0.679, 0.510,
    0.340, 0.340, 0.510, -0.170, 0.000,
    0.170, 0.170, 0.170, 0.000,

node 1:
width: 14:
height: 14:
channel: 255:
number of data (float): 49980:
first 20 data:
    1.048, 0.000, -0.699, 1.048, 0.175, -0.175,
    0.349, -0.175, 0.349, -0.524, 0.175,
    -0.175, 0.000, -0.349, 1.573, 1.223,
    0.699, 0.874, 0.699, 0.349,

dumped node 0 output to 'output_one_bike_many_cars_224x224_node0_7x7x255.txt'
dumped node 1 output to 'output_one_bike_many_cars_224x224_node1_14x14x255.txt'

===========================================================================

```

For example, **'node0_7x7x255.txt'** represents node 0, width x height x channel = 7x7x255, and its content looks like below.

```
1.699, 0.340, -0.170, -0.340, -0.340, -0.340, -1.019, 1.189, 1.189, 0.679, 0.510, 0.340, 0.340, 0.510, -0.170, 0.000, 0.170, 0.170, 0.170, 0.000, -0.340, -0.340, -0.679, -0.679, -0.849, -0.679, -0.510, 0.000, -7.984, -4.586, -4.247, -4.586, -5.266, -5.266, -8.153, -2.718, -4.416, -4.416, -4.077, -3.397, -3.737, -3.058, -6.115, -7.984, -8.833, -8.663, -9.003, -9.682, -8.323, -1.019, -1.019, -1.529, -1.529, -1.869, -3.227, -4.077, -5.096, -6.115, -7.304, -6.964, -7.304, -8.323, -8.153, -7.304, -10.192, -10.701, -10.022, -9.512, -8.153, -6.285, -1.529, -1.359, -1.189, -1.019, -0.510, 0.170, 0.679, -0.679
....
```
