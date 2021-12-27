# Kneron PLUS core APIs


Core functions provide fundamental functionality like connection and firmware update
 
 




**Include Header File:**  kp_core.h

- Functions
    - [kp_connect_devices](#kp_connect_devices)
    - [kp_disable_firmware_log](#kp_disable_firmware_log)
    - [kp_disconnect_devices](#kp_disconnect_devices)
    - [kp_enable_firmware_log](#kp_enable_firmware_log)
    - [kp_error_string](#kp_error_string)
    - [kp_get_model_info](#kp_get_model_info)
    - [kp_get_system_info](#kp_get_system_info)
    - [kp_get_version](#kp_get_version)
    - [kp_install_driver_for_windows](#kp_install_driver_for_windows)
    - [kp_load_encrypted_models](#kp_load_encrypted_models)
    - [kp_load_encrypted_models_from_file](#kp_load_encrypted_models_from_file)
    - [kp_load_firmware](#kp_load_firmware)
    - [kp_load_firmware_from_file](#kp_load_firmware_from_file)
    - [kp_load_model](#kp_load_model)
    - [kp_load_model_from_file](#kp_load_model_from_file)
    - [kp_load_model_from_flash](#kp_load_model_from_flash)
    - [kp_profile_get_statistics](#kp_profile_get_statistics)
    - [kp_profile_set_enable](#kp_profile_set_enable)
    - [kp_reset_device](#kp_reset_device)
    - [kp_scan_devices](#kp_scan_devices)
    - [kp_set_timeout](#kp_set_timeout)


---




## **Functions**
### **kp_connect_devices**
> To connect multiple (including one) Kneron devices.

```c
kp_device_group_t kp_connect_devices(
	int num_devices
	int device_port_ids[]
	int *error_code
)
```
**Parameters:**

<pre>
<em>num_devices</em>     [in]      number of devices
<em>device_port_ids</em> [in]      an array contains device's port ID which can be known from kp_scan_devices(), if '0' is given then it will try to connect first connectable device.
<em>error_code</em>      [out]     optional variable to indicate an error if connecting devices failed.
</pre>
**Returns:**

kp_device_group_t represents a set of devices handle, if NULL means failed.


---
### **kp_disable_firmware_log**
> Disable firmware log of all devices with firmware log enabled.

```c
int kp_disable_firmware_log(
	kp_device_group_t devices
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_disconnect_devices**
> To disconnect a Kneron device.

```c
int kp_disconnect_devices(
	kp_device_group_t devices
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_enable_firmware_log**
> Enable firmware log from certain device.

```c
int kp_enable_firmware_log(
	kp_device_group_t devices
	int dev_port_id
	char *log_file_path
)
```
This function enables receiving firmware log from certain device with specific device index.
The firmware log could be written to text file or directly output to stdout.
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>dev_port_id</em>     [in]      the device port id to enable firmware log.
<em>log_file_path</em>   [in]      the log file path, if NULL is passed then firmware log would be directly output to stdout.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_error_string**
> Translate error code to char string.

```c
const char *kp_error_string(
	int error_code
)
```
**Parameters:**

<pre>
<em>error_code</em>      [in]      status/error code from enum KP_API_RETURN_CODE.
</pre>
**Returns:**

a char buffer of string represents the error message.


---
### **kp_get_model_info**
> Get model info (crc, model id, etc.).

```c
int kp_get_model_info(
	kp_device_group_t devices
	int dev_port_id
	kp_model_nef_descriptor_t *all_models_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>dev_port_id</em>     [in]      specific device port id.
<em>all_models_desc</em> [out]     return value of model info.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_get_system_info**
> Get system info (kn number and firmware version).

```c
int kp_get_system_info(
	kp_device_group_t devices
	int dev_port_id
	kp_system_info_t *system_info
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>dev_port_id</em>     [in]      specific device port id.
<em>system_info</em>     [out]     return value of system info.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_get_version**
> Get PLUS version.

```c
const char *kp_get_version()
```
**Returns:**

a string represents the PLUS version.


---
### **kp_install_driver_for_windows**
> Install device driver on Windows

```c
int kp_install_driver_for_windows(
	kp_product_id_t device_pid
)
```
**Parameters:**

<pre>
<em>device_pid</em>                product id of the device
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_encrypted_models**
> upload encrypted models to multiple device through USB

```c
int kp_load_encrypted_models(
	kp_device_group_t devices
	void *nef_buf[]
	int nef_size
	int nef_num
	kp_model_nef_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>nef_buf</em>         [in]      number of buffers that contain the content of NEF files.
<em>nef_size</em>        [in]      file size of the NEF.
<em>nef_num</em>         [in]      total number of NEF files.
<em>model_desc</em>      [out]     this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


**Notes:**

> for `nef_size`, the lengths of all encrypted NEF files originated from the same unencrypted NEF file should be the same.


---
### **kp_load_encrypted_models_from_file**
> Similar to kp_load_encrypted_models(), and it accepts file paths instead of buffers.

```c
int kp_load_encrypted_models_from_file(
	kp_device_group_t devices
	char *file_path[]
	int nef_num
	kp_model_nef_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>file_path</em>       [in]      file pathes of NEF files.
<em>nef_num</em>         [in]      total number of NEF files.
<em>model_desc</em>      [out]     this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_firmware**
> upload firmware from buffers

```c
int kp_load_firmware(
	kp_device_group_t devices
	void *scpu_fw_buf
	int scpu_fw_size
	void *ncpu_fw_buf
	int ncpu_fw_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>scpu_fw_buf</em>     [in]      scpu firmware buffer
<em>scpu_fw_size</em>    [in]      scpu firmware size
<em>ncpu_fw_buf</em>     [in]      ncpu firmware buffer
<em>ncpu_fw_size</em>    [in]      ncpu firmware size
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_firmware_from_file**
> upload firmware from file

```c
int kp_load_firmware_from_file(
	kp_device_group_t devices
	const char *scpu_fw_path
	const char *ncpu_fw_path
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>scpu_fw_path</em>    [in]      scpu firmware file path
<em>ncpu_fw_path</em>    [in]      ncpu firmware file path
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_model**
> upload models to device through USB

```c
int kp_load_model(
	kp_device_group_t devices
	void *nef_buf
	int nef_size
	kp_model_nef_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>nef_buf</em>         [in]      a buffer contains the content of NEF file.
<em>nef_size</em>        [in]      file size of the NEF.
<em>model_desc</em>      [out]     this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_model_from_file**
> Similar to kp_load_model(), and it accepts file path instead of a buffer.

```c
int kp_load_model_from_file(
	kp_device_group_t devices
	const char *file_path
	kp_model_nef_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>file_path</em>       [in]      a buffer contains the content of NEF file.
<em>model_desc</em>      [out]     this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_load_model_from_flash**
> Load model from device flash

```c
int kp_load_model_from_flash(
	kp_device_group_t devices
	kp_model_nef_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>model_desc</em>      [out]     this parameter is output for describing the uploaded models.
                          
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_profile_get_statistics**
> Collect inference profile results.

```c
int kp_profile_get_statistics(
	kp_device_group_t devices
	kp_profile_data_t *profile_data
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>profile_data</em>    [out]     refer to kp_profile_data_t.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_profile_set_enable**
> To set enable/disable debug profile.

```c
int kp_profile_set_enable(
	kp_device_group_t devices
	bool enable
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>enable</em>          [in]      set enable/disable.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_reset_device**
> reset the device in hardware mode or software mode.

```c
int kp_reset_device(
	kp_device_group_t devices
	kp_reset_mode_t reset_mode
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>reset_mode</em>      [in]      refer to kp_reset_mode_t.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_scan_devices**
> Scan all Kneron devices and report a list.

```c
kp_devices_list_t *kp_scan_devices()
```
This function can get devices connectivity information at runtime.
 


**Returns:**

refer to kp_devices_list_t.


---
### **kp_set_timeout**
> To set a global timeout value for all USB communications with the device.

```c
void kp_set_timeout(
	kp_device_group_t devices
	int milliseconds
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>milliseconds</em>    [in]      pre-set timeout value in milliseconds.
</pre>
---
