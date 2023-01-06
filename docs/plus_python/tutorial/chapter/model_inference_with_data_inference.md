## Model Inference - Data Inference  

In some application fields, the model input data cannot leverage image inference (with built-in hardware image pre-processing). In this case, data inference (without built-in hardware image pre-processing) would be the best solution.  

This tutorial shows how to inference none image data (raw data) by Kneron devices **without built-in hardware image pre-processing**.  

In order to infer without hardware image preprocessing, the input data must do the following steps for fitting NPU input format:  

1. Normalization  
2. Quantization (convert to 8-bit fixed point)  
3. Re-layout data to fit NPU data layout format  

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model](./load_nef_model.md) for details.  

---

**Reference Examples**:  

- `KL520DemoGenericDataInference.py`  
- `KL630DemoGenericDataInference.py`  
- `KL720DemoGenericDataInference.py`  

### Inference without Built-In Hardware Image Pre-Processing

> Recommend use **`cv2`** to read the image or capture camera frame.  

- Read image from disk  

    > Please replace `IMAGE_FILE_PATH` by image path. (Example image can be found under `res/images` folder)  

    ```python
    import cv2

    IMAGE_FILE_PATH = 'res/images/one_bike_many_cars_608x608.bmp'

    img = cv2.imread(filename=IMAGE_FILE_PATH)
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
    ```

