# Support no-flash design and boot from UART

(KL520 only)

KL520 can be designed to boot up as a UART XMODEM device.

When KL520 is in UART XMODEM interface, we can use `Minion `( SDK/firmware/utils/minion/ ) to download firmware to KL520 internal ram space via UART0 port, therefore KL520 can be designed without external flash.

## 1. Minion


**Hardware**: 

[Set bootstrap](../flash_management/flash_management.md#24-set-bootstrap-settings-to-manual-boot-mode-program-flash-via-uart0-interface) to manual boot `2. UART(Xmodem) ` or boot from UART directly


**Examples**: 

Please refer to `kneron_plus ` kl520_uart_boot_firmware example for more details.

Reference : Kneron Doc -> Kneron PLUS-C -> introduction -> run_examples_enterprise -> 6. Load Firmware through UART 


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






