# Run Examples for Enterprise

Other than the examples briefed in [Run Examples](./run_examples.md), Kneron PLUS Enterprise also provides few examples for demonstrating the usage of advanced features.

**Note 1**: In the inference related examples, we are using KL520 for most demo. If you wish to use KL630 or KL720, just change the prefix of the example name from kl520 to kl630 or kl720. (There might be no KL520 version, KL630 version or KL720 version on certain examples.)

**Note 2**: Few examples will auto connect multiple devices to run inference. If you put hybrid types of devices on host, the inference may fail.

**Note 3**: If you modify code to change different test image file. Input image aspect ratio is suggested to be aligned to model input aspect ratio.

## 1. Update KDP2 Firmware to KDP2 Flash Boot

This example is to show the sequence of `kp.core.load_firmware_from_file()` and `kp.core._update_kdp2_firmware_from_file()` to update Kneron AI device from KDP2 firmware (both Usb boot and Flash boot are acceptable) to KDP2 Flash boot.

```bash
$ python3 KL520UpdateKdp2ToKdp2FlashBoot.py

[Connect Device]
 - Success
[Upload Firmware]
 - Success
[Update Firmware]
 - Success
```

* **Note**: Firmware Update Support Table

    | Origin Firmware | Target Firmware           | Kneron DFUT | C API | Python API |
    | --------------- | ------------------------- | ----------- | ----- | ---------- |
    | KDP             | KDP2 USB-Boot(KL520 Only) | Yes         | Yes   |            |
    | KDP             | KDP2 Flash-Boot           | Yes         | Yes   |            |
    | KDP2 USB-Boot   | KDP2 Flash-Boot           | Yes         | Yes   | Yes        |
    | KDP2 Flash-Boot | KDP2 USB-Boot(KL520 Only) | Yes         | Yes   |            |
    | KDP2 Flash-Boot | KDP2 Flash-Boot           | Yes         | Yes   | Yes        |