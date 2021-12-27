# Run Inference Examples

The provided examples are designed to show how to use KP APIs and present Kneron Device features. Error handling, wording and application layer features are not covered. They are open for more creatives.

**Note**: If you are using Windows, please execute all the instruction below in MSYS2 MinGW 64-bit.

**Note**: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

**Note**: In the inference related examples, we are using KL520 for most demo. If you wish to use KL720, just change the prefix of the example name from kl520 to kl720.

**Note**: Few examples will auto connect multiple devices to run inference. If you put hybrid types of devices on host, the inference may fail.

**Note**: If you modify code to change different test image file. Input image aspect ratio is suggested to be aligned to model input aspect ratio.

**Note**: Reference to [Yolo Object Name Mapping](./yolo_object_name_mapping.md) for the detection result classes of YOLO examples.

---

## Build PLUS

1. Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

2. Decompress the **kneron_plus_vXXX.zip**

    ```bash
    $ unzip kneron_plus_vX.X.X.zip
    ```

3. Build code

    If you are using Ubuntu:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j
    ```
    **Note**: if you also want to build OpenCV examples at this moment,
    please adjust cmake command as following
    ```bash
    $ cmake -DWITH_OPENCV=ON ..
    ```

    If you are using MSYS2 MinGW 64-bit in Windows:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake .. -G"MSYS Makefiles"
    $ make -j
    ```
    **Note**: if you also want to build OpenCV examples at this moment,
    please adjust cmake command as following
    ```bash
    $ cmake -DWITH_OPENCV=ON .. -G"MSYS Makefiles"
    ```

    **Note**: Some examples may cause warnings during cmake process due to the length of the paths. You can rename these examples to shorter names to avoid these warnings.

    - Once build is done, the **libkplus.so** will be in **build/src/**

    - Example executables will be in **build/bin/**

4. Check if PLUS examples are built successfully.

    ```bash
    $ ls bin/

        kl520_demo_customize_inf_multiple_models
        kl520_demo_customize_inf_single_model
        kl520_demo_generic_inference
        ...
    ```

---

## 1. System Examples

### 1.1 Scan Device Example

Note: This example is to show the usage of `kp_scan_devices()`.

While one or multiple AI devices are plugged into the host, they can be scanned to get some basic device information.

```bash
$ sudo ./scan_devices
```

```bash
scanning kneron devices ...
number of Kneron devices found: 2

listing devices information as follows:

[0] scan_index: '0'
[0] port ID: '517'
[0] product_id: '0x100' (KL520)
[0] USB link speed: 'High-Speed'
[0] USB port path: '1-1-4'
[0] kn_number: '0x270A265C'
[0] Connectable: 'True'
[0] Firmware: 'KDP'

[1] scan_index: '1'
[1] port ID: '38'
[1] product_id: '0x100' (KL520)
[1] USB link speed: 'High-Speed'
[1] USB port path: '1-1-5'
[1] kn_number: '0x63252C53'
[1] Connectable: 'True'
[1] Firmware: 'KDP2 Loader'
```

Above shows that it founds two KL520 devices, a brief description listed below.

- **scan_index** : An index number represents the device in the scanned order, can be used by KP API to establish USB connection.
- **port ID** : An unique number represents the device on the certain usb port, can be used by KP API to establish USB connection.
- **product_id** : The product ID.
- **USB link speed** : USB link speed, High-Speed is speed for USB2.0. Super-Speed is speed for USB3.0.
- **USB port path** : This means the physical USB port path on the host.
- **kn_number** : Kneron's serial number for the device.
- **Connectable** : It tells if this device is connectable; one device can only be connected by one program at the same time.
- **Firmware** : This shows which firmware the AI device is using, KDP or KDP2 Loader.

---

### 1.2 Connect Device Example

This example is to show the usage of `kp_device_group_t`, `kp_connect_device()` and different filter ways of finding target devices to connect. Furthermore, the `kp_device_group_t` is a working unit to be operated in **Kneron PLUS API**.

Notice that it is not allowed to connect different target platform devices into a deivce group.

```bash
sudo ./connect_devices --help
```

```bash
connect_devices example

  show different filter ways of finding target devices to connect
  Notice that it is not allowed to connect different target platform devices into a device group

Arguments:
-help, h   : print help message
-target, t : [by target platform] = (KL520|KL720)
-sidx, s   : [by scan index set] = (specified scan index set, can also be "0,1,2" for multiple devices)
-port, p   : [by port id set] = (specified port id set, can also be "13,537" for multiple devices)
-kn, k     : [by KN number set] = (specified KN number set, scan also be "0x1111aaaa, 0x2222bbbb" for multiple devices)
```

- **target**: using the target platform (KL520 or KL720) to connect.
- **sidx**: using the specified scan index set to connect.
- **port**: using the port id set to connect.
- **kn**: using the KN number set to connect.

---

### 1.3 Install Driver for Windows Example

Note: This example is to show the usage of `kp_install_driver_for_windows()` and help users to install driver to Windows directly.

Note: This example is only available on Windows 10, and it must be run as Administrator.

1. For installing the driver for KL520:

    ```bash
    $ ./install_driver_windows.exe -target KL520
    ```

    ```bash
    [arguments]
    -h     : help
    -target: [target platform] (ALL, KL520, KL720) = KL520

    [note]
        You must run this app as administrator on Windows

    Installing driver for KL520 ... Success (0)
    ```

2. For installing the driver for KL720:

    ```bash
    $ ./install_driver_windows.exe -target KL720
    ```

    ```bash
    [arguments]
    -h     : help
    -target: [target platform] (ALL, KL520, KL720) = KL720

    [note]
        You must run this app as administrator on Windows

    Installing driver for KL720 ... Success (0)
    ```

### 1.4 Load Firmware and Model Example

`kp_load_firmware_from_file()` is an API to load firmware file from host to the AI device via USB. And this API is only available on KL520 (USB Boot Mode). Please refer [Upgrade AI Device To KDP2](./upgrade_ai_device_to_kdp2.md) for more information.

`kp_load_model_from_file()` is an API to load model file from host to the AI device via USB. Please refer [Write Model to Flash](./write_model_to_flash.md) for more information.

`kp_load_model_from_flash()` is an API to load model from the flash memory of the AI device. Please refer [2.1.5 Generic Inference Using Model in Flash](#215-generic-inference-using-model-in-flash) and [Write Model to Flash](./write_model_to_flash.md) for more information.


### 1.5 Generic Command Example

The `generic_command` is an example for showing you how to use few system API:

1. Get System Info : `kp_get_system_info()`.

    Note: Firmware must be loaded into device first.

    ```bash
    $ sudo ./generic_command -target KL520 -port 533 -cmd system
    ```

    ```bash
    [note - using default parameter values if no value is passed]
    -target: [target platform] (KL520, KL720) = KL520 (default: KL520)
    -sidx  : [scan index] = default (specified scan index) (default: scan index of the first scanned Kneron device)
    -port  : [port id] = 533 (specified port id) (default: port ID of the first scanned Kneron device)
            Notice that scan index has higher priority than port id
    -cmd   : [command type] (system-showSystemInfo, model-showModelInfo, reboot, shutdown) = system (default: system)
            Notice that shutdown command is not supported by KL720

    connect target: index '0', port ID '533'
    connect device ... OK

    kn_number:    0xAC0A205C
    FW_version:   1.7.0-build.1217
    PLUS_version: RD version

    disconnecting device ...
    ```

2. Get Model Info : `kp_get_model_info()`.

    Note: Firmware and Model must be loaded into device first.

    ```bash
    $ sudo ./generic_command -target KL520 -port 533 -cmd model
    ```

    ```bash
    [note - using default parameter values if no value is passed]
    -target: [target platform] (KL520, KL720) = KL520 (default: KL520)
    -sidx  : [scan index] = default (specified scan index) (default: scan index of the first scanned Kneron device)
    -port  : [port id] = 533 (specified port id) (default: port ID of the first scanned Kneron device)
            Notice that scan index has higher priority than port id
    -cmd   : [command type] (system-showSystemInfo, model-showModelInfo, reboot, shutdown) = model (default: system)
            Notice that shutdown command is not supported by KL720

    connect target: index '0', port ID '533'
    connect device ... OK

    fw memory contains 1 model(s):
    all models crc = 0x6CBF1FF9
    [1] model ID = 19
    [1] model raw input width = 224
    [1] model raw input height = 224
    [1] model input channel = 3
    [1] model raw image format = RGBA8888
    [1] model raw output size = 85752


    Note that if you want to query the model info in the flash,
    please load model first via 'kp_load_model_from_flash()'
    Be careful that 'kp_load_model_from_flash()' will clean up and replace the model data stored in fw memory!

    disconnecting device ...
    ```

3. Reboot : `kp_reset_device()` with **KP_RESET_REBOOT**.

    Note: Firmware must be loaded into device first.

    ```bash
    $ sudo ./generic_command -target KL520 -port 533 -cmd reboot
    ```

    ```bash
    [note - using default parameter values if no value is passed]
    -target: [target platform] (KL520, KL720) = KL520 (default: KL520)
    -sidx  : [scan index] = default (specified scan index) (default: scan index of the first scanned Kneron device)
    -port  : [port id] = 533 (specified port id) (default: port ID of the first scanned Kneron device)
            Notice that scan index has higher priority than port id
    -cmd   : [command type] (system-showSystemInfo, model-showModelInfo, reboot, shutdown) = reboot (default: system)
            Notice that shutdown command is not supported by KL720

    connect target: index '0', port ID '533'
    connect device ... OK
    reboot device ... OK

    disconnecting device ...
    ```

4. Shutdown : `kp_reset_device()` with **KP_RESET_SHUTDOWN**.

    Note: Firmware must be loaded into device first.
    Note: KL720 does NOT support this feature.

    ```bash
    $ sudo ./generic_command -target KL520 -port 533 -cmd shutdown
    ```

    ```bash
    [note - using default parameter values if no value is passed]
    -target: [target platform] (KL520, KL720) = KL520 (default: KL520)
    -sidx  : [scan index] = default (specified scan index) (default: scan index of the first scanned Kneron device)
    -port  : [port id] = 533 (specified port id) (default: port ID of the first scanned Kneron device)
            Notice that scan index has higher priority than port id
    -cmd   : [command type] (system-showSystemInfo, model-showModelInfo, reboot, shutdown) = shutdown (default: system)
            Notice that shutdown command is not supported by KL720

    connect target: index '0', port ID '533'
    connect device ... OK
    shutdown device ... OK

    disconnecting device ...
    ```

---

## 2.Inference API Examples

Kneron PLUS provides two different API set for inference:

1. [Generic Inference](#21-generic-inference-example)

2. [Customized Inference](#22-customized-inference-example)

The main difference between **Generic Inference** and **Customized Inference** is shown below:

![](../imgs/generic_customized_diff.png)

### 2.1 Generic Inference Example

Following examples show the usage of `kp_generic_raw_inference_send()` and `kp_generic_raw_inference_receive()`.

Generic inference examples are using the **Generic Inference API**, which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code.

**Generic Inference API** allows users to directly run a model with or without Kneron pre-processing and obtain the raw output from the model, without any developments of Kneron AI device's firmware. Please refer [2.1.1 Generic Inference With Raw Output](#211-generic-inference-with-raw-output) and [2.1.2 Generic Inference Without Kneron Pre-Processing On Device](#212-generic-inference-without-kneron-pre-processing-on-device) for the demonstration of the usage.

However, **Generic Inference API** can only provide the raw output from the model without post-processing. If you wish to get the result with post-processing, you may implement the corresponding post-processing in Software (Please refer [2.1.3 Generic Inference With Post-Processing](#213-generic-inference-with-post-processing) for the demonstration).

In **Generic Inference API**, you may customized what to do in the pre-processing. There are few items are provided:

1. Image Resize
    - You can choose to do or not to do the image resize by setting `resize_mode` in `kp_generic_raw_image_header_t`.
2. Image Padding
    - You can choose to do *Symmetric Padding* (Top, Bottom, Left, Right), *Corner Padding* (Right, Bottom), and not to do the image padding by setting `padding_mode` in `kp_generic_raw_image_header_t`.
3. Image Cropping
    - You can choose to do or not to do the image cropping by setting `crop_count` and `inf_crop` in `kp_generic_raw_image_header_t`.
    - Please refer [2.1.4 Generic Inference With Cropping Image in Pre-Process](#214-generic-inference-with-cropping-image-in-pre-process) for the demonstration.
4. Image Format
    - You have to provide the format of the input image correctly by setting `image_format` in `kp_generic_raw_image_header_t`.
    - In the pre-process, the image will be convert to the format *RGBA8888*.
5. Data Normalization
    - You can choose to do *Kneron Normalization*, *Tensor Flow Normalization*, *Yolo Normalization*, or other *Customized Normalization* by setting `normalize_mode` in `kp_generic_raw_image_header_t`.

Furthermore, if you wish to execute the post-processing on Kneron AI devices (or implement different pre-processing on devices), you should use **Customized Inference API** instead of **Generic Inference API**, and need to develope the code into Kneron AI device's firmware. Please refer [2.2 Customized Inference Example](#22-customized-inference-example) for more information.

**Generic Inference API** provide following functions to retrieve specific output node data (More information please reference *API Reference/Inference API*):

| Retrieve Node Function                               | Description                                                                              |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| kp\_generic\_inference\_retrieve\_raw\_fixed\_node() | Retrieves **RAW format data** in fixed-point format on the per-node basis.               |
| kp\_generic\_inference\_retrieve\_fixed\_node()      | Retrieves and converts RAW format data to **fixed-point** data on the per-node basis.    |
| kp\_generic\_inference\_retrieve\_float\_node()      | Retrieves and converts RAW format data to **floating-point** data on the per-node basis. |

#### 2.1.1 Generic Inference With Raw Output

The **kl520_demo_generic_inference** is an example for showing how it works based on a Tiny Yolo v3 model. And this example dumps floating point values into **.txt** files for each output node.

```bash
$ sudo ./kl520_demo_generic_inference
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
.....................................................

inference loop is done

number of output node : 2

node 0:
width: 7:
height: 7:
channel: 255:
number of data (float): 12495:
first 20 data:
    1.359, 0.340, 0.510, -0.510, 0.170, 0.340,
    -0.849, 0.849, 0.849, 0.510, 0.679,
    0.679, 0.679, 0.510, 0.000, 0.340,
    0.510, 0.510, 0.340, 0.000,

node 1:
width: 14:
height: 14:
channel: 255:
number of data (float): 49980:
first 20 data:
    0.874, -0.349, -0.175, 0.000, 0.000, -0.175,
    0.175, 0.349, -0.175, 0.175, -0.175,
    0.000, -0.175, -0.699, 1.398, 1.048,
    1.048, 0.874, 0.524, 0.699,

dumped node 0 output to 'output_bike_cars_street_224x224_node0_7x7x255.txt'
dumped node 1 output to 'output_bike_cars_street_224x224_node1_14x14x255.txt'
```

#### 2.1.2 Generic Inference Without Kneron Pre-Processing On Device

The **kl520_demo_generic_inference_bypass_pre_proc** is an example for showing how it gets raw output from device, running a Tiny Yolo v3 model with a non pre-processing required image (normalized, same size as model input required, and in format RGBA8888). This example shows the usage of `kp_generic_raw_inference_bypass_pre_proc_send()` and `kp_generic_raw_inference_bypass_pre_proc_receive()`.

```bash
$ sudo ./kl520_demo_generic_inference_bypass_pre_proc
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
.....................................................

inference loop is done, starting post-processing ...

number of output node : 2

node 0:
width: 7:
height: 7:
channel: 255:
number of data (float): 12495:
first 20 data:
        1.359, 0.340, 0.340, -0.510, 0.340, 0.340,
        -0.849, 0.849, 0.849, 0.510, 0.679,
        0.510, 0.679, 0.679, 0.000, 0.340,
        0.340, 0.510, 0.340, 0.000,

node 1:
width: 14:
height: 14:
channel: 255:
number of data (float): 49980:
first 20 data:
        0.874, -0.349, 0.000, 0.175, 0.000, -0.175,
        0.175, 0.175, 0.175, 0.175, -0.175,
        0.175, -0.175, -0.699, 1.398, 1.048,
        1.048, 0.874, 0.524, 0.699,

dumped node 0 output to 'output_bike_cars_street_224x224_rgba8888_normalized_node0_7x7x255.txt'
dumped node 1 output to 'output_bike_cars_street_224x224_rgba8888_normalized_node1_14x14x255.txt'
```

#### 2.1.3 Generic Inference With Post-Processing

The **kl520_demo_generic_inference_post_yolo** is an example for showing how it gets raw output from device, running a Tiny Yolo v3 model, and does post-processing in the software.

```bash
$ sudo ./kl520_demo_generic_inference_post_yolo
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
.....................................................

inference loop is done, starting post-processing ...

doing tiny yolo v3 post-processing ...

detectable class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2
Box 5 (x1, y1, x2, y2, score, class) = 1.0, 84.0, 50.0, 181.0, 0.229727, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'

```

And it draws detected objects in a new-created **output_one_bike_many_cars_224x224.bmp**.

![](../imgs/ex_kdp2_generic_inference_raw.bmp)

#### 2.1.4 Generic Inference With Cropping Image in Pre-Process

The **kl520_demo_generic_inference_crop** is an example for showing how to do cropping image on device, execute inference only on the cropped areas of image, get the raw output from device, and does post-processing in the software.

The flow in concept:
1. Setting crop information in `kp_generic_raw_image_header_t`
2. Send an image to inference
3. Receive result *N* times (*N* specify for number of crop bounding boxes)

```bash
$ sudo ./kl520_demo_generic_inference_crop
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 50 times:
..................................................

inference loop is done, starting post-processing ...

doing tiny yolo v3 post-processing ...

crop box width : 400
crop box height : 400
crop box number : 0
detectable class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 119.0, 143.0, 399.0, 398.0, 0.941047, 2
Box 1 (x1, y1, x2, y2, score, class) = 248.0, 52.0, 392.0, 155.0, 0.829827, 2
Box 2 (x1, y1, x2, y2, score, class) = 0.0, 96.0, 201.0, 219.0, 0.663775, 2
Box 3 (x1, y1, x2, y2, score, class) = 46.0, 127.0, 218.0, 301.0, 0.624829, 2
Box 4 (x1, y1, x2, y2, score, class) = 158.0, 22.0, 330.0, 109.0, 0.267690, 2
Box 5 (x1, y1, x2, y2, score, class) = 16.0, 79.0, 62.0, 226.0, 0.223999, 2

output bounding boxes on 'output_one_bike_many_cars_800x800_crop0.bmp'

crop box width : 450
crop box height : 450
crop box number : 1
detectable class count : 80
box count : 3
Box 0 (x1, y1, x2, y2, score, class) = 141.0, 9.0, 279.0, 411.0, 0.954721, 0
Box 1 (x1, y1, x2, y2, score, class) = 150.0, 163.0, 247.0, 442.0, 0.787696, 1
Box 2 (x1, y1, x2, y2, score, class) = 0.0, 4.0, 249.0, 86.0, 0.224773, 2

output bounding boxes on 'output_one_bike_many_cars_800x800_crop1.bmp'
```

And it draws detected objects in a new-created **output_one_bike_many_cars_800x800_crop0.bmp** and **output_one_bike_many_cars_800x800_crop1.bmp**.

![](../imgs/ex_kdp2_generic_inference_crop_1.bmp)

![](../imgs/ex_kdp2_generic_inference_crop_2.bmp)


#### 2.1.5 Generic Inference Using Model in Flash

The `kl520_demo_generic_inference_flash_model` is a example for showing you how to use the model in device flash via `kp_load_model_from_flash()`.

Different from using usb loaded model, the model file must update to device flash first before using `kp_load_model_from_flash()`. Please refer [Write Model to Flash](./write_model_to_flash.md) for more information.

```bash
$ sudo ./kl520_demo_generic_inference_flash_model
```

```bash
connect device ... OK
upload firmware ... OK
loading model from flash ... OK
read image ... OK

starting inference loop 100 times:
....................................................

inference loop is done

number of output node : 2

node 0:
width: 7:
height: 7:
channel: 255:
number of data (float): 12495:
first 20 data:
        1.359, 0.340, 0.510, -0.510, 0.170, 0.340,
        -0.849, 0.849, 0.849, 0.510, 0.679,
        0.679, 0.679, 0.510, 0.000, 0.340,
        0.510, 0.510, 0.340, 0.000,

node 1:
width: 14:
height: 14:
channel: 255:
number of data (float): 49980:
first 20 data:
        0.874, -0.349, -0.175, 0.000, 0.000, -0.175,
        0.175, 0.349, -0.175, 0.175, -0.175,
        0.000, -0.175, -0.699, 1.398, 1.048,
        1.048, 0.874, 0.524, 0.699,

dumped node 0 output to 'output_bike_cars_street_224x224_node0_7x7x255.txt'
dumped node 1 output to 'output_bike_cars_street_224x224_node1_14x14x255.txt'
```

### 2.2 Customized Inference Example

Customized inference examples are using the **Customized Inference API**, which provides some decent flexibility for users to customize their own applications with customized NEF models.

For the detail introduction of **Customized Inference**, please refer the documents in [Customize API](../customized_api/introduction.md) section.


### 2.3 User Define API Inference Example

Although Customized Inference may provide some flexibility, fill the header used in Customized Inference API may not be easy for general users. Therefore, if you wish to provide simple APIs to your users, **User Define API** will be your best choice.

User Define API supposed to be a simple API function which is composed by those things you need to do under Customized Inference. Not only user defined inference send and receive can be created by User Define API, but also user defined command can be joined by User Define API.

The `kl520_demo_user_define_api` is to show you how to use the User Define API:

1. For inference: `kp_app_yolo_inference_send()` and `kp_app_yolo_inference_receive()`.

2. For command: `kp_app_yolo_get_post_proc_parameters()` and `kp_app_yolo_get_post_proc_parameters()`.

All these 4 API functions are implemented by Customized API, please refer the documents in [Customize API](../customized_api/introduction.md) section for more information.

```bash
$ sudo ./kl520_demo_user_define_api
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
get post-process parameters ... OK
set post-process parameters ... OK
read image ... OK

starting inference loop 100 times:
...........................................................
recover post-process parameters ... OK

detectable class count : 80
box count : 2
Box 0 (x1, y1, x2, y2, score, class) = 44.7, 57.0, 92.7, 195.5, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 121.8, 68.4, 218.3, 184.7, 0.997959, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'
```

---

## 3. Parallel Usage Control Examples

### 3.1 Multiple Threads Usage Example

In the previous inference related examples, sending images to device and receiving results from device are running sequentially.

However, sending images and receiving results can be done in different threads to maximum the processing speed.

The **kl520_demo_generic_inference_multithread** is an example for showing how to put sending image to device and receiving results from device into two different threads.

```bash
$ sudo ./kl520_demo_generic_inference_multithread
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
....................................................................................................

total inference 100 images
time spent: 2.09 secs, FPS = 47.9

detectable class count : 80
box count : 5
Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'
```


### 3.2 Drop Frame Usage Example

PLUS provides examples using web camera to do inference.

To build these camera examples, please build PLUS with:

```bash
$ cd kneron_plus/
$ mkdir build
$ cd build
$ cmake -DWITH_OPENCV=ON ..
$ make -j
```

If you are using MSYS2 MinGW 64-bit in Windows:

```bash
$ cd kneron_plus/
$ mkdir build
$ cd build
$ cmake -DWITH_OPENCV=ON .. -G"MSYS Makefiles"
$ make -j
```

If the camera produces frames faster than device inference, displaying frames from camera may be delayed by the inference speed since sending image to device may be blocked when buffer of device is full.

![](../imgs/cam_demo_without_drop_frame.png)

**kl720_demo_cam_generic_inference_drop_frame** is an example for showing how to use `kp_inf_configuration_t` and `kp_inference_configure()` config device to drop frame if the buffer is full.

![](../imgs/cam_demo_with_drop_frame.png)

The image display FPS raised from **25.76** (without drop frame) to **30.13** (with drop frame).

---

## 4. Model Zoo Examples

Model Zoo examples simply show one image inference via different pre-trained models.

The model backbones are available and could be retrained for specific need.

Please refer to [Model Zoo](../modelzoo/index.md) section for more information.



```bash
$ sudo ./kl720_kn-model-zoo_generic_inference_post_yolov5
```

```bash
connect device ... OK
upload model ... OK
read image ... OK

starting inference loop 1 times:
.

inference loop is done

detectable class count : 80
box count : 18
Box 0 (x1, y1, x2, y2, score, class) = 371.0, 354.0, 510.0, 747.0, 0.805185, 0
Box 1 (x1, y1, x2, y2, score, class) = 742.0, 60.0, 794.0, 211.0, 0.515536, 0
Box 2 (x1, y1, x2, y2, score, class) = 87.0, 31.0, 135.0, 76.0, 0.265722, 0
Box 3 (x1, y1, x2, y2, score, class) = 89.0, 189.0, 121.0, 300.0, 0.208385, 0
Box 4 (x1, y1, x2, y2, score, class) = 373.0, 516.0, 480.0, 763.0, 0.528667, 1
Box 5 (x1, y1, x2, y2, score, class) = 139.0, 146.0, 474.0, 449.0, 0.805632, 2
Box 6 (x1, y1, x2, y2, score, class) = 458.0, 149.0, 719.0, 346.0, 0.762070, 2
Box 7 (x1, y1, x2, y2, score, class) = 173.0, 2.0, 319.0, 94.0, 0.731227, 2
Box 8 (x1, y1, x2, y2, score, class) = 706.0, 186.0, 799.0, 489.0, 0.726494, 2
Box 9 (x1, y1, x2, y2, score, class) = 95.0, 117.0, 290.0, 315.0, 0.717568, 2
Box 10 (x1, y1, x2, y2, score, class) = 244.0, 44.0, 407.0, 163.0, 0.661910, 2
Box 11 (x1, y1, x2, y2, score, class) = 428.0, 115.0, 623.0, 233.0, 0.656740, 2
Box 12 (x1, y1, x2, y2, score, class) = 37.0, 79.0, 175.0, 277.0, 0.581318, 2
Box 13 (x1, y1, x2, y2, score, class) = 0.0, 53.0, 33.0, 156.0, 0.493920, 2
Box 14 (x1, y1, x2, y2, score, class) = 24.0, 79.0, 132.0, 212.0, 0.245957, 2
Box 15 (x1, y1, x2, y2, score, class) = 319.0, 0.0, 449.0, 152.0, 0.303165, 7
Box 16 (x1, y1, x2, y2, score, class) = 235.0, 43.0, 410.0, 161.0, 0.226067, 7
Box 17 (x1, y1, x2, y2, score, class) = 0.0, 636.0, 62.0, 686.0, 0.206850, 8

output bounding boxes on 'output_one_bike_many_cars_800x800.bmp'
```

---

## 5. Debug Related Examples
### 5.1 Debug Flow Example

This example is to demonstrate the usage of **kp_dbg_set_enable_checkpoints()** and **kp_dbg_receive_checkpoint_data()**. And the diagram below shows the flow of this two APIs for single model usage.

![](../imgs/debug_checkpoint_flow.png)

There are three check points can be set by **kp_dbg_set_enable_checkpoints()**:

- KP_DBG_CHECKPOINT_BEFORE_PREPROCESS
- KP_DBG_CHECKPOINT_AFTER_PREPROCESS
- KP_DBG_CHECKPOINT_AFTER_INFERENCE

If *KP_DBG_CHECKPOINT_BEFORE_PREPROCESS* is set, the image sent by **kp_xxx_inference_send()** will be retrieved by **kp_dbg_receive_checkpoint_data()**.

If *KP_DBG_CHECKPOINT_AFTER_PREPROCESS* is set, the image which has been performed pre-process will be retrieved by **kp_dbg_receive_checkpoint_data()**.

If *KP_DBG_CHECKPOINT_AFTER_INFERENCE* is set, the raw output data of the model will be retrieved by **kp_dbg_receive_checkpoint_data()**.

After all debug data have been retrieved, **kp_dbg_receive_checkpoint_data()** will receive data with status **KP_DBG_CHECKPOINT_END_37** to notify the debug process has finished.

Note: If you are using multiple models, **kp_dbg_receive_checkpoint_data()** may need to be called more times than the diagram shows.

```bash
$ ./kl520_demo_customize_inf_single_model_debug.exe
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK
debug enable checkpoints ... OK
send one image for inference ... OK

before-pre_process data:
image x, y = (0, 0)
image width, height = (800, 800)
img_format = 0x60 (kp_image_format_t)
inference model ID = 19
image data (hex) = 0x 3D.E7.3D.E7.3D.E7.3D.E7.3C.E7 ...

after-pre_process data:
image width, height = (224, 224)
img_format = 0xd (kp_image_format_t)
inference model ID = 19
image data (hex) = 0x 60.64.68.00.60.64.63.00.60.64 ...

after-inference data:
inference model ID = 19
total raw output size = 85680 bytes
number of nodes = 2
    node 0:
    - width = 7
    - height = 7
    - channel = 255
    - radix = 2
    - scale = 1.472
    node 1:
    - width = 14
    - height = 14
    - channel = 255
    - radix = 2
    - scale = 1.431
raw output (hex) = 0x 0A.01.00.FE.FE.FE.FA.0C.FA.FC ...
got the end of debug loop ... OK
receive inference result ... OK
```

---

### 5.2 Execution Time Profiling Example

This example is to demonstrate the usage of **kp_profile_set_enable()** and **kp_profile_get_statistics()**. And the diagram below shows the flow of this two APIs for single model usage.

![](../imgs/execution_time_profile.png)

Unlike [Debug Flow](#51-debug-flow-example), **kp_profile_get_statistics()** does not need to be called between kp_xxx_inference_send() and kp_xxx_inference_receive(). It only needs to be call after one or more inferences are completed.

Therefore, **kp_xxx_inference_send()** and **kp_xxx_inference_receive()** can be called multiple times between **kp_profile_set_enable()** and **kp_profile_get_statistics()**.

The pre-process time, inference time, and post-process time are the sum of these time in each inference.

```bash
$ ./kl520_demo_customize_inf_single_model_profile
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK
enable profile ... OK

starting inference loop 100 times:
......................................................
inference loop completed.

[profile]
number of models: 1
    - model_id = 19
    - inf_count = 100
    - avg_pre_process_ms = 1.41
    - avg_inference_ms = 18.00
    - avg_post_process_ms = 2.00


detectable class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 44.7, 57.0, 92.7, 195.5, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 42.7, 94.5, 99.9, 210.8, 0.465116, 1
Box 2 (x1, y1, x2, y2, score, class) = 121.8, 68.4, 218.3, 184.7, 0.997959, 2
Box 3 (x1, y1, x2, y2, score, class) = 86.8, 83.5, 130.9, 117.9, 0.499075, 2
Box 4 (x1, y1, x2, y2, score, class) = 27.7, 77.4, 55.1, 100.0, 0.367952, 2
Box 5 (x1, y1, x2, y2, score, class) = 1.1, 83.7, 49.8, 180.9, 0.229727, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'
```
