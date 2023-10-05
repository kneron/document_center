# Command Line Script Tools

## 0. Introduction

Since toolchain version v0.14.0, we introduce Python API and recommend using it for the general work flow. This document provides the usage of all the script utilities. Note that 530 only has the IP evaluator script. For other tools, please refer to the toolchain document.

**Since toolchain version v0.21.0, most of the command line scripts are removed. Please use the Python API instead.**

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

# For KDP530
cd /workspace/scripts && ./compilerIpevaluator_530.sh /workspace/examples/LittleNet/LittleNet.onnx
```

This part uses the default configuration for the hardware and not available for fine-tuning.

#### 1.2 Get the result

A folder called `compiler` will be generated in `/data1`, which stores the result of the compiler and IP Evaluator. If you are using this script with an `onnx` file, please ignore the binary files since they are not quantized and unable to be used.

We can find the following files after running the script above:

* `/data1/compiler/command.bin`: the compiled binary for the hardware.
* `/data1/compiler/setup.bin`: the compiled binary for the hardware.
* `/data1/compiler/weight.bin`: the compiled binary for the hardware.
* `/data1/compiler/ioinfo.csv`: the hardware IO mapping information of the model for 520.
* `/data1/compiler/ioinfo.json`: the hardware IO mapping information of the model for other hardware platforms.
* `/data1/compiler/ip_eval_prof.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 520 version script generate this file.)*
* `/data1/compiler/ProfileResult.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 720 version script generate this file.)*


### 2 Batch-Compile

This part is the instructions for batch-compile, which will generate the binary file requested by firmware with the `bie` files given.

#### 2.1 Fill the input parameters

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
* `/data1/batch_compile/<model_name>.ioinfo.csv`: the hardware IO mapping information of the model. You might find one for every model you list in the json. (520)
* `/data1/batch_compile/<model_name>.ioinfo.json`: the hardware IO mapping information of the model. You might find one for every model you list in the json.
* `/data1/batch_compile/models_520.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 520 version script generate this file.)*
* `/data1/batch_compile/models_720.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware. *(Only the 720 version script generate this file.)*

> **Difference between `*.bin` and `models_*.nef`**
>
> `weight.bin`, `setup.bin` and `weight.bin` are for hardware simulator. They only contains information for a single model. They are mostly for debugging and testing usages.
>
> `model_*.nef` is for the firmware to load onto the chip. It could contain information for multiple models. It's mainly used for firmware testing and deployment.

#### 4.4 Run batch compile with multiple models

The name 'batch compile' comes from its ability to compile multiple models together.

The `/data1/batch_input_params.json` is just like in section 4.1, but with one more model. (This model is not provided. You need to prepare one yourself.)

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
            "path": "/data1/ssd7_0.8_epoch-97_loss-0.1407_val_loss-0.0825_opt.piano.kdp520.scaled.quan.wqbi.bie"
        }
    ]
}
```

The command is the same as in section 4.2 and the results are `.bin` files for each model and on `.nef` file like mentioned in section 4.3.


### 3 Other utilities

#### 3.1 Convert bin file to png

```bash
cd /workspace/scripts/utils && python bintoPng.py -i input_rgb565_file_path –o output_png_file_path –he rgb565_height –w rgb565_width -f bin_format
```

#### 3.2 Post process

```bash
cd /workspace/scripts/utils && python post_process.py -i emulator_result_folder -m model_type
```

#### 3.3 Combine NEF files

You can combine multiple generated NEF files into one with `/workspace/libs/compiler/kneron_nef_utils`. This is very useful when you already have multiple nef files from different versions of the toolchain. The usage is as below:

```bash
/workspace/libs/compiler/kneron_nef_utils -c "nef_file_1 nef_file_2 ..." -O output_folder_name
```

In the command above, the nef file list after `-c` are the nef files you want to compiler. And the result will be saved in the folder given after `-O`. The result file is names as `models_<platform>.def`, e.g. `models_520.nef`. If the output folder is not given in the argument, the result is save in an `output` folder under the current path.

## Appendix

### A. How to configure the `batch_input_params.json`?

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
        }
    ]
}
```

### B. What’s the meaning of IP Evaluator’s output?

* estimate FPS float => average Frame Per Second
* total time => total time duration for single image inference on NPU
* MAC idle time => time duration when NPU MAC engine is waiting for weight loading or data loading
* MAC running time => time duration when NPU MAC engine is running
* average DRAM bandwidth => average DRAM bandwidth used by NPU to complete inference
* total theoretical convolution time => theoretically minimum total run time of the model when MAC efficiency is 100%
* MAC efficiency to total time => time ratio of the theoretical convolution time to the total time

### C. What’s the meaning of the output files?

* `command.bin`: the compiled binary for the hardware.
* `setup.bin`: the compiled binary for the hardware.
* `weight.bin`: the compiled binary for the hardware.
* `ioinfo.csv`: the hardware IO mapping information of the model. (520)
* `ioinfo.json`: the hardware IO mapping information of the model.
* `ip_eval_prof.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 520 version script generate this file.)*
* `ProfileResult.txt`:  the IP evaluation report, which is the estimate performance of your model on the NPU. *(Only the 720 version script generate this file.)*
* `<model_name>.quan.wqbi.bie`: the encrypted result of the model analyzer. It includes the quantize information and the model itself. Can be taken by the compiler and the simulator.
* `models_520/720.nef`: the compiled binary with all the models. This file is designed to be loaded by the firmware.

If you find the cpu node in `ioinfo.csv`, whose format is `c,\**,**`”`, you need to implement and register this function in SDK.
