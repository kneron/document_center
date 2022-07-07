## Upload SCPU/NCPU Firmware

This tutorial shows how to upload SCPU nad NCPU Frimware to Kneron devices in following two ways:  

1. [Upload firmware by file path](#upload-firmware-by-file-path)  
2. [Upload firmware by binary data](#upload-firmware-by-binary-data)  

**Note 1**: Please connect Kneron device and get **`Device Group`** before the following tutorial. See the [Connect to Kneron device
](./connect_device.md) for details.  

**Note 2**: **`load_firmware_from_file`** and **`load_firmware`** only support Kneron KL520 USB-Boot firmware. If you want to update Kneron KL520/KL720 Flash-Boot firmware, please see the [Upgrade AI Device to KDP2
](../../introduction/upgrade_ai_device_to_kdp2.md) for details.  

### Upload firmware by file path
> Please replace `SCPU_FW_PATH`, `NCPU_FW_PATH` by fw_scpu.bin and fw_ncpu.bin path (Please find target device firmware under `res/firmware` folder)  

```python
SCPU_FW_PATH = 'res/firmware/KL520/fw_scpu.bin'
NCPU_FW_PATH = 'res/firmware/KL520/fw_ncpu.bin'

kp.core.load_firmware_from_file(device_group=device_group,
                                scpu_fw_path=SCPU_FW_PATH,
                                ncpu_fw_path=NCPU_FW_PATH)
```

### Upload firmware by binary data
> Please replace `SCPU_FW_PATH`, `NCPU_FW_PATH` by fw_scpu.bin and fw_ncpu.bin path (Please find target device firmware under `res/firmware` folder)  

```python
SCPU_FW_PATH = 'res/firmware/KL520/fw_scpu.bin'
NCPU_FW_PATH = 'res/firmware/KL520/fw_ncpu.bin'

with open(SCPU_FW_PATH, 'rb') as file:
    scpu_fw_buffer = file.read()

with open(NCPU_FW_PATH, 'rb') as file:
    ncpu_fw_buffer = file.read()

kp.core.load_firmware(device_group=device_group,
                      scpu_fw_buffer=scpu_fw_buffer,
                      ncpu_fw_buffer=ncpu_fw_buffer)
```
