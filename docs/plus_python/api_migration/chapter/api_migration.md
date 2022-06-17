## Migrate from Kneron PLUS 1.x to Kneron PLUS 2

This chapter shows how to migrate your code from Kneron PLUS V1.x to Kneron PLUS V2. Before getting started, please reference the [APIs V1 and V2 Mapping Table](./api_migration_mapping_table.md) for mapping V1.x to V2 API. The major migration process is:  

1. [Rewrite model information access usage](#1-rewrite-model-information-access-usage)  
2. [Replace inference usage](#2-replace-inference-usage)  
3. [(Option) Replace built-in YOLO post process function](#3-option-replace-built-in-yolo-post-process-function)  

---

### 1. Rewrite model information access usage  

In Kneron PLUS 1.x, the `kp.ModelNefDescriptor` provides basic and essential information about loaded models, such as model ID, model input size, and model raw output size. It is clear and easy to use.  

But some API usage, such as using data inference (without hardware image pre-processing) needs more model information (e.g. model input NPU data layout, model input quantization parameters ...) to deal with software pre-processing on the host PC.  

To provide more model information, we redesign the `kp.ModelNefDescriptor` in the Kneron PLUS 2.  

- Change model input size access usage  

    - V1.x

        ```python
        ...

        model_nef_descriptor = kp.core.load_model_from_file(device_group=device_group,
                                                            file_path=MODEL_FILE_PATH)

        model_input_channel = model_nef_descriptor.models[0].channel
        model_input_height = model_nef_descriptor.models[0].height
        model_input_width = model_nef_descriptor.models[0].width

        ...
        ```

    - V2

        ```python
        ...

        model_nef_descriptor = kp.core.load_model_from_file(device_group=device_group,
                                                            file_path=MODEL_FILE_PATH)

        /* shape order: BxCxHxW */
        model_input_channel = model_nef_descriptor.models[0].input_nodes[0].shape_npu[1]
        model_input_height = model_nef_descriptor.models[0].input_nodes[0].shape_npu[2]
        model_input_width = model_nef_descriptor.models[0].input_nodes[0].shape_npu[3]

        ...
        ```

    **Note**: For new information added in `kp.ModelNefDescriptor`, please reference `kp.ModelNefDescriptor` definition.  

### 2. Replace inference usage  

#### 2.1. Change **Generic Raw Inference** to **Generic Image Inference**  

1. Replace inference header

    - V1.x

        ```python
        ...

        """
        prepare the image
        """
        import cv2
        img = cv2.imread(filename=IMAGE_FILE_PATH)
        img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)

        """
        prepare generic raw inference image descriptor
        """
        generic_raw_image_header = kp.GenericRawImageHeader(
            model_id=model_nef_descriptor.models[0].id,
            resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
            padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
            normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
            inference_number=0
        )

        ...
        ```

    - V2

        ```python
        ...

        """
        prepare the image
        """
        import cv2
        img = cv2.imread(filename=IMAGE_FILE_PATH)
        img_bgr565 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2BGR565)

        """
        prepare generic image inference input descriptor
        """
        generic_inference_input_descriptor = kp.GenericImageInferenceDescriptor(
            model_id=model_nef_descriptor.models[0].id,
            inference_number=0,
            input_node_image_list=[
                kp.GenericInputNodeImage(
                    image=img_bgr565,
                    image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565
                )
            ]
        )

        ...
        ```

2. Replace inference send and receive function

    - V1.x

        ```python
        ...

        kp.inference.generic_raw_inference_send(device_group=device_group,
                                                generic_raw_image_header=generic_raw_image_header,
                                                image=img_bgr565,
                                                image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)

        generic_raw_result = kp.inference.generic_raw_inference_receive(device_group=device_group,
                                                                        generic_raw_image_header=generic_raw_image_header,
                                                                        model_nef_descriptor=model_nef_descriptor)

        ...
        ```

    - V2

        ```python
        ...

        kp.inference.generic_image_inference_send(device_group=device_group,
                                                  generic_inference_input_descriptor=generic_inference_input_descriptor)

        generic_raw_result = kp.inference.generic_image_inference_receive(device_group=device_group)

        ...
        ```

#### 2.2. Change **Generic Raw Inference Bypass Pre-Processing** to **Generic Data Inference**  

1. Replace inference header  

    - V1.x

        ```python
        ...

        """
        prepare the normalized RGBA8888 binary data
        """
        with open(IMAGE_FILE_PATH, 'rb') as file:
            img_buffer = file.read()


        """
        prepare generic raw inference bypass pre-processing image descriptor
        """
        generic_raw_image_header = kp.v1.GenericRawBypassPreProcImageHeader(
            model_id=model_nef_descriptor.models[0].id,
            image_buffer_size=len(img_buffer),
            inference_number=0
        )

        ...
        ```

    - V2

        ```python
        ...

        """
        prepare the normalized RGBA8888 binary data
        """
        with open(IMAGE_FILE_PATH, 'rb') as file:
            img_buffer = file.read()

        """
        prepare generic data inference input descriptor
        """
        generic_inference_input_descriptor = kp.GenericDataInferenceDescriptor(
            model_id=model_nef_descriptor.models[0].id,
            inference_number=0,
            input_node_data_list=[kp.GenericInputNodeData(buffer=img_buffer)]
        )

        ...
        ```

2. Replace inference send and receive function  

    - V1.x

        ```python
        ...

        kp.inference.generic_raw_inference_bypass_pre_proc_send(
            device_group=device_group,
            generic_raw_image_header=generic_raw_image_header,
            image_buffer=img_buffer)

        generic_raw_bypass_pre_proc_result = kp.inference.generic_raw_inference_bypass_pre_proc_receive(
            device_group=device_group,
            generic_raw_image_header=generic_raw_image_header,
            model_nef_descriptor=model_nef_descriptor)


        ...
        ```

    - V2

        ```python
        ...

        kp.inference.generic_data_inference_send(device_group=device_group,
                                                 generic_inference_input_descriptor=generic_inference_input_descriptor)

        generic_raw_result = kp.inference.generic_data_inference_receive(device_group=device_group)

        ...
        ```

### 3. (Option) Replace built-in YOLO post process function  

- Rewrite `post_process_tiny_yolo_v3()` input parameters

    - V1.x

        ```python
        ...

        """
        post-process the last raw output
        """
        yolo_result = post_process_tiny_yolo_v3(inference_float_node_output_list=inf_node_output_list,
                                                image_width=generic_raw_image_header.width,
                                                image_height=generic_raw_image_header.height, thresh_value=0.2)



        ...
        ```

    - V2

        ```python
        ...

        """
        post-process the last raw output
        """
        yolo_result = post_process_tiny_yolo_v3(inference_float_node_output_list=inf_node_output_list,
                                                hardware_preproc_info=generic_raw_result.header.hw_pre_proc_info,
                                                thresh_value=0.2)

        ...
        ```

- Rewrite `post_process_yolo_v5()` input parameters

    - V1.x

        ```python
        ...

        """
        post-process the last raw output
        """
        yolo_result = post_process_yolo_v5(inference_float_node_output_list=inf_node_output_list,
                                            image_width=generic_raw_image_header.width,
                                            image_height=generic_raw_image_header.height,
                                            thresh_value=0.2)


        ...
        ```

    - V2

        ```python
        ...

        """
        post-process the last raw output
        """
        yolo_result = post_process_yolo_v5(inference_float_node_output_list=inf_node_output_list,
                                            hardware_preproc_info=generic_raw_result.header.hw_pre_proc_info_list[0],
                                            thresh_value=0.2)

        ...
        ```

**Note**: For more  information of YOLO post processing parameters update, please reference `python/example/utils/ExamplePostProcess.py`  
