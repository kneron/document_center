# Core API


Core functions provide fundamental functionality like connection and firmware update.
 
It also contains the generic inference functions.
 




**Include Header File:**  kdp2_core.h

- Functions
    - [kdp2_connect_device](#kdp2_connect_device)
    - [kdp2_connect_device_by_kn_number](#kdp2_connect_device_by_kn_number)
    - [kdp2_connect_device_by_port_path](#kdp2_connect_device_by_port_path)
    - [kdp2_connect_device_by_product](#kdp2_connect_device_by_product)
    - [kdp2_disconnect_device](#kdp2_disconnect_device)
    - [kdp2_get_device_descriptor](#kdp2_get_device_descriptor)
    - [kdp2_load_model](#kdp2_load_model)
    - [kdp2_load_model_from_file](#kdp2_load_model_from_file)
    - [kdp2_raw_inference_receive](#kdp2_raw_inference_receive)
    - [kdp2_raw_inference_retrieve_node](#kdp2_raw_inference_retrieve_node)
    - [kdp2_raw_inference_send](#kdp2_raw_inference_send)
    - [kdp2_reset_device](#kdp2_reset_device)
    - [kdp2_scan_devices](#kdp2_scan_devices)
    - [kdp2_set_timeout](#kdp2_set_timeout)
    - [kdp2_update_firmware](#kdp2_update_firmware)
    - [kdp2_update_firmware_from_file](#kdp2_update_firmware_from_file)


---




## Functions
### kdp2_connect_device
> To connect a Kneron device via the 'scan_index'.

```c
kdp2_device_t kdp2_connect_device(
	int scan_index
)
```
**Parameters:**

<pre>
<em>scan_index</em>                the dev_idx to connect.
                          value starts from 1, can be retrieved through kdp2_scan_devices().
</pre>
**Returns:**

kdp2_device_t represents a device handle, if NULL means failed.


---
### kdp2_connect_device_by_kn_number
> To connect a Kneron device via the 'KN number'.

```c
kdp2_device_t kdp2_connect_device_by_kn_number(
	uint32_t kn_num
)
```
**Parameters:**

<pre>
<em>kn_num</em>                    the unique KN number for a Kneron device.
</pre>
**Returns:**

kdp2_device_t represents a device handle, if NULL means failed.


---
### kdp2_connect_device_by_port_path
> To connect a Kneron device via the port path.

```c
kdp2_device_t kdp2_connect_device_by_port_path(
	const char *port_path
)
```
**Parameters:**

<pre>
<em>port_path</em>                 the USB port path of target device.
</pre>
**Returns:**

kdp2_device_t represents a device handle, if NULL means failed.


---
### kdp2_connect_device_by_product
> To connect the first connectable Kneron device for specified 'product ID'.

```c
kdp2_device_t kdp2_connect_device_by_product(
	kdp2_product_id_t prod_id
)
```
**Parameters:**

<pre>
<em>prod_id</em>                   refer to kdp2_product_id_t.
</pre>
**Returns:**

kdp2_device_t represents a device handle, if NULL means failed.


---
### kdp2_disconnect_device
> To disconnect a Kneron device.

```c
int kdp2_disconnect_device(
	kdp2_device_t device
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_get_device_descriptor
> To get the device descriptor of a connected device from perspective of USB .

```c
kdp2_device_descriptor_t * kdp2_get_device_descriptor(
	kdp2_device_t device
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
</pre>
**Returns:**

refer to kdp2_device_descriptor_t.


---
### kdp2_load_model
> upload models to device through USB

```c
int kdp2_load_model(
	kdp2_device_t device
	void *nef_buf
	int nef_size
	kdp2_all_models_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>nef_buf</em>                   a buffer contains the content of NEF file.
<em>nef_size</em>                  file size of the NEF.
<em>model_desc</em>                this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_load_model_from_file
> Similar to kdp2_load_model(), and it accepts file path instead of a buffer.

```c
int kdp2_load_model_from_file(
	kdp2_device_t device
	const char *file_path
	kdp2_all_models_descriptor_t *model_desc
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>file_path</em>                 a buffer contains the content of NEF file.
<em>model_desc</em>                this parameter is output for describing the uploaded models.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_raw_inference_receive
> Generic raw inference receive.

```c
int kdp2_raw_inference_receive(
	kdp2_device_t device
	kdp2_raw_output_descriptor_t *output_desc
	uint8_t *raw_out_buffer
	uint32_t buf_size
)
```
When a image inference is done, this function can be used to get the results in RAW format.
 
Note that the data received is in Kneron RAW format, users need kdp2_raw_inference_retrieve_node() to convert RAW format data to floating-point data.
 


**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>output_desc</em>               refer to kdp2_raw_output_descriptor_t for describing some information of received data.
<em>raw_out_buffer</em>            a user-allocated buffer for receiving the RAW data results, the needed buffer size can be known from the 'max_raw_out_size' in 'model_desc' through kdp2_load_model().
<em>raw_buf_size</em>              size of raw_out_buffer.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_raw_inference_retrieve_node
> Retrieve single node output data from raw output buffer.

```c
kdp2_node_output_t * kdp2_raw_inference_retrieve_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
)
```
This function retrieves and converts RAW format data to floating-point data on the per-node basis.
 
The pointer of 'kdp2_node_output_t' actually points to raw_out_buffer so do not free raw_out_buffer before completing the use of 'kdp2_node_output_t *'
 


**Parameters:**

<pre>
<em>node_idx</em>                  wanted output node index, starts from 0. Number of total output nodes can be known from 'kdp2_raw_output_descriptor_t'
<em>raw_out_buffer</em>            the RAW output buffer, it should come from kdp2_raw_inference_receive().
</pre>
**Returns:**

refer to kdp2_node_output_t. It describe 'width x height x channel' in conjunction with floating-pint values of this node.


---
### kdp2_raw_inference_send
> Generic raw inference send.

```c
int kdp2_raw_inference_send(
	kdp2_device_t device
	kdp2_raw_input_descriptor_t *inf_desc
	uint8_t *image_buffer
)
```
This is to perform a single image inference, it is non-blocking if device buffer queue is not full.
 
When this is performed, user can issue kdp2_raw_inference_receive() to get the result.
 
In addition, to have better performance, users can issue multiple kdp2_raw_inference_send() then start to receive results through kdp2_raw_inference_receive().
 


**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>inf_desc</em>                  needed parameters for performing inference including image width, height ..etc.
<em>image_buffer</em>              the buffer contains the image.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_reset_device
> reset the device in hardware mode or software mode.

```c
int kdp2_reset_device(
	kdp2_device_t device
	kdp2_reset_mode_t reset_mode
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>reset_mode</em>                refer to kdp2_reset_mode_t.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_scan_devices
> Scan all Kneron devices and report a list.

```c
int kdp2_scan_devices(
	kdp2_devices_list_t **list
)
```
This function can get devices connectivity information at runtime.
 
**kdp2_devices_list_t** is a data structure containing multiple **kdp2_device_descriptor_t** and each represents one scanned device.
 
The **scan_index** in the **kdp2_device_descriptor_t** can be used as inputs when connecting a specified device.
 
Example usage:
 
> kdp2_devices_list_t *list;
 
> kdp2_scan_devices(&list);
 
> .. use list ..
 
> free(list);
 
 


**Parameters:**

<pre>
<em>list</em>                      is an input, the API will allocate memory and fullfill the content.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_set_timeout
> To set a global timeout value for all USB communications with the device.

```c
void kdp2_set_timeout(
	kdp2_device_t device
	int milliseconds
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>milliseconds</em>              pre-set timeout value in milliseconds.
</pre>
---
### kdp2_update_firmware
> update firmware to specified device.

```c
int kdp2_update_firmware(
	kdp2_device_t device
	kdp2_firmware_id_t fw_id
	void *buffer
	int size
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>fw_id</em>                     update ID, refer to kdp2_firmware_id_t.
<em>buffer</em>                    buffer for the update content
<em>size</em>                      buffer size
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
### kdp2_update_firmware_from_file
> Similar to kdp2_update_firmware(), and it accepts file path instead of a buffer.

```c
int kdp2_update_firmware_from_file(
	kdp2_device_t device
	kdp2_firmware_id_t fw_id
	const char *file_path
)
```
**Parameters:**

<pre>
<em>device</em>                    a connected device handle.
<em>fw_id</em>                     update ID, refer to kdp2_firmware_id_t.
<em>file_path</em>                 a buffer contains the content of NEF file.
</pre>
**Returns:**

refer to KDP2_API_RETURN_CODE.


---
