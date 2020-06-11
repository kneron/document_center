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
       |->app_binaries          (KL520 app binaries for example)
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

## 5. Run OTA to Swap Another Pre-build Application Binary (maybe age-gender)

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

## 6. Build New Model Binary (maybe using resnet for classification)

1. explain Model conversion (from keras to onnx)
2. explain Model editing (remove softmax at the end)
3. explain model compile flow (compile to all_model.bin and fw_info.bin)

## 7. Run new model binaries in DME mode (every companion application should be able to initiate DME mode)

1. explain what is DME mode
2. explain pre/post process about the model that going into DME mode
3. explain how to config DME based on the input images
4. explain how to run DME
5. explain the result and performance

## 8. More advance user can dive into SDK example and create their own application

1. explain how to register pre/post process function
2. explain how to register cpu op
3. explain how to make application call in scpu
4. explain how to use host mode template for quick prototype if user like host mode (only for 96 board)
5. explain how to use companion mode template for quick prototype if user like companion mode

## 9. More SDK example code for SOC peripheral drivers

1. refer to API and SDK example project

