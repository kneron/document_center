# Introduction

**note:** SDK v2.0.x is compatible with Kneron PLUS v2.0.x  
**note:** SDK v2.0.x is **NOT COMPATIBLE** to v1.x.x

---

This document mentions the usage of prebuilt features, how to customize a model application, and peripheral features



## 1. Prerequisite

**Hardware**:

Board with KL520 chip. Ex. 520 dongle, 96board, m.2 board

(For applications with MIPI camera/Display) Kneron KL520 series AI SoC Development Kit

**Software:**

required OS: native Windows 10-x86_64 64-bit

licensed software: [ARM Keil MDK](https://www.keil.com)    /   [ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)  



## 2. File Structure

The firmware folder structure is architected with modularize and stratification for all source code. Source code belonged to the same feature is put in a dedicated folder and easy to be included or excluded. Refer to basic FW architecture shown below, the listed items will have corresponding folders.

![](./imgs/file_structure.png)



```txt
.
└── firmware
    ├── app                                          # model flow control example
    ├── build
    │   ├── example_kdrv                             # some middleware/driver examples
    │   ├── lib/system_520/include
    │   ├── solution_XXX                             # solution examples
    ├── include                                      # high level header files 
    ├── lib                                          # libraries
    │   ├── kdp2_ncpu_model_ppp.lib                  #   header file: plateform/kl520/ncpu/drv/include
    │   ├── kdp2_ncpu_sdk.lib                        #   header file: plateform/kl520/ncpu/model_ppp/include
    │   └── system_520.lib                           #   header file: build/lib/system_520/include
    ├── mdw                                          # middleware source code
    ├── platform
    │   ├── board                                    # board configuraiton header files
    │   ├── dev                                      # device drivers
    │   └── kl520                                    # chip API interface
    │       ├── common                                       
    │       ├── ncpu
    │       │   ├── drv                              # ncpu driver API
    │       │   ├── model_ppp                        # ncpu builtin pre/post process API
    │       │   ├── rtos/rtx                             
    │       │   └── startup
    │       └── scpu
    │           ├── drv                              # ncpu driver API and source code
    │           ├── rtos/rtx
    │           ├── startup
    └── utils
        ├── bin_gen
        ├── dfu
        ├── minion
        ├── flash_programmer
        ├── FLM
        ├── JLink_programmer
        ├── nef_utility
        └── pinmux_config/Kneron_pinmux_config.xlsm
```



### 2.1 Folder Tree Root - 'firmware'

**firmware:** Contains all device FW source/lib code, utilities, build environment

```txt
└───firmware
    ├───app         # source code for application layer
    ├───build       # Build environment. Include (Keil) project files, project dependent source code.
    ├───include     # C header files for all source code
    ├───mdw         # Middleware. It's kind of "service", "manager". EX, software timer, DFU function, memory management, etc.
    ├───platform	# Platform consists of an SoC, a PCB, and some onboard devices(flash, eeprom...).
    └───utils       # some useful utilities, such as flash programming, calculate checksum...
```

In general, **firmware source_code = app + mdw + platform(+include)**. 

Source code is suggested to be put in these 3 folders and will not be influenced by any projects. That is, it's a source code data base. All project related code will be put under build folder.



### 2.2 'firmware/build'

There are some components in build folder, **example projects** and **solution projects**. As the name implies, small app demo, simple peripheral drivers demo, or any features demonstration belong to example projects. The purpose is to show how to use our SDK. Solution projects is solution examples for customer. It contains more features, or complex functions in a single project. 
Also, If you need to build a library and share with other projects, create lib projects in **lib** folder. 

```txt
└────firmware/build
    ├───example_kdrv 	# keil projects and example code for example projects
    ├───lib          	# Keil projects and header files for prebuilt libraries
    └────solution_** 	# Keil projects for example solutions
```



### 2.3 'firmware/mdw'

`firmware/mdw ` collects independent modules to become middle ware here.
It can be generic flash driver, firmware upgrade manager, file system, etc.

```txt
└────firmware/mdw
    ├───console
    ├───dfu
    ├───flash
        ...
```



### 2.4 'firmware/platform'

`firmware/platform` collects board, device drivers, SoC chip drivers, OS interface, etc.

**Platform = board + dev + ASIC**-KL520

ASIC-KL520 is composed of 2 cores:

| Core           | OS       | Description                                                  |
| -------------- | -------- | ------------------------------------------------------------ |
| SCPU (ARM CM4) | Keil RTX | system flow control and handle data in/ data out via provided drivers |
| NCPU(ARM CM4)  | Keil RTX | handle pre/post process and trigger NPU core to run a model  |



```txt
└───firmware/platform
    ├───board			   # PCB information, flash size, IO mapping, and board level configuration
    |
    ├───dev                # device drivers, such as drivers for flash, eeprom, panel, sensor, etc.
    │   ├───panel
    │   └───nand
    |       ...            
    └────kl520             # KL520 SoC
        ├───common         # shared header files
        ├────scpu        
        |    ├───drv       # all peripheral drivers
        |    ├───rtos      # Keil RTX operation system 
        |    └───startup   # startup assembly code
        └────ncpu
             ├───drv       # prebuilt driver liberary
             ├───model_ppp # prebuilt model pre/post process functions 
             ├───rtos      # Keil RTX operation system 
             └───startup   # startup assembly code
```



### 2.5 'firmware/utils'

| Utility          | Description                                                  | References                                                   |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| bin_gen          | To generate single image from several image components       | ch 3.3 in [README](flash_management/flash_management.md#3-program-flash-via-uart0-interface) |
| dfu              | To satisfy flash address alignment. It is called by post_build.bat in each Keil project | utils/dfu/readme.txt                                         |
| flash_programmer | Tool to program firmware/model/data via UART interface       | ch 3.4 in [README](flash_management/flash_management.md#3-program-flash-via-uart0-interface) |
| JLink_programmer | Script to program firmware/model/data via JLink              | ch 4 in [README](flash_management/flash_management.md#4-program-flash-via-jtagswd-interface) |
| nef_utility      | utility for model(NEF file)                                  | execute "nef_utility -h"                                     |
| pinmux_config    | pinmux table                                                 | see Kneron_pinmux_config.xlsm                                |
| FLM              | To enable 'load' icon to program flash via JLink in Keil MDK | see README.md                                                |
| minion           | Allows device to boot from uart  without external flash      | see README.txt                                               |



## 3. Solution Project Examples

This SDK provides the following solution project examples.

| Solution Project        | Required Chip | Peripherals                                | Description                                                  | Document Link
| ----------------------- | ------------- | ------------------------------------------ | ------------------------------------------------------------ | --------------------------------
| solution_kdp2_user_ex   | kl520         | none                                       | data input and result output via Kneron PLUS API and customized model inference flow | [README](sdk/solution_kdp2_user_ex.md)
| solution_kdp2_hico_mipi | kl520         | Kneron KL520 series AI SoC Development Kit | image from MIPI camera sensor and output to connected PC via USB    | [README](sdk/solution_kdp2_hico_mipi.md)
| solution_kdp2_host_mipi | kl520         | Kneron KL520 series AI SoC Development Kit | image from MIPI camera sensor and output on display                 | [README](sdk/solution_kdp2_host_mipi.md)

General common files:

- Keil project path: *./firmware/build/soluiton_XXX*
- version info file: *./firmware/include/version.h*
- project configuration: *./firmware/build/solution_xxx/sn520xxx/project.h*



## 4. SoC Peripheral Drivers

In KL520 also provides some simple examples to show how to use basic peripherals such as, I2C, PWM, DMA, GPIO...
See them in  *firmware/build/example_kdrv*.

There is also a PDF file to briefly describe the peripheral APIs

> [KL520_Peripheral_Driver_APIs.pdf](./pdf/KL520_Peripheral_Driver_APIs.pdf)

### Supported/Unsupported Peripheral Table

> **Companion** means controlled by a host PC through USB by Kneron PLUS APIs



**Image Input**

| Peripherals         | Companion | Host Mode         |
| ------------------- | --------- | ----------------- |
| MIPI CSI RX         | x         | O                 |
| DVP                 | x         | driver/example    |
| UVC Host            | x         | specified cameras |
| USB(proprietary)    | O         | x                 |
| SPI Master, non-DMA | x         | driver/example    |
| SPI Slave, non-DMA  | x         | driver/example    |
| SPI Master, DMA     | x         | x                 |
| SPI Slave, DMA      | x         | x                 |
| UART                | x         | x                 |


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
