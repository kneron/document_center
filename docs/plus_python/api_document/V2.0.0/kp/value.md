# kp value

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.DdrManageAttributes(model_size=0, input_buffer_size=0, input_buffer_count=0, result_buffer_size=0, result_buffer_count=0)
DDR memory management descriptor of Kneron device.


* **Attributes**

    * `model_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: DDR space for model.

    * `input_buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Input buffer size for FIFO queue.

    * `input_buffer_count` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Input buffer count for FIFO queue.

    * `result_buffer_size` : `kp.ModelNefDescriptor`, default=kp.ModelNefDescriptor()

            int: Result buffer size for FIFO queue.

    * `result_buffer_count` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Result buffer count for FIFO queue.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** input_buffer_count(: int)
int: Input buffer count for FIFO queue.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** input_buffer_size(: int)
int: Input buffer size for FIFO queue.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_size(: int)
int: DDR space for model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** result_buffer_count(: int)
int: Result buffer count for FIFO queue.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** result_buffer_size(: int)
int: Result buffer size for FIFO queue.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.DeviceDescriptor(usb_port_id=0, vendor_id=0, product_id=0, link_speed=UsbSpeed.KP_USB_SPEED_UNKNOWN, kn_number=0, is_connectable=False, usb_port_path='', firmware='')
Information of one connected device from USB perspectives.


* **Attributes**

    * `usb_port_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: An unique ID representing for a Kneron device, can be used as input while connecting devices.

    * `vendor_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Supposed to be 0x3231.

    * `product_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: USB PID (Product ID).

    * `link_speed` : [`UsbSpeed`](enum.md#kp.UsbSpeed), default=UsbSpeed.KP_USB_SPEED_UNKNOWN

            UsbSpeed: Enum for USB speed mode.

    * `kn_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: KN number.

    * `is_connectable` : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values), default=False

            bool: Indicate if this device is connectable.

    * `usb_port_path` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: “busNo-hub_portNo-device_portNo” (ex: “1-2-3”, means bus 1 - (hub) port 2 - (device) port 3)

    * `firmware` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Firmware description.


<!-- !! processed by numpydoc !! -->

#### **_property_** firmware(: str)
str: Firmware description.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** is_connectable(: bool)
bool: Indicate if this device is connectable.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`bool`](https://docs.python.org/3/library/functions.html#bool)



#### **_property_** kn_number(: int)
int: KN number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** link_speed(: kp.KPEnum.UsbSpeed)
UsbSpeed: Enum for USB speed mode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`UsbSpeed`](enum.md#kp.UsbSpeed)



#### **_property_** product_id(: int)
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** usb_port_id(: int)
int: An unique ID representing for a Kneron device, can be used as input while connecting devices.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** usb_port_path(: str)
str: “busNo-hub_portNo-device_portNo” (ex: “1-2-3”, means bus 1 - (hub) port 2 - (device) port 3)

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### **_property_** vendor_id(: int)
int: Supposed to be 0x3231.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.DeviceDescriptorList(device_descriptor_list=[])
Information of connected devices from USB perspectives.


* **Attributes**

    * `device_descriptor_list` : `List`[`kp.DeviceDescriptor`], default=[]

            List[kp.DeviceDescriptor]: DeviceDescriptor objects list, contain information of connected devices from USB perspectives.


<!-- !! processed by numpydoc !! -->

#### **_property_** device_descriptor_list(: List[kp.KPValue.DeviceDescriptor])
List[kp.DeviceDescriptor]: DeviceDescriptor objects list, contain information of connected devices from USB
perspectives.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`DeviceDescriptor`]



#### **_property_** device_descriptor_number(: int)
int: Number of connected devices.

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



---
 
### **class** kp.DeviceGroup(address)
A handle represent connected Kneron device.


