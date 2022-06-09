# Solution Host input UART output

This solution is an application which KL720 chip plays as a host chip with connected MIPI camera sensors for object detection. The detection result is output to UART. You will need to program the flash image to the device first. The flash image includes SCPU/NCPU firmware and model. Then, you can start/stop object detection by simple command via UART. 

### Hardware Requirements

- Kneron LW 3D module  

### Firmware Preparation

- **Run Keil MDK and compile reference design for SCPU firmware**  
    Open workspace file `[KL720_SDK]/firmware/build/solution_kdp2_host_in_uart_out/sn72096_11x11/proj.uvmpw`  
    and batch build all the projects.  
    Notes:
    User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)

- **Run Xtensa and compile reference design for NCPU firmware**  
    Please refer to [Xtensa Xplorer Overview](xtensa.md) 

- **Program SCPU/NCPU firmware**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    ```bash
    cd [KL720_SDK]/firmware/utils/JLink_programmer  
    flash_prog.bat # program fw_scpu.bin and fw_ncpu.bin to the device  
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
    ```

- **Program model**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    ```bash
    cd [KL720_SDK]/firmware/utils/JLink_programmer  
    move [KL720_SDK]/firmware/utils/bin_gen/flash_bin/models_720.nef  ./bin/  
    flash_prog.bat # program models_720.bin to the device  
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
    ```

- **Run example**  
    1.  Connect to KL720 through serial port
	2.  See command menu and type command (0) - (4) for functions in UART console window (ex. Putty)

### Commands

1. Type "0" in UART console window to **Start YoloV5s Inference with RGB camera**  
    **Bounding box** information is shown on the UART console window.  
   
2. Type "1" to **Start YoloV5s Inference with NIR camera**  
    **Bounding box** information is shown on the UART console window.  

3. Type "2" to **Start YoloV5s Inference with RGB and NIR camera**  
    **Bounding box** information is shown on the UART console window.  

4. Type "3" to **Stop Inference**

5. Type "4" to **Quit**

