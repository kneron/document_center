# Create Multiple Models Example


## 1. Download Source Code

1. Download the latest **kneron_plus_vXXX.zip** into Windows from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

2. Unzip kneron_plus_vXXX.zip

Note: **{PLUS_FOLDER_PATH}** will be used below for representing the unzipped folder path of PLUS.


## 2. PLUS (Software) Development

1. Create my_mul_example folder

    ```bash
    $ cd {PLUS_FOLDER_PATH}/examples/
    $ mkdir my_mul_example
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
        ../common/helper_functions.c
        )

    add_executable(${app_name}
        ${local_src}
        ${common_src})

    target_link_libraries(${app_name} ${KPLUS_LIB_NAME} ${USB_LIB} ${MATH_LIB} pthread)
    ```

3. Add *my_mul_example.h*

    - Please define the customized **header** structure and customized **result** structure in this file.

    - Header (my_mul_example_header_t) is used for **sending** data to SCPU firmware. What kind of data should be contained can be customized based on the your requirement.

    - Result (my_mul_example_result_t) is used for **receiving** data from SCPU firmware. What kind of data should be contained can be customized based on the output of model inference.

    - **kp_inference_header_stamp_t** must be contained in both header and result structures.

    - The **JOB_ID** describes the unique id of the task you want to execute in firmware, and it must be unique and above 1000.

    - This file should be synchronized with the .h file in SCPU firmware.

    ```cpp
    #pragma once

    #define MY_MUL_EXAMPLE_JOB_ID       1003
    #define FD_MAX                      10

    typedef struct
    {
        kp_bounding_box_t fd;                 /**< fd result */
        kp_landmark_result_t lm;              /**< lm result */
    } __attribute__((aligned(4))) one_face_data_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_mul_example_header_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t face_count;
        one_face_data_t faces[FD_MAX];
    } __attribute__((aligned(4))) my_mul_example_result_t;
    ```

