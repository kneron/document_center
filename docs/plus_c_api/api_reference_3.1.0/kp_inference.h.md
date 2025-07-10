# Kneron PLUS inference APIs


The inference functions provide sophisticated functionally for different applications.
Different set of inference APIs would need different models to make it work.
 
 




**Include Header File:**  kp_inference.h

- Functions
    - [kp_customized_command_noack_send](#kp_customized_command_noack_send)
    - [kp_customized_command_send](#kp_customized_command_send)
    - [kp_customized_inference_receive](#kp_customized_inference_receive)
    - [kp_customized_inference_send](#kp_customized_inference_send)
    - [kp_dbg_receive_checkpoint_data](#kp_dbg_receive_checkpoint_data)
    - [kp_dbg_set_enable_checkpoints](#kp_dbg_set_enable_checkpoints)
    - [kp_generic_data_inference_receive](#kp_generic_data_inference_receive)
    - [kp_generic_data_inference_send](#kp_generic_data_inference_send)
    - [kp_generic_image_inference_receive](#kp_generic_image_inference_receive)
    - [kp_generic_image_inference_send](#kp_generic_image_inference_send)
    - [kp_generic_inference_retrieve_fixed_node](#kp_generic_inference_retrieve_fixed_node)
    - [kp_generic_inference_retrieve_float_node](#kp_generic_inference_retrieve_float_node)
    - [kp_generic_inference_retrieve_raw_fixed_node](#kp_generic_inference_retrieve_raw_fixed_node)
    - [kp_inference_configure](#kp_inference_configure)
    - [kp_profile_get_statistics](#kp_profile_get_statistics)
    - [kp_profile_set_enable](#kp_profile_set_enable)
    - [kp_release_dbg_checkpoint_data](#kp_release_dbg_checkpoint_data)
    - [kp_release_fixed_node_output](#kp_release_fixed_node_output)
    - [kp_release_float_node_output](#kp_release_float_node_output)
    - [kp_release_raw_fixed_node_output](#kp_release_raw_fixed_node_output)


---




## **Functions**
### **kp_customized_command_noack_send**
> To sned command.

```c
int kp_customized_command_noack_send(
	kp_device_group_t devices
	void *cmd
	int cmd_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>cmd</em>             [in]      RMI command.
<em>cmd_size</em>        [in]      write length.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_customized_command_send**
> send a user-defined command and receive the command result, users also need to implement code in firmware side as well.

```c
int kp_customized_command_send(
	kp_device_group_t devices
	void *cmd
	int cmd_size
	void *return_buf
	int return_buf_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>cmd</em>             [in]      user-defined command buffer, shoud include 'kp_inference_header_stamp_t' in the beginning; using 'job_id' as user-defined command ID, others will be handled by API.
<em>cmd_size</em>        [in]      command buffer size.
<em>return_buf</em>      [out]     user-defined command return buffer in any user-defined format.
<em>return_buf_size</em> [out]     return buffer size.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_customized_inference_receive**
> receive inference result of age gender

```c
int kp_customized_inference_receive(
	kp_device_group_t devices
	void *result_buffer
	int buf_size
	int *recv_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>result_buffer</em>   [out]     user-prepared result buffer, when receiving data, it begins with 'kp_inference_header_stamp_t'. user should guarantee buffer size is big enough.
<em>buf_size</em>        [in]      result buffer size.
<em>recv_size</em>       [out]     received result size.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_customized_inference_send**
> send image for age gender inference

```c
int kp_customized_inference_send(
	kp_device_group_t devices
	void *header
	int header_size
	uint8_t *image
	int image_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>header</em>          [in]      user-defined image header, shoud include 'kp_inference_header_stamp_t' in the beginning; in the header stamp, only 'job_id' is needed for user to fill in, others will be handled by API.
<em>header_size</em>     [in]      image header size.
<em>image</em>           [in]      image buffer.
<em>image_size</em>      [in]      image buffer size.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_dbg_receive_checkpoint_data**
> To receive debug checkpoint data, use it only if you enable kp_dbg_set_enable_checkpoints().

```c
int kp_dbg_receive_checkpoint_data(
	kp_device_group_t devices
	void **checkpoint_buf
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>checkpoint_buf</em>  [out]     a buffer contains checkpoint data, memory is allocated automatically while needed.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_dbg_set_enable_checkpoints**
> Enable/Disable inference breakpoints in firmware for inference debugging purpose.

```c
int kp_dbg_set_enable_checkpoints(
	kp_device_group_t devices
	uint32_t checkpoint_flags
	bool enable
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>checkpoint_flags</em>[in]      bit-fields settings, refer to kp_dbg_checkpoint_flag_t.
<em>enable</em>          [in]      set enable/disable.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_data_inference_receive**
> 

```c
int kp_generic_data_inference_receive(
	kp_device_group_t devices
	kp_generic_data_inference_result_header_t *output_desc
	uint8_t *raw_out_buffer
	uint32_t buf_size
)
```
When a image inference is done, this function can be used to get the results in RAW format.
 
Note that the data received is in Kneron RAW format, users need kp_generic_inference_retrieve_float_node() to convert RAW format data to floating-point data.
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>output_desc</em>     [in]      refer to kp_generic_data_inference_result_header_t for describing some information of received data.
<em>raw_out_buffer</em>  [out]     a user-allocated buffer for receiving the RAW data results, the needed buffer size can be known from the 'max_raw_out_size' in 'model_desc' through kp_load_model().
<em>buf_size</em>        [in]      size of raw_out_buffer.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_data_inference_send**
> Generic raw inference with multiple input images and bypass pre-process send.

```c
int kp_generic_data_inference_send(
	kp_device_group_t devices
	kp_generic_data_inference_desc_t *inf_data
)
```
This is to perform one model inference with multiple input images without pre-processing on device, it is non-blocking if device buffer queue is not full.
 
When this is performed, user can issue kp_generic_data_inference_receive() to get the result.
 
In addition, to have better performance, users can issue multiple kp_generic_data_inference_send() then start to receive results through kp_generic_data_inference_receive().
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>inf_data</em>        [in]      inference data of needed parameters for performing inference including image buffer size, model id.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_image_inference_receive**
> 

```c
int kp_generic_image_inference_receive(
	kp_device_group_t devices
	kp_generic_image_inference_result_header_t *output_desc
	uint8_t *raw_out_buffer
	uint32_t buf_size
)
```
**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>output_desc</em>     [in]      refer to kp_generic_image_inference_result_header_t for describing some information of received data.
<em>raw_out_buffer</em>  [out]     a user-allocated buffer for receiving the RAW data results, the needed buffer size can be known from the 'max_raw_out_size' in 'model_desc' through kp_load_model().
<em>buf_size</em>        [in]      size of raw_out_buffer.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_image_inference_send**
> Generic raw inference with multiple input images send.

```c
int kp_generic_image_inference_send(
	kp_device_group_t devices
	kp_generic_image_inference_desc_t *inf_data
)
```
This is to perform one model inference with multiple input images, it is non-blocking if device buffer queue is not full.
 
When this is performed, user can issue kp_generic_image_inference_receive() to get the result.
 
In addition, to have better performance, users can issue multiple kp_generic_image_inference_send() then start to receive results through kp_generic_image_inference_receive().
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>inf_data</em>        [in]      inference data of needed parameters for performing inference including image buffer size, model id.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_inference_retrieve_fixed_node**
> Retrieve single node output data from raw output buffer.

```c
kp_inf_fixed_node_output_t *kp_generic_inference_retrieve_fixed_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
	kp_channel_ordering_t ordering
)
```
This function retrieves and converts RAW format data to fixed-point data on the per-node basis.
 


**Parameters:**

<pre>
<em>node_idx</em>        [in]      wanted output node index, starts from 0. Number of total output nodes can be known from 'kp_generic_raw_result_header_t'
<em>raw_out_buffer</em>  [in]      the RAW output buffer, it should come from kp_generic_raw_inference_receive().
<em>ordering</em>        [in]      the RAW output channel ordering
</pre>
**Returns:**

refer to kp_inf_fixed_node_output_t. It describes fixed-point values of this node in specific channel ordering.


---
### **kp_generic_inference_retrieve_float_node**
> Retrieve single node output data from raw output buffer.

```c
kp_inf_float_node_output_t *kp_generic_inference_retrieve_float_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
	kp_channel_ordering_t ordering
)
```
This function retrieves and converts RAW format data to floating-point data on the per-node basis.
 


**Parameters:**

<pre>
<em>node_idx</em>        [in]      wanted output node index, starts from 0. Number of total output nodes can be known from 'kp_generic_raw_result_header_t'
<em>raw_out_buffer</em>  [in]      the RAW output buffer, it should come from kp_generic_raw_inference_receive().
<em>ordering</em>        [in]      the RAW output channel ordering
</pre>
**Returns:**

refer to kp_inf_float_node_output_t. It describes floating-point values of this node in specific channel ordering.


---
### **kp_generic_inference_retrieve_raw_fixed_node**
> Retrieve single node output data from raw output buffer.

```c
kp_inf_raw_fixed_node_output_t *kp_generic_inference_retrieve_raw_fixed_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
)
```
This function retrieves RAW format data in fixed-point format on the per-node basis.
 
The return pointer of 'kp_inf_raw_fixed_node_output_t' actually points to raw_out_buffer so do not free raw_out_buffer before completing the use of 'kp_inf_raw_fixed_node_output_t *'
 


**Parameters:**

<pre>
<em>node_idx</em>        [in]      wanted output node index, starts from 0. Number of total output nodes can be known from 'kp_generic_raw_result_header_t'
<em>raw_out_buffer</em>  [in]      the RAW output buffer, it should come from kp_generic_raw_inference_receive().
</pre>
**Returns:**

refer to kp_inf_raw_fixed_node_output_t. It describes fixed-point values of this node with the Kneron device origin raw data buffer and channel ordering (KL520: height x channel x width (aligned to 16 byte), KL720: channel x height x width (aligned to 16 byte)).


---
### **kp_inference_configure**
> Configure inference settings.

```c
int kp_inference_configure(
	kp_device_group_t devices
	kp_inf_configuration_t *conf
)
```
**Parameters:**

<pre>
<em>conf</em>            [in]      refer to kp_inf_configuration_t.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


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
### **kp_release_dbg_checkpoint_data**
> Release the debug checkpoint data

```c
int kp_release_dbg_checkpoint_data(
	void *checkpoint_buf
)
```
**Parameters:**

<pre>
<em>checkpoint_buf</em>            checkpoint buffer to be released
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_release_fixed_node_output**
> Release the single node output data from raw output buffer

```c
void kp_release_fixed_node_output(
	kp_inf_fixed_node_output_t *fixed_node_output
)
```
**Parameters:**

<pre>
<em>fixed_node_output</em>          kp_inf_fixed_node_output_t to be released
</pre>
---
### **kp_release_float_node_output**
> Release the single node output data from raw output buffer

```c
void kp_release_float_node_output(
	kp_inf_float_node_output_t *float_node_output
)
```
**Parameters:**

<pre>
<em>fixed_node_output</em>          kp_inf_float_node_output_t to be released
</pre>
---
### **kp_release_raw_fixed_node_output**
> Release the single node output data from raw output buffer

```c
void kp_release_raw_fixed_node_output(
	kp_inf_raw_fixed_node_output_t *raw_fixed_node_output
)
```
**Parameters:**

<pre>
<em>raw_fixed_node_output</em>          kp_inf_raw_fixed_node_output_t to be released
</pre>
---
