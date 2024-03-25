# Firmware Configuration

When SCPU activates NCPU to run models, **kmdw_inference_app_config_t** (KL520/KL720) or **VMF_NNM_INFERENCE_APP_CONFIG_T** (KL630/KL730), which contains configurations of NCPU, is required to pass to NCPU.

**kmdw_inference_app_config_t** and **VMF_NNM_INFERENCE_APP_CONFIG_T** contain following configurable options:

- **image_buf**:
    - type: void *
    - The buffer address of the image.

- **image_width**:
    - type: uint32_t
    - The width of the image.

- **image_height**:
    - type: uint32_t
    - The height of the image.

- **image_channel**:
    - type: uint32_t
    - The channel count of the image.

- **image_resize**:
    - type: uint32_t
    - This is used for image resize in pre-process.
    - Please refer to **kp_resize_mode_t**.

- **image_padding**:
    - type: uint32_t
    - This is used for image padding in pre-process.
    - Please refer to **kp_padding_mode_t**.

- **image_format**:
    - type: uint32_t
    - This is used for color space conversion in pre-process.
    - Please refer to **kp_image_format_t**.

- **image_norm**:
    - type: uint32_t
    - This is used for data normalization in pre-process.
    - Please refer to **kp_normalize_mode_t**.

- **bypass_pre_proc**:
    - type: bool
    - If this is true, NCPU will **NOT** execute the pre-process. The size, channel, format, ... of the input image must be exactly the same as the requirement of the model.
    - If this is true, **image_width**, **image_height**, **image_channel**, **image_resize**, **image_padding**, **image_format**, and **image_norm** will be ignored.
    - If this is true, **image_buf_size** must be provided correctly.

- **image_buf_size**:
    - type: uint32_t
    - The size of image buffer.
    - This is only used when **bypass_pre_proc** is true.

- **model_id**:
    - type: int
    - The ID of the target model to be inferenced in NCPU.

- **enable_crop**:
    - type: bool
    - Whether crop a partial area of the image to be inferenced.
    - If this is true, **crop_area** must be set properly.

- **crop_area**:
    - type: kp_inf_crop_box_t
    - The cropping area of the image to be inferrenced.

- **enable_raw_output**:
    - type: bool
    - If this is true, NCPU does not execute the post-process. The post-process may need to be execute at the software on the host server.
    - If this is false, NCPU will execute the post-process. The customized post-process must be registered via **kdpio_post_processing_register()**.

- **enable_parallel**:
    - type: bool
    - This is only available when single model is adapted and the post-process is executed in NCPU.
    - When one inference is in the post-process, the next inference will be start parallelly.
    - After one inference is fully finished, the callback function set to **result_callback** will be invoked.

-  **result_callback**:
    - type [KL520/KL720]: kmdw_inference_result_callback_t
    - type [KL630/KL730]: VMF_NNM_INFERENCE_APP_RESULT_CALLBACK_T
    - The callback function for parallel mode

-  **inf_result_buf**:
    - type: void*
    - This only works for parallel mode to carry it back to user callback function.

- **ncpu_result_buf**
    - type: void*
    - The buffer address where NCPU put the inference result.
    - It will be passed to **result_callback** under parallel mode.

- **pad_value**:
    - type: kp_pad_value_t*
    - The pad_value for the pre-processing in NCPU.

- **user_define_data** (KL520/KL720/KL630)
    - type: void*
    - The user define data for the pre-processing and post-processing in NCPU.

- **pre_proc_config** (KL730)
    - type: void*
    - The user define data for the pre-processing in NCPU.

- **post_proc_config** (KL730)
    - type: void*
    - The user define data for the post-processing in NCPU.

- **pre_proc_func** (KL630/KL730)
    - type: void*
    - The pointer for the customized pre-processing function.

- **post_proc_func** (KL630/KL730)
    - type: void*
    - The pointer for the customized post-processing function.
