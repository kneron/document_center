## Scane All Kneron Device

This tutorial shows how to get USB information of Kneron devices.

### Import **`kp`** into your program:

```python
import kp
```

---

### Get USB information of Kneron devices by `kp.core.scan_devices()`:

```python
device_descriptors = kp.core.scan_devices()
```

---

### Simply show all information:

```python
print(device_descriptors)

'''
{
    "0": {
        "usb_port_id": 13,
        "vendor_id": "0x3231",
        "product_id": "0x100",
        "link_speed": "UsbSpeed.KP_USB_SPEED_HIGH",
        "kn_number": "0xC8062D2C",
        "is_connectable": true,
        "usb_port_path": "1-3",
        "firmware": "KDP2 Loader"
    }
}
'''
```