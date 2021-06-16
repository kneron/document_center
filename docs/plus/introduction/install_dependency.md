# Install Dependency

Currently, only few platform and OS are supported to build and run PLUS:

- Windows 10
- Ubuntu 18.04
- Raspberry Pi 4

And the following sections in this chapter will provide the instructions for installing the tools and dependancy libraries to the correponding platform.

## 1. Ubuntu 18.04 / Raspberry Pi 4

1. Install **CMake**, **libusb-1.0.0-dev** and **build-essential**.

    ```bash
    $ sudo apt install cmake
    $ sudo apt install libusb-1.0-0-dev
    $ sudo apt install build-essential
    ```

## 2. Windows 10

1. Kneron AI Dongle Driver

    - Download Zadig application from zadig.akeo.ie appropriate for Windows 10.

    - Connect Kneron KL520 device to your PC.

    - Run the Zadig application.

    - The application should detect Kneron KL520 device as "Kneron KL520" with USB ID
"3231/0100" as shown below (USB ID will be 3231/0200 if KL720 is used):

        ![](../imgs/zadig_install_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

2. **MSYS2**

    - Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

    - Execute **MSYS2 MinGW 64-bit** to install dependancy.

        ```bash
        $ pacman -Syu
        $ pacman -Sy
        $ pacman -S base-devel gcc vim cmake
        $ pacman -S mingw-w64-x86_64-libusb
        ```