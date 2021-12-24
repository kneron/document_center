# Command Line Script Tools

## 0. Introduction

Since toolchain version v0.14.0, we introduce Python API and recommend using it for the general work flow. But this doesn't mean that the old approad of script utilities are abandoned. This document provides the usage of all the script utilities.

### 1. IP Evaluator

The tool described in this section is mainly used to check your model's performance estimation and whether your model is supported by the toolchain. It can be used with both `.bie` and `.onnx` file. (The `.bie` file is the result of FP analyser which described in the next section.)

#### 1.1 Running the programs

To run the compile and the ip evaluator, you need to have an `.onnx` or a `.bie` file as the input. Here we take the
`LittleNet` as the example which is already inside the docker:

```bash
# For KDP520
cd /workspace/scripts && ./compilerIpevaluator_520.sh /workspace/examples/LittleNet/LittleNet.onnx

# For KDP720
cd /workspace/scripts && ./compilerIpevaluator_720.sh /workspace/examples/LittleNet/LittleNet.onnx
```

This part uses the default configuration for the hardware and not available for fine-tuning.

#### 1.2 Get the result

A folder called `compiler` will be generated in `/data1`, which stores the result of the compiler and IP Evaluator. If you are using this script with an `onnx` file, please ignore the binary files since they are not quantized and unable to be used.

We can find the following files after running the script above:

* `/data1/compiler/command.bin`: the compiled binary for the hardware.
* `/data1/compiler/setup.bin`: the compiled binary for the hardware.
* `/data1/compiler/weight.bin`: the compiled binary for the hardware.
* `/data1/compiler/ioinfo.csv`: the hardware IO mapping information of the model.
* `/data1/compiler/ip_eval_prof.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 520 version script generate this file.)*
* `/data1/compiler/ProfileResult.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 720 version script generate this file.)*


### 2 FpAnalyser, Compiler and IpEvaluator

In this section and the following sections, we'll use the `LittleNet` as an example. You can find the folder under
`/workspace/examples`. To use it, copy it under `/data1`.

```bash
cp -r /workspace/examples/LittleNet /data1
cp /data1/LittleNet/input_params.json /data1
```

#### 2.1 Prepare the input

Before running the programs, you need to prepare the inputs. In our toolchain, all the outputs are placed under `/data1`.
We call it the Interactivate Folder. So, we recommend you create this folder if it is not already there. Then we need to
configure the input parameters using `input_params.json` for the toolchain under `/data1`. As an example,
`input_params.json` for `LittleNet` model is under `/data1/LittleNet`, if you have already copy the folder as described
in the beginning of section 2. You already has the `input_params.json` ready. You can see the detailed explanation
for the input parameters in appendix A.

> The `input_params.json` is different in 0.10.0. Please check the FAQ for new config fields or use section 6.3 to
> upgrade your existed `input_params.json`.

#### 2.2 Running the program

After preparing `input_params.json`, you can run the programs by the following command:

```bash
# For KDP520
# python /workspace/scripts/fpAnalyserCompilerIpevaluator_520.py -t thread_number
python /workspace/scripts/fpAnalyserCompilerIpevaluator_520.py -t 8

# For KDP720
# python /workspace/scripts/fpAnalyserCompilerIpevaluator_720.py -t thread_number
python /workspace/scripts/fpAnalyserCompilerIpevaluator_720.py -t 8
```

`thread_number`: the number of thread to use.

#### 2.3 Get the result

After running this program, the folders called `compiler` and `fpAnalyser` will be generated under `/data1`. `compiler` stores the result of compiler and ipEvaluator. `fpAnalyser` stores the result of the model analyzer.

We can find the following files after running the script above:

