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
}
'''
```