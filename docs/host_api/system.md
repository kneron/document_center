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

   &nbsp;

### Scan Devices

`int kdp_scan_usb_devices(kdp_device_info_list_t **list)`

* Scan all Kneron USB devices and output a report list. 
* Below shows the data structures for `kdp_device_info_list_t`.

```c
enum kdp_usb_speed
{
    KDP_USB_SPEED_UNKNOWN = 0,
    KDP_USB_SPEED_LOW = 1,
    KDP_USB_SPEED_FULL = 2,
    KDP_USB_SPEED_HIGH = 3,
    KDP_USB_SPEED_SUPER = 4,
};

enum kdp_product_id
{
    KDP_DEVICE_KL520 = 0x100,
    KDP_DEVICE_KL720 = 0x200,
};

typedef struct
{
    int scan_index;             // scanned order index, can be used by kdp_connect_usb_device()
    bool isConnectable;         // indicate if this device is connectable
    unsigned short vendor_id;   // supposed to be 0x3231
    unsigned short product_id;  // enum kdp_product_id
    int link_speed;             // enum kdp_usb_speed
    unsigned int serial_number; // KN number
    char device_path[20]; 		// "bus-hub_port-device_port", ex: "1-2-3", means bus 1 - (hub) port 2 - (device) port 3
} kdp_device_info_t;

typedef struct
{
    int num_dev;
    kdp_device_info_t kdevice[1]; // real index range from 0 ~ (num_dev-1)
} kdp_device_info_list_t;
```

 * list: this API automatically allocates memory for the content of `kdp_device_info_list_t` and assigns the pointer value to the 'list'; users may free it after reading needed information.

 * return: it always returns 0.

 * example code:

```c
kdp_device_info_list_t *list = NULL;
kdp_scan_usb_devices(&list);

for (int i = 0; i < list->num_dev; i++)
{
	/* reading the content of list->kdevice[i] for whatever wanted */
}

free(list);
```

   &nbsp;

### Connect To USB Device

`int kdp_connect_usb_device(int scan_index)`

 * Connect to one Kneron USB device via the `scan_index`.
    * `scan_index` basically begins from 1 and it can be correctly informed through `kdp_scan_usb_devices`.
    * If having only one Kneron USB device physically connected, you can make `scan_index = 1 `  without scanning devices.
    * In the case of multiple devices or dongles, it is better to scan all devices to get `scan_index` respectively and use this API to connect wanted one.
 * scan_index: an scanned index representing one Kneron USB device.
 * return dev index (>= 0) on succeed, -1 on failure.
 * Example code (with only one device):

```c
int dev_idx = kdp_connect_usb_device(1);

/* then invoke other APIs with dev_idx as input */
```

&nbsp;

 * Example code (with multiple devices):

```c
kdp_device_info_list_t *list = NULL;
kdp_scan_usb_devices(&list);

int dev_idx[10];

for (int i = 0; i < list->num_dev; i++)
{
    int sidx = list->kdevice[i].scan_index
	dev_idx[i] = kdp_connect_usb_device(sidx);
}

free(list);

/* then invoke other APIs with dev_idx[i] as input */
```

&nbsp;

### Add Device (Deprecated)

`int kdp_add_dev(int type, const char* name);`

 * add one KL520 USB device to the host lib.
    * this API is deprecated. (replaced by **kdp_connect_usb_device**)
    * this API supports only one KL520 USB device.
    
 * type: the device type, only KDP_USB_DEV is supported.

 * name: not used.

 * return dev index (>= 0) on succeed, -1 on failure.

   &nbsp;

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

