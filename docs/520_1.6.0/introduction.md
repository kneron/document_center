# Introduction

**note:** KL520 SDK v1.6.x starts to support Kneron PLUS

## 1. Requirements

**Hardware**:

Board with KL520 chip, like 520 dongle, 96board, m.2 board

(For applications with camera) Kneron KL520 series AI SoC Development Kit

**Software:**

licensed software: [ARM Keil MDK](https://www.keil.com)

[ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)


## 2. [File Structure](./sdk/file_structure.md)

The whole SDK package is composed of device firmware, the folder design is described in this section.

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
