# Kneronnxopt

Kneronnxopt is the ONNX optimizer project for kneron hardware platforms. Its purpose is to provide shapes for all the tensors as well as accelerate the inference and compiling process. Currently, we support ONNX up to opset 18.

## 1. Preparation

Before using the tool, you need to activate the conda environment for it. Required packages are already installed in the environment. You can activate the environment by running the following command:

```bash
conda activate onnx1.13
```

## 2. Usage

The tool is under `/workspace/libs/kneronnxopt`. You can use the following command to run the tool:

```bash
python /workspace/libs/kneronnxopt/kneronnxopt/optimize.py -o <output_onnx_model> <input_onnx_model>
```

It also has the following optional arguments:

* `-h, --help`: Show this help message and exit.
* `--log`: Set log level (default: INFO). Available log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
* `--duplicate-shared-weight`: Duplicate shared weights in the model. Default is False.
* `--skip-check`: Skip the onnxruntime check or not. Enabling this flag can speed up the script, but also introcduce risks for future model deployment.
* `--overwrite-input-shapes`: Overwrite the input shape. The format is "input_name:dim0,dim1,...,dimN" or simply "dim0,dim1,...,dimN" when there is only one input, for example, "data:1,3,224,224" or "1,3,224,224". Note: you might want to use some visualization tools like netron to make sure what the input name and dimension ordering (NCHW or NHWC) is.

## 3. Notes

This tool is still under development. If you have any questions, please feel free to contact us.

This tool automatically update the model opset to 18. This process has no good way to reverse. Please use other tools is you do not want to upgrade your model opset.

If you want to cut the model, please use `onnx.utils.extract_model` from ONNX. Please check <https://onnx.ai/onnx/api/utils.html>