* **Attributes**

    * `address` : [`int`](https://docs.python.org/3/library/functions.html#int)

            int: Memory address of connected Kneron device handler.


<!-- !! processed by numpydoc !! -->

#### **_property_** address(: int)
int: Memory address of connected Kneron device handler.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** content(: kp.KPValue.DeviceGroupContent)
DeviceGroupContent: A DeviceGroup descriptor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `DeviceGroupContent`



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.FirmwareVersion(reserved=0, major=0, minor=0, update=0, build=0)
Information of firmware version.


* **Attributes**

    * `reserved` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Reserved version number for backward compatibility.

    * **major** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    * **minor** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    * **update** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    * **build** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** reserved(: int)
int: Reserved version number for backward compatibility.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.GenericDataInferenceDescriptor(inference_number=0, model_id=0, input_node_data_list=[])
Multiple input inference descriptor for bypass pre-processing inference.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `input_node_data_list` : `List`[`GenericInputNodeData`], default=[]

            List[GenericInputNodeData]: Multiple input inference data descriptors (The data order must be mapping model input tensor order as shown in ModelNefDescriptor).


<!-- !! processed by numpydoc !! -->

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



#### **_property_** input_node_data_list(: List[kp.KPValue.GenericInputNodeData])
List[GenericInputNodeData]: Multiple input inference data descriptors (The data order must be mapping model input tensor order as shown in ModelNefDescriptor).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`GenericInputNodeData`]



#### **_property_** input_node_data_num(: int)
int: Number of multiple input inference data descriptors in input_node_data_list.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_id(: int)
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.GenericDataInferenceResult(buffer_size)
Multiple input bypass pre-processing inference raw result.


* **Attributes**

    * `header` : `kp.GenericDataInferenceResultHeader`

            kp.GenericDataInferenceResultHeader: Multiple input bypass pre-processing inference raw output descriptor.

    * `raw_result` : `kp.GenericRawResultNDArray`

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



#### **_property_** header(: kp.KPValue.GenericDataInferenceResultHeader)
kp.GenericDataInferenceResultHeader: Multiple input bypass pre-processing inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericDataInferenceResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultNDArray`



---
 
### **class** kp.GenericDataInferenceResultHeader(inference_number=0, crop_number=0, num_output_node=0, product_id=0)
Multiple input bypass pre-processing inference raw output descriptor.


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
 
### **class** kp.GenericImageInferenceDescriptor(inference_number=0, model_id=0, input_node_image_list=[])
Multiple input inference descriptor for images.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `input_node_image_list` : `List`[`GenericInputNodeImage`], default=[]

            List[kp.GenericInputNodeImage]: Multiple input inference image data descriptors (Max number of input image is 5) (The image data order must be mapping model input tensor order as shown in ModelNefDescriptor).


<!-- !! processed by numpydoc !! -->

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



#### **_property_** input_node_image_list(: List[kp.KPValue.GenericInputNodeImage])
List[kp.GenericInputNodeImage]: Multiple input inference image data descriptors (Max number of input image is 5) (The image data order must be mapping model input tensor order as shown in ModelNefDescriptor).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`GenericInputNodeImage`]



#### **_property_** input_node_image_num(: int)
int: Number of multiple input inference image data descriptors in input_node_image_list.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_id(: int)
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.GenericImageInferenceResult(buffer_size)
Generic multiple input inference raw result.


* **Attributes**

    * `header` : `kp.GenericImageInferenceResultHeader`

            kp.GenericImageInferenceResultHeader: Multiple input image inference raw output descriptor.

    * `raw_result` : `kp.GenericRawResultNDArray`

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



#### **_property_** header(: kp.KPValue.GenericImageInferenceResultHeader)
kp.GenericImageInferenceResultHeader: Multiple input image inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericImageInferenceResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultNDArray`



---
 
### **class** kp.GenericImageInferenceResultHeader(inference_number=0, crop_number=0, num_output_node=0, product_id=0, hw_pre_proc_info_list=[])
Multiple input image inference raw output descriptor.