* `/data1/fpAnalyser/<model_name>.quan.wqbi.bie`: the encrypted result of the model analyzer. It includes the quantize information and the model itself. Can be taken by the compiler and the simulator.
* `/data1/compiler/command.bin`: the compiled binary for the hardware.
* `/data1/compiler/setup.bin`: the compiled binary for the hardware.
* `/data1/compiler/weight.bin`: the compiled binary for the hardware.
* `/data1/compiler/ioinfo.csv`: the hardware IO mapping information of the model.
* `/data1/compiler/ip_eval_prof.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 520 version script generate this file.)*
* `/data1/compiler/ProfileResult.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 720 version script generate this file.)*

### 3 Hardware validation (optional)

#### 3.1 Run hardware validate script.

This step will make sure whether the mathematical simulator’s result is the same as the hardware simulator’s. In other
words, this step makes sure the model can run correctly on the hardware.

```bash
# For KDP520
python /workspace/scripts/hardware_validate_520.py

# For KDP720
python /workspace/scripts/hardware_validate_720.py
```

If it succeeds, you can the command line print out log: `[info] hardware validating successes!`. Otherwise, you might need to check your model to see if it has passed the converter. If the problem persist, please ask our stuff for help and provide the simulator result and the hardware simulator result under `/data1/simulator` and `/data1/c_sim`.

#### 3.2 Simulator and Emulator

One can also run simulator manually to get the result and check if it meets the need. This part is descibed in the end to end simulator document. Please check.


### 4 Batch-Compile

This part is the instructions for batch-compile, which will generate the binary file requested by firmware with the `bie` files given.

#### 4.1 Fill the input parameters

Fill the input parameters in the `/data1/batch_input_params.json` under `/data1`. Please refer to the appendix B to fill the related parameters.

For the LittleNet example, if you already follow the instructions in the section 2. You should already have `LittleNet.quan.wqbi.bie` under `/data1/fpAnalyser/`

**Please make sure you are generated the bie file with the correct hardware version. For example, if you want to batch-compile for the 520 hardware, you need to generate the bie with the 520 FP-analyzer**

Here is the config `/data1/batch_input_params.json` we need to batch compile the LittleNet:

```json
{
    "models": [
        {
            "id": 32769,
            "version": "1",
            "path": "/data1/fpAnalyser/LittleNet.quan.wqbi.bie"
        }
    ]
}
```

We can also do batch compile with multiple models and with encryption. Please check the appendix fB or more details about the config fields.

#### 4.2 Running the programs

For running the compiler and ip evaluator:

```bash
# For KDP520
# python /workspace/scripts/batchCompile_520.py
python /workspace/scripts/batchCompile_520.py

# For KDP720
# python /workspace/scripts/batchCompile_720.py
python /workspace/scripts/batchCompile_720.py
```

#### 4.3 Get the result

Under `/data1`, you’ll find a folder called `batch_compile`, which contains the output files of batch compile. There so many outputs but not all of them are useful for the user. Here are the main outputs you may need:

* `/data1/batch_compile/<model_name>.command.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.setup.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.weight.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.ioinfo.csv`: the hardware IO mapping information of the model. You might find one for every model you list in the json.
* `/data1/batch_compile/models_520.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 520 version script generate this file.)*
* `/data1/batch_compile/models_720.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 720 version script generate this file.)*

> **Difference between `*.bin` and `models_*.nef`**
>
> `weight.bin`, `setup.bin` and `weight.bin` are for hardware simulator. They only contains information for a single model. They are mostly for debugging and testing usages.
>
> `model_*.nef` is for the firmware to load onto the chip. It could contain information for multiple models. It's mainly used for firmware testing and deployment.

#### 4.4 Run batch compile with multiple models

The name 'batch compile' comes from its ability to compile multiple models together.

The `/data1/batch_input_params.json` is just like in section 4.1, but with one more model which can be found under E2E simulator folder.

```json
{
    "models": [
        {
            "id": 32769,
            "version": "1",
            "path": "/data1/fpAnalyser/LittleNet.quan.wqbi.bie"
        },
        {
            "id": 32770,
            "version": "1",
            "path": "/workspace/E2E_simulator/app/fd_external/model/520/ssd7_0.8_epoch-97_loss-0.1407_val_loss-0.0825_opt.piano.kdp520.scaled.quan.wqbi.bie"
        }
    ]
}
```

