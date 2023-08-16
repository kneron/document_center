# 4. BIE Workflow

As mentioned briefly in the previous section, the bie file is the model file which is usually generated after quantization. It is encrpyted and not available for visuanlization.
In this chapter, we would go through the steps of quantization.

## 4.1. Quantization

Quantization is the step where the floating-point weight are quantized into fixed-point to reduce the size and the calculation complexity. The Python API for this step is called `analysis`. It is also a class function of `ktc.ModelConfig`. It takes a dictionary as input.

Below is the quantization API. Note that there are many fine-tuning parameter. We do not need to utilize them all.

```python
#[API]
classmethod analysis(input_mapping, output_dir="/data1/kneron_flow", threads=4, quantize_mode="default")
```

Fix point analysis for the model. If the object is initialized with an onnx. This step is required before compiling. The result bie path will be returned.

Args:

* input_mapping (Dict): Dictionary of mapping input data to a specific input. Input data should be a list of numpy array.
* output_dir (str, optional): path to the output directory. Defaults to "/data1/kneron_flow"".
* threads (int, optional): multithread setting. Defaults to 4.
* quantize_mode (str, optional): quantize_mode setting. Currently support default and post_sigmoid. Defaults to "default".
* datapath_range_method (str, optional): could be 'mmse' or 'percentage. mmse: use snr-based-range method. percentage: use arbitary percentage. Default to 'percentage'.
* percentile (float, optional): used under 'mmse' mode. The range to search. The larger the value, the larger the search range, the better the performance but the longer the simulation time. Defaults to 0.001,
* outlier_factor (float, optional): used under 'mmse' mode. The factor applied on outliers. For example, if clamping data is sensitive to your model, set outlier_factor to 2 or higher. Higher outlier_factor will reduce outlier removal by increasing range. Defaults to 1.0.
* percentage (float, optional): used under 'percentage' mode. Suggest to set value between 0.999 and 1.0. Use 1.0 for detection models. Defaults to 0.999.
* datapath_bitwidth_mode: choose from "int8"/"int16". ("int16" not supported in kdp520).
* weight_bitwidth_mode: choose from "int8"/"int16". ("int16" not supported in kdp520).
* model_in_bitwidth_mode: choose from "int8"/"int16". ("int16" only for internal debug usage).
* model_out_bitwidth_mode: choose from "int8"/"int16". (currently should be same as model_in_bitwidth_mode).
* fm_cut (str, optional): could be "default" or "deep_search". Get a better image cut method through deep search, so as to improve the efficiency of our NPU. Defaults to "default".
* mode (int, optional): running mode for the analysis. Defaults to 1.
    - 0: run ip_evaluator only. This mode will not output bie file.
    - 1: run knerex (for quantization) only.
    - 2: run knerex with 1 image verification (dynasty, compiler, csim and bit-true-match check).
    - 3: run knerex with all images verification (dynasty, compiler, csim and bit-true-match check). WARNING: This option takes very long time.
* optimize (int, optional): level of optimization. 0-4, the larger number, the better model performance, but takes longer. Defaults to 0.
    * 0: the knerex generated quantization model.
    * 1: bias adjust parallel, no firmware cut improvement.
    * 2: bias adjust parallel, with firmware cut improvement.
    * 3: bias adjust sequential, no firmware cut improvement. SLOW!
    * 4: bias adjust sequential, with firmware cut improvement.  SLOW!
* export_dynasty_dump (bool, optional): whether export the dump result when running dynasty. Defaults to False.

Please also note that this step would be very time-consuming since it analysis the model with every input data you provide.

Here as a simple example, we only use four input image as exmaple and run it with the `ktc.ModelConfig` object `km` created in section 3.2:

```python
# Preprocess images as the quantization inputs. The preprocess function is defined in the previous section.
import os
raw_images = os.listdir("/workspace/examples/mobilenetv2/images")
input_images = [preprocess("/workspace/examples/mobilenetv2/images/" + image_name) for image_name in raw_images]

# We need to prepare a dictionary, which mapping the input name to a list of preprocessed arrays.
input_mapping = {"images": input_images}

# Quantization with only deep_search enabled.
bie_path = km.analysis(input_mapping, threads = 4, fm_cut='deep_search')
```

Since toolchain v0.21.0, the analysis step also generates a detailed report in html format. You can find it under
`/data1/kneron_flow/model_fx_report.html`. You can view it using the command line web browser included in the toolchain:

```bash
w3m /data1/kneron_flow/model_fx_report.html
```

You can learn how to interpret it through the following link: [How to Interpret Fixed-Point Report](appendix/summary.md).

## 4.2. E2E Simulator Check (Fixed Point)

Before going into the next section of compilation, we need to ensure the quantized model do not lose too much precision.

We would use `ktc.kneron_inference` here, too. But here we are using the generated bie file as the input.

The python code would be like:

```python
fixed_results = ktc.kneron_inference(input_data, bie_file=bie_path, input_names=["data_out"], platform=720)
```

The usage is almost the same as using onnx. In the code above, `inf_results` is a list of result data. `bie_file` is the path to the input bie. `input_data` is a list of input data after preprocess the `input_names` is a list of model input name. The requirement is the same as in section 3.3. If your platform is not 520, you need an extra parameter `platform`, e.g. `platform=720` or `platform=530`.

As mentioned above, we do not provide any postprocess. In reality, you may want to have your own postprocess function in Python, too.

After getting the `fixed_results` and post-process it, you may want to compare the result with the `inf_results` which is generated in section 3.3 to see if the precision lose too much. If the result is unacceptable, please check FAQ 2 for possible solutions.

### 4.2.1 Get Radix Value (Deprecated)

In the previous versions or for the debug usage, we may need to get the input quantization value manually, which is the radix. Below is the API.

```python
#[API]
ktc.get_radix(inputs)
```

Get the radix value from the given inputs.

Args:

* inputs (List): a list of numpy arrays which could be the inputs of the target model.

Raises:
* `ValueError`: raise if the input values are out of range


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
