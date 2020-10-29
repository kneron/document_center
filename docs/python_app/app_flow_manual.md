


# Kneron End to End Simulator

This project allows users to perform image inference using Kneron's built in simulator. Some sections will be a little different depending on whether you are using the 520 or 720 version of the simulator: the version type will be denoted in the section subheader.

## File Structure

<div align="center">
<img src="../../imgs/python_app/file_structure.png">
<p>Example app folder structure</p>
</div>

* bin: all of the outputs that the application will dump
	* csim_dump: model inference results will be dumped here if you used CSIM
	* dynasty_dump: model inference results will be dumped here if you used Dynasty
	* out: will store postprocessing results of test images
* logs: log dumps when the application runs
* python_flow: all of the python code that makes up the application framework, this should not be modified
	* common: shared constants and classes
	* emulator/preprocess/postprocess: code for their parts of the test flow 
	* kneron_preprocessing: kneron hardware PPP

<div align="center">
<img src="../../imgs/python_app/user_app_example.png">
<p>Example app folder structure</p>
</div>

* app: where you should place your application and test images
	* application: should hold input jsons, model files, and preprocess/postprocess files
		* flow.py: filled out by the user to create testing flows for their application
		* mappings.py: filled out by the user to set the flow control for postprocess/preprocess functions and tests to run

## Configuring Input

Kneron simulator uses a JSON file to specify parameters used throughout the testing process.
<div align="center">
<img src="../../imgs/python_app/json.png">
<p>Example input JSON configurations</p>
</div>
The outermost key, "flow1", indicates one stage in the test flow: preprocess -> simulator -> postprocess. In each flow, there are three sections (pre, emu, post) to define parameters necessary to complete the testing process. The parameters shown are used in Kneron's testing flow; you may add new parameters to fit your custom preprocess or postprocess functions.


If any of the required keys are missing, the program will end. If you need to add your own parameters, simply add another field into the input JSON file. The required keys for preprocess are img_in_width, img_in_height, npu_width, npu_heighth, raw_img_fmt, and rgba_img_path. The required keys for emulator are dependent on which version inference you would like to run; this will be explained in more detail in the emulator section.
#### Preprocess Parameters
**Required keys:** npu_width, npu_height, raw_img_fmt, rgba_img_path

