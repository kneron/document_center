# Getting Started

## 1. Environment Setup

There are several ways to get the Kneron host example:

1. Get the example folder for Linux environment  
Prerequisite: Cmake, OpenCV  
Download the code here: Link
2. Get the VM for the windows and Mac  
Prerequisite: VMware Workstation  
Download the VM here: Link  
Map USB port and share drive into VM: doc link

## 2. File Structure
In the Kneron folder, you will see the following file folders:

```
Kneron-|
       |->app_binaries-|        (KL520 app binaries for example)
                       |-> tiny_yolo_v3
                       |-> ota/ready_to_load
                       |-> ...
       |-> common               (common shared file between host and KL520)
       |-> example              (host program for different example)
       |-> src                  (source files for host lib, which communicate with KL520)
       |-> test_images          (test image binary)
       |-> CMakeList.txt        (top level cmake list)
       |-> README.md            (simple instruction to build)
```

## 3. Compile and Build

This project use cmake to build the code. There is top level CMakelist.txt, and src folder and example folder have their own CMake List. Src folder cmake list is for building the host lib to communicate with KL520. Users usually do not need to modify files under this folder unless they would like to modify the communication protocol. For the example folder, users can modify the cmake list to add more test or their application.

Use Cmake to build:

```bash
mkdir build
cd build
cmake ../ # or 'cmake -DBUILD_OPENCV_EX=on ..' to build with opencv applicaiton
make -j
```

And then you will see the `bin` directory, and all the example executables are under here.

## 4. Run the Default Application Tiny Yolo v3
Tiny Yolo v3 is an object detection algorithm, and it can classify 80 different classes. Kneron device come with build-in binaries that can run 608x608 RGB565 image in Tiny Yolo v3 object detection.

Here is the class list: Link

Let’s take a look at the example program, isi_yolo.cpp. In this test, we send two different images image_608_1.bin and image_608_2.bin (two RGB565 bianries) into KL520, and get the detection results back.

<div align="center">
<img src="../imgs/getting_start_imgs/4_1.png">
</div>

After we setup the images and image buffer size, the program uses kdp_start_isi_mode to notify the communication and inference setup.

<div align="center">
<img src="../imgs/getting_start_imgs/4_2.png">
</div>

Setup image buffer to load the image binaries.

<div align="center">
<img src="../imgs/getting_start_imgs/4_3.png">
</div>

Since the KL520 application design use ping pong buffer to pipeline the image transfer and npu processing, we can fill up the image buffer first. Therefore, we can use kdp_isi_inference to send images to KL520, without getting the result back yet.

<div align="center">
<img src="../imgs/getting_start_imgs/4_4.png">
</div>

Then the program must wait and get back the result then send the next image. It uses kdp_isi_retrieve_res to get the result, then check the result if it matches the expected results. After that, it uses kdp_isi_inference to send another images to KL520 to process. The loop is set to 100 to estimate the average FPS of 100 images.

<div align="center">
<img src="../imgs/getting_start_imgs/4_5.png">
</div>

Lastly, the program needs to retrieve all the remaining image results, using kdp_isi_retrieve_res.

<div align="center">
<img src="../imgs/getting_start_imgs/4_6.png">
</div>

Run the executable binaries, and we can see initialization messages, and the buffer depth is 3. Image index is keep increasing and the expected 2 and 4 objects are toggling because we ping pong transfer two images, so the results are ping pong as 2 objects and 4 objects as well

<div align="center">
<img src="../imgs/getting_start_imgs/4_7.png">
</div>

Lastly, we can see the average FPS for running 100 images is 11.8, each image take average 84ms to finish.

<div align="center">
<img src="../imgs/getting_start_imgs/4_8.png">
</div>

> If there is a python version with swig or native, explain how to use

## 5. Run OTA to Swap Another Pre-build Application Binary Mask Face Detection

Besides Tiny Yolo v3, Kneron also provides many other applications:

* Age_gender: detect faces and return age and gender estimation of the target face
* Cpn_fdr: simple face recognition
* Objection_detection: Kneron 8 class detections
* Ssd_fd: Mask face detection, detect face with mask and without mask

<div align="center">
<img src="../imgs/getting_start_imgs/5_1.png">
</div>

