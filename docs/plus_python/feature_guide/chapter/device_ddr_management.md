# Device DDR Management

## 1. Introduction

DDR space on Kneron AI device are used for placing the model, working buffers for calculation, and the buffers for usb transmitting.

Kneron PLUS provides the flexibility to allow users customizing the configuration of few kinds of DDR buffers:

1. The size of buffer for the model

2. The quantity and size for buffers for receiving input data in usb transmitting

3. The quantity and size for buffers for sending output data in usb transmitting

## 2. Configuration

**Note**: DDR space of Kneron AI device can be configured only once before rebooting. The second configuration will be ignored.

### 2.1 Auto Configuration

In general, the quantity and the size of these buffers will be auto configured to the suitable value in `kp.core.load_model()`, `kp.core.load_encrypted_models()` and `kp.core.load_model_from_flash()`.

The value will be auto set to:

Buffer              | Category      | Auto Min                  | Auto Max                  | Note
------------------- | :------------ | :------------------------ | :------------------------ | :---
Model               | Size (Byte)   |                           |                           | The size that loaded models required
Receiving Input     | Quantity      | 2                         | 3                         |
Receiving Input     | Size (Byte)   | (1920 * 1080 * 2) + 1024  | (3840 * 2160 * 2) + 1024  | See Note 1 ~ 3
Sending Result      | Quantity      | 1                         | 3                         |
Sending Result      | Size (Byte)   |                           |                           | The size of the largest output raw data of loaded models

**Note 1**: (1920 * 1080 * 2) Bytes is the size for 2 channels of 1920 x 1080 image (RGB565)

**Note 2**: (3840 * 2160 * 2) Bytes is the size for 2 channels of 3840 x 2160 image (RGB565)

**Note 3**: 1024 Bytes is reserved for header size

**Note 4**: After `kp.core.load_model()`, `kp.core.load_encrypted_models()` or `kp.core.load_model_from_flash()`, the DDR configuration will be loaded to `kp.DdrManageAttributes` in `kp.DeviceGroup`.

### 2.2 Customized Configuration

`kp.DdrManageAttributes` and `kp.core.store_ddr_management_attributes()` can be used for customizing the quantity or the size of these buffers.

```python
class DdrManageAttributes(ValueBase, ValueRepresentBase):
    """
    DDR memory management descriptor of Kneron device.

    Attributes
    ----------
    model_size : int, default=0
        DDR space for model.
    input_buffer_size : int, default=0
        Input buffer size for FIFO queue.
    input_buffer_count : int, default=0
        Input buffer count for FIFO queue.
    result_buffer_size : kp.ModelNefDescriptor, default=kp.ModelNefDescriptor()
        Result buffer size for FIFO queue.
    result_buffer_count : int, default=0
        Result buffer count for FIFO queue.
    """
```

1. Each entry in `kp.DdrManageAttributes` can be customized configured, or auto configured if the value is set to 0.

2. `kp.DdrManageAttributes` must be prepared and stored into `kp.DeviceGroup` using `kp.core.store_ddr_management_attributes()` before calling `kp.core.load_model()`, `kp.core.load_encrypted_models()` or `kp.core.load_model_from_flash()`.

3. System has reserved 15 MB from DDR space for other working buffers.

4. If (System Reserved + Model Size + (Input Buffer Count x Input Buffer Size) + (Result Buffer Count x Result Buffer Size)) is larger than the available DDR space, the configuration will fail.

Please refer [6. Device Memory Usage Control Example](../../introduction/run_examples.md#6-device-memory-usage-control-example) for the demonstration.
