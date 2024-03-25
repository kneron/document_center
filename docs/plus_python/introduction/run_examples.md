# Run Examples

The provided examples are designed to show how to use KP APIs and present Kneron Device features. Error handling, wording and application layer features are not covered. They are open for more creatives.

> **Note 1**: In the inference related examples, we are using KL520 for most demo. If you wish to use KL630, KL720, or KL730, just change the prefix of the example name from kl520 to kl630, kl720, or kl730.

> **Note 2**: **[Ubuntu]** Please update Kneron device USB permission before following steps on Ubuntu. See the [Installation
](./install_dependency.md) for details.

> **Note 3**: Few examples will auto connect multiple devices to run inference. If you put hybrid types of devices on host, the inference may fail.

> **Note 4**: If you modify code to change different test image file. Input image aspect ratio is suggested to be aligned to model input aspect ratio.

1. [Scan Device Example](#1-scan-device-example)
2. [Install Driver for Windows Example](#2-install-driver-for-windows-example)
3. [Load Firmware and Model Example](#3-load-firmware-and-model-example)
4. [Generic Command Example](#4-generic-command-example)
5. [Inference API Examples](#5-inference-api-examples)
6. [Multiple Threads Usage Example](#6-multiple-threads-usage-example)
7. [Drop Frame Usage Example](#7-drop-frame-usage-example)
8. [Model Zoo Examples](#8-model-zoo-examples)
9. [Device Memory Usage Control Example](#9-device-memory-usage-control-example)

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

2. For installing the driver for KL630:

    ```bash
    $ python3 InstallDriverWindows.py --target KL630
    ```

    ```bash
    [Note]
     - You must run this app as administrator on Windows
    [Installing Driver]
     - [KP_DEVICE_KL630]
        - Success
    ```

3. For installing the driver for KL720:

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

4. For installing the driver for KL730:

    ```bash
    $ python3 InstallDriverWindows.py --target KL730
    ```

    ```bash
    [Note]
     - You must run this app as administrator on Windows
    [Installing Driver]
     - [KP_DEVICE_KL730]
        - Success
    ```

---

## 3. Load Firmware and Model Example

`kp.core.load_firmware_from_file()` is an API to load firmware file from host to the AI device via USB. And this API is only available when device is on **USB Boot Mode**. Please refer [Upgrade AI Device To KDP2](./upgrade_ai_device_to_kdp2.md) for more information.

`kp.core.load_model_from_file()` is an API to load model file from host to the AI device via USB. Please refer [Write Model to Flash](./write_model_to_flash.md) for more information.

`kp.core.load_model_from_flash()` is an API to load model from the flash memory of the AI device. Please refer [2.4 Generic Image Inference Using Model in Flash](./../feature_guide/chapter/generic_inference.md#24-generic-image-inference-using-model-in-flash) and [Write Model to Flash](./write_model_to_flash.md) for more information.

---

## 4. Generic Command Example

The `GenericCommand.py` is an example for showing you how to use few system API:

1. Get System Info : `kp.core.get_system_info()`.

    Note: Firmware must be loaded into device first.

    ```bash
    $ python3 GenericCommand.py --target KL520 --port 33 --cmd system
    
    [Check Device]
    - success
    [Connect Device]
    - target device: 'KL520'
    - scan index: '0'
    - port ID: '33'
    - command: 'system'
    [System Information]
    {
        "kn_number": "0xC8062D2C",
        "firmware_version": "2.0.0-build.517"
    }
    [PLUS Version]
    RD version
    ```

2. Get Model Info : `kp.core.get_model_info()`.

    Note: Firmware and Model must be loaded into device first.

    ```bash
    $ python3 GenericCommand.py --target KL520 --port 33 --cmd model
    
    [Check Device]
    - success
    [Connect Device]
    - target device: 'KL520'
    - scan index: '0'
    - port ID: '33'
    - command: 'model'
    [Model NEF Information]
    {
        "magic": "0x5AA55AA5",
        "metadata": {
            "kn_number": "0x0",
            "toolchain_version": "",
            "compiler_version": "",
            "nef_schema_version": {
                "version": "0.0.0"
            },
            "platform": ""
        },
        "target_chip": "ModelTargetChip.KP_MODEL_TARGET_CHIP_KL520",
        "crc": "0x6CBF1FF9",
        "models": {
            "0": {
                "target_chip": "ModelTargetChip.KP_MODEL_TARGET_CHIP_KL520",
                "version": "0x0",
                "id": 19,
                "input_nodes": {
                    "0": {
                        "index": 0,
                        "name": "",
                        "shape_npu": [
                            1,
                            3,
                            224,
                            224
                        ],
                        "shape_onnx": [],
                        "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B",
                        "quantization_parameters": {
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": 1.0,
                                    "radix": 8
                                }
                            }
                        }
                    }
                },
                "output_nodes": {
                    "0": {
                        "index": 0,
                        "name": "",
                        "shape_npu": [
                            1,
                            255,
                            7,
                            7
                        ],
                        "shape_onnx": [],
                        "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                        "quantization_parameters": {
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": 1.4717674255371094,
                                    "radix": 2
                                }
                            }
                        }
                    },
                    "1": {
                        "index": 1,
                        "name": "",
                        "shape_npu": [
                            1,
                            255,
                            14,
                            14
                        ],
                        "shape_onnx": [],
                        "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                        "quantization_parameters": {
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": 1.4307060241699219,
                                    "radix": 2
                                }
                            }
                        }
                    }
                },
                "setup_schema_version": {
                    "version": "0.0.0"
                },
                "setup_file_schema_version": {
                    "version": "0.0.0"
                },
                "max_raw_out_size": 86076
            }
        }
    }

    Note that if you want to query the model info in the flash,
    please load model first via 'kp.core.load_model_from_flash()'
    Be careful that 'kp.core.load_model_from_flash()' will clean up and replace the model data stored in fw memory!
    ```

3. Reboot : `kp.core.reset_device()` with **KP_RESET_REBOOT**.

    Note: Firmware must be loaded into device first.

    ```bash
    $ python3 GenericCommand.py --target KL520 --port 33 --cmd reboot

    [Check Device]
    - success
    [Connect Device]
    - target device: 'KL520'
    - scan index: '0'
    - port ID: '33'
    - command: 'reboot'
    [Reboot Device]
    - reboot command success
    ```

4. Shutdown : `kp.core.reset_device()` with **KP_RESET_SHUTDOWN**.

    Note: Firmware must be loaded into device first.
    Note: KL720 does NOT support this feature.

    ```bash
    $ python3 GenericCommand.py --target KL520 --port 33 --cmd shutdown

    [Check Device]
    - success
    [Connect Device]
    - target device: 'KL520'
    - scan index: '0'
    - port ID: '33'
    - command: 'shutdown'
    [Shutdown Device]
    - shutdown command success.
    ```

---

## 5. Inference API Examples

The PLUS provides two categories of API set for model inference.

1. [Generic Image Inference](#51-generic-inference-example)
2. [Generic Data Inference](#51-generic-inference-example)
3. Customized Inference (C Language Only)

The main difference between **Generic Inference** and **Customized Inference** is shown below:

1. Generic Image Inference:
    - Input: Image
    - Pre-process: Auto Hardware Pre-process on Device
    - Post-process: None on Device

2. Generic Data Inference:
    - Input: Data (Absolutely aligned model input)
    - Pre-process: None on Device
    - Post-process: None on Device

3. Customized Inference (C Language Only):
    - Input: Image or Data (Based on pre-process user defined on device)
    - Pre-process: User Developed Pre-process, Auto Hardware Pre-process, or None on Device
    - Post-process: User Developed Post-process, or None on Device

![](../imgs/generic_customized_diff.png)

Below will demonstrate only usage in two examples for **Generic Image inference** and **Generic Data inference**. For **Customized inference (C Language Only)**, please refer the [**C language documents**](../../plus_c/feature_guide/customized_api/introduction.md).

### 5.1 Generic Inference Example  

**Generic Inference** includes two sets of APIs, **Generic Image Inference API** and **Generic Data Inference API**.  

For the detail introduction, please refer the documents in [Generic Inference](./../feature_guide/chapter/generic_inference.md).  

---

## 6. Multiple Threads Usage Example

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

## 7. Drop Frame Usage Example

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

## 8. Model Zoo Examples

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

---

## 9. Device Memory Usage Control Example

This example is to show how to configure the `kp.DdrManageAttributes` and the usage of `kp.core.store_ddr_management_attributes()`.

Please refer [Device DDR Management](../feature_guide/chapter/device_ddr_management.md) for more information.

```bash
$ python3 KL520DemoGenericImageInferenceFifoqConfig.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Setting DDR Manager Attributes]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 10 times
 - ..........
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
        "[[[[  1.3589103    0.33972758   0.5095914  ...   0.16986379",
        "      0.33972758  -0.849319  ]",
        "   [  1.698638    -0.5095914    0.5095914  ...  -0.16986379",
        "     -0.16986379  -0.849319  ]",
        "   [  1.5287741    0.5095914    0.16986379 ...   0.",
        "     -0.33972758  -0.5095914 ]",
        "   ...",
        "   [ -7.643871    -9.682237   -10.361691   ...  -9.002781",
        "    -10.021964    -9.172645  ]",
        "   [ -7.304143   -10.701419   -12.400057   ...  -9.682237",
        "     -9.682237    -9.002781  ]",
        "   [ -6.1150966   -8.153462    -9.342508   ...  -7.983598",
        "     -8.153462    -8.49319   ]]]]"
    ]
}, {
    "width": 14,
    "height": 14,
    "channel": 255,
    "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
    "num_data": 49980,
    "ndarray": [
        "[[[[  0.87369454  -0.3494778   -0.1747389  ...   0.",
        "     -0.1747389   -0.6989556 ]",
        "   [  0.6989556   -0.87369454  -0.6989556  ...  -0.5242167",
        "     -0.1747389   -0.5242167 ]",
        "   [  0.5242167   -0.87369454  -0.6989556  ...  -0.1747389",
        "      0.1747389   -0.87369454]",
        "   ...",
        "   [-11.18329    -15.377024   -18.172846   ... -13.105417",
        "    -12.581201   -10.833812  ]",
        "   [-10.134856   -14.1538515  -16.774935   ... -10.659073",
        "     -9.61064     -8.387467  ]",
        "   [ -9.086423   -12.231723   -12.930678   ... -10.134856",
        "     -9.261162    -7.339034  ]]]]"
    ]
}]
```
