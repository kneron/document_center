# Run Customized Examples

**Note**: We built and run the examples below under OS Windows 10 (19041.1052), Keil uVision5 (5.27.1.0), Xtensa Xplorer (8.0.11), MSYS2 MinGW 64-bit (20210419), and cmake version 3.20.2.

---

## 1. Build Firmware

### 1.1 KL520 SCPU and NCPU
1. Execute Keil uVision5

2. Select **Project** > **Open Project...**

3. Choose {PLUS_FOLDER_PATH}/firmware_development/KL520/firmware/build/solution_kdp2_user_ex/sn52096/proj.uvmpw

4. Expand **Project: scpu** and **dev** in left panel

5. Right click on **inf_app** and choose **Add Existing Files to Group 'inf_app'...**

6. [optional] Select {PLUS_FOLDER_PATH}/firmware_development/KL520/firmware/app/my_kl520_sin_example_inf.c

7. [optional] Select {PLUS_FOLDER_PATH}/firmware_development/KL520/firmware/app/my_kl520_mul_example_inf.c

8. Select **Project** > **Batch Build**

*If build succeeded, **fw_scpu.bin** and **fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL520/

![](../../imgs/keil_build_kl520_firmware.png)

### 1.2 KL630 Firmware

```bash
$ cd {KL630_SDK_FOLDER_PATH}/apps/vmf_nnm
$ bash build.sh
```

*If build succeeded, **kp_firmware.tar** will be put into {KL630_SDK_FOLDER_PATH}/apps/vmf_nnm/bin/

*For further information of building firmware of KL630, please refer **Vienna_NNM_Example_User_Guide.pdf** in {KL630_SDK_TOP_FOLDER_PATH}/03_SDK/01_Documents/

### 1.3 KL720 SCPU
1. Execute Keil uVision5

2. Select **Project** > **Open Project...**

3. Choose {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/build/solution_kdp2_user_ex/sn72096_9x9/proj.uvmpw

4. Expand **Project: scpu** and **dev** in left panel

5. Right click on **inf_app** and choose **Add Existing Files to Group 'inf_app'...**

6. [optional] Select {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/app/my_kl720_sin_example_inf.c

7. [optional] Select {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/app/my_kl720_mul_example_inf.c

8. Select **Project** > **Batch Build**

*If build succeeded, **fw_scpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL720/

![](../../imgs/keil_build_kl720_firmware.png)

### 1.4 KL720 NCPU (Using Xtensa GUI)
1. Execute Xtensa Xplorer

2. Select {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/build/ncpu_bin/kl720_ncpu as workspace

![](../../imgs/xtensa_select_workspace.png)

3. Close the welcome page

4. Right click on **Project Explorer** and choose **Import**

![](../../imgs/xtensa_start_import.png)

5. Select General -> Existing Projects into Workspace

![](../../imgs/xtensa_existing_project.png)

6. Click Browse and click confirm directly

![](../../imgs/xtensa_import.png)

7. Click Finish

![](../../imgs/xtensa_import_finish.png)

8. [optional] Remove the **Hello World** Project

9. Choose **main** as active project

![](../../imgs/xtensa_main.png)

10. Choose **vp6_asic**

![](../../imgs/xtensa_vp6.png)

11. [optional] Drag the new files you added (eg. user_pre_process.c) into src folder

![](../../imgs/xtensa_add_src.png)

12. Click Build or Rebuild Active

![](../../imgs/xtensa_build.png)

*If build succeeded, **fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL720/

### 1.5 KL720 NCPU (Using CMake Script)

**Note**: Xtensa Xplorer must be installed with default path, `C:\user\Xtensa`

**Note**: Modify tool path in `{PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/build/ncpu_bin/xcc/toolenv.sh` if the install path is not the same as above

**Note**: Please run build script on **MSYS2 MinGW 64-bit**

**Note**: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

```bash
$ cd {PLUS_FOLDER_PATH}/firmware_development/KL720/firmware/build/ncpu_bin/xcc
$ source envtool.sh

$ bash build.sh release
or
$ bash build.sh debug
```

*If build succeeded, **fw_ncpu.bin** will be put into {PLUS_FOLDER_PATH}/res/firmware/KL720/

### 1.5 KL730 Firmware

```bash
$ cd {KL730_SDK_FOLDER_PATH}/apps/vmf_nnm
$ bash build.sh
```

*If build succeeded, **kp_firmware.tar** will be put into {KL730_SDK_FOLDER_PATH}/apps/vmf_nnm/bin/

*For further information of building firmware of KL730, please refer **Leipzig_NNM_Example_User_Guide.pdf** in {KL730_SDK_TOP_FOLDER_PATH}/03_SDK/01_Documents/

---

## 2. Build PLUS

Build PLUS in **MSYS2 MinGW 64-bit**

Note: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

```bash
$ cd {PLUS_FOLDER_PATH}
$ mkdir build
$ cd build
$ cmake .. -G"MSYS Makefiles"
$ make -j
```

## 2. Run Example

### 2.1 Run KL520 Single Model Example

```bash
$ cd bin
$ sudo ./my_kl520_sin_example.exe
```

### 2.2 Run KL520 Multiple Models Example

```bash
$ cd bin
$ sudo ./my_kl520_mul_example.exe
```

### 2.3 Run KL630 Single Model Example

```bash
$ cd bin
$ sudo ./my_kl630_sin_example.exe
```

### 2.4 Run KL630 Multiple Models Example

```bash
$ cd bin
$ sudo ./my_kl630_mul_example.exe
```

### 2.5 Run KL720 Single Model Example

```bash
$ cd bin
$ sudo ./my_kl720_sin_example.exe
```

### 2.6 Run KL720 Multiple Models Example

```bash
$ cd bin
$ sudo ./my_kl720_mul_example.exe
```
### 2.7 Run KL730 Single Model Example

```bash
$ cd bin
$ sudo ./my_kl730_sin_example.exe
```

### 2.8 Run KL730 Multiple Models Example

```bash
$ cd bin
$ sudo ./my_kl730_mul_example.exe
```
