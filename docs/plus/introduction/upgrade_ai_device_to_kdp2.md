# Upgrade AI Device to KDP2 Firmware

**Note**: KneronDFUT supports 3 platforms - Windows 10 (x86_64 64-bit), Ubuntu 18.04 (x86_64 64-bit), and Raspberry Pi OS - Buster (armv7l 32-bit)

**Note**: Please use the latest version of KneronDFUT to avoid problems caused by incompatibility.

**Note**: Downgrading Kneron AI device to previous KDP firmware is not allowed.

**Note**: If the Kneron AI device you wish to upgrade is running HICO firmware, please manually reset the device first before the update process.

---

## 1. Introduction

**KDP2 Firmware** is the firmware designed for KP APIs in PLUS. Using KDP2 Firmware allows Kneron AI device performing corresponding operation requested by PLUS.

There are two modes to activate KDP2 firmware in Kneron AI device:

- **Runtime Upload Firmware (USB Boot)**

    - USB boot mode is only available on **KL520**.

    - USB boot mode is using usb to upload KDP2 firmware before the inference process.

    - Uploading firmware requires the assistance from the loader firmware("**KDP2 loader**") in flash memory.

    - The GUI or command line of **KneronDFUT** can be used for writing the loader firmware to flash memory and switch AI devices to USB boot mode.

    - After writing the loader firmware and switching device to USB boot mode, The KDP2 firmware can be uploaded via **kp_load_firmware_from_file()**, a KP API, before inference.


- **Firmware in Flash Memory (Flash Boot)**

    - This mode is using the **KDP2 firmware** stored in the flash memory of AI devices.

    - Once the AI device is electrified, the firmware will be automatically activated.

    - The GUI or command line of **KneronDFUT** can be used for writing KDP2 firmware to flash memory and switch AI devices to Flash boot mode.

---

## 2. Download Kneron DFUT

Download the KneronDFUT_ubuntu.zip into Ubuntu from  https://www.kneron.com/tw/support/developers/. It is located at **Kneron PLUS** section.

```bash
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

Commnand line usage
```bash
$ sudo ./KneronDFUT --help
```

```bash
[Display help message]
    --help                : [no argument]         help message

[Scan and list all information]
    --list                : [no argument]         list all dongles information

[Update dongles to usb boot] (Only works for KL520)
    --kl520-usb-boot      : [no argument]         choose update to Usb Boot
    --port                : [argument required]   port id set ("all" or specified multiple port ids "13,537")

[Update dongles to flash boot] (Only works for KL520)
    --kl520-flash-boot    : [no argument]         choose update to Flash Boot
    --port                : [argument required]   port id set ("all" or specified multiple port ids "13,537")
    --scpu                : [argument required]   self pointed scpu firmware file path (.bin)
    --ncpu                : [argument required]   self pointed ncpu firmware file path (.bin)

[Update firmware file to flash memory in dongles (Only works for KL720)
    --kl720-update        : [no argument]         choose write firmware to flash memory
    --port                : [argument required]   port id set ("all" or specified multiple port ids "13,537")
    --scpu                : [argument required]   self pointed scpu firmware file path (.bin)
    --ncpu                : [argument required]   self pointed ncpu firmware file path (.bin)

[Update model file to flash memory in dongles
    --model-to-flash      : [argument required]   self pointed model file path (.nef)
    --type                : [argument required]   type of device ("KL520" or "KL720")
    --port                : [argument required]   port id set ("all" or specified multiple port ids "13,537")

[Enable Graphic User Interface]
    --gui                 : [no argument]         display GUI

[Get Current Kneron DFUT Version]
    --version             : [no argument]         display the version of Kneron DFUT
```

---

## 3. [KL520] Update to USB Boot Mode

### 3.1 Use GUI to Update AI Device

```bash
$ sudo ./KneronDFUT
```

1. Select **KL520** Tab.

2. Select the KL520 dongles to be update to USB Boot Mode.

3. Select **Update to USB Boot**

4. Push **Run** button.

    ![](../imgs/dfut_kl520_usb_boot.png)


### 3.2 Use Command Line to Update AI Device

1. List all dongles

    ```bash
    $ sudo ./KneronDFUT --list
    ```

    ```bash
    ===========================================
    Index:          1
    Port Id:        133
    Kn Number:      0x270A265C
    Device Type:    KL520
    FW Type:        KDP
    Usb Speed:      High-Speed
    Connectable:    true
    ===========================================
    ```

2. Upgrade the selected KL520 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --kl520-usb-boot --port 133
    ```

    ```bash
    Start Update Device with Port Id 133 to USB Boot

    ==== Update of Device with Port Id: 133 Succeeded ====

    ```


---

## 4. [KL520] Update to Flash Boot Mode

### 4.1 Use GUI to Update AI Device
```bash
$ sudo ./KneronDFUT
```

1. Select **KL520** Tab.

2. Select the KL520 dongles to be **Update to Flash Boot** Mode.

3. Select **Update to Flash Boot**

4. Manually choose **SCPU firmware file** and **NCPU firmware file**.

    SCPU and NCPU firmware file for KL520 can be found in **${PLUS_FOLDER}/res/firmware/KL520/**

5. Push **Run** button.

    ![](../imgs/dfut_kl520_flash_boot.png)

### 4.2 Use Command Line to Update AI Device

1. List all dongles

    ```bash
    $ sudo ./KneronDFUT --list
    ```

    ```bash
    ===========================================
    Index:          1
    Port Id:        133
    Kn Number:      0x270A265C
    Device Type:    KL520
    FW Type:        KDP
    Usb Speed:      High-Speed
    Connectable:    true
    ===========================================
    ```

2. Upgrade the selected KL520 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --kl520-flash-boot --port 133 --scpu ${SCPU_FILE_PATH} --ncpu ${NCPU_FILE_PATH}
    ```

    ```bash
    Start Update Device with Port Id 133 to Flash Boot

    ==== Update of Device with Port Id: 133 Succeeded ====
    ```

    SCPU and NCPU firmware file for KL520 can be found in **${PLUS_FOLDER}/res/firmware/KL520/**

---

## 5. [KL720] Update Firmware to Flash Memory


**Note**: Update flash for KL720 is required under USB3.0\(Super-Speed) model

### 5.1 Use GUI to Update AI Device

```bash
$ sudo ./KneronDFUT
```

1. Select **KL720** Tab.

2. Select the KL720 dongles to be update to KDP2 firmware.

3. Select **Update Firmware to Flash**

4. Manually choose **SCPU firmware file** and **NCPU firmware file**.

    The firmware files can be found in **${PLUS_FOLDER}/res/firmware/KL720/**

5. Push **Run** button.

    ![](../imgs/dfut_kl720_firmware.png)

### 5.2 Use Command Line to Update AI Device

1. List all dongles

    ```bash
    $ sudo ./KneronDFUT --list
    ```

    ```bash
    ===========================================
    Index:          1
    Port Id:        262
    Kn Number:      0x2004142C
    Device Type:    KL720
    FW Type:        KDP
    Usb Speed:      Super-Speed
    Connectable:    true
    ===========================================
    ```

2. Upgrade the selected KL720 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --kl720-update --port 262 --scpu ${SCPU_FILE_PATH} --ncpu ${NCPU_FILE_PATH}
    ```

    ```bash
    Start Update Firmware to Device with Port Id 262

    ==== Update Firmware to Device with Port Id: 262 Succeeded ====
    ```

    SCPU and NCPU firmware file for KL720 can be found in **${PLUS_FOLDER}/res/firmware/KL720/**
