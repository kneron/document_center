# Solution Host input UART Output Example

This solution is an application which Kneron chip plays as a host chip with connected MIPI camera sensors for object detection. The detection result is output to UART. You will need to program the flash image to the device first. The flash image includes SCPU/NCPU firmware and model. Then, you can start/stop object detection by simple command via UART. 

### Hardware Requirements

- Kneron KL520 series AI SoC Development Kit 
- usb-to-serial device 

### Firmware Preparation

- **Run Keil MDK and compile reference design for SCPU firmware**  
    Open workspace file `[SDK]/firmware/build/solution_kdp2_host_in_uart_out/sn52096/proj.uvmpw`  
    and batch build all the projects.  
    Notes:
    User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)

- **Program SCPU/NCPU firmware**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    ```bash
    # program fw_scpu.bin and fw_ncpu.bin to the device
    cd [SDK]/firmware/utils/JLink_programmer  
    flash_prog.bat   
    
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
    ```

- **Program model**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    
    ```bash
    # program models_520.bin to the device 
    cd [SDK]/firmware/utils/JLink_programmer  
    move [SDK]/firmware/utils/bin_gen/flash_bin/models_520.nef  ./bin/  
    flash_model.bat  
    
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
    ```
```
    
- **Run example**  
    1.  Connect to KL520 through serial port. [How to connect](../flash_management/flash_management.md#2-hardware-setting)
	2.  See command menu and type command (0) - (4) for functions in UART console window (ex. Putty)

### Commands

1. Type "1" in UART console window to **Start Tiny YoloV3 Inference with RGB camera**  
    **Bounding box** information is shown on the UART console window.  
   
2. Type "2" to **Start Tiny YoloV3 Inference with NIR camera**  
    **Bounding box** information is shown on the UART console window.  

3. Type "3" to **Start Tiny YoloV3 Inference with RGB and NIR camera**  
    **Bounding box** information is shown on the UART console window.  

4. Type "4" to **Stop Inference**

5. Type "5" to **Quit**


```