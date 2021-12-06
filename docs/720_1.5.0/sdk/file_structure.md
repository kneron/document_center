# File Structure

The whole SDK package is composed of device firmware, the folder design is described below.

## 1. Basic Concept
The basic concept of FW folder structure is modularize and stratification for all source code. FW code belonged to same feature will be put to one dedicated folder and easy to include/exclude it. Refer to basic FW architecture shown below, the listed items will have corresponding folders.

![](../imgs/sdk/file_structure.png)

Here is the example folder design for Kneron SDK.  The <font color="#000066">**dark blue and bold** </font>fonts are mandatory folder name used in SDK. The normal words may vary in different SDK release or depends on your project.

├───<font color="#000066">**firmware**</font><br>
│   ├───<font color="#000066">**app**</font><br>
│   ├───<font color="#000066">**build**</font><br>
│   │   ├───<font color="#000066">**solution_**</font>companion<br>
│   │   │   ├───<font color="#000066">**main_scpu**</font><br>
│   │   │   │   └───include<br>
│   │   │   ├───sn72096_9x9<br>
│   │   │   │   └───scpu_keil<br>
│   ├───<font color="#000066">**include**</font><br>
│   ├───<font color="#000066">**mdw**</font><br>
│   │   ├───console<br>
│   │   ├───dfu<br>
│   │   ├───errand<br>
│   │   ├───flash<br>
│   │   ├───include<br>
│   │   ├───ipc<br>
│   │   ├───memory<br>
│   │   ├───model<br>
│   │   ├───power<br>
│   │   ├───spi_com<br>
│   │   ├───ssp<br>
│   │   ├───system<br>
│   │   ├───tdc<br>
│   │   ├───usbd_com<br>
│   │   ├───usbh2<br>
│   │   └───utilities<br>
│   ├───<font color="#000066">**platform**</font><br>
│   │   ├───<font color="#000066">**board**</font><br>
│   │   │   └───<font color="#000066">**board_**</font>sn72096_9x9<br>
│   │   ├───<font color="#000066">**dev**</font><br>
│   │   │   ├───eeprom<br>
│   │   │   ├───include<br>
│   │   │   ├───nand<br>
│   │   │   │   ├───gigadevice<br>
│   │   │   │   └───winbond<br>
│   │   │   ├───nor<br>
│   │   │   ├───wifi<br>
│   │   │   │   ├───BufList<br>
│   │   │   │   ├───ESP8266<br>
│   │   │   │   │   ├───CMSIS_DV_Results<br>
│   │   │   │   │   └───Config<br>
│   │   ├───<font color="#000066">**kl720**</font><br>
│   │   │   ├───<font color="#000066">**common**</font><br>
│   │   │   ├───<font color="#000066">**scpu**</font><br>
│   │   │   │   ├───<font color="#000066">**drv**</font><br>
│   │   │   │   │   └───include<br>
│   │   │   │   ├───<font color="#000066">**rtos**</font><br>
│   │   │   │   │   ├───rtx<br>
│   │   │   │   │   │   └───include<br>
│   │   │   │   └───<font color="#000066">**startup**</font><br>
│   ├───<font color="#000066">**utils**</font><br>
│   │   ├───bin_gen<br>
│   │   │   └───flash_bin<br>
│   │   ├───<font color="#000066">**dfu**</font><br>
│   │   │   └───src<br>
│   │   ├───<font color="#000066">**flash_programmer**</font><br>
│   │   │   ├───nand<br>
│   │   │   └───nor<br>
│   │   ├───<font color="#000066">**JLink_programmer**</font><br>
│   │   │   ├───bin<br>
│   │   │   ├───Devices<br>
│   │   │   │   ├───Kneron<br>
│   │   │   │   │   └───Winbond<br>
│   │   └───spl_aes<br>


## 2. Detailed explanation

└───<font color="#0000dd">**firmware**</font><br>

