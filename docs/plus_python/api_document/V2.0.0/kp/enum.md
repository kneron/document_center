# kp enum

<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ApiReturnCode(value)
Return code of PLUS APIs.


* **Attributes**

    * **KP_SUCCESS** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

    * **KP_ERROR_USB_IO_N1** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-1

    * **KP_ERROR_USB_INVALID_PARAM_N2** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-2

    * **KP_ERROR_USB_ACCESS_N3** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-3

    * **KP_ERROR_USB_NO_DEVICE_N4** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-4

    * **KP_ERROR_USB_NOT_FOUND_N5** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-5

    * **KP_ERROR_USB_BUSY_N6** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-6

    * **KP_ERROR_USB_TIMEOUT_N7** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-7

    * **KP_ERROR_USB_OVERFLOW_N8** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-8

    * **KP_ERROR_USB_PIPE_N9** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-9

    * **KP_ERROR_USB_INTERRUPTED_N10** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-10

    * **KP_ERROR_USB_NO_MEM_N11** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-11

    * **KP_ERROR_USB_NOT_SUPPORTED_N12** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-12

    * **KP_ERROR_USB_OTHER_N99** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-99

    * **KP_ERROR_WDI_BEGIN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-200

    * **KP_ERROR_WDI_IO_N1** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-201

    * **KP_ERROR_WDI_INVALID_PARAM_N2** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-202

    * **KP_ERROR_WDI_ACCESS_N3** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-203

    * **KP_ERROR_WDI_NO_DEVICE_N4** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-204

    * **KP_ERROR_WDI_NOT_FOUND_N5** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-205

    * **KP_ERROR_WDI_BUSY_N6** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-206

    * **KP_ERROR_WDI_TIMEOUT_N7** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-207

    * **KP_ERROR_WDI_OVERFLOW_N8** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-208

    * **KP_ERROR_WDI_PENDING_INSTALLATION_N9** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-209

    * **KP_ERROR_WDI_INTERRUPTED_N10** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-210

    * **KP_ERROR_WDI_RESOURCE_N11** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-211

    * **KP_ERROR_WDI_NOT_SUPPORTED_N12** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-212

    * **KP_ERROR_WDI_EXISTS_N13** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-213

    * **KP_ERROR_WDI_USER_CANCEL_N14** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-214

    * **KP_ERROR_WDI_NEEDS_ADMIN_N15** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-215

    * **KP_ERROR_WDI_WOW64_N16** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-216

    * **KP_ERROR_WDI_INF_SYNTAX_N17** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-217

    * **KP_ERROR_WDI_CAT_MISSING_N18** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-218

    * **KP_ERROR_WDI_UNSIGNED_N19** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-219

    * **KP_ERROR_WDI_OTHER_N99** : [`int`](https://docs.python.org/3/library/functions.html#int), default=-299

    * **KP_ERROR_DEVICE_NOT_EXIST_10** : [`int`](https://docs.python.org/3/library/functions.html#int), default=10

    * **KP_ERROR_DEVICE_INCORRECT_RESPONSE_11** : [`int`](https://docs.python.org/3/library/functions.html#int), default=11

    * **KP_ERROR_INVALID_PARAM_12** : [`int`](https://docs.python.org/3/library/functions.html#int), default=12

    * **KP_ERROR_SEND_DESC_FAIL_13** : [`int`](https://docs.python.org/3/library/functions.html#int), default=13

    * **KP_ERROR_SEND_DATA_FAIL_14** : [`int`](https://docs.python.org/3/library/functions.html#int), default=14

    * **KP_ERROR_SEND_DATA_TOO_LARGE_15** : [`int`](https://docs.python.org/3/library/functions.html#int), default=15

    * **KP_ERROR_RECV_DESC_FAIL_16** : [`int`](https://docs.python.org/3/library/functions.html#int), default=16

    * **KP_ERROR_RECV_DATA_FAIL_17** : [`int`](https://docs.python.org/3/library/functions.html#int), default=17

    * **KP_ERROR_RECV_DATA_TOO_LARGE_18** : [`int`](https://docs.python.org/3/library/functions.html#int), default=18

    * **KP_ERROR_FW_UPDATE_FAILED_19** : [`int`](https://docs.python.org/3/library/functions.html#int), default=19

    * **KP_ERROR_FILE_OPEN_FAILED_20** : [`int`](https://docs.python.org/3/library/functions.html#int), default=20

    * **KP_ERROR_INVALID_MODEL_21** : [`int`](https://docs.python.org/3/library/functions.html#int), default=21

    * **KP_ERROR_IMAGE_RESOLUTION_TOO_SMALL_22** : [`int`](https://docs.python.org/3/library/functions.html#int), default=22

    * **KP_ERROR_IMAGE_ODD_WIDTH_23** : [`int`](https://docs.python.org/3/library/functions.html#int), default=23

    * **KP_ERROR_INVALID_FIRMWARE_24** : [`int`](https://docs.python.org/3/library/functions.html#int), default=24

    * **KP_ERROR_RESET_FAILED_25** : [`int`](https://docs.python.org/3/library/functions.html#int), default=25

    * **KP_ERROR_DEVICES_NUMBER_26** : [`int`](https://docs.python.org/3/library/functions.html#int), default=26

    * **KP_ERROR_CONFIGURE_DEVICE_27** : [`int`](https://docs.python.org/3/library/functions.html#int), default=27

    * **KP_ERROR_CONNECT_FAILED_28** : [`int`](https://docs.python.org/3/library/functions.html#int), default=28

    * **KP_ERROR_DEVICE_GROUP_MIX_PRODUCT_29** : [`int`](https://docs.python.org/3/library/functions.html#int), default=29

    * **KP_ERROR_RECEIVE_INCORRECT_HEADER_STAMP_30** : [`int`](https://docs.python.org/3/library/functions.html#int), default=30

    * **KP_ERROR_RECEIVE_SIZE_MISMATCH_31** : [`int`](https://docs.python.org/3/library/functions.html#int), default=31

    * **KP_ERROR_RECEIVE_JOB_ID_MISMATCH_32** : [`int`](https://docs.python.org/3/library/functions.html#int), default=32

    * **KP_ERROR_INVALID_CUSTOMIZED_JOB_ID_33** : [`int`](https://docs.python.org/3/library/functions.html#int), default=33

    * **KP_ERROR_FW_LOAD_FAILED_34** : [`int`](https://docs.python.org/3/library/functions.html#int), default=34

    * **KP_ERROR_MODEL_NOT_LOADED_35** : [`int`](https://docs.python.org/3/library/functions.html#int), default=35

    * **KP_ERROR_INVALID_CHECKPOINT_DATA_36** : [`int`](https://docs.python.org/3/library/functions.html#int), default=36

    * **KP_DBG_CHECKPOINT_END_37** : [`int`](https://docs.python.org/3/library/functions.html#int), default=37

    * **KP_ERROR_INVALID_HOST_38** : [`int`](https://docs.python.org/3/library/functions.html#int), default=38

    * **KP_ERROR_MEMORY_FREE_FAILURE_39** : [`int`](https://docs.python.org/3/library/functions.html#int), default=39

    * **KP_ERROR_USB_BOOT_LOAD_SECOND_MODEL_40** : [`int`](https://docs.python.org/3/library/functions.html#int), default=40

    * **KP_ERROR_CHECK_FW_VERSION_FAILED_41** : [`int`](https://docs.python.org/3/library/functions.html#int), default=41

    * **KP_ERROR_OTHER_99** : [`int`](https://docs.python.org/3/library/functions.html#int), default=99

    * **KP_FW_ERROR_UNKNOWN_APP** : [`int`](https://docs.python.org/3/library/functions.html#int), default=100

    * **KP_FW_INFERENCE_ERROR_101** : [`int`](https://docs.python.org/3/library/functions.html#int), default=101

    * **KP_FW_DDR_MALLOC_FAILED_102** : [`int`](https://docs.python.org/3/library/functions.html#int), default=102

    * **KP_FW_INFERENCE_TIMEOUT_103** : [`int`](https://docs.python.org/3/library/functions.html#int), default=103

    * **KP_FW_LOAD_MODEL_FAILED_104** : [`int`](https://docs.python.org/3/library/functions.html#int), default=104

    * **KP_FW_CONFIG_POST_PROC_ERROR_MALLOC_FAILED_105** : [`int`](https://docs.python.org/3/library/functions.html#int), default=105

    * **KP_FW_CONFIG_POST_PROC_ERROR_NO_SPACE_106** : [`int`](https://docs.python.org/3/library/functions.html#int), default=106

    * **KP_FW_IMAGE_SIZE_NOT_MATCH_MODEL_INPUT_107** : [`int`](https://docs.python.org/3/library/functions.html#int), default=107

    * **KP_FW_NOT_SUPPORT_PREPROCESSING_108** : [`int`](https://docs.python.org/3/library/functions.html#int), default=108

    * **KP_FW_GET_MODEL_INFO_FAILED_109** : [`int`](https://docs.python.org/3/library/functions.html#int), default=109

    * **KP_FW_WRONG_INPUT_BUFFER_COUNT_110** : [`int`](https://docs.python.org/3/library/functions.html#int), default=110

    * **KP_FW_INVALID_PRE_PROC_MODEL_INPUT_SIZE_111** : [`int`](https://docs.python.org/3/library/functions.html#int), default=111

    * **KP_FW_INVALID_INPUT_CROP_PARAM_112** : [`int`](https://docs.python.org/3/library/functions.html#int), default=112

    * **KP_FW_NCPU_ERR_BEGIN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=200

    * **KP_FW_NCPU_INVALID_IMAGE_201** : [`int`](https://docs.python.org/3/library/functions.html#int), default=201

    * **KP_FW_EFUSE_CAN_NOT_BURN_300** : [`int`](https://docs.python.org/3/library/functions.html#int), default=300

    * **KP_FW_EFUSE_PROTECTED_301** : [`int`](https://docs.python.org/3/library/functions.html#int), default=301

    * **KP_FW_EFUSE_OTHER_302** : [`int`](https://docs.python.org/3/library/functions.html#int), default=302


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ChannelOrdering(value)
enum for feature map channels ordering.


* **Attributes**

    * **KP_CHANNEL_ORDERING_HCW** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            KL520 default, height/channel/width in order.

    * **KP_CHANNEL_ORDERING_CHW** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            KL720 default, channel/height/width in order.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.FixedPointDType(value)
enum for fixed-point data type.


* **Attributes**

    * **KP_FIXED_POINT_DTYPE_UNKNOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            Unknown data type.

    * **KP_FIXED_POINT_DTYPE_INT8** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            Represent one fixed-point value by 8-bit data type.

    * **KP_FIXED_POINT_DTYPE_INT16** : [`int`](https://docs.python.org/3/library/functions.html#int), default=2

            Represent one fixed-point value by 16-bit data type.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ImageFormat(value)
enum for image format supported for inference.


* **Attributes**

    * **KP_IMAGE_FORMAT_UNKNOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x0

            Unknown format.

    * **KP_IMAGE_FORMAT_RGB565** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x60

            RGB565 16bits.

    * **KP_IMAGE_FORMAT_RGBA8888** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x0D

            RGBA8888 32bits.

    * **KP_IMAGE_FORMAT_YUYV** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x2F

            YUYV 16bits.

    * **KP_IMAGE_FORMAT_YCBCR422_CRY1CBY0** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x30

            YCbCr422 16bit (order: CrY1CbY0).

    * **KP_IMAGE_FORMAT_YCBCR422_CBY1CRY0** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x31

            YCbCr422 16bit (order: CbY1CrY0).

    * **KP_IMAGE_FORMAT_YCBCR422_Y1CRY0CB** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x32

            YCbCr422 16bit (order: Y1CrY0Cb).

    * **KP_IMAGE_FORMAT_YCBCR422_Y1CBY0CR** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x33

            YCbCr422 16bit (order: Y1CbY0Cr).

    * **KP_IMAGE_FORMAT_YCBCR422_CRY0CBY1** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x34

            YCbCr422 16bit (order: CrY0CbY1).

    * **KP_IMAGE_FORMAT_YCBCR422_CBY0CRY1** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x35

            YCbCr422 16bit (order: CbY0CrY1).

    * **KP_IMAGE_FORMAT_YCBCR422_Y0CRY1CB** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x36

            YCbCr422 16bit (order: Y0CrY1Cb).

    * **KP_IMAGE_FORMAT_YCBCR422_Y0CBY1CR** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x37

            YCbCr422 16bit (order: Y0CbY1Cr).

    * **KP_IMAGE_FORMAT_RAW8** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x20

            RAW 8bits (Grayscale).


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ModelTargetChip(value)
enum for model target chip.


* **Attributes**

    * **KP_MODEL_TARGET_CHIP_UNKNOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            Model for unknown chip.

    * **KP_MODEL_TARGET_CHIP_KL520** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            Model for KL520.

    * **KP_MODEL_TARGET_CHIP_KL720** : [`int`](https://docs.python.org/3/library/functions.html#int), default=2

            Model for KL720.

    * **KP_MODEL_TARGET_CHIP_KL530** : [`int`](https://docs.python.org/3/library/functions.html#int), default=3

            Model for KL530.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ModelTensorDataLayout(value)
enum for npu raw data layout format for tensors.


* **Attributes**

    * **KP_MODEL_TENSOR_DATA_LAYOUT_UNKNOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            Unknown NPU data layout.

    * **KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            Layout - width: 4  bits, channel: 4  bits, depth: 8  bits.

    * **KP_MODEL_TENSOR_DATA_LAYOUT_1W16C8B** : [`int`](https://docs.python.org/3/library/functions.html#int), default=2

            Layout - width: 1  bits, channel: 16 bits, depth: 8  bits.

    * **KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B** : [`int`](https://docs.python.org/3/library/functions.html#int), default=3

            Layout - width: 16 bits, channel: 4  bits, depth: 8  bits.

    * **KP_MODEL_TENSOR_DATA_LAYOUT_8W1C16B** : [`int`](https://docs.python.org/3/library/functions.html#int), default=4

            Layout - width: 8  bits, channel: 1  bits, depth: 16 bits.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.NormalizeMode(value)
enum for normalization mode.


* **Attributes**

    * **KP_NORMALIZE_DISABLE** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0xFF

            Disable normalize.

    * **KP_NORMALIZE_KNERON** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x1

            RGB/256 - 0.5, refer to the toolchain manual.

    * **KP_NORMALIZE_TENSOR_FLOW** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x2

            RGB/127.5 - 1.0, refer to the toolchain manual.

    * **KP_NORMALIZE_YOLO** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x3

            RGB/255.0, refer to the toolchain manual.

    * **KP_NORMALIZE_CUSTOMIZED_DEFAULT** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x4

            Customized, default, refer to the toolchain manual.

    * **KP_NORMALIZE_CUSTOMIZED_SUB128** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x5

            Customized, subtract 128, refer to the toolchain manual.

    * **KP_NORMALIZE_CUSTOMIZED_DIV2** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x6

            Customized, divide by 2, refer to the toolchain manual.

    * **KP_NORMALIZE_CUSTOMIZED_SUB128_DIV2** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x7

            Customized, subtract 128 and divide by 2, refer to the toolchain manual.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.PaddingMode(value)
enum for padding mode.


* **Attributes**

    * **KP_PADDING_DISABLE** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x1

            Disable padding in pre-process.

    * **KP_PADDING_CORNER** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x2

            Enable corner padding (padding right and bottom) in pre-process.

    * **KP_PADDING_SYMMETRIC** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x3

            Enable symmetric padding (padding right, left, top and bottom) in pre-process.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ProductId(value)
enum for USB PID(Product ID).


* **Attributes**

    * **KP_DEVICE_KL520** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x100

            Product ID of KL520.

    * **KP_DEVICE_KL720** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x720

            Product ID of KL720.

    * **KP_DEVICE_KL720_LEGACY** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x200

            Legacy Product ID of KL720.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ResetMode(value)
enum for reset mode.


* **Attributes**

    * **KP_RESET_REBOOT** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            Higheset level to reset Kneron device. Kneron device would disconnect after this reset.

    * **KP_RESET_INFERENCE** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            Soft reset - reset inference FIFO queue.

    * **KP_RESET_SHUTDOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=2

            Shut down Kneron device. For KL520, only useful if HW circuit supports (ex. 96 bord), dongle is not supported. For KL720, this function is not supported.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.ResizeMode(value)
enum for resize mode.


* **Attributes**

    * **KP_RESIZE_DISABLE** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x1

            Disable resize in pre-process.

    * **KP_RESIZE_ENABLE** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0x2

            Enable resize in pre-process.


<!-- !! processed by numpydoc !! -->

---
 
### **class** kp.UsbSpeed(value)
enum for USB speed mode.


* **Attributes**

    * **KP_USB_SPEED_UNKNOWN** : [`int`](https://docs.python.org/3/library/functions.html#int), default=0

            unknown speed.

    * **KP_USB_SPEED_LOW** : [`int`](https://docs.python.org/3/library/functions.html#int), default=1

            Low speed.

    * **KP_USB_SPEED_FULL** : [`int`](https://docs.python.org/3/library/functions.html#int), default=2

            Full speed.

    * **KP_USB_SPEED_HIGH** : [`int`](https://docs.python.org/3/library/functions.html#int), default=3

            High speed.

    * **KP_USB_SPEED_SUPER** : [`int`](https://docs.python.org/3/library/functions.html#int), default=4

            Super speed.


<!-- !! processed by numpydoc !! -->