The command is the same as in section 4.2 and the results are `.bin` files for each model and on `.nef` file like mentioned in section 4.3.


### 5 FpAnalyser and Batch-Compile (Not Recommend)

This part is the instructions for FP-analysis and batch-compile. The script introduced in this part is actually an combination of section 2 and section 4.

We recommend doing FP-analysis (section 2) and batch-compile (section 4) separately. The fP-Analysis is very time-consuming. Thus, saving the `bie` file of each model for the future usage is more convinient.

Back to this section, again, we'll use the `LittleNet` as an example. Just like in the section 4, we need `batch_input_params.json`. But this time, **the fields we need to prepare are different**. Please check the next section.

#### 5.1 Fill the input parameters

As said in section 4, the details of the config can be found in the appendix. You can use the following code to create the `batch_input_params.json` for a walk through.

```json
{
    "encryption": {
        "whether_encryption": false,
        "encryption mode": 1,
        "encryption_key": "0x12345678",
        "key_file": "",
        "encryption_efuse_key": "0x12345678"
    },
    "models": [
        {
            "id": 32769,
            "version": "1",
            "path": "/data1/LittleNet/LittleNet.onnx",
            "input_params": "/data1/LittleNet/input_params.json"
        }
    ]
}
```

 We can take a look on what are the differences. Ignore the encryption section which is set to false. The real differences here are that we are giving `onnx` instead of `bie` in the model's `path`, and giving an extra `input_params.json` in a field called `input_params`. This `input_params.json` is the one that we use in section 2. With the onnx and the json, it could run the FP-analysis just like what we do in secion 2, uses the generated `bie` to do batch-compile right after all the FP-analysis is finished.

#### 5.2 Running the programs

For running the FP-analysis and batch-compiler:

```bash
# For KDP520
# python /workspace/scripts/fpAnalyserBatchCompile_520.py -t thread_number
python /workspace/scripts/fpAnalyserBatchCompile_520.py -t 8

# For KDP720
# python /workspace/scripts/fpAnalyserBatchCompile_720.py -t thread_number
python /workspace/scripts/fpAnalyserBatchCompile_720.py -t 8
```

`thread_number`: the number of thread to use

#### 5.3 Get the result

Under `/data1`, you’ll find a folder called `batch_compile`, which contains the output files of batch compile and FP-analysis. There so many outputs but not all of them are useful for the user. Here are the main outputs you may need:

* `/data1/batch_compile/<model_name>.quan.wqbi.bie`: the encrypted result of the model analyzer. It includes the quantize information and the model itself. Can be taken by the compiler and the simulator.
* `/data1/batch_compile/<model_name>.command.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.setup.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.weight.bin`: the compiled binary for the hardware of a single model. You might find one for every model you list in the json.
* `/data1/batch_compile/<model_name>.ioinfo.csv`: the hardware IO mapping information of the model. You might find one for every model you list in the json.
* `/data1/batch_compile/models_520.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 520 version script generate this file.)*
* `/data1/batch_compile/models_720.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 720 version script generate this file.)*

### 6 Other utilities

#### 6.1 Convert bin file to png

```bash
cd /workspace/scripts/utils && python bintoPng.py -i input_rgb565_file_path –o output_png_file_path –he rgb565_height –w rgb565_width -f bin_format
```

#### 6.2 Post process

```bash
cd /workspace/scripts/utils && python post_process.py -i emulator_result_folder -m model_type
```

#### 6.3 Upgrade `input_params.json`

If you have the configuration file from toolchain v0.9.0, you can use the following script to convert the old
`input_params.json` into a new one.

```bash
python /workspace/scripts/upgrade_input_params.py old_input_params.json new_input_params.json
```

#### 6.4 Combine NEF files

