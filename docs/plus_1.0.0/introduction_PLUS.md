## 1. Introduction

&nbsp;

In order to run the inference of models on Kneron AI dongles, there are three parts of AI application development are required:

- **model development**
- **software development**
- **firmware development**

Below diagram depicts three parts of development in a big picture.

![](./imgs/getting_start_imgs_520_PLUS/KL520_develop_flow.png)

However, this document only focuses on the **software development** and the **firmware development**. For the **model development**, please refer to the **Toolchain Docker** part.

In this document, we will introduce the **PLUS** architecture comprising new software(SW) and firmware(FW) design for KL520 (and alpha for KL720).

In comparison with the previous SW/FW architecture, this aims to simplify the design flow for AI applications development.

Below gives some definitions regarding the Kneron PLUS:

- **PLUS** is a software library developed by Kneron and it allows users to manipulate the AI dongle through sophisticated C/C++/Python API.

- **KP** API is part of the PLUS written in C and it provides simplied functions and examples to help users develop their software applications. For the complete list of KP API, please refer to another document.

- **NEF** represents for **NPU Executable Format** which may comprise one or multiple models and it can only work on Kneron's SoC. The host_lib comes with some NEFs for demonstration purposes. We will use the **Tiny Yolo v3** NEF as the model input in our inference examples.

- **Firmware** is the code responsible for driving Kneron SoC and make it work with the software library. The KDP2 firmware can work with the PLUS and it has prebuilt images included in the PLUS.


The features which PLUS Supported are listed below:

Index   | Category          | Supported Item
------- | :---------------- | :---------------
1       | Image Format      | RGBA8888
2       |                   | RAW8
3       |                   | YUYV422
4       |                   | RGB565
5       | System            | Firmware In Flash
6       |                   | Runtime Upload Firmware
7       |                   | Runtime Upload Model
8       |                   | Software Reset
9       |                   | Scan Devices
10      | Device Connection | Specific Single Dongle
11      |                   | Random Single Dongle
12      |                   | Specific Multilple Dongles
13      |                   | All Dongles
14      | Inference         | Sync Mode Inference
15      |                   | Async Mode Inference
16      |                   | Multiple Dongle Auto Dispatch
17      |                   | Enable / Disable Pre-process on Device
18      |                   | Enable / Disable Post-process on Device
19      | Utility           | Get CRC
20      |                   | Get KN Number
21      |                   | Get Model Info
22      |                   | Get NEF Model Meta Data
23      | Application API   | Tiny Yolo v3
24      |                   | Generic Inference
25      |                   | Customized Inference
26      | Example           | Tiny Yolo v3
27      |                   | Generic Inference (Tiny Yolo v3)
28      |                   | Customized Inference with Single Model (Tiny Yolo v3)
29      |                   | Customized Inference with Multiple Models (Face Detect + Landmark)


The following components are contained in Kneron PLUS:

- KP API
- PLUS examples code
- KDP2 firmware code
- Pre-build firmware binary files
- Some demonstrative NEF files


Here we will demonstrate below diagram scenario with followings:

1. Build and run a PLUS example on host server - Ubuntu 18.04 (Chapter 4).

2. Write a software example and a corresponding firmeware for the customized models (Chapter 5).

    ![](./imgs/getting_start_imgs_520_PLUS/KL520_develop_flow_sw.png)



## 2. Install Dependancy

### 2.1 Ubuntu 18.04 / Raspberry Pi 4

1. Install **CMake**, **libusb-1.0.0-dev** and **build-essential**.

    ```bash
    $ sudo apt install cmake
    $ sudo apt install libusb-1.0-0-dev
    $ sudo apt install build-essential
    ```

### 2.2 Windows 10

1. Kneron AI Dongle Driver

    - Download Zadig application from zadig.akeo.ie appropriate for Windows 10.
    - Connect Kneron KL520 device to your PC.
    - Run the Zadig application.
    - The application should detect Kneron KL520 device as "Kneron KL520" with USB ID
"3231/0100" as shown below:

        ![](./imgs/introduction_PLUS/zadig_install_driver.png)

        (USB ID will be 3231/0200 if KL720 is used.)

    - Make sure that the Driver field, has WinUSB option selected.
    - Click "Install Driver" button.

2. **MSYS2**

    - Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

    - Execute **MSYS2 MinGW 64-bit** to install dependancy.

        ```
        $ pacman -Syu
        $ pacman -Sy
        $ pacman -S base-devel gcc vim cmake
        $ pacman -S mingw-w64-x86_64-libusb
        ```

