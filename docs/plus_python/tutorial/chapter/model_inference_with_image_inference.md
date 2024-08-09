## Model Inference - Image Inference  

This tutorial shows how to inference image data by Kneron devices **with built-in hardware image pre-processing**. The `kp` module support following image inference interfaces:  

1. [Inference general format image](#inference-general-format-image)
2. [Inference binary image data](#inference-binary-image-data)

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

---

**Reference Examples**:  

- `KL520DemoGenericImageInference.py`  
- `KL630DemoGenericImageInference.py`  
- `KL720DemoGenericImageInference.py`  
- `KL730DemoGenericImageInference.py`

### Inference general format image:
Kneron PLUS support **`BGR565`**, **`BGRA8888`**, **`RAW8 (Grayscale)`** numpy.ndarray (dtype=numpy.uint8, dim=3) image inference.  

> * More supported image format information please reference [Supported Image Format](../../../plus_c/appendix/supported_image_format.md)  

> * Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    * Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    * Please make sure the input image meet the following requirements for **hardware image preprocessing** :  
        1. The `input image size` must be large than the model input size. (Only for KL520)  
        2. The `width of input image` must be multiple of 4. (Only for KL520)  
        3. The `padding limitation` after keep aspect ratio resize to model input size:  
            * KL520 left/right/top/bottom 127  
            * KL720 left/right/top/bottom 255  
        4. Limitation of the resize destination size for KL720:
            * Width < 1023
            * Hight < 2047

    ```python
    IMAGE_FILE_PATH = 'res/images/bike_cars_street_224x224.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)
    ```

- Prepare generic image inference input descriptor  

    ```python
    generic_inference_input_descriptor = kp.GenericImageInferenceDescriptor(
        model_id=model_nef_descriptor.models[0].id,
        inference_number=0,
        input_node_image_list=[
            kp.GenericInputNodeImage(
                image=img_bgr565,
                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565,
                resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
                padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
                normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON
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
                    "[[[165  73]",
                    "  [230  81]",
                    "  [177 172]",
                    "",
                    " ...",
                    "",
                    "  [240 123]",
                    "  [ 16 124]",
                    "  [ 49 132]]]"
                ],
                "width": 224,
                "height": 224,
                "image_format": "ImageFormat.KP_IMAGE_FORMAT_RGB565",
                "resize_mode": "ResizeMode.KP_RESIZE_ENABLE",
                "padding_mode": "PaddingMode.KP_PADDING_CORNER",
                "normalize_mode": "NormalizeMode.KP_NORMALIZE_KNERON",
                "crop_count": "0",
                "inference_crop_box_list": {}
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

    - Receive inference raw result from connected Kneron devices
        ```python
        generic_raw_result = kp.inference.generic_image_inference_receive(device_group=device_group)
        ```

    - Simply show GenericImageInferenceResult
        ```python
        print(generic_raw_result)

        '''
        {
            "header": {
                "inference_number": 0,
                "crop_number": 0,
                "num_output_node": 2,
                "product_id": 256,
                "num_hw_pre_proc_info": 1,
                "hw_pre_proc_info_list": {
                    "0": {
                        "img_width": 224,
                        "img_height": 224,
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
                            "width": 0,
                            "height": 0
                        }
                    }
                }
            },
            "raw_result": {
                "buffer_size": 86180
            }
        }
        '''
        ```

        Above shows kp.GenericImageInferenceResult results, a brief description listed below.

        - **inference_number** : Inference sequence number.
        - **crop_number** : Crop box sequence number.
        - **num_output_node** : Total number of output nodes.
        - **product_id** : USB PID (Product ID).
        - **num_hw_pre_proc_info** : Total number of floating-point values.
        - **hw_pre_proc_info_list** : Hardware pre-process information for each input node, refer to kp.HwPreProcInfo.
        - **raw_result** : Inference raw result buffer.

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
        "name": "",
        "shape": [
            1,
            255,
            7,
            7
        ],
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
        "name": "",
        "shape": [
            1,
            255,
            14,
            14
        ],
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
    '''
    ```

    Above shows kp.InferenceFloatNodeOutput results, a brief description listed below.

    - **name** : Name of the tensor.
    - **shape** : ONNX shape of the tensor.
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW, KP_CHANNEL_ORDERING_DEFAULT)

---

### Inference binary image data:
Kneron PLUS support **`BGR565`**, **`BGRA8888`**, **`RAW8 (Grayscale)`**, **`YCbCr422 (YUYV422)`** bytes data inference.

> More supported image format information please reference [Supported Image Format](../../../plus_c/appendix/supported_image_format.md)  

- Read RGB565 image from disk  

    * Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    * Please make sure the input image meet the following requirements for **hardware image preprocessing** :  
        1. The `input image size` must be large than the model input size. (Only for KL520)  
        2. The `width of input image` must be multiple of 4. (Only for KL520)  
        3. The `padding limitation` after keep aspect ratio resize to model input size:  
            * KL520 left/right/top/bottom 127  
            * KL720 left/right/top/bottom 255  
        4. Limitation of the resize destination size (Only for KL720):
            * Width < 1023
            * Hight < 2047

    ```python
    IMAGE_FILE_PATH = '../../res/images/bike_cars_street_224x224_rgb565.bin'

    with open(IMAGE_FILE_PATH, 'rb') as file:
        img_bgr565 = file.read()
    ```

- Prepare generic image inference input descriptor
    ```python
    generic_inference_input_descriptor = kp.GenericImageInferenceDescriptor(
        model_id=model_nef_descriptor.models[0].id,
        inference_number=0,
        input_node_image_list=[
            kp.GenericInputNodeImage(
                image=img_bgr565,
                width=224,
                height=224,
                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565,
                resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
                padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
                normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON
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
                    "[[[165  73]",
                    "  [230  81]",
                    "  [177 172]",
                    "",
                    " ...",
                    "",
                    "  [240 123]",
                    "  [ 16 124]",
                    "  [ 49 132]]]"
                ],
                "width": 224,
                "height": 224,
                "image_format": "ImageFormat.KP_IMAGE_FORMAT_RGB565",
                "resize_mode": "ResizeMode.KP_RESIZE_ENABLE",
                "padding_mode": "PaddingMode.KP_PADDING_CORNER",
                "normalize_mode": "NormalizeMode.KP_NORMALIZE_KNERON",
                "crop_count": "0",
                "inference_crop_box_list": {}
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

    - Receive inference raw result from connected Kneron devices
        ```python
        generic_raw_result = kp.inference.generic_image_inference_receive(device_group=device_group)
        ```

    - Simply show GenericImageInferenceResult
        ```python
        print(generic_raw_result)

        '''
        {
            "header": {
                "inference_number": 0,
                "crop_number": 0,
                "num_output_node": 2,
                "product_id": 256,
                "num_hw_pre_proc_info": 1,
                "hw_pre_proc_info_list": {
                    "0": {
                        "img_width": 224,
                        "img_height": 224,
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
                            "width": 0,
                            "height": 0
                        }
                    }
                }
            },
            "raw_result": {
                "buffer_size": 86180
            }
        }
        '''
        ```

        Above shows kp.GenericImageInferenceResult results, a brief description listed below.

        - **inference_number** : Inference sequence number.
        - **crop_number** : Crop box sequence number.
        - **num_output_node** : Total number of output nodes.
        - **product_id** : USB PID (Product ID).
        - **num_hw_pre_proc_info** : Total number of floating-point values.
        - **hw_pre_proc_info_list** : Hardware pre-process information for each input node, refer to kp.HwPreProcInfo.
        - **raw_result** : Inference raw result buffer.

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
        "name": "",
        "shape": [
            1,
            255,
            7,
            7
        ],
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
        "name": "",
        "shape": [
            1,
            255,
            14,
            14
        ],
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
    '''
    ```

    Above shows **`kp.InferenceFloatNodeOutput`** results, a brief description listed below.

    - **name** : Name of the tensor.
    - **shape** : ONNX shape of the tensor.
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW, KP_CHANNEL_ORDERING_DEFAULT)
