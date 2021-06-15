# Kneron PLUS data structure




**Include Header File:**  kp_struct.h

- Defines
    - APP_PADDING_BYTES
    - KDP2_MAGIC_TYPE_COMMAND
    - KDP2_MAGIC_TYPE_INFERENCE
    - MAX_CROP_BOX
    - YOLO_GOOD_BOX_MAX
    - LAND_MARK_POINTS
- Simple Typedef
    - [typedef void *kp_device_group_t;](#typedef-void-kp_device_group_t)
- Enumerations
    - [ KP_API_RETURN_CODE](#kp_api_return_code)
    - [ kp_channel_ordering_t](#kp_channel_ordering_t)
    - [ kp_image_format_t](#kp_image_format_t)
    - [ kp_normalize_mode_t](#kp_normalize_mode_t)
    - [ kp_preprocess_mode_t](#kp_preprocess_mode_t)
    - [ kp_product_id_t](#kp_product_id_t)
    - [ kp_reset_mode_t](#kp_reset_mode_t)
    - [ kp_usb_speed_t](#kp_usb_speed_t)
- Structs
    - [kp_bounding_box_t](#kp_bounding_box_t)
    - [kp_device_descriptor_t](#kp_device_descriptor_t)
    - [kp_devices_list_t](#kp_devices_list_t)
    - [kp_firmware_version_t](#kp_firmware_version_t)
    - [kp_generic_raw_image_header_t](#kp_generic_raw_image_header_t)
    - [kp_generic_raw_result_header_t](#kp_generic_raw_result_header_t)
    - [kp_inf_crop_box_t](#kp_inf_crop_box_t)
    - [kp_inf_fixed_node_metadata_t](#kp_inf_fixed_node_metadata_t)
    - [kp_inf_fixed_node_output_t](#kp_inf_fixed_node_output_t)
    - [kp_inf_float_node_output_t](#kp_inf_float_node_output_t)
    - [kp_inference_header_stamp_t](#kp_inference_header_stamp_t)
    - [kp_landmark_result_t](#kp_landmark_result_t)
    - [kp_model_nef_descriptor_t](#kp_model_nef_descriptor_t)
    - [kp_point_t](#kp_point_t)
    - [kp_single_model_descriptor_t](#kp_single_model_descriptor_t)
    - [kp_system_info_t](#kp_system_info_t)
    - [kp_yolo_result_t](#kp_yolo_result_t)


---




## **Defines**
| Define | Value | Description |
|:---|:---|:---|
|APP_PADDING_BYTES|20                    | Default padding size |
|KDP2_MAGIC_TYPE_COMMAND|0xAB67CD13      | Magic number for data check |
|KDP2_MAGIC_TYPE_INFERENCE|0x11FF22AA    | Magic number for data check |
|MAX_CROP_BOX|4 | MAX crop count |
|YOLO_GOOD_BOX_MAX|100 | maximum number of bounding boxes for Yolo models |
|LAND_MARK_POINTS|5 | the number of land marks points |


---




## **Simple Typedefs**
### **typedef void *kp_device_group_t;**
> a pointer handle represent connected Kneron device.


---




## **Enumerations**
### **KP_API_RETURN_CODE**
enum **KP_API_RETURN_CODE** {...}
> return code of most APIs.

| Enumerator | |
|:---|:--- |
|KP_SUCCESS = 0,| |
|KP_ERROR_USB_IO_N1 = -1,| |
|KP_ERROR_USB_INVALID_PARAM_N2 = -2,| |
|KP_ERROR_USB_ACCESS_N3 = -3,| |
|KP_ERROR_USB_NO_DEVICE_N4 = -4,| |
|KP_ERROR_USB_NOT_FOUND_N5 = -5,| |
|KP_ERROR_USB_BUSY_N6 = -6,| |
|KP_ERROR_USB_TIMEOUT_N7 = -7,| |
|KP_ERROR_USB_OVERFLOW_N8 = -8,| |
|KP_ERROR_USB_PIPE_N9 = -9,| |
|KP_ERROR_USB_INTERRUPTED_N10 = -10,| |
|KP_ERROR_USB_NO_MEM_N11 = -11,| |
|KP_ERROR_USB_NOT_SUPPORTED_N12 = -12,| |
|KP_ERROR_USB_OTHER_N99 = -99,| |
|KP_ERROR_DEVICE_NOT_EXIST_10 = 10,| |
|KP_ERROR_DEVICE_INCORRECT_RESPONSE_11 = 11,| |
|KP_ERROR_INVALID_PARAM_12 = 12,| |
|KP_ERROR_SEND_DESC_FAIL_13 = 13,| |
|KP_ERROR_SEND_DATA_FAIL_14 = 14,| |
|KP_ERROR_SEND_DATA_TOO_LARGE_15 = 15,| |
|KP_ERROR_RECV_DESC_FAIL_16 = 16,| |
|KP_ERROR_RECV_DATA_FAIL_17 = 17,| |
|KP_ERROR_RECV_DATA_TOO_LARGE_18 = 18,| |
|KP_ERROR_FW_UPDATE_FAILED_19 = 19,| |
|KP_ERROR_FILE_OPEN_FAILED_20 = 20,| |
|KP_ERROR_INVALID_MODEL_21 = 21,| |
|KP_ERROR_IMAGE_RESOLUTION_TOO_SMALL_22 = 22,| |
|KP_ERROR_IMAGE_INVALID_WIDTH_23 = 23,| |
|KP_ERROR_INVALID_FIRMWARE_24 = 24,| |
|KP_ERROR_RESET_FAILED_25 = 25,| |
|KP_ERROR_DEVICES_NUMBER_26 = 26,| |
|KP_ERROR_CONFIGURE_DEVICE_27 = 27,| |
|KP_ERROR_CONNECT_FAILED_28 = 28,| |
|KP_ERROR_DEVICE_GROUP_MIX_PRODUCT_29 = 29,| |
|KP_ERROR_RECEIVE_INCORRECT_HEADER_STAMP_30 = 30,| |
|KP_ERROR_RECEIVE_SIZE_MISMATCH_31 = 31,| |
|KP_ERROR_RECEIVE_JOB_ID_MISMATCH_32 = 32,| |
|KP_ERROR_INVALID_CUSTOMIZED_JOB_ID_33 = 33,| |
|KP_ERROR_FW_LOAD_FAILED_34 = 34,| |
|KP_ERROR_OTHER_99 = 99,| |
|KP_FW_ERROR_UNKNOWN_APP = 100,| |
|KP_FW_INFERENCE_ERROR_101 = 101,| |
|KP_FW_DDR_MALLOC_FAILED_102 = 102,| |


---
### **kp_channel_ordering_t**
typedef enum **kp_channel_ordering_t** {...}
> enum for generic raw data channel ordering

| Enumerator | |
|:---|:--- |
|KP_CHANNEL_ORDERING_HCW = 0,            | KL520 default, height/channel/width in order |
|KP_CHANNEL_ORDERING_CHW = 1,            | KL720 default, channel/height/width in order |


---
### **kp_image_format_t**
typedef enum **kp_image_format_t** {...}
> image format supported for inference.

| Enumerator | |
|:---|:--- |
|KP_IMAGE_FORMAT_UNKNOWN = 0x0,| |
|KP_IMAGE_FORMAT_RGB565 = 0x1,           | RGB565 16bits |
|KP_IMAGE_FORMAT_RGBA8888 = 0x2,         | RGBA8888 32bits |
|KP_IMAGE_FORMAT_YUYV = 0x3,             | YUYV 16bits |
|KP_IMAGE_FORMAT_RAW8 = 0x4,             | RAW 8bits |


---
### **kp_normalize_mode_t**
typedef enum **kp_normalize_mode_t** {...}
> normalization mode

| Enumerator | |
|:---|:--- |
|KP_NORMALIZE_KNERON = 0x1,              | RGB/256 - 0.5, refer to the toolchain manual |
|KP_NORMALIZE_TENSOR_FLOW,               | RGB/127.5 - 1.0, refer to the toolchain manual |
|KP_NORMALIZE_YOLO,                      | RGB/255.0, refer to the toolchain manual |
|KP_NORMALIZE_CUSTOMIZED,                | customized, refer to the toolchain manual |


---
### **kp_preprocess_mode_t**
typedef enum **kp_preprocess_mode_t** {...}
> preprocess mode

| Enumerator | |
|:---|:--- |
|KP_PREPROCESS_AUTO = 0x1, | device will do auto preprocess including image resolution scaling, color space conversion and normalization |
|KP_PREPROCESS_NONE = 0x0, | none of any pre-process will be done, user should make sure everything fits and cropping is not allowed |


---
### **kp_product_id_t**
typedef enum **kp_product_id_t** {...}
> enum for USB PID(Product ID)

| Enumerator | |
|:---|:--- |
|KP_DEVICE_KL520 = 0x100,                | KL520 USB PID |
|KP_DEVICE_KL720 = 0x720,                | KL720 USB PID |


---
### **kp_reset_mode_t**
typedef enum **kp_reset_mode_t** {...}
> reset mode

| Enumerator | |
|:---|:--- |
|KP_RESET_REBOOT = 0,    | Higheset level to reset Kneron device. Kneron device would disconnect after this reset. |
|KP_RESET_INFERENCE = 1, | Soft reset: reset inference FIFO queue. |
|KP_RESET_SHUTDOWN = 2,  | Shut down Kneron device, only useful if HW circuit supports (ex. 96 board), dongle is not supported. |


---
### **kp_usb_speed_t**
typedef enum **kp_usb_speed_t** {...}
> enum for USB speed mode

| Enumerator | |
|:---|:--- |
|KP_USB_SPEED_UNKNOWN = 0,| |
|KP_USB_SPEED_LOW = 1,| |
|KP_USB_SPEED_FULL = 2,| |
|KP_USB_SPEED_HIGH = 3,| |
|KP_USB_SPEED_SUPER = 4,| |


---




## **Structs**
### **kp_bounding_box_t**
typedef struct **kp_bounding_box_t** {...}
> describe a bounding box

|Members| |
|:---|:--- |
|float x1;| top-left corner: x |
|float y1;| top-left corner: y |
|float x2;| bottom-right corner: x |
|float y2;| bottom-right corner: y |
|float score;| probability score |
|int32_t class_num;| class # (of many) with highest probability |


---
### **kp_device_descriptor_t**
typedef struct **kp_device_descriptor_t** {...}
> information of device (USB)

|Members| |
|:---|:--- |
|uint32_t port_id;| an unique ID representing for a Kneron device, can be used as input while connecting devices |
|uint16_t vendor_id;| supposed to be 0x3231. |
|uint16_t product_id;| enum kp_product_id_t. |
|int link_speed;| enum kp_usb_speed_t. |
|uint32_t kn_number;| KN number. |
|bool isConnectable;| indicate if this device is connectable. |
|char port_path[20];| "busNo-hub_portNo-device_portNo"<br />ex: "1-2-3", means bus 1 - (hub) port 2 - (device) port 3 |
|char firmware[16];| Firmware description. |


---
### **kp_devices_list_t**
typedef struct **kp_devices_list_t** {...}
> information of connected devices from USB perspectives.

|Members| |
|:---|:--- |
|int num_dev;| connected devices |
|kp_device_descriptor_t device[];| real index range from 0 ~ (num_dev-1) |


---
### **kp_firmware_version_t**
typedef struct **kp_firmware_version_t** {...}
> describe version string

|Members| |
|:---|:--- |
|uint8_t reserved;| for backward compatibility |
|uint8_t major;| major number |
|uint8_t minor;| minor number |
|uint8_t update;| update number |
|uint32_t build;| build number |


---
### **kp_generic_raw_image_header_t**
typedef struct **kp_generic_raw_image_header_t** {...}
> inference descriptor for images

|Members| |
|:---|:--- |
|uint32_t inference_number;| inference sequence number |
|uint32_t width;| image width |
|uint32_t height;| image height |
|uint32_t preprocess_mode;| preprocess mode, none or auto refer to kp_preprocess_mode_t |
|uint32_t image_format;| image format, refer to kp_image_format_t |
|uint32_t normalize_mode;| inference normalization, refer to kp_normalize_mode_t |
|uint32_t model_id;| target inference model ID |
|uint32_t crop_count;| crop count |
|kp_inf_crop_box_t inf_crop[MAX_CROP_BOX];| box information to crop |


---
### **kp_generic_raw_result_header_t**
typedef struct **kp_generic_raw_result_header_t** {...}
> inference RAW output descriptor

|Members| |
|:---|:--- |
|uint32_t inference_number;| inference sequence number |
|uint32_t crop_number;| crop box sequence number |
|uint32_t num_output_node;| total number of output nodes |


---
### **kp_inf_crop_box_t**
typedef struct **kp_inf_crop_box_t** {...}
> data structure for a crop

|Members| |
|:---|:--- |
|uint32_t crop_number;| index number |
|uint32_t x1;| top-left corner: x |
|uint32_t y1;| top-left corner: y |
|uint32_t width;| width |
|uint32_t height;| height |


---
### **kp_inf_fixed_node_metadata_t**
typedef struct **kp_inf_fixed_node_metadata_t** {...}
> Metadata of RAW node output in fixed-point format

|Members| |
|:---|:--- |
|uint32_t height;| node height |
|uint32_t channel;| node channel |
|uint32_t width;| node width, should be aligned to 16 byte for futher processing due to low level output |
|uint32_t radix;| radix for fixed/floating point conversion |
|float scale;| scale for fixed/floating point conversion |


---
### **kp_inf_fixed_node_output_t**
typedef struct **kp_inf_fixed_node_output_t** {...}
> RAW node output in fixed-point format

|Members| |
|:---|:--- |
|kp_inf_fixed_node_metadata_t metadata;| metadata of RAW node output in fixed-point format |
|uint32_t num_data;| total number of fixed-poiont values, should be<br />metadata->width (aligned to 16 byte) * metadata->height * metadata->channel |
|int8_t *data;| array of fixed-point values|


---
### **kp_inf_float_node_output_t**
typedef struct **kp_inf_float_node_output_t** {...}
> RAW node output in floating-point format

|Members| |
|:---|:--- |
|uint32_t width;| node width |
|uint32_t height;| node height |
|uint32_t channel;| node channel |
|uint32_t num_data;| total number of floating-point values |
|float data[];| array of floating-point values |


---
### **kp_inference_header_stamp_t**
typedef struct **kp_inference_header_stamp_t** {...}
> header stamp for user-defined data transfer

|Members| |
|:---|:--- |
|uint32_t magic_type;| must be 'KDP2_MAGIC_TYPE_INFERENCE' |
|uint32_t total_size;| total size of user-defined header data struct and data (image) |
|uint32_t job_id;| user-defind ID to synchronize with firmware side, must >= 1000 |
|uint32_t status_code;| this field is valid only for result data, refer to KP_API_RETURN_CODE |


---
### **kp_landmark_result_t**
typedef struct **kp_landmark_result_t** {...}
> describe a landmark

|Members| |
|:---|:--- |
|kp_point_t marks[LAND_MARK_POINTS];| landmark points |
|float score;| score of this landmark |
|float blur;| blur score of this landmark |
|int32_t class_num;| class number |


---
### **kp_model_nef_descriptor_t**
typedef struct **kp_model_nef_descriptor_t** {...}
> a basic descriptor for a NEF

|Members| |
|:---|:--- |
|uint32_t crc;| crc of all models |
|int num_models;| number of models |
|kp_single_model_descriptor_t models[10];| model descriptors |


---
### **kp_point_t**
typedef struct **kp_point_t** {...}
> decribe a point

|Members| |
|:---|:--- |
|uint32_t x;| x value |
|uint32_t y;| y value |


---
### **kp_single_model_descriptor_t**
typedef struct **kp_single_model_descriptor_t** {...}
> a basic descriptor for a model

|Members| |
|:---|:--- |
|uint32_t id;| model ID |
|uint32_t max_raw_out_size;| needed raw output buffer size for this model |
|uint32_t width;| the input width of this model |
|uint32_t height;| the input height of this model |
|uint32_t channel;| the input channel of this model |
|kp_image_format_t img_format;| the input image format of this model  |


---
### **kp_system_info_t**
typedef struct **kp_system_info_t** {...}
> describe system information

|Members| |
|:---|:--- |
|uint32_t kn_number;| Chip K/N number |
|kp_firmware_version_t firmware_version;| FW version |


---
### **kp_yolo_result_t**
typedef struct **kp_yolo_result_t** {...}
> describe a yolo output result after post-processing

|Members| |
|:---|:--- |
|uint32_t class_count;| total class count |
|uint32_t box_count;| boxes of all classes |
|kp_bounding_box_t boxes[YOLO_GOOD_BOX_MAX];| box information |


---
