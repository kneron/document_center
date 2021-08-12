# Write Model To Flash

**Note**: We run the examples below under OS Ubuntu 18.04.5 LTS with cmake version 3.10.2.

---

## 1. Introduction

The inference model must be loaded into Kneron AI dongle before the inference process.

There are two ways to load models:

- **Upload Model via USB**

    - The model file (.nef) can be uploaded to Kneron AI dongle using **kp_load_model_from_file\(\)**, a KP API, before inference.

    - For the usage, please refer examples related to inference.

- **Load Model from Flash**

    - The model file (.nef) is written in flash, and it can be loaded using **kp_load_model_from_flash\(\)**, a KP API, before inference.

    - The GUI or command line of **KneronDFUT** can be used for writing the model file into flash.

    - For the usage, please refer the example **kl520_demo_app_yolo_inference_flash_model** or **kl720_demo_app_yolo_inference_flash_model**.

**Note**: Only one model can be loaded, no matter it was uploaded via USB or loaded from flash. If you want to change the model, please reboot the Kneron AI dongle.

**Note**: Upload model via USB can be directly used without writting model into flash.

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

### 3.1 Use GUI to Write Model into AI Dongle

```bash
$ sudo ./KneronDFUT
```

1. Select **KL520** Tab.

2. Select the KL520 dongles to write model into.

3. Select **Update Model to Flash**

4. Manually choose **Model file**.

5. Push **Run** button.

    ![](../imgs/dfut_kl520_model.png)

### 3.2 Use Command Line to Write Model into AI Dongle

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

3. Write model into the selected KL520 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --model-to-flash ${MODEL_FILE_PATH} --port 133 -- type KL520
    ```

    ```bash
    Start Update Model to Device with Port Id 133

    ==== Update Model to Device with Port Id: 133 Succeeded ====
    ```

---

## 4. Write Model Into KL720

### 4.1 Use GUI to Write Model into AI Dongle

```bash
$ sudo ./KneronDFUT
```

1. Select **KL720** Tab.

2. Select the KL720 dongles to write model into.

3. Select **Update Model to Flash**

4. Manually choose **Model file**.

5. Push **Run** button.

    ![](../imgs/dfut_kl720_model.png)

### 4.2 Use Command Line to Write Model into AI Dongle

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

2. Write model into the selected KL720 dongles using the port id

    ```bash
    $ sudo ./KneronDFUT --model-to-flash ${MODEL_FILE_PATH} --port 262 --type KL720
    ```

    ```bash
    Start Update Model to Device with Port Id 262

    ==== Update Model to Device with Port Id: 262 Succeeded ====
    ```
