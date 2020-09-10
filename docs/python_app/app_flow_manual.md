# Kneron End to End Simulator

This project allows users to perform image inference using Kneron's built in simulator. Most sections will have a 520 version and a 720 version, as the requirements for those are a bit different.

## File Structure

* bin folder: all of the inputs and outputs that the application will use and dump, also used as the working directory
	* app: binaries and other required files for the simulator to run, DO NOT MODIFY
	* fdr: example model
		* binaries, CSV, and INI files used as input for CSIM
		* ONNX and JSON used for dynasty float and fixed inference
	* input_jsons: example input JSONs for the application
	* out: will store postprocessing results of test images
	* test: default reference test image
* example: example of how to connect C code with ctypes using a shared library
* python_flow: all of the python code that makes up the application
	* common: shared constants and classes
	* emulator/preprocess/postprocess: code for their parts of the test flow 
	* kneron_preprocessing: kneron hardware PPP
	* logs: holds log dumps when application runs
* src: holds our preprocessing/postprocessing C libraries

## Configuring Input

Kneron simulator uses a JSON file to specify parameters used throughout the testing process.
<div align="center">
<img src="../../imgs/python_app/json.png">
</div>
The outermost key, "flow1", indicates one whole test flow: preprocess -> simulator -> postprocess. In each flow, there are three sections (pre_proc, emulator, post_proc) to define parameters necessary to complete the testing process. The parameters shown are used in Kneron's testing flow; you may add new parameters to fit your custom preprocess or postprocess functions.

If any of the required keys are missing, the program will end. If any other key is missing, the default value is used. None of the following parameters in the appropriate section are required if you are using custom preprocess or postprocess functions.
#### Preprocess Parameters
**Required keys:** rgba_img_path, raw_img_fmt

While not "required", some parameters without values may cause errors during execution: npu_width, npu_height, bit_width, radix, img_in_width, and img_in_height.

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| api_mode | Specified whether fixed or floating mode should be used. Only used for the kneron_preprocessing library in the default preprocessing method. | "fixed" | "fixed", "float" |
| bit_width | Bit width of image pixels | 0 | non-negative integers |
| img_in_width | Width of the original input image before preprocessing | 0 | non-negative integers |
| img_in_height | Height of the original input image before preprocessing | 0 | non-negative integers |
| keep_aspect_ratio | Specifies whether to keep the aspect ratio of the original image after preprocess | true | true, false |
| norm_mode | Normalization mode | "kneron" | "yolo", "kneron", "caffe", "tf", "torch" |
| npu_width | Width of the image for the model input | 0 | non-negative integers |
| npu_height | Height of the image for the model input | 0 | non-negative integers |
| out_img_fmt | Color format of the preprocessed image | "L" | "BGR", "L", "RGB" |
| pad_mode | Type of padding to be done, 1 indicates one side of padding (right or bottom) and 0 indicates both sides | 1 | 0, 1 |
| pre_bypass | Specifies whether preprocessing should be bypassed | false | true, false |
| pre_type | Name of the preprocess function to run | "default" | "face_recognition", "landmark", "nir_liveness", "primitive", "default", or any custom defined functions |
| radix | Radix for converting float values to int values, int((float)x * 2<sup>radix</sup>) | 0 | non-negative integers |
| **raw_img_fmt** | Color format of the input test images | X | "NIR888", "RGB565", "RGB888" |
| **rgba_img_path** | Name of the preprocessed RGBA binary file used as simulator input | X | any string |
| rotate | Type of rotation to be done, 0 indicates no rotate, 1 indicates a clockwise rotation, and 2 indicates counter-clockwise rotation | 0 | 0, 1, 2 |
| to_crop | Specifies whether the image needs to be cropped, 0 indicates no crop and any other value indicates crop | 0 | non-negative integers |
| crop_x | Upper left x coordinate of the original image to start the crop | 0 | integers between 0 and img_in_width |
| crop_y | Upper left y coordinate of the original image to start the crop | 0 | integers between 0 and img_in_height |
| crop_w | Width of crop | 0 | non-negative integers |
| crop_y | Height of crop | 0 | non-negative integers |

