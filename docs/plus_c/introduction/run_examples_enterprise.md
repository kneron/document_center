# Run Examples for Kneron PLUS Enterprise

Other than the examples briefed in [Run Examples](./run_examples.md), Kneron PLUS Enterprise also provides few examples for demonstrating the usage of advanced features.

**Note**: Please build [Kneron PLUS](./build_plus.md) first.

**Note**: If you are using Windows, please execute all the instruction below in MSYS2 MinGW 64-bit.

**Note**: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

**Note**: In the inference related examples, we are using KL520 for most demo. If you wish to use KL630, KL720, or KL730, just change the prefix of the example name from kl520 to kl630, kl720, or kl730. (There might be no KL520 version, KL630 version, KL720 version, or KL730 version on certain examples.)

**Note**: Few examples will auto connect multiple devices to run inference. If you put hybrid types of devices on host, the inference may fail.

**Note**: If you modify code to change different test image file. Input image aspect ratio is suggested to be aligned to model input aspect ratio.

---

## 1. Update KDP Firmware to KDP2 USB Boot (KL520 only)

This example is to show how to connect a Kneron AI device in KDP firmware via `kp_connect_device()`, and the sequence of `kp_load_firmware_from_file()`, `kp_update_kdp2_usb_loader_from_file()` and `kp_switch_to_kdp2_usb_boot()` to update Kneron AI device from KDP firmware to KDP2 USB boot.

```bash
$ sudo ./kl520_update_kdp_to_kdp2_usb_boot
```

```bash
connect device ... succeeded, return code: 0
update to kdp2 usb loader ... succeeded, return code: 0
upload to kdp2 firmware ... succeeded, return code: 0
switch to kdp2 usb boot ... succeeded, return code: 0
disconnecting device ...
```

---

## 2. Update KDP2 Firmware to KDP2 USB Boot (KL520 only)

This example is to show the sequence of `kp_load_firmware_from_file()` and `kp_switch_to_kdp2_usb_boot()` to update Kneron AI device from KDP2 firmware (both USB boot and Flash boot are acceptable) to KDP2 Usb boot.

```bash
$ ./kl520_update_kdp2_to_kdp2_usb_boot
```

```bash
connect device ... OK
upload firmware ... OK
update to kdp2 usb boot ... OK
```

---

## 3. Update KDP Firmware to KDP2 Flash Boot

This example is to show how to connect a Kneron AI device in KDP firmware via `kp_connect_device()`, and the sequence of `kp_update_kdp2_usb_loader_from_file()`, `kp_load_firmware_from_file()` and `kp_update_kdp2_firmware_from_files()` to update Kneron AI device from KDP firmware to KDP2 Flash boot.

```bash
$ sudo ./kl520_update_kdp_to_kdp2_flash_boot
```

```bash
connect device ... succeeded, return code: 0
update to kdp2 usb boot ... succeeded, return code: 0
upload firmware ... succeeded, return code: 0
update to kdp2 flash boot ... succeeded, return code: 0
disconnecting device ...
```

---

## 4. Update KDP2 Firmware to KDP2 Flash Boot

This example is to show the sequence of `kp_load_firmware_from_file()` and `kp_update_kdp2_firmware_from_files()` to update Kneron AI device from KDP2 firmware (both Usb boot and Flash boot are acceptable) to KDP2 Flash boot.

```bash
$ ./kl520_update_kdp2_to_kdp2_flash_boot
```

```bash
connect device ... OK
upload firmware ... OK
update kdp2 firmware ... OK
```

---

## 5. Update Model to Flash

This example is to show the usage of `kp_update_model_from_file()` to update the model into Kneron AI device's flash.

```bash
$ sudo ./kl520_update_flash_model
```

```bash
connect device ... OK
upload firmware ... OK
update model ... OK
```

---

## 6. Load Firmware through UART (KL520 only)

Note: After device is reset, the firmware is required to be loaded again.

This example shows the usage of loading firmware into device via UART instead of loading through USB or loading from Flash.

No matter loading firmware through USB or from Flash, we need the flash of Kneron AI device to assist the process.

For those who does not import the flash module, loading firmware through UART would be the best solution.

```bash
$ sudo ./kl520_uart_boot_firmware ${COM_PORT_IDX}
```

```bash
com port number \\.\COM5 !!......
To program
 > SCPU FW: ../../res/firmware/KL520/fw_scpu.bin
 > NCPU FW: ../../res/firmware/KL520/fw_ncpu.bin

opening serial port successfulGetCommState successful!
SetCommState 115200 successful!
GetCommState successful!
Please press RESET btn!!......
sent 2 successful
Sending Minion through XModem...
Xmodem successfully transmitted 2688 bytes
SetCommState 115200 successful!
SetCommState 921600 successful
Writing KDP2 flag value at 0x10100100
Sending SCPU bin to addr 0x10104000...
Sending NCPU bin to addr 0x28000000...
Run code from addr 0x10104000...
SetCommState 115200 successful!
SetCommState 115200 successful

[0.000]
[0.000] starting KDP2 middleware ...
[0.000] creating image queue with size 10
[0.000] creating result queue with size 10
[0.000] KDP2 FW is running in flash-boot mode
[0.000] boot ncpu fw from flash
kdp2 ncpu: Ready!


CloseHandle...
```