* **Attributes**

    * `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference sequence number.

    * `crop_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Crop box sequence number.

    * `num_output_node` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of output nodes.

    * `product_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: USB PID (Product ID).

    * `hw_pre_proc_info_list` : `List`[`kp.HwPreProcInfo`], default=[]

            List[kp.HwPreProcInfo]: Hardware pre-process information for each input node.


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



#### **_property_** hw_pre_proc_info_list(: List[kp.KPValue.HwPreProcInfo])
List[kp.HwPreProcInfo]: Hardware pre-process information for each input node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`HwPreProcInfo`]



#### **_property_** inference_number(: int)
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** num_hw_pre_proc_info(: int)
int: Number of hardware pre-process information.

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
 
### **class** kp.GenericInputNodeData(buffer=b'')
Single data descriptor for bypass pre-processing inference.


* **Attributes**

    * `buffer` : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), default=bytes()

            bytes: The data bytes contains the inference data.


<!-- !! processed by numpydoc !! -->

#### **_property_** buffer(: bytes)
bytes: The data bytes contains the inference data.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)



#### **_property_** buffer_size(: int)
int: Inference data buffer size.

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



---
 
### **class** kp.GenericInputNodeImage(image=array([], shape=(0, 0, 2), dtype=uint8), width=0, height=0, image_format=ImageFormat.KP_IMAGE_FORMAT_RGB565, resize_mode=ResizeMode.KP_RESIZE_ENABLE, padding_mode=PaddingMode.KP_PADDING_CORNER, normalize_mode=NormalizeMode.KP_NORMALIZE_KNERON, inference_crop_box_list=[])
Single inference image data descriptor.


* **Attributes**

    * `image` : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), default=numpy.ndarray([0, 0, `kp.Const.CHANNEL_NUM_OTHER_FORMAT.value`], dtype=np.uint8)

            numpy.ndarray: The data bytes or numpy.ndarray (dtype=numpy.uint8, dim=3) contains the image.

    * `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference image width (Must apply when using bytes image data).

    * `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Inference image height (Must apply when using bytes image data).

    * `image_format` : [`kp.ImageFormat`](enum.md#kp.ImageFormat), default=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565

            kp.ImageFormat: Inference image format, refer to ImageFormat.

    * `resize_mode` : [`kp.ResizeMode`](enum.md#kp.ResizeMode), default=kp.ResizeMode.KP_RESIZE_ENABLE

            kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

    * `padding_mode` : [`kp.PaddingMode`](enum.md#kp.PaddingMode), default=kp.PaddingMode.KP_PADDING_CORNER

            kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

    * `normalize_mode` : [`kp.NormalizeMode`](enum.md#kp.NormalizeMode), default=kp.NormalizeMode.KP_NORMALIZE_KNERON

            kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

    * `inference_crop_box_list` : `List`[`kp.InferenceCropBox`], default=[]

            List[kp.InferenceCropBox]: Box information to crop.


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
int: Inference image height (Must apply when using bytes image data).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** image(: numpy.ndarray)
numpy.ndarray: The data bytes or numpy.ndarray (dtype=numpy.uint8, dim=3) contains the image.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)



#### **_property_** image_format(: kp.KPEnum.ImageFormat)
kp.ImageFormat: Inference image format, refer to ImageFormat.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ImageFormat`](enum.md#kp.ImageFormat)



#### **_property_** inference_crop_box_list(: List[kp.KPValue.InferenceCropBox])
List[kp.InferenceCropBox]: Box information to crop.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`InferenceCropBox`]



#### **_property_** normalize_mode(: kp.KPEnum.NormalizeMode)
kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`NormalizeMode`](enum.md#kp.NormalizeMode)



#### **_property_** padding_mode(: kp.KPEnum.PaddingMode)
kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`PaddingMode`](enum.md#kp.PaddingMode)



#### **_property_** resize_mode(: kp.KPEnum.ResizeMode)
kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ResizeMode`](enum.md#kp.ResizeMode)



#### **_property_** width(: int)
int: Inference image width (Must apply when using bytes image data).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.GenericRawResultNDArray(buffer_size)
Inference raw result buffer.


* **Attributes**

    * `buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int)

            int: Size of generic inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### **_property_** buffer_size(: int)
int: Size of generic inference raw result buffer.

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



