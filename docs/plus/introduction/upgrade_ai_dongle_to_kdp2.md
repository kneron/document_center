# Upgrade AI Dongle to KDP2

**Note**: KneronDFUT has supported 3 platforms - Windows 10, Ubuntu 18.04, and Raspberry Pi 4

**Note**: We run the examples below under OS Ubuntu 18.04.5 LTS with cmake version 3.10.2.

**Note**: Downgrading Kneron AI dongle to previous KDP firmware is not allowed.


## 1. Introduction

**KDP2 Firmware** is the firmware designed for KP APIs in PLUS. Using KDP2 Firmware allows Kneron AI dongle performing corresponding operation requested by PLUS.

There are two kinds of KDP2 firmware are provided:

- **[KL520] Runtime Upload Firmware**

    - This kind of firmware are using usb to be uploaded and activated before inference process.

    - This kind of firmware requires the firmware loader in flash to assist the upload and activation for firmware.

    - The firmware loader can be written to flash memory via the GUI or command line of **KneronDFUT**.

    - The firmware can be uploaded via **kp_load_firmware_from_file()**, a KP API, before inference.

- **[KL720] Firmware in Flash Memory**

    - This kind of firmware are stored in the flash memory of Kneron AI dongles.

    - Once the AI dongle is electrified, the firmware will be automatically activated.

    - This kind of firmware can be written to flash memory via the GUI or command line of **KneronDFUT**.

## 2. [KL520] Write Firmware Loader into Flash Memory

Download the KneronDFUT_ubuntu.zip into Ubuntu from https://www.kneron.com/tw/support/developers/.

```bash
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

### 2.1 Use GUI to Update AI Dongle

```bash
$ sudo ./KneronDFUT
```

1. Select **KL520** Tab.

2. Select the KL520 dongles to be update to KDP2 firmware loader.

3. Push **Run** button.

![](../imgs/dfut_upgrade_firmware_loader.png)


### 2.2 Use Command Line to Update AI Dongle

1. Show help message
    ```bash
    $ sudo ./KneronDFUT --help

        [Display help message]
            --help                : [no argument]         help message

        [Scan and list all information]
            --list                : [no argument]         list all dongles information

        [Update dongles to usb loader] (Only works for KL520)
            --usb                 : [no argument]         choose update to Usb Loader
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Update firmware file to flash memory in dongles
            --type                : [argument required]   type of firmware ("KL520" or "KL720")
            --scpu                : [argument required]   self pointed scpu firmware file path (.bin)
            --ncpu                : [argument required]   selp pointed ncpu firmware file path (.bin)
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Enable Graphic User Interface]
            --gui                 : [no argument]         display GUI
    ```

2. List all dongles

    ```bash
    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        517
        Kn Number:      0x270A265C
        Device Type:    KL520
        FW Type:        KDP
        Connectable:    true
        ===========================================
    ```

3. Upgrade the selected KL520 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --port 517 --usb

        Start Update Device with Port Id 517 to USB Loader

        ==== Update of Device with Port Id: 517 Succeeded ====
    ```

## 3. [KL720] Write Firmware into Flash Memory

Download the KneronDFUT_ubuntu.zip into Ubuntu from https://www.kneron.com/tw/support/developers/. It is located at **Kneron PLUS** section.

```bash
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

### 3.1 Use GUI to Update AI Dongle

```bash
$ sudo ./KneronDFUT
```

1. Select **KL720** Tab.

2. Select the KL720 dongles to be update to KDP2 firmware.

3. Manually choose **SCPU firmware file** and **NCPU firmware file**.

4. Push **Run** button.

![](../imgs/dfut_upgrade_firmware_flash.png)

### 3.2 Use Command Line to Update AI Dongle

1. Show help message
    ```bash
    $ sudo ./KneronDFUT --help

        [Display help message]
            --help                : [no argument]         help message

        [Scan and list all information]
            --list                : [no argument]         list all dongles information

        [Update dongles to usb loader] (Only works for KL520)
            --usb                 : [no argument]         choose update to Usb Loader
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Update firmware file to flash memory in dongles
            --type                : [argument required]   type of firmware ("KL520" or "KL720")
            --scpu                : [argument required]   self pointed scpu firmware file path (.bin)
            --ncpu                : [argument required]   selp pointed ncpu firmware file path (.bin)
            --port                : [argument required]   port id set ("all", "auto" or specified multiple port ids "13,537")

        [Enable Graphic User Interface]
            --gui                 : [no argument]         display GUI
    ```

2. List all dongles

    ```bash
    $ sudo ./KneronDFUT --list

        ===========================================
        Index:          1
        Port Id:        273
        Kn Number:      0x2004142C
        Device Type:    KL720
        FW Type:        KDP
        Connectable:    true
        ===========================================
    ```

3. Upgrade the selected KL720 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --port 273 --type KL720 --scpu ${SCPU_FILE} --ncpu ${NCPU_FILE}

        Start Update Firmware to Device with Port Id 273

        ==== Update Firmware to Device with Port Id: 273 Succeeded ====
    ```