- Do Preprocessing at Software (Host side)  

    - Get required model/data information  


        ```python
        # get input image size
        img_height, img_width, img_channel = img.shape

        # get model input radix, scale, refer to QuantizationParameters
        model_input_radix = model_nef_descriptor.models[0].input_nodes[0].quantization_parameters.quantized_fixed_point_descriptor_list[0].radix
        model_input_scale = model_nef_descriptor.models[0].input_nodes[0].quantization_parameters.quantized_fixed_point_descriptor_list[0].scale

        # get model input data layout, refer to ModelTensorDataLayout
        model_input_data_layout = model_nef_descriptor.models[0].input_nodes[0].data_layout

        # get model input size (shape order: BxCxHxW), refer to TensorDescriptor
        model_input_channel = model_nef_descriptor.models[0].input_nodes[0].shape_npu[1]
        model_input_height = model_nef_descriptor.models[0].input_nodes[0].shape_npu[2]
        model_input_width = model_nef_descriptor.models[0].input_nodes[0].shape_npu[3]
        ```

    - Do normalization (Depend on model training)  

        ```python
        # do normalization - this model is trained with normalize method: (data - 128) / 256
        data = img.astype(np.int32)
        data = (data - 128) / 256.0
        ```

    - Quantization (convert to 8-bit fixed point)  

        ```python
        # toolchain calculate the radix value from input data (after normalization), and set it into NEF model.
        # NPU will divide input data "2^radix" automatically, so, we have to scaling the input data here due to this reason.
        data *= (np.power(2, model_input_radix) * model_input_scale)
        data = np.round(data)
        data = np.clip(data, -128, 127).astype(np.int8)
        ```

    - Re-layout data to fit NPU data layout format  
        - For KL520  

            > 1. More information about *NPU data layout format*,please refer to [Supported NPU Data Layout Format](../../../plus_c/appendix/supported_npu_data_layout_format.md)  
            > 2. For the KL520 hardware limitation, the '4W' in '4W4C8B' need to be width aligned to 16  

            ```python
            # re-layout the data to fit NPU data layout format
            # KL520 supported NPU input layout format: 4W4C8B
            # [Note] For the KL520 hardware limitation, the '4W' need to be width aligned to 16

            if kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B == model_input_data_layout:
                width_align_base = 16
                channel_align_base = 4
            else:
                print(' - Error: invalid input NPU layout format {}'.format(str(model_input_data_layout)))
                exit(0)

            # calculate width alignment size, channel block count
            model_input_width_align = width_align_base * math.ceil(model_input_width / float(width_align_base))
            model_input_channel_block_num = math.ceil(model_input_channel / float(channel_align_base))

            # create re-layout data container
            # KL520 dimension order: HxCxW
            re_layout_data = np.zeros((model_input_height,
                                    model_input_channel_block_num,
                                    model_input_width_align,
                                    channel_align_base), dtype=np.int8)

            # fill data in re-layout data container
            model_input_channel_block_offset = 0
            for model_input_channel_block_idx in range(model_input_channel_block_num):
                model_input_channel_block_offset_end = model_input_channel_block_offset + channel_align_base
                model_input_channel_block_offset_end = model_input_channel_block_offset_end if model_input_channel_block_offset_end < model_input_channel else model_input_channel

                re_layout_data[:model_input_height, model_input_channel_block_idx, :model_input_width, :(model_input_channel_block_offset_end - model_input_channel_block_offset)] = \
                    data[:, :, model_input_channel_block_offset:model_input_channel_block_offset_end]

                model_input_channel_block_offset += channel_align_base

            # convert re-layout data to npu inference buffer
            npu_input_buffer = re_layout_data.tobytes()
            ```

        - For KL630

            > More information about *NPU data layout format*, please refer to [Supported NPU Data Layout Format](../../../plus_c/appendix/supported_npu_data_layout_format.md)  

            ```python
            # re-layout the data to fit NPU data layout format
            # KL720 supported NPU input layout format: 4W4C8B, 1W16C8B, 16W1C8B

            if kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B == model_input_data_layout:
                width_align_base = 4
                channel_align_base = 4
            elif kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_1W16C8B == model_input_data_layout:
                width_align_base = 1
                channel_align_base = 16
            elif kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B == model_input_data_layout:
                width_align_base = 16
                channel_align_base = 1
            else:
                print(' - Error: invalid input NPU layout format {}'.format(str(model_input_data_layout)))
                exit(0)

            # calculate width alignment size, channel block count
            model_input_width_align = width_align_base * math.ceil(model_input_width / float(width_align_base))
            model_input_channel_block_num = math.ceil(model_input_channel / float(channel_align_base))

            # create re-layout data container
            # KL630 dimension order: CxHxW
            re_layout_data = np.zeros((model_input_channel_block_num,
                                    model_input_height,
                                    model_input_width_align,
                                    channel_align_base), dtype=np.int8)

            # fill data in re-layout data container
            model_input_channel_block_offset = 0
            for model_input_channel_block_idx in range(model_input_channel_block_num):
                model_input_channel_block_offset_end = model_input_channel_block_offset + channel_align_base
                model_input_channel_block_offset_end = model_input_channel_block_offset_end if model_input_channel_block_offset_end < model_input_channel else model_input_channel

                re_layout_data[model_input_channel_block_idx, :model_input_height, :model_input_width, :(model_input_channel_block_offset_end - model_input_channel_block_offset)] = \
                    data[:, :, model_input_channel_block_offset:model_input_channel_block_offset_end]

                model_input_channel_block_offset += channel_align_base

            # convert re-layout data to npu inference buffer
            npu_input_buffer = re_layout_data.tobytes()
            ```

        - For KL720

            > More information about *NPU data layout format*, please refer to [Supported NPU Data Layout Format](../../../plus_c/appendix/supported_npu_data_layout_format.md)  

            ```python
            # re-layout the data to fit NPU data layout format
            # KL720 supported NPU input layout format: 4W4C8B, 1W16C8B, 16W1C8B

            if kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B == model_input_data_layout:
                width_align_base = 4
                channel_align_base = 4
            elif kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_1W16C8B == model_input_data_layout:
                width_align_base = 1
                channel_align_base = 16
            elif kp.ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B == model_input_data_layout:
                width_align_base = 16
                channel_align_base = 1
            else:
                print(' - Error: invalid input NPU layout format {}'.format(str(model_input_data_layout)))
                exit(0)

            # calculate width alignment size, channel block count
            model_input_width_align = width_align_base * math.ceil(model_input_width / float(width_align_base))
            model_input_channel_block_num = math.ceil(model_input_channel / float(channel_align_base))

            # create re-layout data container
            # KL720 dimension order: CxHxW
            re_layout_data = np.zeros((model_input_channel_block_num,
                                    model_input_height,
                                    model_input_width_align,
                                    channel_align_base), dtype=np.int8)

            # fill data in re-layout data container
            model_input_channel_block_offset = 0
            for model_input_channel_block_idx in range(model_input_channel_block_num):
                model_input_channel_block_offset_end = model_input_channel_block_offset + channel_align_base
                model_input_channel_block_offset_end = model_input_channel_block_offset_end if model_input_channel_block_offset_end < model_input_channel else model_input_channel

                re_layout_data[model_input_channel_block_idx, :model_input_height, :model_input_width, :(model_input_channel_block_offset_end - model_input_channel_block_offset)] = \
                    data[:, :, model_input_channel_block_offset:model_input_channel_block_offset_end]

                model_input_channel_block_offset += channel_align_base

            # convert re-layout data to npu inference buffer
            npu_input_buffer = re_layout_data.tobytes()
            ```