In order to swap the KL520 application, Kneron provides update application feature to update the firmware via USB. Here is an introduction how to do it.

First, user can copy the target application into app_binaries/ota/ready_to_load. Here we will load the mask fd application into KL520. As you can see, there are 3 files, fw_ncpu.bin fw_scpu.bin, and model_ota.bin. Fw_ncpu.bin and Fw_scpu.bin are program binaries that run in the two cpu in KL520. And model_ota.bin is the binary for deep learning models.

<div align="center">
<img src="../imgs/getting_start_imgs/5_2.png">
</div>

Then we can go to build/bin, and run ./update_app. This will load all 3 binaries into KL520, and program them into the flash so that even without power, the KL520 can still maintain the applications. Since the model are relatively large and flash programming is slow, users need to wait for couple mins to update the application. It takes about 3 minutes here.

<div align="center">
<img src="../imgs/getting_start_imgs/5_3.png">
</div>

As you can see the log, the SCPU and NCPU firmware are updated successfully, and model update successfully. Last, it will print out the SCPU firmware id and NCPU firmware id to ensure it is updated with the correct version of code.
After KL520 is updated with the mask face detection, we can start to run this corresponding example. We are going to try the interactive with camera example, therefore, we will make sure we build the apps require opencv. Make sure to do “cmake -DBUILD_OPENCV_EX=on ..” and “make -j” again to make the cam application.

<div align="center">
<img src="../imgs/getting_start_imgs/5_4.png">
</div>

A Camera output window will pop out and use light blue box to get the human face.

<div align="center">
<img src="../imgs/getting_start_imgs/5_5.png">
</div>

And when you put on the mask, there will be a green bounding box around the human face. After 1000 inference, the program will stop.

<div align="center">
<img src="../imgs/getting_start_imgs/5_6.png">
</div>

## 6. Build new model binary based on MobileNet V2 image classification 

Now, let's try to use Kneron tool chain to build a model binary for a public model. In this example, we pick the MobileNet V2 from Keras application. This is a model that doing Image classification, which is 1000 classes from ImageNet. we can get a public MobileNetV2 keras model by executing Python code on Keras 2.2.4.


```python
from keras.applications.mobilenet_v2 import MobileNetV2

model = MobileNetV2(include_top=True, weights='imagenet')
model.save('MobileNetV2.h5')
```

### 6.1. Model Convertion
After getting the keras model, copy the model and a folder of jpg/png images which fall into the categories of ImageNet to /data1 of vm. The recommended size of images is more than 100, which the tools will use it for quantization.

<div align="center">
<img src="../imgs/getting_start_imgs/6_1.png">
</div>

Run toolchain in vm and map ~/data1 folder of vm into /data1 of toolchain

       sudo docker run -it --rm -v ~/data1:/data1 kneron/toolchain:linux_command_toolchain

After that, we will enter toolchain docker container, and it is at workspace/. Check if the /data1 is mapped with the external folder successfully or not.

<div align="center">
<img src="../imgs/getting_start_imgs/6_2.png">
</div>

 Then we can run toolchain in vm to convert the keras model into onnx model. The command is:

       python /workspace/onnx-keras/generate_onnx.py -o /data1/MobileNetV2.h5.onnx /data1/keras/MobileNetV2.h5 -O --duplicate-shared-weights

Then we can see that a MobileNetV2 ONNX model is created under /data1

<div align="center">
<img src="../imgs/getting_start_imgs/6_3.png">
</div>


### 6.2. Model editing (remove softmax at the end)

When we check the MobileNetV2 ONNX model with Netron, we can see that the network's final output layer is a softmax layer, which cannot be handled by KL520 NPU. It is very common to see the softmax layer at the end of classification network, but it is not computation extensive layer, and we can move this softmax layer into network's post process.  

<div align="center">
<img src="../imgs/getting_start_imgs/6_4.png">
</div>

Toolchain provides the Python script (onnx2onnx.py) to optimize the onnx model, and the script (editor.py) to cut layers starting from a specific layer. To remove the softmax layer, we can just simply run the onnx2onnx.py as follow:

       python /workspace/scripts/onnx2onnx2.py /data1/MobileNetV2.h5.onnx -o /data1/MobileNetV2_opt.h5.onnx

