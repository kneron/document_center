# Legacy Kneron PLUS inference APIs


**(To be deprecated in future release)**
The inference functions provide sophisticated functionally for different applications.
Different set of inference APIs would need different models to make it work.
 
 




**Include Header File:**  kp_inference_v1.h

- Functions
    - [kp_generic_raw_inference_bypass_pre_proc_receive](#kp_generic_raw_inference_bypass_pre_proc_receive)
    - [kp_generic_raw_inference_bypass_pre_proc_send](#kp_generic_raw_inference_bypass_pre_proc_send)
    - [kp_generic_raw_inference_receive](#kp_generic_raw_inference_receive)
    - [kp_generic_raw_inference_send](#kp_generic_raw_inference_send)


---




## **Functions**
### **kp_generic_raw_inference_bypass_pre_proc_receive**
> Generic raw inference bypass pre-processing receive.

```c
int kp_generic_raw_inference_bypass_pre_proc_receive(
	kp_device_group_t devices
	kp_generic_raw_bypass_pre_proc_result_header_t *output_desc
	uint8_t *raw_out_buffer
	uint32_t buf_size
)
```
When a image inference is done, this function can be used to get the results in RAW format.
 
Note that the data received is in Kneron RAW format, users need kp_generic_inference_retrieve_float_node() to convert RAW format data to floating-point data.
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>output_desc</em>     [in]      refer to kp_generic_raw_bypass_pre_proc_result_header_t for describing some information of received data.
<em>raw_out_buffer</em>  [out]     a user-allocated buffer for receiving the RAW data results, the needed buffer size can be known from the 'max_raw_out_size' in 'model_desc' through kp_load_model().
<em>buf_size</em>        [in]      size of raw_out_buffer.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_raw_inference_bypass_pre_proc_send**
> Generic raw inference bypass pre-processing send.

```c
int kp_generic_raw_inference_bypass_pre_proc_send(
	kp_device_group_t devices
	kp_generic_raw_bypass_pre_proc_image_header_t *inf_desc
	uint8_t *image_buffer
)
```
This is to perform a single image inference, it is non-blocking if device buffer queue is not full.
 
When this is performed, user can issue kp_generic_raw_inference_bypass_pre_proc_receive() to get the result.
 
In addition, to have better performance, users can issue multiple kp_generic_raw_inference_bypass_pre_proc_receive() then start to receive results through kp_generic_raw_inference_receive().
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>inf_desc</em>        [in]      needed parameters for performing inference including image buffer size, model id.
<em>image_buffer</em>    [in]      the buffer contains the image.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_raw_inference_receive**
> Generic raw inference receive.

```c
int kp_generic_raw_inference_receive(
	kp_device_group_t devices
	kp_generic_raw_result_header_t *output_desc
	uint8_t *raw_out_buffer
	uint32_t buf_size
)
```
When a image inference is done, this function can be used to get the results in RAW format.
 
Note that the data received is in Kneron RAW format, users need kp_generic_inference_retrieve_float_node() to convert RAW format data to floating-point data.
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>output_desc</em>     [in]      refer to kp_generic_raw_result_header_t for describing some information of received data.
<em>raw_out_buffer</em>  [out]     a user-allocated buffer for receiving the RAW data results, the needed buffer size can be known from the 'max_raw_out_size' in 'model_desc' through kp_load_model().
<em>buf_size</em>        [in]      size of raw_out_buffer.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
### **kp_generic_raw_inference_send**
> Generic raw inference send.

```c
int kp_generic_raw_inference_send(
	kp_device_group_t devices
	kp_generic_raw_image_header_t *inf_desc
	uint8_t *image_buffer
)
```
This is to perform a single image inference, it is non-blocking if device buffer queue is not full.
 
When this is performed, user can issue kp_generic_raw_inference_receive() to get the result.
 
In addition, to have better performance, users can issue multiple kp_generic_raw_inference_send() then start to receive results through kp_generic_raw_inference_receive().
 


**Parameters:**

<pre>
<em>devices</em>         [in]      a set of devices handle.
<em>inf_desc</em>        [in]      needed parameters for performing inference including image width, height ..etc.
<em>image_buffer</em>    [in]      the buffer contains the image.
</pre>
**Returns:**

int refer to KP_API_RETURN_CODE in kp_struct.h


---
