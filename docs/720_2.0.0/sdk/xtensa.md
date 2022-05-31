

# Xtensa Xplorer Overview

The Cadence® Tensilica® Xtensa® Software Developer's Toolkit (SDK) provides a comprehensive collection of code generation and analysis tools that speed the application software development process. Eclipse-based Xtensa Xplorer Integrated Development Environment (IDE) serves as the cockpit for the entire development experience.
Xtensa Xplorer (including both GUI and command-line environment) is the only available development IDE for KL720 DSP core



# Install Xtensa Toolchain

For details on installation guidelines, see the ***Xtensa Development Tools Installation Guide*** which is available from Cadence Support.

Xtensa Software Tools are officially supported on the following platforms:

- Windows: Win 10 64-bit, Win 8 64-bit, Win 7 64-bit
- Linux: RHEL 6 64-bit (with ‘Desktop’ package installed)

There may be compatibility issues with other versions of Linux or Windows. Security-enhanced Linux (SELinux) is not a supported platform because the OS can prevent different shared libraries (including Xtensa Tools) from loading.



> Note:
>
> 1. This document only shows the usage on **windows 10 64-bit** platform.
> 2. This document is writen for **Xtensa Xplorer 0.8.11** and toolchain **RI-2019.2**



# Install KL720 DSP Build Configuration

***Build Configuration*** describes all parameters and build includes for the Tensilica processor implementation you are developing with. Before starting development for Kneron KL720 DSP core, a specific build configuration must to be installed first.

The build configuration is provided by Kneron as a binary file that can be imported into your Xtensa Xplorer IDE environment. This file can be downloaded from [Kneron Develop Center](https://www.kneron.com/tw/support/developers/) -> **KL720 SDK** -> **kl720_vp6_asic_win32.tgz** 

The build configuration can be installed into Xplorer IDE using the **System Overview** panel which is in the lower left corner by default, or it can be toggled using menu item **Window > Show View - System Overview**.

Then, right -click on **Configurations** and then select **Find and Install a Configuration Build**

![](../imgs/xtensa/build_configuration_1.png)



Click **Browse...** and selected the download file, *kl720_vp6_asic_win32.tgz*. 
And then, click **Install Tools ...** to install the specific Configuration Build.

![](../imgs/xtensa/build_configuration_2.png)



# Compile Reference Design

We provide two approches to compile DSP design. One is using Xtensa Xplorer IDE and another is from command line environment. 



## Using Xtensa Xplorer IDE

1. Select workspace, ex. **<path_to_720_SDK>\KL720_SDK\firmware\build\ncpu_bin\kl720_ncpu**  
   ![](../imgs/xtensa/select_a_workspace.png)

2. click "cross" symbol to close welcome page  
   ![](../imgs/xtensa/xtensa_welcome.png)

3. remove auto-created HelloWorld project by **right-click on "HelloWorld" -> Delete**  
   ![](../imgs/xtensa/xtensa_remove_helloworld.png)

4. import design by using menu item **File > Import > Existing Projects into Workspace** , and then click **Next**  
   ![](../imgs/xtensa/xtensa_import.png)

   

5. click **Browse...** to select the workspace mentioned in step 1, **<path_to_720_SDK>\KL720_SDK\firmware\build\ncpu_bin\kl720_ncpu**. 
   And then, click **Finish**. 
The 'main’ project appears in the Project Explorer.  
   ![](../imgs/xtensa/xtensa_import_2.png)
   
6. Select active project as **main**
   Select Configuration Build as **vp6_asic**
   Select Target as **_debug**  (or **_release** for compiler parameters with optimization)  
   ![](../imgs/xtensa/xtensa_settings.png)

7. Click **Build Active** to compile design

8. The complied binary file, ***fw_ncpu.bin***, will be placed under *firmware/build/ncpu_bin/kl720_ncpu/main/* and cloned to utilities folder



>  Note:
>  
> 1. Xtensa Xplorer is Eclipse-based IDE, some personal workspace settings will be created at the first run. 
> If not in the first run, **step2 - step6** can be skip
> 2. Check **Help-> Help Contents -> Xtensa Xplorer -> Tutorials -> Xtensa Software Quick Start** for basic usage



## From Command Line Environment

### **Prerequisite**

- MSYS2/MINGW64 environment in winodws10 64-bit
- **cmake** and develop essential modules installed



> Note: 
> 	see **Kneron PLUS - C -> Instroduction -> Install Dependency -> Windows 10**   for installation instructions



### **To Initialize Toolchain Environment**

In SDK folder, ***envtool.sh*** is provided to setup toolchain environment. 


>  Note
>
> 1. All settings are for Xtensa installation with default path settings. 
> 2. LM_LICENSE_FILE must be configured to correct setting



Then, run ***envtool.sh*** in MINGW64/MSYS2 console

```bash
$ cd <path_to_720_SDK>/KL720_SDK/firmware/build/ncpu_bin/xcc
$ source envtool.sh
```



### **To Compile Design**

We use **cmake** to generate build files and then do compilzation accordingly. 

```bash
$ cd <path_to_720_SDK>/KL720_SDK/firmware/build/ncpu_bin/xcc

$ mkdir build
$ cd build

$ cmake ../../../../platform/kl720/ncpu -DCMAKE_TOOLCHAIN_FILE=../xt-toolchain-for-720.cmake -DCMAKE_BUILD_TYPE=Debug
# if no debug symbol version is needed, -DCMAKE_BUILD_TYPE=Release

$ make -j
```

Once you have a successful build, the build binary, ***fw_scpu.bin***, can be found under ***<path_to_720_SDK>/KL720_SDK/firmware/build/ncpu_bin/xcc/build/ncpu_main***

Then, copy the binary file to ***<path_to_720_SDK>/KL720_SDK/firmware/utils/JLink_programmer/bin*** for flash programming later