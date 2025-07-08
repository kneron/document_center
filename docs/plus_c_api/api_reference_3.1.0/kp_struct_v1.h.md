# Legacy Kneron PLUS data structure


**(To be deprecated in future release)**
 
 




**Include Header File:**  kp_struct_v1.h

- Structs
    - [kp_generic_raw_bypass_pre_proc_image_header_t](#kp_generic_raw_bypass_pre_proc_image_header_t)
    - [kp_generic_raw_bypass_pre_proc_result_header_t](#kp_generic_raw_bypass_pre_proc_result_header_t)
    - [kp_generic_raw_image_header_t](#kp_generic_raw_image_header_t)
    - [kp_generic_raw_result_header_t](#kp_generic_raw_result_header_t)


---




## **Structs**
### **kp_generic_raw_bypass_pre_proc_image_header_t**
typedef struct **kp_generic_raw_bypass_pre_proc_image_header_t** {...}
> inference descriptor for images bypass pre-processing

|Members| |
|:---|:--- |
|uint32_t inference_number;| inference sequence number |
|uint32_t model_id;| target inference model ID |
|uint32_t image_buffer_size;| image buffer size |


---
### **kp_generic_raw_bypass_pre_proc_result_header_t**
typedef struct **kp_generic_raw_bypass_pre_proc_result_header_t** {...}
> inference RAW output descriptor for bypass pre-processing

|Members| |
|:---|:--- |
|uint32_t inference_number;| inference sequence number |
|uint32_t crop_number;| crop box sequence number |
|uint32_t num_output_node;| total number of output nodes |
|uint32_t product_id;| product id, refer to kp_product_id_t |


---
### **kp_generic_raw_image_header_t**
typedef struct **kp_generic_raw_image_header_t** {...}
> inference descriptor for images

|Members| |
|:---|:--- |
|uint32_t inference_number;| inference sequence number |
|uint32_t model_id;| target inference model ID |
|uint32_t width;| image width |
|uint32_t height;| image height |
|uint32_t resize_mode;| resize mode, refer to kp_resize_mode_t |
|uint32_t padding_mode;| padding mode, refer to kp_resize_mode_t |
|uint32_t image_format;| image format, refer to kp_image_format_t |
|uint32_t normalize_mode;| inference normalization, refer to kp_normalize_mode_t |
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
|uint32_t product_id;| product id, refer to kp_product_id_t |
|kp_hw_pre_proc_info_t pre_proc_info;| hardware pre-process related value |


---
