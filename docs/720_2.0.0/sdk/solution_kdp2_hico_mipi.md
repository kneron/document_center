# Solution HICO MIPI Example

This solution is an application which KL720 chip plays as a host chip with connected MIPI camera sensors (**host input**) for object detection while sending images by a host PC and receiving detection results from it (**companion output through USB**). Host input and companion output is abbreviated as **HICO**. You will need to program the SCPU/NCPU firmware to the device first. Then, you can start object detection by running an application at host with **Kneron PLUS**.

### Hardware Requirements

- Kneron LW 3D module  


### Firmware Preparation

- **Run Keil MDK and compile reference design for SCPU firmware**  
    Open workspace file `[KL720_SDK]/firmware/build/solution_kdp2_hico_mipi/sn72096_11x11/proj.uvmpw`  
    and batch build all the projects.
    Notes:
    User can edit and debug with Keil MDK for further implementation  [keil/MDK docs](https://www2.keil.com/mdk5/docs)

- **Run Xtensa and compile reference design for NCPU firmware**  
    Please refer to [Xtensa Xplorer Overview](xtensa.md) 

- **Program SCPU/NCPU firmware**  
    Reference:  [Jlink programming](../flash_management/flash_management.md#4-program-flash-via-jtagswd-interface)  
    ```bash
    # program fw_scpu.bin and fw_ncpu.bin to the device  
    cd [KL720_SDK]/firmware/utils/JLink_programmer  
    flash_prog.bat 
    # follow the instructions to finish JLink programming
    # Note that you may need to substitute '/' for '\' in the path
    ```

### Software Preparation

- **Run example**
    Build and run `[kneron_plus]/examples_enterprise/kl720_demo_hico_cam_inference/kl720_demo_hico_cam_inference.cpp`, note that `-DWITH_OPENCV=ON` should be added when running cmake command. You will see the RGB video captured by the camera and and the detection result are streaming on host PC. 
    
    For more details about how to use Kneron PLUS, please start with *Kneron Document Center -> Kneron PLUS -C -> Getting Started*

