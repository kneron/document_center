# kp.inference

<!-- !! processed by numpydoc !! -->

---
 
### kp.inference.generic_data_inference_receive(device_group)
Generic raw data inference multiple input receive.
When multiple input data inference is done, this function can be used to get the results in RAW format.
Note that data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.



* **Returns**

    * **generic_data_inference_result** : [`kp.GenericDataInferenceResult`](value.md#kp.GenericDataInferenceResult)

            GenericDataInferenceResult object contained the received RAW data results.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericDataInferenceResult`](value.md#kp.GenericDataInferenceResult)



---
 
### kp.inference.generic_data_inference_send(device_group, generic_inference_input_descriptor)
Generic raw data inference multiple input send.
This is to perform a multiple input data inference, it is non-blocking if device buffer queue is not full.
When this is performed, user can issue
kp.inference.generic_data_inference_receive() to get the result.
In addition, to have better performance, users can issue multiple
kp.inference.generic_data_inference_send() then start to receive results through
kp.inference.generic_data_inference_receive().


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_inference_input_descriptor** : [`kp.GenericDataInferenceDescriptor`](value.md#kp.GenericDataInferenceDescriptor)

            Needed parameters for performing multiple data inference including image buffers, image buffers size, model ID … etc.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.inference.generic_image_inference_receive(device_group)
Generic image inference multiple input receive.
When multiple input image inference is done, this function can be used to get the results in RAW format.
Note that the data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.



* **Returns**

    * **generic_image_inference_result** : [`kp.GenericImageInferenceResult`](value.md#kp.GenericImageInferenceResult)

            GenericImageInferenceResult object contained the received RAW data results.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericImageInferenceResult`](value.md#kp.GenericImageInferenceResult)



---
 
### kp.inference.generic_image_inference_send(device_group, generic_inference_input_descriptor)
Generic image inference multiple input send.
This is to perform multiple input image inference, it is non-blocking if device buffer queue is not full.
When this is performed, user can issue kp.inference.generic_image_inference_receive() to get the
result. In addition, to have better performance, users can issue multiple
kp.inference.generic_image_inference_send() then start to receive results through
kp.inference.generic_image_inference_receive().


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_inference_input_descriptor** : [`kp.GenericImageInferenceDescriptor`](value.md#kp.GenericImageInferenceDescriptor)

            Needed parameters for performing image inference including model ID, images width, height ..etc.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.inference.generic_inference_retrieve_fixed_node(node_idx, generic_raw_result, channels_ordering)
Retrieve single node output fixed-point data from GenericRawResult/GenericRawBypassPreProcResult/GenericImageInferenceResult/GenericDataInferenceResult object.


* **Parameters**

    * **node_idx** : [`int`](https://docs.python.org/3/library/functions.html#int)

            Wanted output node index, starts from 0. Number of total output nodes can be known
            from ‘GenericRawResult.header.num_output_node’

    * **generic_raw_result** : [`kp.v1.GenericRawResult`](v1/value.md#kp.v1.GenericRawResult), [`kp.v1.GenericRawBypassPreProcResult`](v1/value.md#kp.v1.GenericRawBypassPreProcResult), [`kp.GenericImageInferenceResult`](value.md#kp.GenericImageInferenceResult), [`kp.GenericDataInferenceResult`](value.md#kp.GenericDataInferenceResult)

            GenericRawResult/GenericRawBypassPreProcResult/GenericImageInferenceResult/GenericDataInferenceResult object contained the received RAW data results, it should
            come from ‘kp.v1.inference.generic_raw_inference_receive()’/’kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive()’/’kp.inference.generic_image_inference_receive()’/’kp.inference.generic_data_inference_receive()’

    * **channels_ordering** : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering)

            The raw output feature map channel ordering.



* **Returns**

    * **inference_fixed_node_output** : [`kp.InferenceFixedNodeOutput`](value.md#kp.InferenceFixedNodeOutput)

            Raw node output in fixed-point format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`InferenceFixedNodeOutput`](value.md#kp.InferenceFixedNodeOutput)



---
 
### kp.inference.generic_inference_retrieve_float_node(node_idx, generic_raw_result, channels_ordering)
Retrieve single node output floating-point data from GenericRawResult/GenericRawBypassPreProcResult/GenericImageInferenceResult/GenericDataInferenceResult object.


* **Parameters**

    * **node_idx** : [`int`](https://docs.python.org/3/library/functions.html#int)

            Wanted output node index, starts from 0. Number of total output nodes can be known
            from ‘GenericRawResult.header.num_output_node’

    * **generic_raw_result** : [`kp.v1.GenericRawResult`](v1/value.md#kp.v1.GenericRawResult), [`kp.v1.GenericRawBypassPreProcResult`](v1/value.md#kp.v1.GenericRawBypassPreProcResult), [`kp.GenericImageInferenceResult`](value.md#kp.GenericImageInferenceResult), [`kp.GenericDataInferenceResult`](value.md#kp.GenericDataInferenceResult)

            GenericRawResult/GenericRawBypassPreProcResult/GenericImageInferenceResult/GenericDataInferenceResult object contained the received RAW data results, it should
            come from ‘kp.v1.inference.generic_raw_inference_receive()’/’kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive()’/’kp.inference.generic_image_inference_receive()’/’kp.inference.generic_data_inference_receive()’

    * **channels_ordering** : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering)

            The raw output feature map channel ordering.



* **Returns**

    * **inference_float_node_output** : [`kp.InferenceFloatNodeOutput`](value.md#kp.InferenceFloatNodeOutput)

            Raw node output in floating-point format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`InferenceFloatNodeOutput`](value.md#kp.InferenceFloatNodeOutput)



---
 
### kp.inference.profile_get_statistics(device_group)
Collect inference profile results.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
Please using following steps to profile the model inference performance:
1. Enable feature by kp.inference.profile_set_enable()
2. Run inference
3. Collect the statistic result by kp.inference.profile_get_statistics()
4. Disable feature by kp.inference.profile_set_enable()

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ProfileData`](value.md#kp.ProfileData)



---
 
### kp.inference.profile_set_enable(device_group, enable)
To set enable/disable model profile.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **enable** : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)

            Set enable/disable.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
Please using following steps to profile the model inference performance:
1. Enable feature by kp.inference.profile_set_enable()
2. Run inference
3. Collect the statistic result by kp.inference.profile_get_statistics()
4. Disable feature by kp.inference.profile_set_enable()

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.inference.set_inference_configuration(device_group, inference_configuration)
Configure inference settings.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **inference_configuration** : [`kp.InferenceConfiguration`](value.md#kp.InferenceConfiguration)

            Inference configurations.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)
