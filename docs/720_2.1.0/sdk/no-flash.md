# Support no-flash design and boot from USB

(KL720 only)

KL720 can be designed to boot up as a USB-DFU device.

When KL720 is in USB-DFU mode, we can use `Minion ` ( SDK/firmware/utils/minion/ ) to download firmware to KL720 internal ram space via USB port, therefore KL720 can boot from USB directly without external flash.

## 1. Minion


**Hardware**: 

[Set bootstrap](../flash_management/flash_management.md#24-bootstrap-settings) to manual boot `3. USB ` or boot from USB directly

**Driver installation**:

 `Minion ` uses libusb for usb access, so on Windows you have to register the device with the WinUSB driver, for more details please refer to Kneron Doc -> Kneron PLUS-c -> Introduction -> Install Dependency ->  section 2.1.3 .


**Examples**:

Please refer to `kneron_plus ` usb_dfu_scan_download() and _load_firmware_to_720() for more details.

Reference : Kneron Doc -> Kneron PLUS-C -> introduction -> run_examples_enterprise -> 7. Load Firmware through Usb for No-Flash Device


## 2. Firmware build with no-flash design

**Project.h**:

In `board setting ` section, please set FLASH_TYPE definition as FLASH_TYPE_NULL.

```bash
#define FLASH_TYPE                              FLASH_TYPE_NULL
```


**Remove flash related drivers**:

Please be noted that all the flash read/write functions are not allowed to be used in no-flash design.


![](../imgs/rm_flash_driver.png)




![](../imgs/rm_spif_driver.png)