After running onnx2onnx.py script, the optimized model MobileNetV2_opt.h5.onnx is saved in /data1. The final layer of the optimized onnx model is Gemm layer now.

<div align="center">
<img src="../imgs/getting_start_imgs/6_5.png">
</div>

<div align="center">
<img src="../imgs/getting_start_imgs/6_6.png">
</div>


### 6.3. Model Compile Flow (compile to all_model.bin and fw_info.bin)

Copy the /workspace/examples/batch_compile_input_params.json into /data1 and modify it before batch-compiling MobileNetV2.

<div align="center">
<img src="../imgs/getting_start_imgs/6_7.png">
</div>

The batch_compile_input_params.json is modified as:  

specify the input_image_folder to be "data1/images", this give the image folder path for the tool to do fixed point analysis.

specify the model input width and height to be "224" and "224", user needs to modify this to fit thier models input size.

tensorflow for public MobileNetV2 as img_preprocess_method. this implies using tensorflow default preprocess, which is `X/127. 5 -1` 

specify the model "input_onnx_file" to be "/data1/MobileNetV2_opt.h5.onnx", which is the model we just edited.

Modify the model_id to be 1000 for MobileNetV2.

<div align="center">
<img src="../imgs/getting_start_imgs/6_8.png">
</div>

Execute the command to batch-compile MobileNetV2 model. 

       cd /workspace/scripts && ./fpAnalyserBatchCompiler.sh.x       

<div align="center">
<img src="../imgs/getting_start_imgs/6_9.png">
</div>

After batch-compilation, a new batch_compile folder with all_models.bin and fw_info.bin is present in /data1. These two binaries will be used for running the model in KL520 later.  

<div align="center">
<img src="../imgs/getting_start_imgs/6_10.png">
</div>

### 6.4. Estimated NPU Run Time for Model

We can use Toolchain to get the evaluation result of NPU performance for Kneron device. The result does not include the time to do pre/post process and cpu node process.
Firstly copy the input_params.json under /workspace/examples to /data1. Same as doing batch compile

<div align="center">
<img src="../imgs/getting_start_imgs/6_11.png">
</div>

Modify the input_params.json as:  tensorflow for public MobileNetV2 as img_preprocess_method, False for add_norm.

<div align="center">
<img src="../imgs/getting_start_imgs/6_12.png">
</div>

Execute the command to run evaluation for MobileNetV2 model. 

       cd /workspace/scripts && ./fpAnalyserCompilerIpevaluator.sh.x

<div align="center">
<img src="../imgs/getting_start_imgs/6_13.png">
</div>

After the evaluation process is finished, we can get the evaluation_result.txt under /data1/compiler.

<div align="center">
<img src="../imgs/getting_start_imgs/6_14.png">
</div>

The evaluation result does not count in the time to do pre/post process and cpu node process. For this MobileNetV2 model, it will take around 15.7ms (total time)

<div align="center">
<img src="../imgs/getting_start_imgs/6_15.png">
</div>


## 7. Run Model Binaries in DME Mode 

Please refer to the example code in example/user_test_dme_async_mobilenet_classification.cpp

### 7.1. DME mode Introduction

In DME mode, the test images, model binaries, and configuration are dynamically sent from host to Kneron device via USB, and the detection results are dynamically retrieved back from Kneron device to host via USB. 

In host side, 5 APIs are used for DME.

| API          | Description   | Note         |
| ------------ | ------------- | ------------ |
| kdp_start_dme | Send model data of all_models.bin/fw_info.bin to Kneron device | Call once |
| kdp_dme_configure	| Send DME configuration to Kneron device	| Call once |
| kdp_dme_inference	| Send image data to Kneron device and start inference	| Call multiple times to send image for inference |
| kdp_dme_get_status	 | Poll the completed status from Kneron device	| Call multiple times after kdp_dme_inference |
| kdp_dme_retrieve_res | Retrieve the inference result (fix-point data) back to host | Call multiple times after kdp_dme_get_status |

### 7.2. DME Mode Pre/Post Process 

Kneron provides default pre/post process function in firmware code if it is run in DME mode. 

### Pre Process

The default preprocess function finish the tasks: 

Reformat: Transfer original format, such as RGB565 or YUV422, to RGBA8888 

Resize: Resize image size to model input size 

Subtract: Subtract the same value for all data