You can combine multiple generated NEF files into one with `/workspace/libs/compiler/kneron_nef_utils`. This is very useful when you already have multiple nef files from different versions of the toolchain. The usage is as below:

```bash
/workspace/libs/compiler/kneron_nef_utils -c "nef_file_1 nef_file_2 ..." -O output_folder_name
```

In the command above, the nef file list after `-c` are the nef files you want to compiler. And the result will be saved in the folder given after `-O`. The result file is names as `models_<platform>.def`, e.g. `models_520.nef`. If the output folder is not given in the argument, the result is save in an `output` folder under the current path.

## Appendix

### A. How to configure the `input_params.json`?

By following the above instructions, the `input_params.json` will be saved in `/data1`.
Please do not change the parameters’ names.

Here is an example JSON with comments. **Please remove all the comments in the real configuration file.**

```json
{
    // The basic information of the model needed by the toolchain.
    "model_info": {
        // The input model file. If you are not sure about the input names, you can
        // check it through model visualize tool like [netron](https://netron.app/).
        // If the configuration is referred by `batch_input_params.json`, this field
        // will be ignored.
        "input_onnx_file": "/data1/yolov5s_e.onnx",
        // A list of the model inputs name with the absolute path of their corresponding
        // inputs image folders. It is required by FP-analysis.
        "model_inputs": [{
            "model_input_name": "data_out_0" ,
            "input_image_folder": "/data1/100_image/yolov5",
        }],
        // Special mode for fp-analysis. Currently available mode:
        // - default: for most of the models.
        // - post_sigmoid: recommand for yolo models.
        // If this option is not present, it uses the 'default' mode.
        "quantize_mode": "default",
        // For fp-analysis, remove outliers when calculating max & min. It should be between 0.0 and 1.0.
        // If not given, default value is 0.999.
        "outlier": 0.999
    },
    // The preprocess method of the input images.
    "preprocess": {
        // The image preprocess methods.
        // Options: `kneron`, `tensorflow`, `yolo`, `caffe`, `pytorch`
        // `kneron`: RGB/256 - 0.5,
        // `tensorflow`: RGB/127.5 - 1.0,
        // `yolo`: RGB/255.0
        // `pytorch`: (RGB/255. -[0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
        // `caffe`(BGR format) BGR  - [103.939, 116.779, 123.68]
        // `customized”`: please refer to FAQ question 8
        "img_preprocess_method": "kneron",
        // The channel information after the input image is preprocessed.
        // Options: RGB, BGR, L
        // L means single channel.
        "img_channel": "RGB",
        // The radix information for the npu image process.
        // The formula for radix is 7 – ceil(log2 (abs_max)).
        // For example, if the image processing method we utilize is "kneron",
        // the related image processing formula is "kneron": RGB/256 - 0.5,
        // and the processed value range will be (-0.5, 0.5).
        // abs_max = max(abs(-0.5), abs(0.5)) = 0.5
        // radix = 7 – ceil(log2(abs_max)) = 7 - (-1) = 8
        "radix": 8,
        // [optional]
        // Indicates whether or not to keep the aspect ratio. Default is true.
        "keep_aspect_ratio": true,
        // [optioanl]
        // This is the option for the mode of adding paddings, and it will be utilized only
        // when `keep_aspect_ratio` is true. Default is 1.
        // Options: 0, 1
        // 0 – If the original width is too small, the padding will be added at both right
        //     and left sides equally; if the original height is too small, the padding
        //     will be added at both up and down sides equally.
        // 1 – If the original width is too small, the padding will be added at the right
        //     side only, if the original height is too small, the padding will be only
        //     added at the down side.
        "pad_mode": 1,
        // [optional]
        // The parameters for cropping image. And it has four sub parameters. Default are 0s.
        // -crop_x, cropy, the left cropping point coordinate.
        // -crop_y, cropy, the up cropping point coordinate.
        // -crop_h, the width of the cropped image.
        // -crop_w, the height of the cropped image.
        "p_crop": {
            "crop_x": 0,
            "crop_y": 0,
            "crop_w": 0,
            "crop_h": 0
        }
    },
    // [optional]
    // A list of the model inputs name with the absolute path of their corresponding
    // input images. It is used by the hardware validator. If this field is not given,
    // a random image for each input will be picked up from the `input_image_folder`
    // in the `model_info`.
    "simulator_img_files": [{
            "model_input_name": "data_out" ,
            "input_image": "/data1/100_image/yolov5/a.jpg",
    }]
}
```

