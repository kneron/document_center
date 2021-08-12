# Install Dependency

Verifed platforms and OS to build and run PLUS:

- Windows 10 (x86_64 64-bit)
- Ubuntu 18.04 (x86_64 64-bit)
- Raspberry Pi OS - Buster (armv7l 32-bit)

And the following sections in this chapter will provide the instructions for installing the tools and dependancy libraries to the correponding platform.


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

### 2.1 Kneron AI Dongle Driver

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

    **Note**: After Upgrade Kneron KL720 to KDP2, you may need to reinstall the driver of KL720, since the USB ID will be changed to "3231/0720".



### 2.2 **MSYS2**

- Download and install the latest **MSYS2** into Windows from <https://www.msys2.org/>.

- Execute **MSYS2 MinGW 64-bit** to install dependancy.

    ```bash
    $ pacman -Syu
    $ pacman -Sy
    $ pacman -S base-devel gcc vim cmake
    $ pacman -S mingw-w64-x86_64-libusb
    ```
