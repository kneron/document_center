# Firmware Configuration

When SCPU activates NCPU to run models, **kmdw_inference_app_config_t**, which contains configurations of NCPU, is required to pass to NCPU.

**kmdw_inference_app_config_t** contains following configurable options:

- void* **image_buf**:
    - The buffer address of the image.

- uint32_t **image_width**:
    - The width of the image.

- uint32_t **image_height**:
    - The height of the image.

- uint32_t **image_channel**:
    - The channel count of the image.

- uint32_t **image_resize**:
    - This is used for image resize in pre-process.
    - Please refer to **kp_resize_mode_t**.

- uint32_t **image_padding**:
    - This is used for image padding in pre-process.
    - Please refer to **kp_padding_mode_t**.

- uint32_t **image_format**:
    - This is used for color space conversion in pre-process.
    - Please refer to **kp_image_format_t**.

- uint32_t **image_norm**:
    - This is used for data normalization in pre-process.
    - Please refer to **kp_normalize_mode_t**.

- bool **bypass_pre_proc**:
    - If this is true, NCPU will **NOT** execute the pre-process. The size, channel, format, ... of the input image must be exactly the same as the requirement of the model.
    - If this is true, **image_width**, **image_height**, **image_channel**, **image_resize**, **image_padding**, **image_format**, and **image_norm** will be ignored.
    - If this is true, **image_buf_size** must be provided correctly.

- uint32_t **image_buf_size**:
    - The size of image buffer.
    - This is only used when **bypass_pre_proc** is true.

- int **model_id**:
    - The ID of the target model to be inferenced in NCPU.

- bool **enable_crop**:
    - Whether crop a partial area of the image to be inferenced.
    - If this is true, **crop_area** must be set properly.

- kp_inf_crop_box_t **crop_area**:
    - The cropping area of the image to be inferrenced.

- bool **enable_raw_output**:
    - If this is true, NCPU does not execute the post-process. The post-process may need to be execute at the software on the host server.
    - If this is false, NCPU will execute the post-process. The customized post-process must be registered via **kdpio_post_processing_register()**.

- bool **enable_parallel**:
    - This is only available when single model is adapted and the post-process is executed in NCPU.
    - When one inference is in the post-process, the next inference will be start parallelly.
    - After one inference is fully finished, the callback function set to **result_callback** will be invoked.

- kmdw_inference_result_callback_t **result_callback**:
    - The callback function for parallel mode

- void* **inf_result_buf**:
    - This only works for parallel mode to carry it back to user callback function.

- void* **ncpu_result_buf**
    - The buffer address where NCPU put the inference result.
    - It will be passed to **result_callback** under parallel mode.

- kp_pad_value_t* **pad_value**:
    - The pad_value for the pre-processing in NCPU.

- void* **user_define_data**
    - The user define data for the pre-processing in NCPU.
