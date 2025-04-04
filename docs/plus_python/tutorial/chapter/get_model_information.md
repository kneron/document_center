## Get Model Information on Kneron Device

This tutorial shows how to get model information from Kneron devices. NEF model is Kneron provided model format, which can combine multiple models in one NEF file. You can use `kp.core.get_model_info(device_group: DeviceGroup, usb_port_id: int)` to check models contain in uploaded NEF file.

**Note**: Please upload NEF model on Kneron device before the following tutorial. See the [Load NEF Model
](./load_nef_model.md) for details.

---

### Get model information of Kneron devices by *kp.core.get_model_info(device_group: DeviceGroup, usb_port_id: int)*:

```python
model_nef_descriptors = []

for usb_port_id in usb_port_ids:
    model_nef_descriptor = kp.core.get_model_info(device_group=device_group,
                                                  usb_port_id=usb_port_id)
    model_nef_descriptors.append(model_nef_descriptor)
```

---

### Simply show all information:

```python
print(model_nef_descriptors)

'''
[{
    "magic": "0x5AA55AA5",
    "metadata": {
        "kn_number": "0x0",
        "toolchain_version": "",
        "compiler_version": "v0.9.0(bf6cf311)",
        "nef_schema_version": {
            "version": "0.0.0"
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
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_4W4C8B",
                    "tensor_shape_info": {
                        "version": "ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1",
                        "data": {
                            "shape_npu": [
                                1,
                                3,
                                224,
                                224
                            ],
                            "shape_onnx": [
                                1,
                                3,
                                224,
                                224
                            ],
                            "axis_permutation_onnx_to_npu": [
                                0,
                                1,
                                2,
                                3
                            ]
                        }
                    },
                    "quantization_parameters": {
                        "version": "QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VERSION_1",
                        "data": {
                            "quantized_axis": 1,
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": {
                                        "dtype": "DataType.KP_DTYPE_FLOAT32",
                                        "value": 1.0
                                    },
                                    "radix": 8
                                }
                            }
                        }
                    }
                }
            },
            "output_nodes": {
                "0": {
                    "index": 0,
                    "name": "",
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                    "tensor_shape_info": {
                        "version": "ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1",
                        "data": {
                            "shape_npu": [
                                1,
                                255,
                                7,
                                7
                            ],
                            "shape_onnx": [
                                1,
                                255,
                                7,
                                7
                            ],
                            "axis_permutation_onnx_to_npu": [
                                0,
                                1,
                                2,
                                3
                            ]
                        }
                    },
                    "quantization_parameters": {
                        "version": "QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VERSION_1",
                        "data": {
                            "quantized_axis": 1,
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": {
                                        "dtype": "DataType.KP_DTYPE_FLOAT32",
                                        "value": 1.4717674255371094
                                    },
                                    "radix": 2
                                }
                            }
                        }
                    }
                },
                "1": {
                    "index": 1,
                    "name": "",
                    "data_layout": "ModelTensorDataLayout.KP_MODEL_TENSOR_DATA_LAYOUT_16W1C8B",
                    "tensor_shape_info": {
                        "version": "ModelTensorShapeInformationVersion.KP_MODEL_TENSOR_SHAPE_INFO_VERSION_1",
                        "data": {
                            "shape_npu": [
                                1,
                                255,
                                14,
                                14
                            ],
                            "shape_onnx": [
                                1,
                                255,
                                14,
                                14
                            ],
                            "axis_permutation_onnx_to_npu": [
                                0,
                                1,
                                2,
                                3
                            ]
                        }
                    },
                    "quantization_parameters": {
                        "version": "QuantizationParametersVersion.KP_MODEL_QUANTIZATION_PARAMS_VERSION_1",
                        "data": {
                            "quantized_axis": 1,
                            "quantized_fixed_point_descriptor_list": {
                                "0": {
                                    "scale": {
                                        "dtype": "DataType.KP_DTYPE_FLOAT32",
                                        "value": 1.4307060241699219
                                    },
                                    "radix": 2
                                }
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
            "max_raw_out_size": 86180
        }
    }
}]
'''
```