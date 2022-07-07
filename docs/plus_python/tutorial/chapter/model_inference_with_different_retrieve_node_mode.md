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
        "factor": 5.8870697021484375,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "dtype": "FixedPointDType.KP_FIXED_POINT_DTYPE_INT8",
        "num_data": 12495,
        "ndarray": [
            "[[[[  8   2   3 ...   1   2  -5]",
            "   [ 10  -3   3 ...  -1  -1  -5]",
            "   [  9   3   1 ...   0  -2  -3]",
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
        "factor": 5.7228240966796875,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "dtype": "FixedPointDType.KP_FIXED_POINT_DTYPE_INT8",
        "num_data": 49980,
        "ndarray": [
            "[[[[   5   -2   -1 ...    0   -1   -4]",
            "   [   4   -5   -4 ...   -3   -1   -3]",
            "   [   3   -5   -4 ...   -1    1   -5]",
            "   ...",
            "   ...",
            "   [ -64  -88 -104 ...  -75  -72  -62]",
            "   [ -58  -81  -96 ...  -61  -55  -48]",
            "   [ -52  -70  -74 ...  -58  -53  -42]]]]"
        ]
    }]
    ```

    Above shows `kp.InferenceFixedNodeOutput` results, a brief description listed below.

    - **width** : Width of output node.
    - **height** : Height of output node.
    - **channel** : Channel of output node.
    - **radix** : Radix for fixed/floating point conversion.
    - **scale** : Scale for fixed/floating point conversion.
    - **factor** : Conversion factor for fixed-point to floating-point conversion - formulation: scale * (2 ^ radix).
    - **channels_ordering** : Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)
    - **dtype** : fixed-point data type, refer to kp.FixedPointDType.
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
            "[[[[  1.35891032   0.33972758   0.5095914  ...   0.16986379",
            "      0.33972758  -0.84931898]",
            "   [  1.69863796  -0.5095914    0.5095914  ...  -0.16986379",
            "     -0.16986379  -0.84931898]",
            "   [  1.52877414   0.5095914    0.16986379 ...   0.",
            "     -0.33972758  -0.5095914 ]",
            "   ...",
            "   [ -7.64387083  -9.68223667 -10.36169147 ...  -9.00278091",
            "    -10.02196407  -9.17264462]",
            "   [ -7.30414295 -10.70141888 -12.40005684 ...  -9.68223667",
            "     -9.68223667  -9.00278091]",
            "   [ -6.11509657  -8.15346241  -9.34250832 ...  -7.98359823",
            "     -8.15346241  -8.49318981]]]]"
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
            "   [  0.6989556   -0.87369454  -0.6989556  ...  -0.52421671",
            "     -0.1747389   -0.52421671]",
            "   [  0.52421671  -0.87369454  -0.6989556  ...  -0.1747389",
            "      0.1747389   -0.87369454]",
            "   ...",
            "   [-11.18328953 -15.3770237  -18.17284584 ... -13.10541725",
            "    -12.5812006  -10.83381176]",
            "   [-10.13485622 -14.15385151 -16.77493477 ... -10.65907288",
            "     -9.61063957  -8.38746738]",
            "   [ -9.08642292 -12.23172283 -12.93067837 ... -10.13485622",
            "     -9.2611618   -7.33903408]]]]"
        ]
    }]
    '''
    ```
