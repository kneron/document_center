# Kneron End to End Simulator

This project allows users to perform image inference using Kneron's built in simulator.

## Configuring Input

Kneron simulator uses a JSON file to specify parameters used throughout the testing process.
<div align="center">
<img src="../../imgs/python_app/json.png">
</div>
The outermost key, "flow1", indicates one whole test flow: preprocess -> simulator -> postprocess. In each flow, there are three sections (pre_proc, emulator, post_proc) to define parameters necessary to complete the testing process. The parameters shown are used in Kneron's testing flow; you may add new parameters to fit your custom preprocess or postprocess functions.

If any of the required keys are missing, the program will end. If any other key is missing, the default value is used. None of the following parameters in the appropriate section are required if you are using custom preprocess or postprocess functions.
#### Preprocess Parameters
**Required keys:** rgba_img_path, raw_img_fmt, prp_func_name

While not "required", some parameters without values may cause errors during execution: npu_width, npu_height, bit_width, radix, img_in_width, and img_in_height.

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| is_bin_img | Specifies whether input test images are binary files (true) or image files (false) | true | "true", "false" |
| **raw_img_fmt** | Color format of the input test images | X | "NIR888", "RGB565", "RGB888" |
| **rgba_img_path** | Name of the preprocessed RGBA binary file used as simulator input | X | any string |
| preproc | Specifies whether preprocessing should be done | true | "true", "false" |
| **prp_func_name** | Name of the preprocess function to run | X | "app_flow_preproc_face_recognition", "app_flow_preproc_landmark", "app_flow_preproc_nir_liveness", "app_flow_preproc_primitive", or any custom defined functions |
| out_img_fmt | Color format of the preprocessed image | "L" | "BGR", "L", "RGB" |
| npu_width | Width of the image for the model input | 0 | non-negative integers |
| npu_height | Height of the image for the model input | 0 | non-negative integers |
| bKeepRatio | Specifies whether to keep the aspect ratio of the original image after preprocess | true | "true", "false" |
| norm_mode | Normalization mode | "kneron" | "yolo", "kneron", "caffe", "tf", "torch" |
| bit_width | Bit width of image pixels | 0 | non-negative integers |
| radix | Radix for converting float values to int values, int((float)x * 2<sup>radix</sup>) | 0 | non-negative integers |
| img_in_width | Width of the original input image before preprocessing | 0 | non-negative integers |
| img_in_height | Height of the original input image before preprocessing | 0 | non-negative integers |
| pad_mode | Type of padding to be done, 1 indicates one side of padding (right or bottom) and 0 indicates both sides | 0 | 0, 1 |
| rotate | Type of rotation to be done, 0 indicates no rotate, 1 indicates a clockwise rotation, and 2 indicates counter-clockwise rotation | 0 | 0, 1, 2 |
| bCropFirstly | Specifies whether the image needs to be cropped, 0 indicates no crop and any other value indicates crop | 0 | non-negative integers |
| crop_x | Upper left x coordinate of the original image to start the crop | 0 | integers between 0 and img_in_width |
| crop_y | Upper left y coordinate of the original image to start the crop | 0 | integers between 0 and img_in_height |
| crop_w | Width of crop | 0 | non-negative integers |
| crop_y | Height of crop | 0 | non-negative integers |

#### Simulator Parameters
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
| run_fixed_dynasty | Specifies whether to run Kneron dynasty fixed point simulator, this value is ignored if run_float_dynasty is set to true | false | true, false |
| onnx_file | Name of ONNX file to use for the Kneron dynasty simulator | X | any string |
| json_file | Name of JSON file to use for the Kneron dynasty fixed point simulator | X | any string |

#### Postprocess Parameters
**Required keys:** pop_func_name

| Name | Description | Default Value | Acceptable Values |
|:----:|:-----------:|:-------------:|:-----------------:|
| postproc | Specifies whether postprocess should be done | true | true, false |
| **pop_func_name** | Name of the postprocess function to run | X | "app_flow_postproc_face_recog", "app_flow_postproc_landmark", "app_flow_postproc_nir_liveness", "app_flow_postproc_nir_liveness_float", "app_flow_postproc_ssd_face_detect", "app_flow_postproc_ssd_face_detect_float", or any custom defined functions |
| bFinal | Specifies whether this flow is the last one in the testing process | true | true, false |

