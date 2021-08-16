# Install Dependency

the developing of customized api must be proceeded under OS Windows 10.

1. **MSYS2**

    - Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

    - Execute **MSYS2 MinGW 64-bit** to install dependancy.

        ```bash
        $ pacman -Syu
        $ pacman -Sy
        $ pacman -S base-devel gcc vim cmake
        $ pacman -S mingw-w64-x86_64-libusb
        ```

2. **Keil MDK version 5**

    - Download and install Keil MDK version 5 (at least MDK-Essential) from https://www2.keil.com/mdk5

    - This is used for building the firmware.