Pad: Pad the same value to any position that applied 

Right-shift if configured 

Because this MobileNetV2 model needs to apply tensorflow preprocess, which is `X/127.5 -1`, it is similar to apply DME default pre process. In section 7.3, we will see how to config the pre process for this MobileNetV2 model.

### Post Process

The default postprocess function in DME mode would send back the original output from KL520 NPU, and user needs to implement post process functions in order to get the correct result. 

finish the tasks: 
1. KL520 send the fix-point data of all output nodes to one with the sequence of total_out_number + (c/h/w/radix/scale) + (c/h/w/radix/scale) + ... + fp_data + fp_data + ...
With this data format, host needs to converts it back to a shared structure `struct kdp_image_s` that can easily identify each output nodes parameters, such as channel, height, width, radix, and scales.

<div align="center">
<img src="../imgs/getting_start_imgs/7_2_1.png">
</div>

2. Host will call actual model post process function `post_imgnet_classificaiton()` in example/post_processing_ex.c

<div align="center">
<img src="../imgs/getting_start_imgs/7_2_2.png">
</div>

In KL520, the results are in 16-byte aligned format for each row, and these values are in fixed point. As a result, host need to convert these values back to floating by using the radix and scale value for each output node. `do_div_scale()` is for this purpose.

<div align="center">
<img src="../imgs/getting_start_imgs/7_2_3.png">
</div>

After converting all the output values back to float, host post process program need to add back the softmax layer, which was cut in model editor (onnx2onnx.py). Lastly, host use qsort to find the top N probability from the 1000 classes. 

<div align="center">
<img src="../imgs/getting_start_imgs/7_2_4.png">
</div>

### 7.3. How to config DME based on the input images

After getting the parameters of input images and models, we can set DME configuration and postprocessing configuration as shown in the example code of dme_async_mobilenet_classification.cpp. 

The following settings mean that the host would send 640x480 RGB565 image to KL520, and KL520 will resize it to 224x224 for model input. Then KL520 will send back raw NPU output back to Host, which suggests host side need to perform post process in order to get the results. Please note that when we compile the model in section 6, we assign model id 1000 to this MobileNetV2 model, and we need to pass this model id in the dme config as well.

<div align="center">
<img src="../imgs/getting_start_imgs/7_3_1.png">
</div>

Then we can call API `kdp_dme_configure()` to config DME.

<div align="center">
<img src="../imgs/getting_start_imgs/7_3_2.png">
</div>

### 7.4. Run DME App

After building the example code using `make -j`, we can run the MobileNetV2 example in command line.

<div align="center">
<img src="../imgs/getting_start_imgs/7_4_1.png">
</div>

The top 5 results for each image is printed out. After finishing the inference for 100 images, the average time of each frame and the fps is calculated and printed out.

<div align="center">
<img src="../imgs/getting_start_imgs/7_4_2.png">
</div>

We can compare the classification index results with the index list on here: [Imagenet Class Index](<https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a>)

## 8. Create New SDK Application

### 8.1. KL520 Firmware Architecture

KL520 firmware is consisted of two bootloaders, IPL and SPL, and two RTOS (Real Time Operating System) images running on system cpu (SCPU) and NPU-assisting cpu (NCPU).

When IPL (Initial Program Loader) in ROM starts to run on SCPU after power-on or reset, it loads SPL (Secondary Program Loader) from flash (automatically or type 1 in UART menu), then SPL loads SCPU firmware image from flash, and finally SCPU firmware loads NCPU firmware image which runs on NCPU.

Both SCPU and NCPU firmware run RTOS with SCPU handling application, media input/output and peripheral drivers and NCPU handling CNN model pre/post processing. Two CPUs use interrupts and shared memory to achieve IPC (Inter Processor Communication).

<div align="center">
<img src="../imgs/getting_start_imgs/8_1_1.png">
</div>

The examples of SDK here are for SCPU RTOS firmware and NCPU RTOS firmware. Both uses ARM Keil RTX.


### 8.2. Firmware components

* SCPU firmware:
    * Project: companion or host
        * a. Output: fw_scpu.bin
    * Libs:
        * a. sdk.lib			-- system/middle/peripheral drivers
        * b. kapp.lib		-- FDR application lib [lib only]
        * c. kdp-system.lib		-- System lib [lib only]
        * d. kcomm.lib		-- Communication handler driver
