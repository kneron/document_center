## Model Inference - Inference on Cropped Regions  

This tutorial shows how to inference model with **Generic Inference** with cropped regions. The **crop configuration** will do cropping image on device, execute inference only on the cropped areas of image, get the raw output from device, and does post-processing in the software.  

The flow in concept:  

1. Setting crop information in `kp.GenericRawImageHeader`  
2. Send an image to inference  
3. Receive result *N* times (*N* specify for number of crop bounding boxes)  

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

**Reference Examples**:  

- `KL520DemoGenericInferenceCrop.py`  
- `KL720DemoGenericInferenceCrop.py`  

---

### Inference on Cropped Regions  

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    ```python
    IMAGE_FILE_PATH = 'res/images/bike_cars_street_224x224.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)
    ```

- Prepare generic inference configuration with **`cropped box configuration`**

    ```python
    crop_box_list = [
        kp.InferenceCropBox(
            crop_box_index=0,
            x=0,
            y=0,
            width=400,
            height=400
        ),
        kp.InferenceCropBox(
            crop_box_index=1,
            x=230,
            y=335,
            width=450,
            height=450
        )
    ]

    generic_raw_image_header = kp.GenericRawImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
        padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
        normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
        inference_number=0,
        inference_crop_box_list=crop_box_list
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
            "crop_count": 2,
            "inference_crop_box_list": {
                "0": {
                    "crop_box_index": 0,
                    "x": 0,
                    "y": 0,
                    "width": 400,
                    "height": 400
                },
                "1": {
                    "crop_box_index": 1,
                    "x": 230,
                    "y": 335,
                    "width": 450,
                    "height": 450
                }
            }
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

    - Receive **`crop_count`** times of inference raw result from connected Kneron devices

        ```python
        generic_crop_raw_result_list = []

        for idx in range(generic_raw_image_header.crop_count):
            generic_raw_result = kp.inference.generic_raw_inference_receive(device_group=device_group,
                                                                            generic_raw_image_header=generic_raw_image_header,
                                                                            model_nef_descriptor=model_nef_descriptor)
            generic_crop_raw_result_list.append(generic_raw_result)
        ```

- Retrieve inference node output of each cropped area inference raw result  

    ```python
    crop_inference_float_node_output_list = []

    for generic_raw_result in generic_crop_raw_result_list:

        inference_float_node_output_list = []

        for node_idx in range(generic_raw_result.header.num_output_node):
            inference_float_node_output_list.append(
                kp.inference.generic_inference_retrieve_float_node(node_idx=node_idx,
                                                                   generic_raw_result=generic_raw_result,
                                                                   channels_ordering=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW))
        crop_inference_float_node_output_list.append(inference_float_node_output_list)

    print(crop_inference_float_node_output_list)

    '''
    [[{ # 1th crop box result
        "width": 7,
        "height": 7,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  1.698638    -0.16986379   0.33972758 ...  -0.67945516",
            "     -0.16986379  -0.67945516]",
            "   [  1.8685017    0.16986379  -0.33972758 ...  -0.16986379",
            "      0.16986379  -2.547957  ]",
            "   [  1.3589103    1.0191827   -0.67945516 ...   0.16986379",
            "      0.67945516  -2.2082293 ]",
            "   ...",
            "   [  1.0191827    1.698638     0.16986379 ...   0.16986379",
            "     -0.849319    -0.67945516]",
            "   [  1.5287741   -0.849319     1.0191827  ...   0.849319",
            "     -1.5287741   -0.50959134]",
            "   [  1.1890465   -0.16986379  -0.16986379 ...   0.849319",
            "     -0.67945516  -0.50959134]]",
            "",
            "  ...",
            "",
            "  [[ -6.9644156   -7.304143    -7.1342793  ...  -6.794552",
            "     -6.794552    -6.454824  ]",
            "   [ -6.9644156   -8.6630535   -9.342508   ...  -9.682236",
            "     -8.49319     -6.794552  ]",
            "   [ -7.8137345  -10.871283   -12.569921   ... -12.400057",
            "    -10.871283    -8.6630535 ]",
            "   ...",
            "   [ -8.323326   -11.890466   -15.797333   ... -18.515154",
            "    -15.627469   -10.531555  ]",
            "   [ -7.983598   -10.701419   -12.909648   ... -17.49597",
            "    -14.438422    -9.852099  ]",
            "   [ -7.6438704   -8.6630535   -9.852099   ... -10.871283",
            "     -8.832917    -6.9644156 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  0.5242167   0.1747389   0.        ...   0.5242167  -0.3494778",
            "     -0.6989556]",
            "   [  0.1747389  -0.3494778   0.5242167 ...   0.3494778  -0.5242167",
            "     -0.3494778]",
            "   [  0.1747389  -0.3494778   0.1747389 ...   0.1747389   0.1747389",
            "      0.3494778]",
            "   ...",
            "   [ -1.0484334  -0.6989556  -0.5242167 ...   0.          0.1747389",
            "      0.3494778]",
            "   [ -1.0484334  -0.6989556  -0.3494778 ...  -0.1747389   0.1747389",
            "      0.       ]",
            "   [  0.1747389  -0.6989556   0.        ...   0.         -0.1747389",
            "     -0.5242167]]",
            "",
            "  ...",
            "",
            "  [[ -9.261162  -10.833812  -10.134856  ... -12.231723  -12.231723",
            "    -10.134856 ]",
            "   [-12.231723  -15.202284  -13.105417  ... -15.027545  -13.979112",
            "    -11.358028 ]",
            "   [-12.581201  -16.600195  -14.678067  ... -15.7265005 -13.280156",
            "    -10.833812 ]",
            "   ...",
            "   [-15.7265005 -19.22128   -17.998106  ... -11.18329    -9.785378",
            "     -9.61064  ]",
            "   [-13.979112  -17.823368  -17.124413  ...  -9.086423   -8.736945",
            "     -9.435901 ]",
            "   [ -9.785378  -13.629634  -13.280156  ...  -8.03799    -8.03799",
            "     -8.562206 ]]]]"
        ]
    }], [{ # 2th crop box result
        "width": 7,
        "height": 7,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  1.8685017    0.67945516  -0.67945516 ...  -0.33972758",
            "      0.16986379  -0.50959134]",
            "   [  1.8685017    0.67945516   0.50959134 ...  -0.849319",
            "      0.67945516  -1.0191827 ]",
            "   [  1.5287741   -0.33972758   2.2082293  ...  -1.1890465",
            "      0.849319    -1.1890465 ]",
            "   ...",
            "   [  1.698638     0.849319     2.2082293  ...  -1.8685017",
            "      0.50959134  -0.50959134]",
            "   [  1.5287741    0.67945516   2.0383654  ...  -1.0191827",
            "      0.50959134  -0.67945516]",
            "   [  0.849319     0.16986379   0.50959134 ...  -0.16986379",
            "      0.16986379  -0.50959134]]",
            "",
            "  ...",
            "",
            "  [[ -6.2849603   -6.794552    -7.304143   ...  -8.49319",
            "     -7.4740067   -7.304143  ]",
            "   [ -6.9644156   -6.9644156   -6.9644156  ...  -7.4740067",
            "     -7.304143    -7.6438704 ]",
            "   [ -6.9644156   -7.6438704   -8.6630535  ...  -8.153461",
            "     -9.002781    -7.8137345 ]",
            "   ...",
            "   [ -7.6438704  -11.550737   -12.400057   ...  -9.172645",
            "     -7.983598    -7.6438704 ]",
            "   [ -7.304143   -11.21101    -12.739784   ...  -9.852099",
            "     -7.6438704   -7.304143  ]",
            "   [ -7.304143    -7.8137345   -8.153461   ...  -7.304143",
            "     -6.794552    -6.9644156 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  1.2231723  -0.5242167   0.1747389 ...   0.1747389   0.",
            "      0.       ]",
            "   [  0.6989556  -0.8736945   0.5242167 ...  -0.1747389   0.",
            "      0.       ]",
            "   [  0.         -0.3494778   0.        ...  -0.3494778   0.",
            "      0.6989556]",
            "   ...",
            "   [ -1.2231723  -0.5242167  -0.3494778 ...   0.3494778   0.",
            "      1.0484334]",
            "   [ -0.6989556  -0.3494778  -0.1747389 ...   0.1747389  -0.3494778",
            "      0.8736945]",
            "   [  0.6989556  -0.5242167  -0.3494778 ...   0.6989556   0.",
            "      0.1747389]]",
            "",
            "  ...",
            "",
            "  [[ -8.562206  -11.18329   -13.280156  ... -11.008551  -10.134856",
            "     -8.562206 ]",
            "   [-10.833812  -14.503328  -15.202284  ... -13.629634  -12.7559395",
            "    -10.134856 ]",
            "   [ -9.960117  -13.979112  -15.377023  ... -13.804373  -13.105417",
            "    -10.833812 ]",
            "   ...",
            "   [-13.629634  -16.949673  -16.600195  ...  -7.6885114  -7.1642947",
            "     -6.2906003]",
            "   [-12.231723  -14.852806  -14.153851  ...  -6.465339   -6.2906003",
            "     -5.591645 ]",
            "   [ -9.960117  -12.056984  -11.707506  ...  -6.1158614  -5.9411225",
            "     -5.067428 ]]]]"
        ]
    }]]
    '''
    ```

    Above shows **`kp.InferenceFloatNodeOutput`** results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.