#### Simulator Parameters for 520
**Required keys if hardware csim is used:** setup_file, cmd_file, weight_file, dram_dump_file, emu_dump_file_prefix

**Required key if dynasty float is used:** onnx_file

**Required keys if dynasty fixed is used:** onnx_file, json_file

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| setup_file | Name of the binary setup file used for Kneron hardware csim | X | any string |
| cmd_file | Name of the binary command file used for Kneron hardware csim | X | any string |
| weight_file | Name of binary weight file used for Kneron hardware csim | X | any string |
| exec_emulator | Specifies whether simulation should be done | true | true, false |
| dram_dump_file | Name of file to dump Kneron hardware csim results | X | any string |
| emu_dump_files_prefix | Name of prefix to distinguish dram_dump_file results | X | any string |
| run_float_dynasty | Specifies whether to run Kneron dynasty float point simulator | false | true, false |
| run_fixed_dynasty | Specifies whether to run Kneron dynasty fixed point simulator. This value is ignored if run_float_dynasty is set to true | false | true, false |
| onnx_file | Name of ONNX file to use for the Kneron dynasty simulator | X | any string |
| json_file | Name of JSON file to use for the Kneron dynasty fixed point simulator | X | any string |

#### Simulator Parameters for 720
**Required keys if hardware csim is used:** ini_file, setup_file, cmd_file, weight_file, csv_file

**Required key if dynasty float is used:** onnx_file, onnx_input, onnx_output_nodes

**Required keys if dynasty fixed is used:** onnx_file, json_file, onnx_input, onnx_output_nodes

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| emu_bypass | Specifies whether inference should be bypassed | false | true, false |
| ini_file | Name of input configuration file for hardware CSIM | X | any string |
| setup_file | Name of the binary setup file used for Kneron hardware csim. This path should be relative to the "ini_file" | X | any string |
| cmd_file | Name of the binary command file used for Kneron hardware csim. This path should be relative to the "ini_file" | X | any string |
| weight_file | Name of binary weight file used for Kneron hardware csim. This path should be relative to the "ini_file" | X | any string |
| csv_file | Name of the csv file that holds input model dimensions. This path should be relative to the "ini_file" | X | any string |
| run_float_dynasty | Specifies whether to run Kneron dynasty float point simulator | false | true, false |
| run_fixed_dynasty | Specifies whether to run Kneron dynasty fixed point simulator. This value is ignored if run_float_dynasty is set to true | false | true, false |
| onnx_file | Name of ONNX file to use for the Kneron dynasty simulator | X | any string |
| json_file | Name of JSON file to use for the Kneron dynasty fixed point simulator | X | any string |
| onnx_input | Name of the input node in the ONNX file | X | any string |
| onnx_output | Name of the folder to store inference results | test_file_name + "_output" | any string |

#### Postprocess Parameters
**Required keys:** post_type

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| anchors | Name of numpy file used as anchors for face detection postprocessing. Only needed when Python version of postprocessing is used | X | any string ending in '.npy' |
| post_bypass | Specifies whether postprocess should be bypassed | false | true, false |
| **post_type** | Name of the postprocess function to run | X | "face_recognition", "landmark", "nir_liveness", "ssd_face_detection", "ssd_face_detection_py" or any custom defined functions |

## Adding custom preprocess or postprocess function
Since inference results can vary based on users' intentions, we provide support for integrating custom preprocess and postprocess functions.

### Preprocess
#### Python defined
If your preprocess functions are defined in Python, integration is simple.

1. Make sure your python function takes two parameters as input: an InputConfig class and an output data class. The InputConfig class holds the configurations parsed from the input JSON and the output data class holds the postprocessing results. More details about these classes can be found in the common directory.
2. Make sure the preprocessed output is dumped into the path specified by "rgba_img_path" in the input JSON.
3. Copy your python module into the preprocess subdirectory.
4. In preprocess.py, import your python module.
5. Add a key, value pair with your custom function as the value to the mapping called PREPROCESS_MAPPING in preprocess.py. The key you add here should be the value that goes in the "pre_type" field in the input JSON.
6. Run the flow!

