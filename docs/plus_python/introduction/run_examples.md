# Run Examples

The provided examples are designed to show how to use KP APIs and present Kneron Device features. Error handling, wording and application layer features are not covered. They are open for more creatives.

> **Note 1**: In the inference related examples, we are using KL520 for most demo. If you wish to use KL720, just change the prefix of the example name from kl520 to kl720.

> **Note 2**: **[Ubuntu]** Please update Kneron device USB permission before following steps on Ubuntu. See the [Installation
](./install_dependency.md) for details.

> **Note 3**: Few examples will auto connect multiple devices to run inference. If you put hybrid types of devices on host, the inference may fail.

> **Note 4**: If you modify code to change different test image file. Input image aspect ratio is suggested to be aligned to model input aspect ratio.

1. [Scan Device Example](#1-scan-device-example)
2. [Install Driver for Windows Example](#2-install-driver-for-windows-example)
3. [Run Examples](#3-run-inference-examples)
4. [Multiple Threads Usage Example](#4-multiple-threads-usage-example)
5. [Drop Frame Usage Example](#5-drop-frame-usage-example)
6. [Model Zoo Examples](#6-model-zoo-examples)

---

## 1. Scan Device Example

Note: This example is to show the usage of `kp.core.scan_devices()`.

While one or multiple AI devices are plugged into the host, they can be scanned to get some basic device information.

```bash
$ python3 ScanDevices.py

scanning kneron devices ...
number of Kneron devices found: 2
listing devices information as follows:

[0] USB scan index: '0'
[0] USB port ID: '25'
[0] Product ID: '0x100 (KL520)'
[0] USB link speed: '3'
[0] USB port path: '1-6'
[0] KN number: '0xC8062D2C'
[0] Connectable: 'True'
[0] Firmware: 'KDP2 Loader'

[1] USB scan index: '1'
[1] USB port ID: '61'
[1] Product ID: '0x720 (KL720)'
[1] USB link speed: '4'
[1] USB port path: '1-15'
[1] KN number: '0x1B04132C'
[1] Connectable: 'True'
[1] Firmware: 'KDP2'
```

Above shows that it founds two Kneron devices, a brief description listed below.

- **USB scan index** : An index number represents the device in the scanned order, can be used by KP API to establish USB connection.
- **USB port ID** : An unique number represents the device on the certain usb port, can be used by KP API to establish USB connection.
- **Product ID** : The product ID.
- **USB link speed** : USB link speed, High-Speed is fastest speed for USB2.0.
- **USB port path** : This means the physical USB port path on the host.
- **KN number** : Kneron's serial number for the device.
- **Connectable** : It tells if this device is connectable; one device can only be connected by one program at the same time.
- **Firmware** : This shows which firmware the AI device is using, KDP, KDP2 or KDP2 Loader.

---

## 2. Install Driver for Windows Example

Note: This example is to show the usage of `kp.core.install_driver_for_windows()` and help users to install driver to Windows directly.

Note: This example is only available on Windows 10, and it must be run as Administrator (Run CMD/PowerShell as administrator).

1. For installing the driver for KL520:

    ```bash
    $ python3 InstallDriverWindows.py --target KL520
    ```

    ```bash
    [Note]
     - You must run this app as administrator on Windows
    [Installing Driver]
     - [KP_DEVICE_KL520]
        - Success
    ```

2. For installing the driver for KL720:

    ```bash
    $ python3 InstallDriverWindows.py --target KL720
    ```

    ```bash
    [Note]
     - You must run this app as administrator on Windows
    [Installing Driver]
     - [KP_DEVICE_KL720_LEGACY]
        - Success
     - [KP_DEVICE_KL720]
        - Success
    ```

---

## 3. Run Inference Examples

The PLUS provides two categories of API set for model inference.

1. **Generic inference** category which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code.

2. **Customized inference (C Language Only)** category which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code **on Kneron AI devices** (or implement different pre-processing on devices)

The main difference between **Generic Inference** and **Customized Inference** is shown below:

![](../imgs/generic_customized_diff.png)

Below will demonstrate only usage in two examples for **Generic inference**. For **Customized inference (C Language Only)**, please refer the [**C language documents**](../../plus_c/customized_api/introduction.md).

### 3.2 Generic Inference Example

Following examples show the usage of `kp.inference.generic_raw_inference_send()` and `kp.inference.generic_raw_inference_receive()`.

Generic inference examples are using the **Generic Inference API**, which is intended for advanced users who are interested in developing their models and implement corresponding pre/post-processing code.

**Generic Inference API** allows users to directly run a model with or without Kneron pre-processing and obtain the raw output from the model, without any developments of Kneron AI device's firmware. Please refer following sections for the demonstration of the usage:

* [3.2.1 Generic Inference With Raw Output](#321-generic-inference-with-raw-output)
* [3.2.2 Generic Inference Without Kneron Pre-Processing On Device](#322-generic-inference-without-kneron-pre-processing-on-device)

However, **Generic Inference API** can only provide the raw output from the model without post-processing. If you wish to get the result with post-processing, you may implement the corresponding post-processing in Software. Please refer following sections for the demonstration of the usage:

* [3.2.3 Generic Inference With Post-Processing](#323-generic-inference-with-post-processing)

In **Generic Inference API**, you may customized what to do in the pre-processing. There are few items are provided:

1. Image Resize
    - You can choose to do or not to do the image resize by setting `resize_mode` in `kp.GenericRawImageHeader`.
2. Image Padding
    - You can choose to do *Symmetric Padding* (Top, Bottom, Left, Right), *Corner Padding* (Right, Bottom), and not to do the image padding by setting `padding_mode` in `kp.GenericRawImageHeader`.
3. Image Cropping
    - You can choose to do or not to do the image cropping by setting `inference_crop_box_list` in `kp.GenericRawImageHeader`.
    - Please refer [3.2.4 Generic Inference With Cropping Image in Pre-Process](#324-generic-inference-with-cropping-image-in-pre-process) for the demonstration.
4. Image Format
    - You have to provide the format of the input image correctly by setting `image_format` in `kp.GenericRawImageHeader`.
    - In the pre-process, the image will be convert to the format *RGBA8888*.
5. Data Normalization
    - You can choose to do *Kneron Normalization*, *Tensor Flow Normalization*, *Yolo Normalization*, or other *Customized Normalization* by setting `normalize_mode` in `kp.GenericRawImageHeader`.

**Generic Inference API** provide following functions to retrieve specific output node data (More information please reference [kp API Document - kp.inference](../api_document/kp/inference.md)):

| Retrieve Node Function                                   | Description                                                                              |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| kp.inference.generic\_inference\_retrieve\_fixed\_node() | Retrieves and converts RAW format data to **fixed-point** data on the per-node basis.    |
| kp.inference.generic\_inference\_retrieve\_float\_node() | Retrieves and converts RAW format data to **floating-point** data on the per-node basis. |

#### 3.2.1 Generic Inference With Raw Output

The example **'KL520DemoGenericInference'** not do any post-processing and prints feature map raw output for each output node.

```bash
$ python3 KL520DemoGenericInference.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
[Retrieve Inference Node Output ]
 - Success
[Result]
[{
    "width": 7,
    "height": 7,
    "channel": 255,
    "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
    "num_data": 12495,
    "ndarray": [
        "[[[[  1.3589103    0.33972758   0.50959134 ...   0.16986379",
        "      0.33972758  -0.849319  ]",
        "   [  1.698638    -0.50959134   0.50959134 ...  -0.16986379",
        "     -0.16986379  -0.849319  ]",
        "   [  1.5287741    0.50959134   0.16986379 ...   0.",
        "     -0.33972758  -0.50959134]",
        "   ...",
        "   [  1.3589103    1.5287741   -1.0191827  ...   2.547957",
        "     -1.1890465   -0.67945516]",
        "   [  1.3589103    1.8685017   -1.0191827  ...   1.0191827",
        "     -0.67945516  -0.33972758]",
        "   [  0.849319     0.849319    -0.16986379 ...   0.16986379",
        "      0.16986379  -0.33972758]]",
        "",
        "  ...",
        "",
        "  [[ -8.49319     -9.342508   -10.021964   ... -10.191828",
        "     -9.002781    -7.6438704 ]",
        "   [ -7.983598   -10.021964    -9.852099   ...  -9.172645",
        "     -8.323326    -6.6246877 ]",
        "   [ -7.983598   -10.191828   -10.021964   ...  -8.153461",
        "     -7.983598    -7.304143  ]",
        "   ...",
        "   [ -7.6438704   -9.682236   -10.361691   ...  -9.002781",
        "    -10.021964    -9.172645  ]",
        "   [ -7.304143   -10.701419   -12.400057   ...  -9.682236",
        "     -9.682236    -9.002781  ]",
        "   [ -6.1150966   -8.153461    -9.342508   ...  -7.983598",
        "     -8.153461    -8.49319   ]]]]"
    ]
}, {
    "width": 14,
    "height": 14,
    "channel": 255,
    "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
    "num_data": 49980,
    "ndarray": [
        "[[[[  0.8736945  -0.3494778  -0.1747389 ...   0.         -0.1747389",
        "     -0.6989556]",
        "   [  0.6989556  -0.8736945  -0.6989556 ...  -0.5242167  -0.1747389",
        "     -0.5242167]",
        "   [  0.5242167  -0.8736945  -0.6989556 ...  -0.1747389   0.1747389",
        "     -0.8736945]",
        "   ...",
        "   [ -1.0484334   0.          0.        ...   0.3494778   0.3494778",
        "      0.1747389]",
        "   [ -0.6989556  -0.5242167  -0.1747389 ...   0.5242167   0.3494778",
        "      0.1747389]",
        "   [  0.1747389   0.          0.1747389 ...   0.5242167   0.3494778",
        "      0.       ]]",
        "",
        "  ...",
        "",
        "  [[ -7.5137725  -9.261162   -9.785378  ... -10.659073  -10.484334",
        "     -8.562206 ]",
        "   [-10.484334  -13.280156  -14.678067  ... -15.202284  -15.202284",
        "    -11.008551 ]",
        "   [-11.18329   -14.678067  -15.202284  ... -16.07598   -15.027545",
        "    -12.231723 ]",
        "   ...",
        "   [-11.18329   -15.377023  -18.172846  ... -13.105417  -12.581201",
        "    -10.833812 ]",
        "   [-10.134856  -14.153851  -16.774935  ... -10.659073   -9.61064",
        "     -8.387467 ]",
        "   [ -9.086423  -12.231723  -12.930678  ... -10.134856   -9.261162",
        "     -7.3390336]]]]"
    ]
}]
```

#### 3.2.2 Generic Inference Without Kneron Pre-Processing On Device

The **'KL520DemoGenericInferenceBypassPreProc.py'** is an example for showing how it gets raw output from device, running a Tiny Yolo v3 model with a non pre-processing required image (normalized, same size as model input required, and in format RGBA8888). This example shows the usage of `kp.inference.generic_raw_inference_bypass_pre_proc_send()` and `kp.inference.generic_raw_inference_bypass_pre_proc_receive()`.

```bash
$ python3 KL520DemoGenericInferenceBypassPreProc.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
[Retrieve Inference Node Output ]
 - Success
[Tiny Yolo V3 Post-Processing]
 - Success
[Result]
{
    "class_count": 80,
    "box_count": 6,
    "box_list": {
        "0": {
            "x1": 46,
            "y1": 62,
            "x2": 91,
            "y2": 191,
            "score": 0.9704,
            "class_num": 0
        },
        "1": {
            "x1": 44,
            "y1": 96,
            "x2": 99,
            "y2": 209,
            "score": 0.5356,
            "class_num": 1
        },
        "2": {
            "x1": 122,
            "y1": 70,
            "x2": 217,
            "y2": 183,
            "score": 0.9976,
            "class_num": 2
        },
        "3": {
            "x1": 87,
            "y1": 85,
            "x2": 131,
            "y2": 117,
            "score": 0.4992,
            "class_num": 2
        },
        "4": {
            "x1": 28,
            "y1": 77,
            "x2": 56,
            "y2": 99,
            "score": 0.4109,
            "class_num": 2
        },
        "5": {
            "x1": 3,
            "y1": 84,
            "x2": 48,
            "y2": 181,
            "score": 0.2346,
            "class_num": 2
        }
    }
}
```

#### 3.2.3 Generic Inference With Post-Processing

**Note**: Reference to [Yolo Object Name Mapping](./yolo_object_name_mapping.md) for the detection result classes of YOLO examples.  

The **'KL520DemoGenericInferencePostYolo.py'** is an example for showing how it gets raw output from device, running a Tiny Yolo v3 model, and does post-processing in the software (host side).

```bash
$ python3 KL520DemoGenericInferencePostYolo.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
[Retrieve Inference Node Output ]
 - Success
[Tiny Yolo V3 Post-Processing]
 - Success
[Result]
{
    "class_count": 80,
    "box_count": 6,
    "box_list": {
        "0": {
            "x1": 46,
            "y1": 62,
            "x2": 91,
            "y2": 191,
            "score": 0.965,
            "class_num": 0
        },
        "1": {
            "x1": 44,
            "y1": 96,
            "x2": 99,
            "y2": 209,
            "score": 0.4651,
            "class_num": 1
        },
        "2": {
            "x1": 122,
            "y1": 70,
            "x2": 218,
            "y2": 183,
            "score": 0.998,
            "class_num": 2
        },
        "3": {
            "x1": 87,
            "y1": 85,
            "x2": 131,
            "y2": 117,
            "score": 0.4991,
            "class_num": 2
        },
        "4": {
            "x1": 28,
            "y1": 77,
            "x2": 55,
            "y2": 100,
            "score": 0.368,
            "class_num": 2
        },
        "5": {
            "x1": 3,
            "y1": 84,
            "x2": 48,
            "y2": 181,
            "score": 0.2297,
            "class_num": 2
        }
    }
}
[Output Result Image]
 - Output bounding boxes on 'output_bike_cars_street_224x224.bmp'
```

It draws detected objects in a new-created **output_one_bike_many_cars_224x224.bmp**.

![](../imgs/ex_kdp2_kl520_generic_inference_raw.bmp)

#### 3.2.4 Generic Inference With Cropping Image in Pre-Process

**Note**: Reference to [Yolo Object Name Mapping](./yolo_object_name_mapping.md) for the detection result classes of YOLO examples.  

The **'KL520DemoGenericInferenceCrop.py'** is an example for showing how to do cropping image on device, execute inference only on the cropped areas of image, get the raw output from device, and does post-processing in the software.

The flow in concept:

1. Setting crop information in `kp.GenericRawImageHeader`
2. Send an image to inference
3. Receive result *N* times (*N* specify for number of crop bounding boxes)

```bash
$ python3 KL520DemoGenericInferenceCrop.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
[Retrieve Inference Node Output ]
 - Success
[Tiny Yolo V3 Post-Processing]
 - Success
[Result]
[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
 - Retrieve 2 Nodes Success
[Post-Processing]
 - Success
[Result]
 - total inference 50 images

[Crop Box 0]
 - [Crop Box Information]
{
    "crop_box_index": 0,
    "x": 0,
    "y": 0,
    "width": 400,
    "height": 400
}
 - [Crop Box Result]
{
    "class_count": 80,
    "box_count": 5,
    "box_list": {
        "0": {
            "x1": 120,
            "y1": 144,
            "x2": 399,
            "y2": 397,
            "score": 0.941,
            "class_num": 2
        },
        "1": {
            "x1": 248,
            "y1": 54,
            "x2": 392,
            "y2": 154,
            "score": 0.8298,
            "class_num": 2
        },
        "2": {
            "x1": 0,
            "y1": 96,
            "x2": 198,
            "y2": 218,
            "score": 0.6638,
            "class_num": 2
        },
        "3": {
            "x1": 159,
            "y1": 25,
            "x2": 330,
            "y2": 106,
            "score": 0.2677,
            "class_num": 2
        },
        "4": {
            "x1": 17,
            "y1": 81,
            "x2": 62,
            "y2": 224,
            "score": 0.224,
            "class_num": 2
        }
    }
}

[Crop Box 1]
 - [Crop Box Information]
{
    "crop_box_index": 1,
    "x": 230,
    "y": 335,
    "width": 450,
    "height": 450
}
 - [Crop Box Result]
{
    "class_count": 80,
    "box_count": 3,
    "box_list": {
        "0": {
            "x1": 149,
            "y1": 10,
            "x2": 271,
            "y2": 410,
            "score": 0.9547,
            "class_num": 0
        },
        "1": {
            "x1": 153,
            "y1": 173,
            "x2": 243,
            "y2": 433,
            "score": 0.7877,
            "class_num": 1
        },
        "2": {
            "x1": 0,
            "y1": 9,
            "x2": 240,
            "y2": 82,
            "score": 0.2248,
            "class_num": 2
        }
    }
}
[Output Result Image]
 - Output bounding boxes on 'output_one_bike_many_cars_800x800_crop0.bmp'
 - Output bounding boxes on 'output_one_bike_many_cars_800x800_crop1.bmp'
```

And it draws detected objects in a new-created **output_one_bike_many_cars_800x800_crop0.bmp** and **output_one_bike_many_cars_800x800_crop1.bmp**.

![](../imgs/ex_kdp2_generic_inference_crop_1.bmp)

![](../imgs/ex_kdp2_generic_inference_crop_2.bmp)

---

## 4. Multiple Threads Usage Example

In the previous inference related examples, sending images to device and receiving results from device are running sequentially.

However, sending images and receiving results can be done in different threads to maximum the processing speed.

The **'KL520DemoGenericInferenceMultiThread.py'** is an example for showing how to put sending image to device and receiving results from device into two different threads.

```bash
$ python3 KL520DemoGenericInferenceMultiThread.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 100 times
 - ....................................................................................................
[Result]
 - Total inference 100 images
 - Time spent: 1.99 secs, FPS = 50.2
[Retrieve Inference Node Output ]
 - Success
[Result]
[{
    "width": 7,
    "height": 7,
    "channel": 255,
    "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
    "num_data": 12495,
    "ndarray": [
        "[[[[  1.3589103    0.33972758   0.50959134 ...   0.16986379",
        "      0.33972758  -0.849319  ]",
        "   [  1.698638    -0.50959134   0.50959134 ...  -0.16986379",
        "     -0.16986379  -0.849319  ]",
        "   [  1.5287741    0.50959134   0.16986379 ...   0.",
        "     -0.33972758  -0.50959134]",
        "  ...",
        "   [ -7.6438704   -9.682236   -10.361691   ...  -9.002781",
        "    -10.021964    -9.172645  ]",
        "   [ -7.304143   -10.701419   -12.400057   ...  -9.682236",
        "     -9.682236    -9.002781  ]",
        "   [ -6.1150966   -8.153461    -9.342508   ...  -7.983598",
        "     -8.153461    -8.49319   ]]]]"
    ]
}, {
    "width": 14,
    "height": 14,
    "channel": 255,
    "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
    "num_data": 49980,
    "ndarray": [
        "[[[[  0.8736945  -0.3494778  -0.1747389 ...   0.         -0.1747389",
        "     -0.6989556]",
        "   [  0.6989556  -0.8736945  -0.6989556 ...  -0.5242167  -0.1747389",
        "     -0.5242167]",
        "   [  0.5242167  -0.8736945  -0.6989556 ...  -0.1747389   0.1747389",
        "     -0.8736945]",
        "  ...",
        "   [-11.18329   -15.377023  -18.172846  ... -13.105417  -12.581201",
        "    -10.833812 ]",
        "   [-10.134856  -14.153851  -16.774935  ... -10.659073   -9.61064",
        "     -8.387467 ]",
        "   [ -9.086423  -12.231723  -12.930678  ... -10.134856   -9.261162",
        "     -7.3390336]]]]"
    ]
}]
```

---

## 5. Drop Frame Usage Example

If the camera produces frames faster than device inference, displaying frames from camera may be delayed by the inference speed since sending image to device may be blocked when buffer of device is full.

**'KL520DemoCamGenericInferenceDropFrame.py'** is an example for showing how to config device to drop frame if the buffer is full.

The configure function shows in the following code block:
```python
"""
configure inference settings (make it frame-droppable for real-time purpose)
"""
try:
    print('[Configure Inference Settings]')
    kp.inference.set_inference_configuration(device_group=device_group,
                                             inference_configuration=kp.InferenceConfiguration(enable_frame_drop=True))
    print(' - Success')
except kp.ApiKPException as exception:
    print('Error: configure inference settings failed, error = \'{}\''.format(str(exception)))
    exit(0)
```

---

## 6. Model Zoo Examples

Model Zoo examples simply show one image inference via different pre-trained models. The model backbones are available and could be retrained for specific need. Please refer to [Model Zoo](../modelzoo/index.md) section for more information.

```bash
$ python3 KL720KnModelZooGenericInferenceClassification.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 1 times
 - .
[Retrieve Inference Node Output ]
 - Success
[Result]
Top1 class: 0, score: 0.94401616
- Success
```