## Load NEF Model

This tutorial shows how to load NEF model to Kneron devices in the following three ways:  

1. [Upload NEF model by file path](#upload-nef-model-by-file-path)  
2. [Upload NEF model by binary data](#upload-nef-model-by-binary-data)  
3. [Load NEF model from device flash](#load-nef-model-from-device-flash)  

**Note**: Please upload firmware on Kneron device before the following tutorial. See the [Upload SCPU/NCPU Firmware
](./upload_firmware.md) for details.  

---

### Upload NEF model by file path
> Please replace `MODEL_FILE_PATH` by models_520.nef path (Please find target device NEF model under `res/models` folder)

```python
MODEL_FILE_PATH = 'res/models/KL520/tiny_yolo_v3/models_520.nef'

model_nef_descriptor = kp.core.load_model_from_file(device_group=device_group,
                                                    file_path=MODEL_FILE_PATH)
```

---

### Upload NEF model by binary data
> Please replace `MODEL_FILE_PATH` by models_520.nef path (Please find target device NEF model under `res/models` folder)

```python
MODEL_FILE_PATH = 'res/models/KL520/tiny_yolo_v3/models_520.nef'

with open(MODEL_FILE_PATH, 'rb') as file:
    nef_buffer = file.read()

model_nef_descriptor = kp.core.load_model(device_group=device_group,
                                          nef_buffer=nef_buffer)
```

---

### Load NEF model from device flash
> Please update NEF model in device flash by **`Kneron DFUT`** before `load_model_from_flash`. Reference chapter [**`Write Model To Flash`**](../../introduction/write_model_to_flash.md) for more information.

```python
model_nef_descriptor = kp.core.load_model_from_flash(device_group=device_group)
```

---

### Simply show **`ModelNefDescriptor`** information:

```python
print(model_nef_descriptor)

'''
{
    "magic": "0x5AA55AA5",
    "metadata": {
        "kn_number": "0x0",
        "toolchain_version": "",
        "compiler_version": "v0.9.0(bf6cf311)",
        "nef_schema_version": {
            "version": "0.9.0"
        },
        "platform": "USB dongle"
    },
    "target_chip": "ModelTargetChip.KP_MODEL_TARGET_CHIP_KL520",
    "crc": "0x6CBF1FF9",
    "models": {
        "0": {
            "target_chip": "ModelTargetChip.KP_MODEL_TARGET_CHIP_KL520",
            "version": "0x1",
            "id": 19,
            "input_nodes": {
                "0": {
                    "index": 0,
                    "name": "",
                    "shape_npu": [
                        1,
                        3,
                        224,
                        224
                    ],
                    "shape_onnx": [],
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B",
                    "quantization_parameters": {
                        "quantized_fixed_point_descriptor_list": {
                            "0": {
                                "scale": 1.0,
                                "radix": 8
                            }
                        }
                    }
                }
            },
            "output_nodes": {
                "0": {
                    "index": 0,
                    "name": "",
                    "shape_npu": [
                        1,
                        255,
                        7,
                        7
                    ],
                    "shape_onnx": [],
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                    "quantization_parameters": {
                        "quantized_fixed_point_descriptor_list": {
                            "0": {
                                "scale": 1.4717674255371094,
                                "radix": 2
                            }
                        }
                    }
                },
                "1": {
                    "index": 1,
                    "name": "",
                    "shape_npu": [
                        1,
                        255,
                        14,
                        14
                    ],
                    "shape_onnx": [],
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                    "quantization_parameters": {
                        "quantized_fixed_point_descriptor_list": {
                            "0": {
                                "scale": 1.4307060241699219,
                                "radix": 2
                            }
                        }
                    }
                }
            },
            "setup_schema_version": {
                "version": "0.0.0"
            },
            "setup_file_schema_version": {
                "version": "0.0.0"
            },
            "max_raw_out_size": 86076
        }
    }
}
'''
```