3. **Keil MDK version 5**

    - Download and install Keil MDK version 5 (at least MDK-Essential) from https://www2.keil.com/mdk5

    - This is used for building the firmware.



## 3. Upgrade Kneron AI Dongle to KDP2 Firmware

**KDP2 Firmware** is the firmware designed for KP APIs in PLUS. Using KDP2 Firmware allows Kneron AI dongle performing corresponding operation requested by PLUS.

There are two kinds of KDP2 firmware are provided:

- **Firmware in Flash Memory**

    - This kind of firmware are stored in the flash memory of Kneron AI dongles.

    - Once the AI dongle is electrified, the firmware will be automatically activated.

    - This kind of firmware can be written to flash memory via the GUI or command line of **KneronDFUT**.

- **Runtime Upload Firmware**

    - This kind of firmware are uploaded and activated after the dongle is electrified.

    - This kind of firmware requires the firmware loader in flash to assist the upload and activation for firmware.

    - The firmware loader can be written to flash memory via the GUI or command line of **KneronDFUT**.

    - The firmware can be uploaded via **kp_load_firmware_from_file()**, a KP API, in the run time.

### 3.1 Write Firmware into Flash Memory

1. Download the KneronDFUT_ubuntu.zip into Ubuntu from https://www.kneron.com/tw/support/developers/.

    ```
    $ unzip KneronDFUT_ubuntu.zip
    $ cd Kneron_DFUT/bin/
    ```

2. Use GUI to Update AI Dongle

    ```bash
    $ sudo ./KneronDFUT
    ```

    - Select **Choose Fimware**.  
    - Manually choose **SCPU firmware file** and **NCPU firmware file**.
    - Select the AI dongles to be updated. and push **Run** button.

    ![](./imgs/introduction_PLUS/dfut_upgrade_firmware_flash.png)

3. Use Command Line to Update AI Dongle

    ```bash 
    $ sudo ./KneronDFUT --help

        [Display help message]
            --help              : help message

        [Scan and list all information]
            --list              : list all dongles' information

        [Upgrade dongles to PLUS]
        If scpu and ncpu firmwares are NOT provided, this process will auto upgrade dongles to KDP2 Firmware Loader
            --port              : port id set ("all", "auto" or specified multiple port ids "13,537")
            --scpu (optional)   : self pointed scpu firmware file path (.bin)
            --ncpu (optional)   : selp pointed ncpu firmware file path (.bin)

        [Enable Graphic User Interface]
            --gui               : display GUI
    ```

    ```bash
    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        517
        Kn Number:      0x270A265C
        Device Type:    KL520
        Connectable:    true
        ===========================================
    ```

    ```bash
    $ sudo ./KneronDFUT --port 517 --scpu ${SCPU_FILE} --ncpu {NCPU_FILE}

        flash target is 'Flash-boot FW'
        it is running KDP FW ...
        updating fw1 buf ...
        updating fw1 buf ... done, try to re-connect it ..
        updating fw1 buf ... re-connect done
        updating fw2 buf ...
        updating fw2 buf ... done, try to re-connect it ..
        updating fw2 buf ... re-connect done

        ==== Upgrading of Port Id: 517 Succeeded ====
    ```

    *The steps for downgrading Kneron AI dongle to previous KDP firmware are the same as writing KDP2 firmware into flash memory.

### 3.2 Write Firmware Loader into Flash Memory

1. Download the KneronDFUT_ubuntu.zip into Ubuntu from https://www.kneron.com/tw/support/developers/.

    ```bash
    $ unzip KneronDFUT_ubuntu.zip
    $ cd Kneron_DFUT/bin/
    ```

2. Use GUI to Update AI Dongle

    ```bash
    $ sudo ./KneronDFUT
    ```

    Select the AI dongle to be update to KDP2 firmware, and push **Run** button.

    ![](./imgs/getting_start_imgs_520_PLUS/KneronDFUT.png)


3. Use Command Line to Update AI Dongle

    ```bash
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
    ```

    ```bash
    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        517
        Kn Number:      0x270A265C
        Device Type:    KL520
        Connectable:    true
        ===========================================
    ```

    ```bash
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



## 4. Run Inference Example

*Note: **Ubuntu 18.04** is used in this chapter.
### 4.1 Build PLUS

Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>, it is located at **KNEO Stem (USB Dongle)/kneron_plus/**

Decompress the **kneron_plus_v1.0.0.zip** 

```bash
$ unzip kneron_plus_v1.0.0.zip
```

Build code

```bash
$ cd kneron_plus/
$ mkdir build ; cd build/
$ cmake ..
$ make -j
```

Once build is done, the **libkplus.so** will be in **build/src/**
Example executables will be in **build/bin/**


Check if PLUS examples are built successfully.

```bash
$ ls bin/

