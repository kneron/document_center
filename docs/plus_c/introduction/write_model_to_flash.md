# Write Model To Flash

**Note**: KneronDFUT supports 3 platforms - Windows 10 (x86_64 64-bit), Ubuntu 18.04 (x86_64 64-bit), and Raspberry Pi OS - Buster (armv7l 32-bit)

**Note**: If you are not using the 3 platforms, you may use the DFUT_console provided in Kneron PLUS. Please refer [Build with DFUT_console](../../plus_c/introduction/build_plus.md#23-build-with-dfutconsole)

**Note**: Please use the latest version of KneronDFUT to avoid problems caused by incompatibility.

## 1. Introduction

The inference model must be loaded into Kneron AI device before the inference process.

There are two ways to load models:

- **Upload Model via USB**

    - The model file (.nef) can be uploaded to Kneron AI device using `kp_load_model_from_file()`, a KP API, before inference.

    - For Python users, the model file (.nef) can be uploaded to Kneron AI device using `kp.core.load_model_from_file()`.

    - For the usage, please refer examples related to inference.

    - In this method, the size of the model in device DDR memory (larger than NEF file size) must be below **35 MB** for KL520, and **75 MB** for KL720.

- **Load Model from Flash**

    - The model file (.nef) is written in flash, and it can be loaded using `kp_load_model_from_flash()`, a KP API, before inference.

    - For Python users, the model file (.nef) is written in flash, and it can be loaded using `kp.core.load_model_from_flash()`.

    - The GUI or command line of **KneronDFUT** can be used for writing the model file into flash.

    - For the usage, please refer the example **kl520_demo_generic_inference_flash_model** or **kl720_demo_generic_inference_flash_model**.

    - For Python users, please refer the example **KL520DemoGenericInferenceFlashModel.py** or **KL720DemoGenericInferenceFlashModel.py**.

    - In this method, the size of the model file must be below **32 MB** for KL520, and **70 MB** for KL720.

**Note**: Only one model file (.nef) can be loaded, no matter it was uploaded via USB or loaded from flash. If you want to change the model, please reboot the Kneron AI device.

**Note**: Upload model via USB can be directly used without writing model into flash.

---

## 2. Download Kneron DFUT

Download the KneronDFUT_ubuntu.zip into Ubuntu from  https://www.kneron.com/tw/support/developers/. It is located at **Kneron PLUS** section.

```bash
$ unzip KneronDFUT_ubuntu.zip
$ cd Kneron_DFUT/bin/
```

Show help message
```bash
$ sudo ./KneronDFUT --help
```

---

## 3. Write Model Into KL520

### 3.1 Use GUI to Write Model into AI Device

```bash
$ sudo ./KneronDFUT
```

1. Select **KL520** Tab.

2. Select the KL520 devices to write model into.

3. Select **Update Model to Flash**

4. Manually choose **Model file**.

5. Push **Run** button.

    ![](../imgs/dfut_kl520_model.png)

### 3.2 Use Command Line to Write Model into AI Device

1. List all devices

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

3. Write model into the selected KL520 devices using the port id

    ```bash
    $ sudo ./KneronDFUT --model-to-flash ${MODEL_FILE_PATH} --port 133 -- type KL520
    ```

    ```bash
    Start Update Model to Device with Port Id 133

    ==== Update Model to Device with Port Id: 133 Succeeded ====
    ```

---

## 4. Write Model Into KL720

### 4.1 Use GUI to Write Model into AI Device

```bash
$ sudo ./KneronDFUT
```

1. Select **KL720** Tab.

2. Select the KL720 devices to write model into.

3. Select **Update Model to Flash**

4. Manually choose **Model file**.

5. Push **Run** button.

    ![](../imgs/dfut_kl720_model.png)

### 4.2 Use Command Line to Write Model into AI Device

1. List all devices

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

2. Write model into the selected KL720 devices using the port id

    ```bash
    $ sudo ./KneronDFUT --model-to-flash ${MODEL_FILE_PATH} --port 262 --type KL720
    ```

    ```bash
    Start Update Model to Device with Port Id 262

    ==== Update Model to Device with Port Id: 262 Succeeded ====
    ```
