## Model Inference - Inference without Pre-Processing  

This tutorial shows how to inference model without pre-processing in Kneron device  

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.  

**Reference Examples**:  

- `KL520DemoGenericInferenceBypassPreProc.py`  
- `KL720DemoGenericInferenceBypassPreProc.py`  

### Inference without Pre-Processing

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk
    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  
    ```python
    import cv2

    IMAGE_FILE_PATH = 'res/images/one_bike_many_cars_608x608.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    ```

- Do Image Preprocessing at Software (Host side)  
    In order to bypass preprocessing, input image must meet following requirements:  
    1. Input Width Alignment  
    The width of the NPU input data must be the least multiple of *N*, which is greater than the input width of the model.
        * KL520: *N* = 16
        * KL720: *N* = 4
        > **Note:** Those pixels over the model input size will not be inferenced.
    2. RGBA8888 Color Space  
    The image data format need to be converted to NPU inference formate RGBA8888 (32-bit)
    3. Normalization  
    User need to handel the normalization at software by following scripts:
        * KP_NORMALIZE_KNERON (RGB/256 - 0.5)
            ```python
            img_norm = img - 128
            ```
        * KP_NORMALIZE_TENSOR_FLOW (RGB/127.5 - 1.0)
            ```python
            img_norm = img - 128
            ```
        * KP_NORMALIZE_YOLO (RGB/255.0)
            ```python
            import numpy as np
            img_norm = (img / 2).astype(np.uint8)
            ```

    ```python
    platform = 'KL520'

    if platform == 'KL520':
        image_width_aligned = 16 * math.ceil(model_nef_descriptor.models[0].width / 16.0)
    elif platform == 'KL720':
        image_width_aligned = 4 * math.ceil(model_nef_descriptor.models[0].width / 4.0)

    model_input_height = model_nef_descriptor.models[0].height
    model_input_width = model_nef_descriptor.models[0].width
    model_input_channel = model_nef_descriptor.models[0].channel

    ''' prepare aligned NPU input data buffer '''
    img_aligned = np.zeros((model_input_width_aligned, model_input_height, model_input_channel), dtype=np.uint8)

    ''' resize / padding input data to model input size '''
    img_resized = cv2.resize(img, (model_input_width, model_input_height))

    ''' simulation of hardware KP_NORMALIZE_KNERON normalization (RGB/256 - 0.5) '''
    img_norm = img_resized - 128

    ''' fill input data to aligned NPU input data buffer '''
    img_aligned[:img_norm.shape[0], :img_norm.shape[1], :] = img_norm

    ''' change image color space to RGBA8888 '''
    img_aligned_bgra = cv2.cvtColor(src=img_aligned, code=cv2.COLOR_BGR2BGRA)

    ''' convert to binary buffer '''
    img_aligned_buffer = img_aligned_bgra.tobytes()
    ```

- Prepare generic inference configuration
    ```python
    generic_raw_image_header = kp.GenericRawBypassPreProcImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        image_buffer_size=len(img_aligned_buffer),
        inference_number=0
    )

    print(generic_raw_image_header)

    '''
    {
        "inference_number": 0,
        "model_id": 19,
        "image_buffer_size": 200704
    }
    '''
    ```

    Above shows `kp.GenericRawBypassPreProcImageHeader` configurations, a brief description listed below.

    - **inference_number** : Inference sequence number, for reordering multiple Kneron device inference results.
    - **model_id** : Target inference model ID.
    - **image_buffer_size** : Inference image buffer size.

- Start inference work
    - Send image to connected Kneron devices for bypass pre-processing inference
        ```python
        kp.inference.generic_raw_inference_bypass_pre_proc_send(
                device_group=device_group,
                generic_raw_image_header=generic_raw_image_header,
                image_buffer=img_aligned_buffer)
        ```
    - Receive bypass pre-processing inference raw result from connected Kneron devices
        ```python
        generic_raw_bypass_pre_proc_result = kp.inference.generic_raw_inference_bypass_pre_proc_receive(
                device_group=device_group,
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
            "[[[[ 0.849319    0.33972758 -0.33972758 ...  0.33972758 -0.16986379",
            "    -0.849319  ]",
            "   [ 1.1890465  -0.50959134 -0.16986379 ...  0.849319   -0.16986379",
            "    -1.0191827 ]",
            "   [ 1.1890465  -0.33972758 -0.16986379 ...  1.0191827  -0.33972758",
            "    -1.5287741 ]",
            "   ...",
            "   [ 2.0383654  -0.849319    1.0191827  ...  0.          0.",
            "    -2.547957  ]",
            "   [ 1.5287741  -0.67945516  0.67945516 ...  0.33972758 -0.849319",
            "    -1.0191827 ]",
            "   [ 0.67945516  0.          0.33972758 ...  0.67945516 -0.16986379",
            "    -0.50959134]]",
            "",
            "   ...",
            "",
            "  [[-7.4740067  -7.1342793  -7.983598   ... -8.49319    -8.153461",
            "    -7.8137345 ]",
            "   [-7.1342793  -8.323326   -9.682236   ... -8.832917   -7.6438704",
            "    -7.1342793 ]",
            "   [-7.304143   -8.153461   -7.983598   ... -8.323326   -7.8137345",
            "    -7.8137345 ]",
            "   ...",
            "   [-7.8137345  -8.832917   -7.983598   ... -6.794552   -6.9644156",
            "    -7.8137345 ]",
            "   [-6.454824   -6.794552   -6.794552   ... -6.1150966  -7.1342793",
            "    -7.6438704 ]",
            "   [-6.6246877  -6.2849603  -6.794552   ... -6.794552   -6.9644156",
            "    -7.4740067 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  0.8736945  -0.8736945  -0.3494778 ...  -0.1747389   0.1747389",
            "     -0.6989556]",
            "   [  0.5242167  -1.2231723  -0.1747389 ...  -0.5242167   0.",
            "     -0.3494778]",
            "   [  0.1747389  -1.3979112  -0.1747389 ...  -0.1747389   0.1747389",
            "     -0.3494778]",
            "   ...",
            "   [  0.6989556  -0.3494778  -0.1747389 ...   0.         -1.5726501",
            "      0.       ]",
            "   [  1.0484334   0.1747389  -0.3494778 ...   0.6989556   0.",
            "      0.1747389]",
            "   [  1.2231723   0.6989556  -0.6989556 ...   1.0484334   0.3494778",
            "     -0.8736945]]",
            "",
            "   ...",
            "",
            "  [[ -6.2906003  -8.562206   -9.261162  ...  -6.640078   -6.465339",
            "     -5.242167 ]",
            "   [ -7.8632503 -11.18329   -12.581201  ...  -9.61064    -7.8632503",
            "     -5.9411225]",
            "   [ -9.435901  -12.406462  -13.105417  ...  -9.785378   -8.911684",
            "     -7.3390336]",
            "   ...",
            "   [-10.309595  -11.882245  -10.134856  ...  -8.736945   -8.562206",
            "     -8.2127285]",
            "   [-11.18329   -11.882245  -10.309595  ...  -9.086423   -8.911684",
            "     -7.8632503]",
            "   [ -9.785378   -9.61064    -8.562206  ...  -7.8632503  -8.562206",
            "     -7.5137725]]]]"
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
