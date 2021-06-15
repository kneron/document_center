# Run Customized Examples

**Note**: We built and run the examples below under OS Windows 10 (19041.1052), Keil uVision5 (5.27.1.0), MSYS2 MinGW 64-bit (20210419), and cmake version 3.20.2.

## 1. Build Firmware

1. Execute Keil uVision5

2. Select **Project** > **Open Project...**

3. Choose {PLUS_FOLDER_PATH}/firmware_development/KL520/example_projects/kdp2_companion_user_ex/workspace.uvmpw

4. Expand **Project: kdp2_scpu** in left panel

5. Right click on **app** and choose **Add Existing Files to Group 'kdp2_inference'...**

6. Select {PLUS_FOLDER_PATH}/firmware_development/KL520/scpu_kdp2/app/my_example_inf.c

7. Select **Project** > **Batch Build**

*If build succeeded, **kdp2_fw_scpu.bin** and **kdp2_fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL520/

![](../imgs/keil_build_firmware.png)

## 2. Build PLUS

Build PLUS in **MSYS2 MinGW 64-bit**

```bash
$ cd {PLUS_FOLDER_PATH}
$ mkdir build
$ cd build
$ cmake .. -G "MSYS Makefiles"
$ make -j
```

## 2. Run Example

### 2.1 Run Single Model Example

```bash
$ cd bin
$ sudo ./my_sin_example.exe
```

### 2.2 Run Multiple Models Example

```bash
$ cd bin
$ sudo ./my_mul_example.exe
```
