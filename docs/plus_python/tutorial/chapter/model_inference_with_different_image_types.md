## Model Inference - Image Types  

This tutorial shows how to inference model by Kneron devices in following two types image:  

1. [Inference general format image](#inference-general-format-image)
2. [Inference binary image data](#inference-binary-image-data)

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

---

### Inference general format image:
Kneron PLUS support **`BGR565`**, **`BGRA8888`**, **`Grayscale`** numpy.ndarray image inference.  

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    * Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    * Please make sure the input image meet the following requirements for hardware image preprocessing :  
        1. The `input image size` must be large than the model input size. (Only for KL520)  
        2. The `width of input image` must be multiple of 4. (Only for KL520)  
        3. The `padding limitation` after keep aspect ratio resize to model input size:  
            * KL520 left/right/top/bottom 127  
            * KL720 left/right/top/bottom 255  

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

    print(generic_raw_image_header)

    '''
    {
        "image": {
            "width": 0,
            "height": 0,
            "image_format": "ImageFormat.KP_IMAGE_FORMAT_RGB565"
        },
        "inference_configuration": {
            "resize_mode": "ResizeMode.KP_RESIZE_ENABLE",
            "padding_mode": "PaddingMode.KP_PADDING_CORNER",
            "normalize_mode": "NormalizeMode.KP_NORMALIZE_KNERON",
            "inference_number": 0,
            "model_id": 19,
            "crop_count": 0,
            "inference_crop_box_list": {}
        }
    }
    '''
    ```

    Above shows GenericRawImageHeader configurations, a brief description listed below.

    - **width** : Inference image width. (Required when inference binary image data)
    - **height** : Inference image height. (Required when inference binary image data)
    - **image_format** : Inference image format, refer to kp.ImageFormat.
    - **resize_mode** : Preprocess resize mode, refer to ResizeMode.
    - **padding_mode** : Preprocess padding mode, refer to PaddingMode.
    - **normalize_mode** : Inference normalization, refer to NormalizeMode.
    - **inference_number** : Inference sequence number, for reordering multiple Kneron device inference results.
    - **model_id** : Target inference model ID.
    - **crop_count** : Number of crop box in `inference_crop_box_list`.
    - **inference_crop_box_list** : Box information to crop.

- Start inference work
    - Send image to connected Kneron devices for inference
        ```python
        kp.inference.generic_raw_inference_send(device_group=device_group,
                                                generic_raw_image_header=generic_raw_image_header,
                                                image=img_bgr565,
                                                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)
        ```
    - Receive inference raw result from connected Kneron devices
        ```python
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

    Above shows kp.InferenceFloatNodeOutput results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.

---

### Inference binary image data:
Kneron PLUS support **`BGR565`**, **`BGRA8888`**, **`Grayscale`** numpy.ndarray image inference.

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read RGB565 image from disk  

    * Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    * Please make sure the input image meet the following requirements for hardware image preprocessing :  
        1. The `input image size` must be large than the model input size. (Only for KL520)  
        2. The `width of input image` must be multiple of 4. (Only for KL520)  
        3. The `padding limitation` after keep aspect ratio resize to model input size:  
            * KL520 left/right/top/bottom 127  
            * KL720 left/right/top/bottom 255  

    ```python
    IMAGE_FILE_PATH = '../../res/images/bike_cars_street_224x224_rgb565.bin'

    with open(IMAGE_FILE_PATH, 'rb') as file:
        img_bgr565 = file.read()
    ```

- Prepare generic inference configuration
    ```python
    generic_raw_image_header = kp.GenericRawImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
        padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
        normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
        inference_number=0,
        width=224,
        height=224
    )

    print(generic_raw_image_header)

    '''
    {
        "image": {
            "width": 224,
            "height": 224,
            "image_format": "ImageFormat.KP_IMAGE_FORMAT_RGB565"
        },
        "inference_configuration": {
            "resize_mode": "ResizeMode.KP_RESIZE_ENABLE",
            "padding_mode": "PaddingMode.KP_PADDING_CORNER",
            "normalize_mode": "NormalizeMode.KP_NORMALIZE_KNERON",
            "inference_number": 0,
            "model_id": 19,
            "crop_count": 0,
            "inference_crop_box_list": {}
        }
    }
    '''
    ```

    Above shows kp.GenericRawImageHeader configurations, a brief description listed below.

    - **width** : Inference image width. (Required when inference binary image data)
    - **height** : Inference image height. (Required when inference binary image data)
    - **image_format** : Inference image format, refer to kp.ImageFormat.
    - **resize_mode** : Preprocess resize mode, refer to ResizeMode.
    - **padding_mode** : Preprocess padding mode, refer to PaddingMode.
    - **normalize_mode** : Inference normalization, refer to NormalizeMode.
    - **inference_number** : Inference sequence number, for reordering multiple Kneron device inference results.
    - **model_id** : Target inference model ID.
    - **crop_count** : Number of crop box in `inference_crop_box_list`.
    - **inference_crop_box_list** : Box information to crop.

- Start inference work
    - Send image to connected Kneron devices for inference
        ```python
        kp.inference.generic_raw_inference_send(device_group=device_group,
                                                generic_raw_image_header=generic_raw_image_header,
                                                image=img_bgr565,
                                                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)
        ```
    - Receive inference raw result from connected Kneron devices
        ```python
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

    Above shows **`kp.InferenceFloatNodeOutput`** results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.
