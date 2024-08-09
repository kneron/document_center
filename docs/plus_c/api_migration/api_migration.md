## Migrate from Kneron PLUS 1.x to Kneron PLUS 2 / 3

This chapter shows how to migrate your code from Kneron PLUS V1.x to Kneron PLUS V2. Before getting started, please reference the [APIs V1 and V2 / V3 Mapping Table](./api_migration_mapping_table.md) for mapping V1.x to V2 / V3 API. The major migration process is:

1. [Rewrite model information access usage](#1-rewrite-model-information-access-usage)
2. [Replace inference usage](#2-replace-inference-usage)
3. [(Option) Replace built-in YOLO post process function](#3-option-replace-built-in-yolo-post-process-function)

---

### 1. Rewrite model information access usage

In Kneron PLUS 1. x, the `kp_model_nef_descriptor_t` provides basic and essential information about loaded models, such as model ID, model input size, and model raw output size. It is clear and easy to use.

But some API usage, such as using data inference (without hardware image pre-processing) needs more model information (e.g. model input NPU data layout, model input quantization parameters ...) to deal with software pre-processing on the host PC.

To provide more model information, we redesign the `kp_model_nef_descriptor_t` in the Kneron PLUS 2.

- Change model input size access usage

    - V1.x

        ```c
        ...

        kp_model_nef_descriptor_t _model_desc;
        int ret = kp_load_model_from_file(_device, _model_file_path, &_model_desc);

        uint32_t model_input_channel = _model_desc.models[0].channel;
        uint32_t model_input_height = _model_desc.models[0].height;
        uint32_t model_input_width = _model_desc.models[0].width;

        ...
        ```

    - V2

        ```c
        ...

        kp_model_nef_descriptor_t _model_desc;
        int ret = kp_load_model_from_file(_device, _model_file_path, &_model_desc);

        /* shape order: BxCxHxW */
        uint32_t model_input_channel = _model_desc.models[0].input_nodes[0]->shape_npu[1];
        uint32_t model_input_height = _model_desc.models[0].input_nodes[0]->shape_npu[2];
        uint32_t model_input_width = _model_desc.models[0].input_nodes[0]->shape_npu[3];

        ...
        ```

    - V3

        ```c
        ...

        kp_model_nef_descriptor_t _model_desc;
        int ret = kp_load_model_from_file(_device, _model_file_path, &_model_desc);
        kp_tensor_descriptor_t *input_node_0 = &(_model_desc.models[0].input_nodes[0]);
        int shape_info_version = input_node_0->tensor_shape_info.version;

        if (KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1 == shape_info_version) {
            kp_tensor_shape_info_v1_t* tensor_shape_info    = &(input_node_0->tensor_shape_info.tensor_shape_info_data.v1);
            uint32_t npu_data_channel                       = tensor_shape_info->shape_npu[1];
            uint32_t npu_data_height                        = tensor_shape_info->shape_npu[2];
            uint32_t npu_data_width                         = tensor_shape_info->shape_npu[3];
            uint32_t onnx_data_channel                      = tensor_shape_info->shape_onnx[1];
            uint32_t onnx_data_height                       = tensor_shape_info->shape_onnx[2];
            uint32_t onnx_data_width                        = tensor_shape_info->shape_onnx[3];
        } else if (KP_MODEL_TENSOR_SHAPE_INFO_VERSION_2 == shape_info_version) {
            kp_tensor_shape_info_v2_t* tensor_shape_info    = &(input_node_0->tensor_shape_info.tensor_shape_info_data.v2);
            uint32_t onnx_data_channel                      = tensor_shape_info->shape[1];
            uint32_t onnx_data_height                       = tensor_shape_info->shape[2];
            uint32_t onnx_data_width                        = tensor_shape_info->shape[3];
        }

        ...
        ```

- Release `kp_model_nef_descriptor_t` by `kp_release_model_nef_descriptor()` in V2

    - V2 / V3

        ```c
        ...

        kp_model_nef_descriptor_t _model_desc;
        int ret = kp_load_model_from_file(_device, _model_file_path, &_model_desc);

        /* please release kp_model_nef_descriptor_t by kp_release_model_nef_descriptor */
        kp_release_model_nef_descriptor(&_model_desc);

        ...
        ```

    **Note**: For new information added in `kp_model_nef_descriptor_t`, please reference `kp_model_nef_descriptor_t` struct definition.

### 2. Replace inference usage

#### 2.1. Change **Generic Raw Inference** to **Generic Image Inference**

1. Replace inference header

    - V1.x

        ```c
        ...

        kp_generic_raw_image_header_t _input_desc;

        /******* prepare the image buffer read from file *******/
        // here convert a bmp file to RGB565 format buffer
        int _img_width, _img_height;
        char *_img_buf = helper_bmp_file_to_raw_buffer(_image_file_path, &_img_width, &_img_height, KP_IMAGE_FORMAT_RGB565);

        /******* set up the input descriptor *******/
        _input_desc.model_id = _model_desc.models[0].id;   // first model ID
        _input_desc.resize_mode = KP_RESIZE_ENABLE;        // enable resize in pre-process
        _input_desc.padding_mode = KP_PADDING_CORNER;      // enable corner padding in pre-process
        _input_desc.normalize_mode = KP_NORMALIZE_KNERON;  // this depends on models
        _input_desc.image_format = KP_IMAGE_FORMAT_RGB565; // image format
        _input_desc.width = _img_width;                    // image width
        _input_desc.height = _img_height;                  // image height
        _input_desc.inference_number = 0;                  // inference number, used to verify with output result
        _input_desc.crop_count = 0;                        // number of crop area, 0 means no cropping

        ...
        ```

    - V2 / V3

        ```c
        ...

        kp_generic_image_inference_desc_t _input_data;

        _input_data.model_id = _model_desc.models[0].id;    // first model ID
        _input_data.inference_number = 0;                   // inference number, used to verify with output result
        _input_data.num_input_node_image = 1;               // number of image

        /******* prepare the image buffer read from file *******/
        // here convert a bmp file to RGB565 format buffer
        int _img_width, _img_height;
        char *_img_buf = helper_bmp_file_to_raw_buffer(_image_file_path, &_img_width, &_img_height, KP_IMAGE_FORMAT_RGB565);

        /******* set up the input descriptor *******/
        _input_data.input_node_image_list[0].resize_mode = KP_RESIZE_ENABLE;        // enable resize in pre-process
        _input_data.input_node_image_list[0].padding_mode = KP_PADDING_CORNER;      // enable corner padding in pre-process
        _input_data.input_node_image_list[0].normalize_mode = KP_NORMALIZE_KNERON;  // this depends on models
        _input_data.input_node_image_list[0].image_format = KP_IMAGE_FORMAT_RGB565; // image format
        _input_data.input_node_image_list[0].width = _img_width;                    // image width
        _input_data.input_node_image_list[0].height = _img_height;                  // image height
        _input_data.input_node_image_list[0].crop_count = 0;                        // number of crop area, 0 means no cropping
        _input_data.input_node_image_list[0].image_buffer = (uint8_t *)_img_buf;    // buffer of image data

        ...
        ```

2. Replace inference send and receive function

    - V1.x

        ```c
        ...

        int ret;

        ret = kp_generic_raw_inference_send(_device, &_input_desc, (uint8_t *)_img_buf);
        if (ret != KP_SUCCESS)
            break;

        ret = kp_generic_raw_inference_receive(_device, &_output_desc, raw_output_buf, raw_buf_size);
        if (ret != KP_SUCCESS)
            break;

        ...
        ```

    - V2 / V3

        ```c
        ...

        int ret;

        ret = kp_generic_image_inference_send(_device, &_input_data);
        if (ret != KP_SUCCESS)
            break;

        ret = kp_generic_image_inference_receive(_device, &_output_desc, raw_output_buf, raw_buf_size);
        if (ret != KP_SUCCESS)
            break;

        ...
        ```

#### 2.2. Change **Generic Raw Inference Bypass Pre-Processing** to **Generic Data Inference**

1. Replace inference header

    - V1.x

        ```c
        ...

        kp_generic_raw_bypass_pre_proc_image_header_t _input_desc;

        /******* set up the input descriptor *******/
        _input_desc.model_id = _model_desc.models[0].id;    // first model ID
        _input_desc.inference_number = 0;                   // inference number, used to verify with output result
        _input_desc.image_buffer_size = _img_width * _img_height * 4;

        ...
        ```

    - V2 / V3

        ```c
        ...

        kp_generic_data_inference_desc_t _input_data;

        /******* prepare the image buffer read from file *******/
        // read normalized RGBA8888 binary data to buffer
        char *_img_buf = helper_bin_file_to_raw_buffer(_image_file_path, _img_width, _img_height, KP_IMAGE_FORMAT_RGBA8888);

        /******* set up the input descriptor *******/
        _input_data.input_node_data_list[0].buffer_size = re_layout_buf_size;
        _input_data.input_node_data_list[0].buffer = (uint8_t *)_img_buf;

        ...
        ```

2. Replace inference send and receive function

    - V1.x

        ```c
        ...

        /******* prepare the image buffer read from file *******/
        // read normalized RGBA8888 binary data to buffer
        char *_img_buf = helper_bin_file_to_raw_buffer(_image_file_path, _img_width, _img_height, KP_IMAGE_FORMAT_RGBA8888);

        int ret;

        ret = kp_generic_raw_inference_bypass_pre_proc_send(_device, &_input_desc, (uint8_t *)_img_buf);
        if (ret != KP_SUCCESS)
            break;

        ret = kp_generic_raw_inference_bypass_pre_proc_receive(_device, &_output_desc, raw_output_buf, raw_buf_size);
        if (ret != KP_SUCCESS)
            break;

        ...
        ```

    - V2 / V3

        ```c
        ...

        int ret;

        ret = kp_generic_data_inference_send(_device, &_input_data);
        if (ret != KP_SUCCESS)
            break;

        ret = kp_generic_data_inference_receive(_device, &_output_desc, raw_output_buf, raw_buf_size);
        if (ret != KP_SUCCESS)
            break;

        ...
        ```

### 3. (Option) Replace built-in YOLO post process function

* **KL520**

    - Rewrite `post_process_yolo_v3()` input parameters

        - V1.x

            ```c
            ...

            post_process_yolo_v3(output_nodes, _output_desc.num_output_node, _img_width, _img_height, 0.2, yolo_result);

            ...
            ```

        - V2 / V3

            ```c
            ...

            post_process_yolo_v3(output_nodes, _output_desc.num_output_node, &_output_desc.pre_proc_info[0], 0.2, yolo_result);

            ...
            ```

    - Rewrite `post_process_yolo_v5_520()` input parameters

        - V1.x

            ```c
            ...

            post_process_yolo_v5_520(output_nodes, _output_desc.num_output_node, _img_width, _img_height, 0.2, yolo_result);

            ...
            ```

        - V2 / V3

            ```c
            ...

            post_process_yolo_v5_520(output_nodes, _output_desc.num_output_node, &_output_desc.pre_proc_info[0], 0.2, yolo_result);

            ...
            ```

* **KL720**

    - Rewrite `post_process_yolo_v5_720()` input parameters

        - V1.x

            ```c
            ...

            post_process_yolo_v5_720(output_nodes, _output_desc.num_output_node, _img_width, _img_height, 0.15, yolo_result);

            ...
            ```

        - V2 / V3

            ```c
            ...

            post_process_yolo_v5_720(output_nodes, _output_desc.num_output_node, &_output_desc.pre_proc_info[0], 0.15, yolo_result);

            ...
            ```

**Note**: For more  information of YOLO post processing parameters update, please reference `kneron_plus/ex_common/postprocess.h`
