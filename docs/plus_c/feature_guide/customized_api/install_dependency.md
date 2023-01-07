# Install Dependency

the developing of customized api must be proceeded under OS Windows 10.

1. **MSYS2**

    - Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

    - Execute **MSYS2 MinGW 64-bit** to install dependancy.

        Note: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

        ```bash
        $ pacman -Syu
        $ pacman -S --needed base-devel mingw-w64-x86_64-toolchain
        $ pacman -S mingw-w64-x86_64-libusb
        $ pacman -S mingw-w64-x86_64-cmake
        $ pacman -S vim zip unzip
        ```

2. **Keil MDK version 5**

    - Download and install Keil MDK version 5 (at least MDK-Essential) from https://www2.keil.com/mdk5

    - This is used for building the firmware.

3. **Xtensa Xplorer**

    - Only required when developing ncpu firmware for KL720
    - Please refer [Xtensa Xplorer Overview](../../../720_2.0.0/sdk/xtensa.md) for the instruction of installation.

4. **Cross Compiler for KL630**

    - Only required when developing firmware for KL630

    - Download the latest **KL630_SDK_vXXX.zip** from <https://www.kneron.com/tw/support/developers/>. It is located at **KL620 SDK** section.
    - Unzip KL630_SDK_vXXX.zip
    - Please refer KLM5S3_Development_Environment_User_Guide.pdf in {KL630_SDK_TOP_FOLDER_PATH}/02_BSP/01_Documents