- Prepare generic data inference input descriptor
    ```python
    generic_inference_input_descriptor = kp.GenericDataInferenceDescriptor(
        model_id=model_nef_descriptor.models[0].id,
        inference_number=0,
        input_node_data_list=[kp.GenericInputNodeData(buffer=npu_input_buffer)]
    )
    ```

- Start inference work
    - Send data to connected Kneron devices for data inference
        ```python
        kp.inference.generic_data_inference_send(device_group=device_group,
                                                    generic_inference_input_descriptor=generic_inference_input_descriptor)

        ```
    - Receive data inference raw result from connected Kneron devices
        ```python
        generic_raw_result = kp.inference.generic_data_inference_receive(device_group=device_group)
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
            "[[[[  1.3589103    0.33972758   0.33972758 ...   0.33972758",
            "      0.33972758  -0.849319  ]",
            "   [  1.698638    -0.33972758   0.5095914  ...  -0.16986379",
            "     -0.16986379  -0.849319  ]",
            "   [  1.5287741    0.5095914    0.16986379 ...   0.",
            "     -0.33972758  -0.5095914 ]",
            "   ...",
            "   [ -7.474007    -9.512373   -10.361691   ...  -8.832917",
            "     -9.8521      -8.832917  ]",
            "   [ -7.304143   -10.871283   -12.569921   ...  -9.8521",
            "     -9.8521      -9.002781  ]",
            "   [ -6.1150966   -8.153462    -9.342508   ...  -8.153462",
            "     -8.323326    -8.6630535 ]]]]"
        ]
    }, {
        "width": 14,
        "height": 14,
        "channel": 255,
        "channels_ordering": "ChannelOrdering.KP_CHANNEL_ORDERING_CHW",
        "num_data": 49980,
        "ndarray": [
            "[[[[  0.87369454  -0.3494778    0.         ...   0.1747389",
            "     -0.1747389   -0.6989556 ]",
            "   [  0.6989556   -0.87369454  -0.5242167  ...  -0.5242167",
            "     -0.1747389   -0.5242167 ]",
            "   [  0.5242167   -0.87369454  -0.5242167  ...   0.",
            "      0.          -0.6989556 ]",
            "   ...",
            "   [-10.484334   -15.202285   -18.347586   ... -13.105417",
            "    -12.7559395  -10.659073  ]",
            "   [ -9.61064    -13.804374   -16.774935   ... -11.18329",
            "    -10.484334    -8.911684  ]",
            "   [ -8.736945   -11.882245   -12.581201   ... -10.833812",
            "     -9.960117    -7.8632507 ]]]]"
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
