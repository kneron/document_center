# Create KL730 Single Model with Software NPU Format Convert Example

In this customized inference example, we will focus on converting source data into NPU format. Some specific model inputs in NPU format that cannot utilize the [Hardware Image Preprocessing](./../../appendix/hardware_image_preprocessing.md) conversion will use this example to learn how to perform the conversion manually.  

For more information about the NPU format and the hardware NPU data layout conversion support list, please refer to the [Hardware Image Preprocessing](./../../appendix/hardware_image_preprocessing.md#limitation) documentation.

---

## 1. Download Source Code

1. Download the latest **kneron_plus_vXXX.zip** into Windows/Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

2. Unzip kneron_plus_vXXX.zip

    Note: **{PLUS_FOLDER_PATH}** will be used below for representing the unzipped folder path of PLUS.

3. Please contact Kneron to obtain the latest **KL730_SDK_vXXX.zip**.

    Note: KL730 SDK can only be developed on Ubuntu

4. Unzip KL730_SDK_vXXX.zip

    Note: **{KL730_SDK_TOP_FOLDER_PATH}** will be used below for representing the unzipped folder path of KL730 Develop Package.

5. Unzip {KL730_SDK_TOP_FOLDER_PATH}/02_APP/02_Software_Tool_Kit/sdk_vX.X.X.tar.gz

    Note: **{KL730_SDK_FOLDER_PATH}** will be used below for representing the unzipped folder path of KL730 SDK.

---

## 2. PLUS (Software) Development

1. Create my_KL730_sin_with_sw_npu_fmt_cvt_example folder

    ```bash
    $ cd {PLUS_FOLDER_PATH}/examples/
    $ mkdir my_KL730_sin_with_sw_npu_fmt_cvt_example
    ```


2. Add *CMakelists.txt*

    ```bash
    # build with current *.c/*.cpp plus common source files in parent folder
    # executable name is current folder name.

    get_filename_component(app_name ${CMAKE_CURRENT_SOURCE_DIR} NAME)
    string(REPLACE " " "_" app_name ${app_name})

    file(GLOB local_src
        "*.c"
        "*.cpp"
        )

    set(common_src
        ../../ex_common/helper_functions.c
        )

    add_executable(${app_name}
        ${local_src}
        ${common_src})

    target_link_libraries(${app_name} ${KPLUS_LIB_NAME} ${USB_LIB} ${MATH_LIB} pthread)
    ```

3. Add *my_KL730_sin_with_sw_npu_fmt_cvt_example.h*

    - Please define the customized **header** structure and customized **result** structure in this file.

    - Header (my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t) is used for **sending** data to SCPU firmware. What kind of data should be contained can be customized based on the your requirement.

    - Result (my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t) is used for **receiving** data from SCPU firmware. What kind of data should be contained can be customized based on the output of model inference.

    - **kp_inference_header_stamp_t** must be contained in both header and result structures.

    - The **JOB_ID** describes the unique id of the task you want to execute in firmware, and it must be unique and above 1000.

    - This file should be synchronized with the .h file in SCPU firmware.

    ```cpp
    #pragma once

    #define MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID 4002
    #define YOLO_BOX_MAX                                    100

    typedef struct {
        uint32_t class_count;
        uint32_t box_count;
        kp_bounding_box_t boxes[YOLO_BOX_MAX];
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_yolo_result_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        my_KL730_sin_with_sw_npu_fmt_cvt_example_yolo_result_t yolo_result;
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t;
    ```

4. Add *my_KL730_sin_with_sw_npu_fmt_cvt_example.c*

    - There are 6 steps for inferencing in Kneron AI device:

        1. Connect Kneron AI device.

        2. Upload the firmware to AI device.

        3. Upload the model to AI device.

        4. Prepare data for the header.

        5. Send the header and image buffer to firmware via **kp_customized_inference_send()**.

        6. Receive the result from firmware via **kp_customized_inference_receive()**.

    - In this example, the **image** is transcoded into RGB565, and the width and height of the image is carried by the header.

    - Sending header and receiving result can be executed sequentially or on two different threads.

    ```cpp
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>

    #include "kp_core.h"
    #include "kp_inference.h"
    #include "helper_functions.h"

    #include "my_KL730_sin_with_sw_npu_fmt_cvt_example.h"

    static char _scpu_fw_path[128] = "../../res/firmware/KL730/kp_firmware.tar";
    static char _model_file_path[128] = "../../res/models/KL730/YoloV5s_640_640_3/models_730.nef";
    static char _image_file_path[128] = "../../res/images/one_bike_many_cars_608x608.bmp";
    static int _loop = 10;

    int main(int argc, char *argv[])
    {
        kp_device_group_t device;
        kp_model_nef_descriptor_t model_desc;
        int ret;

        /******* connect the device *******/
        {
            int port_id = 0; // 0 for one device auto-search
            int error_code;

            // internal parameter to indicate the desired port id
            if (argc > 1) {
                port_id = atoi(argv[1]);
            }

            // connect device
            device = kp_connect_devices(1, &port_id, &error_code);
            if (!device) {
                printf("connect device failed, port ID = '%d', error = '%d'\n", port_id, error_code);
                exit(0);
            }

            kp_set_timeout(device, 5000);
            printf("connect device ... OK\n");
        }

        /******* upload firmware to device *******/
        {
            ret = kp_load_firmware_from_file(device, _scpu_fw_path, NULL);
            if (ret != KP_SUCCESS) {
                printf("upload firmware failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload firmware ... OK\n");
        }

        /******* upload model to device *******/
        {
            ret = kp_load_model_from_file(device, _model_file_path, &model_desc);
            if (ret != KP_SUCCESS) {
                printf("upload model failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload model ... OK\n");
        }

        /******* prepare the image buffer read from file *******/
        // here convert a bmp file to RGB565 format buffer

        int img_width, img_height;
        char *img_buf = helper_bmp_file_to_raw_buffer(_image_file_path, &img_width, &img_height, KP_IMAGE_FORMAT_RGB565);

        if (!img_buf) {
            printf("read image file failed\n");
            exit(0);
        }

        printf("read image ... OK\n");
        printf("\nstarting inference loop %d times:\n", _loop);

        /******* prepare input and output header/buffers *******/
        my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t input_header;
        my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t output_result;

        input_header.header_stamp.job_id = MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID;
        input_header.header_stamp.total_image = 1;
        input_header.header_stamp.image_index = 0;
        input_header.img_width = img_width;
        input_header.img_height = img_height;

        int header_size = sizeof(my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t);
        int image_size = img_width * img_height * 2; // RGB565
        int result_size = sizeof(my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t);
        int recv_size = 0;

        /******* starting inference work *******/

        for (int i = 0; i < _loop; i++)
        {
            ret = kp_customized_inference_send(device, (void *)&input_header, header_size, (uint8_t *)img_buf, image_size);

            if (ret != KP_SUCCESS) {
                break;
            }

            ret = kp_customized_inference_receive(device, (void *)&output_result, result_size, &recv_size);

            if (ret != KP_SUCCESS) {
                break;
            }

            printf("\n[loop %d]\n", i + 1);
            helper_print_yolo_box_on_bmp((kp_yolo_result_t *)&output_result.yolo_result, _image_file_path);
        }

        printf("\n");

        if (ret != KP_SUCCESS) {
            printf("\ninference failed, error = %d\n", ret);
            return -1;
        }

        free(img_buf);
        kp_disconnect_devices(device);

        return 0;
    }
    ```


---

## 3. Firmware Development

**Note**: For further information of KL730 VMF_NNM, please refer **Leipzig_SDK_Multimedia_Framework_Programming_Guide.pdf** in {KL730_SDK_TOP_FOLDER_PATH}/02_APP/01_Documents/

1. Go to App Flow Folder {KL730_SDK_FOLDER_PATH}/apps/vmf_nnm/solution/app_flow

2. Add *my_KL730_sin_with_sw_npu_fmt_cvt_example_inf.h* into include folder

    - The content of this file should be synchronized with **my_KL730_sin_with_sw_npu_fmt_cvt_example.h** in PLUS.

    ```cpp
    #include "kp_struct.h"

    #define MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID 4002
    #define YOLO_BOX_MAX                                    100

    typedef struct {
        uint32_t class_count;
        uint32_t box_count;
        kp_bounding_box_t boxes[YOLO_BOX_MAX];
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_yolo_result_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        my_KL730_sin_with_sw_npu_fmt_cvt_example_yolo_result_t yolo_result;
    } __attribute__((aligned(4))) my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t;

    void my_KL730_sin_with_sw_npu_fmt_cvt_example_inf(int job_id, int num_input_buf, void **inf_input_buf_list);
    void my_KL730_sin_with_sw_npu_fmt_cvt_example_inf_deinit();
    ```

3. Add *my_KL730_sin_with_sw_npu_fmt_cvt_example_inf.c*

    - There are four steps for inferencing in one model:

        1. Prepare the memory space for the result.

        2. Prepare **VMF_NNM_INFERENCE_APP_CONFIG_T**, which is used for configure the inference process.

        3. Activate NCPU firmware via **VMF_NNM_Inference_App_Execute()**.

        4. Send the result to PLUS via **VMF_NNM_Fifoq_Manager_Result_Enqueue()**.

    - For the customized model, **model_id** of **VMF_NNM_INFERENCE_APP_CONFIG_T** should be set to the id of the customized model.

    - For the customized pre-process and post-process, please provide the function pointer to **pre_proc_func** and **post_proc_func** of **VMF_NNM_INFERENCE_APP_CONFIG_T**. Please refer [Pre/Post Process](#4-pre-process-and-post-process-development) for more information.

    - The inference result will be written to **ncpu_result_buf** of **VMF_NNM_INFERENCE_APP_CONFIG_T**. Therefore, you must provide a memory space for it (In this example, **ncpu_result_buf** is pointed to **yolo_result** in **output_result**.)

    ```cpp
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>
    #include <stdio.h>

    #include "model_type.h"
    #include "vmf_nnm_inference_app.h"
    #include "vmf_nnm_fifoq_manager.h"

    #include "my_KL730_sin_with_sw_npu_fmt_cvt_example_inf.h"
    #include "user_post_process_yolov5.h"
    #include "user_pre_process_yolov5_with_sw_npu_format_convert.h"

    static bool g_bSensorEnable                             = false;
    static bool g_isInit                                    = false;
    static ex_yolo_post_proc_config_t post_proc_params_v5s  = {
        .prob_thresh                = 0.15,
        .nms_thresh                 = 0.5,
        .max_detection              = YOLO_BOX_MAX,
        .max_detection_per_class    = YOLO_BOX_MAX,
        .nms_mode                   = EX_NMS_MODE_SINGLE_CLASS,
        .anchor_layer_num           = 3,
        .anchor_cell_num_per_layer  = 3,
        .data                       = {{{10, 13}, {16, 30}, {33, 23}},
                                       {{30, 61}, {62, 45}, {59, 119}},
                                       {{116, 90}, {156, 198}, {373, 326}},
                                       {{0, 0}, {0, 0}, {0, 0}},
                                       {{0, 0}, {0, 0}, {0, 0}}},
    };

    void my_KL730_sin_with_sw_npu_fmt_cvt_example_inf(int job_id, int num_input_buf, void **inf_input_buf_list)
    {
        // 'inf_input_buf' and 'inf_result_buf' are provided by kdp2 middleware
        // the content of 'inf_input_buf' is transmitted from host SW = header + image
        // 'inf_result_buf' is used to carry inference result back to host SW = header + inference result (from ncpu/npu)

        // now get an available free result buffer
        // normally the begin part of result buffer should contain app-defined result header
        // and the rest is for ncpu/npu inference output data
        int ret = KP_SUCCESS;

        // initializing the resources required for preprocessing for the first time
        if (false == g_isInit) {
            ret = user_pre_process_yolov5_with_sw_npu_format_convert_init();
            if (KP_SUCCESS != ret) {
                VMF_NNM_Fifoq_Manager_Status_Code_Enqueue(job_id, ret);
                return;
            }

            g_isInit = true;
        }

        // verify that the input data number meets the requirements of the model
        if (1 != num_input_buf) {
            VMF_NNM_Fifoq_Manager_Status_Code_Enqueue(job_id, KP_FW_WRONG_INPUT_BUFFER_COUNT_110);
            return;
        }

        int result_buf_size;
        uintptr_t inf_result_buf;
        uintptr_t inf_result_phy_addr;

        /******* Prepare the memory space of result *******/
        if (0 != VMF_NNM_Fifoq_Manager_Result_Get_Free_Buffer(&inf_result_buf, &inf_result_phy_addr, &result_buf_size, -1)) {
            printf("[%s] get result free buffer failed\n", __FUNCTION__);
            return;
        }

        my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t *input_header = (my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t *)inf_input_buf_list[0];
        my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t *output_result = (my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t *)inf_result_buf;

        /******* Prepare the configuration *******/

        // config image preprocessing and model settings
        VMF_NNM_INFERENCE_APP_CONFIG_T inf_config;
        memset(&inf_config, 0, sizeof(VMF_NNM_INFERENCE_APP_CONFIG_T));

        // image buffer address should be just after the header
        inf_config.num_image                    = 1;
        inf_config.image_list[0].image_buf      = (void *)((uintptr_t)input_header + sizeof(my_KL730_sin_with_sw_npu_fmt_cvt_example_header_t));
        inf_config.image_list[0].image_width    = input_header->img_width;
        inf_config.image_list[0].image_height   = input_header->img_height;
        inf_config.image_list[0].image_channel  = 3;                                        // assume RGB565
        inf_config.image_list[0].image_format   = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_list[0].image_norm     = KP_NORMALIZE_KNERON;                      // this depends on model
        inf_config.image_list[0].image_resize   = KP_RESIZE_ENABLE;                         // enable resize
        inf_config.image_list[0].image_padding  = KP_PADDING_CORNER;                        // enable padding on corner
        inf_config.model_id                     = KNERON_YOLOV5S_COCO80_640_640_3;          // this depends on model

        // setting pre/post-proc configuration
        inf_config.pre_proc_config              = NULL;
        inf_config.pre_proc_func                = user_pre_process_yolov5_with_sw_npu_format_convert;
        inf_config.post_proc_config             = (void *)&post_proc_params_v5s;            // yolo post-process configurations for yolo v5 series
        inf_config.post_proc_func               = user_post_yolov5_no_sigmoid;

        // set up result output buffer for ncpu/npu
        inf_config.ncpu_result_buf              = (void *)&(output_result->yolo_result);    // give result buffer for ncpu/npu, callback will carry it


        /******* Activate inferencing in NCPU *******/

        // run preprocessing and inference, trigger ncpu/npu to do the work
        // if enable_parallel=true (works only for single model), result callback is needed
        // however if inference error then no callback will be invoked
        ret = VMF_NNM_Inference_App_Execute(&inf_config);

        /******* Send the result to PLUS *******/

        // header_stamp is a must to correctly transfer result data back to host SW
        output_result->header_stamp.magic_type  = KDP2_MAGIC_TYPE_INFERENCE;
        output_result->header_stamp.total_size  = sizeof(my_KL730_sin_with_sw_npu_fmt_cvt_example_result_t);
        output_result->header_stamp.job_id      = job_id;
        output_result->header_stamp.status_code = ret;

        // send output result buffer back to host SW
        VMF_NNM_Fifoq_Manager_Result_Enqueue(inf_result_buf, inf_result_phy_addr, result_buf_size, -1, false);
    }

    void my_KL730_sin_with_sw_npu_fmt_cvt_example_inf_deinit()
    {
        if (true == g_isInit) {
            if (KP_SUCCESS != user_pre_process_yolov5_with_sw_npu_format_convert_deinit()) {
                printf("[%s] user_pre_process_yolov5_with_sw_npu_format_convert_deinit fail ...\n", __FUNCTION__);
            } else {
                g_isInit = false;
            }
        }
    }
    ```

    - Dig into the registered preprocessing function to demonstrate the conversion of source data to NPU format (In *{KL730_SDK_FOLDER_PATH}/apps/vmf_nnm/solution/app_flow/pre_post_proc/user_pre_process_yolov5_with_sw_npu_format_convert.c*)  

        - The major process in *user_pre_process_yolov5_with_sw_npu_format_convert.c*:
            - Initialization function `user_pre_process_yolov5_with_sw_npu_format_convert_init()`  
                1. Get the model input tensor information  
                2. Allocate the memory for the working buffer  
            - Release function `user_pre_process_yolov5_with_sw_npu_format_convert_deinit()`  
                1. Release the working buffer
            - Process function `user_pre_process_yolov5_with_sw_npu_format_convert()`  
                1. Do image preprocessing for fitting the model input shape
                2. Convert the image data to ONNX data layout (HxWxC to CxHxW)
                3. Do normalization
                4. Convert the ONNX data to NPU data by `ex_convert_onnx_data_to_npu_data()` and the input tensor information

        - **Note:** The conversion process details can be found in the source code of the ex_convert_onnx_data_to_npu_data() function and [Convert ONNX & NPU Data on the KL730 Platform](../../appendix/convert_onnx_data_to_npu_data_on_kl730.md)  

        ```cpp
        #include <stdio.h>

        #include "user_pre_process_yolov5_with_sw_npu_format_convert.h"
        #include "vmf_nnm_inference_app.h"
        #include "model_type.h"
        #include "user_utils.h"

        static VMF_NNM_MODEL_TENSOR_DESCRIPTOR_T tensor_descriptor  = {0};
        static uint32_t onnx_data_channel                           = 0;
        static uint32_t onnx_data_height                            = 0;
        static uint32_t onnx_data_width                             = 0;
        static uint32_t onnx_data_buf_size                          = 0;
        static float* onnx_data_buf                                 = NULL;

        int user_pre_process_yolov5_with_sw_npu_format_convert_init()
        {
            int ret = KP_SUCCESS;
            
            VMF_NNM_MODEL_TENSOR_INFO_V2_T *tensor_info = NULL;

            if (NULL == onnx_data_buf) {
                /* get YOLOv5 model input shape */
                ret = VMF_NNM_MODEL_Get_Input_Tensor_Descriptor(KNERON_YOLOV5S_COCO80_640_640_3, 0, &tensor_descriptor);
                if (0 == ret) {
                    ret = KP_FW_GET_MODEL_INFO_FAILED_109;
                    goto FUNC_OUT;
                } else {
                    ret = KP_SUCCESS;
                }

                if (NGS_MODEL_TENSOR_SHAPE_INFO_VERSION_2 != tensor_descriptor.tensor_shape_info.version) {
                    ret = KP_FW_ERROR_UNSUPPORT_TOOLCHAIN_VERSION_136;
                    goto FUNC_OUT;
                }

                /* get model input size (shape order: BxCxHxW) (KL730 only support kp_tensor_shape_info_v2_t) */
                tensor_info         = &(tensor_descriptor.tensor_shape_info.tensor_shape_info_data.v2);
                onnx_data_channel   = tensor_info->shape[1];
                onnx_data_height    = tensor_info->shape[2];
                onnx_data_width     = tensor_info->shape[3];

                /* malloc origin model input data */
                onnx_data_buf_size  = onnx_data_width * onnx_data_height * onnx_data_channel;
                onnx_data_buf       = calloc(onnx_data_buf_size, sizeof(float));

                if (NULL == onnx_data_buf) {
                    ret = KP_FW_DDR_MALLOC_FAILED_102;
                    goto FUNC_OUT;
                }
            }

        FUNC_OUT:
            return ret;
        }

        int user_pre_process_yolov5_with_sw_npu_format_convert_deinit()
        {
            int ret = KP_SUCCESS;

            if (NULL != onnx_data_buf) {
                free(onnx_data_buf);
                onnx_data_buf = NULL;
            } else {
                ret = KP_FW_DDR_MALLOC_FAILED_102;
                goto FUNC_OUT;
            }

        FUNC_OUT:
            return ret;
        }

        int user_pre_process_yolov5_with_sw_npu_format_convert(struct kdp_image_s *image_p, unsigned int index)
        {
            int ret                                             = KP_SUCCESS;

            /* get image source information and model input information */
            unsigned int dwSrcWidth                             = RAW_INPUT_COL(image_p, index);
            unsigned int dwSrcHeight                            = RAW_INPUT_ROW(image_p, index);
            unsigned char *pSrcBuffer                           = (unsigned char*)RAW_IMAGE_MEM_ADDR(image_p, index);
            unsigned int dwSrcBufferSize                        = RAW_IMAGE_MEM_LEN(image_p, index);
            unsigned int dwSrcNormalization                     = RAW_FORMAT(image_p, index);

            unsigned int dwDstWidth                             = DIM_INPUT_COL(image_p, index);
            unsigned int dwDstHeight                            = DIM_INPUT_ROW(image_p, index);
            unsigned char *pDstBuffer                           = (unsigned char*)PREPROC_INPUT_MEM_ADDR(image_p, index);
            unsigned int dwDstBufferSize                        = PREPROC_INPUT_MEM_LEN(image_p, index);

            /* setting pre-process related image configuration */
            float fScaleWidth                                   = (float)(dwDstWidth - 1) / (float)(dwSrcWidth - 1);
            float fScaleHeight                                  = (float)(dwDstHeight - 1) / (float)(dwSrcHeight - 1);
            float fScale                                        = 0;
            unsigned int dwResizeWidth                          = 0;
            unsigned int dwResizeHeight                         = 0;
            unsigned int dwPadLeft                              = 0;
            unsigned int dwPadRight                             = 0;
            unsigned int dwPadTop                               = 0;
            unsigned int dwPadBottom                            = 0;
            unsigned int img_buf_rgba8888_offset                = 0;
            unsigned int onnx_data_buf_offset                   = 0;

            /* to set the image engine (IE) for hardware image processing, the process involves resizing, padding, and converting the color space */
            /* Note: In this example function, we only use IE for general image processing without any exceptional Kneron pre-processing support, such as hardware normalization. */
            VMF_NNM_IE_CONFIG_T ie_config                       = {0};

            ie_config.src_buffer_addr                           = pSrcBuffer;
            ie_config.src_buffer_size                           = dwSrcBufferSize;
            ie_config.src_format                                = RAW_FORMAT(image_p, index) & IMAGE_FORMAT_NPU;
            ie_config.src_width                                 = dwSrcWidth;
            ie_config.src_height                                = dwSrcHeight;

            ie_config.dst_buffer_addr                           = pDstBuffer;
            ie_config.dst_buffer_size                           = dwDstBufferSize;
            ie_config.dst_format                                = KP_IMAGE_FORMAT_RGBA8888;
            ie_config.dst_width                                 = dwDstWidth;
            ie_config.dst_height                                = dwDstHeight;
            ie_config.dst_angle                                 = 0;

            ie_config.enable_crop                               = false;

            ie_config.image_norm                                = KP_NORMALIZE_DISABLE; /* Note: Disable hardware normalization when using software quantization and NPU layout conversion */
            ie_config.image_resize                              = KP_RESIZE_ENABLE;
            ie_config.image_padding                             = KP_PADDING_CORNER;

            ret = VMF_NNM_IE_Execute(&ie_config);
            if (KP_SUCCESS != ret) {
                printf("VMF_NNM_IE_Execute failed\n");
                goto FUNC_OUT;
            }

            /* prepare origin model input data (re-layout 640x640x3 rgba8888 image to 1x3x640x640 model input data) */
            for (unsigned int channel = 0; channel < onnx_data_channel; channel++) {
                img_buf_rgba8888_offset = channel;

                for (unsigned int pixel = 0; pixel < onnx_data_height * onnx_data_width; pixel++) {
                    onnx_data_buf[onnx_data_buf_offset + pixel] = (float)pDstBuffer[img_buf_rgba8888_offset];
                    img_buf_rgba8888_offset += 4;
                }

                onnx_data_buf_offset += (onnx_data_height * onnx_data_width);
            }

            /* do software normalization process (assume KP_NORMALIZE_KNERON normalization) */
            /* ---------------------------------------------------------------------------- */
            /* kp_normalize_mode_t and HW normalization flag mapping                        */
            /* ---------------------------------------------------------------------------- */
            /* KP_NORMALIZE_KNERON:             IMAGE_FORMAT_SUB128                         */
            /* KP_NORMALIZE_TENSOR_FLOW:        IMAGE_FORMAT_SUB128                         */
            /* KP_NORMALIZE_CUSTOMIZED_SUB128:  IMAGE_FORMAT_SUB128                         */
            /* KP_NORMALIZE_YOLO:               IMAGE_FORMAT_RIGHT_SHIFT_ONE_BIT            */
            /* KP_NORMALIZE_CUSTOMIZED_DIV2:    IMAGE_FORMAT_RIGHT_SHIFT_ONE_BIT            */
            if (!(dwSrcNormalization & IMAGE_FORMAT_SUB128)) {
                printf("Unsupport normalization configuration\n");
                ret = KP_FW_NOT_SUPPORT_PREPROCESSING_108;
                goto FUNC_OUT;
            }

            for (unsigned int idx = 0; idx < onnx_data_buf_size; idx++) {
                onnx_data_buf[idx] = onnx_data_buf[idx] / 256.0 - 0.5f;
            }

            /* convert ONNX data to NPU data */
            ret = ex_convert_onnx_data_to_npu_data(&tensor_descriptor,          /* tensor information */
                                                   onnx_data_buf,               /* tensor data in ONNX format */
                                                   onnx_data_buf_size,          /* element number of onnx_data_buf */
                                                   (int8_t **)&pDstBuffer,      /* tensor data in NPU format */
                                                   (int32_t *)&dwDstBufferSize  /* data size of npu_data_buf */);
            if (KP_SUCCESS != ret) {
                printf("ex_convert_onnx_data_to_npu_data failed\n");
                goto FUNC_OUT;
            }

            /* setting pre-process related image configuration */
            if (fScaleWidth < fScaleHeight) {
                fScale = fScaleWidth;
            } else {
                fScale = fScaleHeight;
            }

            dwResizeWidth                                       = (dwSrcWidth - 1) * fScale + 1.5f;
            dwResizeHeight                                      = (dwSrcHeight - 1) * fScale + 1.5f;
            dwPadRight                                          = dwDstWidth - dwResizeWidth;
            dwPadBottom                                         = dwDstHeight - dwResizeHeight;

            RAW_PAD_TOP(image_p, index)                         = dwPadTop;
            RAW_PAD_BOTTOM(image_p, index)                      = dwPadBottom;
            RAW_PAD_LEFT(image_p, index)                        = dwPadLeft;
            RAW_PAD_RIGHT(image_p, index)                       = dwPadRight;
            RAW_CROP_TOP(image_p, index)                        = 0;
            RAW_CROP_LEFT(image_p, index)                       = 0;
            RAW_CROP_RIGHT(image_p, index)                      = 0;
            RAW_CROP_BOTTOM(image_p, index)                     = 0;
            RAW_SCALE_WIDTH(image_p, index)                     = (float)dwSrcWidth / (float)dwResizeWidth;
            RAW_SCALE_HEIGHT(image_p, index)                    = (float)dwSrcHeight / (float)dwResizeHeight;

        FUNC_OUT:
            return ret;
        }
        ```  

4. Go to Companion Solution Folder {KL730_SDK_FOLDER_PATH}/apps/vmf_nnm/solution/solution_companion_user_ex

5. Edit *application_init.c*

    - **_app_func** is the entry interface for all inference request.

    - Inference jobs will be dispatched to the corresponding function based on the **job_id** in **kp_inference_header_stamp_t** in the header.

    - You need to establish a switch case for **MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID** and correspond the switch case to **my_KL730_sin_with_sw_npu_fmt_cvt_example_inf()**.

    ```cpp
    #include <stdio.h>
    #include <stdlib.h>
    #include <signal.h>
    #include <string.h>
    #include <sys/stat.h>
    #include <sys/time.h>
    #include <getopt.h>
    #include <unistd.h>

    #include <vmf_nnm_inference_app.h>
    #include <vmf_nnm_fifoq_manager.h>

    // inference app
    #include "kdp2_inf_app_yolo.h"
    #include "demo_customize_inf_single_model.h"
    #include "demo_customize_inf_multiple_models.h"
    #include "application_init.h"
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    #include "my_KL730_sin_with_sw_npu_fmt_cvt_example_inf.h"
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    /**
    * @brief To register AI applications
    * @param[in] num_input_buf number of data inputs in list
    * @param[in] inf_input_buf_list list of data input for inference task
    * @return N/A
    * @note Add a switch case item for a new inf_app application
    */
    static void _app_func(int num_input_buf, void** inf_input_buf_list);

    static void _app_func(int num_input_buf, void** inf_input_buf_list)
    {
        // check header stamp
        if (0 >= num_input_buf) {
            kmdw_printf("No input buffer for app function\n");
            return;
        }

        kp_inference_header_stamp_t *header_stamp = (kp_inference_header_stamp_t *)inf_input_buf_list[0];
        uint32_t job_id = header_stamp->job_id;

        switch (job_id)
        {
        case KDP2_INF_ID_APP_YOLO:
            kdp2_app_yolo_inference(job_id, num_input_buf, inf_input_buf_list);
            break;
        case KDP2_JOB_ID_APP_YOLO_CONFIG_POST_PROC:
            kdp2_app_yolo_config_post_process_parameters(job_id, num_input_buf, inf_input_buf_list);
            break;
        case DEMO_KL730_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from one model
            demo_customize_inf_single_model(job_id, num_input_buf, inf_input_buf_list);
            break;
        case DEMO_KL730_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from two models
            demo_customize_inf_multiple_models(job_id, num_input_buf, inf_input_buf_list);
            break;
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        case MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID:
            my_KL730_sin_with_sw_npu_fmt_cvt_example_inf(job_id, num_input_buf, inf_input_buf_list);
            break;
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */
        default:
            VMF_NNM_Fifoq_Manager_Status_Code_Enqueue(job_id, KP_FW_ERROR_UNKNOWN_APP);
            printf("unsupported job_id %d \n",job_id);
            break;
        }
    }

    static void _app_func_deinit(unsigned int job_id);

    void _app_func_deinit(unsigned int job_id)
    {
        switch (job_id)
        {
        case KDP2_INF_ID_APP_YOLO:
            kdp2_app_yolo_inference_deinit();
            break;
        case DEMO_KL730_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID:
            demo_customize_inf_single_model_deinit();
            break;
        case DEMO_KL730_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID:
            demo_customize_inf_multiple_model_deinit();
            break;
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        case MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID:
            my_KL730_sin_with_sw_npu_fmt_cvt_example_inf_deinit();
            break;
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */
        default:
            printf("%s, unsupported job_id %d \n", __func__, job_id);
            break;
        }
    }

    void app_initialize(void)
    {
        printf(">> Start running KL730 KDP2 companion mode ...\n");

        /* initialize inference app */
        /* register APP functions */
        /* specify depth of inference queues */
        VMF_NNM_Inference_App_Init(_app_func);
        VMF_NNM_Fifoq_Manager_Init();

        return;
    }

    void app_destroy(void)
    {
        _app_func_deinit(KDP2_INF_ID_APP_YOLO);
        _app_func_deinit(DEMO_KL730_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID);
        _app_func_deinit(DEMO_KL730_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID);
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        _app_func_deinit(MY_KL730_SIN_WITH_SW_NPU_FMT_CVT_EXAMPLE_JOB_ID);
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */

        VMF_NNM_Inference_App_Destroy();
        VMF_NNM_Fifoq_Manager_Destroy();
    }
    ```

---

## 4. Pre-process and Post-process Development


If the customized models need a customized pre-process or post-process on Kneron AI device, you can add the pre-process and post-process in the following files.

1. Go to NCPU Project Main Folder {KL730_SDK_FOLDER_PATH}/apps/vmf_nnm/solution/app_flow/pre_post_proc

2. Add your customized pre-process/post-process header file into include folder.

3. Add your customized post-process/post-process implementation c file into current folder.

4. Register the pre/post process into **pre_proc_func** and **post_proc_func** of **VMF_NNM_INFERENCE_APP_CONFIG_T** during [firmware development](#3-firmware-development).

    - If **pre_proc_func** of **VMF_NNM_INFERENCE_APP_CONFIG_T** is not set, hardware auto pre-process will be adapted during inference flow.

    - If **post_proc_func** of **VMF_NNM_INFERENCE_APP_CONFIG_T** is not set, inference raw output data will be put into result buffer without post-process.

**Note**: During developing the post-processing, you must be aware of what pre-process has done, including image resize, image padding, and image cropping.

**Note**: In post-processing, the memory layout of data in **raw_cnn_res_t** for KL520, KL730 and KL720 are different. Please reference [Kneron NPU Raw Output Channel Order](../../appendix/npu_raw_output_memory_layout.md).
