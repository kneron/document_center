# Solution HICO ToF

This solution is an application which KL720 chip plays as a host chip with connected MIPI ToF (Time of Flight) module (**host input**) for object detection and depth measurement while sending images and detection results to host PC (**companion output**). Host input and companion output is abbreviated as **HICO**. You will need to program the SCPU/NCPU firmware to the device first. Then, you can start object detection and depth measurement by running `[kneron_plus]/examples_enterprise/kl720_demo_hico_tof_inference/kl720_demo_hico_tof_inference.cpp`.

### Hardware Requirements

- ToF_ISR module  

### Firmware Preparation

- **Run Keil MDK and compile reference design for SCPU firmware**  
    Open workspace file `[KL720_SDK]/firmware/build/solution_kdp2_hico_tof/sn72096_11x11/proj.uvmpw`  
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

### Software Preparation

- **Run example**
    Build and run `[kneron_plus]/examples_enterprise/kl720_demo_hico_tof_inference/kl720_demo_hico_tof_inference.cpp`, note that `-DWITH_OPENCV=ON` should be added when running cmake command. You will see the RGB video captured, the depth map measured by the ToF module and the detection result are streaming on host PC. For more detail about how to use Kneron PLUS, please refer to Kneron Document Center