4. Add *my_mul_example.c*

    - There are 6 steps for inferencing in Kneron AI dongle:

        1. Connect Kneron AI dongle.

        2. Upload the firmware to AI dongle.

        3. Upload the model to AI dongle.

        4. Prepare data for the header.

        5. Send the header and image buffer to SCPU firmware via **kp_customized_inference_send()**.

        6. Receive the result from SCPU firmware via **kp_customized_inference_receive()**.

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

    #include "my_mul_example.h"

    static char _scpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_scpu.bin";
    static char _ncpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_ncpu.bin";
    static char _model_file_path[128] = "../../res/models/KL520/ssd_fd_lm/models_520.nef";
    static char _image_file_path[128] = "../../res/images/a_woman_640x480.bmp";
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
                printf("error ! connect device failed, port ID = '%d', error = '%d'\n", port_id, error_code);
                exit(0);
            }

            kp_set_timeout(device, 5000);
            printf("connect device ... OK\n");
        }

        /******* upload firmware to device *******/
        {
            ret = kp_load_firmware_from_file(device, _scpu_fw_path, _ncpu_fw_path);
            if (KP_SUCCESS != ret) {
                printf("error ! upload firmware failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload firmware ... OK\n");
        }

        /******* upload model to device *******/
        {
            ret = kp_load_model_from_file(device, _model_file_path, &model_desc);
            if (KP_SUCCESS != ret) {
                printf("error ! upload model failed, error = %d\n", ret);
                exit(0);
            }

            printf("upload model ... OK\n");
        }

        /******* prepare the image buffer read from file *******/
        // here convert a bmp file to RGB565 format buffer

        int img_width, img_height;
        char *img_buf = helper_bmp_file_to_raw_buffer(_image_file_path, &img_width, &img_height, KP_IMAGE_FORMAT_RGB565);

        if (!img_buf) {
            printf("error ! read image file failed\n");
            exit(0);
        }

        printf("read image ... OK\n");
        printf("\nstarting inference loop %d times:\n", _loop);

        /******* prepare input and output header/buffers *******/
        my_mul_example_header_t input_header;
        my_mul_example_result_t output_result;

        input_header.header_stamp.job_id = MY_NUL_EXAMPLE_JOB_ID;
        input_header.img_width = img_width;
        input_header.img_height = img_height;

        int header_size = sizeof(my_mul_example_header_t);
        int image_size = img_width * img_height * 2; // RGB565
        int result_size = sizeof(my_mul_example_result_t);
        int recv_size = 0;

        /******* starting inference work *******/

        for (int i = 0; i < _loop; i++) {
            ret = kp_customized_inference_send(device, (void *)&input_header, header_size, (uint8_t *)img_buf, image_size);

            if (KP_SUCCESS != ret) {
                printf("\ninference failed, error = %d\n", ret);
                break;
            }

            ret = kp_customized_inference_receive(device, (void *)&output_result, result_size, &recv_size);

            if (KP_SUCCESS != ret) {
                printf("\ninference failed, error = %d\n", ret);
                break;
            }

            printf("\n[loop %d]\n", i + 1);

            for (int j = 0; j < output_result.face_count; j++) {
                printf("\nFace %d (x1, y1, x2, y2, score) = %d, %d, %d, %d, %f\n", j + 1
                                                                                , (int)output_result.faces[j].fd.x1
                                                                                , (int)output_result.faces[j].fd.y1
                                                                                , (int)output_result.faces[j].fd.x2
                                                                                , (int)output_result.faces[j].fd.y2
                                                                                , output_result.faces[j].fd.score);

                for (int k = 0; k < LAND_MARK_POINTS; k++) {
                    printf("    - Landmark %d: (x, y) = %d, %d\n", k + 1
                                                                , output_result.faces[j].lm.marks[k].x
                                                                , output_result.faces[j].lm.marks[k].y);
                }
            }
        }

        printf("\n");

        free(img_buf);
        kp_disconnect_devices(device);

        return 0;
    }
    ```


## 3. SCPU Firmware Development for Face Detect + Landmark

1. Go to SCPU App Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app

2. Add *my_mul_example_inf.h*

    - The content of this file should be synchronized with **my_mul_example.h** in PLUS.

    ```cpp
    #pragma once

    #define MY_MUL_EXAMPLE_JOB_ID       1003
    #define FD_MAX                      10

    typedef struct
    {
        kp_bounding_box_t fd;                 /**< fd result */
        kp_landmark_result_t lm;              /**< lm result */
    } __attribute__((aligned(4))) one_face_data_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_mul_example_header_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;

        uint32_t face_count;
        one_face_data_t faces[FD_MAX];
    } __attribute__((aligned(4))) my_mul_example_result_t;
    ```

3. Add *my_mul_example_inf.c*

    - There are 8 steps for inferencing in face detect model and landmark model:

        1. Prepare the memory space for the result.

        2. Prepare header of output result.

        3. Prepare the temporary memory space for the result of middle model via **kmdw_ddr_reserve()**

        4. Prepare **kdp2_inference_config_t** for face detect model, which is used for configure the inference in NCPU firmware.

        5. Activate NCPU firmware for face detect model via **kdp2_inference_start()**.

        6. Prepare **kdp2_inference_config_t** for landmark model.

        7. Activate NCPU firmware for landmark model via **kdp2_inference_start()**.

        8. Send the result to PLUS via **kdp2_inference_send_result()**.

    - For the customized model, **model_id** of **kdp2_inference_config_t** should be set to the id of the customized model.

    - The inference result of NCPU will be written to **ncpu_result_buf** of **kdp2_inference_config_t**. Therefore, you must provide a memory space for it (In this example, **ncpu_result_buf** is pointed to **fd_result** for face detect model, and **lm_result** for landmark model.)

    - For the detail of **kdp2_inference_config_t**, please refer to section **6.4 Firmware Configuration**

    ```cpp
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "model_type.h"
    #include "model_res.h"
    #include "kmdw_console.h"

    #include "kmdw_inference.h"
    #include "my_mul_example_inf.h"

    #define TY_MAX_BOX_NUM (50)
    #define FACE_SCORE_THRESHOLD 0.8f

    // for face detection result, should be in DDR
    static struct yolo_result_s *fd_result = NULL;

    static int inference_face_detection(my_mul_example_header_t *input_header,
                                        struct yolo_result_s *fd_result /* output */)
    {
        /******* Prepare the configuration *******/

        kmdw_inference_config_t inf_config;

        // Set the initial value of config to 0, false and NULL
        memset(&inf_config, 0, sizeof(kmdw_inference_config_t));

        // image buffer address should be just after the header
        inf_config.image_buf = (void *)((uint32_t)input_header + sizeof(my_mul_example_header_t));
        inf_config.image_width = input_header->img_width;
        inf_config.image_height = input_header->img_height;
        inf_config.image_channel = 3;                                       // assume RGB565
        inf_config.image_format = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_norm = KP_NORMALIZE_KNERON;                        // this depends on model
        inf_config.model_id = KNERON_FD_MASK_MBSSD_200_200_3;               // this depends on model
        inf_config.enable_preprocess = true;                                // enable preprocess in ncpu/npu

        // set up fd result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)fd_result;

        /******* Activate inferencing in NCPU *******/

        return kmdw_inference_start(&inf_config);
    }

    static int inference_face_landmarks(my_mul_example_header_t *input_header,
                                        struct bounding_box_s *face_box,
                                        kp_landmark_result_t *lm_result /* output */)
    {
        /******* Prepare the configuration *******/

        kmdw_inference_config_t inf_config;

        // Set the initial value of config to 0, false and NULL
        memset(&inf_config, 0, sizeof(kmdw_inference_config_t));

        int32_t left = (int32_t)(face_box->x1);
        int32_t top = (int32_t)(face_box->y1);
        int32_t right = (int32_t)(face_box->x2);
        int32_t bottom = (int32_t)(face_box->y2);

        // image buffer address should be just after the header
        inf_config.image_buf = (void *)((uint32_t)input_header + sizeof(my_mul_example_header_t));
        inf_config.image_width = input_header->img_width;
        inf_config.image_height = input_header->img_height;
        inf_config.image_channel = 3;                                       // assume RGB565
        inf_config.image_format = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_norm = KP_NORMALIZE_KNERON;                        // this depends on model
        inf_config.model_id = KNERON_LM_5PTS_ONET_56_56_3;                  // this depends on model
        inf_config.enable_crop = true;                                      // enable crop image in ncpu/npu
        inf_config.enable_preprocess = true;                                // enable preprocess in ncpu/npu

        // set crop box
        inf_config.crop_area.crop_number = 0;
        inf_config.crop_area.x1 = left;
        inf_config.crop_area.y1 = top;
        inf_config.crop_area.width = right - left;
        inf_config.crop_area.height = bottom - top;

        // set up landmark result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)lm_result;

        /******* Activate inferencing in NCPU *******/

        return kmdw_inference_start(&inf_config);
    }

    static bool init_temp_buffer()
    {
        // allocate DDR memory for ncpu/npu output restult
        fd_result = (struct yolo_result_s *)kmdw_ddr_reserve(sizeof(struct yolo_result_s) + TY_MAX_BOX_NUM * sizeof(struct bounding_box_s));

        if (fd_result == NULL) {
            return false;
        }

        return true;
    }

    void my_mul_example_inf(void *inf_input_buf)
    {
        my_mul_example_header_t *input_header = (my_mul_example_header_t *)inf_input_buf;

        /******* Prepare the memory space of result *******/

        int result_buf_size = sizeof(my_mul_example_result_t);
        void *inf_result_buf = kmdw_inference_request_result_buffer(&result_buf_size);
        my_mul_example_result_t *output_result = (my_mul_example_result_t *)inf_result_buf;

        /******* Prepare header of output result *******/

        output_result->header_stamp.magic_type = KDP2_MAGIC_TYPE_INFERENCE;
        output_result->header_stamp.total_size = sizeof(my_mul_example_result_t);
        output_result->header_stamp.job_id = MY_MUL_EXAMPLE_JOB_ID;

        /******* Prepare the temporary memory space for the result of middle model *******/

        static bool is_init = false;

        if (!is_init) {
            int status = init_temp_buffer();
            if (!status) {
                // notify host error !
                output_result->header_stamp.status_code = KP_FW_DDR_MALLOC_FAILED_102;
                kmdw_inference_send_result((void *)output_result);
                return;
            }

            is_init = true;
        }

        /******* Run face detect model *******/

        int inf_status = inference_face_detection(input_header, fd_result);

        if (inf_status != KP_SUCCESS) {
            // notify host error !
            output_result->header_stamp.status_code = inf_status;
            kmdw_inference_send_result((void *)output_result);
            return;
        }

        int face_cnt = 0;
        int max_face = (fd_result->box_count > FD_MAX) ? FD_MAX : fd_result->box_count;

        /******* Run landmark model for every faces *******/

        for (int i = 0; i < max_face; i++) {
            struct bounding_box_s *face_box = &fd_result->boxes[i];
            kp_landmark_result_t *face_lm_result = &output_result->faces[face_cnt].lm;

            if (FACE_SCORE_THRESHOLD < face_box->score) {
                // do face landmark for each faces
                inf_status = inference_face_landmarks(input_header, face_box, face_lm_result);

                if (KP_SUCCESS != inf_status) {
                    // notify host error !
                    output_result->header_stamp.status_code = inf_status;
                    kmdw_inference_send_result((void *)output_result);
                    return;
                }

                // skip it if face lm is not good
                if (0.99f > face_lm_result->score) {
                    continue;
                }

                memcpy(&output_result->faces[face_cnt].fd, face_box, sizeof(kp_bounding_box_t));
                face_cnt++;
            }
        }

        /******* Send the result to PLUS *******/

        output_result->face_count = face_cnt;
        output_result->header_stamp.status_code = KP_SUCCESS;

        kmdw_inference_send_result((void *)output_result);
    }
    ```

4. Go to SCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/project/scpu_companion_user_ex/main

4. Edit *main.c*

    - **_app_entry_func** is the entry interface for all inference request.

    - Inference jobs will be dispatched to the coresponding function based on the **job_id** in **kp_inference_header_stamp_t** in the header.

    - You need to establish a switch case for **MY_MUL_EXAMPLE_JOB_ID** and corespond the switch case to **my_mul_example_inf()**.

    ```cpp
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "kp_struct.h"
    #include "kmdw_inference.h"

    #include "kdp2_inf_app_yolo.h"
    #include "demo_customize_inf_single_model.h"
    #include "demo_customize_inf_multiple_models.h"
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    #include "my_mul_example_inf.h"
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    extern void SystemCoreClockUpdate(void);

    /* Kneron usb companion interface implementation to work with PLUS host SW */
    extern void kdp2_usb_companion_init(void);
    extern void main_init_usboot(void);

    /* declare inference code implementation here */
    extern void kdp2_app_yolo_inference(void *inf_input_buf);            // kdp2_inf_app_yolo.c
    extern void demo_customize_inf_single_model(void *inf_input_buf);    // demo_customize_inf_single_model.c
    extern void demo_customize_inf_multiple_models(void *inf_input_buf); // demo_customize_inf_multiple_models.c
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    extern void my_mul_example_inf(void *inf_input_buf);
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    static void _app_entry_func(void *inf_input_buf)
    {
        // check header stamp
        kp_inference_header_stamp_t *header_stamp = (kp_inference_header_stamp_t *)inf_input_buf;

        switch (header_stamp->job_id)
        {
        case KDP2_INF_ID_APP_YOLO:
            kdp2_app_yolo_inference(inf_input_buf);
            break;
        case DEMO_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from one model
            demo_customize_inf_single_model(inf_input_buf);
            break;
        case DEMO_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized infernece from two models
            demo_customize_inf_multiple_models(inf_input_buf);
            break;
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        case MY_MUL_EXAMPLE_JOB_ID:
            my_mul_example_inf(inf_input_buf);
            break;
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */
        default:
            kmdw_inference_send_error_code(0, KP_FW_ERROR_UNKNOWN_APP);
            break;
        }
    }

    /**
    * @brief main, main function
    */
    int main(void)
    {
        SystemCoreClockUpdate(); // System Initialization
        osKernelInitialize();    // Initialize CMSIS-RTOS

        /* SDK main init for companion mode */
        main_init_usboot();

        /* initialize inference core threads and memory with user-specified app entry function */
        kmdw_inference_init(_app_entry_func);

        /* start an interface implementation as input/ouput to co-work with inference framework */
        // this can be changed by other interface implementation
        kdp2_usb_companion_init();

        /* Start RTOS Kernel */
        if (osKernelGetState() == osKernelReady)
        {
            osKernelStart();
        }

        while (1)
        {
        }
    }
    ```

## 4. NCPU Firmware Development for The Pre-process and Post-process


If the customized models need a customized pre-process or post-process on Kneron AI dongle, you can add the pre-process and post-process in the following files.

1. Go to NCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/ncpu_kdp2/project/ncpu_companion_user_ex/main/

2. Add your customized pre-process function into **user_pre_process.c**

3. Add your customized post-process function into **user_post_process.c**

4. Edit **main.c**

    - Register your customized pre-process by **kdpio_pre_processing_register()**.

    - Register your customized post-process by **kdpio_post_processing_register()**.

    - Once pre-process and post-process are registered, they will automatically execute before and after the inference of model.

    - The pre-process and post-process for certain model are specified by the model Id.
