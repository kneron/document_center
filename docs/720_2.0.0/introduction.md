# Introduction

**note:** SDK v2.0.x is compatible with Kneron PLUS v2.0.x
**note:** SDK v2.0.x is **NOT COMPATIBLE** to v1.x.x

---

This document mentions the usage of prebuilt features, how to customize a model application, and peripheral features



## 1. Requirements

**Hardware**:

Board with KL720 chip, like dongle, 96board, m.2 board.

(for MIPI application example) Kneron LW 3D module

(for ToF application example) ToF_ISR module



**Software:**

licensed software: [ARM Keil MDK](https://www.keil.com)        [ARM Keil/MDK docs](https://www2.keil.com/mdk5/docs)

licensed software: [Cadence Tensilica Xtensa SDK](https://ip.cadence.com/swdev) 



> [Xtensa IDE installation and configuration for KL720](sdk/xtensa.md)



## 2. File Structure

The firmware folder structure is architected with modularize and stratification for all source code. Source code belonged to the same feature is put in a dedicated folder and easy to be included or excluded. Refer to basic FW architecture shown below, the listed items will have corresponding folders.

![](./imgs/file_structure.png)



```txt
.
└── firmware
    ├── app                                          # model flow control example
    ├── build
    │   ├── example_kdrv                             # some middleware/driver examples
    │   ├── lib
    │   ├── solution_XXX                             # solution examples
    ├── include                                      # shared header files 
    ├── lib                                          # libraries
    │   ├── kmdw_dfs_fuzzy_720.lib
    │   ├── libToF.lib
    │   └── system_720.lib
    ├── mdw                                          # middleware source code
    ├── platform
    │   ├── board                                    # board configuraiton header files
    │   ├── dev                                      # device drivers
    │   └── kl720                                    # chip API interface
    │       ├── common                                       
    │       ├── ncpu
    │       │   ├── libs                             # ncpu driver API (library only)
    │       │   └── ncpu_main                        # main entry to hook pre/post process functions
    │       └── scpu
    │           ├── drv                              # ncpu driver API and source code
    │           ├── rtos/rtx
    │           └── startup
    └── utils
        ├── bin_gen
        ├── dfu
        ├── dfw_boot
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

**Platform = board + dev + ASIC**-KL720

ASIC-KL720 is composed of 2 cores:

| Core             | OS       | Description                                                  |
| ---------------- | -------- | ------------------------------------------------------------ |
| SCPU (ARM CM4)   | Keil RTX | system flow control and handle data in/ data out via provided drivers |
| NCPU(Xtensa VP6) | FreeRTOS | handle pre/post process and trigger NPU core to run a model  |



```txt
└───firmware/platform
    ├───board			   # PCB information, flash size, IO mapping, and board level configuration
    |
    ├───dev                # device drivers, such as drivers for flash, eeprom, panel, sensor, etc.
    │   ├───panel
    │   └───nand
    |       ...            
    └────kl720             # KL720 SoC
        ├───common         # shared header files
        ├────scpu        
        |    ├───drv       # all peripheral drivers
        |    ├───rtos      # Keil RTX operation system 
        |    └───startup   # startup assembly code
        └────ncpu
             ├───ncpu_main # entry to hook model pre/post process functions
             └───libs      # builtin ncpu libraries to contron NCPU(DSP) core
```



### 2.5 'firmware/utils'

| Utility               | Description | References |
| --------------------- | ----------- |---------------------|
| bin_gen / bin_gen_nor | To generate single image from several image components | ch 3.1 in [README](flash_management/flash_management.md#3-program-flash-via-uart0-interface) |
| dfu                   | To satisfy flash address alignment. It is called by post_build.bat in each Keil project | utils/dfu/readme.txt |
| flash_programmer      | Tool to program firmware/model/data via UART interface | ch 3.3 in [README](flash_management/flash_management.md#3-program-flash-via-uart0-interface) |
| JLink_programmer      | Script to program firmware/model/data via JLink | ch 4 in [README](flash_management/flash_management.md#4-program-flash-via-jtagswd-interface) |
| nef_utility           | utility for model(NEF file) | execute "nef_utility -h" |
| pinmux_config         | pinmux table | see the excel file |
| setenc                | KL720 provides secure boot protected with AES and SHA | [README](sdk/secure_boot.md) |
| minion            | Allows device to boot from uart or usb without external flash | utils/minion/app/readme.txt |



## 3. Solution Project Examples
This SDK provides the following solution project examples.

| Solution Project               | Required Chip | Peripherals         | Description                                                  |
| ------------------------------ | ------------- | ------------------- | ------------------------------------------------------------ |
| solution_kdp2_user_ex          | kl720_9x9     | none                | data input and result output via Kneron PLUS API and customized model inference flow |
| solution_kdp2_hico_mipi        | kl720_11x11   | Kneron LW 3D module | image from MIPI sensor and output to connected PC via USB    |
| solution_kdp2_hico_tof         | kl720_11x11   | ToF_ISR module      | image from MIPI ToF sensor and output to connected PC via USB |
| solution_kdp2_host_in_uart_out | kl720_11x11   | Kneron LW 3D module | image from MIPI sensor and output to connected PC via UART   |

General common files:

- Keil project path: *./firmware/build/soluiton_XXX*
- version info file: *./firmware/include/version.h*
- project configuration: *./firmware/build/solution_xxx/sn720xxx/project.h*



> Step by step to create new application, please refer to the section **Kneron PLUS / Customized API** (reference: solution_kdp2_user_ex)



## 4. SoC Peripheral Drivers

The peripheral definitions and prototypes for the application programming reference.
> [Peripheral Driver APIs](sdk/soc_peripheral_drivers.md)


### Supported/Unsupported Peripheral Table

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



## 5. Appendix

| item             | Description                                                  | References                        |
| ---------------- | ------------------------------------------------------------ | --------------------------------- |
| Power Management | Provide functions to allow developers control the power states switching | [README](sdk/power_management.md) |

