# Getting Started

## 1. Environment Setup

There are several ways to get the Kneron host example:

- Get the example folder for **Linux** environment  
    Prerequisite: Cmake, OpenCV  
    Download the code from **[[kl520_sdk_v1.4.0.1.zip]](https://www.kneron.com/tw/support/developers/?folder=KL520%20SDK/&download=492)**, or  **KNEO Stem (USB Dongle) -> host_lib** in **[Kneron Develop Center](https://www.kneron.com/tw/support/developers/) :** 

- Get the VM for the **windows** and **Mac**  
     Prerequisite: VMware Workstation  
       Download the VM  total five files :**[Part1](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=276)**  **[Part2](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=277)** **[Part3](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=278)** **[Part4](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=279)**  **[Part5](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=280)**

       Map USB port and share drive into VM: **[Link](http://www.kneron.com/tw/support/developers/?folder=KNEO%20Stem%20(USB%20Dongle)/VM%20ubuntu/&download=251)**




## 2. File Structure
In the host_lib folder, you will see the following file folders:

```
host_lib-|
         |->app_binaries-|        (KL520 app binaries for example)
                         |-> *KL520/tiny_yolo_v3
                         |-> *KL520/ota/ready_to_load
                         |-> ...
         |-> common               (common shared file between host and KL520)
         |-> dll                  (dll files for Windows MINGW64)
         |-> docs                 (images in README)
         |-> example/KL520        (host program for different C++ examples)
         |-> kdp2                 (source files for new Host KDP2 API)
         |-> python               (host program for different Python examples)
         |-> src                  (source files for host lib, which communicate with KL520)
         |-> input_images         (test image binary)
         |-> input_models/*KL520  (models for examples)
         |-> CMakeList.txt        (top level cmake list)
         |-> README_CPP.md        (simple instruction to build for C++ examples)
         |-> README_Python.md     (simple instruction for Python examples)


*KL520 stands for KL520 examples/models
 KL720 stands for KL720 examples/models
```



## 3. Compile and Build

This project use cmake to build the code. There is top level ```CMakeLists.txt```, and ```src``` folder and ```example/KL520``` folder have their own ```CMakeLists.txt```. 

- ```src``` folder cmake list is for building the host lib to communicate with KL520. Users usually do not need to modify files under this folder unless they would like to modify the communication protocol. 
- For ``` example``` folder, users can modify the cmake list to add more test or their application.

Use Cmake to build:

```bash
# in linux
mkdir build
cd build
cmake ../ # or append '-DBUILD_OPENCV_EX=on ..' to build with opencv applicaiton
make -j
```

And then you will see the `bin` directory, and all the example executables are under here.



## 4. Run the Default Application Tiny Yolo v3
Tiny Yolo v3 is an object detection algorithm, and it can classify 80 different classes. 

Kneron device come with build-in binaries that can run 608x608 RGB565 image in Tiny Yolo v3 object detection.



### 4.1 C++ Example

Let’s take a look at the C++ example program, ```kl520_isi_async_parallel_yolo.cpp```. 
In this test, we send two different images ```cars_street_at_night_608x608_rgb565.bin``` and ```car_park_barrier_608x608_rgb565.bin``` (two RGB565 binaries) into KL520, and get the detection results back.

```cpp
#define ISI_IMAGE_FILE      (HOST_LIB_DIR "/input_images/cars_street_at_night_608x608_rgb565.bin")
#define ISI_IMAGE_FILE_T    (HOST_LIB_DIR "/input_images/car_park_barrier_608x608_rgb565.bin")
#define IMG_SOURCE_W        608
#define IMG_SOURCE_H        608
#define ISI_IMG_SIZE        (IMG_SOURCE_W * IMG_SOURCE_H * 2)
#define ISI_APP_ID          APP_TINY_YOLO3
// isi initial result memory size in bytes
#define ISI_RESULT_SIZE     2048
```

After we setup the images and image buffer size, the program uses kdp_start_isi_mode to notify the communication and inference setup.

```cpp
uint16_t width  = IMG_SOURCE_W;
uint16_t height = IMG_SOURCE_H;
// image format flags
// IMAGE_FORMAT_SUB128: subtract 128 for R/G/B value in Kneron device
// NPU_FORMAT_RGB565: image input is RGB565
// IMAGE_FORMAT_PARALLEL_PROC: pipeline between ncpu and npu
uint32_t format = IMAGE_FORMAT_SUB128 | NPU_FORMAT_RGB565 | IMAGE_FORMAT_PARALLEL_PROC;

// Flash the firmware code with companion mode for tiny_yolo_v3 !!!
printf("starting ISI mode ...\n");
// call kdp_start_isi_mode to start isi mode        
int ret = kdp_start_isi_mode(
    dev_idx, ISI_APP_ID, ISI_RESULT_SIZE, width, height, format, &error_code, &image_buf_size);
if (ret != 0) {
    printf("could not set to ISI mode: %d ..\n", ret);
    return -1;
}

if (image_buf_size < 3) {
    printf("ISI mode window %d too small...\n", image_buf_size);
    return -1;
}

printf("ISI mode succeeded (window = %d)...\n", image_buf_size);
usleep(SLEEP_TIME);
```

Setup image buffer to load the image binaries.

```cpp
int n_len = read_file_to_buf(img_buf1, ISI_IMAGE_FILE, ISI_IMG_SIZE);
if (n_len <= 0) {
    printf("reading image file 1 failed:%d...\n", n_len);
    return -1;
}

n_len = read_file_to_buf(img_buf2, ISI_IMAGE_FILE_T, ISI_IMG_SIZE);
if (n_len <= 0) {
    printf("reading image file 2 failed:%d...\n", n_len);
    return -1;
}
```

Since the KL520 application design uses image buffer to pipeline the image transfer and npu processing, we can fill up the image buffer first. Therefore, we can use kdp_isi_inference to send images to KL520, without getting the result back yet.

```cpp
printf("starting ISI inference ...\n");
uint32_t img_id_tx = 1234;
uint32_t img_id_rx = img_id_tx;
uint32_t img_left = 12;
uint32_t result_size = 0;
uint32_t buf_len = ISI_IMG_SIZE;
char inf_res[ISI_RESULT_SIZE];

// start time for the first frame
double start_time = what_time_is_it_now();

// Send 2 images first
// do inference for each input
ret = do_inference(dev_idx, img_buf1, buf_len, img_id_tx, &error_code, &img_left);
if (ret)
    return ret;
img_id_tx++;
// do inference for each input
ret = do_inference(dev_idx, img_buf2, buf_len, img_id_tx, &error_code, &img_left);
if (ret)
    return ret;
img_id_tx++;

// Send the rest and get result in loop, with 2 images alternatively
uint32_t loop = 0;
if (test_loop > 3)
    loop = test_loop - 2;

while (loop && !check_ctl_break()) {
    // do inference for each input
    ret = do_inference(dev_idx, img_buf1, buf_len, img_id_tx, &error_code, &img_left);
    if (ret)
        return ret;
    img_id_tx++;
```

Then the program must wait and get back the result then send the next image. It uses kdp_isi_retrieve_res to get the result. After that, it uses kdp_isi_inference to send another images to KL520 to process. The loop is set to 300 to estimate the average FPS of 300 images.

```cpp
    ret = do_get_result(dev_idx, img_id_rx, &error_code, &result_size, inf_res);
    if (ret)
        return ret;
    img_id_rx++;

    loop--;
    // Odd loop case
    if (loop == 0)
        break;
    // do inference for each input
    ret = do_inference(dev_idx, img_buf2, buf_len, img_id_tx, &error_code, &img_left);
    if (ret)
        return ret;
    img_id_tx++;

    // retrieve the detection results for each input
    ret = do_get_result(dev_idx, img_id_rx, &error_code, &result_size, inf_res);
    if (ret)
        return ret;
    img_id_rx++;

    loop--;
}
```

Then, the program needs to retrieve all the remaining image results, using kdp_isi_retrieve_res.

```cpp
// Get last 2 results
// retrieve the detection results for each input
ret = do_get_result(dev_idx, img_id_rx, &error_code, &result_size, inf_res);
if (ret)
    return ret;
img_id_rx++;
// retrieve the detection results for each input
ret = do_get_result(dev_idx, img_id_rx, &error_code, &result_size, inf_res);
if (ret)
    return ret;
img_id_rx++;
// calculate the FPS
if (1) {
    double end_time = what_time_is_it_now();
    double elapsed_time, avg_elapsed_time, avg_fps;

    elapsed_time = (end_time - start_time) * 1000;
    avg_elapsed_time = elapsed_time / test_loop;
    avg_fps = 1000.0f / avg_elapsed_time;

    printf("\n=> Avg %.2f FPS (%.2f ms = %.2f/%d)\n\n",
        avg_fps, avg_elapsed_time, elapsed_time, test_loop);
}
```

Lastly, the program calls kdp_end_isi to end isi mode.
```cpp
// call kdp_end_isi to end isi mode after finishing the inference for all frames
kdp_end_isi(dev_idx);
```

Run the executable binaries, and we can see initialization messages, and the buffer depth is 3. Image index is keep increasing and the expected 5 and 3 objects are toggling because we ping pong transfer two images, so the results are ping pong as 5 objects and 3 objects as well

```bash
Kneron@Ubuntu:~/host_lib/build/bin$ ./kl520_isi_async_parallel_yolo
init kdp host lib log....
adding devices....
start kdp host lib....
doing test :0....
starting ISI mode ...
ISI mode succeeded (window = 3)...
starting ISI inference ...
image 1234 -> 5 object(s)
image 1235 -> 3 object(s)
image 1236 -> 5 object(s)
image 1237 -> 3 object(s)
```

Lastly, we can see the average FPS for running 300 images is 11.7, each image take average 85ms to finish.

```bash
image 1532 -> 5 object(s)
image 1533 -> 3 object(s)

=> Avg 11.70 FPS (85.46 ms = 25637.14/300)

de init kdp host lib....
```



### 4.2. Python Example

Let’s take a look at the Python example program (path=```python/examples_kl520```), ```cam_isi_async_parallel_yolo.py```. In this test, we send frames (RGB565) of camera into KL520, and get the detection results back.

Setup video capture device for the image width and height

```python
"""User test cam yolo."""
image_source_h = 480
image_source_w = 640
app_id = constants.APP_TINY_YOLO3
image_size = image_source_w * image_source_h * 2
frames = []

# Setup video capture device.
capture = kdp_wrapper.setup_capture(0, image_source_w, image_source_h)
if capture is None:
    return -1
```

After we setup the video capture device, the program uses start_isi_parallel to notify the communication and inference setup.

```python
# Start ISI mode.
if kdp_wrapper.start_isi_parallel_ext(dev_idx, app_id, image_source_w, image_source_h):
    return -1
```

Since the KL520 application design use image buffer to pipeline the image transfer and npu processing, we can fill up the image buffer first. Therefore, we can use fill_buffer to send frames to KL520, without getting the result back yet.

```python
start_time = time.time()
# Fill up the image buffers.
ret, img_id_tx, img_left, buffer_depth = kdp_wrapper.fill_buffer(
    dev_idx, capture, image_size, frames)
if ret:
    return -1
```

Then the program must wait and get back the result then send the next image. It uses pipeline_inference to get the result and to send another images to KL520 to process. The loop is set to 1000 to estimate the average FPS of 1000 images.

```python
# Send the rest and get result in loop, with 2 images alternatively
print("Companion image buffer depth = ", buffer_depth)
kdp_wrapper.pipeline_inference(
    dev_idx, app_id, test_loop - buffer_depth, image_size,
    capture, img_id_tx, img_left, buffer_depth, frames, handle_result)

end_time = time.time()
diff = end_time - start_time 
estimate_runtime = float(diff/test_loop)
fps = float(1/estimate_runtime)    
print("Parallel inference average estimate runtime is ", estimate_runtime)
print("Average FPS is ", fps)
```

Lastly, the program calls kdp_end_isi to end isi mode.
```python
kdp_wrapper.kdp_exit_isi(dev_idx)
```

Run the Python example, and we can see initialization messages, and the buffer depth is 3. Image index keeps increasing and the number of detected objects are outputted

```bash
$ python3 main.py -t cam_isi_aync_parallel_yolo
adding devices...
start kdp host lib....
Task:    cam_isi_aysnc_parallel_yolo
starting ISI mode...
ISI mode succeeded (window = 3)...
starting ISI inference ...
Companion image buffer depth =  3
image 1234 -> 1 object(s)
image 1235 -> 1 object(s)
image 1236 -> 1 object(s)
image 1237 -> 2 object(s)
```

Lastly, we can see the average FPS for running 1000 images is 12.2, each image take average 82ms to finish.

```bash
image 2233 -> 2 object(s)

Parallel inference average estimate runtime is  0.08506509852409362
Average FPS is  11.755702601305547
de init kdp host lib....
```




## 5. Run OTA to Swap Another Pre-build Application Binary Mask Face Detection

Besides Tiny Yolo v3, Kneron also provides the following for OTA usage example

* **ssd_fd_lm**: Mask face detection, detect face with mask and without mask

```shell
Kneron@ubuntu:~/host_lib/app_binaries/KL520$ ls
ota/  readme.txt  ssd_fd_lm/  tiny_yolo_v3/
```



In order to swap the KL520 application, Kneron provides update application feature to update the firmware via USB. 

Here is an introduction how to do it.

First, user can copy the target application into ``app_binaries/KL520/ota/ready_to_load``. Here we will load the mask fd application into KL520. 
As you can see, there are 3 files, 

- ``fw_ncpu.bin`` ``fw_scpu.bin`` from parent folders, are program binaries that run in the two cpu cores in KL520.
- ``models_520.nef`` from model folder, is the binary for deep learning models

```shell
Kneron@ubuntu:~/host_lib/app_binaries/KL520/ota/ready_to_load$ cp ../../ssd_fd_lm/*.bin .
Kneron@ubuntu:~/host_lib/app_binaries/KL520/ota/ready_to_load$ cp ../../../../input_models/KL520/ssd_fd_lm/models_520.nef .
Kneron@ubuntu:~/host_lib/app_binaries/KL520/ota/ready_to_load$ ls
fw_ncpu.bin  fw_scpu.bin  models_520.nef
```



Then we can go to ``build/bin``, and run ``./update_app``. This will load all 3 binaries into KL520, and program them into the flash so that even without power, the KL520 can still maintain the applications. Since the model are relatively large and flash programming is slow, users need to wait for couple mins to update the application. It takes about 3-5 minutes here.

```shell
Kneron@ubuntu:~/host_lib/build/bin$ ./update_app_nef_model
init kdp host lib log....
adding devices....
start kdp host lib....
doing test :0....
starting update fw ...
update SCPU firmware successed...
update NCPU firmware successed...
starting update model :1...
update model succeeded...
starting report sys status ...
report sys status succeeded...

SCPU firmware_id 01040000 build_id 00000000
SCPU firmware_id 01030001 build_id 00000002

de init kdp host lib....
```



As you can see the log, the SCPU and NCPU firmware are updated successfully, and model update successfully. Last, it will print out the SCPU firmware id and NCPU firmware id to ensure it is updated with the correct version of code.

After KL520 is updated with the mask face detection, we can start to run this corresponding example. We are going to try the interactive with camera example, therefore, we will make sure we build the apps require **opencv**. Make sure to do ``cmake -DBUILD_OPENCV_EX=on `` and ``make -j`` again to make the cam application.

```shell
Kneron@ubuntu:~/host_lib/build/bin$ ./k520_cam_isi_async_ssd_fd
```



A Camera output window will pop out and use light blue box to get the human face.

![](./imgs/getting_start_imgs/5_5.png)

And when you put on the mask, there will be a green bounding box around the human face. After 1000 inference, the program will stop.

![](./imgs/getting_start_imgs/5_6.png)


## 6. Build New Model Binary Based on MobileNet V2 Image Classification 

Now, let's try to use **Kneron tool chain** to build a model binary for a public model. 

In this example, we pick the MobileNet V2 from Keras application. This is a model that doing Image classification, which is 1000 classes from ImageNet. we can get a public MobileNetV2 keras model by executing Python code on Keras 2.2.4.


```python
from keras.applications.mobilenet_v2 import MobileNetV2

model = MobileNetV2(include_top=True, weights='imagenet')
model.save('MobileNetV2.h5')
```



### 6.1. Model Conversion

After getting the keras model, copy the model and a folder of jpg/png images which fall into the categories of ImageNet to /data1 of vm. The recommended size of images is more than 100, which the tools will use it for quantization.

```shell
Kneron@ubuntu:~/data1$ ls
images/ MobileNetV2.h5
```



Run toolchain in vm and map ~/data1 folder of vm into /data1 of toolchain

    $ sudo docker run -it --rm -v ~/data1:/data1 kneron/toolchain:linux_command_toolchain



After that, we will enter toolchain docker container, and it is at workspace/. Check if the /data1 is mapped with the external folder successfully or not.

```shell
root@6093d5502017:/workspace# ls
README.md	libs		onnx-keras		requirements.txt		tmp
examples	onnx-caffe	onnx-tensorflow	scripts
root@6093d5502017:/workspace# cd /data1
root@6093d5502017:/data1# ls
images/ MobileNetV2.h5
```



 Then we can run toolchain in vm to convert the keras model into onnx model. The command is:

    $ python /workspace/onnx-keras/generate_onnx.py -o /data1/MobileNetV2.h5.onnx /data1/keras/MobileNetV2.h5 -O --duplicate-shared-weights



Then we can see that a MobileNetV2 ONNX model is created under /data1

```shell
root@6093d5502017:/data1# ls
images/ 	MobileNetV2.h5	 MobileNetV2.h5.onnx
```



### 6.2. Model editing (remove softmax at the end)

When we check the MobileNetV2 ONNX model with Netron, we can see that the network's final output layer is a softmax layer, which cannot be handled by KL520 NPU. It is very common to see the softmax layer at the end of classification network, but it is not computation extensive layer, and we can move this softmax layer into network's post process.  

![](./imgs/getting_start_imgs/6_4.png)

Toolchain provides the Python script (onnx2onnx.py) to optimize the onnx model, and the script (editor.py) to cut layers starting from a specific layer. To remove the softmax layer, we can just simply run the onnx2onnx.py as follow:

    $ python /workspace/scripts/onnx2onnx2.py /data1/MobileNetV2.h5.onnx -o /data1/MobileNetV2_opt.h5.onnx

After running onnx2onnx.py script, the optimized model MobileNetV2_opt.h5.onnx is saved in /data1. The final layer of the optimized onnx model is Gemm layer now.

```shell
root@6093d5502017:/data1# ls
images/ 	MobileNetV2.h5	 MobileNetV2.h5.onnx   MobileNetV2_opt.h5.onnx  
```


![](./imgs/getting_start_imgs/6_6.png)


### 6.3. Model Compile Flow (compile to .nef file)

Copy the /workspace/examples/batch_compile_input_params.json into /data1 and modify it before batch-compiling MobileNetV2.

```shell
root@6093d5502017:/data1# cp /workspace/examples/batch_compile_input_params.json .

root@6093d5502017:/data1# ls
images/ 				 MobileNetV2.h5	 				  MobileNetV2.h5.onnx   
MobileNetV2_opt.h5.onnx  batch_compile_input_params.json
```




The ``batch_compile_input_params.json`` is modified as:  

specify the input_image_folder to be ``data1/images``, this give the image folder path for the tool to do fixed point analysis.

specify the model input width and height to be "224" and "224", user needs to modify this to fit thier models input size.

tensorflow for public MobileNetV2 as img_preprocess_method. this implies using tensorflow default preprocess, which is `X/127. 5 -1` 

specify the model "input_onnx_file" to be ``/data1/MobileNetV2_opt.h5.onnx``, which is the model we just edited.

Modify the model_id to be 1000 for MobileNetV2.

```json
{
    "input_image_folder": ["/data1/images"],
    "img_channel": ["RGB"],
    "model_input_width": [224],
    "model_input_height": [224],
    "img_preprocess_method": ["tensorflow"],
    "input_onnx_file": ["/data1/MobileNetV2_opt.h5.onnx"],
    "keep_aspect_ratio": ["False"],
    "command_addr": "0x30000000",
    "weight_addr": "0x40000000",
    "sram_addr": "0x50000000",
    "dram_addr": "0x60000000",
    "whether_encryption": "No",
    "encryption_key": "0x12345678",
    "model_id_list": [1000],
    "model_version_list": [1],
    "add_norm_list": ["False"],
    "dedicated_output_buffer": "True"
}
```


Execute the command to batch-compile MobileNetV2 model. 

    $ cd /workspace/scripts && ./fpAnalyserBatchCompiler.sh.x       

![](./imgs/getting_start_imgs/6_9.png)

After batch-compilation, a new batch_compile folder with .nef file is present in /data1. This file will be used for running the model in KL520 later.  

![](./imgs/getting_start_imgs/6_10.png)


### 6.4. Estimated NPU Run Time for Model

We can use Toolchain to get the evaluation result of NPU performance for Kneron device. The result does not include the time to do pre/post process and cpu node process.
Firstly copy the input_params.json under /workspace/examples to /data1. Same as doing batch compile

![](./imgs/getting_start_imgs/6_11.png)

Modify the input_params.json as:  tensorflow for public MobileNetV2 as img_preprocess_method, False for add_norm.

```json
{
    "input_image_folder": ["/data1/images"],
    "img_channel": ["RGB"],
    "model_input_width": [224],
    "model_input_height": [224],
    "img_preprocess_method": ["tensorflow"],
    "input_onnx_file": ["/data1/MobileNetV2_opt.h5.onnx"],
    "keep_aspect_ratio": ["False"],
    "command_addr": "0x30000000",
    "weight_addr": "0x40000000",
    "sram_addr": "0x50000000",
    "dram_addr": "0x60000000",
    "whether_encryption": "No",
    "encryption_key": "0x12345678",
    "simulator_img_file": "/data1/images/n01503061_3560_bird.jpg",
    "emulator_img_folder": "/data1/images",
    "cmd_bin": "/data1/compiler/command.bin",
    "weight_bin": "/data1/compiler/weight.bin",
	"setup.bin": "/data1/compiler/setup.bin",
    "whether_npu_preprocess": false,
    "raw_img_fmt": "IMG",
    "radix": 8,
    "pad_mode": 1,
    "roate":0,
    "pCrop": {
        "crop_x": 0,
        "crop_y": 0,
        "crop_w": 0,
        "crop_h": 0,
        "bCropFirstly": false
    },
    "imgSize":{
        "width": 640,
        "height": 480
    },
    "add_norm": "False"
}
```




Execute the command to run evaluation for MobileNetV2 model. 

```shell
 $ cd /workspace/scripts && ./fpAnalyserCompilerIpevaluator.sh.x
```

![](./imgs/getting_start_imgs/6_13.png)

After the evaluation process is finished, we can get the evaluation_result.txt under /data1/compiler.

```shell
root@92ace5540942:/data1# cd complier/
root@92ace5540942:/data1/complier# ls
command.bin  evaluation_result.txt  setup.bin  weight.bin
```



The evaluation result does not count in the time to do pre/post process and cpu node process. For this MobileNetV2 model, it will take around 15.7ms (total time)

```
[Evaluation Result]
estimate FPS float = 63.6315
total time = 15.7105 ms
total theoretical covolution time = 3.81611 ms
average DRAM bandwidth = 0.386193 GB/s
MAC efficiency to total time = 24.2901 %
MAC idle time = 2.3849 ms
MAC running time = 13.3256 ms
```



## 7. Run Model Binaries in DME Mode 

Please refer to the example code in ``example/KL520/kl520_dme_async_mobilenet_classification``



### 7.1. DME mode Introduction

In DME mode, the test images, model binaries, and configuration are dynamically sent from host to Kneron device via USB, and the detection results are dynamically retrieved back from Kneron device to host via USB. 

In host side, 6 APIs are used for DME.

| API          | Description   | Note         |
| ------------ | ------------- | ------------ |
| kdp_start_dme_ext | Send model data of **models_520.nef**  to Kneron device | Call once |
| kdp_dme_configure	| Send DME configuration to Kneron device	| Call once |
| kdp_dme_inference	| Send image data to Kneron device and start inference	| Call multiple times to send image for inference |
| kdp_dme_get_status	 | Poll the completed status from Kneron device	| Call multiple times after kdp_dme_inference (only in DME async mode) |
| kdp_dme_retrieve_res | Retrieve the inference result (fix-point data) back to host | Call multiple times after kdp_dme_get_status |
| kdp_end_dme | End DME mode by sending command to Kneron device | Call once |


### 7.2. DME Mode Pre/Post Process 

Kneron provides default pre/post process function in firmware code if it is run in DME mode. 

### Pre Process

The default preprocess function finish the tasks: 

**Reformat**: Transfer original format, such as RGB565 or YUV422, to RGBA8888 

**Resize**: Resize image size to model input size 

**Subtract**: Subtract 128 for all data if configured 

**Right-shift for 1 bit** if configured 

Because this MobileNetV2 model needs to apply tensorflow preprocess, which is `X/127.5 -1`, it is similar to apply DME default pre process. In section 7.3, we will see how to config the pre process for this MobileNetV2 model.



### Post Process

The default postprocess function in DME mode would send back the original output from KL520 NPU, and user needs to implement post process functions in order to get the correct result. 

finish the tasks: 
1. KL520 send the fix-point data of all output nodes to one with the sequence of total_out_number + (c/h/w/radix/scale) + (c/h/w/radix/scale) + ... + fp_data + fp_data + ...
    With this data format	, host needs to converts it back to a shared structure `struct kdp_image_s` that can easily identify each output nodes parameters, such as channel, height, width, radix, and scales.

  ```c
      // Prepare for postprocessing
      int output_num = inf_res[0];
      struct output_node_params *p_node_info;
      int r_len, offset;
      struct imagenet_result_s *det_res = (struct imagenet_result_s *)calloc(IMAGENET_TOP_MAX, sizeof(imagenet_result_s));
  
      struct kdp_image_s *image_p = (struct kdp_image_s *)calloc(1, sizeof(struct kdp_image_s));
      offset = sizeof(int) + output_num * sizeof(output_node_params);
  
      // Struct to pass the parameters
      RAW_INPUT_COL(image_p) = post_par.raw_input_col;
      RAW_INPUT_ROW(image_p) = post_par.raw_input_row;
      DIM_INPUT_COL(image_p) = post_par.model_input_row;
      DIM_INPUT_ROW(image_p) = post_par.model_input_row;
      RAW_FORMAT(image_p) = post_par.image_format;
      POSTPROC_RESULT_MEM_ADDR(image_p) = (uint32_t *)det_res;
      POSTPROC_OUTPUT_NUM(image_p) = output_num;
  
      for (int i = 0; i < output_num; i++) {
          if (check_ctl_break())
              return;
          p_node_info = (struct output_node_params *)(inf_res + sizeof(int) + i * sizeof(output_node_params));
          r_len = p_node_info->channel * p_node_info->height * round_up(p_node_info->width);
  
          POSTPROC_OUT_NODE_ADDR(image_p, i) = inf_res + offset;
          POSTPROC_OUT_NODE_ROW(image_p, i) = p_node_info->height;
          POSTPROC_OUT_NODE_CH(image_p, i) = p_node_info->channel;
          POSTPROC_OUT_NODE_COL(image_p, i) = p_node_info->width;
          POSTPROC_OUT_NODE_RADIX(image_p, i) = p_node_info->radix;
          POSTPROC_OUT_NODE_SCALE(image_p, i) = p_node_info->scale;
  
          offset = offset + r_len;
      }
  
  ```


2. Host will call actual model post process function `post_imgnet_classificaiton()` in example/post_processing_ex.c

```c
int post_imgnet_classification(int model_id, struct kdp_image_s *image_p)
{
   struct imagenet_post_globals_s *gp = &u_globals.imgnet;
   uint8_t *result_p;
   int i, len, data_size, div;
   float scale;

   data_size = (POSTPROC_OUTPUT_FORMAT(image_p) & BIT(0)) + 1;     /* 1 or 2 in bytes */

   int8_t *src_p = (int8_t *)POSTPROC_OUT_NODE_ADDR(image_p, 0);
   int grid_w = POSTPROC_OUT_NODE_COL(image_p, 0);
   len = grid_w * data_size;
   int grid_w_bytes_aligned = round_up(len);
   int w_bytes_to_skip = grid_w_bytes_aligned - len;
   len = grid_w_bytes_aligned;

   int ch = POSTPROC_OUT_NODE_CH(image_p, 0);

   /* Convert to float */
   scale = POSTPROC_OUT_NODE_SCALE(image_p, 0);
   div = 1 << POSTPROC_OUT_NODE_RADIX(image_p, 0);
   for (i = 0; i < ch; i++) {
       gp->temp[i].index = i;
       gp->temp[i].score = (float)*src_p;
       gp->temp[i].score = do_div_scale(gp->temp[i].score, div, scale);
       src_p += data_size + w_bytes_to_skip;
   }

   softmax(gp->temp, ch);
   qsort(gp->temp, ch, sizeof(struct imagenet_result_s), inet_comparator);

   result_p = (uint8_t *)(POSTPROC_RESULT_MEM_ADDR(image_p));
   len = sizeof(struct imagenet_result_s) * IMAGENET_TOP_MAX;
   memcpy(result_p, gp->temp, len);
   return len;
}
```

   

In KL520, the results are in 16-byte aligned format for each row, and these values are in fixed point. As a result, host need to convert these values back to floating by using the radix and scale value for each output node. `do_div_scale()` is for this purpose.

```c
static float do_div_scale(float v, int div, float scale)
{
	return ((v / div) / scale);
}
```



After converting all the output values back to float, host post process program need to add back the softmax layer, which was cut in model editor (onnx2onnx.py). Lastly, host use qsort to find the top N probability from the 1000 classes. 

```c
softmax(gp->temp, ch);
qsort(gp->temp, ch, sizeof(struct imagenet_result_s), inet_comparator);
```




### 7.3. How to config DME based on the input images

After getting the parameters of input images and models, we can set DME configuration and postprocessing configuration as shown in the example code of kl520_	dme_async_mobilenet_classification.cpp. 

The following settings mean that the host would send 640x480 RGB565 image to KL520, and KL520 will resize it to 224x224 for model input. Then KL520 will send back raw NPU output back to Host, which suggests host side need to perform post process in order to get the results. Please note that when we compile the model in section 6, we assign model id 1000 to this MobileNetV2 model, and we need to pass this model id in the dme config as well.

```c
// parameters for postprocessing
post_par.raw_input_col   = 640;
post_par.raw_input_row   = 480;
post_par.model_input_row = 224;
post_par.model_input_col = 224;
post_par.image_format    = IMAGE_FORMAT_SUB128 	| 
                           NPU_FORMAT_RGB565 	| 
                           IMAGE_FORMAT_RAW_OUTPUT  | 
                           IMAGE_FORMAT_CHANGE_ASPECT_RATIO;

// dme configuration
dme_cfg.model_id     = IMAGENET_CLASSIFICATION_MOBILENET_V2_224_224_3;// model id when compiling in toolchain
dme_cfg.output_num   = 1;                             // number of output node for the model
dme_cfg.image_col    = post_par.raw_input_col;
dme_cfg.image_row    = post_par.raw_input_row;
dme_cfg.image_ch     = 3;
dme_cfg.image_format = post_par.image_format;
```

Then we can call API `kdp_dme_configure()` to config DME.

```c
dat_size = sizeof(struct kdp_dme_cfg_s);
printf("starting DME configure ...\n");
int ret = kdp_dme_configure(dev_idx, (char *)&dme_cfg, dat_size, &model_id);
if (ret != 0) {
    printf("could not set to DME configure mode..\n");
    return -1;
}
printf("DME configure model [%d] succeeded...\n", model_id);
```




### 7.4. Run DME App

After building the example code using `make -j`, we can run the MobileNetV2 example in command line.

```shell
Kneron@ubuntu:~/host_lib/build/bin$ ./kl520_dme_async_mobilenet_classificaiton
```



The top 5 results for each image is printed out. After finishing the inference for 100 images, the average time of each frame and the fps is calculated and printed out.

```shell
/****************Top 5 Results***********************/
Index 281: score 0.595752
Index 285: score 0.162995
Index 282: score 0.146307
Index 904: score 0.007110
Index 173: score 0.001945
/****************Top 5 Results***********************/
Index 169: score 0.344763
Index 247: score 0.309466
Index 256: score 0.044287
Index 188: score 0.015038
Index 215: score 0.015038
[INFO] average time on 100 frames: 48.570648 ms/frame, fps: 20.588566
```


We can compare the classification index results with the index list on here: [Imagenet Class Index](<https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a>)



## 8. Create New SDK Application



### 8.1. KL520 Firmware Architecture

KL520 firmware is consisted of two bootloaders, IPL and SPL, and two RTOS (Real Time Operating System) images running on system cpu (SCPU) and NPU-assisting cpu (NCPU).

When IPL (Initial Program Loader) in ROM starts to run on SCPU after power-on or reset, it loads SPL (Secondary Program Loader) from flash (automatically or type 1 in UART menu), then SPL loads SCPU firmware image from flash, and finally SCPU firmware loads NCPU firmware image which runs on NCPU.

Both SCPU and NCPU firmware run RTOS with SCPU handling application, media input/output and peripheral drivers and NCPU handling CNN model pre/post processing. Two CPUs use interrupts and shared memory to achieve IPC (Inter Processor Communication).

![](./imgs/getting_start_imgs/8_1_1.png)

The examples of SDK here are for SCPU RTOS firmware and NCPU RTOS firmware. Both uses ARM Keil RTX.

> download the firmware source code: KL520 SDK section in [Kneron Develop Center](https://www.kneron.com/tw/support/developers/)

### 8.2. Firmware components

* SCPU firmware:
    * Project: companion or host
        * Output: fw_scpu.bin
    * Libs:
        * sdk.lib			-- system/middle/peripheral drivers
        * kapp.lib			-- FDR application lib **[lib only]**
        * kdp-system.lib	-- System lib **[lib only]**
        * kcomm.lib			-- Communication handler driver
* NCPU firmware:
    * Project: ncpu
        * Output: fw_ncpu.bin
    * Libs:
        * kdpio-lib.lib		-- NPU i/o lib **[lib only]**
        * sdk-ncpu.lib		-- NCPU supporting drivers
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

![](./imgs/getting_start_imgs/8_3_1.png)



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
```c
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
```c
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
```c
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

## 9. SOC peripheral drivers
This chapter describes the peripheral definitions and prototypes for the application progamming reference.

User can find the code in the following folder.

├───scpu<br>
│   ├───config<br>
│   ├───device<br>
│   ├───drivers<br>
│   ├───framework<br>
│   ├───kapp<br>
│   ├───kdev<br>
│   ├───<font color="#0000dd">**kdrv_KL520**</font><br>
│   ├───kmdw<br>
│   ├───lib<br>
│   ├───project<br>

KL520 SDK also provides some simple examples to show how to use basic peripherals such as, I2C, PWM, DMA, GPIO...

User can find them from the following folder.

├───bootloader<br>
├───...<br>
├───scpu<br>
├───<font color="#0000dd">**sdkexamples**</font><br>
├───utils<br>

We hope that the peripheral examples can help user to test it on your board and hopefully base it to desgign your application.

User can also refer to kdrv usage from the middleware(mdw) folder.

├───scpu<br>
│   ├───config<br>
│   ├───device<br>
│   ├───drivers<br>
│   ├───framework<br>
│   ├───kapp<br>
│   ├───kdev<br>
│   ├───kdrv_KL520<br>
│   ├───<font color="#0000dd">**kmdw**</font><br>
│   ├───lib<br>
│   ├───project<br>

### 9.0. Peripheral Name Description
The table below lists all the Kneron device peripherals along with the description.

| Name          | Description   |
| ------------ | ------------- |
| KDRV_ADC | Kneron Driver - Analog-to-Digital Converter |
| KDRV_CLOCK | Kneron Driver - Clock |
| KDRV_GDMA | Kneron Driver - Generic Direct Memory Access |
| KDRV_GPIO | Kneron Driver - General Purpose Input/Output |
| KDRV_I2C | Kneron Driver - Inter-integrated Circuit |
| KDRV_LCDC | Kneron Driver - Liquid Crystal Display |
| KDRV_LCM | Kneron Driver -  Liquid Crystal Module |
| KDRV_MIPICSIRX | Kneron Driver -  MIPI CSI RX |
| KDRV_MPU | Kneron Driver - Memory Protection Unit |
| KDRV_NCPU | Kneron Driver - Neuro Control Process Unit |
| KDRV_PINMUX | Kneron Driver - Pin Multiplexing Configuration |
| KDRV_POWER | Kneron Driver - Power |
| KDRV_PWM | Kneron Driver - Pulse Width Modulation Timer |
| KDRV_SPIF | Kneron Driver - SPI Flash Controller |
| KDRV_SYSTEM | Kneron Driver - System|
| KDRV_TIMER | Kneron Driver - Timer/Counter |
| KDRV_UART | Kneron Driver - Universal Asynchronous Receiver/Transmitter |
| KDRV_USBD | Kneron Driver - USB Device |
| KDRV_WDT | Kneron Driver - Watchdog |

### 9.1. KDRV_ADC
####### Kneron generic adc driver

**Include Header File:**  kdrv_adc.h

- Structs
    - [ kdrv_adc_resource_t](#kdrv_adc_resource_t)
- Functions
    - [kdrv_adc_enable](#kdrv_adc_enable)
    - [kdrv_adc_initialize](#kdrv_adc_initialize)
    - [kdrv_adc_read](#kdrv_adc_read)
    - [kdrv_adc_rest](#kdrv_adc_rest)
    - [kdrv_adc_uninitialize](#kdrv_adc_uninitialize)


---

#### Structs
### kdrv_adc_resource_t
typedef struct **kdrv_adc_resource_t** {...}
> ADC Resource Configuration

|Members| |
|:---|:--- |
|int io_base;| ADC register interface |
|int irq;| ADC Event IRQ Number |


---

####  Functions
### kdrv_adc_enable
> ADC enable control

```c
kdrv_status_t kdrv_adc_enable(
	kdrv_adc_resource_t *res
	int mode
)
```
**Parameters:**

<pre>
<em>*res</em>            [in]      a handle of a ADC resource
                          mode                  which mode to be enabled
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_adc_initialize
> ADC driver initialization

```c
kdrv_status_t kdrv_adc_initialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_adc_read
> ADC data read control

```c
int kdrv_adc_read(
	int id
)
```
**Parameters:**

<pre>
<em>id</em>              [in]      which adc channel to be enabled
</pre>
**Returns:**

int                   return ADC data


---
### kdrv_adc_rest
> ADC reset control

```c
kdrv_status_t kdrv_adc_rest(
	kdrv_adc_resource_t *res
)
```
**Parameters:**

<pre>
<em>*res</em>            [in]      a handle of a ADC resource
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_adc_uninitialize
> ADC driver uninitialization

```c
kdrv_status_t kdrv_adc_uninitialize(
	kdrv_adc_resource_t *res
)
```
**Parameters:**

<pre>
<em>*res</em>            [in]      a handle of a ADC resource
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---

### 9.2. KDRV_CLOCK
####### Kneron generic clock driver


**Include Header File:**  kdrv_clock.h

- Simple Typedef
    - [typedef int (*fn_set)(struct kdrv_clock_node *, struct kdrv_clock_value *);](#typedef int (*fn_set)(struct kdrv_clock_node *, struct kdrv_clock_value *);)
- Enumerations
    - [ clk ](#clk)
    - [ pll_id ](#pll_id)
    - [ scuclkin_type ](#scuclkin_type)
- Structs
    - [ kdrv_clock_list ](#kdrv_clock_list)
    - [ kdrv_clock_node ](#kdrv_clock_node)
    - [ kdrv_clock_value ](#kdrv_clock_value)
- Functions
    - [kdrv_clock_disable](#kdrv_clock_disable)
    - [kdrv_clock_enable](#kdrv_clock_enable)
    - [kdrv_clock_mgr_change_pll3_clock](#kdrv_clock_mgr_change_pll3_clock)
    - [kdrv_clock_mgr_change_pll5_clock](#kdrv_clock_mgr_change_pll5_clock)
    - [kdrv_clock_mgr_close](#kdrv_clock_mgr_close)
    - [kdrv_clock_mgr_close_pll1](#kdrv_clock_mgr_close_pll1)
    - [kdrv_clock_mgr_close_pll2](#kdrv_clock_mgr_close_pll2)
    - [kdrv_clock_mgr_close_pll4](#kdrv_clock_mgr_close_pll4)
    - [kdrv_clock_mgr_init](#kdrv_clock_mgr_init)
    - [kdrv_clock_mgr_open](#kdrv_clock_mgr_open)
    - [kdrv_clock_mgr_open_pll1](#kdrv_clock_mgr_open_pll1)
    - [kdrv_clock_mgr_open_pll2](#kdrv_clock_mgr_open_pll2)
    - [kdrv_clock_mgr_open_pll3](#kdrv_clock_mgr_open_pll3)
    - [kdrv_clock_mgr_open_pll4](#kdrv_clock_mgr_open_pll4)
    - [kdrv_clock_mgr_open_pll5](#kdrv_clock_mgr_open_pll5)
    - [kdrv_clock_mgr_set_muxsel](#kdrv_clock_mgr_set_muxsel)
    - [kdrv_clock_mgr_set_scuclkin](#kdrv_clock_mgr_set_scuclkin)
    - [kdrv_clock_set_csiclk](#kdrv_clock_set_csiclk)
    - [kdrv_delay_us](#kdrv_delay_us)


---

######## Simple Typedefs
### **typedef int (*fn_set)(struct kdrv_clock_node *, struct kdrv_clock_value *);**
> Function pointer to set clock node


---

###### Enumerations
### **clk**
enum **clk** {...}
> Enumeration of clock type

| Enumerator | |
|:---|:--- |
|CLK_PLL1            = 1,        | Enum 1|
|CLK_PLL1_OUT,                   | Enum 2|
|CLK_PLL2,                       | Enum 3|
|CLK_PLL2_OUT,                   | Enum 4|
|CLK_PLL3,                       | Enum 5|
|CLK_PLL3_OUT1,                  | Enum 6|
|CLK_PLL3_OUT2,                  | Enum 7|
|CLK_PLL4,                       | Enum 8|
|CLK_PLL4_OUT,                   | Enum 9|
|CLK_PLL5,                       | Enum 10|
|CLK_PLL5_OUT1,                  | Enum 11|
|CLK_PLL5_OUT2,                  | Enum 12|
|CLK_FCS_PLL2        = 20,       | Enum 20|
|CLK_FCS_DLL,                    | Enum 21|
|CLK_PLL4_FREF_PLL0,             | Enum 22|
|CLK_BUS_SAHB        = 30,       | Enum 30|
|CLK_BUS_NAHB,                   | Enum 31|
|CLK_BUS_PAHB1,                  | Enum 32|
|CLK_BUS_PAHB2,                  | Enum 33|
|CLK_BUS_APB0,                   | Enum 34|
|CLK_BUS_APB1,                   | Enum 35|
|CLK_SCPU            = 50,       | Enum 50|
|CLK_SCPU_TRACE,                 | Enum 51|
|CLK_NCPU            = 60,       | Enum 60|
|CLK_NCPU_TRACE,                 | Enum 61|
|CLK_NPU,                        | Enum 62|
|CLK_SPI_CLK         = 100,      | Peripheral clocks, Enum 100|
|CLK_ADC_CLK,                    | Peripheral clocks, Enum 101|
|CLK_WDT_EXT_CLK,                | Peripheral clocks, Enum 102|
|CLK_SD_CLK,                     | Peripheral clocks, Enum 103|
|CLK_MIPI_TXHSPLLREF_CLK,        | Peripheral clocks, Enum 104|
|CLK_MIPI_TX_ESC_CLK,            | Peripheral clocks, Enum 105|
|CLK_MIPI_CSITX_DSI_CLK,         | Peripheral clocks, Enum 106|
|CLK_MIPI_CSITX_CSI_CLK,         | Peripheral clocks, Enum 107|
|CLK_MIPI_CSIRX1_TXESC_CLK,      | Peripheral clocks, Enum 108|
|CLK_MIPI_CSIRX1_CSI_CLK,        | Peripheral clocks, Enum 109|
|CLK_MIPI_CSIRX1_VC0_CLK,        | Peripheral clocks, Enum 110|
|CLK_MIPI_CSIRX0_TXESC_CLK,      | Peripheral clocks, Enum 111|
|CLK_MIPI_CSIRX0_CSI_CLK,        | Peripheral clocks, Enum 112|
|CLK_MIPI_CSIRX0_VC0_CLK,        | Peripheral clocks, Enum 113|
|CLK_LC_SCALER,                  | Peripheral clocks, Enum 114|
|CLK_LC_CLK,                     | Peripheral clocks, Enum 115|
|CLK_TMR1_EXTCLK3,               | Peripheral clocks, Enum 116|
|CLK_TMR1_EXTCLK2,               | Peripheral clocks, Enum 117|
|CLK_TMR1_EXTCLK1,               | Peripheral clocks, Enum 118|
|CLK_TMR0_EXTCLK3,               | Peripheral clocks, Enum 119|
|CLK_TMR0_EXTCLK2,               | Peripheral clocks, Enum 120|
|CLK_TMR0_EXTCLK1,               | Peripheral clocks, Enum 121|
|CLK_PWM_EXTCLK6,                | Peripheral clocks, Enum 122|
|CLK_PWM_EXTCLK5,                | Peripheral clocks, Enum 123|
|CLK_PWM_EXTCLK4,                | Peripheral clocks, Enum 124|
|CLK_PWM_EXTCLK3,                | Peripheral clocks, Enum 125|
|CLK_PWM_EXTCLK2,                | Peripheral clocks, Enum 126|
|CLK_PWM_EXTCLK1,                | Peripheral clocks, Enum 127|
|CLK_UART1_3_FREF,               | Peripheral clocks, Enum 128|
|CLK_UART1_2_FREF,               | Peripheral clocks, Enum 129|
|CLK_UART1_1_FREF,               | Peripheral clocks, Enum 130|
|CLK_UART1_0_FREF,               | Peripheral clocks, Enum 131|
|CLK_UART0_FREF,                 | Peripheral clocks, Enum 132|
|CLK_SSP1_1_SSPCLK,              | Peripheral clocks, Enum 133|
|CLK_SSP1_0_SSPCLK,              | Peripheral clocks, Enum 134|
|CLK_SSP0_1_SSPCLK,              | Peripheral clocks, Enum 135|
|CLK_SSP0_0_SSPCLK               | Peripheral clocks, Enum 136|


---
### **pll_id**
enum **pll_id** {...}
> Enumeration of PLL ID

| Enumerator | |
|:---|:--- |
|pll_1 = 0,      | Enum 0|
|pll_2,          | Enum 1|
|pll_3,          | Enum 2|
|pll_4,          | Enum 3|
|pll_5           | Enum 4|


---
### **scuclkin_type**
enum **scuclkin_type** {...}
> Enumeration of SCPU clock in type

| Enumerator | |
|:---|:--- |
|scuclkin_osc = 0,       | Enum 0|
|scuclkin_rtcosc,        | Enum 1|
|scuclkin_pll0div3,      | Enum 2|
|scuclkin_pll0div4       | Enum 3|


---

##### Structs
### kdrv_clock_list
struct **kdrv_clock_list** {...}
> Structure of clock list

|Members| |
|:---|:--- |
|struct kdrv_clock_list *next;| next pointer to @ref struct kdrv_clock_list|


---
### kdrv_clock_node
struct **kdrv_clock_node** {...}
> Structure of clock list node element

|Members| |
|:---|:--- |
|struct kdrv_clock_node *parent;| Parent pointer to @ref struct kdrv_clock_node|
|struct kdrv_clock_node *child_head;| Child head pointer to @ref struct kdrv_clock_node|
|struct kdrv_clock_node *child_next;| Child next pointer to @ref struct kdrv_clock_node|
|fn_set set;| Function pointer, @ref fn_set|
|uint8_t is_enabled;| Is the clock node enabled|
|char name[15];| String of clock name|


---
### kdrv_clock_value
struct **kdrv_clock_value** {...}
> Structure of clock value

|Members| |
|:---|:--- |
|uint16_t ms;|ms|
|uint16_t ns;|ns|
|uint16_t ps;|ps|
|uint8_t div;| Divider |
|uint8_t enable;| Enable or disable |


---

###### Functions
### kdrv_clock_disable
> Disable Clock

```c
void kdrv_clock_disable(
	enum clk clk
)
```
**Parameters:**

<pre>
<em>clk</em>             [in]      @ref enum clk
</pre>
---
### kdrv_clock_enable
> Enable Clock

```c
void kdrv_clock_enable(
	enum clk clk
)
```
**Parameters:**

<pre>
<em>clk</em>             [in]      @ref enum clk
</pre>
---
### kdrv_clock_mgr_change_pll3_clock
> Change clock PLL3

```c
void kdrv_clock_mgr_change_pll3_clock(
	uint32_t ms
	uint32_t ns
	uint32_t ps
	uint32_t csi0_txesc
	uint32_t csi0_csi
	uint32_t csi0_vc0
	uint32_t csi1_txesc
	uint32_t csi1_csi
	uint32_t csi1_vc0
)
```
**Parameters:**

<pre>
<em>ms</em>              [in]      milli-seconds
<em>ns</em>              [in]      nano-seconds
<em>ps</em>              [in]      pico-seconds
<em>csi0_txesc</em>      [in]      CSI0 txesc
<em>csi0_csi</em>        [in]      CSI0 csi
<em>csi0_vc0</em>        [in]      CSI0 vc0
<em>csi1_txesc</em>      [in]      CSI1 txesc
<em>csi1_csi</em>        [in]      CSI1 csi
<em>csi1_vc0</em>        [in]      CSI1 vc0
</pre>
---
### kdrv_clock_mgr_change_pll5_clock
> Change clock PLL5

```c
void kdrv_clock_mgr_change_pll5_clock(
	uint32_t ms
	uint32_t ns
	uint32_t ps
)
```
**Parameters:**

<pre>
<em>ms</em>              [in]      milli-seconds
<em>ns</em>              [in]      nano-seconds
<em>ps</em>              [in]      pico-seconds
</pre>
---
### kdrv_clock_mgr_close
> Close the specific clock and deactive it

```c
void kdrv_clock_mgr_close(
	struct kdrv_clock_node *node
)
```
**Parameters:**

<pre>
<em>*node</em>           [in]      Pointer to struct @ref kdrv_clock_node
</pre>
---
### kdrv_clock_mgr_close_pll1
> Close Clock PLL1

```c
void kdrv_clock_mgr_close_pll1(
	void
)
```
---
### kdrv_clock_mgr_close_pll2
> Close Clock PLL2

```c
void kdrv_clock_mgr_close_pll2(
	void
)
```
---
### kdrv_clock_mgr_close_pll4
> Close Clock PLL4

```c
void kdrv_clock_mgr_close_pll4(
	void
)
```
---
### kdrv_clock_mgr_init
> Initialize all clock

```c
void kdrv_clock_mgr_init(
	void
)
```
---
### kdrv_clock_mgr_open
> Open the specific clock and active it

```c
void kdrv_clock_mgr_open(
	struct kdrv_clock_node *node
	struct kdrv_clock_value *clock_val
)
```
**Parameters:**

<pre>
<em>*node</em>           [in]      Pointer to struct @ref kdrv_clock_node
<em>*clock_val</em>      [in]      Pointer to struct @ref kdrv_clock_value
</pre>
---
### kdrv_clock_mgr_open_pll1
> Open Clock PLL1

```c
void kdrv_clock_mgr_open_pll1(
	void
)
```
---
### kdrv_clock_mgr_open_pll2
> Open Clock PLL2

```c
void kdrv_clock_mgr_open_pll2(
	void
)
```
---
### kdrv_clock_mgr_open_pll3
> Open Clock PLL3

```c
void kdrv_clock_mgr_open_pll3(
	void
)
```
---
### kdrv_clock_mgr_open_pll4
> Open Clock PLL4

```c
void kdrv_clock_mgr_open_pll4(
	void
)
```
---
### kdrv_clock_mgr_open_pll5
> Open Clock PLL5

```c
void kdrv_clock_mgr_open_pll5(
	void
)
```
---
### kdrv_clock_mgr_set_muxsel
> Set clock mux selection

```c
void kdrv_clock_mgr_set_muxsel(
	uint32_t flags
)
```
**Parameters:**

<pre>
<em>flags</em>           [in]      Flags mask
</pre>
---
### kdrv_clock_mgr_set_scuclkin
> Set SCU clock source in

```c
void kdrv_clock_mgr_set_scuclkin(
	enum scuclkin_type type
	bool enable
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref scuclkin_type
<em>enable</em>          [in]      enable or disable PLL control register
</pre>
---
### kdrv_clock_set_csiclk
> Set MIPI CSI clock

```c
void kdrv_clock_set_csiclk(
	uint32_t cam_idx
	uint32_t enable
)
```
**Parameters:**

<pre>
<em>cam_idx</em>         [in]      Index of MIPI camera
<em>enable</em>          [in]      Enable or Disable
</pre>
---
### kdrv_delay_us
> Delay us

```c
void kdrv_delay_us(
	uint32_t usec
)
```
**Parameters:**

<pre>
<em>usec</em>            [in]      usec what to delay
</pre>
---

### 9.3. KDRV_GDMA
####### Kneron generic DMA driver


**Include Header File:**  kdrv_gdma.h

- Simple Typedef
    - [typedef int32_t kdrv_gdma_handle_t;](#typedef int32_t kdrv_gdma_handle_t;)
    - [typedef void (*gdma_xfer_callback_t)(kdrv_status_t status, void *arg);](#typedef void (*gdma_xfer_callback_t)(kdrv_status_t status, void *arg);)
- Enumerations
    - [ gdma_address_control_t](#gdma_address_control_t)
    - [ gdma_burst_size_t](#gdma_burst_size_t)
    - [ gdma_transfer_width_t](#gdma_transfer_width_t)
    - [ gdma_work_mode_t](#gdma_work_mode_t)
- Structs
    - [ gdma_setting_t](#gdma_setting_t)
- Functions
    - [kdrv_gdma_acquire_handle](#kdrv_gdma_acquire_handle)
    - [kdrv_gdma_configure_setting](#kdrv_gdma_configure_setting)
    - [kdrv_gdma_initialize](#kdrv_gdma_initialize)
    - [kdrv_gdma_memcpy](#kdrv_gdma_memcpy)
    - [kdrv_gdma_memcpy_async](#kdrv_gdma_memcpy_async)
    - [kdrv_gdma_release_handle](#kdrv_gdma_release_handle)
    - [kdrv_gdma_transfer](#kdrv_gdma_transfer)
    - [kdrv_gdma_transfer_async](#kdrv_gdma_transfer_async)
    - [kdrv_gdma_uninitialize](#kdrv_gdma_uninitialize)


---

######## Simple Typedefs
### **typedef int32_t kdrv_gdma_handle_t;**
> GDMA handle type which represents for a DMA channel and related DMA operations


---
### **typedef void (*gdma_xfer_callback_t)(kdrv_status_t status, void *arg);**
> GDMA user callback function with transfer status notification.


---

###### Enumerations
### **gdma_address_control_t**
typedef enum **gdma_address_control_t** {...}
> Enumeration of DMA address control, auto-increasing/descreading or fixed

| Enumerator | |
|:---|:--- |
|GDMA_INCREMENT_ADDRESS = 0x0,   | DMA address control, auto-increasing, default value |
|GDMA_DECREMENT_ADDRESS,         | DMA address control, auto-descreading |
|GDMA_FIXED_ADDRESS,             | DMA address control, fixed |


---
### **gdma_burst_size_t**
typedef enum **gdma_burst_size_t** {...}
> Enumeration of GDMA transfer burst : 1/4/8/16/32/64/128/256, this is about performance

| Enumerator | |
|:---|:--- |
|GDMA_BURST_SIZE_1 = 0x0,        | GDMA transfer burst size: 1 |
|GDMA_BURST_SIZE_4,              | GDMA transfer burst size: 4 |
|GDMA_BURST_SIZE_8,              | GDMA transfer burst size: 8 |
|GDMA_BURST_SIZE_16,             | GDMA transfer burst size: 16, default value |
|GDMA_BURST_SIZE_32,             | GDMA transfer burst size: 32 |
|GDMA_BURST_SIZE_64,             | GDMA transfer burst size: 64 |
|GDMA_BURST_SIZE_128,            | GDMA transfer burst size: 128 |
|GDMA_BURST_SIZE_256,            | GDMA transfer burst size: 256 |


---
### **gdma_transfer_width_t**
typedef enum **gdma_transfer_width_t** {...}
> Enumeration of GDMA transfer size: 8/16/32 bits, this is about byte-alignment

| Enumerator | |
|:---|:--- |
|GDMA_TXFER_WIDTH_8_BITS = 0x0,  | GDMA transfer size: 8 bits |
|GDMA_TXFER_WIDTH_16_BITS,       | GDMA transfer size: 16 bits |
|GDMA_TXFER_WIDTH_32_BITS,       | GDMA transfer size: 32 bits, default value |


---
### **gdma_work_mode_t**
typedef enum **gdma_work_mode_t** {...}
> Enumeration of DMA working mode, can be normal or hardware handshake mode

| Enumerator | |
|:---|:--- |
|GDMA_NORMAL_MODE = 0x0,     | DMA working mode, normal mode , default value|
|GDMA_HW_HANDSHAKE_MODE,     | DMA working mode, hardware handshake mode |


---

#### Structs
### gdma_setting_t
typedef struct **gdma_setting_t** {...}
> Structure of GDMA advanced settings for a specified DMA handle (channel)

|Members| |
|:---|:--- |
|gdma_transfer_width_t dst_width;| see @ref gdma_transfer_width_t |
|gdma_transfer_width_t src_width;| see @ref gdma_transfer_width_t |
|gdma_burst_size_t burst_size;| see @ref gdma_burst_size_t |
|gdma_address_control_t dst_addr_ctrl;| see @ref gdma_address_control_t |
|gdma_address_control_t src_addr_ctrl;| see @ref gdma_address_control_t |
|gdma_work_mode_t dma_mode;| see @ref gdma_work_mode_t |
|uint32_t dma_dst_req;| for HW handshake mode, refer to kneron_mozart.h XXX_DMA_REQ |
|uint32_t dma_src_req;| for HW handshake mode, refer to kneron_mozart.h XXX_DMA_REQ |


---

###### Functions
### kdrv_gdma_acquire_handle
> Acquire a GDMA handle

```c
kdrv_status_t kdrv_gdma_acquire_handle(
	kdrv_gdma_handle_t *handle
)
```
**Parameters:**

<pre>
<em>handle</em>          [out]     a handle of a DMA channel, see @ref kdrv_gdma_handle_t
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t
Example:\n
kdrv_gdma_handle_t dma_handle;
kdrv_status_t sts = kdrv_gdma_acquire_handle(&dma_handle);
if(sts == KDRV_STATUS_OK) printf("Succeeds to get valid dma_handle");


---
### kdrv_gdma_configure_setting
> Configure the DMA working behavior on specified DMA handle with specified dma settings

```c
kdrv_status_t kdrv_gdma_configure_setting(
	kdrv_gdma_handle_t handle
	gdma_setting_t *dma_setting
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      a handle of a DMA channel, see @ref kdrv_gdma_handle_t
<em>dma_setting</em>     [in]      pointer of dma_setting, see @ref gdma_setting_t
</pre>
**Returns:**

@ref kdrv_status_t


**Notes:**

> Before call this API, you should get a valid dma_handle via @ref kdrv_gdma_acquire_handle() firstly.


---
### kdrv_gdma_initialize
> GDMA driver initialization

```c
kdrv_status_t kdrv_gdma_initialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_gdma_memcpy
> Start DMA transfer with automatic DMA handle running in synchronous (blocking) mode

```c
kdrv_status_t kdrv_gdma_memcpy(
	uint32_t dst_addr
	uint32_t src_addr
	uint32_t num_bytes
)
```
**Parameters:**

<pre>
<em>dst_addr</em>        [in]      destination address
<em>src_addr</em>        [in]      source address
<em>num_bytes</em>       [in]      number of bytes to be transfered
</pre>
**Returns:**

@ref kdrv_status_t


---
### kdrv_gdma_memcpy_async
> Start DMA transfer with automatic DMA handle running in asynchronous (non-blocking) mode

```c
kdrv_status_t kdrv_gdma_memcpy_async(
	uint32_t dst_addr
	uint32_t src_addr
	uint32_t num_bytes
	gdma_xfer_callback_t xfer_isr_cb
	void *usr_arg
)
```
**Parameters:**

<pre>
<em>dst_addr</em>        [in]      destination address
<em>src_addr</em>        [in]      source address
<em>num_bytes</em>       [in]      number of bytes to be transfered
<em>xfer_isr_cb</em>     [in]      user callback function, see @ref gdma_xfer_callback_t
<em>usr_arg</em>         [in]      user's own argument
</pre>
**Returns:**

@ref kdrv_status_t


---
### kdrv_gdma_release_handle
> Release the DMA handle

```c
kdrv_status_t kdrv_gdma_release_handle(
	kdrv_gdma_handle_t handle
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      a handle of a DMA channel, see @ref kdrv_gdma_handle_t
</pre>
**Returns:**

@ref kdrv_status_t


---
### kdrv_gdma_transfer
> Start DMA transfer with specified DMA handle running in synchronous (blocking) mode

```c
kdrv_status_t kdrv_gdma_transfer(
	kdrv_gdma_handle_t handle
	uint32_t dst_addr
	uint32_t src_addr
	uint32_t num_bytes
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      a handle of a DMA channel, see @ref kdrv_gdma_handle_t
<em>dst_addr</em>        [in]      destination address
<em>src_addr</em>        [in]      source address
<em>num_bytes</em>       [in]      number of bytes to be transfered
</pre>
**Returns:**

@ref kdrv_status_t


---
### kdrv_gdma_transfer_async
> Start DMA transfer with specified DMA handle running in asynchronous (non-blocking) mode

```c
kdrv_status_t kdrv_gdma_transfer_async(
	kdrv_gdma_handle_t handle
	uint32_t dst_addr
	uint32_t src_addr
	uint32_t num_bytes
	gdma_xfer_callback_t xfer_isr_cb
	void *usr_arg
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      a handle of a DMA channel, see @ref kdrv_gdma_handle_t
<em>dst_addr</em>        [in]      destination address
<em>src_addr</em>        [in]      source address
<em>num_bytes</em>       [in]      number of bytes to be transfered
<em>xfer_isr_cb</em>     [in]      user callback function, see @ref gdma_xfer_callback_t
<em>usr_arg</em>         [in]      user's argument
</pre>
**Returns:**

@ref kdrv_status_t


---
### kdrv_gdma_uninitialize
> GDMA driver uninitialization

```c
kdrv_status_t kdrv_gdma_uninitialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---

### 9.4. KDRV_GPIO
####### Kneron GPIO driver

**Include Header File:**  kdrv_gpio.h

- Simple Typedef
    - [typedef void (*gpio_interrupt_callback_t)(kdrv_gpio_pin_t pin, void *arg);](#typedef void (*gpio_interrupt_callback_t)(kdrv_gpio_pin_t pin, void *arg);)
- Enumerations
    - [ kdrv_gpio_attribute_t](#kdrv_gpio_attribute_t)
    - [ kdrv_gpio_pin_t](#kdrv_gpio_pin_t)
- Functions
    - [kdrv_gpio_initialize](#kdrv_gpio_initialize)
    - [kdrv_gpio_read_pin](#kdrv_gpio_read_pin)
    - [kdrv_gpio_register_callback](#kdrv_gpio_register_callback)
    - [kdrv_gpio_set_attribute](#kdrv_gpio_set_attribute)
    - [kdrv_gpio_set_debounce](#kdrv_gpio_set_debounce)
    - [kdrv_gpio_set_interrupt](#kdrv_gpio_set_interrupt)
    - [kdrv_gpio_uninitialize](#kdrv_gpio_uninitialize)
    - [kdrv_gpio_write_pin](#kdrv_gpio_write_pin)


---

###### Simple Typedefs
### **typedef void (*gpio_interrupt_callback_t)(kdrv_gpio_pin_t pin, void *arg);**
> GPIO user callback function with specified GPIO pin.


---

#### Enumerations
### **kdrv_gpio_attribute_t**
typedef enum **kdrv_gpio_attribute_t** {...}
> Enumerations of GPIO pin attributes, input or output, interrupt trigger settings

| Enumerator | |
|:---|:--- |
|GPIO_DIR_INPUT = 0x1,        | pin direction digital input|
|GPIO_DIR_OUTPUT = 0x2,       | pin direction digital output|
|GPIO_INT_EDGE_RISING = 0x4,  | indicate pin interrupt triggered when at rising edge |
|GPIO_INT_EDGE_FALLING = 0x8, | indicate pin interrupt triggered when at falling edge |
|GPIO_INT_EDGE_BOTH = 0x10,   | indicate pin interrupt triggered when at both edge rsising or falling |
|GPIO_INT_LEVEL_HIGH = 0x20,  | indicate pin interrupt triggered when at high voltage level |
|GPIO_INT_LEVEL_LOW = 0x40,   | indicate pin interrupt triggered when at low voltage level |

---
### **kdrv_gpio_pin_t**
typedef enum **kdrv_gpio_pin_t** {...}
> Enumerations of GPIO pin ID, there 32 GPIO pins

| Enumerator | |
|:---|:--- |
|GPIO_PIN_0 = 0, |  GPIO pin ID 0 |
|GPIO_PIN_1,     |  GPIO pin ID 1 |
|GPIO_PIN_2,     |  GPIO pin ID 2 |
|GPIO_PIN_3,     |  GPIO pin ID 3 |
|GPIO_PIN_4,     |  GPIO pin ID 4 |
|GPIO_PIN_5,     |  GPIO pin ID 5 |
|GPIO_PIN_6,     |  GPIO pin ID 6 |
|GPIO_PIN_7,     |  GPIO pin ID 7 |
|GPIO_PIN_8,     |  GPIO pin ID 8 |
|GPIO_PIN_9,     |  GPIO pin ID 9 |
|GPIO_PIN_10,    |  GPIO pin ID 10 |
|GPIO_PIN_11,    |  GPIO pin ID 11 |
|GPIO_PIN_12,    |  GPIO pin ID 12 |
|GPIO_PIN_13,    |  GPIO pin ID 13 |
|GPIO_PIN_14,    |  GPIO pin ID 14 |
|GPIO_PIN_15,    |  GPIO pin ID 15 |
|GPIO_PIN_16,    |  GPIO pin ID 16 |
|GPIO_PIN_17,    |  GPIO pin ID 17 |
|GPIO_PIN_18,    |  GPIO pin ID 18 |
|GPIO_PIN_19,    |  GPIO pin ID 19 |
|GPIO_PIN_20,    |  GPIO pin ID 20 |
|GPIO_PIN_21,    |  GPIO pin ID 21 |
|GPIO_PIN_22,    |  GPIO pin ID 22 |
|GPIO_PIN_23,    |  GPIO pin ID 23 |
|GPIO_PIN_24,    |  GPIO pin ID 24 |
|GPIO_PIN_25,    |  GPIO pin ID 25 |
|GPIO_PIN_26,    |  GPIO pin ID 26 |
|GPIO_PIN_27,    |  GPIO pin ID 27 |
|GPIO_PIN_28,    |  GPIO pin ID 28 |
|GPIO_PIN_29,    |  GPIO pin ID 29 |
|GPIO_PIN_30,    |  GPIO pin ID 30 |
|GPIO_PIN_31     |  GPIO pin ID 31 |

---

###### Functions
### kdrv_gpio_initialize
> GPIO driver initialization, this must be invoked once before any GPIO manipulations

```c
kdrv_status_t kdrv_gpio_initialize(
	void
)
```
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_read_pin
> read GPIO digitial pin value

```c
kdrv_status_t kdrv_gpio_read_pin(
	kdrv_gpio_pin_t pin
	bool *pValue
)
```
This function read a high or low value from a digital pin.\n
The specified pin must be configured as digital input and not in interrupt mode.

**Parameters:**

<pre>
<em>pin</em>             [in]      GPIO pin ID, see @ref kdrv_gpio_pin_t
<em>pValue</em>          [out]     pointer to a value to read out GPIO voltage level
</pre>
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_register_callback
> register user callback with user argument for GPIO interrupt in this callback can get interrupts for all GPIO pins

```c
kdrv_status_t kdrv_gpio_register_callback(
	gpio_interrupt_callback_t gpio_isr_cb
	void *usr_arg
)
```
**Parameters:**

<pre>
<em>gpio_isr_cb</em>     [in]      user callback function for GPIO interrupts, see @ref gpio_interrupt_callback_t
<em>usr_arg</em>         [in]      user's argument
</pre>
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_set_attribute
> set pin attributes for a specified GPIO pin

```c
kdrv_status_t kdrv_gpio_set_attribute(
	kdrv_gpio_pin_t pin
	uint32_t attributes
)
```
it must be well set up before GPIO pin to be used.



**Parameters:**

<pre>
<em>pin</em>             [in]      After configuring the desired pin as a GPIO pin, the corresponding GPIO pin name should be used as kdp_gpio_pin_e indicated
<em>attributes</em>      [in]      This is to specify the function of specified GPIO pin,\n
                          for digital output, set only DIR_OUTPUT,\n
                          for digital input for read, set only DIR_INPUT,\n
                          for interrupt usage, set DIR_INPUT and one of EDGE or LEVEL trigger attributes, this implies pin is used as an interrupt input\n
</pre>
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_set_debounce
> set debounce enable/disable with clock setting in Hz

```c
kdrv_status_t kdrv_gpio_set_debounce(
	kdrv_gpio_pin_t pin
	bool isEnable
	uint32_t debounce_clock /* in Hz */
)
```
This can enable internal debouncing hardware for interrupt mode to eliminate the switch bounce.\n
It is very useful for connecting devices like a switch button or a keypad thing.



**Parameters:**

<pre>
<em>pin</em>             [in]      GPIO pin ID, see @ref kdrv_gpio_pin_t
<em>isEnable</em>        [in]      enable/disable
<em>debounce_clock</em>  [in]      The debouncing clock frequency in Hz
</pre>
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_set_interrupt
> set interrupt enable/disable for a specified GPIO pin

```c
kdrv_status_t kdrv_gpio_set_interrupt(
	kdrv_gpio_pin_t pin
	bool isEnable
)
```
**Parameters:**

<pre>
<em>pin</em>             [in]      GPIO pin ID, see @ref kdrv_gpio_pin_t
<em>isEnable</em>        [in]      enable/disable
</pre>
**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_uninitialize
> GPIO driver uninitialization

```c
kdrv_status_t kdrv_gpio_uninitialize(
	void
)
```
This function disables the corresponding clock and frees resources allocated for GPIO operations.



**Returns:**

KDRV_STATUS_OK only


---
### kdrv_gpio_write_pin
> write GPIO digitial pin value

```c
kdrv_status_t kdrv_gpio_write_pin(
	kdrv_gpio_pin_t pin
	bool value
)
```
This function writes a high or low value to a digital pin.\n
The specified pin must be configured as digital output.


**Parameters:**

<pre>
<em>pin</em>             [in]      GPIO pin ID, see @ref kdrv_gpio_pin_t
<em>value</em>           [in]      Output value as digital high or digital low
</pre>
**Returns:**

KDRV_STATUS_OK only


---

### 9.5. KDRV_I2C
####### Kneron I2C driver


Here are the design highlight points:\n
* At present it supports only 7-bit slave address \n
* It is designed in polling way instead of interrupt way, user should be aware of this


**Include Header File:**  kdrv_i2c.h

- Enumerations
    - [ kdrv_i2c_bus_speed_t](#kdrv_i2c_bus_speed_t)
    - [kdrv_i2c_ctrl_t](#kdrv_i2c_ctrl_t)
- Functions
    - [kdp_i2c_receive](#kdp_i2c_receive)
    - [kdp_i2c_transmit](#kdp_i2c_transmit)
    - [kdrv_i2c_initialize](#kdrv_i2c_initialize)
    - [kdrv_i2c_read_register](#kdrv_i2c_read_register)
    - [kdrv_i2c_uninitialize](#kdrv_i2c_uninitialize)
    - [kdrv_i2c_write_register](#kdrv_i2c_write_register)

---

#### Enumerations
### **kdrv_i2c_bus_speed_t**
typedef enum **kdrv_i2c_bus_speed_t** {...}
> Enumerations of I2C bus speed

| Enumerator | |
|:---|:--- |
|KDRV_I2C_SPEED_100K = 0, | Kdrv I2C bus speed 100KHz, standard mode |
|KDRV_I2C_SPEED_200K,     | Kdrv I2C bus speed 200KHz |
|KDRV_I2C_SPEED_400K,     | Kdrv I2C bus speed 400KHz, fast mode |
|KDRV_I2C_SPEED_1M        | Kdrv I2C bus speed 1MHz, fast plus mode |


---
### **kdrv_i2c_ctrl_t**
typedef enum **kdrv_i2c_ctrl_t** {...}
> Enumerations of I2C controller instances

| Enumerator | |
|:---|:--- |
|KDRV_I2C_CTRL_0 = 0,     | Kdrv I2C controller 0 |
|KDRV_I2C_CTRL_1,         | Kdrv I2C controller 1 |
|KDRV_I2C_CTRL_2,         | Kdrv I2C controller 2 |
|KDRV_I2C_CTRL_3,         | Kdrv I2C controller 3 |
|TOTAL_KDRV_I2C_CTRL      | Total Kdrv I2C controllers |


---

###### Functions
### kdp_i2c_receive
> receive data from a specified slave address, the STOP condition can be optionally not generated.

```c
kdrv_status_t kdp_i2c_receive(
	kdrv_i2c_ctrl_t ctrl_id
	uint16_t slave_addr
	uint8_t *data
	uint32_t num
	bool with_STOP
)
```
This function will first set START condition then send slave address for write operations;\n
if 9th bit is NACK, it returns DEV_NACK error, and if it is ACK, \n
controller will continue to send out all data with specified number of bytes,\n
once it is done it will set STOP condition while the 'with_STOP' is KDP_BOOL_TRUE.\n
For every byte transmission, it returns DEV_NACK error while encountering NACK at 9th bit


**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
<em>slave_addr</em>      [in]      Address of the slave(7-bit by default)
<em>data</em>            [out]     data buffer address
<em>num</em>             [in]      Length of data to be written (in bytes)
<em>with_STOP</em>       [in]      STOP condition will be generated or not
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdp_i2c_transmit
> transmit data to a specified slave address, the STOP condition can be optionally not generated.\n

```c
kdrv_status_t kdp_i2c_transmit(
	kdrv_i2c_ctrl_t ctrl_id
	uint16_t slave_addr
	uint8_t *data
	uint32_t num
	bool with_STOP
)
```
This function will first set START condition then send slave address for write operations; \n
if 9th bit is NACK, it returns DEV_NACK error, and if it is ACK, \n
controller will continue to send out all data with specified number of bytes, \n
once it is done it will set STOP condition while the 'with_STOP' is KDP_BOOL_TRUE.\n
For every byte transmission, it returns DEV_NACK error while encountering NACK at 9th bit.


**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
<em>slave_addr</em>      [in]      Address of the slave(7-bit by default)
<em>data</em>            [in]      data buffer address
<em>num</em>             [in]      Length of data to be written (in bytes)
<em>with_STOP</em>       [in]      STOP condition will be generated or not
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_i2c_initialize
> Initializes Kdrv I2C driver (as master) and configures it for the specified speed.

```c
kdrv_status_t kdrv_i2c_initialize(
	kdrv_i2c_ctrl_t ctrl_id
	kdrv_i2c_bus_speed_t bus_speed
)
```
**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
<em>bus_speed</em>       [in]      see @ref kdrv_i2c_bus_speed_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> This API MUST be called before using the Read/write APIs for I2C.


---
### kdrv_i2c_read_register
> specialized function to read from the register of slave device, register address can be 1 or 2 bytes.

```c
kdrv_status_t kdrv_i2c_read_register(
	kdrv_i2c_ctrl_t ctrl_id
	uint16_t slave_addr
	uint16_t reg
	uint16_t reg_size
	uint16_t len
	uint8_t *data
)
```
**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
<em>slave_addr</em>      [in]      Address of the slave(7-bit by default)
<em>reg</em>             [in]      Register address
<em>reg_size</em>        [in]      Length of register address
<em>len</em>             [in]      Length of data to be read (in bytes).
<em>data</em>            [out]     data buffer to read register value
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_i2c_uninitialize
> Uninitializes Kdrv I2C driver

```c
kdrv_status_t kdrv_i2c_uninitialize(
	kdrv_i2c_ctrl_t ctrl_id
)
```
**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_i2c_write_register
> specialized function to write to the register of slave device, register address can be 1 or 2 bytes.

```c
kdrv_status_t kdrv_i2c_write_register(
	kdrv_i2c_ctrl_t ctrl_id
	uint16_t slave_addr
	uint16_t reg
	uint16_t reg_size
	uint16_t len
	uint8_t *data
)
```
**Parameters:**

<pre>
<em>ctrl_id</em>         [in]      see @ref kdrv_i2c_ctrl_t
<em>slave_addr</em>      [in]      Address of the slave(7-bit by default)
<em>reg</em>             [in]      Register address
<em>reg_size</em>        [in]      Length of register address
<em>len</em>             [in]      Length of data to be written (in bytes).
<em>data</em>            [in]      data write register value
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---

### 9.6. KDRV_LCDC
####### Kneron LCDC driver


**Include Header File:**  kdrv_lcdc.h

- Functions
    - [MAX_FRAME_NUM](#MAX_FRAME_NUM)
    - [kdrv_lcdc_down_scale](#kdrv_lcdc_down_scale)
    - [kdrv_lcdc_set_auo052_mode](#kdrv_lcdc_set_auo052_mode)
    - [kdrv_lcdc_set_bgrsw](#kdrv_lcdc_set_bgrsw)
    - [kdrv_lcdc_set_bus_bandwidth_ctrl](#kdrv_lcdc_set_bus_bandwidth_ctrl)
    - [kdrv_lcdc_set_endian](#kdrv_lcdc_set_endian)
    - [kdrv_lcdc_set_frame_buffer](#kdrv_lcdc_set_frame_buffer)
    - [kdrv_lcdc_set_framerate](#kdrv_lcdc_set_framerate)
    - [kdrv_lcdc_set_image_color_params](#kdrv_lcdc_set_image_color_params)
    - [kdrv_lcdc_set_panel_type](#kdrv_lcdc_set_panel_type)
    - [kdrv_lcdc_set_pixel_colorseq](#kdrv_lcdc_set_pixel_colorseq)
    - [kdrv_lcdc_set_pixel_delta_type](#kdrv_lcdc_set_pixel_delta_type)
    - [kdrv_lcdc_set_pixel_serial_mode](#kdrv_lcdc_set_pixel_serial_mode)
    - [kdrv_lcdc_set_pixel_sr](#kdrv_lcdc_set_pixel_sr)


---

###### Functions
### MAX_FRAME_NUM
> Definition of Display Draw Event

```c
#define FLAGS_KDP520_LCDC_START_DRAW_RECT_EVT    BIT0#define FLAGS_KDP520_LCDC_STOP_DRAW_RECT_EVT     BIT1/*** @brief Definition of maximum number of frame buffer*/#define MAX_FRAME_NUM                           (
	1)/*** @brief Definition of bounding-box margin length*/#define LCDC_HINT_BOUNDINGBOX_MARGIN_LEN        (30)/*** @brief Enumerations of lcdc screen control*/typedef enum{KDRV_LCDC_SCREEN_OFF = 0
	/**< LCDC screen control off */KDRV_LCDC_SCREEN_ON          /**< LCDC screen control on  */} kdrv_lcdc_screen_ctrl_t;/*** @brief Enumerations of lcdc panel pixel parameter
	image pixel format in FIFO*/typedef enum{KDRV_LCDC_IMG_PIXFMT_1BPP = 0
	/**< 000: 1 bpp */KDRV_LCDC_IMG_PIXFMT_2BPP
	/**< 001: 2 bpp */KDRV_LCDC_IMG_PIXFMT_4BPP
	/**< 010: 4 bpp */KDRV_LCDC_IMG_PIXFMT_8BPP
	/**< 011: 8 bpp */KDRV_LCDC_IMG_PIXFMT_16BPP
	/**< 100: 16 bpp */KDRV_LCDC_IMG_PIXFMT_24BPP
	/**< 101: 24 bpp */KDRV_LCDC_IMG_PIXFMT_ARGB8888
	/**< 110: ARGB8888 */KDRV_LCDC_IMG_PIXFMT_ARGB1555   /**< 111: ARGB1555 */} kdrv_lcdc_img_pixfmt_t;/*** @brief Enumerations of lcdc panel pixel parameter
	TFT panel color depth selection*/typedef enum{KDRV_LCDC_6BIT_PER_CHANNEL = 0
	/**< 6 bits per channel with a 18-bit panel interface */KDRV_LCDC_8BIT_PER_CHANNEL      /**< 8 bits per channel with a 24-bit panel interface */} kdrv_lcdc_panel_type_t;/*** @brief Enumerations of lcdc panel pixel parameter
	output format selection*/typedef enum{KDRV_LCDC_OUTPUT_FMT_RGB = 0
	/**< RGB normal output */KDRV_LCDC_OUTPUT_FMT_BGR        /**< BGR red and blue swapped output */} kdrv_lcdc_output_fmt_t;/*** @brief Enumerations of lcdc serial panel pixel parameter
	shift rotate*/typedef enum{KDRV_LCDC_SERIAL_PIX_RSR = 0
	/**< Even line sequence from through the odd line rotating right */KDRV_LCDC_SERIAL_PIX_LSR      /**< Even line sequence from through the odd line rotating left */} kdrv_lcdc_serial_pix_sr_t;/*** @brief Enumerations of lcdc serial panel pixel parameter
	color sequence of odd line*/typedef enum{KDRV_LCDC_SERIAL_PIX_COLORSEQ_RGB = 0
	/**< RGB decides the sub-pixel sequence of the odd line */KDRV_LCDC_SERIAL_PIX_COLORSEQ_BRG
	/**< BRG decides the sub-pixel sequence of the odd line */KDRV_LCDC_SERIAL_PIX_COLORSEQ_GBR       /**< GBR decides the sub-pixel sequence of the odd line */} kdrv_lcdc_serial_pix_colorseq_t;/*** @brief Enumerations of lcdc serial panel pixel parameter
	delta type arrangement of color filter*/typedef enum{KDRV_LCDC_SERIAL_PIX_DELTA_TYPE_SAME_SEQ = 0
	/**< Odd line and even line have the same data sequence */KDRV_LCDC_SERIAL_PIX_DELTA_TYPE_DIFF_SEQ        /**< Odd line and even line have the difference data sequence */} kdrv_lcdc_serial_pix_delta_type_t;/*** @brief Enumerations of lcdc serial panel pixel parameter
	RGB serial output mode*/typedef enum{KDRV_LCDC_SERIAL_PIX_RGB_PARALLEL_OUTPUT = 0
	/**< RGB parallel format output */KDRV_LCDC_SERIAL_PIX_RGB_SERIAL_OUTPUT          /**< RGB serial format output */} kdrv_lcdc_serial_pix_output_mode_t;/*** @brief Enumerations of lcdc image format parameter
	endian control*/typedef enum{KDRV_LCDC_FB_DATA_ENDIAN_LBLP = 0
	/**< 00: Little-endian byte little-endian pixel*/KDRV_LCDC_FB_DATA_ENDIAN_BBBP
	/**< 01: Big-endian byte big-endian pixel*/KDRV_LCDC_FB_DATA_ENDIAN_LBBP
	/**< 10: Little-endian byte big-endian pixel (WinCE)*/} kdrv_lcdc_fb_data_endianness_t;/*** @brief Enumerations of lcdc function enable parameter
	test pattern generator*/typedef enum{KDRV_LCDC_PAT_GEN_DISABLE = 0
	/**< Turn-off pattern generator*/KDRV_LCDC_PAT_GEN_ENABLE
	/**< Turn-on pattern generator*/} kdrv_lcdc_pat_gen_t;/*** @brief Enumerations of lcdc panel pixel parameter
	AUO052 mode*/typedef enum{KDRV_LCDC_AUO052_OFF = 0
	/**< 0: Turn off the AUO052 mode */KDRV_LCDC_AUO052_ON       /**< 1: Turn on the AUO052 mode */} kdrv_lcdc_auo052_mode_t;/*** @brief       Control display screen ON/OFF** @param[in]   ctrl            see @ref kdrv_lcdc_screen_ctrl_t* @return      kdrv_status_t   see @ref kdrv_status_t*/kdrv_status_t kdrv_display_screen_control(kdrv_lcdc_screen_ctrl_t ctrl
)
```
---
### kdrv_lcdc_down_scale
> Set image down scale

```c
kdrv_status_t kdrv_lcdc_down_scale(
	uint16_t hor_no_in
	uint16_t hor_no_out
	uint16_t ver_no_in
	uint16_t ver_no_out
)
```
**Parameters:**

<pre>
<em>hor_no_in</em>       [in]      Width of input image source
<em>hor_no_out</em>      [in]      Height of input image source
<em>ver_no_in</em>       [in]      Width of output image source
<em>ver_no_out</em>      [in]      Height of output image source
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_auo052_mode
> Set data endian

```c
kdrv_status_t kdrv_lcdc_set_auo052_mode(
	kdrv_lcdc_auo052_mode_t mode
)
```
**Parameters:**

<pre>
<em>mode</em>            [in]      see @ref kdrv_lcdc_auo052_mode_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_bgrsw
> Set output format selection of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_bgrsw(
	kdrv_lcdc_output_fmt_t format
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref kdrv_lcdc_output_fmt_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_bus_bandwidth_ctrl
> Set frame rate of lcdc vsync

```c
kdrv_status_t kdrv_lcdc_set_bus_bandwidth_ctrl(
	uint32_t ctrl
)
```
**Parameters:**

<pre>
<em>ctrl</em>            [in]      [BIT9]          Enable the LOCK command\n
                          0:Disable the LOCK command\n
                          1:Enable the LOCK command\n
                          [BIT8]          Enable the bus bandwidth ratio\n
                          0:Disable the bus bandwidth ratio\n
                          1:Enable the bus bandwidth ratio\n
                          [BIT7:BIT6]     Bus bandwidth control ratio for the Image3 Frame buffer\n
                          00:Ratio 1\n
                          01:Ratio 2\n
                          10:Ratio 4\n
                          [BIT5:BIT4]     Bus bandwidth control ratio for the Image2 Frame buffer\n
                          00:Ratio 1\n
                          01:Ratio 2\n
                          10:Ratio 4\n
                          [BIT3:BIT2]     Bus bandwidth control ratio for the Image1 Frame buffer\n
                          00:Ratio 1\n
                          01:Ratio 2\n
                          10:Ratio 4\n
                          [BIT1:BIT0]     Bus bandwidth control ratio for the Image0 Frame buffer\n
                          00:Ratio 1\n
                          01:Ratio 2\n
                          10:Ratio 4\n
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_endian
> Set data endian

```c
kdrv_status_t kdrv_lcdc_set_endian(
	kdrv_lcdc_fb_data_endianness_t endian_type
)
```
**Parameters:**

<pre>
<em>mode</em>            [in]      see @ref kdrv_lcdc_fb_data_endianness_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_frame_buffer
> Set frame buffer parameter

```c
kdrv_status_t kdrv_lcdc_set_frame_buffer(
	uint32_t img_scal_down
)
```
**Parameters:**

<pre>
<em>img_scal_down</em>   [in]      [BIT15:BIT14] Scaling down for image3\n
                          The image from LCDImage3FrameBase can be scaled down depending on the value.\n
                          00: Disable\n
                          01:Image3 will be scaling down to 1/2 x 1/2\n
                          10:Image3 will be scaling down to 1/2 x 1\n
                          [BIT13:BIT12] Scaling down for image2\n
                          The image from LCDImage2FrameBase can be scaled down depending on the value.\n
                          00: Disable\n
                          01:Image2 will be scaling down to 1/2 x 1/2\n
                          10:Image2 will be scaling down to 1/2 x 1\n
                          [BIT11:BIT10] Scaling down for image1\n
                          The image from LCDImage1FrameBase can be scaled down depending on the value.\n
                          00: Disable\n
                          01:Image1 will be scaling down to 1/2 x 1/2\n
                          10:Image1 will be scaling down to 1/2 x 1\n
                          [BIT9:BIT8] Scaling down for image0\n
                          The image from LCDImage0FrameBase can be scaled down depending on the value.\n
                          00: Disable\n
                          01:Image0 will be scaling down to 1/2 x 1/2\n
                          10:Image0 will be scaling down to 1/2 x 1\n
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> Please note that these filed values can only be set to '00' under the folloing conditions:\n
> - VirtualScreenEn or LCM_En is set\n
> - PiP has a chance to be turned-on when TV is enabled.


---
### kdrv_lcdc_set_framerate
> Set frame rate of lcdc vsync

```c
kdrv_status_t kdrv_lcdc_set_framerate(
	int framerate
	int width
	int height
)
```
**Parameters:**

<pre>
<em>framerate</em>       [in]      Image height
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_image_color_params
> Set LCD color management parameter

```c
kdrv_status_t kdrv_lcdc_set_image_color_params(
	uint32_t color0
	uint32_t color1
	uint32_t color2
	uint32_t color3
)
```
**Parameters:**

<pre>
<em>color0</em>          [in]      [BIT13_BIT8] Saturation value.\n
                          Cb(sat) = Cb(org) * (SatValue/32).\n
                          Cr(sat) = Cr(org) * (SatValue/32).\n
                          [BIT7] Sign bit of brightness value.\n
                          0: The value of brightness is positive.\n
                          1: The value of brightness is negative.\n
                          [BIT6:BIT0] Brightness level\n
                          The range of the brightness level is from 0 to 127.\n
<em>color1</em>          [in]      This register value defines the coefficient of the hur operation\n
                          [BIT14] Sign bit of HuCosValue.\n
                          0: The value of HuCosValue is positive.\n
                          1: The value of HuCosValue is negative.\n
                          [BIT13:BIT8] Hue value of coefficient Cos -180~180 degree.\n
                          [BIT6] Sigh bit of HuSinValue\n
                          0: The value of HuSinValue is positive.\n
                          1: The value of HuSinValue is negative.\n
                          [BIT5:BIT0] Hue value of coefficient Sin -180~180 degree.\n
<em>color2</em>          [in]      This register value defines the coefficient of the sharpness operation\n
                          [BIT23:BIT20] Sharpness weight value 1.\n
                          The value determines the second weight of sharpness.\n
                          [BIT19:BIT16] Sharpness weight value 0.\n
                          The value determines the first weight of sharpness.\n
                          [BIT15:BIT8]  Sharpness threshold value 1.\n
                          The value determines the second threshold of sharpness.\n
                          [BIT7:BIT0]   Sharpness threshold value 0.\n
                          The value determines the second threshold of sharpness.\n
<em>color3</em>          [in]      This register value defines the coefficient of the contast operation\n
                          [BIT20:BIT16] Contrast cure slope.\n
                          The value determines the slope of contrast cure. The actual slope is the value devided by 4.\n
                          Note: This value cannot be programmed to 0.\n
                          [BIT12]       Contrast offset sign\n
                          1: (Contr_slope x 128) > 512.\n
                          0: (Contr_slope x 128) < 512.\n
                          [BIT11:BIT0]  Contrast offset value.\n
                          The value is defined as absolute of "Contr_slope x 128 - 512".\n
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_panel_type
> Set TFT panel color depth selection of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_panel_type(
	kdrv_lcdc_panel_type_t type
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref kdrv_lcdc_panel_type_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_pixel_colorseq
> Set color sequence of odd line of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_pixel_colorseq(
	kdrv_lcdc_serial_pix_colorseq_t color
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref kdrv_lcdc_serial_pix_colorseq_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_pixel_delta_type
> Set delta type arrangement of color filter of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_pixel_delta_type(
	kdrv_lcdc_serial_pix_delta_type_t type
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref kdrv_lcdc_serial_pix_delta_type_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_pixel_serial_mode
> Set RGB serial output mode of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_pixel_serial_mode(
	kdrv_lcdc_serial_pix_output_mode_t mode
)
```
**Parameters:**

<pre>
<em>mode</em>            [in]      see @ref kdrv_lcdc_serial_pix_output_mode_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_lcdc_set_pixel_sr
> Set odd line shift rotate of LCD serial panel pixel parameter

```c
kdrv_status_t kdrv_lcdc_set_pixel_sr(
	kdrv_lcdc_serial_pix_sr_t rotate
)
```
**Parameters:**

<pre>
<em>type</em>            [in]      see @ref kdrv_lcdc_serial_pix_sr_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---

### 9.7. KDRV_LCM
######### Kneron LCM driver




**Include Header File:**  kdrv_lcm.h

- Functions
    - [kdrv_lcm_get_backlight](#kdrv_lcm_get_backlight)
    - [kdrv_lcm_get_db_frame](#kdrv_lcm_get_db_frame)
    - [kdrv_lcm_pressing](#kdrv_lcm_pressing)
    - [kdrv_lcm_pressingnir](#kdrv_lcm_pressingnir)
    - [kdrv_lcm_read_data](#kdrv_lcm_read_data)
    - [kdrv_lcm_write_cmd](#kdrv_lcm_write_cmd)
    - [kdrv_lcm_write_data](#kdrv_lcm_write_data)


---




#### Functions
### kdrv_lcm_get_backlight
> Get the lightness value of backlight

```c
u8 kdrv_lcm_get_backlight(
	void
)
```
**Returns:**

u8  lightness value


---
### kdrv_lcm_get_db_frame
> Get address of frame buffer which was showed on display

```c
uint32_t kdrv_lcm_get_db_frame(
	void
)
```
**Returns:**

uint32_t   Address of frame buffer


---
### kdrv_lcm_pressing
> Update frame data of RGB camerea on display

```c
kdrv_status_t kdrv_lcm_pressing(
	kdrv_display_t *display_drv
	u32 addr
)
```
**Parameters:**

<pre>
<em>*display_drv</em>    [in]      @ref kdrv_display_t
<em>addr</em>            [in]      Address of frame buffer
</pre>
**Returns:**

kdrv_status_t   @ref kdrv_status_t


---
### kdrv_lcm_pressingnir
> Update image data of NIR camera n display

```c
kdrv_status_t kdrv_lcm_pressingnir(
	kdrv_display_t *display_drv
	u32 addr
)
```
**Parameters:**

<pre>
<em>*display_drv</em>    [in]      @ref kdrv_display_t
<em>addr</em>            [in]      Address of frame buffer
</pre>
**Returns:**

kdrv_status_t   @ref kdrv_status_t


---
### kdrv_lcm_read_data
> Read data from LCM

```c
unsigned int kdrv_lcm_read_data(
	uint32_t base
)
```
**Parameters:**

<pre>
<em>base</em>            [in]      base address
</pre>
**Returns:**

unsigned int    data


---
### kdrv_lcm_write_cmd
> Write command to LCM

```c
kdrv_status_t kdrv_lcm_write_cmd(
	uint32_t base
	unsigned char data
)
```
**Parameters:**

<pre>
<em>base</em>            [in]      base address
<em>data</em>            [in]      data to write
</pre>
**Returns:**

kdrv_status_t   @ref kdrv_status_t


---
### kdrv_lcm_write_data
> Write data to LCM

```c
kdrv_status_t kdrv_lcm_write_data(
	uint32_t base
	unsigned char data
)
```
**Parameters:**

<pre>
<em>base</em>            [in]      base address
<em>data</em>            [in]      data to write
</pre>
**Returns:**

kdrv_status_t   @ref kdrv_status_t


---

### 9.8. KDRV_MIPICSIRX
#### Kneron mipicsirx driver




**Include Header File:**  kdrv_mipicsirx.h

- Enumerations
    - [ csirx_cam_e ](#csirx_cam_e)
- Functions
    - [kdrv_csi2rx_enable](#kdrv_csi2rx_enable)
    - [kdrv_csi2rx_initialize](#kdrv_csi2rx_initialize)
    - [kdrv_csi2rx_reset](#kdrv_csi2rx_reset)
    - [kdrv_csi2rx_set_power](#kdrv_csi2rx_set_power)
    - [kdrv_csi2rx_start](#kdrv_csi2rx_start)


---




#### Enumerations
### **csirx_cam_e**
enum **csirx_cam_e** {...}
> Enumeration of index of CSI2RX camera

| Enumerator | |
|:---|:--- |
|CSI2RX_CAM_0,       | Enum 0, CSI2RX camera 0 |
|CSI2RX_CAM_1,       | Enum 1, CSI2RX camera 1 |
|CSI2RX_CAM_NUM,     | Enum 2, total of CSI2RX cameras |


---




#### Functions
### kdrv_csi2rx_enable
> Set mipicsirx related register for IP enable.

```c
kdrv_status_t kdrv_csi2rx_enable(
	uint32_t input_type
	uint32_t cam_idx
	uint32_t sensor_idx
	struct cam_format* fmt
)
```
**Parameters:**

<pre>
<em>input_type</em>      [in]      sensor input type
<em>cam_idx</em>         [in]      cam idx
<em>sensor_idx</em>      [in]      sensor idx
<em>fmt</em>             [in]      camera related format setting
</pre>
**Returns:**

kdrv_status_t


---
### kdrv_csi2rx_initialize
> Initiclize mipicsirx related variable.

```c
kdrv_status_t kdrv_csi2rx_initialize(
	uint32_t cam_idx
)
```
**Parameters:**

<pre>
<em>cam_idx</em>         [in]      cam idx
</pre>
**Returns:**

kdrv_status_t


---
### kdrv_csi2rx_reset
> Reset mipicsirx.

```c
kdrv_status_t kdrv_csi2rx_reset(
	uint32_t cam_idx
	uint32_t sensor_idx
)
```
**Parameters:**

<pre>
<em>cam_idx</em>         [in]      cam_idx
<em>on</em>              [in]      csirx power status, 1: ON, 0:Off
</pre>
**Returns:**

kdrv_status_t


---
### kdrv_csi2rx_set_power
> Set mipicsirx power related register.

```c
kdrv_status_t kdrv_csi2rx_set_power(
	uint32_t cam_idx
	uint32_t on
)
```
**Parameters:**

<pre>
<em>cam_idx</em>         [in]      cam_idx
<em>on</em>              [in]      csirx power status, 1: ON, 0:Off
</pre>
**Returns:**

kdrv_status_t


---
### kdrv_csi2rx_start
> Set mipicsirx related register for IP start.

```c
kdrv_status_t kdrv_csi2rx_start(
	uint32_t input_type
	uint32_t cam_idx
)
```
**Parameters:**

<pre>
<em>input_type</em>      [in]      sensor input type
<em>cam_idx</em>         [in]      cam_idx
</pre>
**Returns:**

kdrv_status_t


---

### 9.9. KDRV_MPU
#### Kneron MPU driver




**Include Header File:**  kdrv_mpu.h

- Functions
    - [kdrv_mpu_config](#kdrv_mpu_config)
    - [kdrv_mpu_niram_disable](#kdrv_mpu_niram_disable)
    - [kdrv_mpu_niram_enable](#kdrv_mpu_niram_enable)


---

#### Functions
### kdrv_mpu_config
> config memorty protect space, siram + niram

```c
void kdrv_mpu_config(
	void
)
```
**Returns:**

N/A


---
### kdrv_mpu_niram_disable
> mpu protect disable for niram memory space

```c
void kdrv_mpu_niram_disable(
	void
)
```
**Returns:**

N/A


---
### kdrv_mpu_niram_enable
> mpu protect enable for niram memory space

```c
void kdrv_mpu_niram_enable(
	void
)
```
**Returns:**

N/A


---

### 9.10. KDRV_NCPU
#### Kneron NCPU driver


**Include Header File:**  kdrv_ncpu.h

- Simple Typedef
    - [typedef void (*ipc_handler_t)(int ipc_idx, int state);](#typedef void (*ipc_handler_t)(int ipc_idx, int state);)
- Functions
    - [kdrv_ncpu_get_avail_com](#kdrv_ncpu_get_avail_com)
    - [kdrv_ncpu_get_input](#kdrv_ncpu_get_input)
    - [kdrv_ncpu_get_output](#kdrv_ncpu_get_output)
    - [kdrv_ncpu_initialize](#kdrv_ncpu_initialize)
    - [kdrv_ncpu_set_image_active](#kdrv_ncpu_set_image_active)
    - [kdrv_ncpu_set_model](#kdrv_ncpu_set_model)
    - [kdrv_ncpu_set_model_active](#kdrv_ncpu_set_model_active)
    - [kdrv_ncpu_set_ncpu_debug_lvl](#kdrv_ncpu_set_ncpu_debug_lvl)
    - [kdrv_ncpu_set_scpu_debug_lvl](#kdrv_ncpu_set_scpu_debug_lvl)
    - [kdrv_ncpu_trigger_int](#kdrv_ncpu_trigger_int)


---


#### Simple Typedefs
### **typedef void (*ipc_handler_t)(int ipc_idx, int state);**
> Function pointer of IPC callback


---


#### Functions
### kdrv_ncpu_get_avail_com
> Get available COM

```c
int kdrv_ncpu_get_avail_com(
	void
)
```
**Returns:**

COM index


---
### kdrv_ncpu_get_input
> Get ncpu_to_scpu_s

```c
ncpu_to_scpu_t* kdrv_ncpu_get_input(
	void
)
```
**Returns:**

Pointer to struct struct ncpu_to_scpu_s


---
### kdrv_ncpu_get_output
> Get scpu_to_ncpu_s

```c
scpu_to_ncpu_t* kdrv_ncpu_get_output(
	void
)
```
**Returns:**

Pointer to struct scpu_to_ncpu_s


---
### kdrv_ncpu_initialize
> Initialize NPU functionality

```c
void kdrv_ncpu_initialize(
	ipc_handler_t ipc_handler
)
```
**Parameters:**

<pre>
<em>ipc_handler</em>     [in]      IPC callback
</pre>
---
### kdrv_ncpu_set_image_active
> Set active image index

```c
int kdrv_ncpu_set_image_active(
	uint32_t index
)
```
**Parameters:**

<pre>
<em>index</em>           [in]      image index
</pre>
**Returns:**

available COM


---
### kdrv_ncpu_set_model
> Set model information

```c
void kdrv_ncpu_set_model(
	struct kdp_model_s *model_info_addr
	uint32_t info_idx
	int32_t slot_idx
)
```
**Parameters:**

<pre>
<em>model_info_addr</em> [in]      model information address
<em>info_idx</em>        [in]      information index
<em>slot_idx</em>        [in]      slot index
</pre>
---
### kdrv_ncpu_set_model_active
> Set active model index

```c
void kdrv_ncpu_set_model_active(
	int ipc_idx
	uint32_t index
)
```
**Parameters:**

<pre>
<em>ipc_idx</em>         [in]      IPC index
<em>index</em>           [in]      model slot index
</pre>
---
### kdrv_ncpu_set_ncpu_debug_lvl
> Set NCPU debug level

```c
void kdrv_ncpu_set_ncpu_debug_lvl(
	uint32_t lvl
)
```
**Parameters:**

<pre>
<em>lvl</em>             [in]      level
</pre>
---
### kdrv_ncpu_set_scpu_debug_lvl
> Set SCPU debug level

```c
void kdrv_ncpu_set_scpu_debug_lvl(
	uint32_t lvl
)
```
**Parameters:**

<pre>
<em>lvl</em>             [in]      level
</pre>
---
### kdrv_ncpu_trigger_int
> Trigger NCPU interrupt

```c
void kdrv_ncpu_trigger_int(
	int ipc_idx
)
```
**Parameters:**

<pre>
<em>ipc_idx</em>         [in]      IPC channel to trigger
</pre>
---

### 9.11. KDRV_PINMUX
#### Kneron pinmux config driver


**Include Header File:**  kdrv_pinmux.h

- Enumerations
    - [ kdrv_pin_name](#kdrv_pin_name)
    - [kdrv_pin_driving](#kdrv_pin_driving)
    - [kdrv_pin_pull](#kdrv_pin_pull)
    - [kdrv_pinmux_mode](#kdrv_pinmux_mode)
- Functions
    - [kdrv_pinmux_config](#kdrv_pinmux_config)
    - [kdrv_pinmux_init](#kdrv_pinmux_init)


---


#### Enumerations
### **kdrv_pin_name**
typedef enum **kdrv_pin_name** {...}
> Enumerations of KDP520 all configurable pins

| Enumerator | |
|:---|:--- |
|KDRV_PIN_SPI_WP_N = 0,      | PAD name X_SPI_WP_N, default PIN_MODE_0|
|KDRV_PIN_SPI_HOLD_N,        | PAD name X_SPI_HOLD_N, default PIN_MODE_0|
|KDRV_PIN_JTAG_TRST_N,       | PAD name X_JTAG_TRST_N, default PIN_MODE_0|
|KDRV_PIN_JTAG_TDI,          | PAD name X_JTAG_TDI, default PIN_MODE_0|
|KDRV_PIN_JTAG_SWDITMS,      | PAD name X_JTAG_SWDITMS, default PIN_MODE_0|
|KDRV_PIN_JTAG_SWCLKTCK,     | PAD name X_JTAG_SWCLKTCK, default PIN_MODE_0|
|KDRV_PIN_JTAG_TDO,          | PAD name X_JTAG_TDO, default PIN_MODE_0|
|KDRV_PIN_LC_PCLK,           | PAD name X_LC_PCLK, default PIN_MODE_0|
|KDRV_PIN_LC_VS,             | PAD name X_LC_VS, default PIN_MODE_0|
|KDRV_PIN_LC_HS,             | PAD name X_LC_HS, default PIN_MODE_0|
|KDRV_PIN_LC_DE,             | PAD name X_LC_DE, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_0,         | PAD name X_LC_DATA_0, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_1,         | PAD name X_LC_DATA_1, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_2,         | PAD name X_LC_DATA_2, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_3,         | PAD name X_LC_DATA_3, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_4,         | PAD name X_LC_DATA_4, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_5,         | PAD name X_LC_DATA_5, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_6,         | PAD name X_LC_DATA_6, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_7,         | PAD name X_LC_DATA_7, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_8,         | PAD name X_LC_DATA_8, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_9,         | PAD name X_LC_DATA_9, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_10,        | PAD name X_LC_DATA_10, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_11,        | PAD name X_LC_DATA_11, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_12,        | PAD name X_LC_DATA_12, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_13,        | PAD name X_LC_DATA_13, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_14,        | PAD name X_LC_DATA_14, default PIN_MODE_0|
|KDRV_PIN_LC_DATA_15,        | PAD name X_LC_DATA_15, default PIN_MODE_0|
|KDRV_PIN_SD_CLK,            | PAD name X_SD_CLK, default PIN_MODE_0|
|KDRV_PIN_SD_CMD,            | PAD name X_SD_CMD, default PIN_MODE_0|
|KDRV_PIN_SD_DAT_0,          | PAD name X_SD_DAT_0, default PIN_MODE_0|
|KDRV_PIN_SD_DAT_1,          | PAD name X_SD_DAT_1, default PIN_MODE_0|
|KDRV_PIN_SD_DAT_2,          | PAD name X_SD_DAT_2, default PIN_MODE_0|
|KDRV_PIN_SD_DAT_3,          | PAD name X_SD_DAT_3, default PIN_MODE_0|
|KDRV_PIN_UART0_RX,          | PAD name X_UART0_RX, default PIN_MODE_0|
|KDRV_PIN_UART0_TX,          | PAD name X_UART0_TX, default PIN_MODE_0|
|KDRV_PIN_I2C0_SCL,          | PAD name X_I2C0_SCL, default PIN_MODE_0|
|KDRV_PIN_I2C0_SDA,          | PAD name X_I2C0_SDA, default PIN_MODE_0|
|KDRV_PIN_PWM0               | PAD name X_PWM0, default PIN_MODE_0|


---
### **kdrv_pin_driving**
typedef enum **kdrv_pin_driving** {...}
> Enumerations of KDP520 output driving capability

| Enumerator | |
|:---|:--- |
|PIN_DRIVING_4MA,            | 4mA  - 00, Enum 0|
|PIN_DRIVING_8MA,            | 8mA  - 01, Enum 1|
|PIN_DRIVING_12MA,           | 12mA - 10, Enum 2|
|PIN_DRIVING_16MA,           | 16mA - 11, Enum 3|


---
### **kdrv_pin_pull**
typedef enum **kdrv_pin_pull** {...}
> Enumerations of KDP520 pull status

| Enumerator | |
|:---|:--- |
|PIN_PULL_NONE,              | Pin none,      Enum 0 |
|PIN_PULL_UP,                | Pin pull up,   Enum 1 |
|PIN_PULL_DOWN,              | Pin pull down, Enum 2|


---
### **kdrv_pinmux_mode**
typedef enum **kdrv_pinmux_mode** {...}
> Enumerations of KDP520 pinmux modes

| Enumerator | |
|:---|:--- |
|PIN_MODE_0 = 0,             | Pimux mode 0, Enum 0|
|PIN_MODE_1,                 | Pimux mode 1, Enum 1|
|PIN_MODE_2,                 | Pimux mode 2, Enum 2|
|PIN_MODE_3,                 | Pimux mode 3, for GPIO mode only, Enum 3|
|PIN_MODE_4,                 | Pimux mode 4, Enum 4|
|PIN_MODE_5,                 | Pimux mode 5, Enum 5|
|PIN_MODE_6,                 | Pimux mode 6, Enum 6|
|PIN_MODE_7                  | Pimux mode 7, Enum 7|


---


#### Functions
### kdrv_pinmux_config
> Pinmux configure

```c
void kdrv_pinmux_config(
	kdrv_pin_name pin
	kdrv_pinmux_mode mode
	kdrv_pin_pull pull_type
	kdrv_pin_driving driving
)
```
**Parameters:**

<pre>
<em>pin</em>             [in]      see @ref kdrv_pin_name
<em>mode</em>            [in]      see @ref kdrv_pinmux_mode
<em>pull_type</em>       [in]      see @ref kdrv_pin_pull
<em>driving</em>         [in]      see @ref kdrv_pin_driving
</pre>
**Returns:**

N/A


---
### kdrv_pinmux_init
> Pinmux init

```c
void kdrv_pinmux_init(
	void
)
```
**Returns:**

N/A


---

### 9.12. KDRV_POWER
#### Kneron power driver


KL520 is a system with one NPU, two CPUs, and peripherals.\n
One CPU handles system requests such as host communication, camera video and display, and peripherals.\n
Another CPU assists NPU to do works like input image preprocessing and postprocessing.\n
Two CPUs use shared memory and interrupt for their communication (IPC).\n\n
Upon power-on, default power domain will be turned on and the initial bootloader code (IPL) in ROM starts to run on SCPU.\n
Once the secondary bootloader (SPL) is loaded to system internal SRAM by IPL, SPL will load SCPU OS and NCPU OS in SRAM and\n
pass over the execution SCPU OS.\n
Once NCPU OS is started (by SCPU OS), it will stay in idle thread and listen to commands from SCPU.\n
SCPU will also stay in idle thread and listen to host commands in companion mode or listen to user commands in standalone mode.



**Include Header File:**  kdrv_power.h

- Enumerations
    - [ kdrv_power_domain_t](#kdrv_power_domain_t)
    - [ kdrv_power_mode_t](#kdrv_power_mode_t)
    - [ kdrv_power_ops_t](#kdrv_power_ops_t)
- Functions
    - [kdrv_power_ops](#kdrv_power_ops)
    - [kdrv_power_set_domain](#kdrv_power_set_domain)
    - [kdrv_power_softoff](#kdrv_power_softoff)
    - [kdrv_power_sw_reset](#kdrv_power_sw_reset)


---

#### Enumerations
### **kdrv_power_domain_t**
typedef enum **kdrv_power_domain_t** {...}
> Enumerations of kl520 power domains

| Enumerator | |
|:---|:--- |
|POWER_DOMAIN_DEFAULT = 1,   | Enum 1, Power to Default power domain triggered by wake-up events |
|POWER_DOMAIN_NPU,           | Enum 2, Power to NPU power domain controlled by software |
|POWER_DOMAIN_DDRCK          | Enum 3, Power to DDRCK power domain controlled by software |


---
### **kdrv_power_mode_t**
typedef enum **kdrv_power_mode_t** {...}
> Enumerations of kl520 power modes

| Enumerator | |
|:---|:--- |
|POWER_MODE_RTC = 0,          | Enum 0, RTC |
|POWER_MODE_ALWAYSON,         | Enum 1, RTC + Default |
|POWER_MODE_FULL,             | Enum 2, RTC + Default + DDR + NPU |
|POWER_MODE_RETENTION,        | Enum 3, RTC + Default + DDR(Self-refresh) |
|POWER_MODE_DEEP_RETENTION    | Enum 4, RTC + DDR(Self-refresh) |


---
### **kdrv_power_ops_t**
typedef enum **kdrv_power_ops_t** {...}
> Enumerations of kl520 power operations

| Enumerator | |
|:---|:--- |
|POWER_OPS_FCS = 0,          | Enum 0 |
|POWER_OPS_CHANGE_BUS_SPEED, | Enum 1 |
|POWER_OPS_PLL_UPDATE,       | Enum 2 |
|POWER_OPS_SLEEPING          | Enum 3 |

---


#### Functions
### kdrv_power_ops
> Power operation

```c
kdrv_status_t kdrv_power_ops(
	kdrv_power_ops_t ops
)
```
**Parameters:**

<pre>
<em>ops</em>             [in]      see @ref kdrv_power_ops_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t

---
### kdrv_power_set_domain
> Set power domain

```c
kdrv_status_t kdrv_power_set_domain(
	kdrv_power_domain_t domain
	int enable
)
```
There are three powe domain in Kneron kl520 chip, see @ref kdrv_power_domain_t


**Parameters:**

<pre>
<em>domain</em>          [in]      see @ref kdrv_power_domain_t
<em>enable</em>          [in]      Enable the power domain
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_power_softoff
> Shutdown the power supply to all blocks, except the logic in the RTC domain and DDR memory is in self-refresh state.

```c
kdrv_status_t kdrv_power_softoff(
	kdrv_power_mode_t mode
)
```
**Parameters:**

<pre>
<em>mode</em>            [in]      see @ref kdrv_power_mode_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_power_sw_reset
> Watchdog reset

```c
void kdrv_power_sw_reset(
	void
)
```
---

### 9.13. KDRV_PWM
#### Kneron PWM timer driver

**Include Header File:**  kdrv_owm.h

- Functions
    - [PWMTMR_1000MSEC_PERIOD](#PWMTMR_1000MSEC_PERIOD)
    - [kdrv_current_t2_tick](#kdrv_current_t2_tick)
    - [kdrv_current_t3_tick](#kdrv_current_t3_tick)
    - [kdrv_current_t4_tick](#kdrv_current_t4_tick)
    - [kdrv_current_t5_tick](#kdrv_current_t5_tick)
    - [kdrv_current_t6_tick](#kdrv_current_t6_tick)
    - [kdrv_pwm_config](#kdrv_pwm_config)
    - [kdrv_pwm_disable](#kdrv_pwm_disable)
    - [kdrv_pwm_enable](#kdrv_pwm_enable)
    - [kdrv_pwmtimer_close](#kdrv_pwmtimer_close)
    - [kdrv_pwmtimer_delay_ms](#kdrv_pwmtimer_delay_ms)
    - [kdrv_pwmtimer_initialize](#kdrv_pwmtimer_initialize)
    - [kdrv_pwmtimer_tick_reset](#kdrv_pwmtimer_tick_reset)


---

#### Functions
### PWMTMR_1000MSEC_PERIOD
> Definition of PWM timer period

```c
#define APB_CLK                     APB_CLOCK                       /**< APB bus clock grequency */#define PWMTMR_1000MSEC_PERIOD      (
	uint32_t)(APB_CLK)             /**< PWM timer 1000 ms period */#define PWMTMR_5000MSEC_PERIOD      (uint32_t)(APB_CLK*5)           /**< PWM timer 5000 ms period */#define PWMTMR_100MSEC_PERIOD       (uint32_t)(APB_CLK/10)          /**< PWM timer 100 ms period */#define PWMTMR_20MSEC_PERIOD        (uint32_t)(APB_CLK/50)          /**< PWM timer 20 ms period */#define PWMTMR_15MSEC_PERIOD        (uint32_t)(((APB_CLK/100)*3)/2) /**< PWM timer 15 ms period */#define PWMTMR_10MSEC_PERIOD        (uint32_t)(APB_CLK/100)         /**< PWM timer 10 ms period */#define PWMTMR_1MSEC_PERIOD         (uint32_t)(APB_CLK/1000)        /**< PWM timer 1 ms period */#define PWMTMR_01MSEC_PERIOD        (uint32_t)(APB_CLK/10000)       /**< PWM timer 100 us period *//*** @brief  Enumerations of all timer callback event return status*/typedef enum {PWMTIMER1=1
	/**< Enum 1
	PWM timer callback instance 1 */PWMTIMER2=2
	/**< Enum 2
	PWM timer callback instance 2 */PWMTIMER3=3
	/**< Enum 3
	PWM timer callback instance 3 */PWMTIMER4=4
	/**< Enum 4
	PWM timer callback instance 4 */PWMTIMER5=5
	/**< Enum 5
	PWM timer callback instance 5 */PWMTIMER6=6     /**< Enum 6
	PWM timer callback instance 6 */} pwmtimer;/*** @brief Enumerations of kl520 power domains*/typedef enum Timer_IoType{IO_TIMER_RESETALL
	/**< Enum 0 */IO_TIMER_GETTICK
	/**< Enum 1 */IO_TIMER_SETTICK
	/**< Enum 2 */IO_TIMER_SETCLKSRC  /**< Enum 3 */} timeriotype;/*** @brief Enumerations of polarity of a PWM signal*/typedef enum {PWM_POLARITY_NORMAL = 0
	/**< Enum 0
	A high signal for the duration of the duty-cycle
	followed by a low signal for the remainder of the pulse period*/PWM_POLARITY_INVERSED       /**< Enum 1
	A low signal for the duration of the duty-cycle
	followed by a high signal for the remainder of the pulse period*/} pwmpolarity;/*** @brief        Get t1 tick* @return       t1_tick*/uint32_t kdrv_current_t1_tick(void
)
```
---
### kdrv_current_t2_tick
> Get t2 tick

```c
uint32_t kdrv_current_t2_tick(
	void
)
```
**Returns:**

t2_tick


---
### kdrv_current_t3_tick
> Get t3 tick

```c
uint32_t kdrv_current_t3_tick(
	void
)
```
**Returns:**

t3_tick


---
### kdrv_current_t4_tick
> Get t4 tick

```c
uint32_t kdrv_current_t4_tick(
	void
)
```
**Returns:**

t4_tick


---
### kdrv_current_t5_tick
> Get t5 tick

```c
uint32_t kdrv_current_t5_tick(
	void
)
```
**Returns:**

t5_tick


---
### kdrv_current_t6_tick
> Get t6 tick

```c
uint32_t kdrv_current_t6_tick(
	void
)
```
**Returns:**

t6_tick


---
### kdrv_pwm_config
> kdrv_pwm_config

```c
kdrv_status_t kdrv_pwm_config(
	pwmtimer timer
	pwmpolarity polarity
	uint32_t duty
	uint32_t period
	bool ns2clkcnt
)
```
After config pwm timer via this API, you should call kdrv_pwm_enable() to let pwm timer work well.



**Parameters:**

<pre>
<em>timer</em>           [in]      pwm timer id, see @ref pwmtimer
<em>polarity</em>        [in]      polarity, see @ref pwmpolarity
<em>duty_ms</em>         [in]      duty cycle(ms)
<em>period_ms</em>       [in]      period(ms)
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> Example:\n
> kdrv_pwm_config(PWMTIMER1, PWM_POLARITY_NORMAL, duty, PWM0_FREQ_CNT, 0);\n
> kdrv_pwm_enable(PWMTIMER1);


---
### kdrv_pwm_disable
> kdrv_pwm_disable

```c
kdrv_status_t kdrv_pwm_disable(
	pwmtimer timer
)
```
**Parameters:**

<pre>
<em>timer</em>           [in]      pwm timer id, see @ref pwmtimer
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_pwm_enable
> kdrv_pwm_enable

```c
kdrv_status_t kdrv_pwm_enable(
	pwmtimer timer
)
```
**Parameters:**

<pre>
<em>timer</em>           [in]      pwm timer id, see @ref pwmtimer
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_pwmtimer_close
> Close specifiec pwm timer id.

```c
kdrv_status_t kdrv_pwmtimer_close(
	pwmtimer timer
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pwm timer id, see @ref pwmtimer
</pre>
**Returns:**

kdrv_status_t       see @ref kdrv_status_t


---
### kdrv_pwmtimer_delay_ms
> Use pwm timer to delay for certain time interval.

```c
kdrv_status_t kdrv_pwmtimer_delay_ms(
	uint32_t msec
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      timer id
</pre>
**Returns:**

kdrv_status_t       see @ref kdrv_status_t


**Notes:**

> This API uses @ref PWMTIMER1 to run pwm timer tick.\n
> You should avoid to use the duplicated @ref pwmtimer.\n
> If you don't want to occupy one PWM timer instance, please refer to use @ref kdrv_timer_delay_ms()


---
### kdrv_pwmtimer_initialize
> Initialize specific timer id and give tick.

```c
kdrv_status_t kdrv_pwmtimer_initialize(
	pwmtimer timer
	uint32_t tick
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pwm timer id, see @ref pwmtimer
<em>tick</em>            [in]      tick number
</pre>
**Returns:**

kdrv_status_t       see @ref kdrv_status_t


---
### kdrv_pwmtimer_tick_reset
> Reset pwm timer tick

```c
kdrv_status_t kdrv_pwmtimer_tick_reset(
	pwmtimer timer
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pwm timer id, see @ref pwmtimer
</pre>
**Returns:**

kdrv_status_t       see @ref kdrv_status_t


---

### 9.14. KDRV_SPIF
#### Kneron spi flash driver

**Include Header File:**  kdrv_spif.h

- Functions
    - [MEMXFER_OPS_MASK](#MEMXFER_OPS_MASK)
    - [kdrv_spif_check_quad_status_till_ready](#kdrv_spif_check_quad_status_till_ready)
    - [kdrv_spif_check_status_till_ready](#kdrv_spif_check_status_till_ready)
    - [kdrv_spif_check_status_till_ready_2](#kdrv_spif_check_status_till_ready_2)
    - [kdrv_spif_memxfer_initialize](#kdrv_spif_memxfer_initialize)
    - [kdrv_spif_pre_log](#kdrv_spif_pre_log)
    - [kdrv_spif_read_Rx_FIFO](#kdrv_spif_read_Rx_FIFO)
    - [kdrv_spif_read_data](#kdrv_spif_read_data)
    - [kdrv_spif_rxfifo_depth](#kdrv_spif_rxfifo_depth)
    - [kdrv_spif_set_commands](#kdrv_spif_set_commands)
    - [kdrv_spif_switch_low_speed](#kdrv_spif_switch_low_speed)
    - [kdrv_spif_switch_org](#kdrv_spif_switch_org)
    - [kdrv_spif_txfifo_depth](#kdrv_spif_txfifo_depth)
    - [kdrv_spif_uninitialize](#kdrv_spif_uninitialize)
    - [kdrv_spif_wait_command_complete](#kdrv_spif_wait_command_complete)
    - [kdrv_spif_wait_rx_full](#kdrv_spif_wait_rx_full)
    - [kdrv_spif_write_data](#kdrv_spif_write_data)


---

#### Functions
### MEMXFER_OPS_MASK
> Definition of memory transfer operations

```c
#define MEMXFER_OPS_NONE  0x00    /**< Memory transfer operations - none */#define MEMXFER_OPS_CPU   0x01    /**< Memory transfer operations - cpu */#define MEMXFER_OPS_DMA   0x02    /**< Memory transfer operations - dma */#define MEMXFER_INITED    0x10    /**< Memory transfer operations - initialization */#define MEMXFER_OPS_MASK  (
	MEMXFER_OPS_CPU | MEMXFER_OPS_DMA) /**< Memory transfer operations - bit mask *//*-----------------------------------------------------------------------*                          Puclic flash driver API*-----------------------------------------------------------------------*//*** @brief       Initialize spi flash include hardware setting
	operation frequency
	and flash status check** @note        This API MUST be called before using the Read/write APIs for spi flash.*/void kdrv_spif_initialize(void
)
```
---
### kdrv_spif_check_quad_status_till_ready
> wait quad read command completed and check status till ready

```c
void kdrv_spif_check_quad_status_till_ready(
	void
)
```
---
### kdrv_spif_check_status_till_ready
> wait command completed and check status till it's ready

```c
void kdrv_spif_check_status_till_ready(
	void
)
```
---
### kdrv_spif_check_status_till_ready_2
> check status till the progress is done and ready for next step

```c
void kdrv_spif_check_status_till_ready_2(
	void
)
```
---
### kdrv_spif_memxfer_initialize
> Initialize spi flash for memxfer include hardware setting, operation frequency, and flash status check.

```c
void kdrv_spif_memxfer_initialize(
	uint8_t flash_mode
	uint8_t mem_mode
)
```
**Parameters:**

<pre>
<em>flash_mode</em>      [in]      flash operating mode
<em>mem_mode</em>        [in]      memory operating mode
</pre>
---
### kdrv_spif_pre_log
> to remeber the original settings for SPI flash

```c
void kdrv_spif_pre_log(
	void
)
```
---
### kdrv_spif_read_Rx_FIFO
> read Rx FIFO data

```c
void kdrv_spif_read_Rx_FIFO(
	uint32_t *buf_word
	uint16_t *buf_word_index
	uint32_t target_byte
)
```
**Parameters:**

<pre>
<em>*buf_word</em>       [in]      buffer for the data read from flash
<em>*buf_word_index</em> [in]      start from specific flash index
<em>target_byte</em>     [in]      data size
</pre>
---
### kdrv_spif_read_data
> read data from specific index in spi flash

```c
void kdrv_spif_read_data(
	/*uint8_t*/uint32_t *buf
	uint32_t length
)
```
**Parameters:**

<pre>
<em>*buf</em>            [in]      buffer for the data read from flash
                          length      data size
</pre>
---
### kdrv_spif_rxfifo_depth
> Check the RX FIFO size, unit in byte

```c
uint32_t kdrv_spif_rxfifo_depth(
	void
)
```
**Returns:**

>0          RX FIFO depth


---
### kdrv_spif_set_commands
> set spi communication commands including read/write by 3/4bytes address, dummy byte size, operation mode, etc

```c
void kdrv_spif_set_commands(
	uint32_t cmd0
	uint32_t cmd1
	uint32_t cmd2
	uint32_t cmd3
)
```
**Parameters:**

<pre>
<em>cmd0</em>            [in]      ~ 3
</pre>
---
### kdrv_spif_switch_low_speed
> to switch to low speed (50Mhz) SPI flash settings

```c
void kdrv_spif_switch_low_speed(
	void
)
```
---
### kdrv_spif_switch_org
> to switch back to original SPI flash settings

```c
void kdrv_spif_switch_org(
	void
)
```
---
### kdrv_spif_txfifo_depth
> Check the TX FIFO size, unit in byte

```c
uint32_t kdrv_spif_txfifo_depth(
	void
)
```
**Returns:**

>0          TX FIFO depth


---
### kdrv_spif_uninitialize
> Uninitialize spi flash and clear related variables

```c
kdrv_status_t kdrv_spif_uninitialize(
	void
)
```
**Returns:**

@ref kdrv_status_t


---
### kdrv_spif_wait_command_complete
> Check status bit to wait until command completed

```c
void kdrv_spif_wait_command_complete(
	void
)
```
---
### kdrv_spif_wait_rx_full
> Wait until the RX FIFO is full so ready to read

```c
void kdrv_spif_wait_rx_full(
	void
)
```
---
### kdrv_spif_write_data
> write data to specific index in spi flash

```c
void kdrv_spif_write_data(
	uint8_t *buf
	uint32_t length
)
```
**Parameters:**

<pre>
<em>*buf</em>            [in]      buffer for the data to write to flash
<em>length</em>          [in]      data size
</pre>
---

### 9.15. KDRV_SYSTEM
#### Kneron system driver


**Include Header File:**  kdrv_system.h

- Functions
    - [kdrv_system_init](#kdrv_system_init)
    - [kdrv_system_init_ncpu](#kdrv_system_init_ncpu)
    - [kdrv_system_reset](#kdrv_system_reset)


---

#### Functions
### kdrv_system_init
> Definition of index of FW

```c
#define SCPU_FW     1   /**< Index of SCPU FW */#define NCPU_FW     2   /**< Index of NCPU FW *//*** @brief Enumeration of system reset*/enum {SUBSYS_NPU      = 1,    /**< Software reset for NPU */SUBSYS_PD_NPU,          /**< Software reset for whole NPU domain */SUBSYS_LCDC,            /**< Software reset for LCDC */SUBSYS_NCPU,            /**< The signal controls SYSRESETn of NCPU */};/*** @brief           System initialize* @details         Turn on NPU/DDR power domain and enable some main clock PLL .\n*/void kdrv_system_init(
	void
)
```
---
### kdrv_system_init_ncpu
> NCPU system initialize

```c
void kdrv_system_init_ncpu(
	void
)
```
Enable NCPU/NPU and some main PLL clock .\n


**Notes:**

> This API should be called after @ref kdrv_system_init() to make sure NPU/DDR power domain is powered on.


---
### kdrv_system_reset
> System reset

```c
void kdrv_system_reset(
	int32_t subsystem
)
```
**Parameters:**

<pre>
<em>subsystem</em>       [in]      subsystem reset id
</pre>
**Notes:**

> SUBSYS_NPU:         reset NPU
> SUBSYS_PD_NPU:      reset whole NPU domain(clk+ddr phy)
> SUBSYS_LCDC:        reset LCDC
> SUBSYS_NCPU:        reset NCPU


---

### 9.16. KDRV_TIMER
#### Kneron timer driver

**Include Header File:**  kdrv_timer.h

- Simple Typedef
    - [typedef void (*timer_cb_fr_isr_t) (cb_event_t argument, void* arg);](#typedef void (*timer_cb_fr_isr_t) (cb_event_t argument, void* arg);)
- Enumerations
    - [cb_event_t](#cb_event_t)
    - [timer_stat_t](#timer_stat_t)
- Functions
    - [kdrv_timer_close](#kdrv_timer_close)
    - [kdrv_timer_delay_ms](#kdrv_timer_delay_ms)
    - [kdrv_timer_delay_us](#kdrv_timer_delay_us)
    - [kdrv_timer_initialize](#kdrv_timer_initialize)
    - [kdrv_timer_open](#kdrv_timer_open)
    - [kdrv_timer_perf_get_instant](#kdrv_timer_perf_get_instant)
    - [kdrv_timer_perf_measure_get](#kdrv_timer_perf_measure_get)
    - [kdrv_timer_perf_measure_start](#kdrv_timer_perf_measure_start)
    - [kdrv_timer_perf_open](#kdrv_timer_perf_open)
    - [kdrv_timer_perf_reset](#kdrv_timer_perf_reset)
    - [kdrv_timer_perf_set](#kdrv_timer_perf_set)
    - [kdrv_timer_set](#kdrv_timer_set)
    - [kdrv_timer_uninitialize](#kdrv_timer_uninitialize)


---

#### Simple Typedefs
### **typedef void (*timer_cb_fr_isr_t) (cb_event_t argument, void* arg);**
> Enumerations of all timer status for kdrv_timer_set


---

#### Enumerations
### **cb_event_t**
typedef enum **cb_event_t** {...}
> Enumerations of all timer call back even return status

| Enumerator | |
|:---|:--- |
|TIMER_M1_TIMEOUT,   | Enum 0, reach timer M1 level |
|TIMER_M2_TIMEOUT,   | Enum 1, reach timer M2 level|
|TIMER_OF_TIMEOUT    | Enum 2, timer overfloor|


---
### **timer_stat_t**
typedef enum **timer_stat_t** {...}
> Enumerations of all timer status for kdrv_timer_set

| Enumerator | |
|:---|:--- |
|TIMER_PAUSE,        | Enum 0, Timer state pause |
|TIMER_START,        | Enum 1, Timer state start |
|TIMER_STAT_DEFAULT  | Enum 2, Timer state default |


---

#### Functions
### kdrv_timer_close
> Close specific timer id.

```c
kdrv_status_t kdrv_timer_close(
	uint32_t* TimerId
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pointer of timer id
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_delay_ms
> Let system delay ms

```c
kdrv_status_t kdrv_timer_delay_ms(
	uint32_t msec
)
```
**Parameters:**

<pre>
<em>usec</em>            [in]      time interval(ms).
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_delay_us
> Let system delay us

```c
kdrv_status_t kdrv_timer_delay_us(
	uint32_t usec
)
```
**Parameters:**

<pre>
<em>usec</em>            [in]      time interval(us).
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_initialize
> Enable clock, init timer ip, register IRQ/ISR function

```c
kdrv_status_t kdrv_timer_initialize(
	void
)
```
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_open
> Request one timer id for further usage.

```c
kdrv_status_t kdrv_timer_open(
	uint32_t* TimerId
	timer_cb_fr_isr_t event_cb
	void *arg
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [out]     pointer of timer id.
<em>event_cb</em>        [in]      timer_cb_fr_isr_t, see @ref timer_cb_fr_isr_t
<em>arg</em>             [in]      user define argument
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_perf_get_instant
> Get time consumption.

```c
kdrv_status_t kdrv_timer_perf_get_instant(
	uint32_t* TimerId
	uint32_t* instant
	uint32_t* time
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pointer of timer id
<em>instant</em>         [out]     pointer of time instant register
</pre>
**Returns:**

Time cunsumption


---
### kdrv_timer_perf_measure_get
> Get time interval

```c
kdrv_status_t kdrv_timer_perf_measure_get(
	uint32_t *instant
	uint32_t *time
)
```
**Parameters:**

<pre>
<em>instant</em>         [in]      Difference time interval compare to last time instant.
<em>time</em>            [in]      Current time.
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_perf_measure_start
> Start to use performance measurement function.

```c
kdrv_status_t kdrv_timer_perf_measure_start(
	void
)
```
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---
### kdrv_timer_perf_open
> Open a timer with specific timer id for performance measurement.

```c
kdrv_status_t kdrv_timer_perf_open(
	uint32_t* TimerId
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [out]     pointer of timer id
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> Need use @ref kdrv_timer_perf_set() to start timing measurement.


---
### kdrv_timer_perf_reset
> Reset performance timer.

```c
kdrv_status_t kdrv_timer_perf_reset(
	uint32_t* TimerId
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pointer of timer id
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> After call @ref kdrv_timer_perf_open(), you should reset this timer first.\n
> Example:\n
> uint32_t perftimerid;
> kdrv_timer_perf_open(&pftimerid);\n
> kdrv_timer_perf_reset(&pftimerid);


---
### kdrv_timer_perf_set
> Set specific timer for performance measurment usage.

```c
kdrv_status_t kdrv_timer_perf_set(
	uint32_t* TimerId
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pointer of timer id
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> You should call @ref kdrv_timer_perf_open() and @ref kdrv_timer_perf_reset() firstly before call this API.\n
> Example:\n
> uint32_t perftimerid;\n
> kdrv_timer_perf_open(&pftimerid);\n
> kdrv_timer_perf_reset(&pftimerid);\n
> kdrv_timer_perf_set(&perftimerid);


---
### kdrv_timer_set
> Set specific timer with interval and status.

```c
kdrv_status_t kdrv_timer_set(
	uint32_t* TimerId
	uint32_t Intval
	timer_stat_t State
)
```
**Parameters:**

<pre>
<em>TimerId</em>         [in]      pointer of timer id
<em>Interval</em>        [in]      set timer interval
<em>timer_stat</em>      [in]      see timer_stat, see @ref timer_stat_t
</pre>
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


**Notes:**

> This API should be called after kdrv_timer_open()\n
> Example:\n
> uint32_t timerid;\n
> kdrv_timer_open(&timerid, NULL, NULL);\n
> kdrv_timer_set(&timerid, 5000000, TIMER_START);


---
### kdrv_timer_uninitialize
> Disable clock, and timer IRQ

```c
kdrv_status_t kdrv_timer_uninitialize(
	void
)
```
**Returns:**

kdrv_status_t   see @ref kdrv_status_t


---

### 9.17. KDRV_UART
#### Kneron UART driver


Here are the design highlight points:\n
* The architecture adopts a lightweight non-thread design\n
* ISR driven architecture.\n
* Can support both synchronous and asynchronous mode\n
* Utilizes FIFO advantage to reduce interrupts and improve robust to accommodate more latency than normal.


**Include Header File:**  kdrv_uart.h

- Enumerations
    - [ DRVUART_PORT](#DRVUART_PORT)
    - [ kdrv_uart_control_t](#kdrv_uart_control_t)
    - [ kdrv_uart_dev_id_t](#kdrv_uart_dev_id_t)
    - [ kdrv_uart_mode_t](#kdrv_uart_mode_t)
- Structs
    - [ kdrv_uart_config_t](#kdrv_uart_config_t)
    - [ kdrv_uart_fifo_config_t](#kdrv_uart_fifo_config_t)
- Functions
    - [BAUD_921600](#BAUD_921600)
    - [kdrv_uart_close](#kdrv_uart_close)
    - [kdrv_uart_configure](#kdrv_uart_configure)
    - [kdrv_uart_get_char](#kdrv_uart_get_char)
    - [kdrv_uart_get_rx_count](#kdrv_uart_get_rx_count)
    - [kdrv_uart_get_tx_count](#kdrv_uart_get_tx_count)
    - [kdrv_uart_initialize](#kdrv_uart_initialize)
    - [kdrv_uart_open](#kdrv_uart_open)
    - [kdrv_uart_read](#kdrv_uart_read)
    - [kdrv_uart_uninitialize](#kdrv_uart_uninitialize)
    - [kdrv_uart_write](#kdrv_uart_write)


---

#### Enumerations
### **DRVUART_PORT**
typedef enum **DRVUART_PORT** {...}
> Enumerations of UART port parameters.

| Enumerator | |
|:---|:--- |
|DRVUART_PORT0 = 0,  | Enum 0, UART port 0 |
|DRVUART_PORT1 = 1,  | Enum 1, UART port 1 |
|DRVUART_PORT2 = 2,  | Enum 2, UART port 2 |
|DRVUART_PORT3 = 3,  | Enum 3, UART port 3 |
|DRVUART_PORT4 = 4   | Enum 4, UART port 4 |


---
### **kdrv_uart_control_t**
typedef enum **kdrv_uart_control_t** {...}
> Enumerations of UART control hardware signals

| Enumerator | |
|:---|:--- |
|UART_CTRL_CONFIG,       | Enum 0, set @ref kdrv_uart_config_t |
|UART_CTRL_FIFO_RX,      | Enum 1, set @ref kdrv_uart_fifo_config_t |
|UART_CTRL_FIFO_TX,      | Enum 2, set @ref kdrv_uart_fifo_config_t |
|UART_CTRL_LOOPBACK,     | Enum 3, UART loopback enable |
|UART_CTRL_TX_EN,        | Enum 4, UART transmitter enable |
|UART_CTRL_RX_EN,        | Enum 5, UART receiver enable |
|UART_CTRL_ABORT_TX,     | Enum 6, UART abort transmitter |
|UART_CTRL_ABORT_RX,     | Enum 7, UART abort receiver |
|UART_CTRL_TIMEOUT_RX,   | Enum 8, UART receiver timeout value |
|UART_CTRL_TIMEOUT_TX    | Enum 9, UART transmitter timeout value |


---
### **kdrv_uart_dev_id_t**
typedef enum **kdrv_uart_dev_id_t** {...}
> Enumerations of UART device instance parameters.

| Enumerator | |
|:---|:--- |
|UART0_DEV = 0,          | Enum 0, UART device instance 0 |
|UART1_DEV,              | Enum 1, UART device instance 1 |
|UART2_DEV,              | Enum 2, UART device instance 2 |
|UART3_DEV,              | Enum 3, UART device instance 3 |
|UART4_DEV,              | Enum 4, UART device instance 4 |
|TOTAL_UART_DEV          | Enum 5, Total UART device instances |


---
### **kdrv_uart_mode_t**
typedef enum **kdrv_uart_mode_t** {...}
> Enumerations of UART mode parameters.

| Enumerator | |
|:---|:--- |
|UART_MODE_ASYN_RX = 0x1,    | Enum 0x1, UART asynchronous receiver mode. |
|UART_MODE_ASYN_TX = 0x2,    | Enum 0x2, UART asynchronous transmitter mode. |
|UART_MODE_SYNC_RX = 0x4,    | Enum 0x4, UART synchronous receiver mode. |
|UART_MODE_SYNC_TX = 0x8     | Enum 0x8,  UART synchronous transmitter mode. |


---


#### Structs
### kdrv_uart_config_t
typedef struct **kdrv_uart_config_t** {...}
> The structure of UART configuration parameters.

|Members| |
|:---|:--- |
|uint32_t baudrate;| UART baud rate. |
|uint8_t data_bits;| UART data bits, a data character contains 5~8 data bits. |
|uint8_t frame_length;| UART frame length, non-zero value for FIR mode|
|uint8_t stop_bits;| UART stop bit, a data character is proceded by a start bit \n<br />and is followed by an optional parity bit and a stop bit. |
|uint8_t parity_mode;| UART partity mode, see @ref UART_PARITY_DEF |
|bool fifo_en;| UART fifo mode. |


---
### kdrv_uart_fifo_config_t
typedef struct **kdrv_uart_fifo_config_t** {...}
> The structure of UART FIFO configuration parameters.

|Members| |
|:---|:--- |
|bool bEnFifo;| Is FIFO enabled |
|uint8_t fifo_trig_level;| FIFO trigger level |


---

#### Functions
### BAUD_921600
> Enumerations of UART baud rate.

```c
#define BAUD_921600 (
	UART_CLOCK / 14745600)     /**< UART baud rate: 921600. */#define BAUD_460800 (UART_CLOCK / 7372800)      /**< UART baud rate: 460800. */#define BAUD_115200 (UART_CLOCK / 1843200)      /**< UART baud rate: 115200. */#define BAUD_57600 (UART_CLOCK / 921600)        /**< UART baud rate: 57600. */#define BAUD_38400 (UART_CLOCK / 614400)        /**< UART baud rate: 38400. */#define BAUD_19200 (UART_CLOCK / 307200)        /**< UART baud rate: 19200. */#define BAUD_14400 (UART_CLOCK / 230400)        /**< UART baud rate: 14400. */#define BAUD_9600 (UART_CLOCK / 153600)         /**< UART baud rate: 9600. */#define BAUD_4800 (UART_CLOCK / 76800)          /**< UART baud rate: 4800. */#define BAUD_2400 (UART_CLOCK / 38400)          /**< UART baud rate: 2400. */#define BAUD_1200 (UART_CLOCK / 19200)          /**< UART baud rate: 1200. *//*** @brief The definition of UART parity.*/#define PARITY_NONE 0       /**< Disable Parity */#define PARITY_ODD 1        /**< Odd Parity */#define PARITY_EVEN 2       /**< Even Parity */#define PARITY_MARK 3       /**< Stick odd Parity */#define PARITY_SPACE 4      /**< Stick even Parity */typedef int32_t kdrv_uart_handle_t;typedef void (*kdrv_uart_callback_t)(uint32_t event
)
```
---
### kdrv_uart_close
> close the UART port

```c
kdrv_status_t kdrv_uart_close(
	kdrv_uart_handle_t handle
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_configure
> set control for the opened UART port

```c
kdrv_status_t kdrv_uart_configure(
	kdrv_uart_handle_t handle
	kdrv_uart_control_t prop
	uint8_t *val
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
<em>prop</em>            [in]      control enumeration
<em>val</em>             [in]      pointer to control value/structure
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_get_char
> read character data from UART port

```c
kdrv_status_t kdrv_uart_get_char(
	kdrv_uart_handle_t handle
	char *ch
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
<em>ch</em>              [out]     character data
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_get_rx_count
> get char number in RX buffer

```c
uint32_t kdrv_uart_get_rx_count(
	kdrv_uart_handle_t handle
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
</pre>
**Returns:**

number of RX count in the buffer


---
### kdrv_uart_get_tx_count
> get char number in TX buffer

```c
uint32_t kdrv_uart_get_tx_count(
	kdrv_uart_handle_t handle
)
```
**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
</pre>
**Returns:**

number of TX count in the buffer


---
### kdrv_uart_initialize
> UART driver initialization, it shall be called once in lifecycle

```c
kdrv_status_t kdrv_uart_initialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_open
> Open one UART port and acquire a uart port handle

```c
kdrv_status_t kdrv_uart_open(
	kdrv_uart_handle_t *handle
	uint8_t com_port
	uint32_t mode
	kdrv_uart_callback_t callback
)
```
This API will open a UART device (com_port: 0-5) for use.\n
It will return a UART device handle for future device reference.\n
The client can choose work mode: asynchronization or synchronization.\n
Synchronization mode will poll the hardware status to determine send/receiving point,\n
it will consume more power and introduce more delay to system execution.\n
But in the case of non-thread light weight environment, such as message log function, this mode is easy and suitable.\n
Asynchronization mode lets the driver interrupt driven, save more system power and more efficient,\n
the client needs to have a thread to listen/wait for the event/signal sent from callback function.\n
Callback function parameter 'callback' will be registered with this device which is mandatory for async mode,\n
will be invoked whenever Tx/Rx complete or timeout occur.\n
This callback function should be very thin, can only be used to set flag or send signals



**Parameters:**

<pre>
<em>handle</em>          [out]     a handle of an UART port
<em>com_port</em>        [in]      UART port id
<em>mode</em>            [in]      bit combination of kdrv_uart_mode_t
<em>callback</em>        [in]      user callback function
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_read
> read data from the UART port

```c
kdrv_status_t kdrv_uart_read(
	kdrv_uart_handle_t handle
	uint8_t *buf
	uint32_t len
)
```
The client can call this API to receive UART data from remote side.\n
Depending on the work mode, a little bit different behavior exists there.\n
In synchronous mode, the API call will not return until all data was received physically.\n
In asynchronous mode, the API call shall return immediately with UART_API_RX_BUSY.\n
When enough bytes are received or timeout occurs, the client registered callback function will be invoked.\n
The client shall have a very thin code there to set flags/signals. The client thread shall be listening the signal after this API call.\n
The client shall allocate the receiving buffer with max possible receiving length.\n
When one frame is sent out, after 4 chars transmission time, a timeout interrupt will be generated.


**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
<em>buf</em>             [out]     data buffer
<em>len</em>             [in]      data buffer length
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_uninitialize
> UART driver uninitialization

```c
kdrv_status_t kdrv_uart_uninitialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_uart_write
> write data to uart port, such as command, parameters, but not suitable for chunk data

```c
kdrv_status_t kdrv_uart_write(
	kdrv_uart_handle_t hdl
	uint8_t *buf
	uint32_t len
)
```
The client calls this API to send data out to remote side.\n
Depending on the work mode, a little bit different behavior exists there.\n
In synchronous mode, the API call will not return until all data was sent out physically;\n
In asynchronous mode, the API call shall return immediately with UART_API_TX_BUSY.\n
When all the buffer data is sent out, the client registered callback function will be invoked.\n
The client shall have a very thin code there to set flags/signals. The client thread shall be listening the signal after this API call.\n


**Parameters:**

<pre>
<em>handle</em>          [in]      device handle for an UART port
<em>buf</em>             [in]      data buffer
<em>len</em>             [in]      data buffer length
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---

### 9.18. KDRV_USBD
#### Kneron USB device mode driver


This USBD driver API implementation is based on an event-driven architecture.\n
For async mode API usage, to get notified of specific USB events,\n
user of USBD API needs to create a user thread to listen events by waiting for a specified thread flag (CMSIS-RTOS v2)\n
which is registered at early time.\n\n
Listening events is optional for sync mode usage by not setting notification for events and use synchronous mode API to perform transfers.\n
Once user is notified with the specified thread flag, a get-event API can be used to retrieve the exact USB event and take a corresponding action for it.\n
USBD handles hardware interrupts directly in ISR context, based on USB protocol to accomplish USB events and transfer work.\n\n
There are two layers of software for a complete USB device mode driver (software layer block diagram is shown as below),\n
one is USBD driver itself which provides a set of generic APIs with prefix "kdrv_usbd" them,\n
another is the function driver which can leverage USBD API to implement.\n\n
At present there is none of class drivers like MSC or CDC come with the USBD implementation, however users can implement their own function\n
driver for custom use cases.


**Include Header File:**  kdrv_usbd.h

- Defines
    - MAX_USBD_CONFIG
    - MAX_USBD_INTERFACE
    - MAX_USBD_ENDPOINT
- Enumerations
    - [ kdrv_usbd_event_name_t](#kdrv_usbd_event_name_t)
    - [ kdrv_usbd_speed_t](#kdrv_usbd_speed_t)
    - [ kdrv_usbd_status_respond_t](#kdrv_usbd_status_respond_t)
- Structs
    - [](#)
    - [ kdrv_usbd_config_descriptor_t](#kdrv_usbd_config_descriptor_t)
    - [ kdrv_usbd_device_descriptor_t](#kdrv_usbd_device_descriptor_t)
    - [ kdrv_usbd_device_qualifier_descriptor_t](#kdrv_usbd_device_qualifier_descriptor_t)
    - [ kdrv_usbd_endpoint_descriptor_t](#kdrv_usbd_endpoint_descriptor_t)
    - [ kdrv_usbd_interface_descriptor_t](#kdrv_usbd_interface_descriptor_t)
    - [ kdrv_usbd_prd_string_descriptor_t](#kdrv_usbd_prd_string_descriptor_t)
    - [ kdrv_usbd_setup_packet_t](#kdrv_usbd_setup_packet_t)
    - [ kdrv_usbd_string_descriptor_t](#kdrv_usbd_string_descriptor_t)
- Functions
    - [kdrv_usbd_bulk_receive_async](#kdrv_usbd_bulk_receive_async)
    - [kdrv_usbd_bulk_send](#kdrv_usbd_bulk_send)
    - [kdrv_usbd_bulk_send_async](#kdrv_usbd_bulk_send_async)
    - [kdrv_usbd_control_receive](#kdrv_usbd_control_receive)
    - [kdrv_usbd_control_respond](#kdrv_usbd_control_respond)
    - [kdrv_usbd_control_send](#kdrv_usbd_control_send)
    - [kdrv_usbd_get_event](#kdrv_usbd_get_event)
    - [kdrv_usbd_initialize](#kdrv_usbd_initialize)
    - [kdrv_usbd_interrupt_receive](#kdrv_usbd_interrupt_receive)
    - [kdrv_usbd_interrupt_send](#kdrv_usbd_interrupt_send)
    - [kdrv_usbd_is_dev_configured](#kdrv_usbd_is_dev_configured)
    - [kdrv_usbd_register_thread_notification](#kdrv_usbd_register_thread_notification)
    - [kdrv_usbd_reset_device](#kdrv_usbd_reset_device)
    - [kdrv_usbd_reset_endpoint](#kdrv_usbd_reset_endpoint)
    - [kdrv_usbd_set_device_descriptor](#kdrv_usbd_set_device_descriptor)
    - [kdrv_usbd_set_device_qualifier_descriptor](#kdrv_usbd_set_device_qualifier_descriptor)
    - [kdrv_usbd_set_enable](#kdrv_usbd_set_enable)
    - [kdrv_usbd_set_string_descriptor](#kdrv_usbd_set_string_descriptor)
    - [kdrv_usbd_uninitialize](#kdrv_usbd_uninitialize)


---

#### Defines
| Define | Value | Description |
|:---|:---|:---|
|MAX_USBD_CONFIG|1    | maximum number of configuration descriptor |
|MAX_USBD_INTERFACE|1 | maximum number of interface descriptor |
|MAX_USBD_ENDPOINT|4  | maximum number of endpoint descriptor |


---


#### Enumerations
### **kdrv_usbd_event_name_t**
typedef enum **kdrv_usbd_event_name_t** {...}
> Enumeration of USB event name type

| Enumerator | |
|:---|:--- |
|KDRV_USBD_EVENT_BUS_RESET = 1,       | Enum 1, USBD event of bus reset |
|KDRV_USBD_EVENT_BUS_SUSPEND,         | Enum 2, USBD event of bus suspend |
|KDRV_USBD_EVENT_BUS_RESUME,          | Enum 3, USBD event of bus resume |
|KDRV_USBD_EVENT_SETUP_PACKET,        | Enum 4, USBD event of setup packet |
|KDRV_USBD_EVENT_DEV_CONFIGURED,      | Enum 5, USBD event of device configuration|
|KDRV_USBD_EVENT_TRANSFER_BUF_FULL,   | Enum 6, USBD event of transfer buffer full |
|KDRV_USBD_EVENT_TRANSFER_DONE,       | Enum 7, USBD event of transfer done |
|KDRV_USBD_EVENT_TRANSFER_OUT,        | Enum 8, USBD event of transfer out |
|KDRV_USBD_EVENT_TRANSFER_TERMINATED, | Enum 9, USBD event of transfer terminated |
|KDRV_USBD_EVENT_DMA_ERROR,           | Enum 10, USBD event of DMA error |

---
### **kdrv_usbd_speed_t**
typedef enum **kdrv_usbd_speed_t** {...}
> Enumeration of connection speed

| Enumerator | |
|:---|:--- |
|KDRV_USBD_HIGH_SPEED,   | Enum 0, USB high speed |
|KDRV_USBD_FULL_SPEED    | Enum 1, USB full speed, not supported yet |


---
### **kdrv_usbd_status_respond_t**
typedef enum **kdrv_usbd_status_respond_t** {...}
> Enumeration of code for response to host in control transfer

| Enumerator | |
|:---|:--- |
|KDRV_USBD_RESPOND_OK,       | Enum 0, send ACK in the status stage |
|KDRV_USBD_RESPOND_ERROR     | Enum 1, send STALL in the status stage |


---

#### Structs
###
typedef struct **** {...}
> USB event, it includes kdrv_usbd_event_name_t and related data

|Members| |
|:---|:--- |
|kdrv_usbd_event_name_t ename;| see @ref kdrv_usbd_event_name_t |
|union {| Union struct|
|kdrv_usbd_setup_packet_t setup;| see @ref kdrv_usbd_setup_packet_t |
|struct| Structure of bit field |
|uint32_t data1;| 4 bytes data 1|
|uint32_t data2;| 4 bytes data 2|


---
### kdrv_usbd_config_descriptor_t
typedef struct **kdrv_usbd_config_descriptor_t** {...}
> Configuration descriptor struct

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint16_t wTotalLength;| Total length |
|uint8_t bNumInterfaces;| Number of interfaces|
|uint8_t bConfigurationValue;| Configuration value |
|uint8_t iConfiguration;| Configuration|
|uint8_t bmAttributes;| Attribute|
|uint8_t MaxPower;| Max power|
|kdrv_usbd_interface_descriptor_t *interface[MAX_USBD_INTERFACE];| *interface, @ref  kdrv_usbd_interface_descriptor_t|


---
### kdrv_usbd_device_descriptor_t
typedef struct **kdrv_usbd_device_descriptor_t** {...}
> Device descriptor struct

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint16_t bcdUSB;| bcd USB |
|uint8_t bDeviceClass;| Device class |
|uint8_t bDeviceSubClass;| Device sub-class |
|uint8_t bDeviceProtocol;| Device protocol |
|uint8_t bMaxPacketSize0;| Max. packet size |
|uint16_t idVendor;| Vendor id |
|uint16_t idProduct;| Product id |
|uint16_t bcdDevice;| bcd device |
|uint8_t iManufacturer;| Manufacturer |
|uint8_t iProduct;| Product|
|uint8_t iSerialNumber;| Serial number|
|uint8_t bNumConfigurations;| Number of configurations |
|kdrv_usbd_config_descriptor_t *config[MAX_USBD_CONFIG];| *config, @ref  kdrv_usbd_config_descriptor_t|


---
### kdrv_usbd_device_qualifier_descriptor_t
typedef struct **kdrv_usbd_device_qualifier_descriptor_t** {...}
> Device qualifier descriptor struct

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint16_t bcdUSB;| bcd USB |
|uint8_t bDeviceClass;| Device class |
|uint8_t bDeviceSubClass;| Device sub-class |
|uint8_t bDeviceProtocol;| Device protocol |
|uint8_t bMaxPacketSize0;| Max. packet size |
|uint8_t bNumConfigurations;| Number of configurations |
|uint8_t bReserved;| Reserved |


---
### kdrv_usbd_endpoint_descriptor_t
typedef struct **kdrv_usbd_endpoint_descriptor_t** {...}
> Endpoint descriptor struct

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint8_t bEndpointAddress;| Endpoint address |
|uint8_t bmAttributes;| Attributes |
|uint16_t wMaxPacketSize;| Max. packet size |
|uint8_t bInterval;| Interval|


---
### kdrv_usbd_interface_descriptor_t
typedef struct **kdrv_usbd_interface_descriptor_t** {...}
> Interface descriptor struct

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint8_t bInterfaceNumber;| Interface mumber |
|uint8_t bAlternateSetting;| Alternate setting |
|uint8_t bNumEndpoints;| Number of endpoints|
|uint8_t bInterfaceClass;| Interface class|
|uint8_t bInterfaceSubClass;| Interface sub-class|
|uint8_t bInterfaceProtocol;| Interface protocol |
|uint8_t iInterface;| Interface |
|kdrv_usbd_endpoint_descriptor_t *endpoint[MAX_USBD_ENDPOINT];| *endpoint, @ref  kdrv_usbd_endpoint_descriptor_t|


---
### kdrv_usbd_prd_string_descriptor_t
typedef struct **kdrv_usbd_prd_string_descriptor_t** {...}
> Device prd string descriptor

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint8_t bString[32];| 32 Bytes string |


---
### kdrv_usbd_setup_packet_t
typedef struct **kdrv_usbd_setup_packet_t** {...}
> 8-byte setup packet struct

|Members| |
|:---|:--- |
|uint8_t bmRequestType;| Request type |
|uint8_t bRequest;| Request |
|uint16_t wValue;| Write value |
|uint16_t wIndex;| Write index |
|uint16_t wLength;| Write length |


---
### kdrv_usbd_string_descriptor_t
typedef struct **kdrv_usbd_string_descriptor_t** {...}
> Device string descriptor

|Members| |
|:---|:--- |
|uint8_t bLength;| Length |
|uint8_t bDescriptorType;| Descriptor type |
|uint16_t bLanguageID;| Language Id |
|kdrv_usbd_prd_string_descriptor_t *desc[3];| *desc, @ref  ;       |


---

#### Functions
### kdrv_usbd_bulk_receive_async
> Bulk-OUT transfser, receive data from the host through a bulk-out endpoint in non-blocking mode

```c
kdrv_status_t kdrv_usbd_bulk_receive_async(
	uint32_t endpoint
	uint32_t *buf
	uint32_t blen
)
```
this works with kdrv_usbd_get_event(), when receiving a 'KDRV_USBD_EVENT_TRANSFER_OUT' event,
user should commit a buffer for Bulk Out transfer through this function.
when transfer is done by usbd, eihter a 'KDRV_USBD_EVENT_TRANSFER_DONE' or 'KDRV_USBD_EVENT_TRANSFER_BUF_FULL' event
will be sent to user.



**Parameters:**

<pre>
<em>endpoint</em>        [in]      a bulk-out endpoint address, should be the value from bEndpointAddress
<em>buf</em>             [in]      buffer for receiving data
<em>blen</em>            [in]      buffer length
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_bulk_send
> Bulk-IN transfser, send data to host through a bulk-in endpont in blocking mode

```c
kdrv_status_t kdrv_usbd_bulk_send(
	uint32_t endpoint
	uint32_t *buf
	uint32_t txLen
	uint32_t timeout_ms
)
```
**Parameters:**

<pre>
<em>endpoint</em>        [in]      a bulk-in endpoint address, should be the value from bEndpointAddress
<em>buf</em>             [in]      data to be sent to host
<em>txLen</em>           [in]      number of bytes to be transfered
<em>timeout_ms</em>      [in]      timeout in millisecond
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_bulk_send_async
> Bulk-IN transfser, send data to host through a bulk-in endpont in non-blocking mode

```c
kdrv_status_t kdrv_usbd_bulk_send_async(
	uint32_t endpoint
	// should be the value from bEndpointAddressuint32_t *buf
	// memory addres to be read fromuint32_t txLen);   // transfer length/*** @brief           Bulk-OUT transfser
	receive data from the host through a bulk-out endpoint in blocking mode** @param[in]       endpoint              a bulk-out endpoint address
	should be the value from bEndpointAddress* @param[out]      buf                   buffer for receiving data* @param[in
	out]   blen                  buffer length for input
	actual transfered length for output* @param[in]       timeout_ms            timeout in millisecond* @return          kdrv_status_t         see @ref kdrv_status_t*/kdrv_status_t kdrv_usbd_bulk_receive(uint32_t endpoint
	uint32_t *buf
	uint32_t *blen
	uint32_t timeout_ms
)
```
user can commit a buffer for Bulk In transfer, and then wait for KDRV_USBD_EVENT_TRANSFER_DONE
to be notified that the transfer is done or some error code if failed.
This function works with kdrv_usbd_get_event().

**Parameters:**

<pre>
<em>endpoint</em>        [in]      a bulk-in endpoint address, should be the value from bEndpointAddress
<em>buf</em>             [in]      data to be sent to host
<em>txLen</em>           [in]      number of bytes to be transfered
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_control_receive
> Control-OUT transfer, receive data from host through the control endpont

```c
kdrv_status_t kdrv_usbd_control_receive(
	uint8_t *buf
	uint32_t *size
	uint32_t timeout_ms
)
```
for a user-defined vendor reqeust & control OUT & wLength > 0,
user should use this function to receive data from host,
or respond an error via kdrv_usbd_control_respond(KDRV_USBD_RESPOND_ERROR) to claim STALL

**Parameters:**

<pre>
<em>buf</em>             [out]     buffer for receiving data
<em>size</em>            [in]      buffer length
<em>timeout_ms</em>      [in]      timeout in millisecond
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_control_respond
> respond to host through control transfer in the status stage

```c
kdrv_status_t kdrv_usbd_control_respond(
	kdrv_usbd_status_respond_t status
)
```
this function is used as response function to report status for a user-defined vendor request



**Parameters:**

<pre>
<em>status</em>          [in]      status, see @ref kdrv_usbd_status_respond_t
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_control_send
> Control-IN transfer, send data to host through the control endpont

```c
kdrv_status_t kdrv_usbd_control_send(
	uint8_t *buf
	uint32_t size
	uint32_t timeout_ms
)
```
for a user-defined vendor reqeust & control IN & wLength > 0,
user should use this function to send data to host,
or respond an error via kdrv_usbd_control_respond(KDRV_USBD_RESPOND_ERROR) to claim STALL



**Parameters:**

<pre>
<em>buf</em>             [in]      data to be sent to host
<em>size</em>            [in]      number of bytes to be transfered
<em>timeout_ms</em>      [in]      timeout in millisecond
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_get_event
> get a usbd event, this is a blocking function for sync mode usage of USBD APIs

```c
kdrv_status_t kdrv_usbd_get_event(
	kdrv_usbd_event_t *uevent
)
```
@kdrv_usbd_get_event() when awake from osThreadFlagsWait( ) due to USBD notification,\n
users can use this function to retrieve which event is appearing and then take the corresponding action.\n
While performing transfers, user can also get notified through this call such as bulk-in notification or transfer complete notifications.



**Parameters:**

<pre>
<em>uevent</em>          [in]      usbd event to be notified, see @ref kdrv_usbd_event_t
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_initialize
> USB device mode driver initialization

```c
kdrv_status_t kdrv_usbd_initialize(
	void
)
```
This API should be the first call for USBD driver initialization and to invoke the driver thread.


**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_interrupt_receive
> Interrupt-OUT transfer in blocking mode

```c
kdrv_status_t kdrv_usbd_interrupt_receive(
	uint32_t endpoint
	// should be the value from bEndpointAddressuint32_t *buf
	uint32_t *rxLen
	uint32_t timeout_ms
)
```
**Parameters:**

<pre>
<em>endpoint</em>        [in]      a interrupt-out endpoint address, should be the value from bEndpointAddress
<em>buf</em>             [out]     buffer for receiving data
<em>rxLen</em>           [in,out]  buffer length for input, actual transfered length for output, should be less than MaxPacketSize
<em>timeout_ms</em>      [in]      timeout in millisecond
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_interrupt_send
> Interrupt-IN transfer in blocking mode

```c
kdrv_status_t kdrv_usbd_interrupt_send(
	uint32_t endpoint
	uint32_t *buf
	uint32_t txLen
	uint32_t timeout_ms
)
```
Immediately write data to the FIFO buffer for periodic interrupt-in transfer.
Note even while the old data is not yet read by host, this function will overwrite it.



**Parameters:**

<pre>
<em>endpoint</em>        [in]      a interrupt-in endpoint address, should be the value from bEndpointAddress
<em>buf</em>             [in]      data to be sent to host
<em>txLen</em>           [in]      transfer length, shoudl be less then MaxPacketSize
<em>timeout_ms</em>      [in]      timeout in millisecond
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_is_dev_configured
> check if device is enumerated and configured by a host

```c
bool kdrv_usbd_is_dev_configured(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_register_thread_notification
> register user thread ID and thread flag for notifications including events or transfer completion/errors

```c
kdrv_status_t kdrv_usbd_register_thread_notification(
	osThreadId_t tid
	uint32_t tflag
)
```
**Parameters:**

<pre>
<em>tid</em>             [in]      CMSIS-RTOS v2 thread ID
<em>tflag</em>           [in]      user defined thread flag to be notified by osThreadFlagsSet()
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_reset_device
> reset device and then it can be re-enumerated by host

```c
kdrv_status_t kdrv_usbd_reset_device(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_reset_endpoint
> reset specified endpoint

```c
kdrv_status_t kdrv_usbd_reset_endpoint(
	uint32_t endpoint
)
```
**Parameters:**

<pre>
<em>status</em>          [in]      status
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_set_device_descriptor
> configure device descriptor including configuration, interface and all endpoints descriptors

```c
kdrv_status_t kdrv_usbd_set_device_descriptor(
	kdrv_usbd_speed_t speed
	kdrv_usbd_device_descriptor_t *dev_desc
)
```
USBD driver API provides specific data structs for these descriptors, users must statically declare instances of these descriptors in memory which will be used when being enumerated by a USB host.\n
At present some limitations should be noted:\n
1. Support only one configuration descriptor, one interface descriptor and 4 endpoint descriptors.\n
2. Isochronous transfer is not supported yet.\n
3. If enabling log message through USB then one endpoint must be reserved for USBD internal use.\n



**Parameters:**

<pre>
<em>speed</em>           [in]      speed want to run, now support only High-Speed
<em>dev_desc</em>        [in]      user crated device descriptor, this must be kept during device enumeration
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_set_device_qualifier_descriptor
> configure device qualifier descriptor, this is optional

```c
kdrv_status_t kdrv_usbd_set_device_qualifier_descriptor(
	kdrv_usbd_speed_t speed
	kdrv_usbd_device_qualifier_descriptor_t *dev_qual_desc
)
```
This API is to set other speed when acting in high-speed, users can set a meaningful content in this descriptor.



**Parameters:**

<pre>
<em>speed</em>           [in]      speed want to run, now support only High-Speed
<em>dev_qual_desc</em>   [in]      user crated device qualifier descriptor, this must be kept during device enumeration
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_set_enable
> set enable/disabale of USB device mode, host can enumerate this device only if device is enabled

```c
kdrv_status_t kdrv_usbd_set_enable(
	bool enable
)
```
Once above calls are done properly, users can invoke this function to enable the device and after that it can start to be seen and be enumerated by a USB host.\n
Once device is enabled and enumerated by a host, some USB events may start appearing,\n
user must start to wait for a specified thread flag to be notified of USB events through the osThreadFlagsWait(), events will be introduced in next section.



**Parameters:**

<pre>
<em>enable</em>          [in]      true to enable, false to disable
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_set_string_descriptor
> configure device manufacturer, product , serial number

```c
kdrv_status_t kdrv_usbd_set_string_descriptor(
	kdrv_usbd_speed_t speed
	kdrv_usbd_string_descriptor_t *dev_str_desc
)
```
**Parameters:**

<pre>
<em>speed</em>           [in]      speed want to run, now support only High-Speed
<em>dev_str_desc</em>    [in]      device string descriptor
</pre>
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---
### kdrv_usbd_uninitialize
> USB device mode driver uninitialization

```c
kdrv_status_t kdrv_usbd_uninitialize(
	void
)
```
**Returns:**

kdrv_status_t         see @ref kdrv_status_t


---

### 9.19. KDRV_WDT
#### Kneron WDT driver

**Include Header File:**  kdrv_usbd.h

- Functions
    - [REG_WDT_CNT](#REG_WDT_CNT)
    - [kdrv_wdt_disable](#kdrv_wdt_disable)
    - [kdrv_wdt_is_counter_zero](#kdrv_wdt_is_counter_zero)
    - [kdrv_wdt_read_counter](#kdrv_wdt_read_counter)
    - [kdrv_wdt_reset](#kdrv_wdt_reset)
    - [kdrv_wdt_set_auto_reload](#kdrv_wdt_set_auto_reload)
    - [kdrv_wdt_set_clear_status](#kdrv_wdt_set_clear_status)
    - [kdrv_wdt_set_int_counter](#kdrv_wdt_set_int_counter)
    - [kdrv_wdt_sys_int_disable](#kdrv_wdt_sys_int_disable)
    - [kdrv_wdt_sys_int_enable](#kdrv_wdt_sys_int_enable)
    - [kdrv_wdt_sys_reset_disable](#kdrv_wdt_sys_reset_disable)
    - [kdrv_wdt_sys_reset_enable](#kdrv_wdt_sys_reset_enable)


---

#### Functions
### REG_WDT_CNT
> wdt registers definition

```c
#define KDRV_WDT_BASE                   WDT_FTWDT010_PA_BASE    /**<  wdt timer base address*/#define REG_WDT_CNT                     (
	KDRV_WDT_BASE + 0x00)  /**<  wdt timer counter */#define REG_WDT_LOAD                    (KDRV_WDT_BASE + 0x04)  /**<  auto reload register */#define REG_WDT_RST                     (KDRV_WDT_BASE + 0x08)  /**<  restart register */#define REG_WDT_CR                      (KDRV_WDT_BASE + 0x0C)  /**<  control register */#define REG_WDT_STS                     (KDRV_WDT_BASE + 0x10)  /**<  wdt status register */#define REG_WDT_CLR                     (KDRV_WDT_BASE + 0x14)  /**<  wdt time cleared register */#define REG_WDT_INTR_LEN                (KDRV_WDT_BASE + 0x18)  /**<  wdt intr length register */#define REG_WDT_REV                     (KDRV_WDT_BASE + 0x1C)  /**<  wdt revision *//*** @brief wdt control register*/#define WDT_CR_EN                        BIT(0)  /**< WDT enable bit
	0: disable
	1: enable */#define WDT_CR_RST_EN                    BIT(1)  /**< WDT reset bit
	0: disable
	1: enable */#define WDT_CR_INT_EN                    BIT(2)  /**< WDT int enable bit
	0: disable
	1: enable */#define WDT_CR_EXT_EN                    BIT(3)  /**< WDT extclk enable bit
	0:disable
	1:enable */#define WDT_CR_EXTCLK                    BIT(4)  /**< WDT clock source bit
	0:PCLK
	1:EXTCLK *//*** @brief       watchdog enable*/void kdrv_wdt_enable(void
)
```
---
### kdrv_wdt_disable
> watchdog disable

```c
void kdrv_wdt_disable(
	void
)
```
---
### kdrv_wdt_is_counter_zero
> watchdog, is counter zero

```c
bool kdrv_wdt_is_counter_zero(
	void
)
```
**Returns:**

bool


---
### kdrv_wdt_read_counter
> watchdog read counter

```c
uint32_t kdrv_wdt_read_counter(
	void
)
```
**Returns:**

counter value


---
### kdrv_wdt_reset
> watchdog reset

```c
void kdrv_wdt_reset(
	void
)
```
---
### kdrv_wdt_set_auto_reload
> watchdog reload

```c
void kdrv_wdt_set_auto_reload(
	uint32_t value
)
```
**Parameters:**

<pre>
<em>value</em>           [in]      watchdog reload value
</pre>
---
### kdrv_wdt_set_clear_status
> watchdog status clear

```c
void kdrv_wdt_set_clear_status(
	void
)
```
---
### kdrv_wdt_set_int_counter
> watchdog set interrupt counter

```c
void kdrv_wdt_set_int_counter(
	uint8_t counter
)
```
**Parameters:**

<pre>
<em>[in[</em>            [in[   counter set the duration of assertion of wd_intr, the default value is 0xFF.\]counter set the duration of assertion of wd_intr, the default value is 0xFF.\n
                          which means that the default assertion duration is 256 clock cycles(PCLK)
</pre>
---
### kdrv_wdt_sys_int_disable
> watchdog interrupt disable

```c
void kdrv_wdt_sys_int_disable(
	void
)
```
---
### kdrv_wdt_sys_int_enable
> watchdog interrupt enable

```c
void kdrv_wdt_sys_int_enable(
	void
)
```
---
### kdrv_wdt_sys_reset_disable
> watchdog reset disable

```c
void kdrv_wdt_sys_reset_disable(
	void
)
```
---
### kdrv_wdt_sys_reset_enable
> watchdog reset enable

```c
void kdrv_wdt_sys_reset_enable(
	void
)
```
---


## 10. Flash programming



### 10.1. Board Overview

![](./imgs/getting_start_imgs/10_1_1.png)

![](./imgs/getting_start_imgs/10_1_2.png)


### 10.2. Hardware Setting

#### 10.2.1. Connecting UART0 (Program Flash via UART0 Interface)

UART0: Command Port

![](./imgs/getting_start_imgs/10_2_1.png)

#### 10.2.2. Connecting 5V power and trun on power switch

Power from Adapter or from Power Bank (USB PD)

![](./imgs/getting_start_imgs/10_2_2.png)

#### 10.2.3. Wake up chip from RTC power domain by pressing PTN button

Please do it every time after plugging in the power

![](./imgs/getting_start_imgs/10_2_3.png)

#### 10.2.4. Set bootstrap settings to manual boot mode (Program Flash via UART0 Interface)

1. Must set bootstrap settings to manual boot mode
2. Reset pin or power must be controllable to enter manual boot mode.

![](./imgs/getting_start_imgs/10_2_4.png)

### 10.3. Program Flash via UART0 Interface

#### 10.3.1. Flash programmer necessaries

1. Open command terminal for flash programmer execution

   Tool path: kl520_sdk\utils\flash_programmer\flash_programmer.py

2. Install Necessary python modules: kl520_sdk\utils\requirements.txt

3. Limitations: Only the listed argument combinations below are allowed.

#### 10.3.2. Edit python verification setting

1. Check UART port number from device manager

2. Edit setup.py, search “COM_ID” and modify the ID to match your UART port number

   EX: COM_ID = 3 # COM3

   ![](./imgs/getting_start_imgs/10_3_1.png)

#### 10.3.3 Firmware Binary Generation (FW + MODELS)
Generate flash final bin file from other seperate bin files.

The script combines .bin files in "flash_bin" in predefined order.

Morever, the addressing is in 4KB alignment.

**Command**

```shell
$ python3 bin_gen.py
```

    options argument:
    
    -h, --help      Show this help message and exit
    -p, --CPU_ONLY  SPL/SCPU/NCPU only

**Output**

``flash_image.bin``

**Note**

>  The following bin files are must 

```shell
flash_bin/
├── boot_spl.bin		// bool spl bin file
├── fw_ncpu.bin       	// SCPU FW bin file (generated by Keil)
├── fw_scpu.bin			// NCPU FW bin file (generated by Keil)
├── models_520.nef		// model information(copied from [host_lib]/input_models/KL520/[app]/)
```


#### 10.3.4 Flash Chip Programming (FW + DATA)

```shell
$ python flash_programmer.py -a flash_image.bin
```

Please press RESET BTN while you are seeing “Please press reset button!!”

![](./imgs/getting_start_imgs/10_3_2.png)

Afterwards, just wait until all progresses are finished (erase, program, verify)

![](./imgs/getting_start_imgs/10_3_3.png)

**Note**:
"flash_programmer.py -a" means to do flash chip erase + programming + verification

#### 10.3.5 Flash Verification (optional)

```shell
$ python flash_programmer.py -v flash_image.bin
```

#### 10.3.6 Flash Erase (optional)

```shell
$ python flash_programmer.py -e
```

#### 10.3.7 Flash Partial Programming (optional)

```shell
$ python flash_programmer.py -i 0x00002000 -p fw_scpu.bin
```

**Note**:

> To program specific bin file to specific flash address
> "-i" means the flash index/address you would like to program
> "-p" means the FW code you would like to program



### 10.4. Program Flash via JTAG/SWD Interface

#### 10.4.1. Jlink programmer necessaries

Connect JTAG/SWD.

![](./imgs/getting_start_imgs/10_4_1.png)

#### 10.4.2. Edit flash_prog.jlink device setting

1. Check your flash manufacturer: Winbond or Mxic or GigaDevice 

2. Select a specific device based on flash manufacturer

    EX:

    ```
    device KL520-WB	//Winbond
    device KL520-MX	//Mxic
    device KL520-GD	//GigaDevice
    ```

    Copy the bin file to kl520_sdk\utils\JLink_programmer\bin folder

    EX: flash_image.bin, boot_spl.bin, fw_scpu.bin, fw_ncpu.bin, etc.


#### 10.4.3. Double click "flash_prog.bat"

Afterwards, just wait until all progresses are finished (chip erase, program, verify)

![](./imgs/getting_start_imgs/10_4_2.png)

#### 10.4.4. Check programming result

Please ensure all the results are "O.K.", and enter "qc" to quit and close J-Link commander

![](./imgs/getting_start_imgs/10_4_3.png)

#### 10.4.5. Edit flash_prog_partial.jlink device setting(optional)

To program specific bin file to specific flash address

1. Copy the bin file to kl520_sdk\utils\JLink_programmer\bin\

2. Select a specific device+’-P’ based on flash manufacturer

    EX: 

    ```
device KL520-WB-P	//Winbond
device KL520-MX-P	//Mxic
device KL520-GD-P	//GigaDevice
    ```

3. Edit loadbin command: Load *.bin file into target memory

	**Syntax**:

	```
	loadbin <filename>, <addr>  
	loadbin .\bin\boot_spl.bin,0x00000000
	loadbin .\bin\fw_scpu.bin,0x00002000
	loadbin .\bin\fw_ncpu.bin,0x00018000
	```

4. Double click “flash_prog_partial.bat” and wait until all progresses are finished

5. Check programming result

    Please ensure the results is “O.K.”, and enter “qc” to quit and close J-Link commander

    EX:
    ![](./imgs/getting_start_imgs/10_4_4.png)

## 11. UART Device Firmware Write (DFW) Boot 


### 11.1. Hardware Setting

Please refer to chapter 10.2



### 11.2. Design Principles
The purpose of this document is to descript how to develop/apply the DFW (Device Firmware Write) (via UART) Boot feature for KL520.
You can download firmware bin file to KL520 internal Memory space through UART and then directly boot KL520 up from internal memory, therefore external flash could be optional.

#### 11.2.1 KL520 internal memory space address
1.	Minion FW starts from 0x10100000 and size must < 0x2000 bytes
2.	SCPU FW starts from 0x10102000
3.	NCPU FW starts from 0x28000000

![](./imgs/getting_start_imgs/11.2.1.png)

#### 11.2.2 UART_DFW_Boot Workflow
1.	Send Minion FW through UART0/XMODEM and also process the followings sequence through UART0 interface
2.	Minion is the bridge to handle host command, collect bin data and then save it into internal memory space

![](./imgs/getting_start_imgs/11.2.2.png)

#### 11.2.3 Host control principle
1. Initial UART COM port with baud rate 115200 and send ‘2’ to tell KL520 to enter 2.UART(XMODEM) mode.
2. Send Minion.bin through UART by XMODEM protocol.
Reference: https://pythonhosted.org/xmodem/xmodem.html
3. Switch to baud rate 921600.
4. Send SCPU FW to address 0x10102000.
	``Buf[n] = Msg_header + data_buf[4096]``  
	- Msg_header: 

		```
		typedef struct {
			uint16_t preamble;
			uint16_t crc16;
			uint32_t cmd;
			uint32_t addr;
			uint32_t len;
		} __attribute__((packed)) MsgHdr;
		```
	
	- data_buf[4096]: transfer bin by unit 4096 bytes(max.) each time
	- Packet TX Preamble: PKTX_PAMB = 0xA583
	- crc16: calculate checksum from buf[4] to buf[n-1] except preamble and crc16
	- cmd for mem_write: 0x1004
	- cmd for mem_read: 0x1003 (read back for verification)
	- addr: 0x10102000
	- len: 4096 or remainder

5. Send NCPU FW to address 0x28000000.
	``Buf[n] = Msg_header + data_buf[4096]``
	- Msg_header:

		```
		typedef struct {
			uint16_t preamble;
			uint16_t crc16;
			uint32_t cmd;
			uint32_t addr;
			uint32_t len;
		} __attribute__((packed)) MsgHdr; 
		```

	- data_buf[4096]: transfer bin by unit 4096 bytes(max.) each time
	- Packet TX Preamble: PKTX_PAMB = 0xA583
	- crc16: calculate checksum from buf[4] to buf[n-1] except preamble and crc16
	- cmd for mem_write: 0x1004
	- cmd for mem_read: 0x1003 (read back for verification)
	- addr: 0x28000000
	- len: 4096 or remainder

6. Send CHIP_RUN command with address set as 0x10102000.
	``Buf[n] = Msg_header``
	- Msg_header:

		```
		typedef struct {
			uint16_t preamble;
			uint16_t crc16;
			uint32_t cmd;
			uint32_t addr;
			uint32_t len;
		} __attribute__((packed)) MsgHdr;
		```
	
	- Packet TX Preamble: PKTX_PAMB = 0xA583
	- crc16: calculate checksum from buf[4] to buf[n-1] except preamble and crc16
	- cmd for scup_run: 0x1005
	- addr: 0x10102000
	- len: 0


### 11.3. Build dfw_companion firmware
The dfw_companion project in mozart_sw\example_projects\dfw_companion\ is the example for users to develop the firmware without external SPI Flash drivers.
You can rebuild dfw_companion project then get the updated fw_scpu.bin/fw_ncpu.bin in mozart_sw\utils\bin_gen\flash_bin folder.

### 11.4. DFW via UART0 Interface with Python

#### 11.4.1. DFW Boot necessaries

1. Open command terminal for flash programmer execution

   Tool path: kl520_sdk\utils\dfw_boot\uart_dfu_boot.py

2. Install Necessary python modules: kl520_sdk\utils\requirements.txt

3. Limitations: Only the listed argument combinations below are allowed.

#### 11.4.2. Edit python verification setting

Please refer to chapter 10.3.2

#### 11.4.3 Chip Initialize and Send/Start Minion FW

```shell
$ python uart_dfu_boot.py -s
```

Please press RESET BTN while you are seeing “Please press reset button!!”

![](./imgs/getting_start_imgs/11.3.2.png)


Afterwards, just wait until seeing “Xmodem sends Minion file DONE!!!”

![](./imgs/getting_start_imgs/11.3.3.png)


#### 11.4.4 DFW fw_scpu.bin to memory address 0x10102000

```shell
$ python uart_dfu_boot.py -i 0x10102000 -p fw_scpu.bin
```

![](./imgs/getting_start_imgs/11.3.4.png)


#### 11.4.5 DFW fw_ncpu.bin to memory address 0x28000000

```shell
$ python uart_dfu_boot.py -i 0x28000000 -p fw_ncpu.bin
```

![](./imgs/getting_start_imgs/11.3.5.png)


#### 11.4.6 Command to boot up KL520 from memory address 0x10102000

```shell
$ python uart_dfu_boot.py -i 0x10102000 -r
```

![](./imgs/getting_start_imgs/11.3.6.png)

**Note**:

> To write specific bin file to specific memory address
> “-i" means the memory index/address
> “-p" means the FW code you would like to program



### 11.5. DFW via UART0 Interface with hostlib
The kl520_util_uart_dfw_boot example in host_lib\example\KL520\kl520_util_uart_dfw_boot is the reference code for users to develop UART_DFW_Boot feature on their own platform.
You can do integration test with kl520_util_uart_dfw_boot to write SCPU/NCPU firmware to KL520 internal memory space and boot from specific memory address directly.

#### 11.5.1. Edit kl520_util_uart_dfw_boot.cpp to assign proper com port 
Search “#define com_port” and modify the ID to match your UART port number listed on device management.

#### 11.5.2. Build host_lib examples
Refer to host_lib\README_CPP.md for further information.

#### 11.5.3 UART_DFW_Boot integration tests
1. Copy fw_scpu.bin and fw_ncpu.bin to hostlib host_lib\app_binaries\KL520\dfw folder.
2. Execute host_lib\build\bin\kl520_util_uart_dfw_boot, and please press reset button when you see "Please press RESET btn!!......"
3. Please check the message showed after kl520_util_uart_dfw_boot executed, make sure minion bin is transmitted via UART/Xmodem successfully, send fw_scpu.bin/fw_ncpu.bin successfully, and reboot KL520 from specific memory address successfully.

    EX:
    ![](./imgs/getting_start_imgs/11.5.1.png)


## Appendix　

###　Host Mode Example  
This sample code is an application which KL520 chip plays as a host chip with connected display and cameras for Object detection. You will need to program the flash image to device first. The flash image includes SCPU/NCPU firmware and model. Then, you can Start/Stop object detection by simple command via UART. 

**WARNING:** 
**DO NOT** program this FW to Kneron Dongle

---
#### Hardware Requirements

Kneron KL520 series AI SoC Development Kit  

---
#### Firmware Preparation and Installation

- Run Keil MDK and compile reference design 
   Open workspace file ``[KL520_SDK]\example_projects\tiny_yolo_v3_host\workspace.uvmpw``  

	**Notes:**
	User can edit and debug with Keil MDK for further implementation  
	[keil/MDK docs](https://www2.keil.com/mdk5/docs)
	
- Generate the firmware bin image 

	**Reference:** [Firmware Binary Generator](#1033-firmware-binary-generation-fw-models)
```
   #in Windows MINGW64 console
   
   cd [SDK]/utils/bin_gen/flash_bin
   cp -f [KL520_SDK]/models/tiny_yolo_v3/models_520.nef .
   cd ..
   python3 bin_gen.py
   #The compiled SCPU/NCPU FW in step 1 will be placed under flash_bin/ automatically 
   #bin_gen.py will concate SCPU/NCPU FW and models_520.nef and generate flash_image.bin
```

- Program the image  

	**Reference:** [Flash programming](#10-flash-programming)
```
   cd [SDK]/utils/flash_programmer
   python3 flash_programmer.py -a ..\bin_gen\flash_image.bin 
   # follow the instructions to finish flash progrmming
```


---
#### Run example 

1. Turn on KL520 
2. Press PTN button 
3. Select “1” to boot from SPI to boot from the programmed FW
4. Once it’s started, RGB camera and LCD will be turned on, and image will be continuously captured by camera and displayed on LCD panel. 
5. Also, see command menu and type command (1) - (4) for functions in UART console window(ex. Putty)
   
---
#### Commands
1. type "1" in UART console window to **Start Tiny  Yolo**
   When a person is detected, **yellow box** is drawn around the person. 
   Other detected objects are drawn around by **blue boxes**.  
   
	Console window shows detected objects with FPS info. 

2. Type "2" to Stop Object detection
3. Type "3" to turn off Pipeline mode, or toggle the mode, at runtime.  
	- This pipeline mode can be toggled on/off (1/0) to demonstrate performance improvement. 
	- Note that there may be delay to see first good inference due to opening camera/sensor. 


    ![](./imgs/getting_start_imgs/appendix.PNG)
