# Solution Host MIPI

This solution is an application which KL520 chip plays as a host chip with connected display and MIPI camera sensors for object detection. You will need to program the flash image to the device first. The flash image includes SCPU/NCPU firmware and model. Then, you can start/stop object detection by simple command via UART. 

### Hardware Requirements

- Kneron KL520 series AI SoC Development Kit  
- usb-to-serial device



### Firmware Preparation

- **Run Keil MDK and compile reference design**  
    Open workspace file `[KL520_SDK]/firmware/build/solution_kdp2_host_mipi/sn52096/proj.uvmpw`  
    and batch build all the projects.    
    
    **Notes:**
User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)
    
- **Generate the firmware bin image**  
  
    ```bash
    cd [KL520_SDK]/firmware/utils/bin_gen  
    python3 bin_gen.py  
    # The compiled SCPU/NCPU FW in the previous step will be placed under flash_bin/ automatically  
    # bin_gen.py will concatenate SCPU/NCPU FW, models_520.nef to generate flash_image.bin  
    # Note that you may need to substitute '/' for '\' in the path
    ```
```
    
- **Program the firmware bin image**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    
    ```bash
    cd [KL520_SDK]/firmware/utils/JLink_programmer  
    move [KL520_SDK]/firmware/utils/bin_gen/flash_image.bin  ./bin/  
    flash_prog.bat # program flash_image.bin to the device  
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
```

- **Run example**  
    1.  Connect to KL520 through serial port. Reference:  [How to connect](../flash_management/flash_management.md#2-hardware-setting)
	2.  Turn on KL520 
	3.  Press PTN button 
	4.  See command menu and type command (1) - (5) for functions in UART console window (ex. Putty)

### Commands

1. Type "1" in UART console window to **Start Tiny YoloV3 Inference with RGB camera**  
    **Bounding box** is drawn around the detected object.  
   
2. Type "2" to **Start Tiny YoloV3 Inference with NIR camera**  
    **Bounding box** is drawn around the detected object.  

3. Type "3" to **Start Tiny YoloV3 Inference with NIR and RGB camera**  
    Default only show the detection result on RGB camera

4. Type "4" to **Stop Inference**

5. Type "5" to **Quit and shut down KL520**
