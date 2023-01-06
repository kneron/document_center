# Create KL720 Multiple Models Example


---

## 1. Download Source Code

1. Download the latest **kneron_plus_vXXX.zip** into Windows from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

2. Unzip kneron_plus_vXXX.zip

Note: **{PLUS_FOLDER_PATH}** will be used below for representing the unzipped folder path of PLUS.

---

## 2. PLUS (Software) Development

1. Create my_kl720_mul_example folder

    ```bash
    $ cd {PLUS_FOLDER_PATH}/examples/
    $ mkdir my_kl720_mul_example
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

3. Add *my_kl720_mul_example.h*

    - Please define the customized **header** structure and customized **result** structure in this file.

    - Header (my_kl720_mul_example_header_t) is used for **sending** data to SCPU firmware. What kind of data should be contained can be customized based on the your requirement.

    - Result (my_kl720_mul_example_result_t) is used for **receiving** data from SCPU firmware. What kind of data should be contained can be customized based on the output of model inference.

    - **kp_inference_header_stamp_t** must be contained in both header and result structures.

    - The **JOB_ID** describes the unique id of the task you want to execute in firmware, and it must be unique and above 1000.

    - This file should be synchronized with the .h file in SCPU firmware.

    ```cpp
    #pragma once

    #define MY_KL720_MUL_EXAMPLE_JOB_ID 2003
    #define DME_OBJECT_MAX              80

    /**
     * @brief describe a pedestrian detect classification result of one detected person
    */
    typedef struct
    {
        float pd_class_socre;   /**< a pedestrian classification score */
        kp_bounding_box_t pd;   /**< a pedestrian box information */
    } __attribute__((aligned(4))) one_pd_classification_result_t;

    /**
    * @brief describe a pedestrian detect classification output result
    */
    typedef struct
    {
        uint32_t box_count;                                     /**< boxes of all classes */
        one_pd_classification_result_t pds[DME_OBJECT_MAX];     /**< pedestrian detect information */
    } __attribute__((aligned(4))) pd_classification_result_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;
        uint32_t width;
        uint32_t height;
    } __attribute__((aligned(4))) my_kl720_mul_example_header_t;

    // result (header + data) for 'Customize Inference Multiple Models'
    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;
        pd_classification_result_t pd_classification_result;
    } __attribute__((aligned(4))) my_kl720_mul_example_result_t;

    ```

4. Add *my_kl720_mul_example.c*

    - There are 5 steps for inferencing in Kneron AI device:

        1. Connect Kneron AI device.

        2. Upload the model to AI device.

        3. Prepare data for the header.

        4. Send the header and image buffer to SCPU firmware via **kp_customized_inference_send()**.

        5. Receive the result from SCPU firmware via **kp_customized_inference_receive()**.

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

    #include "my_kl720_mul_example.h"

    static char _model_file_path[128] = "../../res/models/KL720/yolov5_pd/models_720.nef";
    static char _image_file_path[128] = "../../res/images/travel_walk_480x256.bmp";
    static int _loop = 10;

    int main(int argc, char *argv[])
    {
        kp_devices_list_t *device_list;
        kp_device_group_t device;
        kp_model_nef_descriptor_t model_desc;

        // each device has a unique port ID, 0 for auto-search
        int port_id = (argc > 1) ? atoi(argv[1]) : 0;
        int ret;

        /******* check the device USB speed *******/
        {
            int link_speed;
            device_list = kp_scan_devices();
            helper_get_device_usb_speed_by_port_id(device_list, port_id, &link_speed);
            if (KP_USB_SPEED_SUPER != link_speed)
                printf("[warning] device is not run at super speed.\n");
        }

        /******* connect the device *******/
        {
            int error_code;

            // connect device
            device = kp_connect_devices(1, &port_id, &error_code);
            if (!device) {
                printf("error ! connect device failed, port ID = '%d', error = '%d'\n", port_id, error_code);
                exit(0);
            }

            kp_set_timeout(device, 5000);
            printf("connect device ... OK\n");
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
        my_kl720_mul_example_header_t input_header;
        my_kl720_mul_example_result_t output_result;
        pd_classification_result_t* pd_classification_result = &output_result.pd_classification_result;

        input_header.header_stamp.job_id = MY_KL720_MUL_EXAMPLE_JOB_ID;
        input_header.header_stamp.total_image = 1;
        input_header.header_stamp.image_index = 0;
        input_header.img_width = img_width;
        input_header.img_height = img_height;

        int header_size = sizeof(my_kl720_mul_example_header_t);
        int image_size = img_width * img_height * 2; // RGB565
        int result_size = sizeof(my_kl720_mul_example_result_t);
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

            for (int j = 0; j < pd_classification_result->box_count; j++) {
                printf("Box %d (x1, y1, x2, y2, class, score, pb score) = (%d, %d), (%d, %d), %d, %f, %f\n",
                    j + 1,
                    (int)pd_classification_result->pds[j].pd.x1,
                    (int)pd_classification_result->pds[j].pd.y1,
                    (int)pd_classification_result->pds[j].pd.x2,
                    (int)pd_classification_result->pds[j].pd.y2,
                    (int)pd_classification_result->pds[j].pd.class_num,
                    pd_classification_result->pds[j].pd.score,
                    pd_classification_result->pds[j].pd_class_score);
            }
        }

        printf("\n");

        free(img_buf);
        kp_release_model_nef_descriptor(&model_desc);
        kp_disconnect_devices(device);

        return 0;
    }
    ```