demo_customize_inf_multiple_models
demo_customize_inf_single_model
generic_inference
scan_device
...
```

### 4.2 List Device Info

While one or multiple AI dongles are plugged into the host, they can be scanned to get some basic device information.

```bash
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

### 4.3 Run Inference Examples

The PLUS provides three categories of API set for model inference.

1. **APP inference** category, providing some decent functions for specific applications with specified NEF models and it is designed to be used in a easy way.

2. **Customized inference** category, providing some decent functions for user to customize their own applications with customized NEF models.

3. **Generic inference** category which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code.

Below will demonstrate only usage in two examples for **APP inference** and **Generic inference**.

#### 4.3.1 App Inference Example

The **'app_yolo_inference'** example utilizes the **APP inference API** and the **Tiny Yolo V3 model** to perform object detection.

When no parameters, it takes **res/models/KL520/tiny_yolo_v3/models_520.nef** as the inference model, **res/images/bike_cars_street_224x224.bmp** as the input image in BMP format and repeats 20 loops to calculate performance then prints inference results.

```bash
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

#### 4.3.2 Generic Inference Example

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

    ```bash
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
    ```


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
    
    output bounding boxes on 'output_one_bike_many_cars_224x224.bmp'
    ===========================================================================
    
    disconnecting device ...
    ```

From the console output, it can be observed that the information of models in the NEF is printed, including model ID, raw resolution, intput channel, raw image format and raw output size.

**Raw output** size indicates that a buffer of the size should be prepared to receive the output directly from the AI dongle, and it cannot be used until converting the raw output to well-structed floating point values.


If [post process] is set to 'yolo_v3', it draws detected objects in a new-created **output_one_bike_many_cars_224x224.bmp**.

![](./imgs/getting_start_imgs_520_PLUS/ex_kdp2_generic_inference_raw.bmp)


Otherwise if **post process** is set to 'none', the example dumps floating point values into **.txt** files for each output node.

