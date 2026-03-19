# Kneronnxopt

Kneronnxopt is the ONNX optimizer project for Kneron hardware platforms. It prepares tensor shapes and optimizes graph structures to improve inference and compilation flow. Currently, it supports ONNX opset 8 to 18.

## 1. Preparation

Before using the tool, you need to activate the conda environment for it. Required packages are already installed in the environment. You can activate the environment by running the following command:

```bash
conda activate onnx1.13
```

## 2. Usage

### 2.1. Standard model optimization

Use module execution for standard ONNX models:

```bash
python -m kneronnxopt.optimize <input_onnx_model> -o <output_onnx_model>
```

Optional arguments:

* `-h, --help`: Show this help message and exit.
* `--log`: Set log level (default: INFO). Available log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
* `--duplicate-shared-weights`: By what level to duplicate shared weights. `0`: no duplication, `1`: duplicate only when required by compiler, `2`: always duplicate. Default is `1`.
* `--skip-check`: Skip the onnxruntime check. Enabling this flag can speed up the script, but also introduces risks for future model deployment.
* `--overwrite-input-shapes`: Overwrite the input shape. The format is "input_name:dim0,dim1,...,dimN" or simply "dim0,dim1,...,dimN" when there is only one input, for example, "data:1,3,224,224" or "1,3,224,224". Note: you might want to use some visualization tools like netron to make sure what the input name and dimension ordering (NCHW or NHWC) is.
* `--skip-fuse-qkv`: Skip the `fuse_qkv` optimization.
* `--clear-descriptions`: Clear all descriptions in the graph.
* `--clear-shapes`: Clear all existing shapes in the graph except input shapes.
* `--opt-matmul`: Optimize MatMul operators for Kneron compiler.
* `--replace-avgpool-with-conv`: Replace AveragePool with depthwise Conv when possible to avoid CPU nodes.
* `--replace-dilated-conv`: Replace dilated Conv patterns when possible.
* `--defuse-gaps`: Defuse GAP patterns when possible.

Notes:

* If `-o` is not provided, output defaults to `<input>_optimized.onnx`.

### 2.2. Large model optimization (>2 GiB)

For large ONNX models, use the large-model module entry:

```bash
python -m kneronnxopt.large_model_fast_proc <input_onnx_model> -o <output_onnx_model>
```

Optional arguments:

* `-h, --help`: Show this help message and exit.
* `--log`: Set log level (default: INFO). Available log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
* `--overwrite-input-shapes`: Overwrite input shapes for simplify and shape inference.
* `--skip-fuse-qkv`: Skip the `fuse_qkv` optimization.
* `--onnxtool`: Use `onnx-tool` for shape inference. This is useful when shapes cannot be inferred by the default pass. However, this tool may clip off some nodes, so use with caution and always check the output model.

### 2.3. Help command

To inspect full and current options from the tool directly:

```bash
python -m kneronnxopt.optimize -h
python -m kneronnxopt.large_model_fast_proc -h
```

## 3. Notes

This appendix focuses on console usage. For Python API usage, please refer to [3.1.2 ONNX Optimization](../manual_3_onnx.md#312-onnx-optimization).

If you want to cut the model, please use `onnx.utils.extract_model` from ONNX. Please check <https://onnx.ai/onnx/api/utils.html>
