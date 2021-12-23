# Introduction

**note:** KL720 SDK v1.4.x starts to support Kneron PLUS

## 1. Requirements

**Hardware**:

Board with KL720 chip, like 720 dongle, 96board, m.2 board.

(for MIPI application example) Kneron LW 3D module

(for ToF application example) ToF_ISR module

**Software:**

licensed software: [ARM Keil MDK](https://www.keil.com)        [ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)

licensed software: [Cadence Tensilica Xtensa SDK](https://ip.cadence.com/swdev) 



## 2. File Structure

The whole SDK package is composed of device firmware, the folder design is described below.



### 2.1 Basic Concept

The basic concept of FW folder structure is modularize and stratification for all source code. FW code belonged to same feature will be put to one dedicated folder and easy to include/exclude it. Refer to basic FW architecture shown below, the listed items will have corresponding folders.

![](./imgs/file_structure.png)

Here is the example folder design for Kneron SDK.  

```txt
└────firmware
    ├───app
    ├───build
    │   └────solution_**
    ├───include
    ├───mdw
    ├───platform
    │   ├───board
    │   ├───dev
    │   └────kl720
    │       ├───common
    │       └────scpu
    │           ├───drv
    │           ├───rtos/rtx
    │           └───startup
    └────utils
        ├───bin_gen
        ├───dfu
        ├───flash_programmer
        ├───JLink_programmer
        └───spl_aes
```



### 2.2 Detailed explanation

**firmware:** Contains all device FW source/lib code, utilities, build environment

```txt
└───firmware
    ├───app
    ├───build
    ├───include
    ├───mdw
    ├───platform
    └───utils
```

Basically, the firmware source_code=app+mdw+platform(+include). We hope all firmware source code will be put under these 3 folders and will not be influenced by any projects, that is, it's a source code data base. All project related code will be put under build folder.

**app:** All application firmware code. Every module or C file have prefix `kapp_`.

**build:** Build environment. Include (Keil) project files, workspace, main.c, makefiles. C source files will be pulled in a project and then engineer generates a new project.

**include:** C header files for all source code

**mdw:** Middleware. It's kind of "service", "manager". We can put some useful and special purpose pure software feature here, such as file system, software timer, DFU function, memory management.

**platform:** It means a HW platform or a SoC for AI development. Platform consists of an SoC, a PCB, and some onboard devices(flash, eeprom...).

**utils:** some useful utilities, such as flash programming, calculate checksum...

```txt
└────firmware
    └────build
        ├───example_**
        ├───lib
        └────solution_**
```

There are two major components in build folder, example projects and solution projects. As the name implies, small app demo, simple peripheral drivers demo, or any features demonstration belong to example projects. The purpose is to show how to use our SDK. Solution projects is a solution for customer. It contains more features, or complex functions in a single project. 
Example projects will have example_ prefix and solution projects will have solution_ prefix.
If you need to build a library and share with other projects, create lib projects in lib folder.

**example_** : a prefix for example project. ex. `example_i2c`, `example_tiny_yolo`

**solution_** : a prefix for solution project. ex. `solution_kdp2`

**lib:** Some source files need to be hidden or need to generate library. Put the library project here

```txt
└────firmware
    └────mdw
        ├───console
        ├───dfu
        ├───errand
        ├───flash
... ...
```

Collect independent modules to become middle ware here.
It can be generic flash driver, firmware upgrade manager, file system, etc.

```txt
└───firmware
    └───platform
        ├───board
        ├───dev
        │   ├───eeprom
        │   ├───nand
        │   ├───nor
        │   └───wifi
        └────kl720
            ├───common
            └────scpu
                ├───drv
                ├───rtos
                └───startup
```



Platform = board + dev + ASIC



**board**: PCB information, flash size, IO mapping, 

**dev**: device drivers, such as flash driver, eeprom driver, wifi module driver, panel driver, sensor driver

**kl720**: contain all peripheral drivers, real time OS, startup assembly code, and FW init code.

The whole SDK package is composed of device firmware, the folder design is described in this section.



## 3. [Flash Management](flash_management/flash_management.md)
Flash Programming by UART, JLink.



## 4. Create New SDK Application
Step by step to create new SDK application, please refer to the section **Kneron PLUS / Customized API**.



## 5. [Secure Boot](sdk/secure_boot.md)
Kneron KL720 provide secure protect with AES and SHA.



## 6. SoC Peripheral Drivers
The peripheral definitions and prototypes for the application programming reference.

### 6.1 Supported/Unsupported Peripheral Table

**Image Input**

| Peripherals              | Companion | HICO              |
| ------------------------ | --------- | ----------------- |
| MIPI CSI RX              | x         | driver/example    |
| DVP                      | x         | driver/example    |
| UVC Host                 | x         | specified cameras |
| USB(proprietary)         | O         | x                 |
| SPI Master, non-DMA, DMA | x         | driver/example    |
| SPI Slave, non-DMA, DMA  | x         | driver/example    |
| UART                     | x         | x                 |


**Image/Result Output**

| Peripherals              | Companion | HICO           |
| ------------------------ | --------- | -------------- |
| MIPI DSI TX              | x         | x              |
| MIPI CSI TX              | x         | x              |
| DVP                      | x         | O              |
| UVC device               | x         | x              |
| USB bulk                 | x         | O              |
| USB(proprietary)         | O         | x              |
| SPI Master, non-DMA, DMA | x         | driver/example |
| SPI Slave, non-DMA, DMA  | x         | driver/example |
| UART                     | x         | O              |
| I2C                      | x         | driver/example |
| I2S                      | x         | x              |
| INTEL 8080               | x         | x              |

###  [Peripheral Driver APIs](sdk/soc_peripheral_drivers.md)



## 7. [Power Management](sdk/power_management.md)

Provide functions to allow developers control the power states switching.