```bash
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

```bash
1.699, 0.340, -0.170, -0.340, -0.340, -0.340, -1.019, 1.189, 1.189, 0.679, 0.510, 0.340, 0.340, 0.510, -0.170, 0.000, 0.170, 0.170, 0.170, 0.000, -0.340, -0.340, -0.679, -0.679, -0.849, -0.679, -0.510, 0.000, -7.984, -4.586, -4.247, -4.586, -5.266, -5.266, -8.153, -2.718, -4.416, -4.416, -4.077, -3.397, -3.737, -3.058, -6.115, -7.984, -8.833, -8.663, -9.003, -9.682, -8.323, -1.019, -1.019, -1.529, -1.529, -1.869, -3.227, -4.077, -5.096, -6.115, -7.304, -6.964, -7.304, -8.323, -8.153, -7.304, -10.192, -10.701, -10.022, -9.512, -8.153, -6.285, -1.529, -1.359, -1.189, -1.019, -0.510, 0.170, 0.679, -0.679
....
```


## 5. Run Costomized Models

In order to run customized models on Kneron AI dongle, there are four stages are involved:

- **Model Development**

    This will not be introduced in this document.

- **PLUS Development**

    The software interface for sending requests to firmware and receiving results from firmware.

- **SCPU Firmware Development**

    The entry of the firmware. Which models should be run on NCPU Firmware and in what sequence should these models run are determined in SCPU Firmware.

- **NCPU Firmware Development**

    Where models actually run. Besides the model inference, the preprocess and the postprocess can be chosen to run on NCPU Firmware.

&nbsp;

The diagram below demostrates the inference flow for every models runnig on Kneron AI dongle, and how the PLUS, SCPU, and NCPU interact with each other.

![](./imgs/customize_api_520_PLUS/customized_api_develop_flow.png)


### 5.1 PLUS Development for Face Detect + Landmark

1. Create my_example folder

    ```bash
    $ cd {PLUS_FOLDER_PATH}/examples/
    $ mkdir my_example
    ```

2. Add CMakelists.txt

    ```bash
    # build with current *.c/*.cpp plus common source files in parent folder
    # executable name is current folder name.

    get_filename_component(app_name ${CMAKE_CURRENT_SOURCE_DIR} NAME)
    string(REPLACE " " "_" app_name ${app_name})

    file(GLOB local_src
        "*.c"
        "*.cpp"
        )

    set(common_src
        ../common/helper_functions.c
        )

    add_executable(${app_name}
        ${local_src}
        ${common_src})

    target_link_libraries(${app_name} ${KPLUS_LIB_NAME} ${USB_LIB} ${MATH_LIB} pthread)
    ```

3. Add my_example.h

    - Please define the customized **header** structure and customized **result** structure in this file.

    - Header (my_example_header_t) is used for **sending** data to SCPU firmware. What kind of data should be contained can be customized based on the your requirement.

    - Result (my_example_result_t) is used for **receiving** data from SCPU firmware. What kind of data should be contained can be customized based on the output of model inference.

    - **kp_inference_header_stamp_t** must be contained in both header and result structures.

    - The **JOB_ID** describes the unique id of the task you want to execute in firmware, and it must be unique and above 1000.

    - This file should be synchronized with the .h file in SCPU firmware.
    ```c
    #pragma once

    #define MY_EXAMPLE_JOB_ID           1003
    #define FD_MAX                      10

    typedef struct
    {
        kp_bounding_box_t fd;                 /**< fd result */
        kp_landmark_result_t lm;              /**< lm result */
    } __attribute__((aligned(4))) one_face_data_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_example_header_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t face_count;
        one_face_data_t faces[FD_MAX];
    } __attribute__((aligned(4))) my_example_result_t;
    ```

4. Add my_example.c

    - There are 6 steps for inferencing in Kneron AI dongle:

        1. Connect Kneron AI dongle.

        2. Upload the firmware to AI dongle.

        3. Upload the model to AI dongle.

        4. Prepare data for the header.

        5. Send the header and image buffer to SCPU firmware via **kp_customized_inference_send()**.

        6. Receive the result from SCPU firmware via **kp_customized_inference_receive()**.

    - In this example, the **image** is transcoded into RGB565, and the width and height of the image is carried by the header.

    - Sending header and receiving result can be executed sequentially or on two different threads.
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>

    #include "kp_core.h"
    #include "kp_inference.h"
    #include "helper_functions.h"

    #include "my_example.h"

    static char _scpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_scpu.bin";
    static char _ncpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_ncpu.bin";
    static char _model_file_path[128] = "../../res/models/KL520/ssd_fd_lm/models_520.nef";
    static char _image_file_path[128] = "../../res/images/a_woman_640x480.bmp";
    static int _loop = 10;

    int main(int argc, char *argv[])
    {
        kp_device_group_t device;
        kp_model_nef_descriptor_t model_desc;
        int ret;

        /******* connect the device *******/
        {
            int port_id = 0; // 0 for one device auto-search
            int error_code;

            // internal parameter to indicate the desired port id
            if (argc > 1) {
                port_id = atoi(argv[1]);
            }

            // connect device
            device = kp_connect_devices(1, &port_id, &error_code);
            if (!device) {
                printf("error ! connect device failed, port ID = '%d', error = '%d'\n", port_id, error_code);
                exit(0);
            }

            kp_set_timeout(device, 5000);
            printf("connect device ... OK\n");
        }

        /******* upload firmware to device *******/
        {
            ret = kp_load_firmware_from_file(device, _scpu_fw_path, _ncpu_fw_path);
            if (KP_SUCCESS != ret) {
                printf("error ! upload firmware failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload firmware ... OK\n");
        }

        /******* upload model to device *******/
        {
            ret = kp_load_model_from_file(device, _model_file_path, &model_desc);
            if (KP_SUCCESS != ret) {
                printf("error ! upload model failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload model ... OK\n");
        }

        /******* prepare the image buffer read from file *******/
        // here convert a bmp file to RGB565 format buffer

        int img_width, img_height;
        char *img_buf = helper_bmp_file_to_raw_buffer(_image_file_path, &img_width, &img_height, KP_IMAGE_FORMAT_RGB565);

        if (!img_buf) {
            printf("error ! read image file failed\n");
            exit(0);
        }

        printf("read image ... OK\n");
        printf("\nstarting inference loop %d times:\n", _loop);

        /******* prepare input and output header/buffers *******/
        my_example_header_t input_header;
        my_example_result_t output_result;

        input_header.header_stamp.job_id = MY_EXAMPLE_JOB_ID;
        input_header.img_width = img_width;
        input_header.img_height = img_height;

        int header_size = sizeof(my_example_header_t);
        int image_size = img_width * img_height * 2; // RGB565
        int result_size = sizeof(my_example_result_t);
        int recv_size = 0;

        /******* starting inference work *******/

        for (int i = 0; i < _loop; i++) {
            ret = kp_customized_inference_send(device, (void *)&input_header, header_size, (uint8_t *)img_buf, image_size);

            if (KP_SUCCESS != ret) {
                printf("\ninference failed, error = %d\n", ret);
                break;
            }

            ret = kp_customized_inference_receive(device, (void *)&output_result, result_size, &recv_size);

            if (KP_SUCCESS != ret) {
                printf("\ninference failed, error = %d\n", ret);
                break;
            }

            printf("\n[loop %d]\n", i + 1);

            for (int j = 0; j < output_result.face_count; j++) {
                printf("\nFace %d (x1, y1, x2, y2, score) = %d, %d, %d, %d, %f\n", j + 1
                                                                                 , (int)output_result.faces[j].fd.x1
                                                                                 , (int)output_result.faces[j].fd.y1
                                                                                 , (int)output_result.faces[j].fd.x2
                                                                                 , (int)output_result.faces[j].fd.y2
                                                                                 , output_result.faces[j].fd.score);

                for (int k = 0; k < LAND_MARK_POINTS; k++) {
                    printf("    - Landmark %d: (x, y) = %d, %d\n", k + 1
                                                                 , output_result.faces[j].lm.marks[k].x
                                                                 , output_result.faces[j].lm.marks[k].y);
                }
            }
        }

        printf("\n");

        free(img_buf);
        kp_disconnect_devices(device);

        return 0;
    }
    ```


