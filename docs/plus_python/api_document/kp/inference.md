# kp.inference

<!-- !! processed by numpydoc !! -->

---
 
### kp.inference.generic_inference_retrieve_fixed_node(node_idx, generic_raw_result, channels_ordering)
Retrieve single node output fixed-point data from GenericRawResult/GenericRawBypassPreProcResult object.


* **Parameters**

    **node_idx** : [`int`](https://docs.python.org/3/library/functions.html#int)

        Wanted output node index, starts from 0. Number of total output nodes can be known
        from ‘GenericRawResult.header.num_output_node’

    **generic_raw_result** : [`kp.GenericRawResult`](value.md#kp.GenericRawResult), [`kp.GenericRawBypassPreProcResult`](value.md#kp.GenericRawBypassPreProcResult)

        GenericRawResult/GenericRawBypassPreProcResult object contained the received RAW data results, it should
        come from ‘kp.inference.generic_raw_inference_receive()’/’kp.inference.generic_raw_inference_bypass_pre_proc_receive()’

    **channels_ordering** : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering)

        The raw output feature map channel ordering.



* **Returns**

    **inference_fixed_node_output** : [`kp.InferenceFixedNodeOutput`](value.md#kp.InferenceFixedNodeOutput)

        Raw node output in fixed-point format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`InferenceFixedNodeOutput`](value.md#kp.InferenceFixedNodeOutput)



---
 
### kp.inference.generic_inference_retrieve_float_node(node_idx, generic_raw_result, channels_ordering)
Retrieve single node output floating-point data from GenericRawResult/GenericRawBypassPreProcResult object.


* **Parameters**

    **node_idx** : [`int`](https://docs.python.org/3/library/functions.html#int)

        Wanted output node index, starts from 0. Number of total output nodes can be known
        from ‘GenericRawResult.header.num_output_node’

    **generic_raw_result** : [`kp.GenericRawResult`](value.md#kp.GenericRawResult), [`kp.GenericRawBypassPreProcResult`](value.md#kp.GenericRawBypassPreProcResult)

        GenericRawResult/GenericRawBypassPreProcResult object contained the received RAW data results, it should
        come from ‘kp.inference.generic_raw_inference_receive()’/’kp.inference.generic_raw_inference_bypass_pre_proc_receive()’

    **channels_ordering** : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering)

        The raw output feature map channel ordering.



* **Returns**

    **inference_float_node_output** : [`kp.InferenceFloatNodeOutput`](value.md#kp.InferenceFloatNodeOutput)

        Raw node output in floating-point format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`InferenceFloatNodeOutput`](value.md#kp.InferenceFloatNodeOutput)



---
 
### kp.inference.generic_raw_inference_bypass_pre_proc_receive(device_group, generic_raw_image_header, model_nef_descriptor)
Generic raw inference bypass pre-processing receive.
When an image inference is done, this function can be used to get the results in RAW format.
Note that data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.


* **Parameters**

    **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

        Represents a set of devices handle.

    **generic_raw_image_header** : [`kp.GenericRawBypassPreProcImageHeader`](value.md#kp.GenericRawBypassPreProcImageHeader)

        Needed parameters for performing bypass pre-processing inference including image buffer size, model ID ..etc.

    **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

        ModelNefDescriptor object for describing the uploaded models.



* **Returns**

    **generic_raw_result** : [`kp.GenericRawBypassPreProcResult`](value.md#kp.GenericRawBypassPreProcResult)

        GenericRawBypassPreProcResult object contained the received RAW data results.



* **Raises**

    [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawBypassPreProcResult`](value.md#kp.GenericRawBypassPreProcResult)



---
 
### kp.inference.generic_raw_inference_bypass_pre_proc_send(device_group, generic_raw_image_header, image_buffer)
Generic raw inference bypass pre-processing send.
This is to perform a single image inference, it is non-blocking if device buffer queue is not full. When this
is performed, user can issue kp.inference.generic_raw_inference_bypass_pre_proc_receive() to get the result.
In addition, to have better performance, users can issue multiple
kp.inference.generic_raw_inference_bypass_pre_proc_send() then start to receive results through
kp.inference.generic_raw_inference_bypass_pre_proc_receive().


* **Parameters**

    **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

        Represents a set of devices handle.

    **generic_raw_image_header** : [`kp.GenericRawBypassPreProcImageHeader`](value.md#kp.GenericRawBypassPreProcImageHeader)

        Needed parameters for performing bypass pre-processing inference including image buffer size, model ID ..etc.

    **image_buffer** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)

        The data bytes contains the image.



* **Raises**

    [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.inference.generic_raw_inference_receive(device_group, generic_raw_image_header, model_nef_descriptor)
Generic raw inference receive.
When an image inference is done, this function can be used to get the results in RAW format.
Note that the data received is in Kneron RAW format, users need kp.inference.generic_inference_retrieve_float_node() to convert RAW format data to floating-point data.


* **Parameters**

    **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

        Represents a set of devices handle.

    **generic_raw_image_header** : [`kp.GenericRawImageHeader`](value.md#kp.GenericRawImageHeader)

        Needed parameters for performing inference including image width, height ..etc.

    **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

        ModelNefDescriptor object for describing the uploaded models.



* **Returns**

    **generic_raw_result** : [`kp.GenericRawResult`](value.md#kp.GenericRawResult)

        GenericRawResult object contained the received RAW data results.



* **Raises**

    [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node() to convert RAW format data to floating-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawResult`](value.md#kp.GenericRawResult)



---
 
### kp.inference.generic_raw_inference_send(device_group, generic_raw_image_header, image, image_format)
Generic raw inference send.
This is to perform a single image inference, it is non-blocking if device buffer queue is not full.
When this is performed, user can issue kp.inference.generic_raw_inference_receive() to get the result.
In addition, to have better performance, users can issue multiple kp.inference.generic_raw_inference_send() then
start to receive results through kp.inference.generic_raw_inference_receive().


* **Parameters**

    **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

        Represents a set of devices handle.

    **generic_raw_image_header** : [`kp.GenericRawImageHeader`](value.md#kp.GenericRawImageHeader)

        Needed parameters for performing inference including image width, height ..etc.

    **image** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), `numpy.ndarray`

        The data bytes or numpy.ndarray contains the image.

    **image_format** : [`kp.ImageFormat`](enum.md#kp.ImageFormat)

        Image format supported for inference.



* **Raises**

    [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.inference.set_inference_configuration(device_group, inference_configuration)
Configure inference settings.


* **Parameters**

    **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

        Represents a set of devices handle.

    **inference_configuration** : [`kp.InferenceConfiguration`](value.md#kp.InferenceConfiguration)

        Inference configurations.



* **Raises**

    [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)
