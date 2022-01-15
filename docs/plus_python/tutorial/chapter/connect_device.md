## Connect to Kneron device

This tutorial shows how to connect to Kneron devices and get Kneron device handler (Device Group).

### Import **`kp`** into your program:

```python
import kp
```

---

### Get Kneron device USB port IDs for connecting:
Device Group is Kneron device handler, which supports multiple `same product ID` Kneron devices connection ability. 

1. Get **`USB port ID`** of KL520 devices by `kp.core.scan_devices()`
    ```python
    target_device_type = kp.ProductId.KP_DEVICE_KL520
    usb_port_ids = []
    
    device_descriptors = kp.core.scan_devices()

    for device_descriptor in device_descriptors.device_descriptor_list:
        if target_device_type == device_descriptor.product_id and \
           device_descriptor.is_connectable:
            usb_port_ids.append(device_descriptor.usb_port_id)
    ```

2. Connect to Kneron device by **`kp.core.connect_devices(usb_port_ids=List[int])`**  
    - Connect one Kneron device
        ```python
        device_group = kp.core.connect_devices(usb_port_ids=[usb_port_ids[0]])
        ```

    - Connect multiple Kneron devices  
        Note: Multiple Kneron devices connection ability only supports the **same product ID Kneron devices**. Please check your USB port IDs have the same product ID before **`kp.core.connect_devices(usb_port_ids=List[int])`**. 
        ```python
        device_group = kp.core.connect_devices(usb_port_ids=usb_port_ids)
        ```