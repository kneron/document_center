# Kneron NPU Host API


Host API is the API to setup communication channels between host (such as PC, Embedded Chips)
and Kneron NPU Chip. Users can use Host API to write programs that utilize low power and high
performance Kneron NPU Chip to accelarate their deep learning model application.
There are three types of APIs:
 
- System API: These APIs are used to monitor system, update firmware and models in flash.
- DME Mode API: These APIs are for setting up dynamic loaded model, and inference.
- ISI Mode API: These APIs are for setting up image streaming interface, and inference.
- Application specific API: These APIs are specific to certain application
 




**Include Header File:**  kdp_host.h

- Enumerations
    - [ kdp_product_id_e ](#kdp_product_id_e)
    - [ kdp_usb_speed_e ](#kdp_usb_speed_e)
- Structs
    - [ kdp_db_config_s ](#kdp_db_config_s)
    - [ kdp_device_info_list_s ](#kdp_device_info_list_s)
    - [ kdp_device_info_s ](#kdp_device_info_s)
    - [ kdp_dme_cfg_s ](#kdp_dme_cfg_s)
    - [ kdp_isi_cfg_s ](#kdp_isi_cfg_s)
    - [ kdp_metadata_s ](#kdp_metadata_s)
    - [ kdp_nef_info_s ](#kdp_nef_info_s)
- Unions
    - [kapp_db_config_parameter_u ](#kapp_db_config_parameter_u)
- Functions
    - [kdp_add_dev](#kdp_add_dev)
    - [kdp_connect_usb_device](#kdp_connect_usb_device)
    - [kdp_dme_configure](#kdp_dme_configure)
    - [kdp_dme_get_status](#kdp_dme_get_status)
    - [kdp_dme_inference](#kdp_dme_inference)
    - [kdp_dme_retrieve_res](#kdp_dme_retrieve_res)
    - [kdp_end_dme](#kdp_end_dme)
    - [kdp_export_db](#kdp_export_db)
    - [kdp_extract_feature_generic](#kdp_extract_feature_generic)
    - [kdp_fm_compare](#kdp_fm_compare)
    - [kdp_get_crc](#kdp_get_crc)
    - [kdp_get_db_config](#kdp_get_db_config)
    - [kdp_get_db_index](#kdp_get_db_index)
    - [kdp_get_db_meta_data_version](#kdp_get_db_meta_data_version)
    - [kdp_get_db_version](#kdp_get_db_version)
    - [kdp_get_kn_number](#kdp_get_kn_number)
    - [kdp_get_model_info](#kdp_get_model_info)
    - [kdp_get_nef_model_metadata](#kdp_get_nef_model_metadata)
    - [kdp_get_res_mask](#kdp_get_res_mask)
    - [kdp_get_res_size](#kdp_get_res_size)
    - [kdp_import_db](#kdp_import_db)
    - [kdp_init_log](#kdp_init_log)
    - [kdp_isi_config](#kdp_isi_config)
    - [kdp_isi_inference](#kdp_isi_inference)
    - [kdp_isi_retrieve_res](#kdp_isi_retrieve_res)
    - [kdp_end_isi](#kdp_end_isi)
    - [kdp_jpeg_dec](#kdp_jpeg_dec)
    - [kdp_jpeg_dec_config](#kdp_jpeg_dec_config)
    - [kdp_jpeg_dec_retrieve_res](#kdp_jpeg_dec_retrieve_res)
    - [kdp_jpeg_enc](#kdp_jpeg_enc)
    - [kdp_jpeg_enc_config](#kdp_jpeg_enc_config)
    - [kdp_jpeg_enc_retrieve_res](#kdp_jpeg_enc_retrieve_res)
    - [kdp_lib_de_init](#kdp_lib_de_init)
    - [kdp_lib_init](#kdp_lib_init)
    - [kdp_lib_start](#kdp_lib_start)
    - [kdp_list_users](#kdp_list_users)
    - [kdp_query_fm_by_user](#kdp_query_fm_by_user)
    - [kdp_register_user](#kdp_register_user)
    - [kdp_register_user_by_fm](#kdp_register_user_by_fm)
    - [kdp_remove_user](#kdp_remove_user)
    - [kdp_report_sys_status](#kdp_report_sys_status)
    - [kdp_reset_sys](#kdp_reset_sys)
    - [kdp_scan_usb_devices](#kdp_scan_usb_devices)
    - [kdp_set_ckey](#kdp_set_ckey)
    - [kdp_set_db_config](#kdp_set_db_config)
    - [kdp_set_db_version](#kdp_set_db_version)
    - [kdp_set_sbt_key](#kdp_set_sbt_key)
    - [kdp_start_dme](#kdp_start_dme)
    - [kdp_start_dme_ext](#kdp_start_dme_ext)
    - [kdp_start_isi_mode](#kdp_start_isi_mode)
    - [kdp_start_isi_mode_ext](#kdp_start_isi_mode_ext)
    - [kdp_start_reg_user_mode](#kdp_start_reg_user_mode)
    - [kdp_start_sfid_mode](#kdp_start_sfid_mode)
    - [kdp_switch_db_index](#kdp_switch_db_index)
    - [kdp_update_fw](#kdp_update_fw)
    - [kdp_update_model](#kdp_update_model)
    - [kdp_update_nef_model](#kdp_update_nef_model)
    - [kdp_update_spl](#kdp_update_spl)
    - [kdp_verify_user_id_generic](#kdp_verify_user_id_generic)




## Enumerations
### **kdp_product_id_e**
enum **kdp_product_id_e** {...}
> enum for USD PID(Product ID)

| Enumerator | |
|:---|:--- |
|KDP_DEVICE_KL520 = 0x100,  | USB PID alias for KL520 |
|KDP_DEVICE_KL720 = 0x200,  | USB PID alias for KL720 |


---
### **kdp_usb_speed_e**
enum **kdp_usb_speed_e** {...}
> enum for USB speed mode

| Enumerator | |
|:---|:--- |
|KDP_USB_SPEED_UNKNOWN = 0,  | unknown USB speed |
|KDP_USB_SPEED_LOW = 1,      | USB low speed |
|KDP_USB_SPEED_FULL = 2,     | USB full speed |
|KDP_USB_SPEED_HIGH = 3,     | USB high speed |
|KDP_USB_SPEED_SUPER = 4,    | USB super speed |


---




## Structs
### kdp_db_config_s
struct **kdp_db_config_s** {...}
> DB configuration structure

|Members| |
|:---|:--- |
|uint16_t db_num;| number of database |
|uint16_t max_uid;| max number of user ID in each db |
|uint16_t max_fid;| max number of feature map |


---
### kdp_device_info_list_s
struct **kdp_device_info_list_s** {...}
> Information structure of connected devices

|Members| |
|:---|:--- |
|int num_dev;| connnected devices |
|kdp_device_info_t kdevice[1];| real index range from 0 ~ (num_dev-1) |


---
### kdp_device_info_s
struct **kdp_device_info_s** {...}
> Device information structure

|Members| |
|:---|:--- |
|int scan_index;| scanned order index, can be used by kdp_connect_usb_device() |
|bool isConnectable;| indicate if this device is connectable |
|unsigned short vendor_id;| supposed to be 0x3231 |
|unsigned short product_id;| for kdp_product_id_e |
|int link_speed;| for kdp_usb_speed_e |
|unsigned int serial_number;| KN number |
|char device_path[20];| "busNo-hub_portNo-device_portNo"<br />ex: "1-2-3", means bus 1 - (hub) port 2 - (device) port 3 |


---
### kdp_dme_cfg_s
struct **kdp_dme_cfg_s** {...}
> DME image configuration structure

|Members| |
|:---|:--- |
|int32_t model_id;| Model indentification ID |
|int32_t output_num;| Output number |
|int32_t image_col;| Column size.<br />NIR8: must be multiple of 4;<br />RGB565/YCBCR422: must be multiple of 2. |
|int32_t image_row;| Row size |
|int32_t image_ch;| Channel size |
|uint32_t image_format;| Image format |
|struct kdp_pad_value_s pad_values;| for future use |
|float ext_param[MAX_PARAMS_LEN];| extra parameters, such as threshold |


---
### kdp_isi_cfg_s
struct **kdp_isi_cfg_s** {...}
> ISI image configuration structure

|Members| |
|:---|:--- |
|uint32_t app_id;| Application id |
|uint32_t res_buf_size;| Aesult buffer size |
|uint16_t image_col;| Column size.<br />NIR8: must be multiple of 4;<br />RGB565/YCBCR422: must be multiple of 2. |
|uint16_t image_row;| row size |
|uint32_t image_format;| image format |
|struct kdp_pad_value_s pad_values;| for future use |
|float ext_param[MAX_PARAMS_LEN];| extra parameters, such as threshold |


---
### kdp_metadata_s
struct **kdp_metadata_s** {...}
> Metadata for nef model data: metadata / fw_info / all_models

|Members| |
|:---|:--- |
|char platform[32];| usb dongle, 96 board, etc. |
|uint32_t target;| 0: KL520, 1: KL720, etc. |
|uint32_t crc;| CRC value for all_models data |
|uint32_t kn_num;| KN number |
|uint32_t enc_type;| encrypt type |
|char tc_ver[32];| toolchain version |
|char compiler_ver[32];| compiler version |


---
### kdp_nef_info_s
struct **kdp_nef_info_s** {...}
> NEF info for nef model data: metadata / fw_info / all_models

|Members| |
|:---|:--- |
|char* fw_info_addr;| Address of fw_info part |
|uint32_t fw_info_size;| Size of fw_info part |
|char* all_models_addr;| Address of all_model part |
|uint32_t all_models_size;| Size of all_model part |


---




## Uinons
### kapp_db_config_parameter_u
union **kapp_db_config_parameter_u** {...}
> DB config parameter union #total [8 Bytes] (32-bits auto align)

|Members| |
|:---|:--- |
|kdp_db_config_t db_config;| kdp_db_config_t            [6 Bytes] |
|uint32_t uint32_value;| config uint32_t parameter  [4 Bytes] |


---




## Functions
### kdp_add_dev
> To add com device to the host lib

```c
int kdp_add_dev(
	int type
	const char* name
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      device type, only KDP_USB_DEV is supported now
<em>name</em>            [in]      the UART device name
</pre>
**Returns:**

'dev idx' on succeed, -1 on failure


---
### kdp_connect_usb_device
> To connect to a Kneron device via the 'scan_index'

```c
int kdp_connect_usb_device(
	int scan_index
)
```
**Parameters:**

<pre>
<em>scan_index</em>      [in]      the dev_idx to connect.
                          value starts from 1, can be retrieved through kdp_scan_devices()
</pre>
**Returns:**

'dev_idx' if connection is established,
'< 0' means connection is not established,


---
### kdp_dme_configure
> To request for configuring dme

```c
int kdp_dme_configure(
	int dev_idx
	char* data
	int dat_size
	uint32_t* ret_model_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>data</em>            [in]      inference setup data
<em>dat_size</em>        [in]      the size of setup data
<em>ret_model_id</em>    [out]     the return value of model id for this configuration
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_dme_get_status
> To request for getting DME inference status

```c
int kdp_dme_get_status(
	int dev_idx
	uint16_t *ssid
	uint16_t *status
	uint32_t* inf_size
	char* inf_res
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>ssid</em>            [out]     ssid to get inference status
<em>status</em>          [out]     inference status, 0 for not ready, 1 for ready
<em>inf_size</em>        [out]     inference data size
<em>inf_res</em>         [out]     inference result data
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_dme_inference
> To do inference with provided model

```c
int kdp_dme_inference(
	int dev_idx
	char* img_buf
	int buf_len
	uint32_t* inf_size
	bool* res_flag
	char* inf_res
	uint16_t mode
	uint16_t model_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_buf</em>         [in]      the image buffer
<em>buf_len</em>         [in]      the buffer size
<em>inf_size</em>        [in]      the size of inference result in DME 'serial mode'
                          the session id of the image in DME 'async mode'
<em>res_flag</em>        [out]     indicate whether result is requested and available
<em>inf_res</em>         [out]     contains the returned inference result
<em>mode</em>            [in]      running mode: 0:'serial' or 1: 'async mode'
<em>model_id</em>        [in]      the model id for this configuration
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Must call kdp_start_dme() and kdp_dme_configure() to configure the dme model.


---
### kdp_dme_retrieve_res
> To request for retrieving DME result

```c
int kdp_dme_retrieve_res(
	int dev_idx
	uint32_t addr
	int len
	char* inf_res
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>addr</em>            [in]      the ddr address to retrieve
<em>len</em>             [in]      the size of data to retrieve
<em>inf_res</em>         [out]     contains the retrieving result
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_end_dme
> request for ending dme mode

```c
int kdp_end_dme(
	int dev_idx
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_export_db
> To export from DB image from device

```c
int kdp_export_db(
	int dev_idx
	char **p_buf
	uint32_t *p_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>p_buf</em>           [out]     an output pointer for the allocated memory with the exported DB
<em>p_len</em>           [out]     DB size
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Must be called after kdp_start_sfid_mode() is called


---
### kdp_extract_feature_generic
> To extract face feature from image with specified output mask

```c
int kdp_extract_feature_generic(
	int dev_idx
	char* img_buf
	int buf_len
	uint16_t* mask
	char* res
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_buf</em>         [in]      the image buffere
<em>buf_len</em>         [in]      the image buffer size
<em>mask</em>            [in,out]  input:indicate the mask of requested data, output:updated mask
<em>res</em>             [out]     preallocated memory for the specified output
                          call kdp_get_res_size() to get result size
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> bit 0 - FD result: uint16_t for each x/y/w/h
  bit 1 - LM data: uint16_t for each value
  bit 2 - FM feature map: float for each value


---
### kdp_fm_compare
> Calculate similarity of two feature points

```c
float kdp_fm_compare(
	float *user_fm_a
	float *user_fm_b
	size_t fm_size
)
```
**Parameters:**

<pre>
<em>user_fm_a</em>       [in]      buffer A of user feature map data
<em>user_fm_b</em>       [in]      buffer B of user feature map data
<em>fm_size</em>         [in]      size of user feature map data
</pre>
**Returns:**

similarity score: smaller score meas more similar
errcode -1:parameter error


**Notes:**

> must ensure buffer A and B are the same size


---
### kdp_get_crc
> To request for CRC info of models in DDR or Flash

```c
int kdp_get_crc(
	int dev_idx
	int from_ddr
	char *data_buf
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID. A host can connect several devices
<em>from_ddr</em>        [in]      query models in ddr (1) or flash (0)
<em>data_buf</em>        [out]     the pointer to store crc
</pre>
**Returns:**

0 on succeed, -1 on failure


---
### kdp_get_db_config
> Get DB structure configuration

```c
int kdp_get_db_config(
	int dev_idx
	kdp_db_config_t* db_config
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_config</em>       [out]     return configuration data
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_get_db_index
> Get current DB index

```c
int kdp_get_db_index(
	int dev_idx
	uint32_t *db_idx
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_idx</em>          [out]     return current DB index
</pre>
**Returns:**

current DB index


---
### kdp_get_db_meta_data_version
> get DB meta data version number for DB schema confirmation

```c
int kdp_get_db_meta_data_version(
	int dev_idx
	uint32_t *db_meta_data_version
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_meta_data_version</em>[out]     return DB meta data version number
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_get_db_version
> Get DB version number

```c
int kdp_get_db_version(
	int dev_idx
	uint32_t *db_version
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_version</em>      [out]     return DB version number
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_get_kn_number
> To request for device KN number

```c
int kdp_get_kn_number(
	int dev_idx
	uint32_t *kn_num
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID.
<em>kn_num</em>          [in]      the pointer to store KN number
</pre>
**Returns:**

0 on succeed, -1 on failure


---
### kdp_get_model_info
> To request model IDs information for models in DDR or Flash

```c
int kdp_get_model_info(
	int dev_idx
	int from_ddr
	char *data_buf
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID.
<em>from_ddr</em>        [in]      query models in ddr (1) or flash (0)
<em>data_buf</em>        [out]     the pointer to store model info
                          data: total_number(4 bytes) + model_id_1(4 bytes) + model_id_2(4 bytes)
</pre>
**Returns:**

0 on succeed, -1 on failure


**Notes:**

> caller must allocate memory for data_buf.


---
### kdp_get_nef_model_metadata
> To request for metadata of NEF model file

```c
int kdp_get_nef_model_metadata(
	char* model_data
	uint32_t model_size
	struct kdp_metadata_s* metadata
)
```
**Parameters:**

<pre>
<em>model_data</em>      [in]      nef model data
<em>model_size</em>      [in]      size of NEF model
<em>metadata</em>        [out]     returned metadata
</pre>
**Returns:**

0 on succeed, -1 on failure


---
### kdp_get_res_mask
> Get result mask with bit flags

```c
uint16_t kdp_get_res_mask(
	bool fd
	bool lm
	bool fr
	bool liveness
	bool score
)
```
**Parameters:**

<pre>
<em>fd</em>              [in]      checked if need face detection output
<em>lm</em>              [in]      checked if need face detection output
<em>fr</em>              [in]      checked if need feature map of a face
<em>liveness</em>        [in]      checked if need liveness detection output (Beta)
<em>score</em>           [in]      checked if need the recognition score output
</pre>
**Returns:**

mask of bit flags


---
### kdp_get_res_size
> Get result size for memory allocation

```c
uint32_t kdp_get_res_size(
	bool fd
	bool lm
	bool fr
	bool liveness
	bool score
)
```
**Parameters:**

<pre>
<em>fd</em>              [in]      checked if need face detection output
<em>lm</em>              [in]      checked if need face detection output
<em>fr</em>              [in]      checked if need feature map of a face
<em>liveness</em>        [in]      checked if need liveness detection output (Beta)
<em>score</em>           [in]      checked if need the recognition score output
</pre>
**Returns:**

result size in bytes


---
### kdp_import_db
> To import customer DB image to device

```c
int kdp_import_db(
	int dev_idx
	char* p_buf
	uint32_t p_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>buf</em>             [in]      the customer's image buffer pointer
<em>p_len</em>           [in]      image size in buffer
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Must be called after kdp_start_sfid_mode() is called


---
### kdp_init_log
> Init the host lib internal log

```c
int kdp_init_log(
	const char* dir
	const char* name
)
```
**Parameters:**

<pre>
<em>dir</em>             [in]      the directory name of the log file
<em>name</em>            [in]      the log file name
</pre>
**Returns:**

0 on succeed, -1 on failure


---
### kdp_isi_config
> To configure the model for the supported app id

```c
int kdp_isi_config(
	int dev_idx
	uint32_t model_id
	uint32_t param
	uint32_t *rsp_code
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>model_id</em>        [in]      model id to run image inference
<em>param</em>           [in]      the parameter needed for the model
<em>rsp_code</em>        [out]     response code from ISI command handler on device
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_isi_inference
> Start an inference with an image

```c
int kdp_isi_inference(
	int dev_idx
	char* img_buf
	int buf_len
	uint32_t img_id
	uint32_t* rsp_code
	uint32_t* img_buf_available
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_buf</em>         [in]      the image buffer
<em>buf_len</em>         [in]      the buffer size
<em>img_id</em>          [in]      the sequence id of the image
<em>rsp_code</em>        [out]     response code from device
<em>img_buf_available</em>[out]     the number of image buffer still available for input
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Before calling this API, must call kdp_start_isi() first


---
### kdp_isi_retrieve_res
> To request for getting an inference results

```c
int kdp_isi_retrieve_res(
	int dev_idx
	uint32_t img_id
	uint32_t* rsp_code
	uint32_t* r_size
	char* r_data
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_id</em>          [in]      sequence id to get inference results of an image with the specified id
<em>rsp_code</em>        [out]     response code from device
<em>r_size</em>          [out]     inference data size
<em>r_res</em>           [out]     inference result data
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_end_isi
> request for ending isi mode

```c
int kdp_end_isi(
	int dev_idx
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_jpeg_dec
> start jpeg decoding

```c
int kdp_jpeg_dec(
	int dev_idx
	int img_seq
	uint8_t *in_img_buf
	uint32_t in_img_len
	uint32_t *out_img_buf
	uint32_t *out_img_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>in_img_buf</em>      [in]      input JPEG image buffer
<em>in_img_len</em>      [in]      input image size in bytes
<em>out_img_buf</em>     [out]     returned encoding ouput YUV buffer address in SCPU (not host address)
<em>out_img_len</em>     [out]     returned encoding output valid length,
                          host can use this size to allocate memory to retrieve jpeg data from SCPU
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> For KL720 only


---
### kdp_jpeg_dec_config
> Configure for jpeg decoding

```c
int kdp_jpeg_dec_config(
	int dev_idx
	int img_seq
	int width
	int height
	int fmt
	int len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>width</em>           [in]      width of the decoded output image
<em>height</em>          [in]      height of the decoded ouput image
<em>fmt</em>             [in]      decoded output YUV image format
<em>len</em>             [in]      input jpeg valid length in bytes
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> for KL720 only


---
### kdp_jpeg_dec_retrieve_res
> To retrieve jpeg decoding output

```c
int kdp_jpeg_dec_retrieve_res(
	int dev_idx
	uint32_t img_seq
	uint32_t* rsp_code
	uint32_t* r_size
	char* r_data
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>rsp_code</em>        [out]     return code
<em>r_size</em>          [out]     returned result size (bytes)
<em>r_data</em>          [out]     returned data buffer (host address)
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> For KL720 only


---
### kdp_jpeg_enc
> Start jpeg encoding

```c
int kdp_jpeg_enc(
	int dev_idx
	int img_seq
	uint8_t *in_img_buf
	uint32_t in_img_len
	uint32_t *out_img_buf
	uint32_t *out_img_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>in_img_buf</em>      [in]      input YUV image buffer
<em>in_img_len</em>      [in]      input image size in bytes
<em>out_img_buf</em>     [out]     returned encoding ouput jpeg buffer address in SCPU (not host address)
<em>out_img_len</em>     [out]     returned encoding output valid length, host can use this size to allocate memory to retrieve jpeg data from SCPU
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> for KL720 only


---
### kdp_jpeg_enc_config
> To configure for jpeg enc

```c
int kdp_jpeg_enc_config(
	int dev_idx
	int img_seq
	int width
	int height
	int fmt
	int quality
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>width</em>           [in]      width of the image
<em>height</em>          [in]      height of the image
<em>fmt</em>             [in]      input YUV image format
<em>quality</em>         [in]      jpeg encoding quality 0 ~ 100, normally 70~75 is recommended
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> for KL720 only


---
### kdp_jpeg_enc_retrieve_res
> Retrieve jpeg encoding output

```c
int kdp_jpeg_enc_retrieve_res(
	int dev_idx
	uint32_t img_seq
	uint32_t* rsp_code
	uint32_t* r_size
	char* r_data
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_seq</em>         [in]      image sequential number
<em>rsp_code</em>        [out]     return code
<em>r_size</em>          [out]     returned result size (bytes)
<em>r_data</em>          [out]     returned data buffer (host address)
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> for KL720 only


---
### kdp_lib_de_init
> Free the resources used by host lib

```c
int kdp_lib_de_init()
```
**Returns:**

0 on succeed, -1 on failure


---
### kdp_lib_init
> To init the host library

```c
int kdp_lib_init()
```
**Returns:**

0 on succeed, -1 on failure


---
### kdp_lib_start
> To start the host library to wait for messages

```c
int kdp_lib_start()
```
**Returns:**

0 on succeed, -1 on failure


---
### kdp_list_users
> To test if user in device DB

```c
int kdp_list_users(
	int dev_idx
	int user_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>user_id</em>         [in]      the user to be listed.(starts from 1)
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Must be called after kdp_start_sfid_mode() is called


---
### kdp_query_fm_by_user
> To query user's feature map from device DB

```c
int kdp_query_fm_by_user(
	int dev_idex
	char* fm
	uint32_t user_id
	uint32_t face_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>fm</em>              [out]     the buffer to store queried fm data
<em>user_id</em>         [in]      the user id to be queried. start from 1
<em>face_id</em>         [in]      the fm id to be queried. start from 1
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_register_user
> To register the extracted face features to DB in device Flash

```c
int kdp_register_user(
	int dev_idx
	uint32_t user_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>user_id</em>         [in]      the user id that be registered.
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> 
> - The mentioned feature map can be extractd by kdp_extract_feature_generic()
> - user_id must be same as the used in kdp_start_reg_user_mode()


---
### kdp_register_user_by_fm
> To register user by feature map to device DB

```c
int kdp_register_user_by_fm(
	int dev_idx
	uint32_t user_id
	char* fm
	int fm_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>user_id</em>         [in]      the user to be register. start from 1
<em>fm</em>              [in]      feature map data to register
<em>fm_len</em>          [in]      feature map data size in byte
</pre>
**Returns:**

fm index on succeed, -1 on failure


---
### kdp_remove_user
> To remove user from device DB

```c
int kdp_remove_user(
	int dev_idx
	uint32_t user_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>user_id</em>         [in]      the user to be removed. 0 for all users
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> Must be called after kdp_start_sfid_mode() is called


---
### kdp_report_sys_status
> To request for system status

```c
int kdp_report_sys_status(
	int dev_idx
	uint32_t* sfw_id
	uint32_t* sbuild_id
	uint16_t* sys_status
	uint16_t* app_status
	uint32_t* nfw_id
	uint32_t* nbuild_id
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID. A host can connect several devices
<em>sfw_id</em>          [out]     the version of the scpu firmware
<em>sbuild_id</em>       [out]     the build number of the scpu firmware
<em>sys_status</em>      [out]     system status (Beta)
<em>app_status</em>      [out]     application status (Beta)
<em>nfw_id</em>          [out]     the version of the ncpu firmware
<em>nbuild_id</em>       [out]     the build number of the ncpu firmware
</pre>
**Returns:**

0 on succeed, -1 on failure


---
### kdp_reset_sys
> To request for doing system reset

```c
int kdp_reset_sys(
	int dev_idx
	uint32_t reset_mode
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID. A host can connect several devices
<em>reset_mode</em>      [in]      specifies the reset mode
                          0 - no operation
                          1 - reset message protocol
                          3 - switch to suspend mode
                          4 - switch to active mode
                          255 - reset whole system
                          256 - system shutdown(RTC)
                          0x1000xxxx - reset debug output level
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_scan_usb_devices
> To scan all Kneron devices and report a list

```c
int kdp_scan_usb_devices(
	kdp_device_info_list_t **list
)
```
**Parameters:**

<pre>
<em>list</em>            [in]      an input, the API will allocate memory and fullfill the content.
</pre>
**Returns:**

always 0


---
### kdp_set_ckey
> To set a customized key

```c
int kdp_set_ckey(
	int dev_idx
	uint32_t ckey
	uint32_t *set_status
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>ckey</em>            [in]      the key to program
<em>set_status</em>      [out]     status code
                          0xFFFF: command not supported in this FW
                          0x0   : OK
                          0x1   : cannot burn eFuse
                          0x2   : eFuse protected
</pre>
**Returns:**

0 on succeed, -1 on failure


**Notes:**

> 
> WARNING!!! This API is only for ODM/OEM company


---
### kdp_set_db_config
> Configurate DB structure

```c
int kdp_set_db_config(
	int dev_idx
	kdp_db_config_t* db_config
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_config</em>       [in]      configuration data
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> WARNING!!!
> After calling this API, DB will be removed and reformatted
> DB structure by user configuration


---
### kdp_set_db_version
> Set DB version number

```c
int kdp_set_db_version(
	int dev_idx
	uint32_t db_version
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_version</em>      [in]      version number of DB
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_set_sbt_key
> To set security boot key

```c
int kdp_set_sbt_key(
	int dev_idx
	uint32_t entry
	uint32_t key
	uint32_t *set_status
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>entry</em>           [in]      0~13, security key offset
<em>key</em>             [in]      key value
<em>set_status</em>      [out]     status code
</pre>
**Returns:**

0 on succeed, -1 on failure


**Notes:**

> for KL720 only


---
### kdp_start_dme
> To request for starting dynamic model execution (Deprecated)

```c
int kdp_start_dme(
	int dev_idx
	uint32_t model_size
	char* data
	int dat_size
	uint32_t* ret_size
	char* img_buf
	int buf_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>model_size</em>      [in]      size of inference model
<em>data</em>            [in]      firmware setup data
<em>dat_size</em>        [in]      setup data size
<em>ret_size</em>        [out]     returned model size
<em>img_buf</em>         [in]      the model file buffer
<em>buf_len</em>         [in]      the buffer size
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_start_dme_ext
> To request for starting dynamic model execution

```c
int kdp_start_dme_ext(
	int dev_idx
	char* nef_model_data
	uint32_t model_size
	uint32_t* ret_size
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>model_data</em>      [in]      NEF model data
<em>model_size</em>      [in]      size of nef model
<em>ret_size</em>        [out]     returned model size
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> 
> Only support NEF model file with 1 model
> Composed model set is not supported


---
### kdp_start_isi_mode
> start the user isi mode with specified app id and return data size

```c
int kdp_start_isi_mode(
	int dev_idx
	uint32_t app_id
	uint32_t return_size
	uint16_t width
	uint16_t height
	uint32_t format
	uint32_t* rsp_code
	uint32_t* buf_size
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>app_id</em>          [in]      application id. Refer to common/include/kapp_id.h
<em>return_size</em>     [in]      this size reserved for ISI result
<em>img_width</em>       [in]      the width of input image
<em>img_height</em>      [in]      the height of input image
<em>format</em>          [in]      the input image format
<em>rep_code</em>        [out]     response code
<em>buf_size</em>        [out]     the depth of the image buffer will be returned.
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> 
> For format, refer to common/include/inp.h and find IMAGE_FORMAT_XXX


---
### kdp_start_isi_mode_ext
> start the user isi mode with isi configuration

```c
int kdp_start_isi_mode_ext(
	int dev_idx
	char* isi_cfg
	int cfg_size
	uint32_t* rsp_code
	uint32_t* buf_size
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>isi_cfg</em>         [in]      isi configuration data
<em>cfg_size</em>        [in]      isi configuration data size
<em>rsp_code</em>        [out]     response code from device
<em>buf_size</em>        [out]     the depth of the image buffer will be returned.
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_start_reg_user_mode
> Start the user register mode

```c
int kdp_start_reg_user_mode(
	int dev_idx
	uint16_t usr_id
	uint16_t img_idx
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>user_id</em>         [in]      the user id to be registered
<em>img_idx</em>         [in]      the image idx to be saved
</pre>
**Returns:**

0 on succeed, -1 on failure


**Notes:**

> 
> - user_id stars from 1 and limited by DB MAX configuration
> - img_idx is limited by DB MAX configration


---
### kdp_start_sfid_mode
> Start the user sfid mode with specified threshold, image format

```c
int kdp_start_sfid_mode(
	int dev_idx
	uint32_t* img_size
	float thresh
	uint16_t width
	uint16_t height
	uint32_t format
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID.
<em>img_size</em>        [in]      the required image file size will be returned for confirmation
<em>thresh</em>          [in]      threshold used to match face recognition result. range:0.0-1.0
                          0: use default threshold
<em>img_width</em>       [in]      the width of input image
<em>img_height</em>      [in]      the height of input image
<em>format</em>          [in]      the input image format
</pre>
**Returns:**

0 on succeed, error code on failure


**Notes:**

> 
> - The width of input image MUST be multiple of 2 for RGB565/YCBCR422
> - The width of input image MUST be multiple of 4 for NIR8
> - For foramt configuration, refer to common/include/ipc.h and find IMAGE_FORMAT_XXX


---
### kdp_switch_db_index
> Switch current DB index

```c
int kdp_switch_db_index(
	int dev_idx
	uint32_t db_idx
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>db_idx</em>          [in]      index of target db
</pre>
**Returns:**

0 on succeed, error code on failure


---
### kdp_update_fw
> To request for update firmware

```c
int kdp_update_fw(
	int dev_idx
	uint32_t* module_id
	char* img_buf
	int buf_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>module_id</em>       [in]      the module id of which the firmware to be updated
                          0 - no operation
                          1 - scpu module
                          2 - ncpu module
<em>img_buf</em>         [in]      FW image buffer
<em>buf_len</em>         [in]      buffer size
</pre>
**Returns:**

0 if succeed, error code for failure


---
### kdp_update_model
> To request for update model (Deprecated)

```c
int kdp_update_model(
	int dev_idx
	uint32_t* model_id
	uint32_t model_size
	char* img_buf
	int buf_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>model_id</em>        [in]      (reserved, no function) the model id to be updated
<em>model_size</em>      [in]      the size of the model
<em>img_buf</em>         [in]      the fw image buffer
<em>buf_len</em>         [in]      the buffer size
</pre>
**Returns:**

0 if succeed, error code for failure


---
### kdp_update_nef_model
> To request for update nef model

```c
int kdp_update_nef_model(
	int dev_idx
	char* img_buf
	int buf_len
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>img_buf</em>         [in]      the nef model buffer
<em>buf_len</em>         [in]      the buffer size
</pre>
**Returns:**

0 if succeed, else error code


---
### kdp_update_spl
> To request for update spl

```c
int kdp_update_spl(
	int dev_idx
	uint32_t mode
	uint16_t auth_type
	uint16_t spl_size
	uint8_t* auth_key
	char* spl_buf
	uint32_t* rsp_code
	uint32_t* spl_id
	uint32_t* spl_build
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID
<em>mode</em>            [in]      the command mode to be exercised
<em>auth_type</em>       [in]      the authenticator type
<em>spl_size</em>        [in]      the spl fw image file size
<em>auth_key</em>        [in]      the authenticator key
<em>spl_buf</em>         [in]      the spl fw image buf
<em>rsp_code</em>        [out]     respone code
<em>spl_id</em>          [out]     the id of the spl firmware in device (post command execution)
<em>spl_build</em>       [out]     the build number of the spl firmware
</pre>
**Returns:**

0 if succeed, error code for failure


**Notes:**

> 
> WARNING!!! This API is only for ODM/OEM company


---
### kdp_verify_user_id_generic
> Perform the face recognition by input image with specified output

```c
int kdp_verify_user_id_generic(
	int dev_idx
	uint16_t* user_id
	char* img_buf
	int buf_len
	uint16_t* mask
	char* res
)
```
**Parameters:**

<pre>
<em>dev_idx</em>         [in]      connected device ID.
<em>user_id</em>         [in]      found matched user ID
<em>img_buf</em>         [in]      the image buffer
<em>buf_len</em>         [in]      the buffer size
<em>mask</em>            [in,out]  input:indicate the mask of requested data, output:responsed flags
<em>res</em>             [out]     pre-allocated memory for the specified output
                          call kdp_get_res_size() to get result size
</pre>
**Returns:**

0 on succeed, error code on failure


---