---

## 7. Load Firmware through Usb for No-Flash Device


This example is to show the usage of `kp_load_firmware_from_file()` for loading firmware via Usb to Kneron AI device without extern flash.

```bash
$ sudo ./kl720_usb_boot_firmware
```

```bash
connect device ... OK
upload firmware ... OK

kn_number:    0x2504142C
FW_version:   2.0.0-build.517
```

---

## 8. Read / Write Device Memory

This example is to show the usage of `kp_memory_read()` and `kp_memory_write()` for reading or writing a given size of data in Kneron AI device memory.

- For reading data from memory:

    ```bash
    $ sudo ./memory_read_write -target KL520 -port auto -mode read -addr 0x60000000 -len 200704 -file mem_read.bin
    ```

    ```bash
    -target: [target platform] (KL520, KL720) = KL520
    -sidx  : [scan index] = auto (auto or specified scan index), only for single device
    -port  : [port id] = auto (auto or specified port id), only for single device
            Notice that scan index has higher priority than port id
    -mode  : [read write mode] (read, write) = read
    -addr  : [start_address] (32 bit value) = 0x60000000
    -len   : [length of data] (in byte, no need to input in write mode) = 200704
    -data  : [data] (raw hex in byte, please quote it with "",
                    no need to input in read mode or write mode from file) = invalid
    -file  : [file path] (file path to store read back data from FW memory
                        or write all data in file to FW memory) = mem_read.bin

    connect target: index '0', port ID '133'
    connect device ... OK

    memory read ... OK
    output to file done

    disconnecting device ...
    ```

- For writing data to memory:

    ```bash
    $ sudo ./memory_read_write -target KL520 -port auto -mode write -addr 0x60000000 -data mem_write.bin
    ```

    ```bash
    -target: [target platform] (KL520, KL720) = KL520
    -sidx  : [scan index] = auto (auto or specified scan index), only for single device
    -port  : [port id] = auto (auto or specified port id), only for single device
            Notice that scan index has higher priority than port id
    -mode  : [read write mode] (read, write) = write
    -addr  : [start_address] (32 bit value) = 0x60000000
    -len   : [length of data] (in byte, no need to input in write mode) = 1
    -data  : [data] (raw hex in byte, please quote it with "",
                    no need to input in read mode or write mode from file) = 0x0,
    -file  : [file path] (file path to store read back data from FW memory
                        or write all data in file to FW memory) = invalid

    connect target: index '0', port ID '133'
    connect device ... OK

    memory write ... OK

    disconnecting device ...
    ```

---

## 9. Access Firmware Log via USB

This example is to show the usage of `kp_enable_firmware_log()` and `kp_disable_firmware_log()` for enabling and disabling the firmware log via USB.

```bash
$ ./kl720_demo_generic_image_inference_print_log.exe
```

```bash
connect device ... OK
upload model ... OK
[0.326]USB is connected
read image ... OK

starting inference loop 100 times:
..........................................[5.000]Current TDC Temperature is about [55]
..........................................................

inference loop is done
```

---

## 10. HICO Camera Inference (KL720 only)

**Note**: (hardware)96-Board with KL720 11x11 chip is required.

**Note**: (hardware)**Kneron LW 3D module** is required.

**Note**: (firmware)HICO mode is a special firmware different from the regular one. (**KL720_SDK/firmware/build/solution_kdp2_hico_mipi**)

In most of the previous examples, we introduced the usage of the software side to send image to device and receive the inference result from device via USB.

However, Kneron PLUS provides the **HICO mode** (Host In Companion Out) to make the Kneron AI device directly obtain the image to inference from the camera connected to the device. Software side can receive the inference result and the inference image from the device via USB under the **HICO mode**.

This example is using MIPI camera and to demonstrate the usage of activating HICO process and showing the images and inference results received from the device.

```bash
$ sudo ./kl720_demo_hico_cam_inference
```

![](../imgs/hico_camera_inference.png)

---

## 11. HICO TOF Camera Inference (KL720 only)

**Note**: This feature and example are only provided in Kneron PLUS v1.3.0 and above.

**Note**: (hardware)96-Board with KL720 11x11 chip is required.

**Note**: (hardware)**TOF_ISR** and converter board are required.

**Note**: (firmware)HICO mode is a special firmware different from the regular one. (**KL720_SDK/firmware/build/solution_kdp2_hico_tof**)

Similar to *HICO Camera Inference* example, this example is using TOF camera and to demonstrate object detection plus decoding for depth and NIR image from TOF raw data.

The decoder function for depth and NIR image is in a pre-build firmware library. To use the function, please study the details in FW/ncpu part.

```bash
$sudo ./kl720_demo_hico_tof_inference
```

![](../imgs/hico_tof.png)
