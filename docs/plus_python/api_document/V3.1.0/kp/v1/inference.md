# kp.v1.inference (Legacy Module)

<!-- !! processed by numpydoc !! -->

---
 
### kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive(device_group, generic_raw_image_header, model_nef_descriptor)
Generic raw inference bypass pre-processing receive.
When an image inference is done, this function can be used to get the results in RAW format.
Note that data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](../value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_raw_image_header** : [`kp.v1.GenericRawBypassPreProcImageHeader`](value.md#kp.v1.GenericRawBypassPreProcImageHeader)

            Needed parameters for performing bypass pre-processing inference including image buffer size, model ID … etc.

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](../value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Returns**

    * **generic_raw_result** : [`kp.v1.GenericRawBypassPreProcResult`](value.md#kp.v1.GenericRawBypassPreProcResult)

            GenericRawBypassPreProcResult object contained the received RAW data results.



* **Raises**

    * [`kp.ApiKPException`](../exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawBypassPreProcResult`](value.md#kp.v1.GenericRawBypassPreProcResult)



---
 
### kp.v1.inference.generic_raw_inference_bypass_pre_proc_send(device_group, generic_raw_image_header, image_buffer)
Generic raw inference bypass pre-processing send.
This is to perform a single image inference, it is non-blocking if device buffer queue is not full. When this
is performed, user can issue kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive() to get the result.
In addition, to have better performance, users can issue multiple
kp.v1.inference.generic_raw_inference_bypass_pre_proc_send() then start to receive results through
kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive().


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](../value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_raw_image_header** : [`kp.v1.GenericRawBypassPreProcImageHeader`](value.md#kp.v1.GenericRawBypassPreProcImageHeader)

            Needed parameters for performing bypass pre-processing inference including image buffer size, model ID ..etc.

    * **image_buffer** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)

            The data bytes contains the image.



* **Raises**

    * [`kp.ApiKPException`](../exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.v1.inference.generic_raw_inference_receive(device_group, generic_raw_image_header, model_nef_descriptor)
Generic raw inference receive.
When an image inference is done, this function can be used to get the results in RAW format.
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](../value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_raw_image_header** : [`kp.v1.GenericRawImageHeader`](value.md#kp.v1.GenericRawImageHeader)

            Needed parameters for performing inference including image width, height ..etc.

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](../value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Returns**

    * **generic_raw_result** : [`kp.v1.GenericRawResult`](value.md#kp.v1.GenericRawResult)

            GenericRawResult object contained the received RAW data results.



* **Raises**

    * [`kp.ApiKPException`](../exception.md#kp.ApiKPException)


* **Notes**  
The data received is in Kneron RAW format, users need
kp.inference.generic_inference_retrieve_float_node()/kp.inference.generic_inference_retrieve_fixed_node() to
convert RAW format data to floating-point/fixed-point data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawResult`](value.md#kp.v1.GenericRawResult)



---
 
### kp.v1.inference.generic_raw_inference_send(device_group, generic_raw_image_header, image, image_format)
Generic raw inference send.
This is to perform a single image inference, it is non-blocking if device buffer queue is not full.
When this is performed, user can issue kp.v1.inference.generic_raw_inference_receive() to get the result.
In addition, to have better performance, users can issue multiple kp.v1.inference.generic_raw_inference_send() then
start to receive results through kp.v1.inference.generic_raw_inference_receive().


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](../value.md#kp.DeviceGroup)

            Represents a set of devices handle.

    * **generic_raw_image_header** : [`kp.v1.GenericRawImageHeader`](value.md#kp.v1.GenericRawImageHeader)

            Needed parameters for performing inference including image width, height ..etc.

    * **image** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)

            The data bytes or numpy.ndarray contains the image.

    * **image_format** : [`kp.ImageFormat`](../enum.md#kp.ImageFormat)

            Image format supported for inference.



* **Raises**

    * [`kp.ApiKPException`](../exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)
