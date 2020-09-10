# System API

System API is for system control, init/deinit system, and update firmware and models.

### Init

`int kdp_lib_init();`

 * init the host library
 * return 0 on succeed, -1 on failure


### Start

`int kdp_lib_start();`

 * start the host library to wait for messages
 * return 0 on succeed, -1 on failure


### De Init

`int kdp_lib_de_init(); `

 * free the resources used by host lib
 * return 0 on succeed, -1 on failure


### Init Log

`int kdp_init_log(const char* dir, const char* name);`

 * init the host lib internal log
 * dir: the directory name of the log file
 * name: the log file name
 * return 0 on succeed, -1 on failure

### Add Device

`int kdp_add_dev(int type, const char* name);`

 * add com device to the host lib
 * type: the device type, only KDP_UART_DEV supported now
 * name: the UART device name
 * return dev idx on succeed, -1 on failure

### System Reset
`int kdp_reset_sys(int dev_idx, uint32_t reset_mode);`

 * request for doing system reset
 * dev_idx: connected device ID. A host can connect several devices
 * reset_mode: specifies the reset mode

 *             0 - no operation
               1 - reset message protocol
               3 - switch to suspend mode
               4 - switch to active mode
               255 - reset whole system
               256 - system shutdown(RTC)
               0x1000xxxx - reset debug output level

 * return value: 0 on succeed, else for error code



### System Status

`int kdp_report_sys_status(int dev_idx, uint32_t* sfw_id, uint32_t* sbuild_id,
                           uint16_t* sys_status, uint16_t* app_status, 
                           uint32_t* nfw_id, uint32_t* nbuild_id);`

 * request for system status
 * dev_idx: connected device ID. A host can connect several devices
 * device: the name of the device
 * sfw_id: the id of the scpu firmware in device
 * sbuild_id: the build number of the scpu firmware in device
 * sys_status: system status
 * app_status: application status
 * nfw_id: the id of the ncpu firmware in device
 * nbuild_id: the build number of the ncpu firmware in device
 * return value: 0 on succeed, else -1

### Get KN Number

`int kdp_get_kn_number(int dev_idx, uint32_t *kn_num);`

 * request for system KN number
 * dev_idx: connected device ID. A host can connect several devices
 * kn_num: the pointer to store KN number
 * return value: 0 on succeed, else -1

### Get Model Info

`int kdp_get_model_info(int dev_idx, int from_ddr, char *data_buf);`

 * request for model IDs in DDR or Flash
 * dev_idx: connected device ID. A host can connect several devices
 * from_ddr: if models are in ddr (1) or flash (0)
 * data_buf: the pointer to store model info
 * return value: 0 on succeed, else -1

### Update Firmware

`int kdp_update_fw(int dev_idx, uint32_t* module_id, char* img_buf, int buf_len);`

 * request for update firmware
 * dev_idx: connected device ID. A host can connect several devices
 * module_id: the module id of which the firmware to be updated
              0 - no operation
              1 - scpu module
              2 - ncpu module
 * img_buf, buf_len: the fw image buffer and file size
 * return value: 0 if succeed, else error code

### Update Model

`int kdp_update_model(int dev_idx, uint32_t* model_id, uint32_t model_size,
                     char* img_buf, int buf_len);`

 * request for update model
 * dev_idx: connected device ID. A host can connect several devices
 * model_id: the model id to be updated
 * model_size: the size of the model
 * img_buf, buf_len: the fw image buffer and file size
 * return value: 0 if succeed, else error code
 

### Update SPL

`int kdp_update_spl(int dev_idx, uint32_t mode, uint16_t auth_type, uint16_t spl_size,
                    uint8_t* auth_key, char* spl_buf, uint32_t* rsp_code, 
                    uint32_t* spl_id, uint32_t* spl_build);`

 * request for update spl
 * dev_idx: connected device ID. A host can connect several devices
 * mode: the command mode to be exercised
 * auth_type, auth_key: the authenticator type and key
 * spl_buf and size: the spl fw image and file size
 * spl_id: the id of the spl firmware in device (post command execution)
 * spl_build: the build number of the spl firmware in device
 * return value: 0 if succeed, else error code

