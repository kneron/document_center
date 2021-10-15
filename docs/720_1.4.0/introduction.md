# Introduction

## 1. Requirements

**Hardware**:

Board with KL720 chip, like 720 dongle, 96board, m.2 board.

**Software:**

licensed software: [ARM Keil MDK](https://www.keil.com)

[ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)

## 2. [File Structure](sdk/file_structure.md)
The whole SDK package is composed of device firmware, the folder design is described in this section.

## 3. [Flash Management](flash_management/flash_management.md)
Flash Programming by UART, JLink.

## 4. Create New SDK Application
Step by step to create new SDK application, please refer to the section **Kneron PLUS / Customized API**.

## 5. [Secure Boot](sdk/secure_boot.md)
Kneron KL720 provide secure protect with AES and SHA.

## 6. [SOC Peripheral Drivers](sdk/soc_peripheral_drivers.md)
The peripheral definitions and prototypes for the application progamming reference.

### Supported/Unsupported Peripheral Table

**Image Input**

| Peripherals           | Companion     | HICO              |
| --------------------- | ------------- | ----------------- |
| MIPI CSI RX           | x             | driver/example    |
| DVP                   | x             | driver/example    |
| UVC Host              | x             | specified cameras |
| USB(proprietary)      | O             | x                 |
| SPI Master, non-DMA   | x             | driver/example    |
| SPI Slave, non-DMA    | x             | driver/example    |
| SPI Master, DMA       | x             | x                 |
| SPI Slave, DMA        | x             | x                 |
| UART                  | x             | x                 |


**Image/Result Output**

| Peripherals           | Companion     | HICO              |
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

## 7. [Power Management](sdk/power_management.md)
Provide functions to allow developers control the power states switching.