### 5.2 SCPU Firmware Development for Face Detect + Landmark

1. Go to SCPU App Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app

2. Add my_example_inf.h

    - The content of this file should be synchronized with **my_example.h** in PLUS.
    ```c
    #pragma once

    #define MY_EXAMPLE_JOB_ID           1003
    #define FD_MAX                      10

    typedef struct
    {
        kp_bounding_box_t fd;                 /**< fd result */
        kp_landmark_result_t lm;              /**< lm result */
    } __attribute__((aligned(4))) one_face_data_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_example_header_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t face_count;
        one_face_data_t faces[FD_MAX];
    } __attribute__((aligned(4))) my_example_result_t;
    ```

3. Add my_example_inf.c

    - There are 8 steps for inferencing in face detect model and landmark model:

        1. Prepare the memory space for the result.

        2. Prepare header of output result.

        3. Prepare the temporary memory space for the result of middle model via **kmdw_ddr_reserve()**

        4. Prepare **kdp2_inference_config_t** for face detect model, which is used for configure the inference in NCPU firmware.

        5. Activate NCPU firmware for face detect model via **kdp2_inference_start()**.

        6. Prepare **kdp2_inference_config_t** for landmark model.

        7. Activate NCPU firmware for landmark model via **kdp2_inference_start()**.

        8. Send the result to PLUS via **kdp2_inference_send_result()**.

    - For the customized model, **model_id** of **kdp2_inference_config_t** should be set to the id of the customized model.

    - The inference result of NCPU will be written to **ncpu_result_buf** of **kdp2_inference_config_t**. Therefore, you must provide a memory space for it (In this example, **ncpu_result_buf** is pointed to **fd_result** for face detect model, and **lm_result** for landmark model.)

    - For the detail of **kdp2_inference_config_t**, please refer to section **6.4 Firmware Configuration**

    ```c
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "model_type.h"
    #include "model_res.h"
    #include "kmdw_console.h"

    #include "kmdw_inference.h"
    #include "my_example_inf.h"

    #define TY_MAX_BOX_NUM (50)
    #define FACE_SCORE_THRESHOLD 0.8f

    // for face detection result, should be in DDR
    static struct yolo_result_s *fd_result = NULL;

    static int inference_face_detection(my_example_header_t *input_header,
                                        struct yolo_result_s *fd_result /* output */)
    {
        /******* Prepare the configuration *******/

        kmdw_inference_config_t inf_config;

        // Set the initial value of config to 0, false and NULL
        memset(&inf_config, 0, sizeof(kmdw_inference_config_t));

        // image buffer address should be just after the header
        inf_config.image_buf = (void *)((uint32_t)input_header + sizeof(my_example_header_t));
        inf_config.image_width = input_header->img_width;
        inf_config.image_height = input_header->img_height;
        inf_config.image_channel = 3;                                       // assume RGB565
        inf_config.image_format = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_norm = KP_NORMALIZE_KNERON;                        // this depends on model
        inf_config.model_id = KNERON_FD_MASK_MBSSD_200_200_3;               // this depends on model
        inf_config.enable_preprocess = true;                                // enable preprocess in ncpu/npu

        // set up fd result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)fd_result;

        /******* Activate inferencing in NCPU *******/

        return kmdw_inference_start(&inf_config);
    }

    static int inference_face_landmarks(my_example_header_t *input_header,
                                        struct bounding_box_s *face_box,
                                        kp_landmark_result_t *lm_result /* output */)
    {
        /******* Prepare the configuration *******/

        kmdw_inference_config_t inf_config;

        // Set the initial value of config to 0, false and NULL
        memset(&inf_config, 0, sizeof(kmdw_inference_config_t));

        int32_t left = (int32_t)(face_box->x1);
        int32_t top = (int32_t)(face_box->y1);
        int32_t right = (int32_t)(face_box->x2);
        int32_t bottom = (int32_t)(face_box->y2);

        // image buffer address should be just after the header
        inf_config.image_buf = (void *)((uint32_t)input_header + sizeof(my_example_header_t));
        inf_config.image_width = input_header->img_width;
        inf_config.image_height = input_header->img_height;
        inf_config.image_channel = 3;                                       // assume RGB565
        inf_config.image_format = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_norm = KP_NORMALIZE_KNERON;                        // this depends on model
        inf_config.model_id = KNERON_LM_5PTS_ONET_56_56_3;                  // this depends on model
        inf_config.enable_crop = true;                                      // enable crop image in ncpu/npu
        inf_config.enable_preprocess = true;                                // enable preprocess in ncpu/npu

        // set crop box
        inf_config.crop_area.crop_number = 0;
        inf_config.crop_area.x1 = left;
        inf_config.crop_area.y1 = top;
        inf_config.crop_area.width = right - left;
        inf_config.crop_area.height = bottom - top;

        // set up landmark result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)lm_result;

        /******* Activate inferencing in NCPU *******/

        return kmdw_inference_start(&inf_config);
    }

    static bool init_temp_buffer()
    {
        // allocate DDR memory for ncpu/npu output restult
        fd_result = (struct yolo_result_s *)kmdw_ddr_reserve(sizeof(struct yolo_result_s) + TY_MAX_BOX_NUM * sizeof(struct bounding_box_s));

        if (fd_result == NULL) {
            return false;
        }

        return true;
    }

    void my_example_inf(void *inf_input_buf)
    {
        my_example_header_t *input_header = (my_example_header_t *)inf_input_buf;

        /******* Prepare the memory space of result *******/

        int result_buf_size = sizeof(my_example_result_t);
        void *inf_result_buf = kmdw_inference_request_result_buffer(&result_buf_size);
        my_example_result_t *output_result = (my_example_result_t *)inf_result_buf;

        /******* Prepare header of output result *******/

        output_result->header_stamp.magic_type = KDP2_MAGIC_TYPE_INFERENCE;
        output_result->header_stamp.total_size = sizeof(my_example_result_t);
        output_result->header_stamp.job_id = MY_EXAMPLE_JOB_ID;

        /******* Prepare the temporary memory space for the result of middle model *******/

        static bool is_init = false;

        if (!is_init) {
            int status = init_temp_buffer();
            if (!status) {
                // notify host error !
                output_result->header_stamp.status_code = KP_FW_DDR_MALLOC_FAILED_102;
                kmdw_inference_send_result((void *)output_result);
                return;
            }

            is_init = true;
        }

        /******* Run face detect model *******/

        int inf_status = inference_face_detection(input_header, fd_result);

        if (inf_status != KP_SUCCESS) {
            // notify host error !
            output_result->header_stamp.status_code = inf_status;
            kmdw_inference_send_result((void *)output_result);
            return;
        }

        int face_cnt = 0;
        int max_face = (fd_result->box_count > FD_MAX) ? FD_MAX : fd_result->box_count;

        /******* Run landmark model for every faces *******/

        for (int i = 0; i < max_face; i++) {
            struct bounding_box_s *face_box = &fd_result->boxes[i];
            kp_landmark_result_t *face_lm_result = &output_result->faces[face_cnt].lm;

            if (FACE_SCORE_THRESHOLD < face_box->score) {
                // do face landmark for each faces
                inf_status = inference_face_landmarks(input_header, face_box, face_lm_result);

                if (KP_SUCCESS != inf_status) {
                    // notify host error !
                    output_result->header_stamp.status_code = inf_status;
                    kmdw_inference_send_result((void *)output_result);
                    return;
                }

                // skip it if face lm is not good
                if (0.99f > face_lm_result->score) {
                    continue;
                }

                memcpy(&output_result->faces[face_cnt].fd, face_box, sizeof(kp_bounding_box_t));
                face_cnt++;
            }
        }

        /******* Send the result to PLUS *******/

        output_result->face_count = face_cnt;
        output_result->header_stamp.status_code = KP_SUCCESS;

        kmdw_inference_send_result((void *)output_result);
    }
    ```