---

## 3. SCPU Firmware Development for pedestrian detection + pedestrian classification
1. Go to SCPU App Folder {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/app

2. Add *my_kl720_mul_example_inf.h* into include folder

    - The content of this file should be synchronized with **my_kl720_mul_example.h** in PLUS.

    ```cpp
    #pragma once

    #include "model_res.h"

    #define MY_KL720_MUL_EXAMPLE_JOB_ID 2003

    /**
     * @brief describe a pedestrian detect classification result of one detected person
    */
    typedef struct
    {
        float pd_class_socre;   /**< a pedestrian classification score */
        kp_bounding_box_t pd;   /**< a pedestrian box information */
    } __attribute__((aligned(4))) one_pd_classification_result_t;

    /**
    * @brief describe a pedestrian detect classification output result
    */
    typedef struct
    {
        uint32_t box_count;                                     /**< boxes of all classes */
        one_pd_classification_result_t pds[DME_OBJECT_MAX];     /**< pedestrian detect information */
    } __attribute__((aligned(4))) pd_classification_result_t;

    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;
        uint32_t width;
        uint32_t height;
    } __attribute__((aligned(4))) my_kl720_mul_example_header_t;

    // result (header + data) for 'Customize Inference Multiple Models'
    typedef struct
    {
        /* header stamp is necessary for data transfer between host and device */
        kp_inference_header_stamp_t header_stamp;
        pd_classification_result_t pd_classification_result;
    } __attribute__((aligned(4))) my_kl720_mul_example_result_t;

    void my_kl720_mul_example_inf(int job_id, int num_input_buf, void **inf_input_buf_list);
    ```

3. Add *my_kl720_mul_example_inf.c*

    - There are 8 steps for inferencing in pedestrian detect model and pedestrian classification model:

        1. Prepare the memory space for the result.

        2. Prepare header of output result.

        3. Prepare the temporary memory space for the result of middle model via **kmdw_ddr_reserve()**

        4. Prepare **kmdw_inference_app_config_t** for pedestrian detect model, which is used for configure the inference in NCPU firmware.

        5. Activate NCPU firmware for pedestrian detect model via **kmdw_inference_app_execute()**.

        6. Prepare **kmdw_inference_app_config_t** for pedestrian classification model.

        7. Activate NCPU firmware for pedestrian classification model via **kmdw_inference_app_execute()**.

        8. Send the result to PLUS via **kmdw_fifoq_manager_result_enqueue()**.

    - For the customized model, **model_id** of **kmdw_inference_app_config_t** should be set to the id of the customized model.

    - The inference result of NCPU will be written to **ncpu_result_buf** of **kmdw_inference_app_config_t**. Therefore, you must provide a memory space for it (In this example, **ncpu_result_buf** is pointed to **pd_result** for pedestrian detect model, and **imagenet_result** for pedestrian classification model.)

    - For the detail of **kmdw_inference_app_config_t**, please refer to section [NCPU Firmware Configuration](./ncpu_firmware_configuration.md)

    ```cpp
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "model_type.h"
    #include "kmdw_console.h"

    #include "kmdw_inference_app.h"
    #include "kmdw_fifoq_manager.h"
    #include "my_kl720_mul_example_inf.h"

    // for pedestrian detection result, should be in DDR
    static struct yolo_result_s *pd_result = NULL;
    static struct imagenet_result_s *imagenet_result = NULL;

    /**
    * @brief describe a yolo post-process configurations for yolo v5 series
    */
    typedef struct
    {
        float prob_thresh;
        float nms_thresh;
        uint32_t max_detection_per_class;
        uint16_t anchor_row;
        uint16_t anchor_col;
        uint16_t stride_size;
        uint16_t reserved_size;
        uint32_t data[40];
    } __attribute__((aligned(4))) kp_app_yolo_post_proc_config_t;

    static kp_app_yolo_post_proc_config_t post_proc_params_v5s = {
        .prob_thresh = 0.3,
        .nms_thresh = 0.65,
        .max_detection_per_class = 20,
        .anchor_row = 3,
        .anchor_col = 6,
        .stride_size = 3,
        .reserved_size = 0,
        .data = {
            // anchors[3][6]
            10, 13, 16, 30, 33, 23,
            30, 61, 62, 45, 59, 119,
            116, 90, 156, 198, 373, 326,
            // strides[3]
            8, 16, 32,
        },
    };

    static bool init_temp_buffer()
    {
        // allocate DDR memory for ncpu/npu output restult
        pd_result = (struct yolo_result_s *)kmdw_ddr_reserve(sizeof(struct yolo_result_s) + DME_OBJECT_MAX * sizeof(struct bounding_box_s));
        if (pd_result == NULL)
            return false;

        imagenet_result = (struct imagenet_result_s *)kmdw_ddr_reserve(sizeof(struct imagenet_result_s) * IMAGENET_TOP_MAX);
        if (imagenet_result == NULL)
            return false;

        return true;
    }

    static int inference_pedestrian_detection(my_kl720_mul_example_header_t *_input_header,
                                              struct yolo_result_s *_pd_result /* output */)
    {
        // config image preprocessing and model settings
        kmdw_inference_app_config_t inf_config;
        memset(&inf_config, 0, sizeof(kmdw_inference_app_config_t)); // for safety let default 'bool' to 'false'

        // image buffer address should be just after the header
        inf_config.num_image = 1;

        inf_config.image_list[0].image_buf = (void *)((uint32_t)_input_header + sizeof(my_kl720_mul_example_header_t));
        inf_config.image_list[0].image_width = _input_header->width;
        inf_config.image_list[0].image_height = _input_header->height;
        inf_config.image_list[0].image_channel = 3;                                     // assume RGB565
        inf_config.image_list[0].image_format = KP_IMAGE_FORMAT_RGB565;                 // assume RGB565
        inf_config.image_list[0].image_norm = KP_NORMALIZE_KNERON;                      // this depends on model
        inf_config.image_list[0].image_resize = KP_RESIZE_ENABLE;                       // enable resize
        inf_config.image_list[0].image_padding = KP_PADDING_CORNER;                     // enable padding on corner
        inf_config.model_id = KNERON_PERSONDETECTION_YOLOV5sParklot_480_256_3;          // this depends on model
        inf_config.user_define_data = (void *)&post_proc_params_v5s;                    // yolo post-process configurations for yolo v5 series

        // set up fd result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)_pd_result;

        return kmdw_inference_app_execute(&inf_config);
    }

    static int inference_pedestrian_imagenet_classification(my_kl720_mul_example_header_t *_input_header,
                                                            struct bounding_box_s *_box,
                                                            struct imagenet_result_s * _imagenet_result/* output */)
    {
        // config image preprocessing and model settings
        kmdw_inference_app_config_t inf_config;
        memset(&inf_config, 0, sizeof(kmdw_inference_app_config_t)); // for safety let default 'bool' to 'false'

        int32_t left = (int32_t)(_box->x1);
        int32_t top = (int32_t)(_box->y1);
        int32_t right = (int32_t)(_box->x2);
        int32_t bottom = (int32_t)(_box->y2);

        // image buffer address should be just after the header
        inf_config.num_image = 1;

        inf_config.image_list[0].image_buf = (void *)((uint32_t)_input_header + sizeof(my_kl720_mul_example_header_t));
        inf_config.image_list[0].image_width = _input_header->width;
        inf_config.image_list[0].image_height = _input_header->height;
        inf_config.image_list[0].image_channel = 3;                                 // assume RGB565
        inf_config.image_list[0].image_format = KP_IMAGE_FORMAT_RGB565;             // assume RGB565
        inf_config.image_list[0].image_norm = KP_NORMALIZE_KNERON;                  // this depends on model
        inf_config.image_list[0].image_resize = KP_RESIZE_ENABLE;                   // enable resize
        inf_config.image_list[0].image_padding = KP_PADDING_DISABLE;                // disable padding
        inf_config.image_list[0].enable_crop = true;                                // enable crop image in ncpu/npu
        inf_config.model_id = KNERON_PERSONCLASSIFIER_MB_56_32_3;                   // this depends on model

        // set crop box
        inf_config.image_list[0].crop_area.crop_number = 0;
        inf_config.image_list[0].crop_area.x1 = left;
        inf_config.image_list[0].crop_area.y1 = top;
        inf_config.image_list[0].crop_area.width = right - left;
        inf_config.image_list[0].crop_area.height = bottom - top;

        // set up fd result output buffer for ncpu/npu
        inf_config.ncpu_result_buf = (void *)_imagenet_result;

        return kmdw_inference_app_execute(&inf_config);
    }

    void my_kl720_mul_example_inf(int job_id, int num_input_buf, void **inf_input_buf_list)
    {
        if (1 != num_input_buf) {
            kmdw_inference_app_send_status_code(job_id, KP_FW_WRONG_INPUT_BUFFER_COUNT_110);
            return;
        }

        my_kl720_mul_example_header_t *input_header = (my_kl720_mul_example_header_t *)inf_input_buf_list[0];

        /******* Prepare the memory space of result *******/

        int result_buf_size;
        void *inf_result_buf = kmdw_fifoq_manager_result_get_free_buffer(&result_buf_size);
        my_kl720_mul_example_result_t *output_result = (my_kl720_mul_example_result_t *)inf_result_buf;

        /******* Prepare header of output result *******/

        output_result->header_stamp.magic_type = KDP2_MAGIC_TYPE_INFERENCE;
        output_result->header_stamp.total_size = sizeof(my_kl720_mul_example_result_t);
        output_result->header_stamp.job_id = job_id;

        /******* Prepare the temporary memory space for the result of middle model *******/

        static bool is_init = false;

        if (!is_init) {
            int status = init_temp_buffer();
            if (!status) {
                // notify host error !
                output_result->header_stamp.status_code = KP_FW_DDR_MALLOC_FAILED_102;
                kmdw_fifoq_manager_result_enqueue((void *)output_result, result_buf_size, false);
                return;
            }

            is_init = true;
        }

        /******* Run face detect model *******/
        inf_status = inference_pedestrian_detection(input_header, pd_result);
        if (inf_status != KP_SUCCESS) {
            // notify host error !
            output_result->header_stamp.status_code = inf_status;
            kmdw_fifoq_manager_result_enqueue((void *)output_result, result_buf_size, false);
            return;
        }

        int box_count = 0;
        int max_box_count = (pd_result->box_count > DME_OBJECT_MAX) ? DME_OBJECT_MAX : pd_result->box_count;
        pd_classification_result_t *pd_classification_result = &output_result->pd_classification_result;

        for (int i = 0; i < max_box_count; i++) {
            struct bounding_box_s *box = &pd_result->boxes[i];

            // do face landmark for each faces
            inf_status = inference_pedestrian_imagenet_classification(input_header, box, imagenet_result);

            if (KP_SUCCESS != inf_status) {
                // notify host error !
                output_result->header_stamp.status_code = inf_status;
                kmdw_fifoq_manager_result_enqueue((void *)output_result, result_buf_size, false);
                return;
            }

            // pedestrian_imagenet_classification result (class 0 : background, class 1: person)
            if (1 == imagenet_result[0].index)
                pd_classification_result->pds[box_count].pd_class_socre = imagenet_result[0].score;
            else
                pd_classification_result->pds[box_count].pd_class_socre = imagenet_result[1].score;

            memcpy(&pd_classification_result->pds[box_count].pd, box, sizeof(kp_bounding_box_t));

            box_count++;
        }

        pd_classification_result->box_count = box_count;

        output_result->header_stamp.status_code = KP_SUCCESS;
        output_result->header_stamp.total_size = sizeof(my_kl720_mul_example_result_t) - sizeof(pd_classification_result_t) +
                                                 sizeof(pd_classification_result->box_count) + box_count * sizeof(one_pd_classification_result_t);
        // send output result buffer back to host SW
        kmdw_fifoq_manager_result_enqueue((void *)output_result, result_buf_size, false);
    }
    ```

4. Go to SCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/build/solution_kdp2_user_ex/main_scpu

5. Edit *application_init.c*

    - **_app_func** is the entry interface for all inference request.

    - Inference jobs will be dispatched to the coresponding function based on the **job_id** in **kp_inference_header_stamp_t** in the header.

    - You need to establish a switch case for **MY_KL720_MUL_EXAMPLE_JOB_ID** and corespond the switch case to **my_kl720_mul_example_inf()**.

    ```cpp
    #include <stdio.h>
    #include "cmsis_os2.h"

    // inference core
    #include "kp_struct.h"
    #include "kmdw_console.h"
    #include "kmdw_inference_app.h"

    // inference app
    #include "kdp2_inf_app_yolo.h"
    #include "demo_customize_inf_single_model.h"
    #include "demo_customize_inf_multiple_models.h"
    /* ======================================== */
    /*              Add Line Begin              */
    /* ======================================== */
    #include "my_kl720_mul_example_inf.h"
    /* ======================================== */
    /*               Add Line End               */
    /* ======================================== */

    // inference client
    #include "kdp2_usb_companion.h"

    #define MAX_IMAGE_COUNT   10          /**< MAX inference input  queue slot count */
    #define MAX_RESULT_COUNT  10          /**< MAX inference output queue slot count */

    /**
    * @brief To register AI applications
    * @param[in] num_input_buf number of data inputs in list
    * @param[in] inf_input_buf_list list of data input for inference task
    * @return N/A
    * @note Add a switch case item for a new inf_app application
    */
    static void _app_func(int num_input_buf, void **inf_input_buf_list);

    void _app_func(int num_input_buf, void **inf_input_buf_list)
    {
        // check header stamp
        if (0 >= num_input_buf) {
            kmdw_printf("No input buffer for app function\n");
            return;
        }

        void *first_inf_input_buf = inf_input_buf_list[0];
        kp_inference_header_stamp_t *header_stamp = (kp_inference_header_stamp_t *)first_inf_input_buf;
        uint32_t job_id = header_stamp->job_id;

        switch (job_id) {
        case KDP2_INF_ID_APP_YOLO:
            kdp2_app_yolo_inference(job_id, num_input_buf, inf_input_buf_list);
            break;
        case KDP2_JOB_ID_APP_YOLO_CONFIG_POST_PROC:
            kdp2_app_yolo_config_post_process_parameters(job_id, num_input_buf, inf_input_buf_list);
            break;
        case DEMO_KL720_CUSTOMIZE_INF_SINGLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized inference from one model
            demo_customize_inf_single_model(job_id, num_input_buf, inf_input_buf_list);
            break;
        case DEMO_KL720_CUSTOMIZE_INF_MULTIPLE_MODEL_JOB_ID: // a demo code implementation in SCPU for user-defined/customized inference from multiple model
            demo_customize_inf_multiple_model(job_id, num_input_buf, inf_input_buf_list);
            break;
        /* ======================================== */
        /*              Add Line Begin              */
        /* ======================================== */
        case MY_KL720_MUL_EXAMPLE_JOB_ID:
            my_kl720_mul_example_inf(job_id, num_input_buf, inf_input_buf_list);
            break;
        /* ======================================== */
        /*               Add Line End               */
        /* ======================================== */
        default:
            kmdw_inference_app_send_status_code(job_id, KP_FW_ERROR_UNKNOWN_APP);
            break;
        }
    }

    void app_initialize(void)
    {
        info_msg(">> Start running KL720 KDP2 companion mode ...\n");

        /* initialize inference app */
        /* register APP functions */
        /* specify depth of inference queues */
        kmdw_inference_app_init(_app_func, MAX_IMAGE_COUNT, MAX_RESULT_COUNT);

        /* companion mode init */
        kdp2_usb_companion_init();

        return;
    }
    ```

---

## 4. NCPU Firmware Development for The Pre-process and Post-process

If the customized model need a customized pre-process or post-process, you can add the pre-process and post-process in the following files.

1. Go to NCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/platform/kl720/ncpu/ncpu_main/src

2. Add your customized pre-process function into **user_pre_process.c**

3. Add your customized post-process function into **user_post_process.c**

4. You may reference the **pre_post_proc_template.c** for guidance of how to access from input/output node of the model

5. Edit **model_ftr_table.c**

    - Add your customized pre-process into **model_pre_proc_fns** table with the ID of your model.

    - Add your customized post-process into **model_post_proc_fns** talbe with the ID of your model.

    - Once pre-process and post-process are registered, they will automatically execute before and after the inference of model.

    - The pre-process and post-process for certain model are specified by the model Id.

**Note**: During developing the post-processing, you must be aware of what pre-process has done, including image resize, image padding, and image cropping.

**Note**: In post-processing, the memory layout of data in **raw_cnn_res_t** for KL520 and KL720 are different. Please reference [Kneron NPU Raw Output Channel Order](../../appendix/npu_raw_output_memory_layout.md).
