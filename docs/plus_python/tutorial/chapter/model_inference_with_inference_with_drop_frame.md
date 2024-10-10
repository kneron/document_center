## Model Inference - Inference with Drop Frame  

This tutorial shows how to inference model with drop frame configuration  

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

**Reference Examples**:  

- `KL520DemoCamGenericImageInferenceDropFrame.py`  
- `KL630DemoCamGenericImageInferenceDropFrame.py`  
- `KL720DemoCamGenericImageInferenceDropFrame.py`  
- `KL730DemoCamGenericImageInferenceDropFrame.py`  

### Inference with Drop Frame

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk
    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  
    ```python
    IMAGE_FILE_PATH = 'res/images/bike_cars_street_224x224.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)
    ```

- Setting inference configuration for **`enable drop frame`**
    ```python
    inference_configuration = kp.InferenceConfiguration(enable_frame_drop=True)

    kp.inference.set_inference_configuration(device_group=device_group,
                                             inference_configuration=inference_configuration)
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
    ```

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

    Above shows `kp.InferenceFloatNodeOutput` results, a brief description listed below.

    - **name** : Name of the tensor.
    - **shape** : ONNX shape of the tensor.
    - **num_data** : Total number of floating-point values.
    - **ndarray** : N-dimensional numpy.ndarray of feature map.
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW, KP_CHANNEL_ORDERING_DEFAULT)