4. Go to SCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/project/scpu_companion_user_ex/main

4. Edit main.c

    - **_app_entry_func** is the entry interface for all inference request.

    - Inference jobs will be dispatched to the coresponding function based on the **job_id** in **kp_inference_header_stamp_t** in the header.

    - You need to establish a switch case for **MY_EXAMPLE_JOB_ID** and corespond the switch case to **my_example_inf()**.

    ```c
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "kp_struct.h"
    #include "kmdw_inference.h"

    #include "kdp2_inf_app_yolo.h"
    #include "demo_customize_inf_single_model.h"
    #include "demo_customize_inf_multiple_models.h"
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    #include "my_example_inf.h"
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    extern void SystemCoreClockUpdate(void);

    /* Kneron usb companion interface implementation to work with PLUS host SW */
    extern void kdp2_usb_companion_init(void);
    extern void main_init_usboot(void);

    /* declare inference code implementation here */
    extern void kdp2_app_yolo_inference(void *inf_input_buf);            // kdp2_inf_app_yolo.c
    extern void demo_customize_inf_single_model(void *inf_input_buf);    // demo_customize_inf_single_model.c
    extern void demo_customize_inf_multiple_models(void *inf_input_buf); // demo_customize_inf_multiple_models.c
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    extern void my_example_inf(void *inf_input_buf);
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    static void _app_entry_func(void *inf_input_buf)
    {
        // check header stamp
        kp_inference_header_stamp_t *header_stamp = (kp_inference_header_stamp_t *)inf_input_buf;

        switch (header_stamp->job_id)
        {
        case KDP2_INF_ID_APP_YOLO:
            kdp2_app_yolo_inference(inf_input_buf);
            break;
        case DEMO_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from one model
            demo_customize_inf_single_model(inf_input_buf);
            break;
        case DEMO_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from two models
            demo_customize_inf_multiple_models(inf_input_buf);
            break;
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        case MY_EXAMPLE_JOB_ID:
            my_example_inf(inf_input_buf);
            break;
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */
        default:
            kmdw_inference_send_error_code(0, KP_FW_ERROR_UNKNOWN_APP);
            break;
        }
    }

    /**
    * @brief main, main function
    */
    int main(void)
    {
        SystemCoreClockUpdate(); // System Initialization
        osKernelInitialize();    // Initialize CMSIS-RTOS

        /* SDK main init for companion mode */
        main_init_usboot();

        /* initialize inference core threads and memory with user-specified app entry function */
        kmdw_inference_init(_app_entry_func);

        /* start an interface implementation as input/ouput to co-work with inference framework */
        // this can be changed by other interface implementation
        kdp2_usb_companion_init();

        /* Start RTOS Kernel */
        if (osKernelGetState() == osKernelReady)
        {
            osKernelStart();
        }

        while (1)
        {
        }
    }
    ```