<font color="#0000dd">**firmware:**</font> Contains all device FW source/lib code, utilities, build environment


├───firmware<br>
│   ├───<font color="#0000dd">**app**</font><br>
│   ├───<font color="#0000dd">**build**</font><br>
│   ├───<font color="#0000dd">**include**</font><br>
│   ├───<font color="#0000dd">**mdw**</font><br>
│   ├───<font color="#0000dd">**platform**</font><br>
│   └───<font color="#0000dd">**utils**</font><br>

Basically, the firmware source_code=app+mdw+platform(+include). We hope all firmware source code will be put under these 3 folders and will not be influenced by any projects, that is, it's a source code data base. All project related code will be put under build folder.

<font color="#0000dd">**app:**</font> All application firmware code. Every module or C file have prefix kapp_.

<font color="#0000dd">**build:**</font> Build environment. Include (Keil) project files, workspace, main.c, makefiles. C source files will be pulled in a project and then engineer generates a new project.

<font color="#0000dd">**include:**</font> C header files for all source code

<font color="#0000dd">**mdw:**</font> Middleware. It's kind of "service", "manager". We can put some useful and special purpose pure software feature here, such as file system, software timer, DFU function, memory management.

<font color="#0000dd">**platform:**</font> It means a HW platform or a SoC for AI development. Platform consists of an SoC, a PCB, and some onboard devices(flash, eeprom...).

<font color="#0000dd">**utils:**</font> some useful utilities, such as flash programming, calculate checksum...

├───firmware<br>
│   ├───build<br>
│   │   ├───<font color="#0000dd">**example_**</font>xxx<br>
│   │   ├───<font color="#0000dd">**lib**</font><br>
│   │   ├───<font color="#0000dd">**solution_**</font>xxx<br>

There are two major components in build folder, example projects and solution projects. As the name implies, small app demo, simple peripheral drivers demo, or any features demonstration belong to example projects. The purpose is to show how to use our SDK. Solution projects is a solution for customer. It contains more features, or complex functions in a single project. 
Example projects will have example_ prefix and solution projects will have solution_ prefix.
If you need to build a library and share with other projects, create lib projects in lib folder.

<font color="#0000dd">**example_**</font> : a prefix for example project. ex. example_i2c, example_tiny_yolo

<font color="#0000dd">**solution_**</font> : a prefix for solution project. ex. solution_kdp2, solution_door_lock

<font color="#0000dd">**lib:**</font> Some source files need to be hidden or need to generate library. Put the library project here

├───firmware<br>
│   ├───mdw<br>
│   │   ├───<font color="#0000dd">**console**</font><br>
│   │   ├───<font color="#0000dd">**dfu**</font><br>
│   │   ├───<font color="#0000dd">**errand**</font><br>
│   │   ├───<font color="#0000dd">**flash**</font><br>
... ...

Collect independent modules to become middle ware here.
It can be generic flash driver, firmware upgrade manager, file system...etc.

├───firmware<br>
│   ├───platform<br>
│   │   ├───<font color="#0000dd">**board**</font><br>
│   │   ├───<font color="#0000dd">**dev**</font><br>
│   │   │   ├───eeprom<br>
│   │   │   ├───nand<br>
│   │   │   ├───nor<br>
│   │   │   └───wifi<br>
│   │   ├───<font color="#0000dd">**kl720**</font><br>
│   │   │   ├───common<br>
│   │   │   ├───scpu<br>
│   │   │   │   ├───drv<br>
│   │   │   │   ├───rtos<br>
│   │   │   │   └───startup<br>

Platform = board + dev + ASIC. 

<font color="#0000dd">**board**</font>: PCB information, flash size, IO mapping, 

<font color="#0000dd">**dev**</font>: device drivers, such as flash driver, eeprom driver, wifi module driver, panel driver, sensor driver

<font color="#0000dd">**kl720**</font>: contain all peripheral drivers, real time OS, startup assembly code, and FW init code.
