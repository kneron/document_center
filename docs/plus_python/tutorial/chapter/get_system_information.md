## Get System Information on Kneron Device

This tutorial shows how to get system information from Kneron devices.

**Note**: Please upload firmware on Kneron device before the following tutorial. See the [Upload SCPU/NCPU Firmware
](./upload_firmware.md) for details.


---

### Get system information of Kneron devices by *kp.core.get_system_info(device_group: DeviceGroup, usb_port_id: int)*:

```python
system_infos = []

for usb_port_id in usb_port_ids:
    system_info = kp.core.get_system_info(device_group=device_group,
                                          usb_port_id=usb_port_id)
    system_infos.append(system_info)
```

---

### Simply show all information:

```python
print(system_infos)

'''
[{
    "kn_number": "0xC8062D2C",
    "firmware_version": "1.5.0-build.113"
}]
'''
```