### 5.3 NCPU Firmware Development for The Pre-process and Post-process


If the customized models need a customized pre-process or post-process on Kneron AI dongle, you can add the pre-process and post-process in the following files.

1. Go to NCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/ncpu_kdp2/project/ncpu_companion_user_ex/main/

2. Add your customized pre-process function into **user_pre_process.c**

3. Add your customized post-process function into **user_post_process.c**

4. Edit **main.c**

    - Register your customized pre-process by **kdpio_pre_processing_register()**.

    - Register your customized post-process by **kdpio_post_processing_register()**.

    - Once pre-process and post-process are registered, they will automatically execute before and after the inference of model.

    - The pre-process and post-process for certain model are specified by the model Id.


### 5.4 Firmware Configuration

When SCPU activates NCPU to run models, **kdp2_inference_config_t**, which contains configurations of NCPU, is required to pass to NCPU.

**kdp2_inference_config_t** contains following configurable options:

- void* **image_buf**:
    - The buffer address of the image.

- uint32_t **image_width**:
    - The width of the image.

- uint32_t **image_height**:
    - The height of the image.

- uint32_t **image_channel**:
    - The channel count of the image.

- uint32_t **image_format**:
    - This is used for color space conversion in pre-process.
    - Please refer to **kp_image_format_t**.