* NCPU firmware:
    * Project: ncpu
        * a. Output: fw_ncpu.bin
    * Libs:
        * a. kdpio-lib.lib		-- NPU i/o lib [lib only]
        * b. sdk-ncpu.lib		-- NCPU supporting drivers
* Workspace
    * Multiple projects can be organized together
        * a. example_projects/*
    * A workspace includes projects from
        * a. scpu/project/[APP]/[host, companion]/
        * b. scpu/lib/[LIB]
        * c. ncpu/project/[APP]/
        * d. ncpu/lib/[kdpio, sdk-ncpu]

### 8.3. Application Architecture

An application is consisted of one or multiple CNN models for specific purposes, and corresponding preprocessing and postprocessing.
There are many kinds of applications depending on specific use cases. Some application could have their image processing streamlined for best performance and some may not. Some applications could have multiple models, and some may have single model.

A host mode application means that camera(s) and maybe display are located on the same board with KL520, and a companion mode application assumes camera image comes from outside like a different chip or PC.

Tiny Yolo is a single model application with streamlined processing. Both companion mode and host mode are supported. Figure below is a companion mode example. 

<div align="center">
<img src="../imgs/getting_start_imgs/8_3_1.png">
</div>



### 8.4. Create New Application Project

* Use existing application project as template

Example: ./scpu/project/tiny_yolo_v3/companion/
Copy whole directory to a new one with files like this:

```
scpu/project/tiny_yolo_v3/companion/RTE/CMSIS/RTX_Config.c
scpu/project/tiny_yolo_v3/companion/RTE/CMSIS/RTX_Config.h
scpu/project/tiny_yolo_v3/companion/RTE/Device/ARMCM4_FP/startup_ARMCM4.s
scpu/project/tiny_yolo_v3/companion/RTE/Device/ARMCM4_FP/system_ARMCM4.c
scpu/project/tiny_yolo_v3/companion/companion.uvoptx
scpu/project/tiny_yolo_v3/companion/companion.uvprojx
scpu/project/tiny_yolo_v3/companion/main/main.c
scpu/project/tiny_yolo_v3/companion/mozart_96.sct
scpu/project/tiny_yolo_v3/companion/post_build.bat
scpu/project/tiny_yolo_v3/companion/vtor.ini
```

Host mode may include more files to support UART console, camera image inference:

```
scpu/project/tiny_yolo_v3/host/main/main.c
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_console.c
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_inf.c
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_inf.h
```

Furthermore, make sure libraries are included such as these for companion application:

```
kapp.lib
kdp-system.lib
kcomm.lib
sdk.lib
```

Host mode application may include less libraries if no communication (kapp.lib or kcomm.lib) with another chip or PC is needed:

```
kdp-system.lib
sdk.lib
```

### 8.5. Create New NCPU Project

* Use existing application’s Project:ncpu as template

Example: ./ncpu/project/tiny_yolo_v3/
Copy whole directory toa new one with files like this:

```
ncpu/project/tiny_yolo_v3/RTE/CMSIS/RTX_Config.c
ncpu/project/tiny_yolo_v3/RTE/CMSIS/RTX_Config.h
ncpu/project/tiny_yolo_v3/RTE/Device/ARMCM4_FP/startup_ARMCM4.s
ncpu/project/tiny_yolo_v3/RTE/Device/ARMCM4_FP/system_ARMCM4.c
ncpu/project/tiny_yolo_v3/main/main.c
ncpu/project/tiny_yolo_v3/ncpu.uvoptx
ncpu/project/tiny_yolo_v3/ncpu.uvprojx
ncpu/project/tiny_yolo_v3/post_build.bat
```

Also, must include libraries:

```
kdpio-lib.lib
sdk-ncpu.lib
```

### 8.6. Create New Workspace to Include All Projects

* Use existing application’s workspace as template

Copy the workspace.uvmpw file to your directory, add/remove projects as needed.
`example_projects/tiny_yolo_v3_companion/workspace.uvmpw`
A companion application workspace usually contains these projects:

```
Project:sdk
Project:kcomm-lib
Project:companion
Project:sdk-ncpu
Project:ncpu
```

A host application workspace usually contains these projects:
```
Project:sdk
Project:companion
Project:sdk-ncpu
Project:ncpu
```

### 8.7. Create ISI Companion Application

Main tasks in main.c

* Initialize OS
* Initialize SDK with companion mode
`main_init(0)`
* Load ncpu firmware
`main_load_ncpu(0)`
* Initialize communication module
`kcomm_start()`

Add operations for ISI command handler, e.g. in a shared directory/file (app/tiny_yolo_ops.c):
```
static struct kapp_ops kapp_tiny_yolo_ops = {
    .start          = tiny_yolo_start,
    .run_image      = tiny_yolo_run_image,
    .get_result_len = tiny_yolo_get_result_len,
};

/**
  .start: check application id at init time
  .run_image: pass image and parameters to middleware driver to
              run with the model(s) (model id TINY_YOLO_V3 here) 
              of the application
  .get_result_len: tell the length in bytes of a result buffer
**/

