## Quickstart for beginners

This short introduction use **`kp`** to build simple edge AI application by following steps:

1. [Connect Kneron device](#connect-the-device-and-get-kneron-device-handler-device-group)
2. [Upload SCPU/NCPU firmware](#upload-firmware-to-kneron-device)
3. [Upload NEF model](#upload-nef-model-to-kneron-device)
4. [Inference image](#inference-image)

**Note 1**: Please using pip to install **`kp`** API and **`opencv-python`** before the following tutorial. See the [Installation
](../../introduction/install_dependency.md) for details.  

**Note 2**: Please using **`kneronDFUT`** to upgrade firmware from **KDP** to **KDP2** before the following tutorial. See the [Upgrade AI Device to KDP2
](../../introduction/upgrade_ai_device_to_kdp2.md) for details.

---

### Import **`kp`** and **`cv2`** into your program:

```python
import kp
import cv2
```

---

### Get one Kneron device USB port ID for connecting:

```python
device_descriptors = kp.core.scan_devices()

if 0 < device_descriptors.device_descriptor_number:
    usb_port_id = device_descriptors.device_descriptor_list[0].usb_port_id
else:
    print('Error: no Kneron device connect.')
    exit(0)
```

---

### Connect the device and get Kneron device handler (Device Group):

```python
device_group = kp.core.connect_devices(usb_port_ids=[usb_port_id])
```

---

### Set timeout of the USB communication (Default: infinity wait):

```python
kp.core.set_timeout(device_group=device_group,
                    milliseconds=5000)
```

---

### Upload firmware to Kneron device:
> Please replace `SCPU_FW_PATH`, `NCPU_FW_PATH` by kdp2_fw_scpu.bin and kdp2_fw_ncpu.bin path (Please find target device firmware under `res/firmware` folder)  

```python
SCPU_FW_PATH = 'res/firmware/KL520/kdp2_fw_scpu.bin'
NCPU_FW_PATH = 'res/firmware/KL520/kdp2_fw_ncpu.bin'
kp.core.load_firmware_from_file(device_group=device_group,
                                scpu_fw_path=SCPU_FW_PATH,
                                ncpu_fw_path=NCPU_FW_PATH)
```

---

### Upload NEF model to Kneron device:
> Please replace `MODEL_FILE_PATH` by models_520.nef path (Please find target device NEF model under `res/models` folder)  

```python
MODEL_FILE_PATH = 'res/models/KL520/tiny_yolo_v3/models_520.nef'
model_nef_descriptor = kp.core.load_model_from_file(device_group=device_group,
                                                    file_path=MODEL_FILE_PATH)
```

---

### Inference image:
- Read image from disk
    > Please replace `IMAGE_FILE_PATH` by image path (Example image can be found under `res/images` folder)
    ```python
    IMAGE_FILE_PATH = 'res/images/bike_cars_street_224x224.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)
    ```

- Prepare generic inference configuration
    ```python
    generic_raw_image_header = kp.GenericRawImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
        padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
        normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
        inference_number=0
    )
    ```

- Start inference work
    ```python
    kp.inference.generic_raw_inference_send(device_group=device_group,
                                            generic_raw_image_header=generic_raw_image_header,
                                            image=img_bgr565,
                                            image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)

    generic_raw_result = kp.inference.generic_raw_inference_receive(device_group=device_group,
                                                                    generic_raw_image_header=generic_raw_image_header,
                                                                    model_nef_descriptor=model_nef_descriptor)
    ```

- Retrieve inference node output
    ```python
    inf_node_output_list = []

    for node_idx in range(generic_raw_result.header.num_output_node):
        inference_float_node_output = kp.inference.generic_inference_retrieve_float_node(node_idx=node_idx,
                                                                                         generic_raw_result=generic_raw_result,
                                                                                         channels_ordering=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
        inf_node_output_list.append(inference_float_node_output)

    print(inf_node_output_list)

    '''
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
    '''
    ```