- uint32_t **image_norm**:
    - This is used for data normalization in pre-process.
    - Please refer to **kp_normalize_mode_t**.

- int **model_id**:
    - The ID of the target model to be inferenced in NCPU.

- bool **enable_crop**:
    - Whether crop a partial area of the image to be inferenced.
    - If this is true, **crop_area** must be set properly.

- kp_inf_crop_box_t **crop_area**:
    - The cropping area of the image to be inferrenced.

- bool **enable_raw_output**:
    - If this is true, NCPU does not execute the post-process. The post-process may need to be execute at the software on the host server.
    - If this is false, NCPU will execute the post-process. The customized post-process must be registered via **kdpio_post_processing_register()**.

- bool **enable_parallel**:
    - This is only available when single model is adapted and the post-process is executed in NCPU.
    - When one inference is in the post-process, the next inference will be start parallelly.
    - After one inference is fully finished, the callback function set to **result_callback** will be invoked.

- kmdw_inference_result_callback_t **result_callback**:
    - The callback function for parallel mode

- bool **enable_preprocess**:
    - If this is true, NCPU will execute the pre-process. The customized post-process must be registered via **kdpio_pre_processing_register()**.
    - The pre-process are including color space converion, resolution scaling, normalization, ... etc.
    - If this is false, NCPU does not execute the pre-process. The size, channel, format, ... of the input image should be exactly the same as the requirement of the model.

- void* **inf_result_buf**:
    - This only works for parallel mode to carry it back to user callback function.

- void* **ncpu_result_buf**
    - The buffer address where NCPU put the inference result.
    - It will be passed to **result_callback** under parallel mode.

- kp_pad_value_t* **pad_value**:
    - The pad_value for the pre-processing in NCPU.

- void* **user_define_data**
    - The user define data for the pre-processing in NCPU.


### 5.5 Build and Execute My Example

*Note: **Windows 10** is used in this chapter.
#### 5.5.1 Build Firmware

1. Execute Keil uVision5

2. Select **Project** > **Open Project...**

3. Choose {PLUS_FOLDER_PATH}/firmware_development/KL520/example_projects/kdp2_companion_user_ex/workspace.uvmpw

4. Expand **Project: kdp2_scpu** in left panel

5. Right click on **app** and choose **Add Existing Files to Group 'kdp2_inference'...**

6. Select {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app/my_example_inf.c

7. Select **Project** > **Batch Build**

*If build succeeded, **kdp2_fw_scpu.bin** and **kdp2_fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL520/

![](./imgs/customize_api_520_PLUS/keil_build_firmware.png)

#### 5.5.2 Build PLUS and Execute My Example

Build and Execute my_example of PLUS in **MSYS2 MinGW 64-bit**

```bash
$ cd {PLUS_FOLDER_PATH}
$ mkdir build
$ cd build
$ cmake .. -G "MSYS Makefiles"
$ make -j
$ cd bin
$ ./my_example.exe

    connect device ... OK
    upload firmware ... OK
    upload model ... OK
    read image ... OK

    starting inference loop 10 times:

    [loop 1]

    Face 1 (x1, y1, x2, y2, score) = 224, 112, 379, 280, 0.999319
        - Landmark 1: (x, y) = 263, 167
        - Landmark 2: (x, y) = 328, 177
        - Landmark 3: (x, y) = 282, 214
        - Landmark 4: (x, y) = 256, 237
        - Landmark 5: (x, y) = 319, 245

    [loop 2]

    Face 1 (x1, y1, x2, y2, score) = 224, 112, 379, 280, 0.999319
        - Landmark 1: (x, y) = 263, 167
        - Landmark 2: (x, y) = 328, 177
        - Landmark 3: (x, y) = 282, 214
        - Landmark 4: (x, y) = 256, 237
        - Landmark 5: (x, y) = 319, 245

    [loop 3]

    ...
```
