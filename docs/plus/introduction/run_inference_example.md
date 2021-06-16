# Run Inference Examples

**Note**: We built and run the examples below under OS Ubuntu 18.04.5 LTS with cmake version 3.10.2.

## 1. Build PLUS

1. Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

2. Decompress the **kneron_plus_vXXX.zip**

    ```bash
    $ unzip kneron_plus_v1.0.0.zip
    ```

3. Build code

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j
    ```

    - Once build is done, the **libkplus.so** will be in **build/src/**

    - Example executables will be in **build/bin/**

4. Check if PLUS examples are built successfully.

    ```bash
    $ ls bin/

        kl520_demo_app_yolo_inference
        kl520_demo_app_yolo_inference_multithread
        kl520_demo_customize_inf_multiple_models
        kl520_demo_customize_inf_single_model
        kl520_demo_generic_inference
        ...
    ```

## 2. List Device Info

While one or multiple AI dongles are plugged into the host, they can be scanned to get some basic device information.

```bash
$ sudo ./scan_devices

    scanning kneron devices ...
    number of Kneron devices found: 2

    listing devices infomation as follows:

    [0] scan_index: '0'
    [0] port ID: '517'
    [0] product_id: '0x100' (KL520)
    [0] USB link speed: 'High-Speed'
    [0] USB port path: '1-1-4'
    [0] kn_number: '0x270A265C'
    [0] Connectable: 'True'
    [0] Firmware: 'KDP'

    [1] scan_index: '1'
    [1] port ID: '38'
    [1] product_id: '0x100' (KL520)
    [1] USB link speed: 'High-Speed'
    [1] USB port path: '1-1-5'
    [1] kn_number: '0x63252C53'
    [1] Connectable: 'True'
    [1] Firmware: 'KDP2 Loader'

```

Above shows that it founds two KL520 devices, a brief descript listed below.

- **scan_index** : An index number represents the device in the scanned order, can be used by KP API to establish USB connection.
- **port ID** : An unique number represents the device on the certain usb port, can be used by KP API to establish USB connection.
- **product_id** : The product ID.
- **USB link speed** : USB link speed, High-Speed is fastest speed for USB2.0.
- **USB port path** : This means the physical USB port path on the host.
- **kn_number** : Kneron's serial number for the device.
- **Connectable** : It tells if this device is connectable; one device can only be connected by one program at the same time.
- **Firmware** : This shows which firmware the AI dongle is using, KDP or KDP2 Loader.

## 3. Run Inference Examples

The PLUS provides three categories of API set for model inference.

1. **APP inference** category, providing some decent functions for specific applications with specified NEF models and it is designed to be used in a easy way.

2. **Generic inference** category which is intended for advanced users who are interested in developing their models and implement corresponding post-processing code.

3. **Customized inference** category, providing some decent functions for user to customize their own applications with customized NEF models.

Below will demonstrate only usage in two examples for **APP inference** and **Generic inference**. For **Customized inference**, please refer the documents in Customize API folder.

### 3.1 App Inference Example

The **'app_yolo_inference'** example utilizes the **APP inference API** and the **Tiny Yolo V3 model** to perform object detection.

When no parameters, it takes **res/models/KL520/tiny_yolo_v3/models_520.nef** as the inference model, **res/images/bike_cars_street_224x224.bmp** as the input image in BMP format and repeats 20 loops to calculate performance then prints inference results.

```bash
$ sudo ./kl520_demo_app_yolo_inference

    connect device ... OK
    upload firmware ... OK
    upload model ... OK
    read image ... OK

    starting inference loop 100 times:
    .....................................

    class count : 80
    box count : 5
    Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
    Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
    Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
    Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
    Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2

    output bounding boxes on 'output_bike_cars_street_224x224.bmp'

```

Besides output results in the screen console, it also draws detected objects in a new-created **output_bike_cars_street_224x224.bmp**.

![](../imgs/ex_kdp2_tiny_yolo_v3.bmp)

The key features of APP inference are listed below:

- Specified model NEF.
- Normally post-process is done in SoC.
- Simplfied function parameters.

### 3.2 Generic Inference Example

**Generic inference** API is intended for users who have their own models and applications.

It needs more complex input parameters and normally the post-process is implemented by users in host side.


The **'generic_inference'** is an example for showing how it work.

By default, it runs with a Tiny Yolo v3 model NEF and takes an BMP image as input and does post-process in host side.

Below shortly explains the key input parameters:

- **model file path** : NEF file path, it can be changed to user's own NEF.
- **image file path** : An image file path in BMP format. The actual input format for now supported is RGB565 or RGBA8888.
- **inference model ID** : The model ID of one model in the NEF. Each model should have a unique ID.
- **image format** : This indicates what image format preferred to be converted, the example converts BMP to RGB565 or RGBA888.
- **normalize mode** : Normalize mode depends how data is normalized when training the model.
- **post process** : In PLUS we provide a few post-processing functions, if choosing 'yolo_v3' it use an internal post-processing function for processing yolo_v3 and outputs bounding boxes. For other models, users can use 'none' to diretly get floating point values of each output node.

#### 3.2.1 Generic Inference with Post Process on Device

```bash
$ sudo ./kl520_demo_generic_inference_post_yolo
    connect device ... OK
    upload firmware ... OK
    upload model ... OK
    read image ... OK

    starting inference loop 100 times:
    .....................................................

    inference loop is done, starting post-processing ...

    doing tiny yolo v3 post-processing ...

    class count : 80
    box count : 6
    Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
    Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
    Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
    Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
    Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2
    Box 5 (x1, y1, x2, y2, score, class) = 1.0, 84.0, 50.0, 181.0, 0.229727, 2

    output bounding boxes on 'output_bike_cars_street_224x224.bmp'

```

From the console output, it can be observed that the information of models in the NEF is printed, including model ID, raw resolution, intput channel, raw image format and raw output size.

**Raw output** size indicates that a buffer of the size should be prepared to receive the output directly from the AI dongle, and it cannot be used until converting the raw output to well-structed floating point values.


If [post process] is set to 'yolo_v3', it draws detected objects in a new-created **output_one_bike_many_cars_224x224.bmp**.

![](../imgs/ex_kdp2_generic_inference_raw.bmp)


#### 3.2.2 Generic Inference without Post Process on Device

Otherwise if **post process** is set to 'none', the example dumps floating point values into **.txt** files for each output node.

```bash
$ sudo ./kl520_demo_generic_inference
    connect device ... OK
    upload firmware ... OK
    upload model ... OK
    read image ... OK

    starting inference loop 100 times:
    .....................................................

    inference loop is done

    number of output node : 2

    node 0:
    width: 7:
    height: 7:
    channel: 255:
    number of data (float): 12495:
    first 20 data:
        1.359, 0.340, 0.510, -0.510, 0.170, 0.340,
        -0.849, 0.849, 0.849, 0.510, 0.679,
        0.679, 0.679, 0.510, 0.000, 0.340,
        0.510, 0.510, 0.340, 0.000,

    node 1:
    width: 14:
    height: 14:
    channel: 255:
    number of data (float): 49980:
    first 20 data:
        0.874, -0.349, -0.175, 0.000, 0.000, -0.175,
        0.175, 0.349, -0.175, 0.175, -0.175,
        0.000, -0.175, -0.699, 1.398, 1.048,
        1.048, 0.874, 0.524, 0.699,

    dumped node 0 output to 'output_bike_cars_street_224x224_node0_7x7x255.txt'
    dumped node 1 output to 'output_bike_cars_street_224x224_node1_14x14x255.txt'

```
