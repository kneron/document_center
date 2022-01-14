## Model Inference - Retrieve Node Mode  

This tutorial shows how to inference model by Kneron devices in the following two retrieve node modes:  

1. [Retrieve floating-point node](#retrieve-floating-point-node)
2. [Retrieve fixed-point node](#retrieve-fixed-point-node)

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

---

### Retrieve floating-point node:

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  
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

- Retrieve inference node output with floating-point mode
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

    Above shows `kp.InferenceFloatNodeOutput` results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.

---

### Retrieve fixed-point node:  

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  
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

- Retrieve inference node output with fixed-point mode
    ```python
    inf_node_output_list = []

    for node_idx in range(generic_raw_result.header.num_output_node):
        inference_fixed_node_output = kp.inference.generic_inference_retrieve_fixed_node(node_idx=node_idx,
                                                                                        generic_raw_result=generic_raw_result,
                                                                                        channels_ordering=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
        inf_node_output_list.append(inference_fixed_node_output)

    print(inf_node_output_list)

    '''
    [{
        "width": 7,
        "height": 7,
        "channel": 255,
        "radix": 2,
        "scale": 1.4717674255371094,
        "factor": 0.16986379027366638,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  8   2   3 ...   1   2  -5]",
            "   [ 10  -3   3 ...  -1  -1  -5]",
            "   [  9   3   1 ...   0  -2  -3]",
            "   ...",
            "   [  8   9  -6 ...  15  -7  -4]",
            "   [  8  11  -6 ...   6  -4  -2]",
            "   [  5   5  -1 ...   1   1  -2]]",
            "",
            "  ...",
            "",
            "  [[-50 -55 -59 ... -60 -53 -45]",
            "   [-47 -59 -58 ... -54 -49 -39]",
            "   [-47 -60 -59 ... -48 -47 -43]",
            "   ...",
            "   [-45 -57 -61 ... -53 -59 -54]",
            "   [-43 -63 -73 ... -57 -57 -53]",
            "   [-36 -48 -55 ... -47 -48 -50]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "radix": 2,
        "scale": 1.4307060241699219,
        "factor": 0.17473889887332916,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[   5   -2   -1 ...    0   -1   -4]",
            "   [   4   -5   -4 ...   -3   -1   -3]",
            "   [   3   -5   -4 ...   -1    1   -5]",
            "   ...",
            "   [  -6    0    0 ...    2    2    1]",
            "   [  -4   -3   -1 ...    3    2    1]",
            "   [   1    0    1 ...    3    2    0]]",
            "",
            "  ...",
            "",
            "  [[ -43  -53  -56 ...  -61  -60  -49]",
            "   [ -60  -76  -84 ...  -87  -87  -63]",
            "   [ -64  -84  -87 ...  -92  -86  -70]",
            "   ...",
            "   [ -64  -88 -104 ...  -75  -72  -62]",
            "   [ -58  -81  -96 ...  -61  -55  -48]",
            "   [ -52  -70  -74 ...  -58  -53  -42]]]]"
        ]
    }]
    '''
    ```

    Above shows `kp.InferenceFixedNodeOutput` results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **radix** : Radix for fixed/floating point conversion.
    - **scale** : Scale for fixed/floating point conversion.
    - **factor** : Conversion factor for fixed-point to floating-point conversion - formula: 1 / (scale * (2 ^ radix)).
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.

- Convert `kp.InferenceFixedNodeOutput` results to `kp.InferenceFloatNodeOutput` results  
    ```python
    inf_floating_node_output_list = []

    for inf_node_output in inf_node_output_list:
        inf_floating_node_output_list.append(inf_node_output.to_float_node_output())

    print(inf_floating_node_output_list)

    '''
    [{
        "width": 7,
        "height": 7,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  1.35891032   0.33972758   0.50959134 ...   0.16986379",
            "      0.33972758  -0.84931898]",
            "   [  1.69863796  -0.50959134   0.50959134 ...  -0.16986379",
            "     -0.16986379  -0.84931898]",
            "   [  1.52877414   0.50959134   0.16986379 ...   0.",
            "     -0.33972758  -0.50959134]",
            "   ...",
            "   [  1.35891032   1.52877414  -1.01918268 ...   2.54795694",
            "     -1.1890465   -0.67945516]",
            "   [  1.35891032   1.86850166  -1.01918268 ...   1.01918268",
            "     -0.67945516  -0.33972758]",
            "   [  0.84931898   0.84931898  -0.16986379 ...   0.16986379",
            "      0.16986379  -0.33972758]]",
            "",
            "  ...",
            "",
            "  [[ -8.49318981  -9.34250832 -10.02196407 ... -10.19182777",
            "     -9.00278091  -7.64387035]",
            "   [ -7.98359823 -10.02196407  -9.85209942 ...  -9.17264462",
            "     -8.32332611  -6.62468767]",
            "   [ -7.98359823 -10.19182777 -10.02196407 ...  -8.15346146",
            "     -7.98359823  -7.30414295]",
            "   ...",
            "   [ -7.64387035  -9.68223572 -10.36169147 ...  -9.00278091",
            "    -10.02196407  -9.17264462]",
            "   [ -7.30414295 -10.70141888 -12.40005684 ...  -9.68223572",
            "     -9.68223572  -9.00278091]",
            "   [ -6.11509657  -8.15346146  -9.34250832 ...  -7.98359823",
            "     -8.15346146  -8.49318981]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  0.87369448  -0.3494778   -0.1747389  ...   0.",
            "     -0.1747389   -0.6989556 ]",
            "   [  0.6989556   -0.87369448  -0.6989556  ...  -0.52421671",
            "     -0.1747389   -0.52421671]",
            "   [  0.52421671  -0.87369448  -0.6989556  ...  -0.1747389",
            "      0.1747389   -0.87369448]",
            "   ...",
            "   [ -1.04843342   0.           0.         ...   0.3494778",
            "      0.3494778    0.1747389 ]",
            "   [ -0.6989556   -0.52421671  -0.1747389  ...   0.52421671",
            "      0.3494778    0.1747389 ]",
            "   [  0.1747389    0.           0.1747389  ...   0.52421671",
            "      0.3494778    0.        ]]",
            "",
            "  ...",
            "",
            "  [[ -7.51377249  -9.2611618   -9.78537846 ... -10.65907288",
            "    -10.48433399  -8.56220627]",
            "   [-10.48433399 -13.28015614 -14.67806721 ... -15.20228386",
            "    -15.20228386 -11.00855064]",
            "   [-11.18328953 -14.67806721 -15.20228386 ... -16.07597923",
            "    -15.02754498 -12.23172283]",
            "   ...",
            "   [-11.18328953 -15.37702274 -18.17284584 ... -13.10541725",
            "    -12.5812006  -10.83381176]",
            "   [-10.13485622 -14.15385056 -16.77493477 ... -10.65907288",
            "     -9.61063957  -8.38746738]",
            "   [ -9.08642292 -12.23172283 -12.93067837 ... -10.13485622",
            "     -9.2611618   -7.3390336 ]]]]"
        ]
    }]
    '''
    ```
