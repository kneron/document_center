# kp.core

<!-- !! processed by numpydoc !! -->

---
 
### kp.core.connect_devices(usb_port_ids)
To connect multiple (including one) Kneron devices.


* **Parameters**

    * **usb_port_ids** : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)]

            An list contains device’s port ID which can be known from scan_devices(), if [0] is given then it will
            try to connect first connectable device.



* **Returns**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`DeviceGroup`](value.md#kp.DeviceGroup)



---
 
### kp.core.connect_devices_without_check(usb_port_ids)
To connect multiple (including one) Kneron devices without any examinations of system info.


* **Parameters**

    * **usb_port_ids** : `List`[[`int`](https://docs.python.org/3/library/functions.html#int)]

            An list contains device’s port ID which can be known from scan_devices(), if [0] is given then it will
            try to connect first connectable device.



* **Returns**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            Represents a set of devices handle.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`DeviceGroup`](value.md#kp.DeviceGroup)



---
 
### kp.core.disable_firmware_log(device_group)
Disable firmware log of all devices with firmware log enabled.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.disconnect_devices(device_group)
To disconnect a Kneron device.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.enable_firmware_log(device_group, usb_port_id, log_file_path)
Enable firmware log from certain device.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **usb_port_id** : [`int`](https://docs.python.org/3/library/functions.html#int)

            The device port ID to enable firmware log.

    * **log_file_path** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

            The log file output path.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.get_model_info(device_group, usb_port_id)
Get model information (crc, model id, etc.).


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **usb_port_id** : [`int`](https://docs.python.org/3/library/functions.html#int)

            Specific device port ID.



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.get_system_info(device_group, usb_port_id)
Get system information (kn number and firmware version).


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **usb_port_id** : [`int`](https://docs.python.org/3/library/functions.html#int)

            Specific device port ID.



* **Returns**

    * **system_info** : [`kp.SystemInfo`](value.md#kp.SystemInfo)

            SystemInfo object for describing the system information of specific device.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`SystemInfo`](value.md#kp.SystemInfo)



---
 
### kp.core.get_version()
Get Kneron PLUS version


* **Returns**

    * **plus_version_string** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

            Kneron PLUS version string.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



---
 
### kp.core.install_driver_for_windows(product_id)
Install device driver on Windows


* **Parameters**

    * **product_id** : [`kp.ProductId`](enum.md#kp.ProductId)

            enum for USB PID(Product ID).



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.load_encrypted_models(device_group, nef_buffer_list)
Upload encrypted NEF models data bytes to device through USB.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **nef_buffer_list** : `List`[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]

            A list of byte buffer that contains the content of encrypted NEF file(s).



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.load_encrypted_models_from_file(device_group, file_path_list)
Upload encrypted NEF Models to device through USB by encrypted NEF file path(s).


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **file_path_list** : `List`[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]

            A list of encrypted NEF model file path(s).



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * `ApiKPException`


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.load_firmware(device_group, scpu_fw_buffer, ncpu_fw_buffer)
Upload firmware data bytes to device through USB.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **scpu_fw_buffer** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)

            A bytes buffer contains the content of SCPU firmware file.

    * **ncpu_fw_buffer** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)

            A bytes buffer contains the content of NCPU firmware file.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.load_firmware_from_file(device_group, scpu_fw_path, ncpu_fw_path)
Upload firmware to device through USB by firmware file path.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **scpu_fw_path** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

            SCPU firmware file path.

    * **ncpu_fw_path** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

            NCPU firmware file path.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.load_model(device_group, nef_buffer)
Upload NEF models data bytes to device through USB.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **nef_buffer** : [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)

            A bytes buffer contains the content of NEF file.



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.load_model_from_file(device_group, file_path)
Upload NEF Model to device through USB by NEF file path.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **file_path** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

            NEF model file path.



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * `ApiKPException`


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.load_model_from_flash(device_group)
Load model from device flash (Please update NEF model in flash by Kneron DFUT).


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.



* **Returns**

    * **model_nef_descriptor** : [`kp.ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)

            ModelNefDescriptor object for describing the uploaded models.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`ModelNefDescriptor`](value.md#kp.ModelNefDescriptor)



---
 
### kp.core.reset_device(device_group, reset_mode, sleep_secs=0)
Reset the device in hardware mode or software mode.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **reset_mode** : [`kp.ResetMode`](enum.md#kp.ResetMode)

            Refer to ResetMode.

    * **sleep_secs** : [`float`](https://docs.python.org/3/library/functions.html#float)

            Set sleep time in seconds for reboot device.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.scan_devices()
Scan all Kneron devices and report a list.
This function can get devices connectivity information at runtime.


* **Returns**

    * **device_descriptor_list** : [`kp.DeviceDescriptorList`](value.md#kp.DeviceDescriptorList)

            DeviceDescriptorList object, contain information of connected devices from USB perspectives.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`DeviceDescriptorList`](value.md#kp.DeviceDescriptorList)



---
 
### kp.core.set_timeout(device_group, milliseconds)
To set a global timeout value for all USB communications with the device.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **milliseconds** : [`int`](https://docs.python.org/3/library/functions.html#int)

            Pre-set timeout value in milliseconds.


<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)



---
 
### kp.core.store_ddr_management_attributes(device_group, ddr_manage_attributes)
(Advance) Store DDR memory management attributes into DeviceGroup.


* **Parameters**

    * **device_group** : [`kp.DeviceGroup`](value.md#kp.DeviceGroup)

            A set of devices handle.

    * **ddr_manage_attributes** : [`kp.DdrManageAttributes`](value.md#kp.DdrManageAttributes)

            DDR memory management descriptor of Kneron device.



* **Raises**

    * [`kp.ApiKPException`](exception.md#kp.ApiKPException)


* **Notes**  
Must reset-reboot device before setting the DDR memory management attributes.
Must issue kp.core.store_ddr_management_attributes before kp.core.load_model()/kp.core.load_model_from_file()/kp.core.load_encrypted_models()/kp.core.load_encrypted_models_from_file()/kp.core.load_model_from_flash

<!-- !! processed by numpydoc !! -->

* **Return type**

    [`None`](https://docs.python.org/3/library/constants.html#None)