struct kapp_ops *tiny_yolo_get_ops(void)
{
    return &kapp_tiny_yolo_ops;
}
```

Register new ops with ISI command handler:
```
struct kapp_ops *ops;

ops = tiny_yolo_get_ops();
kcomm_enable_isi_cmds(ops);
```

#### Support multiple models:
	
When an application includes multiple models, each model needs a separate result memory, and all result memory buffers must be allocated in DDR using kmdw_ddr_reserve() because they are filled up by NCPU.

For companion mode this can be all done in .run_image callback function like age_gender ISI example where two models (KNERON_FDSSD and KNERON_AGE_GENDER) are run one after another.
`scpu/project/age_gender/app/age_gender_ops.c`

#### Parallel image processing for NPU and NCPU:

When incoming images could be fed to NPU running model while previous image’s postposing to run on NCPU in parallel, a parallel bit can be set in image format to enable this feature.

`define IMAGE_FORMAT_PARALLEL_PROC          BIT27`


### 8.8. Create Host Mode Application with MIPI Camera
Main tasks in main.c

* Initialize OS
* Initialize SDK with host mode (camera/display is initialized, ncpu firmware is loaded )
`main_init(1)`
* Initialize application console
`console_entry()`

Add your application needed console/camera/display and inference controls, such as those in:
```
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_console.c
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_inf.c
scpu/project/tiny_yolo_v3/host/main/kapp_tiny_yolo_inf.h
```
Host mode application can use the common operations as in companion mode with example in kapp_tiny_yolo_inf.c:
```
struct kapp_ops *ops;

ops = tiny_yolo_get_ops();
kcomm_enable_isi_cmds(ops);
```

### 8.9. Register New Pre/Post Processing and CPU functions

For application that using new model, users need to register the corresponding pre and post process functions. User can refer to tiny_yolo_v3_companion project's main function in ncpu. 

First, user need to define an new model ID for the model. For example, `TINY_YOLO_V3` is defined model ID for tiny yolo v3 model.

There is a default pre-processing function to handle scaling, cropping, rotation, 0-normalization with hardware acceleration. 

If a special processing is needed for incoming raw image, this API can be called to register in `void pre_processing_add(void)` function.

`kdpio_pre_processing_register(TINY_YOLO_V3, new_pre_yolo_v3);`

Same procedure can be applied to post process as well. We need to add the following into the `void post_processing_add(void)` function.

`kdpio_post_processing_register(TINY_YOLO_V3, new_post_yolo_v3);`

Sometime, KL520 NPU cannot handle some layers in the model, and user need to implement a CPU function to complete the model. The user will require to register the cpu function so that the runtime library knows what to do during the cpu node. Users can do it in `void cpu_processing_add(void)` function, add the cpu funcitons:

`kdpio_cpu_op_register(ZERO_UPSAMPLE, new_zero_upsample_op);`

Please note that user needs to define an new cpu function ID for this cpu function.

## 9. More SDK example code for SOC peripheral drivers

KL520 also provides some simple examples to show how to use basic peripherals such as, I2C, PWM, DMA, GPIO...
User can find them from **sdkexamples** folder.

There is also a PDF file to briefly describe the peripheral APIs. Please down it from the following link:
<div align="center">
<a href="../pdf/KL520_Peripheral_Driver_APIs.pdf">KL520_Peripheral_Driver_APIs.pdf</a>
</div>