---
 
### **class** kp.HwPreProcInfo(img_width=0, img_height=0, resized_img_width=0, resized_img_height=0, pad_top=0, pad_bottom=0, pad_left=0, pad_right=0, model_input_width=0, model_input_height=0, crop_area={'crop_box_index': 0, 'x': 0, 'y': 0, 'width': 0, 'height': 0})
Information of Hardware Pre Process.


* **Attributes**

    * `img_width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Image width before hardware pre-process.

    * **img_height: int, default=0**

            Image height before hardware pre-process.

    * **resized_img_width: int, default=0**

            Image width after resize.

    * **resized_img_height: int, default=0**

            Image height after resize.

    * **pad_top: int, default=0**

            Pixels padding on top.

    * **pad_bottom: int, default=0**

            Pixels padding on bottom.

    * **pad_left: int, default=0**

            Pixels padding on left.

    * **pad_right: int, default=0**

            Pixels padding on right.

    * **model_input_width: int, default=0**

            Model required input width.

    * **model_input_height: int, default=0**

            Model required input height.

    * **crop_area: InferenceCropBox, default=InferenceCropBox()**

            Information of crop area. (may not be the same as input due to hardware limitation)


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_area(: kp.KPValue.InferenceCropBox)
InferenceCropBox: Information of crop area. (may not be the same as input due to hardware limitation)

<!-- !! processed by numpydoc !! -->

* **Return type**

    `InferenceCropBox`



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** img_height(: int)
int: Image height before hardware pre-process.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** img_width(: int)
int: Image width before hardware pre-process.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_input_height(: int)
int: Model required input height.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** model_input_width(: int)
int: Model required input width.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** pad_bottom(: int)
int: Pixels padding on bottom.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** pad_left(: int)
int: Pixels padding on left.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** pad_right(: int)
int: Pixels padding on right.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** pad_top(: int)
int: Pixels padding on top.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** resized_img_height(: int)
int: Image height after resize.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** resized_img_width(: int)
int: Image width after resize.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.InferenceConfiguration(enable_frame_drop=False)
Inference configurations.


* **Attributes**

    * `enable_frame_drop` : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values), default=False

            bool: Enable this to keep inference non-blocking by dropping oldest and unprocessed frames.


<!-- !! processed by numpydoc !! -->

#### **_property_** enable_frame_drop(: bool)
bool: Enable this to keep inference non-blocking by dropping oldest and unprocessed frames.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`bool`](https://docs.python.org/3/library/functions.html#bool)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.InferenceCropBox(crop_box_index=0, x=0, y=0, width=0, height=0)
Class for an image crop region.


* **Attributes**

    * `crop_box_index` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Index number of crop box.

    * `x` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: X coordinate of crop box top-left corner.

    * `y` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Y coordinate of crop box top-left corner.

    * `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Width coordinate of crop box.

    * `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Height coordinate of crop box.


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_box_index(: int)
int: Index number of crop box.

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
int: Height coordinate of crop box.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** width(: int)
int: Width coordinate of crop box.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** x(: int)
int: X coordinate of crop box top-left corner.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** y(: int)
int: Y coordinate of crop box top-left corner.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.InferenceFixedNodeOutput(width=0, height=0, channel=0, radix=0, scale=0, factor=0, dtype=FixedPointDType.KP_FIXED_POINT_DTYPE_UNKNOWN, num_data=0, data=array([], dtype=float64), channels_ordering=ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
Generic inference node output in fixed-point format.


* **Attributes**

    * `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Width of output node.

    * `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Height of output node.

    * `channel` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Channel of output node.

    * `radix` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Radix for fixed/floating point conversion.

    * `scale` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Scale for fixed/floating point conversion.

    * `factor` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Conversion factor for fixed-point to floating-point conversion - formulation: scale \* (2 ^ radix).

    * `dtype` : [`FixedPointDType`](enum.md#kp.FixedPointDType), default=FixedPointDType.

            FixedPointDType: fixed-point data type.

    * `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of fixed-point values.

    * **data** : [`np.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), default=np.array([])

            N-dimensional numpy.ndarray of feature map. (Channel ordering: KL520 - H,C,W; KL720 - C,H,W)

    * `channels_ordering` : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering), default=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW

            kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)


<!-- !! processed by numpydoc !! -->

#### **_property_** channel(: int)
int: Channel of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** channels_ordering(: kp.KPEnum.ChannelOrdering)
kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ChannelOrdering`](enum.md#kp.ChannelOrdering)



#### **_property_** dtype(: kp.KPEnum.FixedPointDType)
FixedPointDType: fixed-point data type.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`FixedPointDType`](enum.md#kp.FixedPointDType)



#### **_property_** factor(: float)
float: Conversion factor for fixed-point to floating-point conversion - formulation: scale \* (2 ^ radix).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`float`](https://docs.python.org/3/library/functions.html#float)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** height(: int)
int: Height of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** ndarray(: numpy.ndarray)
numpy.ndarray: N-dimensional numpy.ndarray of feature map.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)