| Name              | Description                                                                                  | Acceptable Values                    |
|:-----------------:|:--------------------------------------------------------------------------------------------:|:------------------------------------:|
| api_mode          | Specified whether fixed or floating mode should be used. (kneron_preprocessing library only. | "fixed", "float"                     |
| bit_width         | Bit width of image pixels                                                                    | non-negative integers                |
| crop_x            | Upper left x coordinate of the original image to start the crop                              | integers between 0 and img_in_width  |
| crop_y            | Upper left y coordinate of the original image to start the crop                              | integers between 0 and img_in_height |
| crop_w            | Width of crop                                                                                | non-negative integers                |
| crop_h            | Height of crop                                                                               | non-negative integers                |
| img_in_width      | Width of the original input image before preprocessing                                       | non-negative integers                |
| img_in_height     | Height of the original input image before preprocessing                                      | non-negative integers                |
| keep_aspect_ratio | Specifies whether to keep the aspect ratio of the original image after preprocess            | true, false                          |
| norm_mode         | Normalization mode                                                                           | "yolo", "kneron", "caffe", "tf", "torch" [^1] |
| **npu_width**     | Width of the image for the model input                                                       | non-negative integers                |
| **npu_height**    | Height of the image for the model input                                                      | non-negative integers                |
| out_img_fmt       | Color format of the preprocessed image                                                       | "BGR", "L", "RGB"                    |
| pad_mode          | Type of padding to be done                                                                   | 0, 1 [^2]                            |
| pre_bypass        | Specifies whether preprocessing should be bypassed                                           | true, false                          |
| pre_type          | Name of the preprocess function to run                                                       | any key in the PRE dictionary in mapping.py ([more info](#adding-own-flows)) |
| radix             | Radix for converting float values to int values, int((float)x * 2<sup>radix</sup>)           | non-negative integers                |
| **raw_img_fmt**   | Color format of the input test images                                                        | "NIR888", "RGB565", "RGB888"         |
| **rgba_img_path** | Name of the preprocessed RGBA binary file used as simulator input                            | any string                           |
| rotate            | Type of rotation to be done                                                                  | 0, 1, 2 [^3]                         |
| to_crop           | Specifies whether the image needs to be cropped                                              | non-negative integers [^4]           |


#### Simulator Parameters for 520
Hardware CSIM will be used if both the "run_float" and "run_fixed" parameters are set to false.

**Required keys if hardware CSIM is used:** setup_file, command_file, weight_file

**Required key if Dynasty float is used:** onnx_file, onnx_input

**Required keys if Dynasty fixed is used:** onnx_file, json_file, onnx_input

| Name           | Description                                                                                                | Acceptable Values |
|:--------------:|:----------------------------------------------------------------------------------------------------------:|:-----------------:|
| emu_bypass     | Specifies whether simulator should be bypassed                                                             | true, false       |
| model_type     | Used to create output directory for less confusion                                                         | any string        |
| setup_file     | Name of the binary setup file used for Kneron hardware CSIM                                                | any string        |
| command_file   | Name of the binary command file used for Kneron hardware CSIM                                              | any string        |
| weight_file    | Name of the binary weight file used for Kneron hardware CSIM                                               | any string        |
| csim_output    | Name of folder to dump CSIM output                                                                         | any string        |
| run_float      | Specifies whether to run Kneron Dynasty float point simulator                                              | true, false       |
| run_fixed      | Specifies whether to run Kneron Dynasty fixed point simulator. Ignored if run_float_dynasty is set to true | true, false       |
| onnx_file      | Name of ONNX or BIE file to use for the Kneron Dynasty simulator.                                          | any string        |
| json_file      | Name of JSON file to use for the Kneron Dynasty fixed point simulator                                      | any string        |
| onnx_input     | Name of the input node to the ONNX model                                                                   | any string        |
| dynasty_output | Name of folder to dump Dynasty output                                                                      | any string        |

#### Simulator Parameters for 720
**Required keys if hardware CSIM is used:** ini_file, setup_file, cmd_file, weight_file, csv_file

**Required key if Dynasty float is used:** onnx_file, onnx_input

**Required keys if Dynasty fixed is used:** onnx_file, json_file, onnx_input

| Name           | Description                                                                                                | Acceptable Values |
|:--------------:|:----------------------------------------------------------------------------------------------------------:|:-----------------:|
| emu_bypass     | Specifies whether simulator should be bypassed                                                             | true, false       |
| model_output   | Used to create output directory for less confusion                                                         | any string        |
| ini_file       | Name of input configuration file for hardware CSIM                                                         | any string        |
| setup_file     | Name of the binary setup file used for Kneron hardware CSIM                                                | any string        |
| cmd_file       | Name of the binary command file used for Kneron hardware CSIM                                              | any string        |
| weight_file    | Name of binary weight file used for Kneron hardware CSIM                                                   | any string        |
| csv_file       | Name of the csv file that holds input model dimension                                                      | any string        |
| run_float      | Specifies whether to run Kneron Dynasty float point simulator                                              | true, false       |
| run_fixed      | Specifies whether to run Kneron Dynasty fixed point simulator. Ignored if run_float_dynasty is set to true | true, false       |
| onnx_file      | Name of ONNX file to use for the Kneron Dynasty simulator                                                  | any string        |
| json_file      | Name of JSON file to use for the Kneron Dynasty fixed point simulator                                      | any string        |
| onnx_input     | Name of the input node to the ONNX model                                                                   | any string        |
| dynasty_output | Name of the folder to dump Dynasty output                                                                  | any string        |

#### Postprocess Parameters
**Required keys:** post_type

| Name          | Description                                                       | Acceptable Values           |
|:-------------:|:-----------------------------------------------------------------:|:---------------------------:|
| anchors | Name of numpy file for fd postprocessing anchors (only Python version). | any string ending in '.npy' |
| post_bypass   | Specifies whether postprocess should be bypassed                  | true, false                 |
| **post_type** | Name of the postprocess function to run                           | any key in the POST dictionary in mapping.py ([more info](#adding-own-flows))) |

## Adding custom preprocess or postprocess function
Since inference results can vary based on users' intentions, we provide support for integrating custom preprocess and postprocess functions.

### Preprocess
#### Python defined (520)
If your preprocess functions are defined in Python, integration is simple.

1. Make sure your python function takes two parameters as input: an InputConfig class and an output data class. The InputConfig class holds the configurations parsed from the input JSON. The output data class will be defined by you and holds the postprocessing results. For reference, the InputConfig class is in python_flow/common/config.py.
2. Make sure the preprocessed output is dumped into the path specified by "rgba_img_path" in the input JSON.
3. Copy your python module into your application's directory under "app/".
4. In mapping.py, import your python module.
5. Add a key, value pair with your custom function as the value to the mapping called PRE in mapping.py. The key you add here should be the value that goes in the "pre_type" field in the input JSON.
6. Run the flow!

#### C defined
1. Compile the C/C++ functions into a shared library (.so). Be sure to add ```extern "C"``` to any C++ functions you intend to directly call in the Python flow. An example of how to do this is in the example folder.
2. Copy the library into your application's directory under "app/".
3. Import the shared library into whichever module needs it using the standard ctypes module:
    ```
    MY_LIB = ctypes.CDLL("./my_lib.so")
    ```
4. Define any C/C++ structures that are needed for parameters as classes in Python. These classes must extend ```ctypes.Structure``` and store the structure fields in the "_fields_" variable. This is a list of tuples where the first item is the name of the variable, and the second item is the type of that variable. The names  and order must be defined exactly as in the C code.
5. Define a wrapper to the C/C++ function you wish to call. You need to specify three items: the function name as defined in the C code, the input argument types, and the result argument types.
6. Create a Python function that takes an InputConfig class and output data class as input that calls your function wrapper. You can get the inputs you need from the Input Config class and pass it to the wrapper as needed.
7. Add the function from step 6 into PRE similar to as in the Python case. 
8. Run the flow!

### Postprocess
#### Python defined (520)
If your postprocess functions are defined in Python, integration is simple yet again.

1. Make sure your python function takes the same two parameters as the preprocesses function.
2. You will need to get the data from the output inference. To get the output data, you should call either csim_to_np or dynasty_to_np, depending on whether you are using CSIM or Dynasty inference. This will place all of the output data into a list of numpy arrays. This function can be referenced at python_flow/postprocess/convert.py, and example usage can be found in app/app1/postprocess/fd.py. Use this data in your postprocess function.
3. Copy your python module into your application's directory under "app/".
4. In mapping.py, import your python module.
5. Add a key, value pair with your custom function as the value to the mapping called POST in mapping.py. The key you add here should be the value that goes in the "post_type" field in the input JSON.
6. Run the flow!

#### Python defined (720)
1. Make sure your python function takes the same two parameters as the preprocesses function.
2. You will need to get the data from the output inference. Currently, only Dynasty works with python postprocessing. To get the output data, you should call dynasty_output_to_np in python_flow/postprocess/convert.py. This will place all of the output data into a list of numpy arrays. Inputs to this function are the folder to ONNX results, the names of the output nodes, a flag of whether Dynasty float was used, and an input JSON file if Dynasty fixed was used. These are all found in the InputConfig class, and a reference example can be found in app/app1/postprocess/fd.py in the postprocess_py function.
3. Copy your python module into your application's directory under "app/".
4. In mapping.py, import your python module.
5. Add a key, value pair with your custom function as the value to the mapping called POST in mapping.py. The key you add here should be the value that goes in the "post_type" field in the input JSON.
6. Run the flow!

#### C defined (520)
1. Like the preprocess, compile the C/C++ functions into a shared library (.so).
2. However, your postprocess C function should take in an kdp_image structure, as this holds data parsed from the model binaries. For reference, the Python class is defined in python_flow/common/kdp_image.py, and the C structure is defined in app/app1/postprocess_c/post_proc_interface.h.
3. Copy the library into your application's directory under "app/".
4. Import the shared library into whichever module needs it using the standard ctypes module.
5. Define any C/C++ structures and function wrappers that are needed as in the preprocess.
6. Create a Python function that takes an InputConfig class and output data class as input that calls your function wrapper. To load the output data into memory, call either csim_to_memory or dynasty_to_memory. Information to how the data is loaded into memory can be found in python_flow/postprocess/convert.py. Example usage can be found in app/app1/postprocess/fd.py under the postprocess_py function.
7. Add a key, value pair with your custom function as the value to the mapping called POST in mapping.py.
8. Run the flow!

#### C defined (720)
1. Like the preprocess, compile the C/C++ functions into a shared library (.so).
2. However, your postprocess function should take in an KDPImage structure, as this holds data parsed from the model binaries. The Python class is defined in python_flow/common/kdp_image.py (this is different than the one in 520), and the C structure is defined in app/app1/postprocess_c/kdpio.h.
3. Copy the library into your application's directory under "app/".
4. Import the shared library into whichever module needs it using the standard ctypes module.
5. Define any C/C++ structures and function wrappers that are needed as in the preprocess. 
6. Currently, only CSIM works with C postprocessing. To load the output data into memory, call the load_csim_data function under python_flow/postprocess/convert.py. Example usage can be found in app/app1/postprocess/fd.py under the postprocess function.
7. Accessing the data is a bit tricky, but examples can be found in app/app1/postprocess/post_processing_main.c in the load_data function. Get the output node x you want by accessing the pNodePositions array for node x + 1 (the first node will be an input node). The memory location for the node data can be accessed by calling the macro OUT_NODE_ADDR(node).
7. Add a key, value pair with your custom function as the value to the mapping called POST in mapping.py.
9. Run the flow!

If there are any parameters necessary for your custom function, simply add another field in the respective section in the input JSON configuration. Additionally, before running the flow, you may need to [modify the data](#simulator-output) returned from the Kneron simulator to fit the inputs for your custom postprocess function.

## Usage

```
simulator.py [-h] [-i {binary,image}] [-t TEST] [-s {1,2,3}]
                  [-w WORKERS] [-f {RGB,NIR,INF,ALL}] [-n NUM_IMAGES]
                  [-b BOX]
                  app_folder directory

Runs a test on multiple images

positional arguments:
  app_folder            directory of your application, should be in the app folder)
  directory             directory of images to test, images should be in the
                        app folder ('app')

optional arguments:
  -h, --help            show this help message and exit
  -i {binary,image}, --inputs {binary,image}
                        type of inputs to be tested
  -t TEST, --test TEST  type of test to be run
  -s {1,2,3}, --stages {1,2,3}
                        number of stages of the test to run through
  -w WORKERS, --workers WORKERS
                        number of worker processes to run
  -f {RGB,NIR,INF,ALL}, --fmt {RGB,NIR,INF,ALL}
                        format of the input images to test
  -n NUM_IMAGES, --num_images NUM_IMAGES
                        number of images to test
  -b BOX, --box BOX     flag to save bounding box results
```

* -t: default will be one of the keys in your application's mapping.py
	* The parameter here should be one of the keys in your application's mapping.py, with the exact same spelling
* -s: default number is all of the stages
* -w: default number is 1
* -f: default is "ALL", other format specifiers will filter the test images to only images with that prefix
* -n: default is all of the images in the test directory
* -b: default is false
	* If you use binary input, you will need a jpg file with the same name in your input directory for this to work
	* The results will be saved in bin/out/path_to_your_input_image

You will need the following to run a test.
* a set of test images placed in the app folder
* a test model placed in your application folder under app
	* ONNX and JSON if you are running Dynasty
	* weight, setup, and command binaries if you are running CSIM
* to modify the input JSON to fit the input data
* setup flow.py and mapping.py in your application folder under app so the flow control knows what to run

We have provided an example application at app/app1. There are the postprocess and preprocess functions, models, and example mapping.py and flow.py files. To run this example, be in the root directory and run this command, with test_image_folder as your folder of test images:
```
python3 simulator.py app/app1 app/test_image_folder
```

## Simulator output
The results of the simulator vary depending on which one is invoked: hardware CSIM or Dynasty. 
### 520 Hardware CSIM
The 520 hardware CSIM output is floating point values for every output node in the given ONNX model. They are stored in the output folder specified in the input JSON in files called "node_000x_output.txt." The results are stored in (channel, height, width) format.
### 720 Hardware CSIM
The 720 hardware CSIM output is a hex dump for every output node in the ONNX model. The dump is called "dram_output.hex". For each output node, there will be one line specifying the address that the data can be found in DRAM. Following that line, there will be lines of up to 16 bytes that contain the results from the CSIM.
### Dynasty
The Dynasty output is a list of float or int values for every output node in the given ONNX model, depending on whether floating point or fixed point inference was used. The results are stored in the output folder specified in the input JSON in a file called "layer_output_outputname_fl.txt" (or fx.txt for fixed point). The fixed point inferencer produces floating point results in addition to the fixed point results. The results are stored in (channel, height, width) format.

## Adding own flows

### (520)
To add your own test flow, add a file called "flow.py" into your current application folder. 
<div align="center">
<img src="../../imgs/python_app/adding_tests.png">
<p>Example test flow</p>
</div>

1. You will need to first import "flow.py" from the python_flow directory, and your output class definition that inherits the OutputData class from python_flow/common/output_data.py.
2. Define a test function that takes in as input an image file (pathlib.Path object) and a Namespace object parsed from the command line.
    1. Instantiate your output class. This class will be passed between each stage of your test flow, so you can pass data between each stage.
    2. Call run_simulator once for each stage in your flow. The inputs will be a string path to the input JSON file, the input image file, your output class object, and the Namespace object. The input image and Namespace object will be passed in from your function's parameters without modification. You can look for more information in the python_flow/flow.py file.
    3. Add any extra work you may need for your testing.
4. Add any preprocess/postprocess functions you intend to call in their respective PRE/POST dictionaries in "mapping.py." The keys in these dictionaries will be the values you enter into the "pre_type"/"post_type" fields in your input JSON file.
3. Add this function call to the TESTS dictionary in "mapping.py" in your current application folder. The key in this dictionary will be the command line argument for the "-t" option.

<div align="center">
<img src="../../imgs/python_app/mapping.png">
<p>Example mapping</p>
</div>

---
[^1]: yolo: data / 255,
	kneron: data / 256 - 0.5,
	caffe: mean = [103.939, 116.779, 123.68], data - mean (per channel),
	tf: data / 127.5 - 1,
	torch: mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225], (data / 255 - mean) / std (per channel)

[^2]: 1 indicates one side of padding (right or bottom), 0 indicates both sides

[^3]: 0 indicates no rotate, 1 indicates a clockwise rotation, and 2 indicates counter-clockwise rotation

[^4]: 0 indicates no crop, any other value indicates crop