#### C defined
If your functions are defined in C or C++, integration is a bit trickier. To be able to run the code through Python, you first need to compile the C functions into a shared library for Python to import.

1. Compile the C/C++ functions into a shared library (.so). Be sure to add ```extern "C"``` to any C++ functions you intend to directly call in the Python flow. An example of how to do this is in the example folder.
2. Copy the library into this project's python_flow directory.
3. Import the shared library into the constants module using the standard ctypes module:
    ```
    MY_LIB = ctypes.CDLL("./my_lib.so")
    ```
4. Define any C/C++ structures that are needed for parameters as classes in Python. Some examples can be found in classes.py. These classes must extend ```ctypes.Structure``` and store the structure fields in the "_fields_" variable. This is a list of tuples where the first item is the name of the variable, and the second item is the type of that variable. The names  and order must be defined exactly as in the C code.
5. Define a wrapper to the C/C++ function you wish to call. You need to specify three items: the function name as defined in the C code, the input argument types, and the result argument types.
6. Create a function in preprocess.py that takes an InputConfig class and output data class as input that uses your wrapper. You can get the inputs you need from the Input Config class and pass it to the wrapper as needed.
7. Add the function from step 6 into PREPROCESS_MAPPING similar to the Python case. 
8. Run the flow!

### Postprocess
#### Python defined
If your postprocess functions are defined in Python, integration is simple yet again.

1. Make sure your python function takes the same two parameters as the preprocesses function
2. You will need to get the data from the output inference. Currently, only dynasty works with python postprocessing. To get the output data, you should call dynasty_output_to_np in postprocess/wrappers.py. This will place all of the output data into a list of numpy arrays. Inputs to this function are the folder to ONNX results, the names of the output nodes, a flag of whether dynasty float was used, and an input JSON file if dynasty fixed was used. These are all found in the InputConfig class, and a reference example can be found in postprocess/fd.py in the fd_py function.
3. Copy your python module into the postprocess subdirectory.
4. In preprocess.py, import your python module.
5. Add a key, value pair with your custom function as the value to the mapping called POSTPROCESS_MAPPING in postprocess.py. The key you add here should be the value that goes in the "post_type" field in the input JSON.
6. Run the flow!

#### C defined
1. Like the preprocess, compile the C/C++ functions into a shared library (.so).
2. However, your postprocess function should take in an KDPImage structure, as this holds data parsed from the model binaries. The Python class is defined in common/classes.py, and the C structure is defined in src/postprocess/kdpio.h. You may add to this structure however you wish, but make sure that you make changes in both kdpio.h and classes.py.
3. Copy the library into this project's python_flow directory.
4. Import the shared library into the constants module using the standard ctypes module:
    ```
    MY_LIB = ctypes.CDLL("./my_lib.so")
    ```
5. Define any C/C++ structures and function wrappers that are needed as in the preprocess. 
6. Currently, only CSIM works with C postprocessing. To load the output data into memory, call the load_csim_data function under postprocess/wrappers.py. The inputs should be the setup binary file of the model and a KDPImage class. Example usage can be found in postprocess/fd.py under the fd_csim function.
7. Accessing the data is a bit tricky, but examples can be found in src/postprocess/post_processing_main.c in the load_data function. Get the output node x you want by accessing the pNodePositions array for node x + 1 (the first node will be an input node). The memory location for the node data can be accessed by calling the macro OUT_NODE_ADDR(node).
8. Add a key, value pair with your custom function as the value to the mapping called POSTPROCESS_MAPPING in postprocess.py.
9. Run the flow!

