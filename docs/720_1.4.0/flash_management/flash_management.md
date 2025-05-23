﻿# Flash Management

## 1. Board Overview

* **Board 96-A**

    ![](../imgs/flash_management/96board_a.png)

* **Board 96-B**

    ![](../imgs/flash_management/96board_b.png)

## 2. Hardware Setting

### 2.1. Connecting UART0 (Program Flash via UART0 Interface)

UART0: Command Port (either CN10 or J8)

* **Board 96-A**

    ![](../imgs/flash_management/96board_a_connect.png)

* **Board 96-B**

    ![](../imgs/flash_management/96board_b_connect.png)

### 2.2. Connecting JTAG (Program Flash via JTAG/SWD Interface)

### 2.3. Connecting USB3.0 for 5V power supply

## 3. Program Flash via UART0 Interface

### 3.1. Flash programmer necessaries

1. Open command terminal for flash programmer execution

    Tool path: kl720_sdk\firmware\utils\flash_programmer\nand\flash_programmer.py

2. install Necessary python modules: kl720_sdk\firmware\utils\requirements.txt

### 3.2. Edit python verification setting

1. Check UART port number from device manager

2. Edit setup.py, search “COM_ID” and modify the ID to match your UART port number

    ex: COM_ID = 3 # COM3

    ![](../imgs/flash_management/com_port_num.png)

### 3.3 Firmware Binary Generation (FW + MODELS)
Generate flash final bin file from other seperate bin files.

The script combines .bin files in "flash_bin" in predefined order.

Morever, the addressing is in 4KB alignment.

Command:

    >> python3 bin_gen.py <options>

    options argument:

    -h, --help      Show this help message and exit

    -p, --CPU_ONLY  SPL/SCPU/NCPU only

Output:

    flash_image.bin

** The following bin files are must **

flash_bin<br>
├── boot_spl.bin      // bool spl bin file<br>
├── fw_ncpu.bin       // SCPU FW bin file (generated by Keil)<br>
├── fw_scpu.bin       // NCPU FW bin file (generated by Keil)<br>
├── models_720.nef    // model information(copied from kenron_plus/res/models/KL720)<br>

### 3.4 Flash Chip Programming (FW + DATA)

`>> python flash_programmer.py -a flash_image.bin`

Please press RESET BTN while you are seeing “Please press reset button!!”

* **Board 96-A**

    ![](../imgs/flash_management/96board_a_reset_button.png)

* **Board 96-B**

    ![](../imgs/flash_management/96board_b_reset_button.png)

Afterwards, just wait until all progresses are finished (erase, program, verify)

![](../imgs/flash_management/flash_programmer.png)

**Note**:
"flash_programmer.py -a" means to do flash chip erase + programming + verification

### 3.5 Flash Verification (optional)

`>> python flash_programmer.py -v flash_image.bin`

### 3.6 Flash Erase (optional)

`>> python flash_programmer.py -e`

### 3.7 Flash Partial Programming (optional)

`>> python flash_programmer.py -i 0x00040000 -p fw_scpu.bin`

**Note**:
To program specific bin file to specific flash address
"-i" means the flash index/address you would like to program
"-p" means the FW code you would like to program


## 4. Program Flash via JTAG/SWD Interface

### 4.1. Jlink programmer necessaries

Connect JTAG/SWD and USB3.0 for 5V power.

![](../imgs/flash_management/jlink.png)

### 4.2. Edit flash_prog.jlink device setting

1. Check your flash type: Winbond SPI Nand flash 

2. Select a specific device based on flash manufacturer
    EX: device KL720-WB-NAND //Winbond Nand flash

3. Copy the bin file to kl720_sdk\firmware\utils\JLink_programmer\bin folder
    EX: flash_image.bin, boot_spl.bin, fw_scpu.bin, fw_ncpu.bin, fw_ncpu_dram.bin etc.


### 4.3. Double click "flash_prog.bat"

Afterwards, just wait until all progresses are finished (chip erase, program, verify)

![](../imgs/flash_management/jlink_flash_prog.png)

### 4.4. Check programming result

Please ensure all the results are "O.K.", and enter "qc" to quit and close J-Link commander

![](../imgs/flash_management/jlink_flash_prog_end.png)

### 4.5. Edit flash_prog_partial.jlink device setting(optional)

To program ncpu fw partially to specific flash address(sector erase, program, verify)

1. "flash_ncpu.jlink" loadbin command: Load *.bin file into target memory

    **Syntax**:

    `loadbin <filename>, <addr>`

    `loadbin .\bin\fw_ncpu_dram.bin,0x000E0000`

    `loadbin .\bin\fw_ncpu.bin,0x001E0000`

2. Double click “flash_ncpu.bat” and wait until all progresses are finished

3. Check programming result
    Please ensure the results is “O.K.”, and enter “qc” to quit and close J-Link commander
    EX:
    ![](../imgs/flash_management/jlink_flash_prog_partial.png)

