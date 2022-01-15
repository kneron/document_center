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
    "crc": "0x6CBF1FF9",
    "num_models": 1,
    "models": {
        "0": {
            "id": 19,
            "max_raw_out_size": 85752,
            "width": 224,
            "height": 224,
            "channel": 3,
            "img_format": "ImageFormat.KP_IMAGE_FORMAT_RGBA8888"
        }
    }
}]
'''
```