## Adding custom preprocess or postprocess function
Since inference results can vary based on users' intentions, we provide support for integrating custom preprocess and postprocess functions.

### Python defined
If your functions are defined in Python, integration is simple.

1. Import the module containing your preprocess and postprocess functions to preprocess.py and postprocess.py, respectively.
2. Add the specific function to the mappings in the files, PREPROCESS_MAPPING or POSTPROCESS_MAPPING. The key should be the same as the func_name field that you specify in the input JSON configuration. The value will be the name of your custom function.
3. Run the flow!

### C defined
If your functions are defined in C or C++, integration is a bit trickier. To be able to run the code through Python, you first need to compile the C functions into a shared library for Python to import.

1. Compile the C/C++ functions into a shared library (.so). Be sure to add ```extern "C"``` to any C++ functions you intend to directly call in the Python flow. 
2. Copy the library into this project's python_flow directory.
3. Import the shared library into the constants module using the standard ctypes module:
    ```
    MY_LIB = ctypes.CDLL("./my_lib.so")
    ```
4. Define any C/C++ structures that are needed as classes in Python. Some examples can be found in the classes module. These classes must extend ```ctypes.Structure``` and must define the same variables, including type and name.
5. Define a wrapper to the C/C++ function you wish to call. Simply get the function name, define the argument and return types, and call the function.
6. Add the wrapper function into the mappings in the files, PREPROCESS_MAPPING or POSTPROCESS_MAPPING.
7. Run the flow!

If there are any parameters necessary for your custom function, simply add another field in the respective section in the input JSON configuration. Additionally, before running the flow, you may need to [modify the data](#simulator-output) returned from the Kneron simulator to fit the inputs for your custom postprocess function.

## Running a set of images
usage: python3 example.py [-h] [-d DIRECTORY] [-i {binary, image}] [-t {1, 2}] [-s {1, 2, 3}] [-w WORKERS]

Options:
 - -h: displays the help message
 - -d: specifies the directory of images to test
	 - The directory of images should be placed in the bin folder 
 - -i: specifies the type of image input to be tested
	 - The default image type is binary.
 - -t: specifies the type of test to run
	 - The specified types are Kneron tests. To create your own test, check example.py for guidance; the two tests are rgb_fdr and nir_liveness.
 - -s: specifies the number of stages to run through
 - -w: specifies the number of worker processes to utilize
	 - The default number of workers is one, or sequential processing.

To modify the argument parser, check the setup_parser function in example.py. To add a custom test, add it in the example.py module and the TEST_TYPES mapping.

## Simulator output
The results of the simulator vary depending on which one is invoked: hardware csim or dynasty. 
### Hardware csim
The hardware csim output is binary data for every output node in the ONNX model. The results are stored in the following format: [height][channel][width]. The data is also 16-byte aligned, and each data point is one byte. The byte data is in fixed point format, so you will first need to convert if you wish to use floating point values. To do this conversion, a specific radix and scale for each output node will need to be provided. These results are stored in a file called "image_name.bin_dram.bin".
### Dynasty
The Dynasty output is a list of float values for every output node in the given ONNX model. The results for each output are in channel last format. These results are stored in a file called "image_name_test_rgba.bin.onnx_out_num.txt". Be sure to verify that the "num" result file matches the output of the ONNX model you want by checking the number of lines in the file is equal to channel * row * column. After getting the values from the correct files, you can use them in your custom postprocess functions.

## Putting different flows together
To see an example of multiple tests together, here is the predefined rgb_fdr test, where it performs face detection, landmark detection, and face recognition together on one image.
<div align="center">
<img src="../../imgs/python_app/test_flow.png">
</div>
Simply specify the input JSON configuration file for the corresponding test being performed. You may also define any classes that allow for sharing of data between the testing flows. Then call the simulator for each flow and any other processing of data you may need to do. 
In the example, each of the JSON configurations defined has only one flow key, and the entire process uses three configuration files for face detection, landmark detection, and face recognition. However, you can test multiple flows sequentially by adding more outer "flow" keys to one single JSON.
<div align="center">
<img src="../../imgs/python_app/mult_flow_json.png">
</div>
