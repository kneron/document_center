## Model Inference - Inference on Cropped Regions  

This tutorial shows how to inference model with **Generic Inference** with cropped regions. The **crop configuration** will do cropping image on device, execute inference only on the cropped areas of image, get the raw output from device, and does post-processing in the software.  

The flow in concept:  

1. Setting crop information in `kp.GenericImageInferenceDescriptor`  
2. Send an image to inference  
3. Receive result *N* times (*N* specify for number of crop bounding boxes)  

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

**Reference Examples**:  

- `KL520DemoGenericImageInferenceCrop.py`  
- `KL720DemoGenericImageInferenceCrop.py`  

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

- Prepare generic image inference input descriptor with **`cropped box configuration`**

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

    generic_inference_input_descriptor = kp.GenericImageInferenceDescriptor(
        model_id=model_nef_descriptor.models[0].id,
        inference_number=0,
        input_node_image_list=[
            kp.GenericInputNodeImage(
                image=img_bgr565,
                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565,
                resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
                padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
                normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
                inference_crop_box_list=crop_box_list
            )
        ]
    )

    print(generic_inference_input_descriptor)

    '''
    {
        "model_id": 19,
        "inference_number": 0,
        "input_node_image_num": 1,
        "input_node_image_list": {
            "0": {
                "image": [
                    "[[[ 61 231]",
                    "  [ 61 231]",
                    "  [ 61 231]",
                    "",
                    " ...",
                    "",
                    "  [113 148]",
                    "  [146 148]",
                    "  [146 148]]]"
                ],
                "width": 800,
                "height": 800,
                "image_format": "ImageFormat.KP_IMAGE_FORMAT_RGB565",
                "resize_mode": "ResizeMode.KP_RESIZE_ENABLE",
                "padding_mode": "PaddingMode.KP_PADDING_CORNER",
                "normalize_mode": "NormalizeMode.KP_NORMALIZE_KNERON",
                "crop_count": "2",
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
    }
    '''
    ```

    Above shows GenericImageInferenceDescriptor configurations, a brief description listed below.

    - **image** : Inference image in data bytes or numpy.ndarray (dtype=numpy.uint8, dim=3) format.
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
        kp.inference.generic_image_inference_send(device_group=device_group,
                                                  generic_inference_input_descriptor=generic_inference_input_descriptor)
        ```

    - Receive **`crop_count`** times of inference raw result from connected Kneron devices

        ```python
        generic_crop_raw_result_list = []

        for idx in range(generic_raw_image_header.crop_count):
            generic_raw_result = kp.inference.generic_image_inference_receive(device_group=device_group)
            generic_crop_raw_result_list.append(generic_raw_result)
        ```

    - Simply show list of GenericImageInferenceResult
        ```python
        print(generic_crop_raw_result_list)

        '''
        [{ # 1th crop box
            "header": {
                "inference_number": 0,
                "crop_number": 0,
                "num_output_node": 2,
                "product_id": 256,
                "num_hw_pre_proc_info": 1,
                "hw_pre_proc_info_list": {
                    "0": {
                        "img_width": 400,
                        "img_height": 400,
                        "resized_img_width": 224,
                        "resized_img_height": 224,
                        "pad_top": 0,
                        "pad_bottom": 0,
                        "pad_left": 0,
                        "pad_right": 0,
                        "model_input_width": 224,
                        "model_input_height": 224,
                        "crop_area": {
                            "crop_box_index": 0,
                            "x": 0,
                            "y": 0,
                            "width": 400,
                            "height": 400
                        }
                    }
                }
            },
            "raw_result": {
                "buffer_size": 86076
            }
        }, { # 2th crop box
            "header": {
                "inference_number": 0,
                "crop_number": 1,
                "num_output_node": 2,
                "product_id": 256,
                "num_hw_pre_proc_info": 1,
                "hw_pre_proc_info_list": {
                    "0": {
                        "img_width": 452,
                        "img_height": 452,
                        "resized_img_width": 224,
                        "resized_img_height": 224,
                        "pad_top": 0,
                        "pad_bottom": 0,
                        "pad_left": 0,
                        "pad_right": 0,
                        "model_input_width": 224,
                        "model_input_height": 224,
                        "crop_area": {
                            "crop_box_index": 1,
                            "x": 228,
                            "y": 334,
                            "width": 452,
                            "height": 452
                        }
                    }
                }
            },
            "raw_result": {
                "buffer_size": 86076
            }
        }]
        '''
        ```

        Above shows list of GenericImageInferenceResult results, a brief description listed below.

        - **inference_number** : Inference sequence number.
        - **crop_number** : Crop box sequence number.
        - **num_output_node** : Total number of output nodes.
        - **product_id** : USB PID (Product ID).
        - **num_hw_pre_proc_info** : Total number of floating-point values.
        - **hw_pre_proc_info_list** : Hardware pre-process information for each input node, refer to kp.HwPreProcInfo.
        - **raw_result** : Inference raw result buffer.

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
    [[{ # 1th crop box
        "width": 7,
        "height": 7,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  1.698638    -0.16986379   0.33972758 ...  -0.67945516",
            "     -0.16986379  -0.67945516]",
            "   [  1.8685018    0.16986379  -0.33972758 ...  -0.16986379",
            "      0.16986379  -2.547957  ]",
            "   [  1.3589103    1.0191828   -0.67945516 ...   0.16986379",
            "      0.67945516  -2.2082293 ]",
            "   ...",
            "   [ -8.323326   -11.890466   -15.797333   ... -18.515154",
            "    -15.627469   -10.531555  ]",
            "   [ -7.983598   -10.701419   -12.909648   ... -17.495972",
            "    -14.438422    -9.8521    ]",
            "   [ -7.643871    -8.6630535   -9.8521     ... -10.871283",
            "     -8.832917    -6.9644156 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  0.5242167    0.1747389    0.         ...   0.5242167",
            "     -0.3494778   -0.6989556 ]",
            "   [  0.1747389   -0.3494778    0.5242167  ...   0.3494778",
            "     -0.5242167   -0.3494778 ]",
            "   [  0.1747389   -0.3494778    0.1747389  ...   0.1747389",
            "      0.1747389    0.3494778 ]",
            "   ...",
            "   [-15.726501   -19.22128    -17.998106   ... -11.18329",
            "     -9.785378    -9.61064   ]",
            "   [-13.979113   -17.823368   -17.124413   ...  -9.086423",
            "     -8.736945    -9.435901  ]",
            "   [ -9.785378   -13.629634   -13.280156   ...  -8.03799",
            "     -8.03799     -8.562206  ]]]]"
        ]
    }], [{ # 2th crop box
        "width": 7,
        "height": 7,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 12495,
        "ndarray": [
            "[[[[  1.8685018    0.67945516  -0.67945516 ...   0.",
            "      0.          -0.67945516]",
            "   [  1.698638     0.5095914    0.5095914  ...  -0.849319",
            "      0.67945516  -1.0191828 ]",
            "   [  1.3589103   -0.5095914    2.0383656  ...  -1.1890466",
            "      0.849319    -1.1890466 ]",
            "   ...",
            "   [ -7.8137345  -11.720602   -12.909648   ... -10.191828",
            "     -8.323326    -7.983598  ]",
            "   [ -7.1342793  -11.041146   -13.249376   ... -10.191828",
            "     -7.983598    -7.474007  ]",
            "   [ -7.304143    -8.49319     -9.002781   ...  -7.983598",
            "     -6.9644156   -6.9644156 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  1.2231723   -0.5242167    0.         ...   0.1747389",
            "     -0.1747389    0.        ]",
            "   [  0.6989556   -0.6989556    0.         ...  -0.1747389",
            "     -0.1747389    0.        ]",
            "   [  0.          -0.6989556    0.         ...  -0.1747389",
            "      0.1747389    0.5242167 ]",
            "   ...",
            "   [-13.979113   -17.648628   -17.124413   ...  -7.513773",
            "     -6.814817    -5.9411225 ]",
            "   [-12.930678   -15.726501   -14.503329   ...  -6.465339",
            "     -6.1158614   -5.591645  ]",
            "   [-10.484334   -12.581201   -11.532767   ...  -6.814817",
            "     -6.2906003   -5.067428  ]]]]"
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
