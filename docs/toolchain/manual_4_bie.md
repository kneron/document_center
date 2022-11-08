## 4. BIE Workflow

As mentioned briefly in the previous section, the bie file is the model file which is usually generated after quantization. It is encrpyted and not available for visuanlization.
In this chapter, we would go through the steps of quantization.

### 4.1. Quantization

Quantization is the step where the floating-point weight are quantized into fixed-point to reduce the size and the calculation complexity. The Python API for this step is called `analysis`. It is also a class function of `ktc.ModelConfig`. It takes a dictionary as input.

```python
analysis(input_mapping, output_bie = None, threads = 4, mode=1)
```

* `input_mapping` is the a dictionary which maps a list of input data to a specific input name. Generally speaking, the quantization would be preciser with more input data.
* `output_bie` is the path where you want your bie generated. By default, it is under /data1/fpAnalyser.
* `threads` is the threads number you want to utilize. Please note more threads would lead to more RAM usage as well.
* `mode` is an optional flag to determine whether to skip the model verification step while doing the quantization. The model verification makes sure your model can be processed correctly by our toolchain. But this step could take more time and consume more system resources. *Note that if your memory is not enough, the utility would raise segmentation fault.* By default, this flag is set to 1, which means the verification is skipped.
  * 1: only analysis. Skip verification.
  * 2: Verification with one image.
  * 3: Verification with all provided images. (WARNING: This option takes very long time.)
* The return value is the generated bie path.

This is a very simple example usage. There are many more parameters for fine-tuning. Please check Please check [Toolchain Python API](http://doc.kneron.com/docs/toolchain/python_api/) if needed.

Please also note that this step would be very time-consuming since it analysis the model with every input data you provide.

Here as a simple example, we only use four input image as exmaple and run it with the `ktc.ModelConfig` object `km` created in section 3.2:

```python
# Preprocess images and create the input mapping
input_images = [
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0001.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0002.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0003.png"),
    preprocess("/workspace/examples/LittleNet/pytorch_imgs/Abdullah_0004.png"),
]
input_mapping = {"data_out": input_images}

# Quantization
bie_path = km.analysis(input_mapping, output_bie = None, threads = 4)
```

This function has more parameters for fine-tuning. Please check [Toolchain Python API](http://doc.kneron.com/docs/toolchain/python_api/) if needed.

### 4.2. E2E Simulator Check (Fixed Point)

Before going into the next section of compilation, we need to ensure the quantized model do not lose too much precision.

We would use `ktc.kneron_inference` here, too. But here we are using the generated bie file as the input.

The python code would be like:

```python
fixed_results = ktc.kneron_inference(input_data, bie_file=bie_path, input_names=["data_out"])
```

The usage is almost the same as using onnx. In the code above, `inf_results` is a list of result data. `bie_file` is the path to the input bie. `input_data` is a list of input data after preprocess the `input_names` is a list of model input name. The requirement is the same as in section 3.3. If your platform is not 520, you may need an extra parameter `platform`, e.g. `platform=720` or `platform=530`.

As mentioned above, we do not provide any postprocess. In reality, you may want to have your own postprocess function in Python, too.

After getting the `fixed_results` and post-process it, you may want to compare the result with the `inf_results` which is generated in section 3.3 to see if the precision lose too much. If the result is unacceptable, please check FAQ 2 for possible solutions.

## 4.3. FAQ

### 4.3.1. What if the E2E simulator results of floating-point and fixed-point lost too match accuracy?

Please try the following solutions:

1. Try redoing the analysis with more image that are the expected input of the network.
2. Double check if the cut final CPU nodes are added in post-process.
3. Fine tuning the analysis with outlier and quantize mode.

If none of the above works, please search on forum <https://www.kneron.com/forum/categories/ai-model-migration>. You can also contact us through the forum if no match issue found. The technical support would reply directly to your post.

### 4.3.2. What if I get one of the following errors?

#### 4.3.2.1. Invalid program input: undefined CPU op [*OperatorA*] of node [*NodeNameA*]

**Causes**:

This error is caused by an operator type which is not supported in the current current version of toolchain or in the specific hardware. The operator type name is shown in the '*OperatorA*' position and the node name is shown in the place of '*NodeNameA*'.

**Solution**:

Please consider replace the unsupported nodes with other nodes.

#### 4.3.2.2. Command '['/workspace/libs/fpAnalyser/updater/run_updater', '-i', '/workspace/.tmp/updater/json']' died with <Signals, SIGABRT: 6>

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

#### 4.3.2.3. Cannot find the corresponding input image folder of model input `model_input_0`

**Causes**:

To run model updater, one need to provide input images for each input. This error is raised because a specific model input do not has any input image folder configured. The input name is shown in the position of `model_input_0`.

**Solution**:

Please double check your configuration file to see if there is any typo or the path is correct. And remember to provide absolute path.
