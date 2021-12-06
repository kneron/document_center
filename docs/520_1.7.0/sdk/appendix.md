# Appendix
##　Host Mode Example

This sample code is an application which KL520 chip plays as a host chip with connected display and cameras for Object detection. You will need to program the flash image to device first. The flash image includes SCPU/NCPU firmware and model. Then, you can Start/Stop object detection by simple command via UART. 



### Hardware Requirements

Kneron KL520 series AI SoC Development Kit    



### Firmware Preparation

- **Run Keil MDK and compile reference design**  
    Open workspace file `[KL520_SDK]\example_projects\tiny_yolo_v3_host\workspace.uvmpw`  
Notes:
User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)

- **Generate the firmware bin image**  
    Reference: [Firmware Binary Generator](../flash_management/flash_management.md#33-firmware-binary-generation-fw-models)  
    ```bash
    cd [SDK]/utils/bin_gen/flash_bin
    cp -f [KL520_SDK]/models/tiny_yolo_v3/models_520.nef .
    cd ..
    python3 bin_gen.py
    #The compiled SCPU/NCPU FW in step 1 will be placed under flash_bin/ automatically 
    #bin_gen.py will concate SCPU/NCPU FW and models_520.nef and generate flash_image.bin
    ```

- **Program the image**  
    Reference:  [Flash programming](../flash_management/flash_management.md#34-flash-chip-programming-fw-data)  
    ```bash
    cd [SDK]/utils/flash_programmer
    python3 flash_programmer.py -a ..\bin_gen\flash_image.bin 
    # follow the instructions to finish flash progrmming
    ```
- **Run example**  
	1.  Turn on KL520 
	2.  Press PTN button 
	3.  Select “1” to boot from SPI to boot from the programmed FW
	4.  Once it’s started, RGB camera and LCD will be turned on, and image will be continuously captured by camera and displayed on LCD panel. 
	5.  Also, see command menu and type command (1) - (4) for functions in UART console window(ex. Putty)



### Commands

1. Type "1" in UART console window to **Start Tiny Yolo**  
When a person is detected, **yellow box** is drawn around the person.  
   Other detected objects are drawn around by **blue boxes**.  
Console window shows detected objects with FPS info. 
   
2. Type "2" to Stop Object detection

3. Type "3" to turn off Pipeline mode, or toggle the mode, at runtime.  
   This pipeline mode can be toggled on/off (1/0) to demonstrate performance improvement.   
   Note that there may be delay to see first good inference due to opening camera/sensor. 

   

---

## Host Mode with USB Example

Besides Host Model example, this example shows how to output inference result via USB interface. You will need to program the flash image to device first. The flash image includes SCPU/NCPU firmware and model. Then, you can output inference result via USB interface

in `scpu/project/tiny_yolo_v3/host_usbout/main/kapp_tiny_yolo_inf.c`,  `usb_com_write()`is called to send data out



### Hardware Requirements

Kneron KL520 series AI SoC Development Kit  

### Firmware Preparation

- **Run Keil MDK and compile reference design**  
Open workspace file `[KL520_SDK]\example_projects\tiny_yolo_v3_host_usbout\workspace.uvmpw`
Notes: 
  User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)

- **Generate the firmware bin image**  
    **Reference:** [Firmware Binary Generator](../flash_management/flash_management.md#33-firmware-binary-generation-fw-models)  
    ```bash
    cd [SDK]/utils/bin_gen/flash_bin
    cp -f [KL520_SDK]/models/tiny_yolo_v3/models_520.nef .
    cd ..
    python3 bin_gen.py
    #The compiled SCPU/NCPU FW in step 1 will be placed under flash_bin/  automatically 
    #bin_gen.py will concate SCPU/NCPU FW and models_520.nef and    generate flash_image.bin
    ```
- **Program the image**  
    Reference: [Flash programming](../flash_management/flash_management.md#34-flash-chip-programming-fw-data)  
    
    ```bash
    cd [SDK]/utils/flash_programmer
    python3 flash_programmer.py -a ..\bin_gen\flash_image.bin 
    # follow the instructions to finish flash progrmming
    ```

### Software Preparation

**[OS]**

win 10 64bits/mingw64  

  

**[build host side receiver]**

```bash
cd host_usb_receiver
mkdir build
cd build
cmake .. -G"MSYS Makefiles"
make -j
cd bin

#./usbhost.exe will be created
```


**[using a prebuilt binary]**

```
cd host_usb_receiver/bin
cp ../dll/* .
-> then, you can use "usbhost.exe"
```


### Run example 
1. run FW: `example_projects/tiny_yolo_v3_host_usbout`
2. select 1 to Start Tiny Yolo. Now, no bunding box is shown in KL520 display 
3. in a PC terminal console
   ```bash
   cd host_usb_receiver/build/bin
   ./usbhost.exe
   ```
4. in PC terminal console, you can BBOX result is shown   
5. also, bounding box result is drawn in KL520 display


