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

    * `result_buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Result buffer size for FIFO queue.

    * `result_buffer_count` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Result buffer count for FIFO queue.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** input_buffer_count(: [int](https://docs.python.org/3/library/functions.html#int))
int: Input buffer count for FIFO queue.

<!-- !! processed by numpydoc !! -->

#### **_property_** input_buffer_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: Input buffer size for FIFO queue.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: DDR space for model.

<!-- !! processed by numpydoc !! -->

#### **_property_** result_buffer_count(: [int](https://docs.python.org/3/library/functions.html#int))
int: Result buffer count for FIFO queue.

<!-- !! processed by numpydoc !! -->

#### **_property_** result_buffer_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: Result buffer size for FIFO queue.

<!-- !! processed by numpydoc !! -->

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

#### **_property_** firmware(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Firmware description.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** is_connectable(: [bool](https://docs.python.org/3/library/functions.html#bool))
bool: Indicate if this device is connectable.

<!-- !! processed by numpydoc !! -->

#### **_property_** kn_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: KN number.

<!-- !! processed by numpydoc !! -->

#### **_property_** link_speed(: [UsbSpeed](enum.md#kp.UsbSpeed))
UsbSpeed: Enum for USB speed mode.

<!-- !! processed by numpydoc !! -->

#### **_property_** product_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

#### **_property_** usb_port_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: An unique ID representing for a Kneron device, can be used as input while connecting devices.

<!-- !! processed by numpydoc !! -->

#### **_property_** usb_port_path(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: “busNo-hub_portNo-device_portNo” (ex: “1-2-3”, means bus 1 - (hub) port 2 - (device) port 3)

<!-- !! processed by numpydoc !! -->

#### **_property_** vendor_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Supposed to be 0x3231.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.DeviceDescriptorList(device_descriptor_list=[])
Information of connected devices from USB perspectives.


* **Attributes**

    * `device_descriptor_list` : `List`[`kp.DeviceDescriptor`], default=[]

            List[kp.DeviceDescriptor]: DeviceDescriptor objects list, contain information of connected devices from USB perspectives.


<!-- !! processed by numpydoc !! -->

#### **_property_** device_descriptor_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[DeviceDescriptor])
List[kp.DeviceDescriptor]: DeviceDescriptor objects list, contain information of connected devices from USB
perspectives.

<!-- !! processed by numpydoc !! -->

#### **_property_** device_descriptor_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of connected devices.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.DeviceGroup(address)
A handle represent connected Kneron device.


* **Attributes**

    * `address` : [`int`](https://docs.python.org/3/library/functions.html#int)

            int: Memory address of connected Kneron device handler.


<!-- !! processed by numpydoc !! -->

#### **_property_** address(: [int](https://docs.python.org/3/library/functions.html#int))
int: Memory address of connected Kneron device handler.

<!-- !! processed by numpydoc !! -->

#### **_property_** content(: DeviceGroupContent)
DeviceGroupContent: A DeviceGroup descriptor.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** reserved(: [int](https://docs.python.org/3/library/functions.html#int))
int: Reserved version number for backward compatibility.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** inference_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

#### **_property_** input_node_data_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[GenericInputNodeData])
List[GenericInputNodeData]: Multiple input inference data descriptors (The data order must be mapping model input tensor order as shown in ModelNefDescriptor).

<!-- !! processed by numpydoc !! -->

#### **_property_** input_node_data_num(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of multiple input inference data descriptors in input_node_data_list.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** header(: GenericDataInferenceResultHeader)
kp.GenericDataInferenceResultHeader: Multiple input bypass pre-processing inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

#### **_property_** raw_result(: GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

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

#### **_property_** crop_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** inference_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

#### **_property_** num_output_node(: [int](https://docs.python.org/3/library/functions.html#int))
int: Total number of output nodes.

<!-- !! processed by numpydoc !! -->

#### **_property_** product_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** inference_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

#### **_property_** input_node_image_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[GenericInputNodeImage])
List[kp.GenericInputNodeImage]: Multiple input inference image data descriptors (Max number of input image is 5) (The image data order must be mapping model input tensor order as shown in ModelNefDescriptor).

<!-- !! processed by numpydoc !! -->

#### **_property_** input_node_image_num(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of multiple input inference image data descriptors in input_node_image_list.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** header(: GenericImageInferenceResultHeader)
kp.GenericImageInferenceResultHeader: Multiple input image inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

#### **_property_** raw_result(: GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

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

#### **_property_** crop_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** hw_pre_proc_info_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[HwPreProcInfo])
List[kp.HwPreProcInfo]: Hardware pre-process information for each input node.

<!-- !! processed by numpydoc !! -->

#### **_property_** inference_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference sequence number.

<!-- !! processed by numpydoc !! -->

#### **_property_** num_hw_pre_proc_info(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of hardware pre-process information.

<!-- !! processed by numpydoc !! -->

#### **_property_** num_output_node(: [int](https://docs.python.org/3/library/functions.html#int))
int: Total number of output nodes.

<!-- !! processed by numpydoc !! -->

#### **_property_** product_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: USB PID (Product ID).

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.GenericInputNodeData(buffer=b'')
Single data descriptor for bypass pre-processing inference.


* **Attributes**

    * `buffer` : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), default=bytes()

            bytes: The data bytes contains the inference data.


<!-- !! processed by numpydoc !! -->

#### **_property_** buffer(: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes))
bytes: The data bytes contains the inference data.

<!-- !! processed by numpydoc !! -->

#### **_property_** buffer_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference data buffer size.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

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

#### **_property_** crop_count(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of crop box.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** height(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference image height (Must apply when using bytes image data).

<!-- !! processed by numpydoc !! -->

#### **_property_** image(: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray))
numpy.ndarray: The data bytes or numpy.ndarray (dtype=numpy.uint8, dim=3) contains the image.

<!-- !! processed by numpydoc !! -->

#### **_property_** image_format(: [ImageFormat](enum.md#kp.ImageFormat))
kp.ImageFormat: Inference image format, refer to ImageFormat.

<!-- !! processed by numpydoc !! -->

#### **_property_** inference_crop_box_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[InferenceCropBox])
List[kp.InferenceCropBox]: Box information to crop.

<!-- !! processed by numpydoc !! -->

#### **_property_** normalize_mode(: [NormalizeMode](enum.md#kp.NormalizeMode))
kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

<!-- !! processed by numpydoc !! -->

#### **_property_** padding_mode(: [PaddingMode](enum.md#kp.PaddingMode))
kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

<!-- !! processed by numpydoc !! -->

#### **_property_** resize_mode(: [ResizeMode](enum.md#kp.ResizeMode))
kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

<!-- !! processed by numpydoc !! -->

#### **_property_** width(: [int](https://docs.python.org/3/library/functions.html#int))
int: Inference image width (Must apply when using bytes image data).

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.GenericRawResultNDArray(buffer_size)
Inference raw result buffer.


* **Attributes**

    * `buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int)

            int: Size of generic inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### **_property_** buffer_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: Size of generic inference raw result buffer.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

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

