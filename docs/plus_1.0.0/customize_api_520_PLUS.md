## 1. Introduction

In order to run customized models on Kneron AI dongle, there are four stages are involved:

- **Model development**
- **PLUS (software) development**
- **SCPU firmware development**
- **NCPU firmware development**

However, this document only provides illustration for **PLUS development**, **SCPU firmware development**, and **NCPU firmware development**.

The diagram below demonstrates the inference flow for every models running on Kneron AI dongle, and how the PLUS, SCPU, and NCPU interact with each other.

![](./imgs/customize_api_520_PLUS/customized_api_develop_flow.png)

## 2. Download Source Code

1. Download the latest **kneron_plus_vXXX.zip** into Windows from <https://www.kneron.com/tw/support/developers/>, it is located at **KNEO Stem (USB Dongle)/kneron_plus/**.

2. Unzip kneron_plus_vXXX.zip

   

**{PLUS_FOLDER_PATH}** will be used below for representing the unzipped folder path of PLUS.

## 3. Develop an Example using Customized API to Run YOLO Model

### 3.1 PLUS (Software) Development

1. Create my_example folder

    ```
    $ cd {PLUS_FOLDER_PATH}/examples/
    $ mkdir my_example
    ```

2. Add CMakelists.txt

    ```
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

3. Add my_example.h

    - Please define the customized **header** structure and customized **result** structure in this file.

    - Header (my_example_header_t) is used for **sending** data to SCPU firmware. What kind of data should be contained can be customized based on the your requirement.

    - Result (my_example_result_t) is used for **receiving** data from SCPU firmware. What kind of data should be contained can be customized based on the output of model inference.

    - **kp_inference_header_stamp_t** must be contained in both header and result structures.

    - The **JOB_ID** describes the unique id of the task you want to execute in firmware, and it must be unique and above 1000.

    - This file should be synchronized with the .h file in SCPU firmware.
    ```
    #pragma once

    #define MY_EXAMPLE_JOB_ID               1002
    #define YOLO_BOX_MAX                    100

    typedef struct {
        uint32_t class_count;
        uint32_t box_count;
        kp_bounding_box_t boxes[YOLO_BOX_MAX];
    } __attribute__((aligned(4))) my_example_yolo_result_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_example_header_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        my_example_yolo_result_t yolo_result;
    } __attribute__((aligned(4))) my_example_result_t;
    ```

4. Add *my_example.c*

    - There are 6 steps for inferencing in Kneron AI dongle:

        1. Connect Kneron AI dongle.

        2. Upload the firmware to AI dongle.

        3. Upload the model to AI dongle.

        4. Prepare data for the header.

        5. Send the header and image buffer to SCPU firmware via **kp_customized_inference_send()**.

        6. Receive the result from SCPU firmware via **kp_customized_inference_receive()**.

    - In this example, the **image** is transcoded into RGB565, and the width and height of the image is carried by the header.

    - Sending header and receiving result can be executed sequentially or on two different threads.
    ```
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>

    #include "kp_core.h"
    #include "kp_inference.h"
    #include "helper_functions.h"

    #include "my_example.h"

    static char _scpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_scpu.bin";
    static char _ncpu_fw_path[128] = "../../res/firmware/KL520/kdp2_fw_ncpu.bin";
    static char _model_file_path[128] = "../../res/models/KL520/tiny_yolo_v3/models_520.nef";
    static char _image_file_path[128] = "../../res/images/bike_cars_street_224x224.bmp";
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
            ret = kp_load_firmware_from_file(device, _scpu_fw_path, _ncpu_fw_path);
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
        my_example_header_t input_header;
        my_example_result_t output_result;

        input_header.header_stamp.job_id = MY_EXAMPLE_JOB_ID;
        input_header.img_width = img_width;
        input_header.img_height = img_height;

        int header_size = sizeof(my_example_header_t);
        int image_size = img_width * img_height * 2; // RGB565
        int result_size = sizeof(my_example_result_t);
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

### 3.2 SCPU Firmware Development

1. Go to SCPU App Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app

2. Add my_example_inf.h

    - The content of this file should be synchronized with **my_example.h** in PLUS.
    ```
    #pragma once

    #define MY_EXAMPLE_JOB_ID               1002
    #define YOLO_BOX_MAX                    100

    typedef struct {
        uint32_t class_count;
        uint32_t box_count;
        kp_bounding_box_t boxes[YOLO_BOX_MAX];
    } __attribute__((aligned(4))) my_example_yolo_result_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        uint32_t img_width;
        uint32_t img_height;
    } __attribute__((aligned(4))) my_example_header_t;

    typedef struct {
        /* header stamp is necessary */
        kp_inference_header_stamp_t header_stamp;

        my_example_yolo_result_t yolo_result;
    } __attribute__((aligned(4))) my_example_result_t;
    ```

