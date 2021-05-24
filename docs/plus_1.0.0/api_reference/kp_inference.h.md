# Kneron PLUS inference APIs


The inference functions provide sophisticated functionaly for differnt applications.
Differnt set of inference APIs would need different models to make it work.
 
 




**Include Header File:**  kp_inference.h

- Functions
    - [kp_customized_inference_receive](#kp_customized_inference_receive)
    - [kp_customized_inference_send](#kp_customized_inference_send)
    - [kp_generic_inference_retrieve_fixed_node](#kp_generic_inference_retrieve_fixed_node)
    - [kp_generic_inference_retrieve_float_node](#kp_generic_inference_retrieve_float_node)
    - [kp_generic_raw_inference_receive](#kp_generic_raw_inference_receive)
    - [kp_generic_raw_inference_send](#kp_generic_raw_inference_send)


---




## Functions
### kp_customized_inference_receive
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
### kp_customized_inference_send
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
### kp_generic_inference_retrieve_fixed_node
> Retrieve single node output data from raw output buffer.

```c
kp_inf_fixed_node_output_t *kp_generic_inference_retrieve_fixed_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
)
```
This function retrieves RAW format data in fixed-point format on the per-node basis.
 
The return pointer of 'kp_inf_fixed_node_output_t' actually points to raw_out_buffer so do not free raw_out_buffer before completing the use of 'kp_inf_fixed_node_output_t *'
 


**Parameters:**

<pre>
<em>node_idx</em>        [in]      wanted output node index, starts from 0. Number of total output nodes can be known from 'kp_generic_raw_result_header_t'
<em>raw_out_buffer</em>  [in]      the RAW output buffer, it should come from kp_generic_raw_inference_receive().
</pre>
**Returns:**

refer to kp_inf_fixed_node_output_t. It describe 'width (aligned to 16 byte) x height x channel' in conjunction with fixed-point values of this node.


---
### kp_generic_inference_retrieve_float_node
> Retrieve single node output data from raw output buffer.

```c
kp_inf_float_node_output_t *kp_generic_inference_retrieve_float_node(
	uint32_t node_idx
	uint8_t *raw_out_buffer
)
```
This function retrieves and converts RAW format data to floating-point data on the per-node basis.
 


**Parameters:**

<pre>
<em>node_idx</em>        [in]      wanted output node index, starts from 0. Number of total output nodes can be known from 'kp_generic_raw_result_header_t'
<em>raw_out_buffer</em>  [in]      the RAW output buffer, it should come from kp_generic_raw_inference_receive().
</pre>
**Returns:**

refer to kp_inf_float_node_output_t. It describe 'width x height x channel' in conjunction with floating-point values of this node.


---
### kp_generic_raw_inference_receive
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
<em>raw_buf_size</em>    [in]      size of raw_out_buffer.
</pre>
**Returns:**

refer to KP_API_RETURN_CODE in kp_struct.h


---
### kp_generic_raw_inference_send
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

refer to KP_API_RETURN_CODE in kp_struct.h


---