If there are any parameters necessary for your custom function, simply add another field in the respective section in the input JSON configuration. Additionally, before running the flow, you may need to [modify the data](#simulator-output) returned from the Kneron simulator to fit the inputs for your custom postprocess function.

## Running a set of images
usage: python3 example.py [-h] [-d DIRECTORY] [-i {binary,image}] [-t {1,2}]
                  [-s {1,2,3}] [-w WORKERS] [-p PRINT] [-f {RGB,NIR,INF}]
                  [-n NUM_IMAGES] [-b BOX]


Options:
 * -h: displays the help message
 * -d: specifies the directory of images to test
	 * The directory of images should be placed in the bin folder.
 * -i: specifies the type of image input to be tested
	 * The default image type is image (jpg, png, etc.)
 * -t: specifies the type of test to run
	 * The specified types are Kneron tests. To create your own test, check [here](#Adding-own-flows) for guidance.
 * -s: specifies the number of stages to run through
	 * The default number of stages is all of them
 * -w: specifies the number of worker processes to utilize
	 * The default number of workers is one.
 * -p: specifies whether or not to print certain results out
	 * The default is false.
 * -f: specifies format of input images
	 * The default is "RGB."
	 * Currently, this causes only images with the prefix of the specified format to be used as test inputs.
 * -n: specifies number of input images to test
	 * The default is all of the images in the specified test directory.
 * -b: specifies whether or not to display the bounding box results
	 * The default is false.

To modify the argument parser, check the setup_parser function in example.py. 
You will need:
* a set of test images
* a test model:
	* ONNX and JSON if you are running dynasty
	* weight, setup, and command binaries if you are running CSIM
* to modify the input JSON to fit the input data:
* all of these should be placed in the bin folder

## Simulator output
The results of the simulator vary depending on which one is invoked: hardware csim or dynasty. 
### 520 Hardware CSIM
The 520 hardware CSIM output is binary data for every output node in the ONNX model. The results are stored in the following format: [height][channel][width]. The data is also 16-byte aligned, and each data point is one byte. The byte data is in fixed point format, so you will first need to convert if you wish to use floating point values. To do this conversion, a specific radix and scale for each output node will need to be provided. These results are stored in a file called "image_name.bin_dram.bin".
### 520 Dynasty
The 520 Dynasty output is a list of float values for every output node in the given ONNX model. The results for each output are in channel last format. These results are stored in a file called "image_name_test_rgba.bin.onnx_out_num.txt". Be sure to verify that the "num" result file matches the output of the ONNX model you want by checking the number of lines in the file is equal to channel * row * column. After getting the values from the correct files, you can use them in your custom postprocess functions.
### 720 Hardware CSIM
The 720 hardware CSIM output is a hex dump for every output node in the ONNX model. The dump is called "dram_output.hex". For each output node, there will be one line specifying the address that the data can be found in DRAM. Following that line, there will be lines of up to 16 bytes that contain the results from the CSIM.
### 720 Dynasty
The 720 Dynasty output is a list of float or int values for every output node in the given ONNX model, depending on whether floating point or fixed point inference was used. The results are stored in the output folder specified in the input JSON in a file called "layer_output_outputname_fl.txt" (or fx.txt for fixed point). The results are stored in channel first format.

## Adding own flows
To add your own flow, go to app_flow.py. An example flow can be seen in the fdr function. 
<div align="center">
<img src="../../imgs/python_app/adding_flow.png">
</div>
For one stage in the flow, the main function that needs to be called is the run_simulator function. The inputs are input JSON configuration file, a class that holds the output data, the input test file, and the command line options. The input test file and command line options are passed as input from another function and should be accessed through the parameters of your test flow. The JSON configuration file can be set before running the simulator, and the output data class can be instantiated right at the beginning of the test flow. After getting those values, calling run_simulator will run the test. You can also add multiple stages that depend on each other, using the output data class to share data between the stages.
Afterwards, go to example.py and add your new test to the TEST_TYPES mapping. Your flow can now be called through the application using the command line option, -t, with the key that you define.
The key difference between 520 and 720 here is that the output data class in 520 is called ProcessingOutput, and the output data class in 720 is called OutputData.
