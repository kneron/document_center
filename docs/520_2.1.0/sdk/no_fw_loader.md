# Switch to No Firmware-loader Flow

(KL520 only)

*Firmware loader* is designed for flexible firmware change. The firmware can be uploaded to DDR from host side(e.g. a PC). However, it is designed for USB interface integrated application, or say host-companion design. If there is no USB available, it is a potential risk on boot-from-flash with failed flash programing due to single boot partition. 

![](../../imgs/sdk/fw_load_flash_table.png)

As the schematic diagram above shows the beginning SRAM address of fw_scpu.bin are different. Also, flash table for those binaries in with/without firmware loader are different. Due to the difference, we need to rebuild the fw_scpu.bin and use different flash table to use no-fw-loader flow.

**Step 1: rebuild fw_scpu.bin** 

1. set **#define PROJ_NOT_USE_FW_LOADER  1** in *project.h*, e.g. *./build/solution_kdp2_host_mipi/sn52096/project.h*
2. change scatter file by replace *scatter_load.sct* by *kdp.sct* in *firmware/build/solution_kdp2_host_mipi/sn52096/scpu_keil/scpu.uvprojx*
   (you can do the same change by Keil -> Project -> Options for Target 'dev' -> linker tab -> Scatter file)
3. compile/link the project/workspace

**Step 2: compose flash image**

1. prepare the `flash_image.bin` by utility, *bin_gen*, with -n parameter. e.g. "***python3 bin_gen.py -n***"  



Then, the generated `flash_image.bin` is for no-firmware-loader flow. 
