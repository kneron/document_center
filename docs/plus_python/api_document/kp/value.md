# kp value

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.DeviceDescriptor(usb_port_id=0, vendor_id=0, product_id=0, link_speed=UsbSpeed.KP_USB_SPEED_UNKNOWN, kn_number=0, is_connectable=False, usb_port_path='', firmware='')
Information of one connected device from USB perspectives.


* **Attributes**

    `usb_port_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: An unique ID representing for a Kneron device, can be used as input while connecting devices.

    `vendor_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Supposed to be 0x3231.

    `product_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: USB PID (Product ID).

    `link_speed` : [`UsbSpeed`](enum.md#kp.UsbSpeed), default=UsbSpeed.KP_USB_SPEED_UNKNOWN

        UsbSpeed: Enum for USB speed mode.

    `kn_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: KN number.

    `is_connectable` : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values), default=False

        bool: Indicate if this device is connectable.

    `usb_port_path` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

        str: “busNo-hub_portNo-device_portNo” (ex: “1-2-3”, means bus 1 - (hub) port 2 - (device) port 3)

    `firmware` : [`str`](https://docs.python.org/3/library/stdtypes.html#str), default=’’

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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

    `device_descriptor_list` : `List`[`kp.DeviceDescriptor`], default=[]

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.DeviceGroup(address)
A handle represent connected Kneron device.


* **Attributes**

    `address` : [`int`](https://docs.python.org/3/library/functions.html#int)

        int: Memory address of connected Kneron device handler.


<!-- !! processed by numpydoc !! -->

#### **_property_** address(: int)
int: Memory address of connected Kneron device handler.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.FirmwareVersion(reserved=0, major=0, minor=0, update=0, build=0)
Information of firmware version.


* **Attributes**

    `reserved` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Reserved version number for backward compatibility.

    **major** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    **minor** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    **update** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    **build** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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
 
### **class** kp.GenericRawBypassPreProcImageHeader(model_id=0, inference_number=0, image_buffer_size=0)
Inference descriptor for images bypass pre-processing.


* **Attributes**

    `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Target inference model ID.

    `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference sequence number.

    `image_buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference image buffer size.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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
 
### **class** kp.GenericRawBypassPreProcResult(buffer_size)
Generic inference raw result for bypass pre-processing.


* **Attributes**

    `header` : `kp.GenericRawBypassPreProcResultHeader`

        kp.GenericRawBypassPreProcResultHeader: Inference raw output descriptor for bypass pre-processing.

    `raw_result` : `kp.GenericRawResultNDArray`

        kp.GenericRawResultNDArray: Inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** header(: kp.KPValue.GenericRawBypassPreProcResultHeader)
kp.GenericRawBypassPreProcResultHeader: Inference raw output descriptor for bypass pre-processing.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawBypassPreProcResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultNDArray`



---
 
### **class** kp.GenericRawBypassPreProcResultHeader(inference_number=0, crop_number=0, num_output_node=0)
Inference raw output descriptor for bypass pre-processing.


* **Attributes**

    `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference sequence number.

    `crop_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Crop box sequence number.

    `num_output_node` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Total number of output nodes.


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_number(: int)
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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



---
 
### **class** kp.GenericRawImageHeader(model_id=0, resize_mode=ResizeMode.KP_RESIZE_ENABLE, padding_mode=PaddingMode.KP_PADDING_CORNER, normalize_mode=NormalizeMode.KP_NORMALIZE_KNERON, inference_number=0, inference_crop_box_list=[], width=0, height=0, image_format=ImageFormat.KP_IMAGE_FORMAT_RGB565)
Inference descriptor for images.


* **Attributes**

    `model_id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Target inference model ID.

    `resize_mode` : [`kp.ResizeMode`](enum.md#kp.ResizeMode), default=kp.ResizeMode.KP_RESIZE_ENABLE

        kp.ResizeMode: Preprocess resize mode, refer to ResizeMode.

    `padding_mode` : [`kp.PaddingMode`](enum.md#kp.PaddingMode), default=kp.PaddingMode.KP_PADDING_CORNER

        kp.PaddingMode: Preprocess padding mode, none or auto refer to PaddingMode.

    `normalize_mode` : [`kp.NormalizeMode`](enum.md#kp.NormalizeMode), default=kp.NormalizeMode.KP_NORMALIZE_KNERON

        kp.NormalizeMode: Inference normalization, refer to NormalizeMode.

    `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference sequence number.

    `inference_crop_box_list` : `List`[`kp.InferenceCropBox`], default=[]

        List[kp.InferenceCropBox]: Box information to crop.

    `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference image width.

    `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference image height.

    `image_format` : [`kp.ImageFormat`](enum.md#kp.ImageFormat), default=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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

    [`ImageFormat`](enum.md#kp.ImageFormat)



#### **_property_** inference_crop_box_list(: List[kp.KPValue.InferenceCropBox])
List[kp.InferenceCropBox]: Box information to crop.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`InferenceCropBox`]



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
int: Inference image width.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.GenericRawResult(buffer_size)
Generic inference raw result.


* **Attributes**

    `header` : `kp.GenericRawResultHeader`

        kp.GenericRawResultHeader: Inference raw output descriptor.

    `raw_result` : `kp.GenericRawResultNDArray`

        kp.GenericRawResultNDArray: Inference raw result buffer.


<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** header(: kp.KPValue.GenericRawResultHeader)
kp.GenericRawResultHeader: Inference raw output descriptor.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultHeader`



#### **_property_** raw_result(: kp.KPValue.GenericRawResultNDArray)
kp.GenericRawResultNDArray: Inference raw result buffer.

<!-- !! processed by numpydoc !! -->

* **Return type**

    `GenericRawResultNDArray`



---
 
### **class** kp.GenericRawResultHeader(inference_number=0, crop_number=0, num_output_node=0)
Inference raw output descriptor.


* **Attributes**

    `inference_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Inference sequence number.

    `crop_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Crop box sequence number.

    `num_output_node` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Total number of output nodes.


<!-- !! processed by numpydoc !! -->

#### **_property_** crop_number(: int)
int: Crop box sequence number.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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



---
 
### **class** kp.GenericRawResultNDArray(buffer_size)
Inference raw result buffer.


* **Attributes**

    `buffer_size` : [`int`](https://docs.python.org/3/library/functions.html#int)

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.InferenceConfiguration(enable_frame_drop=False)
Inference configurations.


* **Attributes**

    `enable_frame_drop` : [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values), default=False

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



---
 
### **class** kp.InferenceCropBox(crop_box_index=0, x=0, y=0, width=0, height=0)
Class for an image crop region.


* **Attributes**

    `crop_box_index` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Index number of crop box.

    `x` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: X coordinate of crop box top-left corner.

    `y` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Y coordinate of crop box top-left corner.

    `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Width coordinate of crop box.

    `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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
 
### **class** kp.InferenceFixedNodeOutput(width=0, height=0, channel=0, radix=0, scale=0, factor=0, num_data=0, data=array([], dtype=float64), channels_ordering=ChannelOrdering.KP_CHANNEL_ORDERING_CHW)
Generic inference node output in fixed-point format.


* **Attributes**

    `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Width of output node.

    `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Height of output node.

    `channel` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Channel of output node.

    `radix` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Radix for fixed/floating point conversion.

    `scale` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

        float: Scale for fixed/floating point conversion.

    `factor` : [`float`](https://docs.python.org/3/library/functions.html#float), default=0

        float: Conversion factor for fixed-point to floating-point conversion - formulation: 1 / (scale \* (2 ^ radix)).

    `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Total number of fixed-point values.

    **data** : `np.ndarray`, default=np.array([])

        N-dimensional numpy.ndarray of feature map. (Channel ordering: KL520 - H,C,W; KL720 - C,H,W)

    `channels_ordering` : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering), default=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW

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



#### **_property_** factor(: float)
float: Conversion factor for fixed-point to floating-point conversion - formulation: 1 / (scale \* (2 ^ radix)).

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`float`](https://docs.python.org/3/library/functions.html#float)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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

    `ndarray`



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

    **inference_float_node_output** : `kp.InferenceFloatNodeOutput`


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

    `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Width of output node.

    `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Height of output node.

    `channel` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Channel of output node.

    `num_data` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Total number of floating-point values.

    **data** : `np.ndarray`, default=np.array([])

        N-dimensional numpy.ndarray of feature map. (Channel ordering: KL520 - H,C,W; KL720 - C,H,W)

    `channels_ordering` : [`kp.ChannelOrdering`](enum.md#kp.ChannelOrdering), default=kp.ChannelOrdering.KP_CHANNEL_ORDERING_CHW

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

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

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

    `ndarray`



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
 
### **class** kp.ModelNefDescriptor(crc=0, num_models=0, models=[])
A basic descriptor for a NEF.


* **Attributes**

    `crc` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: The CRC of all models.

    `num_models` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: The number of models contains in NEF.

    `models` : `List`[`kp.SingleModelDescriptor`], default=[]

        List[kp.SingleModelDescriptor]: SingleModelDescriptor objects list, contain information of uploaded NEF information.


<!-- !! processed by numpydoc !! -->

#### **_property_** crc(: int)
int: The CRC of all models.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** models(: List[kp.KPValue.SingleModelDescriptor])
List[kp.SingleModelDescriptor]: SingleModelDescriptor objects list, contain information of uploaded NEF information.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`SingleModelDescriptor`]



#### **_property_** num_models(: int)
int: The number of models contains in NEF.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.SingleModelDescriptor(id=0, max_raw_out_size=0, width=0, height=0, channel=0, img_format=ImageFormat.KP_IMAGE_FORMAT_RGBA8888)
A basic descriptor for a model.


* **Attributes**

    `id` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Model ID.

    `max_raw_out_size` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Needed raw output buffer size for this model.

    `width` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: The input width of this model.

    `height` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: input height of this model.

    `channel` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: The input channel of this model.

    `img_format` : [`kp.ImageFormat`](enum.md#kp.ImageFormat), default=kp.ImageFormat.KP_IMAGE_FORMAT_RGBA8888

        kp.ImageFormat: The input image format of this model.


<!-- !! processed by numpydoc !! -->

#### **_property_** channel(: int)
int: The input channel of this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** height(: int)
int: input height of this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** id(: int)
int: Model ID.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** img_format(: kp.KPEnum.ImageFormat)
kp.ImageFormat: The input image format of this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ImageFormat`](enum.md#kp.ImageFormat)



#### **_property_** max_raw_out_size(: int)
int: Needed raw output buffer size for this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



#### **_property_** width(: int)
int: The input width of this model.

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`int`](https://docs.python.org/3/library/functions.html#int)



---
 
### **class** kp.SystemInfo(kn_number=0, firmware_version={'firmware_version': '0.0.0-build.0'})
System Information of Kneron device.


* **Attributes**

    `kn_number` : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

        int: Unique Kneron device ID.

    `firmware_version` : `kp.FirmwareVersion`, default=kp.FirmwareVersion()

        kp.FirmwareVersion: Firmware version of Kneron device.


<!-- !! processed by numpydoc !! -->

#### **_property_** firmware_version()
kp.FirmwareVersion: Firmware version of Kneron device.

<!-- !! processed by numpydoc !! -->

#### get_member_variable_dict()
Represent member variables with Dict format.


* **Returns**

    **ret** : [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)

        Represent member variables in Dict format.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict)



#### **_property_** kn_number()
int: Unique Kneron device ID.

<!-- !! processed by numpydoc !! -->
