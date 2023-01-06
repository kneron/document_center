# Device DDR Management

## 1. Introduction

DDR space on Kneron AI device are used for placing the model, working buffers for calculation, and the buffers for usb transmitting (FIFO Queue buffers).

Kneron PLUS provides the flexibility to allow users customizing the configuration of few kinds of DDR buffers:

1. The size of buffer for the model

2. The quantity and size for buffers for receiving input data in usb transmitting

3. The quantity and size for buffers for sending output data in usb transmitting

## 2. Configuration

**Note**: DDR space of Kneron AI device can be configured only once before rebooting. The second configuration will be ignored.

### 2.1 Auto Configuration

In general, the quantity and the size of these buffers will be auto configured to the suitable value in `kp_load_model()`, `kp_load_encrypted_models()` and `kp_load_model_from_flash()`.

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

**Note 4**: After `kp_load_model()`, `kp_load_encrypted_models()` or `kp_load_model_from_flash()`, the DDR configuration will be loaded to `kp_ddr_manage_attr_t` in `kp_device_group_t`.

### 2.2 Customized Configuration

`kp_ddr_manage_attr_t` and `kp_store_ddr_manage_attr()` can be used for customizing the quantity or the size of these buffers.

```C
typedef struct
{
    uint32_t model_size;            /**< DDR space for model */
    uint32_t input_buffer_size;     /**< input buffer size for FIFO queue */
    uint32_t input_buffer_count;    /**< input buffer count for FIFO queue */
    uint32_t result_buffer_size;    /**< result buffer size for FIFO queue */
    uint32_t result_buffer_count;   /**< result buffer count for FIFO queue */
} __attribute__((aligned(4))) kp_ddr_manage_attr_t;
```

1. Each entry in `kp_ddr_manage_attr_t` can be customized configured, or auto configured if the value is set to 0.

2. `kp_ddr_manage_attr_t` must be prepared and stored into `kp_device_group_s` using `kp_store_ddr_manage_attr()` before calling `kp_load_model()`, `kp_load_encrypted_models()` or `kp_load_model_from_flash()`.

3. System has reserved 15 MB from DDR space for other working buffers.

4. If (System Reserved + Model Size + (Input Buffer Count x Input Buffer Size) + (Result Buffer Count x Result Buffer Size)) is larger than the available DDR space, the configuration will fail.

Please refer [Device FIFO Queue Config Example](../introduction/run_examples.md#17-device-fifo-queue-config-example) for the demonstration.
