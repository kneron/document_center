# Toolchain Common Errors

## ONNX Converter and Optimizers

### RuntimeError: Inferred shape and existing shape differ in rank: (0) vs (3)

**Tags**: RuntimeError, Converter, ONNX

**Causes**:

Inside the converter, we are using `onnx.shape_inference.infer_shapes` from the official onnx repository to do the shape inference. It inferences the shapes of the nodes' input and output one by one. If any existing shape written in the graph is different from the already existed shape, this error is raise. Thus, there might be two main reasons for this error:

1. The input shape and the output shape of this model is invalid.
2. The onnx shape inferencer cannot inference the shape correctly.

**Solution**:

1. Please double check the model see if there is any wrong input/output shape.
2. Check if there is any large blocks of Reshape or Transpose. Those blocks are not friendly for the shape inferencer. Please consider replace those structures.

## FPAnalyser, Compiler and IP Evaluator

### Invalid program input: undefined CPU op [*OperatorA*] of node [*NodeNameA*]

**Tags**: InvalidProgramInput, Compiler

**Causes**:

This error is caused by an operator type which is not supported in the current current version of toolchain or in the specific hardware. The operator type name is shown in the '*OperatorA*' position and the node name is shown in the place of '*NodeNameA*'.

**Solution**:

Please consider replace the unsupported nodes with other nodes.

### Command '['/workspace/libs/fpAnalyser/updater/run_updater', '-i', '/workspace/.tmp/updater/json']' died with <Signals, SIGABRT: 6>

**Tags**: SIGABRT, FP Analyser, Updater

**Causes**:

This error can be caused by many differenct reasons. Here are the possible reasons:

1. The most common ones are that the input image number is too large, the thread number is too large and the model is too large which causes the FP analyser killed by the system.
2. The path in the configuration file is invalid. Thus, the updater failed to load it.
3. The model is not acceptable by the updater.

**Solution**:

We may need to follow try the following solutions one by one to figure out the real reason of the failure. And then resolve the problem.

1. Please try pass the model through IP Evaluator. The command is described in toolchain manual section 3.4. If it generate the report successfully without error message, then the model is acceptable by the toolchain and please try the next step. Otherwise, the IP evaluator tells you what the problem is with the model in the exception.
2. Please double check the path in your configuration file. One common mistake is using relative path instead of the absolute path. In the configuration, we strongly recommend you using the absolute path or full path to avoid the file not found issues.
3. Please try reduce the thread number and the input number.
4. If it still doesn't work. Please consider submit your question on the forum: <https://www.kneron.com/forum/>.

### Cannot find the corresponding input image folder of model input `model_input_0`

**Tags**: LoadConfigException, FP Analyser, Updater

**Causes**:

To run model updater, one need to provide input images for each input. This error is raised because a specific model input do not has any input image folder configured. The input name is shown in the position of `model_input_0`.

**Solution**:

Please double check your configuration file to see if there is any typo or the path is correct. And remember to provide absolute path.
