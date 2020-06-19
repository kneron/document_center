# Kneron End to End Simulator

This project allows users to perform image inference using Kneron's built in simulator.

## Configuring Input

Kneron simulator uses a JSON file to specify parameters used throughout the testing process.

<div align="center">
<img src="../imgs/python_app/json.png">
</div>

The outermost key, "flow1", indicates one whole test flow: preprocess -> simulator -> postprocess. In the example, there is only one test for face detection, but you can test multiple flows sequentially by adding more outer "flow" keys. In each flow, there are three sections (pre_proc, emulator, post_proc) to define parameters necessary to complete the testing process.

If any of the required keys are missing, the program will end. If any other key is missing, the default value is used.
#### Preprocess Parameters
**Required keys:** rgba_img_path, raw_img_fmt, prp_func_name
While not "required", some parameters without values may cause errors during execution: npu_width, npu_height, bit_width, radix, img_in_width, and img_in_height.
 - is_bin_img: Specifies whether the test images are binary files (true) or image files (false).
    - Acceptable values: [true, false], default value: true
 - **raw_img_fmt**: Color format of the test images.
    - Acceptable values: ["NIR888", "RGB565", "RGB888"]
 - **rgba_img_path**: Name of the preprocessed RGBA binary file. This will be the input for the simulator.
 - preproc: Specifies whether preprocessing should be done.
    - Acceptable values: [true, false], default value: true
 - **prp_func_name**: Name of the preprocess function to run.
    - Acceptable values: ["app_flow_preproc_face_recognition", "app_flow_preproc_landmark", "app_flow_preproc_nir_liveness", "app_flow_preproc_primitive"] or any custom defined functions
 - out_img_fmt: Color format of the preprocessed image.
    - Acceptable values: ["BGR", "L", "RGB"], default value: "L"
 - npu_width: Width of the image for the model input.
    - Acceptable values: Non-negative integers, default value: 0
 - npu_height: Height of the image for the model input.
    - Acceptable values: Non-negative integers, default value: 0
 - bKeepRatio: Specifies whether to keep the aspect ratio of the original image after preprocess.
    - Acceptable values: [true, false], default value: true
 - norm_mode: Normalization mode.
    - Acceptable values: ["yolo", "kneron", "caffe", "tf", "torch"], default value: "kneron"
 - bit_width: Bit width of image pixels.
    - Acceptable values: Non-negative integers, default value: 0
 - radix: Radix for converting float values to int values. int((float)x * 2<sup>radix</sup>)
    - Acceptable values: Non-negative integers, default value: 0
 - img_in_width: Width of the original input image before preprocess.
    - Acceptable values: Non-negative integers, default value: 0
 - img_in_height: Height of the original input image before preprocess.
    - Acceptable values: Non-negative integers, default value: 0
 - pad_mode: Type of padding to be done. 1 indicates one side of padding (right or bottom) and 0 indicates both sides.
    - Acceptable values: [0, 1], default value: 0
 - rotate: Type of rotation to be done. 0 indicates no rotate, 1 indicates a clockwise rotation, and 2 indicates counter-clockwise rotation.
    - Acceptable values: [0, 1, 2], default value: 0
 - bCropFirstly: Specifies whether the image needs to be cropped. 0 indicates no crop and any other value indicates crop.
    - Acceptable values: Non-negative integers, default value: 0
 - crop_x: Upper left x coordinate of the original image to start the crop.
    - Acceptable values: Integers between 0 and img_in_width, default value: 0
 - crop_y: Upper left y coordinate of the original image to start the crop.
    - Acceptable values: Integers between 0 and img_in_height, default value: 0
 - crop_w: Width of crop.
    - Acceptable values: Non-negative integers, default value: 0
 - crop_h: Height of crop.
    - Acceptable values: Non-negative integers, default value: 0

#### Simulator Parameters
**Required keys if hardware csim is used:** setup_file, cmd_file, weight_file, dram_dump_file, emu_dump_file_prefix
**Required key if dynasty float is used:** onnx_file
**Required keys if dynasty fixed is used:** onnx_file, json_file
 - setup_file: Name of binary setup file used for Kneron hardware csim.
 - cmd_file: Name of binary command file used for Kneron hardware csim.
 - weight_file: Name of binary weight file used for Kneron hardware csim.
 - exec_emulator: Specifies whether simulation should be done.
	 - Acceptable values: [true, false], default value: true
 - dram_dump_file: Name of file to dump Kneron hardware csim results.
 - emu_dump_files_prefix: Name of prefix to distinguish dram_dump_file results.
 - run_float_dynasty: Specifies whether to run Kneron dynasty float point simulator.
	 - Acceptable values: [true, false], default value: false
 - run_fixed_dynasty: Specifies whether to run Kneron dynasty fixed point simulator. This value is ignored if run_float_dynasty is set to true.
	 - Acceptable values: [true, false], default value: false
 - "onnx_file": Name of onnx file to use for the Kneron dynasty simulator.
 - "json_file": Name of json file to use for the Kneron dynasty fixed point simulator.

#### Postprocess Parameters
**Required keys:** pop_func_name
 - postproc: Specifies whether postprocess should be done.
    - Acceptable values: [true, false], default value: true
 - **pop_func_name**: Name of the postprocess function to run.
	- Acceptable values: ["app_flow_postproc_face_recog", "app_flow_postproc_landmark", "app_flow_postproc_nir_liveness", "app_flow_postproc_nir_liveness_float", "app_flow_postproc_ssd_face_detect", "app_flow_postproc_ssd_face_detect_float"] or any custom defined functions
 - bFinal: Specifies whether this flow is the last one in the testing process.
	 - Acceptable values: [true, false], default value: true

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
3. Import the shared library into the [constants](python_flow/common/constants.py) module using the standard ctypes module:
    ```
    MY_LIB = ctypes.CDLL("./my_lib.so")
    ```
4. Define any C/C++ structures that are needed as classes in Python. Some examples can be found in the [classes](python_flow/common/classes.py) module. These classes must extend ```ctypes.Structure``` and must define the same variables, including type and name.
5. Define a wrapper to the C/C++ function you wish to call. Simply get the function name, define the argument and return types, and call the function. Here is an [example](examples/my_functions.py) of the Python implementation.
6. Add the wrapper function into the mappings in the files, PREPROCESS_MAPPING or POSTPROCESS_MAPPING.
7. Run the flow!

If there are any parameters necessary for your custom function, simply add another field in the respective section in the input JSON configuration. Additionally, before running the flow, you may need to modify the data returned from the Kneron simulator to fit the inputs for your custom postprocess function. (Link to other section here)