### B. How to configure the `batch_input_params.json`?

By following the above instructions, the `batch_input_params.json` will be saved under `/data1`.
Please do not change the parameters’ names.

Here is an example JSON with comments. **Please remove all the comments in the real configuration file.**

```json
{
    // [optional]
    // The encryption setting for the batch compiler. Default is not enabled.
    "encryption": {
        // Whether enable encrytion
        "whether_encryption": false,
        // Encrytion mode selection
        // Options: 1, 2
        "encryption mode": 1,
        // Encrytion key. A hex string. Required in mode 1.
        "encryption_key": "0x12345678",
        // Encrytion file. An absolute path. Required in mode 1.
        "key_file": "/data1/enc.txt",
        // Encrytion key. A hex string. Required in mode 2, optional in mode 1.
        "encryption_efuse_key": "0x12345678"
    },
    // [optional]
    // Whether seperate buffers for each model output. Default is true.
    "dedicated_output_buffer": true,
    // [optional]
    // Whether compress weight for saving space.
    "weight_compress": false,
    // Batch compile model list
    "models": [
        {
            // Model ID
            "id": 32769,
            // Model version. should be an hex code at most 4 digit.
            "version": "1",
            // The path to the model.
            // If you are running fpAnalyserBatchCompile, this field should be an onnx.
            // If you are running batchCompile, this field could be an onnx or a bie.
            // If onnx is provided in the second case, you also need to provide the
            // `radix_json`.
            "path": "models/output_0.onnx",
            // [optional]
            // Only needed when you are running batchCompile_*.py with an onnx.
            "radix_json": ".json",
            // Required when you are running fpAnalyserBatchCompile. This configuration
            // file is used to provide information for FP-analysis. Please check FAQ 1
            // for details.
            "input_params": "/data1/input_params.json"
        }
    ]
}
```

### C. What’s the meaning of IP Evaluator’s output?

* estimate FPS float => average Frame Per Second
* total time => total time duration for single image inference on NPU
* MAC idle time => time duration when NPU MAC engine is waiting for weight loading or data loading
* MAC running time => time duration when NPU MAC engine is running
* average DRAM bandwidth => average DRAM bandwidth used by NPU to complete inference
* total theoretical convolution time => theoretically minimum total run time of the model when MAC efficiency is 100%
* MAC efficiency to total time => time ratio of the theoretical convolution time to the total time

### D. What’s the meaning of the output files?

* `command.bin`: the compiled binary for the hardware.
* `setup.bin`: the compiled binary for the hardware.
* `weight.bin`: the compiled binary for the hardware.
* `ioinfo.csv`: the hardware IO mapping information of the model.
* `ip_eval_prof.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 520 version script generate this file.)*
* `ProfileResult.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 720 version script generate this file.)*
* `<model_name>.quan.wqbi.bie`: the encrypted result of the model analyzer. It includes the quantize information and the model itself. Can be taken by the compiler and the simulator.
* `models_520/720.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware.

If you find the cpu node in `ioinfo.csv`, whose format is `c,\**,**`”`, you need to implement and register this function in SDK.


#### E. How to use customized methods for image preprocess?

1. Configure the `input_params.json`, and fill the value of `img_preprocess_method` as `customized`;
2. edit the file `/workspace/scripts/utils/img_preprocess.py`, search for the text `#this is the customized part` and add your customized image preprocess method there.
