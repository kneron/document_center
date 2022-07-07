# kp.v1 value (Legacy Module)

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.v1.GenericRawBypassPreProcImageHeader(model_id=0, inference_number=0, image_buffer_size=0)
Inference descriptor for images bypass pre-processing.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `image_buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference image buffer size.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** image_buffer_size(: int)
int: Inference image buffer size.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** inference_number(: int)
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_id(: int)
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.v1.GenericRawBypassPreProcResult(buffer_size)
Generic inference raw result for bypass pre-processing.


* **Attributes**

    * `header` : `kp.GenericRawBypassPreProcResultHeader`

            kp.GenericRawBypassPreProcResultHeader: Inference raw output descriptor for bypass pre-processing.

    * `raw_result` : [`kp.GenericRawResultNDArray`](../value.md#kp.GenericRawResultNDArray)

            kp.GenericRawResultNDArray: Inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** header(: kp.Legacy.V1.KPValue.GenericRawBypassPreProcResultHeader)
kp.GenericRawBypassPreProcResultHeader: Inference raw output descriptor for bypass pre-processing.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawBypassPreProcResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawResultNDArray`](../value.md#kp.GenericRawResultNDArray)



---
 
### **class** kp.v1.GenericRawBypassPreProcResultHeader(inference_number=0, crop_number=0, num_output_node=0, product_id=0)
Inference raw output descriptor for bypass pre-processing.


* **Attributes**

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `crop_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Crop box sequence number.

    * `num_output_node` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of output nodes.

    * `product_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: USB PID (Product ID).


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_number(: int)
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** inference_number(: int)
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** num_output_node(: int)
int: Total number of output nodes.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** product_id(: int)
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.v1.GenericRawImageHeader(model_id=0, resize_mode=ResizeMode.KP_RESIZE_ENABLE, padding_mode=PaddingMode.KP_PADDING_CORNER, normalize_mode=NormalizeMode.KP_NORMALIZE_KNERON, inference_number=0, inference_crop_box_list=[], width=0, height=0, image_format=ImageFormat.KP_IMAGE_FORMAT_RGB565)
Inference descriptor for images.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `resize_mode` : [`kp.ResizeMode`](../enum.md#kp.ResizeMode), default=kp.ResizeMode.KP_RESIZE_ENABLE

            kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

    * `padding_mode` : [`kp.PaddingMode`](../enum.md#kp.PaddingMode), default=kp.PaddingMode.KP_PADDING_CORNER

            kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

    * `normalize_mode` : [`kp.NormalizeMode`](../enum.md#kp.NormalizeMode), default=kp.NormalizeMode.KP_NORMALIZE_KNERON

            kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `inference_crop_box_list` : `List`[[`kp.InferenceCropBox`](../value.md#kp.InferenceCropBox)], default=[]

            List[kp.InferenceCropBox]: Box information to crop.

    * `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference image width.

    * `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference image height.

    * `image_format` : [`kp.ImageFormat`](../enum.md#kp.ImageFormat), default=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565

            kp.ImageFormat: Inference image format, refer to ImageFormat.


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_count(: int)
int: Number of crop box.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** height(: int)
int: Inference image height.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** image_format(: kp.KPEnum.ImageFormat)
kp.ImageFormat: Inference image format, refer to ImageFormat.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ImageFormat`](../enum.md#kp.ImageFormat)



#### **_property_** inference_crop_box_list(: List[kp.KPValue.InferenceCropBox])
List[kp.InferenceCropBox]: Box information to crop.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`InferenceCropBox`](../value.md#kp.InferenceCropBox)]



#### **_property_** inference_number(: int)
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_id(: int)
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** normalize_mode(: kp.KPEnum.NormalizeMode)
kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`NormalizeMode`](../enum.md#kp.NormalizeMode)



#### **_property_** padding_mode(: kp.KPEnum.PaddingMode)
kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`PaddingMode`](../enum.md#kp.PaddingMode)



#### **_property_** resize_mode(: kp.KPEnum.ResizeMode)
kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ResizeMode`](../enum.md#kp.ResizeMode)



#### **_property_** width(: int)
int: Inference image width.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.v1.GenericRawResult(buffer_size)
Generic inference raw result.


* **Attributes**

    * `header` : `kp.GenericRawResultHeader`

            kp.GenericRawResultHeader: Inference raw output descriptor.

    * `raw_result` : [`kp.GenericRawResultNDArray`](../value.md#kp.GenericRawResultNDArray)

            kp.GenericRawResultNDArray: Inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** header(: kp.Legacy.V1.KPValue.GenericRawResultHeader)
kp.GenericRawResultHeader: Inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`GenericRawResultNDArray`](../value.md#kp.GenericRawResultNDArray)



---
 
### **class** kp.v1.GenericRawResultHeader(inference_number=0, crop_number=0, num_output_node=0, product_id=0, hw_pre_proc_info={'img_width': 0, 'img_height': 0, 'resized_img_width': 0, 'resized_img_heig ...)
Inference raw output descriptor.


* **Attributes**

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `crop_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Crop box sequence number.

    * `num_output_node` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of output nodes.

    * `product_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: USB PID (Product ID).

    * `hw_pre_proc_info` : [`kp.HwPreProcInfo`](../value.md#kp.HwPreProcInfo), default=kp.HwPreProcInfo()

            kp.HwPreProcInfo: Hardware preprocess info


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_number(: int)
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** hw_pre_proc_info(: kp.KPValue.HwPreProcInfo)
kp.HwPreProcInfo: Hardware preprocess info

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`HwPreProcInfo`](../value.md#kp.HwPreProcInfo)



#### **_property_** inference_number(: int)
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** num_output_node(: int)
int: Total number of output nodes.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** product_id(: int)
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)
