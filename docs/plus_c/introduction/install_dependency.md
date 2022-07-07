# Install Dependency

Verified platforms and OS to build and run PLUS:

- Windows 10 (x86_64 64-bit)
- Ubuntu 18.04 (x86_64 64-bit)
- Raspberry Pi OS - Buster (armv7l 32-bit)

And the following sections in this chapter will provide the instructions for installing the tools and dependency libraries to the corresponding platform.


---


## 1. Ubuntu 18.04 / Raspberry Pi OS - Buster

- Install required packages

    ```bash
    $ sudo apt install cmake
    $ sudo apt install libusb-1.0-0-dev
    $ sudo apt install build-essential
    ```

---

## 2. Windows 10

### 2.1 Kneron AI Device Driver

There are three ways to install device driver to Windows:

- Kneron DFUT (Recommended)
- PLUS Example
- Zadig

#### 2.1.1 Using **Kneron DFUT** to Install Driver

Note: This feature is only provided in Kneron DFUT v1.3.0 and above.

- Please refer [Upgrade AI Device To KDP2](./upgrade_ai_device_to_kdp2.md#3-install-driver-for-windows) for the usage.
#### 2.1.2 Using **PLUS Example** to Install Driver

Note: This feature is only provided in Kneron PLUS v1.3.0 and above.

- Please refer [Run Example](./run_examples.md#13-install-driver-for-windows-example) for the usage.

#### 2.1.3 Using **Zadig** to Install Driver

- Download Zadig application from zadig.akeo.ie appropriate for Windows 10.
- Connect Kneron KL520/KL720 device to your PC.
- Run the Zadig application.

1. KL520

    - The application should detect Kneron KL520 device as "Kneron KL520" with USB ID
    "3231/0100" as shown below:

        ![](../imgs/zadig_install_kl520_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

2. KL720

    - The application should detect Kneron KL720 device as "Kneron KL720" with USB ID
    "3231/0200" as shown below:

        ![](../imgs/zadig_install_kl720_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

    **Note**: After Upgrade Kneron KL720 to KDP2 (ex. via Kneron DFUT), you may need to re-install the driver of KL720, since the USB ID will be changed to "3231/0720".



### 2.2 **MSYS2**

- Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

- Execute **MSYS2 MinGW 64-bit** to install dependance.

    Note: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

    ```bash
    $ pacman -Syu
    $ pacman -S --needed base-devel mingw-w64-x86_64-toolchain
    $ pacman -S mingw-w64-x86_64-libusb
    $ pacman -S mingw-w64-x86_64-cmake
    $ pacman -S vim zip unzip
    ```

### 2.3 OpenCV

Kneron Plus provides few examples which are using OpenCV to demonstrate the inference usage with the input of web camera.
To build and run these examples, you need to install OpenCV.

#### 2.3.1 Install Pre-build OpenCV

This section will show how to install the pre-build opencv downloaded from [OpenCV-MinGW-Build](https://github.com/huihut/OpenCV-MinGW-Build).

- Execute **MSYS2 MinGW 64-bit** to build OpenCV

    Note: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

    ```bash
    $ wget https://github.com/huihut/OpenCV-MinGW-Build/archive/refs/tags/OpenCV-3.4.8-x64.zip
    $ unzip OpenCV-3.4.8-x64.zip
    $ mv OpenCV-MinGW-Build-OpenCV-3.4.8-x64 /c/opencv_348
    $ rm OpenCV-3.4.8-x64.zip
    ```

- Add OpenCV into environment value

    - Open "this computer", right click on blank, and choose "Properties".
    ![](../imgs/windows_this_computer.png)

    - Click "Advanced system settings" on the left panel.
    ![](../imgs/windows_system.png)

    - Click "Environment Variables".
    ![](../imgs/windows_system_properties.png)

    - Add "OpenCV_DIR" and set the value to "C:\opencv_348".
    ![](../imgs/windows_add_opencv_path_for_pre_build.png)

    - Edit "Path", and add "%OpenCV_DIR%\x64\mingw\bin" and "%OpenCV_DIR%".
    ![](../imgs/windows_add_opencv_lib_path.png)

- Change properties of MSYS2
    ```bash
    $ cd /
    $ vim msys2_shell.cmd
    ```

    On line 17, change
    ```bash
    rem set MSYS2_PATH_TYPE=inherit
    ```
    to
    ```bash
    set MSYS2_PATH_TYPE=inherit
    ```

- Close and execute **MSYS2 MinGW 64-bit**


#### 2.3.2 Self Build OpenCV

This section will show how to build and install OpenCV from source code.

- Execute **MSYS2 MinGW 64-bit** to build OpenCV

    Note: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

    ```bash
    $ cd /c/
    $ mkdir opencv_348
    $ cd opencv_348

    $ wget https://github.com/opencv/opencv/archive/3.4.8.zip
    $ unzip 3.4.8.zip
    $ rm 3.4.8.zip
    $ mv opencv-3.4.8 opencv

    $ wget https://github.com/opencv/opencv_contrib/archive/3.4.8.zip
    $ unzip 3.4.8.zip
    $ rm 3.4.8.zip
    $ mv opencv_contrib-3.4.8 opencv_contrib

    $ cd opencv
    $ mkdir build
    $ cd build/
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE  -D WITH_CUDA=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D INSTALL_C_EXAMPLES=OFF -D BUILD_EXAMPLES=OFF -D BUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF -D WITH_GSTREAMER=OFF -D WITH_LIBV4L=ON -D ENABLE_PRECOMPILED_HEADERS=OFF -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules .. -G "MSYS Makefiles"
    $ make -j4
    $ make install
    ```

- Add OpenCV into environment value

    - Open "this computer", right click on blank, and choose "Properties".
    ![](../imgs/windows_this_computer.png)

    - Click "Advanced system settings" on the left panel.
    ![](../imgs/windows_system.png)

    - Click "Environment Variables".
    ![](../imgs/windows_system_properties.png)

    - Add "OpenCV_DIR" and set the value to "C:\opencv_348\opencv\build\install".
    ![](../imgs/windows_add_opencv_path.png)

    - Edit "Path", and add "%OpenCV_DIR%\x64\mingw\bin" and "%OpenCV_DIR%".
    ![](../imgs/windows_add_opencv_lib_path.png)

- Change properties of MSYS2
    ```bash
    $ cd /
    $ vim msys2_shell.cmd
    ```

    On line 17, change
    ```bash
    rem set MSYS2_PATH_TYPE=inherit
    ```
    to
    ```bash
    set MSYS2_PATH_TYPE=inherit
    ```

- Close and execute **MSYS2 MinGW 64-bit**