#### **_property_** num_data(: int)
int: Total number of fixed-point values.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** radix(: int)
int: Radix for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** scale(: float)
float: Scale for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`float`](https://docs.python.org/3/library/functions.html#float)



#### to_float_node_output()
Convert fixed-point node output to floating-point node output.


* **Returns**

    * **inference_float_node_output** : `kp.InferenceFloatNodeOutput`


<!-- !! processed by numpydoc !! -->

* **Return type**

    `InferenceFloatNodeOutput`



#### **_property_** width(: int)
int: Width of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.InferenceFloatNodeOutput(width=0, height=0, channel=0, num_data=0, data=array([], dtype=float64), channels_ordering=ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
Generic inference node output in floating-point format.


* **Attributes**

    * `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Width of output node.

    * `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Height of output node.

    * `channel` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Channel of output node.

    * `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of floating-point values.

    * **data** : [`np.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), default=np.array([])

            N-dimensional numpy.ndarray of feature map. (Channel ordering: KL520 - H,C,W; KL720 - C,H,W)

    * `channels_ordering` : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering), default=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW

            kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)


<!-- !! processed by numpydoc !! -->

#### **_property_** channel(: int)
int: Channel of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** channels_ordering(: kp.KPEnum.ChannelOrdering)
kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ChannelOrdering`](enum.md#kp.ChannelOrdering)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** height(: int)
int: Height of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** ndarray(: numpy.ndarray)
numpy.ndarray: N-dimensional numpy.ndarray of feature map.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)



#### **_property_** num_data(: int)
int: Total number of floating-point values.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** width(: int)
int: Width of output node.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.ModelNefDescriptor(magic=0, metadata={'kn_number': '0x0', 'toolchain_version': '', 'compiler_version': '', 'nef_ ..., target_chip=ModelTargetChip.KP_MODEL_TARGET_CHIP_UNKNOWN, crc=0, models=[])
A basic descriptor for NEF.


* **Attributes**

    * `magic` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Magic number for model_nef_descriptor (0x5AA55AA5).

    * `metadata` : `ModelNefMetadata`, default=ModelNefMetadata()

            ModelNefMetadata: NEF metadata.

    * `target_chip` : [`ModelTargetChip`](enum.md#kp.ModelTargetChip), default=ModelTargetChip.KP_MODEL_TARGET_CHIP_UNKNOWN

            ModelTargetChip: Target chip of all models.

    * `crc` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: CRC of NEF models.

    * `models` : `List`[`SingleModelDescriptor`], default=[]

            List[SingleModelDescriptor]: Model descriptors.


<!-- !! processed by numpydoc !! -->

#### **_property_** crc(: int)
int: CRC of NEF models.

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



#### **_property_** magic(: int)
int: Magic number for model_nef_descriptor (0x5AA55AA5).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** metadata(: kp.KPValue.ModelNefMetadata)
ModelNefMetadata: NEF metadata.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `ModelNefMetadata`



#### **_property_** models(: List[kp.KPValue.SingleModelDescriptor])
List[SingleModelDescriptor]: Model descriptors.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`SingleModelDescriptor`]



#### **_property_** target_chip(: kp.KPEnum.ModelTargetChip)
ModelTargetChip: Target chip of all models.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelTargetChip`](enum.md#kp.ModelTargetChip)



---
 
### **class** kp.ModelNefMetadata(kn_number=0, toolchain_version='', compiler_version='', nef_schema_version={'version': '0.0.0'}, platform='')
A basic descriptor for a model NEF metadata.


* **Attributes**

    * `kn_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target KN number device of encrypted all models.

    * `toolchain_version` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Toolchain version of all models.

    * `compiler_version` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Compiler version of all models.

    * `nef_schema_version` : `NefSchemaVersion`, default=NefSchemaVersion()

            NefSchemaVersion: Schema version of nef.

    * `platform` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Target device platform USB dongle, 96 board, etc.


<!-- !! processed by numpydoc !! -->

#### **_property_** compiler_version(: str)
str: Compiler version of all models.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** kn_number(: int)
int: Target KN number device of encrypted all models.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** nef_schema_version(: kp.KPValue.NefSchemaVersion)
NefSchemaVersion: Schema version of nef.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `NefSchemaVersion`



#### **_property_** platform(: str)
str: Target device platform USB dongle, 96 board, etc.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### **_property_** toolchain_version(: str)
str: Toolchain version of all models.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



---
 
### **class** kp.NefSchemaVersion(major=0, minor=0, revision=0)
A NEF schema version object.


* **Attributes**

    * `major`

            int: Major number.

    * `minor`

            int: Minor number.

    * `revision`

            int: Revision number.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** major(: int)
int: Major number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** minor(: int)
int: Minor number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** revision(: int)
int: Revision number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.QuantizationParameters(quantized_fixed_point_descriptor_list=[])
Quantization parameters for tensor.


* **Attributes**

    * `quantized_fixed_point_descriptor_list` : `List`[`QuantizedFixedPointDescriptor`], default=[]

            List[QuantizedFixedPointDescriptor]: (a) List length = 1 for all-channel fixed-point quantization parameter, (b) List length > 1 for per-channel fixed-point quantization parameter.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** quantized_fixed_point_descriptor_list(: List[kp.KPValue.QuantizedFixedPointDescriptor])
List[QuantizedFixedPointDescriptor]: (a) List length = 1 for all-channel fixed-point quantization parameter, (b) List length > 1 for per-channel fixed-point quantization parameter.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`QuantizedFixedPointDescriptor`]



---
 
### **class** kp.QuantizedFixedPointDescriptor(scale=0, radix=0)
Quantization parameters for fixed-point value.


* **Attributes**

    * `scale` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Scale for fixed/floating point conversion.

    * `radix` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Radix for fixed/floating point conversion.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** radix(: int)
int: Radix for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** scale(: float)
float: Scale for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`float`](https://docs.python.org/3/library/functions.html#float)



---
 
### **class** kp.SetupFileSchemaVersion(major=0, minor=0, revision=0)
A setup information file version object.


* **Attributes**

    * `major`

            int: Major number.

    * `minor`

            int: Minor number.

    * `revision`

            int: Revision number.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** major(: int)
int: Major number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** minor(: int)
int: Minor number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** revision(: int)
int: Revision number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.SetupSchemaVersion(major=0, minor=0, revision=0)
A setup information schema version object.


* **Attributes**

    * `major`

            int: Major number.

    * `minor`

            int: Minor number.

    * `revision`

            int: Revision number.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** major(: int)
int: Major number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** minor(: int)
int: Minor number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** revision(: int)
int: Revision number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.SingleModelDescriptor(target_chip=ModelTargetChip.KP_MODEL_TARGET_CHIP_UNKNOWN, version=0, id=0, input_nodes=[], output_nodes=[], setup_schema_version={'version': '0.0.0'}, setup_file_schema_version={'version': '0.0.0'}, max_raw_out_size=0)
A basic descriptor for a model.


* **Attributes**

    * `target_chip` : [`ModelTargetChip`](enum.md#kp.ModelTargetChip), default=KP_MODEL_TARGET_CHIP_UNKNOWN

            ModelTargetChip: Target chip of model.

    * `version` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Version of model.

    * `id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Model ID.

    * `input_nodes` : `List`[`TensorDescriptor`], default=[]

            List[TensorDescriptor]: List of model input node tensor information.

    * `output_nodes` : `List`[`TensorDescriptor`], default=[]

            List[TensorDescriptor]: List of model output node tensor information.

    * `setup_schema_version` : `SetupSchemaVersion`, default=SetupSchemaVersion()

            SetupSchemaVersion: Schema version of setup.

    * `setup_file_schema_version` : `SetupFileSchemaVersion`, default=SetupFileSchemaVersion()

            SetupFileSchemaVersion: File schema version of setup.

    * `max_raw_out_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Needed raw output buffer size for this model.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** id(: int)
int: Model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** input_nodes(: List[kp.KPValue.TensorDescriptor])
List[TensorDescriptor]: List of model input node tensor information.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`TensorDescriptor`]



#### **_property_** max_raw_out_size(: int)
int: Needed raw output buffer size for this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** output_nodes(: List[kp.KPValue.TensorDescriptor])
List[TensorDescriptor]: List of model output node tensor information.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`TensorDescriptor`]



#### **_property_** setup_file_schema_version(: kp.KPValue.SetupFileSchemaVersion)
SetupFileSchemaVersion: File schema version of setup.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `SetupFileSchemaVersion`



#### **_property_** setup_schema_version(: kp.KPValue.SetupSchemaVersion)
SetupSchemaVersion: Schema version of setup.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `SetupSchemaVersion`



#### **_property_** target_chip(: kp.KPEnum.ModelTargetChip)
ModelTargetChip: Target chip of model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelTargetChip`](enum.md#kp.ModelTargetChip)



#### **_property_** version(: int)
int: Version of model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.SystemInfo(kn_number=0, firmware_version={'firmware_version': '0.0.0-build.0'})
System Information of Kneron device.


* **Attributes**

    * `kn_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Unique Kneron device ID.

    * `firmware_version` : `kp.FirmwareVersion`, default=kp.FirmwareVersion()

            kp.FirmwareVersion: Firmware version of Kneron device.


<!-- !! processed by numpydoc !! -->

#### **_property_** firmware_version()
kp.FirmwareVersion: Firmware version of Kneron device.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** kn_number()
int: Unique Kneron device ID.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.TensorDescriptor(index=0, name='', shape_npu=[], shape_onnx=[], data_layout=ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_UNKNOWN, quantization_parameters={'quantized_fixed_point_descriptor_list': {}})
Tensor information.


* **Attributes**

    * `index` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Index number of the tensor.

    * `name` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Name of the tensor.

    * `shape_npu` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: NPU shape of the tensor.

    * `shape_onnx` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: ONNX shape of the tensor.

    * `data_layout` : [`ModelTensorDataLayout`](enum.md#kp.ModelTensorDataLayout), default=ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_UNKNOWN

            ModelTensorDataLayout: NPU data layout of the tensor.

    * `quantization_parameters` : `QuantizationParameters`, default=QuantizationParameters()

            QuantizationParameters: Quantization parameters f the tensor.


<!-- !! processed by numpydoc !! -->

#### **_property_** data_layout(: kp.KPEnum.ModelTensorDataLayout)
ModelTensorDataLayout: NPU data layout of the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelTensorDataLayout`](enum.md#kp.ModelTensorDataLayout)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** index(: int)
int: Index number of the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** name(: str)
str: Name of the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### **_property_** quantization_parameters(: kp.KPValue.QuantizationParameters)
QuantizationParameters: Quantization parameters f the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `QuantizationParameters`



#### **_property_** shape_npu(: List[int])
List[int]: NPU shape of the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]



#### **_property_** shape_onnx(: List[int])
List[int]: ONNX shape of the tensor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`int`](https://docs.python.org/3/library/functions.html#int)]