#### **_property_** crop_area(: InferenceCropBox)
InferenceCropBox: Information of crop area. (may not be the same as input due to hardware limitation)

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** img_height(: [int](https://docs.python.org/3/library/functions.html#int))
int: Image height before hardware pre-process.

<!-- !! processed by numpydoc !! -->

#### **_property_** img_width(: [int](https://docs.python.org/3/library/functions.html#int))
int: Image width before hardware pre-process.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_input_height(: [int](https://docs.python.org/3/library/functions.html#int))
int: Model required input height.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_input_width(: [int](https://docs.python.org/3/library/functions.html#int))
int: Model required input width.

<!-- !! processed by numpydoc !! -->

#### **_property_** pad_bottom(: [int](https://docs.python.org/3/library/functions.html#int))
int: Pixels padding on bottom.

<!-- !! processed by numpydoc !! -->

#### **_property_** pad_left(: [int](https://docs.python.org/3/library/functions.html#int))
int: Pixels padding on left.

<!-- !! processed by numpydoc !! -->

#### **_property_** pad_right(: [int](https://docs.python.org/3/library/functions.html#int))
int: Pixels padding on right.

<!-- !! processed by numpydoc !! -->

#### **_property_** pad_top(: [int](https://docs.python.org/3/library/functions.html#int))
int: Pixels padding on top.

<!-- !! processed by numpydoc !! -->

#### **_property_** resized_img_height(: [int](https://docs.python.org/3/library/functions.html#int))
int: Image height after resize.

<!-- !! processed by numpydoc !! -->

#### **_property_** resized_img_width(: [int](https://docs.python.org/3/library/functions.html#int))
int: Image width after resize.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.InferenceConfiguration(enable_frame_drop=False)
Inference configurations.


* **Attributes**

    * `enable_frame_drop` : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values), default=False

            bool: Enable this to keep inference non-blocking by dropping oldest and unprocessed frames.


<!-- !! processed by numpydoc !! -->

#### **_property_** enable_frame_drop(: [bool](https://docs.python.org/3/library/functions.html#bool))
bool: Enable this to keep inference non-blocking by dropping oldest and unprocessed frames.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

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

#### **_property_** crop_box_index(: [int](https://docs.python.org/3/library/functions.html#int))
int: Index number of crop box.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** height(: [int](https://docs.python.org/3/library/functions.html#int))
int: Height coordinate of crop box.

<!-- !! processed by numpydoc !! -->

#### **_property_** width(: [int](https://docs.python.org/3/library/functions.html#int))
int: Width coordinate of crop box.

<!-- !! processed by numpydoc !! -->

#### **_property_** x(: [int](https://docs.python.org/3/library/functions.html#int))
int: X coordinate of crop box top-left corner.

<!-- !! processed by numpydoc !! -->

#### **_property_** y(: [int](https://docs.python.org/3/library/functions.html#int))
int: Y coordinate of crop box top-left corner.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.InferenceFixedNodeOutput(name='', shape=[], quantization_parameters={'version': 'QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VER ..., dtype=FixedPointDType.KP_FIXED_POINT_DTYPE_UNKNOWN, num_data=0, data=array([], dtype=float64), channels_ordering=ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
Generic inference node output in fixed-point format.


* **Attributes**

    * `name` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Name of the tensor.

    * `shape` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: ONNX shape of the tensor.

    * `quantization_parameters` : `QuantizationParameters`, default=QuantizationParameters()

            QuantizationParameters: Quantization parameters of the tensor.

    * `dtype` : [`FixedPointDType`](enum.md#kp.FixedPointDType), default=FixedPointDType.

            FixedPointDType: fixed-point data type.

    * `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of fixed-point values.

    * **data** : [`np.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), default=np.array([])

            N-dimensional numpy.ndarray of feature map in fixed-point (8-bits/16-bits).

    * `channels_ordering` : [`ChannelOrdering`](enum.md#kp.ChannelOrdering), default=ChannelOrdering.KP_CHANNEL_ORDERING_CHW

            kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW, KP_CHANNEL_ORDERING_DEFAULT)


<!-- !! processed by numpydoc !! -->

#### **_property_** channels_ordering(: [ChannelOrdering](enum.md#kp.ChannelOrdering))
kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW, KP_CHANNEL_ORDERING_DEFAULT)

<!-- !! processed by numpydoc !! -->

#### **_property_** dtype(: [FixedPointDType](enum.md#kp.FixedPointDType))
FixedPointDType: fixed-point data type.

<!-- !! processed by numpydoc !! -->

#### **_property_** factor(: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray))
numpy.ndarray: N-dimensional numpy.ndarray of dequantization factor.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** name(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Name of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** ndarray(: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray))
numpy.ndarray: N-dimensional numpy.ndarray of feature map.

<!-- !! processed by numpydoc !! -->

#### **_property_** num_data(: [int](https://docs.python.org/3/library/functions.html#int))
int: Total number of fixed-point values.

<!-- !! processed by numpydoc !! -->

#### **_property_** quantization_parameters(: QuantizationParameters)
QuantizationParameters: Quantization parameters of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** shape(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: ONNX shape of the tensor.

<!-- !! processed by numpydoc !! -->

#### to_float_node_output()
Convert fixed-point node output to floating-point node output.


* **Returns**

    * **inference_float_node_output** : `kp.InferenceFloatNodeOutput`



* **Return type**

    `InferenceFloatNodeOutput`


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.InferenceFloatNodeOutput(name='', shape=[], num_data=0, data=array([], dtype=float64), channels_ordering=ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
Generic inference node output in floating-point format.


* **Attributes**

    * `name` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Name of the tensor.

    * `shape` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: ONNX shape of the tensor.

    * `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Total number of floating-point values.

    * **data** : [`np.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), default=np.array([])

            N-dimensional numpy.ndarray of feature map. (Channel ordering: KL520 - H,C,W; KL720 - C,H,W)

    * `channels_ordering` : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering), default=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW

            kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)


<!-- !! processed by numpydoc !! -->

#### **_property_** channels_ordering(: [ChannelOrdering](enum.md#kp.ChannelOrdering))
kp.ChannelOrdering: Channel ordering of feature map. (Options: KP_CHANNEL_ORDERING_HCW, KP_CHANNEL_ORDERING_CHW)

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** name(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Name of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** ndarray(: [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray))
numpy.ndarray: N-dimensional numpy.ndarray of feature map.

<!-- !! processed by numpydoc !! -->

#### **_property_** num_data(: [int](https://docs.python.org/3/library/functions.html#int))
int: Total number of floating-point values.

<!-- !! processed by numpydoc !! -->

#### **_property_** shape(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: ONNX shape of the tensor.

<!-- !! processed by numpydoc !! -->

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

#### **_property_** crc(: [int](https://docs.python.org/3/library/functions.html#int))
int: CRC of NEF models.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** magic(: [int](https://docs.python.org/3/library/functions.html#int))
int: Magic number for model_nef_descriptor (0x5AA55AA5).

<!-- !! processed by numpydoc !! -->

#### **_property_** metadata(: ModelNefMetadata)
ModelNefMetadata: NEF metadata.

<!-- !! processed by numpydoc !! -->

#### **_property_** models(: [List](https://docs.python.org/3/library/typing.html#typing.List)[SingleModelDescriptor])
List[SingleModelDescriptor]: Model descriptors.

<!-- !! processed by numpydoc !! -->

#### **_property_** target_chip(: [ModelTargetChip](enum.md#kp.ModelTargetChip))
ModelTargetChip: Target chip of all models.

<!-- !! processed by numpydoc !! -->

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

#### **_property_** compiler_version(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Compiler version of all models.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** kn_number(: [int](https://docs.python.org/3/library/functions.html#int))
int: Target KN number device of encrypted all models.

<!-- !! processed by numpydoc !! -->

#### **_property_** nef_schema_version(: NefSchemaVersion)
NefSchemaVersion: Schema version of nef.

<!-- !! processed by numpydoc !! -->

#### **_property_** platform(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Target device platform USB dongle, 96 board, etc.

<!-- !! processed by numpydoc !! -->

#### **_property_** toolchain_version(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Toolchain version of all models.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** major(: [int](https://docs.python.org/3/library/functions.html#int))
int: Major number.

<!-- !! processed by numpydoc !! -->

#### **_property_** minor(: [int](https://docs.python.org/3/library/functions.html#int))
int: Minor number.

<!-- !! processed by numpydoc !! -->

#### **_property_** revision(: [int](https://docs.python.org/3/library/functions.html#int))
int: Revision number.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.NpuPerformanceMonitorStatistics(model_id=0, npu_clock_rate=0, f0=0, f1=0, f2=0, f3=0, f4=0, f5=0, f6=0, f7=0)
One model inference performance monitor statistic data.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `npu_clock_rate` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: NPU clock rate.

    * `f0` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f0.

    * `f0_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f0.

    * `f1` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f1.

    * `f1_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f1.

    * `f2` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f2.

    * `f2_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f2.

    * `f3` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f3.

    * `f3_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f3.

    * `f4` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f4.

    * `f4_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f4.

    * `f5` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f5.

    * `f5_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f5.

    * `f6` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f6.

    * `f6_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f6.

    * `f7` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Value of performance monitor mode f7.

    * `f7_time` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: time of performance monitor mode f7.


<!-- !! processed by numpydoc !! -->

#### **_property_** f0(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f0.

<!-- !! processed by numpydoc !! -->

#### **_property_** f0_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f0.

<!-- !! processed by numpydoc !! -->

#### **_property_** f1(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f1.

<!-- !! processed by numpydoc !! -->

#### **_property_** f1_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f1.

<!-- !! processed by numpydoc !! -->

#### **_property_** f2(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f2.

<!-- !! processed by numpydoc !! -->

#### **_property_** f2_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f2.

<!-- !! processed by numpydoc !! -->

#### **_property_** f3(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f3.

<!-- !! processed by numpydoc !! -->

#### **_property_** f3_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f3.

<!-- !! processed by numpydoc !! -->

#### **_property_** f4(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f4.

<!-- !! processed by numpydoc !! -->

#### **_property_** f4_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f4.

<!-- !! processed by numpydoc !! -->

#### **_property_** f5(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f5.

<!-- !! processed by numpydoc !! -->

#### **_property_** f5_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f5.

<!-- !! processed by numpydoc !! -->

#### **_property_** f6(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f6.

<!-- !! processed by numpydoc !! -->

#### **_property_** f6_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f6.

<!-- !! processed by numpydoc !! -->

#### **_property_** f7(: [int](https://docs.python.org/3/library/functions.html#int))
int: Value of performance monitor mode f7.

<!-- !! processed by numpydoc !! -->

#### **_property_** f7_time(: [float](https://docs.python.org/3/library/functions.html#float))
float: time of performance monitor mode f7.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** model_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

#### **_property_** npu_clock_rate(: [int](https://docs.python.org/3/library/functions.html#int))
int: NPU clock rate.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.PerformanceMonitorData(npu_clock_rate=0, model_statistic_list=[])
Model inference performance monitor data.


* **Attributes**

    * `model_profiled_num` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Number of profiled model.

    * `model_statistic_list` : `List`[`kp.NpuPerformanceMonitorStatistics`], default=[]

            List[kp.NpuPerformanceMonitorStatistics]: List of performance monitor statistic data.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** model_profiled_num(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of profiled model.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_statistic_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[NpuPerformanceMonitorStatistics])
List[kp.NpuPerformanceMonitorStatistics]: List of performance monitor statistic data.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ProfileData(model_statistic_list=[])
Model inference profiling data.


* **Attributes**

    * `model_profiled_num` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Number of profiled model.

    * `model_statistic_list` : `List`[`kp.ProfileModelStatistics`], default=[]

            List[kp.ProfileModelStatistics]: List of model inference statistic data.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** model_profiled_num(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of profiled model.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_statistic_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[ProfileModelStatistics])
List[kp.ProfileModelStatistics]: List of model inference statistic data.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ProfileModelStatistics(model_id=0, inference_count=0, cpu_op_count=0, avg_pre_process_ms=0, avg_inference_ms=0, avg_cpu_op_ms=0, avg_cpu_op_per_cpu_node_ms=0, avg_post_process_ms=0)
One model inference statistic data.


* **Attributes**

    * `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Target inference model ID.

    * `inference_count` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Number of Inference in the statistic.

    * `cpu_op_count` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Number of CPU operation per inference.

    * `avg_pre_process_ms` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Average pre-process time in milliseconds.

    * `avg_inference_ms` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Average inference time in milliseconds.

    * `avg_cpu_op_ms` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Average CPU operation time per-inference in milliseconds.

    * `avg_cpu_op_per_cpu_node_ms` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Average CPU operation time per-CPU node in milliseconds.

    * `avg_post_process_ms` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

            float: Average post-process time in milliseconds.


<!-- !! processed by numpydoc !! -->

#### **_property_** avg_cpu_op_ms(: [float](https://docs.python.org/3/library/functions.html#float))
float: Average CPU operation time per-inference in milliseconds.

<!-- !! processed by numpydoc !! -->

#### **_property_** avg_cpu_op_per_cpu_node_ms(: [float](https://docs.python.org/3/library/functions.html#float))
float: Average CPU operation time per-CPU node in milliseconds.

<!-- !! processed by numpydoc !! -->

#### **_property_** avg_inference_ms(: [float](https://docs.python.org/3/library/functions.html#float))
float: Average inference time in milliseconds.

<!-- !! processed by numpydoc !! -->

#### **_property_** avg_post_process_ms(: [float](https://docs.python.org/3/library/functions.html#float))
float: Average post-process time in milliseconds.

<!-- !! processed by numpydoc !! -->

#### **_property_** avg_pre_process_ms(: [float](https://docs.python.org/3/library/functions.html#float))
float: Average pre-process time in milliseconds.

<!-- !! processed by numpydoc !! -->

#### **_property_** cpu_op_count(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of CPU operation per inference.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** inference_count(: [int](https://docs.python.org/3/library/functions.html#int))
int: Number of Inference in the statistic.

<!-- !! processed by numpydoc !! -->

#### **_property_** model_id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Target inference model ID.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.QuantizationParameters(version=QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VERSION_1, data={'quantized_axis': 0, 'quantized_fixed_point_descriptor_list': {}})
Quantization parameters data for tensor.


* **Attributes**

    * `version` : [`QuantizationParametersVersion`](enum.md#kp.QuantizationParametersVersion), default=QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VERSION_1

            QuantizationParametersVersion: Quantization parameters version (ref.

    * `data` : `Union`[`QuantizationParametersV1`] = `QuantizationParametersV1`

            Union[QuantizationParametersV1]: Quantization parameters for tensor.


<!-- !! processed by numpydoc !! -->

#### **_property_** data(: QuantizationParametersV1)
Union[QuantizationParametersV1]: Quantization parameters for tensor.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** v1(: QuantizationParametersV1)
QuantizationParametersV1: Quantization parameters for tensor. (Version 1)

<!-- !! processed by numpydoc !! -->

#### **_property_** version(: [QuantizationParametersVersion](enum.md#kp.QuantizationParametersVersion))
QuantizationParametersVersion: Quantization parameters version (ref. QuantizationParametersVersion).

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.QuantizationParametersV1(quantized_axis=0, quantized_fixed_point_descriptor_list=[])
Quantization parameters V1 for tensor.


* **Attributes**

    * `quantized_axis` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: The axis along which the fixed-point quantization information performed.

    * `quantized_fixed_point_descriptor_list` : `List`[`QuantizedFixedPointDescriptor`], default=[]

            List[QuantizedFixedPointDescriptor]: (a) List length = 1 for all-channel fixed-point quantization parameter, (b) List length > 1 for per-channel fixed-point quantization parameter.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** quantized_axis(: [int](https://docs.python.org/3/library/functions.html#int))
int: The axis along which the fixed-point quantization information performed.

<!-- !! processed by numpydoc !! -->

#### **_property_** quantized_fixed_point_descriptor_list(: [List](https://docs.python.org/3/library/typing.html#typing.List)[QuantizedFixedPointDescriptor])
List[QuantizedFixedPointDescriptor]: (a) List length = 1 for all-channel fixed-point quantization parameter, (b) List length > 1 for per-channel fixed-point quantization parameter.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.QuantizedFixedPointDescriptor(scale={'dtype': 'DataType.KP_DTYPE_FLOAT32', 'value': 1.0}, radix=0)
Quantization parameters for fixed-point value.


* **Attributes**

    * `scale` : `Scale`, default=Scale()

            float: Scale for fixed/floating point conversion.

    * `radix` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Radix for fixed/floating point conversion.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** radix(: [int](https://docs.python.org/3/library/functions.html#int))
int: Radix for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

#### **_property_** scale(: Scale)
float: Scale for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.Scale(dtype=DataType.KP_DTYPE_FLOAT32, value=1.0)
Scale of Quantization parameter.


* **Attributes**

    * `dtype` : [`DataType`](enum.md#kp.DataType), default=DataType.KP_DTYPE_FLOAT32

            DataType: enum for Kneron data type.

    * `value` : `Union`[`np.int8`, `np.int16`, `np.int32`, `np.int64`, `np.uint8`, `np.uint16`, `np.uint32`, `np.uint64`, `np.float32`, `np.float64`], default=np.float32(1.0)

            float: Scale for fixed/floating point conversion.


<!-- !! processed by numpydoc !! -->

#### **_property_** dtype(: [DataType](enum.md#kp.DataType))
DataType: enum for Kneron data type.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** value(: [float](https://docs.python.org/3/library/functions.html#float))
float: Scale for fixed/floating point conversion.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** major(: [int](https://docs.python.org/3/library/functions.html#int))
int: Major number.

<!-- !! processed by numpydoc !! -->

#### **_property_** minor(: [int](https://docs.python.org/3/library/functions.html#int))
int: Minor number.

<!-- !! processed by numpydoc !! -->

#### **_property_** revision(: [int](https://docs.python.org/3/library/functions.html#int))
int: Revision number.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** major(: [int](https://docs.python.org/3/library/functions.html#int))
int: Major number.

<!-- !! processed by numpydoc !! -->

#### **_property_** minor(: [int](https://docs.python.org/3/library/functions.html#int))
int: Minor number.

<!-- !! processed by numpydoc !! -->

#### **_property_** revision(: [int](https://docs.python.org/3/library/functions.html#int))
int: Revision number.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** id(: [int](https://docs.python.org/3/library/functions.html#int))
int: Model ID.

<!-- !! processed by numpydoc !! -->

#### **_property_** input_nodes(: [List](https://docs.python.org/3/library/typing.html#typing.List)[TensorDescriptor])
List[TensorDescriptor]: List of model input node tensor information.

<!-- !! processed by numpydoc !! -->

#### **_property_** max_raw_out_size(: [int](https://docs.python.org/3/library/functions.html#int))
int: Needed raw output buffer size for this model.

<!-- !! processed by numpydoc !! -->

#### **_property_** output_nodes(: [List](https://docs.python.org/3/library/typing.html#typing.List)[TensorDescriptor])
List[TensorDescriptor]: List of model output node tensor information.

<!-- !! processed by numpydoc !! -->

#### **_property_** setup_file_schema_version(: SetupFileSchemaVersion)
SetupFileSchemaVersion: File schema version of setup.

<!-- !! processed by numpydoc !! -->

#### **_property_** setup_schema_version(: SetupSchemaVersion)
SetupSchemaVersion: Schema version of setup.

<!-- !! processed by numpydoc !! -->

#### **_property_** target_chip(: [ModelTargetChip](enum.md#kp.ModelTargetChip))
ModelTargetChip: Target chip of model.

<!-- !! processed by numpydoc !! -->

#### **_property_** version(: [int](https://docs.python.org/3/library/functions.html#int))
int: Version of model.

<!-- !! processed by numpydoc !! -->

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



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** kn_number()
int: Unique Kneron device ID.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.TensorDescriptor(index=0, name='', data_layout=ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_UNKNOWN, tensor_shape_info={'version': 'ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_ ..., quantization_parameters={'version': 'QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VER ...)
Tensor information.


* **Attributes**

    * `index` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            int: Index number of the tensor.

    * `name` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

            str: Name of the tensor.

    * `data_layout` : [`ModelTensorDataLayout`](enum.md#kp.ModelTensorDataLayout), default=ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_UNKNOWN

            ModelTensorDataLayout: NPU data layout of the tensor.

    * `tensor_shape_info` : `TensorShapeInfo`, default=TensorShapeInfo()

            TensorShapeInfo: Tensor shape information.

    * `quantization_parameters` : `QuantizationParameters`, default=QuantizationParameters()

            QuantizationParameters: Quantization parameters of the tensor.


<!-- !! processed by numpydoc !! -->

#### **_property_** data_layout(: [ModelTensorDataLayout](enum.md#kp.ModelTensorDataLayout))
ModelTensorDataLayout: NPU data layout of the tensor.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** index(: [int](https://docs.python.org/3/library/functions.html#int))
int: Index number of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** name(: [str](https://docs.python.org/3/library/stdtypes.html#str))
str: Name of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** quantization_parameters(: QuantizationParameters)
QuantizationParameters: Quantization parameters of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** tensor_shape_info(: TensorShapeInfo)
TensorShapeInfo: Tensor shape information.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.TensorShapeInfo(version=ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1, data={'shape_npu': [], 'shape_onnx': [], 'axis_permutation_onnx_to_npu': []})
Tensor shape information.


* **Attributes**

    * `version` : [`ModelTensorShapeInformationVersion`](enum.md#kp.ModelTensorShapeInformationVersion), default=ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1

            ModelTensorShapeInformationVersion: Shape information version (ref.

    * `data` : `Union`[`TensorShapeInfoV1`, `TensorShapeInfoV2`] = `TensorShapeInfoV1`

            Union[TensorShapeInfoV1, TensorShapeInfoV2]: Shape information data.


<!-- !! processed by numpydoc !! -->

#### **_property_** data(: TensorShapeInfoV1 | TensorShapeInfoV2)
Union[TensorShapeInfoV1, TensorShapeInfoV2]: Shape information data.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** v1(: TensorShapeInfoV1)
TensorShapeInfoV1: Tensor shape information. (version 1)

<!-- !! processed by numpydoc !! -->

#### **_property_** v2(: TensorShapeInfoV2)
TensorShapeInfoV2: Tensor shape information. (version 2)

<!-- !! processed by numpydoc !! -->

#### **_property_** version(: [ModelTensorShapeInformationVersion](enum.md#kp.ModelTensorShapeInformationVersion))
ModelTensorShapeInformationVersion: Shape information version (ref. kp_model_tensor_shape_info_version_t).

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.TensorShapeInfoV1(shape_npu=[], shape_onnx=[], axis_permutation_onnx_to_npu=[])
Tensor shape information. (version 1)


* **Attributes**

    * `shape_npu` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: NPU shape of the tensor (Default dimension order: BxCxHxW).

    * `shape_onnx` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: ONNX shape of the tensor.

    * `axis_permutation_onnx_to_npu` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: Remap axis permutation from onnx to npu shape (shape_intrp_dim).


<!-- !! processed by numpydoc !! -->

#### **_property_** axis_permutation_onnx_to_npu(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: Remap axis permutation from onnx to npu shape (shape_intrp_dim).

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** shape_npu(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: NPU shape of the tensor (Default dimension order: BxCxHxW).

<!-- !! processed by numpydoc !! -->

#### **_property_** shape_onnx(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: ONNX shape of the tensor.

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.TensorShapeInfoV2(shape=[], stride_onnx=[], stride_npu=[])
Tensor shape information. (version 2)


* **Attributes**

    * `shape` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: ONNX shape of the tensor.

    * `stride_onnx` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: Data access stride of ONNX (in scalar).

    * `stride_npu` : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)], default=[]

            List[int]: Data access stride of NPU (in scalar).


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    * **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

            Represent member variables in Dict format.



* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)


<!-- !! processed by numpydoc !! -->

#### **_property_** shape(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: ONNX shape of the tensor.

<!-- !! processed by numpydoc !! -->

#### **_property_** stride_npu(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: Data access stride of NPU (in scalar).

<!-- !! processed by numpydoc !! -->

#### **_property_** stride_onnx(: [List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/functions.html#int)])
List[int]: Data access stride of ONNX (in scalar).

<!-- !! processed by numpydoc !! -->
