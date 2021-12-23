# Introduction

**note:** KL520 SDK v1.7.x is compatible with Kneron PLUS v1.3.x

## 1. Requirements

**Hardware**:

Board with KL520 chip, like 520 dongle, 96board, m.2 board

(For applications with camera) Kneron KL520 series AI SoC Development Kit

**Software:**

licensed software: [ARM Keil MDK](https://www.keil.com)

[ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)


## 2. File Structure

The whole SDK package is composed of device firmware, the folder design is described below

```txt
.
├── common                              # common interface between SCPU/NCPU
├── example_projects
│   ├── kdp2_companion_user_ex          # Keil project for Kneron PLUS user example
│   ├── tiny_yolo_v3_host               # Keil project for host mode(Standalone) firmware example
│   └── tiny_yolo_v3_host_usbout        # Keil project for host mode with outputing result vis usb
├── platform
│   └── kl520
│       ├── common                      # part of common interface between SCPU/NCPU 
│       ├── ncpu       
│       |   ├── drv                     # drivers 
│       |   ├── rtos/rtx                # cloned rtos/rtx code
│       |   └── startup                 # startup assembly code, and FW init code
│       └── scpu
│           ├── drv                     # peripheral drivers
│           ├── rtos/rtx                # cloned rtos/rtx code
│           └── startup                 # startup assembly code, and FW init code
├── ncpu
│   ├── device                          # device configurations
│   ├── lib                             # folder for libraries
│   └── project
│       └── tiny_yolo_v3                # ncpu project
├── scpu
│   ├── board                           # for device board configurations
│   ├── config                          # for device board configurations
│   ├── device                          # device memory address configurations
│   ├── drivers                         # system drivers
│   ├── framework                       # framework layer code
│   ├── kdev                            # device driver code
│   ├── kmdw                            # middleware
│   ├── lib                             # folder for libraries
│   └── project
│       └── tiny_yolo_v3                 
│           ├── host                    # Keil project for host mode firmware example
│           └── host_usbout             # Keil project for host mode with outputing result vis usb
├── ncpu_kdp2
│   ├── lib_app                         # folder for kdp2-ncpu-app.lib
│   ├── lib_sdk                         # folder for kdp2-ncpu-sdk.lib
│   └── project
│       └── ncpu_companion_user_ex      # Keil project for Kneron PLUS user example
├── scpu_kdp2
│   ├── app                             # application layer code for Kneron PLUS firmware example
│   ├── lib_sdk                         # kdp2_scpu_sdk.lib folder
│   └── project
│       └── scpu_companion_user_ex      # Keil project for Kneron PLUS example
├── models
│   └── tiny_yolo_v3                    # model file for demo
├── sdkexamples                         # driver examples
└── utils                               # firmware/model utilities
```

## 3. [Flash_Management](./flash_management/flash_management.md)

Flash Programming by UART, JLink.

## 4. SoC Peripheral Drivers

KL520 also provides some simple examples to show how to use basic peripherals such as, I2C, PWM, DMA, GPIO...
User can find them from `sdkexamples` folder.

There is also a PDF file to briefly describe the peripheral APIs. Please download it from the following link:
[KL520_Peripheral_Driver_APIs.pdf](./pdf/KL520_Peripheral_Driver_APIs.pdf)

### Supported/Unsupported Peripheral Table

**Image Input**

| Peripherals           | Companion     | Host Mode         |
| --------------------- | ------------- | ----------------- |
| MIPI CSI RX           | x             | O                 |
| DVP                   | x             | driver/example    |
| UVC Host              | x             | specified cameras |
| USB(proprietary)      | O             | x                 |
| SPI Master, non-DMA   | x             | driver/example    |
| SPI Slave, non-DMA    | x             | driver/example    |
| SPI Master, DMA       | x             | x                 |
| SPI Slave, DMA        | x             | x                 |
| UART                  | x             | x                 |


**Image/Result Output**

| Peripherals           | Companion     | Host Mode         |
| --------------------- | ------------- | ----------------- |
| MIPI DSI TX           | x             | x                 |
| MIPI CSI TX           | x             | x                 |
| DVP                   | x             | O                 |
| UVC device            | x             | x                 |
| USB bulk              | x             | O                 |
| USB(proprietary)      | O             | x                 |
| SPI Master, non-DMA   | x             | driver/example    |
| SPI Slave, non-DMA    | x             | driver/example    |
| SPI Master, DMA       | x             | x                 |
| SPI Slave, DMA        | x             | x                 |
| UART                  | x             | O                 |
| I2C                   | x             | driver/example    |
| I2S                   | x             | x                 |
| INTEL 8080            | x             | x                 |



## [Appendix](./sdk/appendix.md)

**host mode example** and **host mode with USB output example** are shown
