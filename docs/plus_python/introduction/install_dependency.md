# Installation

Verified platforms, OS and Python Version to run Kneron PLUS API:

| OS                            | Platform      | Python Version          |
|-------------------------------|---------------|-------------------------|
| Windows 10                    | x86_64 64-bit | 3.5-3.9 (x86_64 64-bit) |
| Ubuntu 18.04                  | x86_64 64-bit | 3.5-3.9 (x86_64 64-bit) |
| Raspberry Pi OS - Buster 10   | armv7l 32-bit | 3.5-3.9 (armv7l 32-bit) |

And the following sections in this chapter will provide the instructions for installing the tools and dependency python packages to the corresponding platform.

---

## 1. Install Python Package

- Upgrade pip (pip version >= 21.X.X):
    ```bash
    $ python -m pip install --upgrade pip
    ```

- Install the package with pip:
    ```bash
    $ # Please make sure your pip version >= 21.X.X before installing python packages.
    $ cd ./package/{platform}/
    $ pip install KneronPLUS-{version}-py3-none-any.whl
    ```

- Install the examples requirement package with pip:
    ```bash
    $ pip install opencv-python
    ```

- Common problem:  

    If pip install/run application fails, it may cause by using python 2.X as python interpreter. Please make sure the interpreter and pip is `Python 3` on the host:  

    ```bash
    # check pip version
    $ pip -V
    $ pip3 -V

    # check python interpreter version
    $ python -V
    $ python3 -V
    ```

    You also can install package by specify python interpreter by following scripts:  
    ```bash
    $ python -m pip install {package_path}
    # or
    $ python3 -m pip install {package_path}
    ```

## 2. Install Kneron AI Device Driver on Windows 10

There are three ways to install device driver to Windows:

- Kneron DFUT (Recommended)
- PLUS Example
- Zadig

#### 2.1 Using **Kneron DFUT** to Install Driver

Note: This feature is only provided in Kneron DFUT v1.3.0 and above.

- Please refer [Upgrade AI Device To KDP2](./upgrade_ai_device_to_kdp2.md#3-install-driver-for-windows) for the usage.

#### 2.2 Using **PLUS Example** to Install Driver

Note: This feature is only provided in Kneron PLUS v1.3.0 and above.

- Please refer [Run Example](./run_examples.md#2-install-driver-for-windows-example) for the usage.

#### 2.3 Using **Zadig** to Install Driver

- Download Zadig application from zadig.akeo.ie appropriate for Windows 10.
- Connect Kneron KL520/KL630/KL720 device to your PC.
- Run the Zadig application.

1. KL520

    - The application should detect Kneron KL520 device as "Kneron KL520" with USB ID
    "3231/0100" as shown below:

        ![](../imgs/zadig_install_kl520_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

2. KL630

    - The application should detect Kneron KL630 device as "Kneron KL630" with USB ID
    "3231/0630" as shown below:

        ![](../imgs/zadig_install_kl630_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

2. KL720

    - The application should detect Kneron KL720 device as "Kneron KL720" with USB ID
    "3231/0200" as shown below:

        ![](../imgs/zadig_install_kl720_driver.png)

    - Make sure that the Driver field, has WinUSB option selected.

    - Click "Install Driver" button.

    **Note**: After Upgrade Kneron KL720 to KDP2 (ex. via Kneron DFUT), you may need to re-install the driver of KL720, since the USB ID will be changed to "3231/0720".

## 3. Update Kneron AI Device USB Permission on Ubuntu/Raspberry Pi

 * Config USB permission on Ubuntu/Raspberry Pi
   ```bash
   $ sudo bash install_libusb.sh
   ```

 * Or add following rules in `/etc/udev/rules.d/10-local.rules` manually
   ```text
   SUBSYSTEM=="usb",ATTRS{product}=="Kneron KL520",ATTRS{idVendor}=="3231",ATTRS{idProduct}=="0100",MODE="0666"
   SUBSYSTEM=="usb",ATTRS{product}=="Kneron KL720l",ATTRS{idVendor}=="3231",ATTRS{idProduct}=="0200",MODE="0666"
   SUBSYSTEM=="usb",ATTRS{product}=="Kneron KL720",ATTRS{idVendor}=="3231",ATTRS{idProduct}=="0720",MODE="0666"
   SUBSYSTEM=="usb",ATTRS{product}=="Kneron KL630",ATTRS{idVendor}=="3231",ATTRS{idProduct}=="0630",MODE="0666"
   ```
   and apply the new rules by following commands (Or you may need to restart the service after rebooting the host PC)
   ```bash
   $ sudo udevadm control --reload-rules
   $ sudo udevadm trigger
   ```