3. Add my_example_inf.c

    - There are four steps for inferencing in one model:

        1. Prepare the memory space for the result.

        2. Prepare **kdp2_inference_config_t**, which is used for configure the inference in NCPU firmware.

        3. Activate NCPU firmware via **kdp2_inference_start()**.

        4. Send the result to PLUS via **kdp2_inference_send_result()**.

    - For the customized model, **model_id** of **kdp2_inference_config_t** should be set to the id of the customized model.

    - The inference result of NCPU will be written to **ncpu_result_buf** of **kdp2_inference_config_t**. Therefore, you must provide a memory space for it (In this example, **ncpu_result_buf** is pointed to **yolo_result** in **output_result**.)

    ```
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    #include "model_type.h"
    #include "kmdw_console.h"

    #include "kmdw_inference.h"
    #include "my_example_inf.h"

    void my_example_inf(void *inf_input_buf)
    {
        my_example_header_t *input_header = (my_example_header_t *)inf_input_buf;

        /******* Prepare the memory space of result *******/

        void *inf_result_buf = kmdw_inference_request_result_buffer(NULL);
        my_example_result_t *output_result = (my_example_result_t *)inf_result_buf;

        /******* Prepare the configuration *******/
    
        kmdw_inference_config_t inf_config;
    
        // Set the initial value of config to 0, false and NULL
        memset(&inf_config, 0, sizeof(kmdw_inference_config_t));
    
        // image buffer address should be just after the header
        inf_config.image_buf = (void *)((uint32_t)input_header + sizeof(my_example_header_t));
        inf_config.image_width = input_header->img_width;
        inf_config.image_height = input_header->img_height;
        inf_config.image_channel = 3;                                       // assume RGB565
        inf_config.image_format = KP_IMAGE_FORMAT_RGB565;                   // assume RGB565
        inf_config.image_norm = KP_NORMALIZE_KNERON;                        // this depends on model
        inf_config.model_id = TINY_YOLO_V3_224_224_3;                       // this depends on model
        inf_config.enable_preprocess = true;                                // enable preprocess in ncpu/npu
        inf_config.inf_result_buf = inf_result_buf;                         // for callback
        inf_config.ncpu_result_buf = (void *)&(output_result->yolo_result); // give result buffer for ncpu/npu, callback will carry it

        /******* Activate inferencing in NCPU *******/
    
        int inf_status = kmdw_inference_start(&inf_config);

        /******* Send the result to PLUS *******/
    
        // header_stamp is a must to correctly transfer result data back to host SW
        output_result->header_stamp.magic_type = KDP2_MAGIC_TYPE_INFERENCE;
        output_result->header_stamp.total_size = sizeof(my_example_result_t);
        output_result->header_stamp.job_id = MY_EXAMPLE_JOB_ID;
        output_result->header_stamp.status_code = inf_status;
    
        // send output result buffer back to host SW
        kmdw_inference_send_result((void *)output_result);
    }
    ```

4. Go to SCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/project/scpu_companion_user_ex/main

4. Edit *main.c*

    - **_app_entry_func** is the entry interface for all inference request.

    - Inference jobs will be dispatched to the coresponding function based on the **job_id** in **kp_inference_header_stamp_t** in the header.

    - You need to establish a switch case for **MY_EXAMPLE_JOB_ID** and corespond the switch case to **my_example_inf()**.

    ```
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
    #include "my_example_inf.h"
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
    extern void my_example_inf(void *inf_input_buf);
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
        case MY_EXAMPLE_JOB_ID:
            my_example_inf(inf_input_buf);
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

### 3.3 NCPU Firmware Development

If the customized model need a customized pre-process or post-process, you can add the pre-process and post-process in the following files.

1. Go to NCPU Project Main Folder {PLUS_FOLDER_PATH}/firmware_development/KL520/ncpu_kdp2/project/ncpu_companion_user_ex/main/

2. Add your customized pre-process function into **user_pre_process.c**

3. Add your customized post-process function into **user_post_process.c**

3. Edit **main.c**

    - Register your customized pre-process by **kdpio_pre_processing_register()**.
- Register your customized post-process by **kdpio_post_processing_register()**.
    - Once pre-process and post-process are registered, they will automatically execute before and after the inference of model.
- The pre-process and post-process for certain model are specified by the model Id.



## 4. Build and Execute My Example

### Notice: The building example below are operated in **Windows 10**.

### 4.1 Build Firmware

1. Download and install Keil MDK version 5 (at least MDK-Essential) from <https://www2.keil.com/mdk5>

2. Execute Keil uVision5

3. Select **Project** > **Open Project...**

4. Choose {PLUS_FOLDER_PATH}/firmware_development/KL520/example_projects/kdp2_companion_user_ex/workspace.uvmpw

5. Expand **Project: kdp2_scpu** in left panel

6. Right click on **app** and choose **Add Existing Files to Group 'kdp2_inference'...**

7. Select {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app/my_example_inf.c

8. Select **Project** > **Batch Build**

*If build succeeded, **kdp2_fw_scpu.bin** and **kdp2_fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL520/

![](./imgs/customize_api_520_PLUS/keil_build_firmware.png)

### 4.2 Build PLUS and Execute My Example

1. Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

2. Execute **MSYS2 MinGW 64-bit** to install dependency.
    ```
    $ pacman -Syu
    $ pacman -Sy
    $ pacman -S base-devel gcc vim cmake
    $ pacman -S mingw-w64-x86_64-libusb
    ```

3. Build and Execute my_example of PLUS in **MSYS2 MinGW 64-bit**
    ```
    $ cd {PLUS_FOLDER_PATH}
    $ mkdir build
    $ cd build
    $ cmake .. -G "MSYS Makefiles"
    $ make -j
    $ cd bin
    $ ./my_example.exe
    ```
