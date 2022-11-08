## 5. NEF Workflow

The nef file is the binary file after compiling and can be taken by the Kneron hardware. But unlike the utilities mentioned above, the process in this chapter can compile multiple models into one nef file. This process is call batch process. In this chapter, we would go through how to batch compile and how to verify the nef file.

### 5.1. Batch Compile

Batch compile turns multiple models into a single binary file. But, we would start with single model first.

The Python API is very simple:

```python
compile_result = ktc.compile(model_list)
```

The `compile_result` is the path for the generated nef file. By default, it is under /data1/batch_compile. It takes a list of `ktc.ModelConfig` object as the input `model_list`. The usage of `kt.ModelConfig` can be found in section 3.2. Note that the ModelConfig onject must have bie file inside. In details, it must be under either of the following status: the ModelConfig is initialized with `bie_path`, the ModelConfig is initialized with `onnx_model` or `onnx_path` but it have successfully run `analysis` function.

For the LittleNet example, please check the code below. Note that `km` is the `ktc.ModelConfig` object we generate in section 3.2 and use in the section 4.

```python
compile_result = ktc.compile([km])
```

For multiple models, we can simply extend the model list.

```python
# dummy.bie is not a real example bie which is available in the docker. Just for command showcase.
# Please adjust the parameters according to your actual input.
km2 = ktc.ModelConfig(32770, "0001", "520", bie_path="dummy.bie")
compile_result = ktc.compile([km, km2])
```

Note that for multiple models, all the models should share the same hardware platform and the model ID should be different.

This function has more parameters for fine-tuning. Please check [Toolchain Python API](http://doc.kneron.com/docs/toolchain/python_api/) if needed.

### 5.2. E2E Simulator Check (Hardware)

After compilation, we need to check if the nef can work as expected.

We would use `ktc.kneron_inference` here again. And we are using the generated nef file this time.

For the batch compile with only LittleNet, the python code would be like:

```python
hw_results = ktc.kneron_inference(input_data, nef_file=compile_result)
```

The usage is a little different here. In the code above, `hw_results` is a list of result data. `nef_file` is the path to the input nef. `input_data` is a list of input data after preprocess. The requirement is the same as in section 3.3. If your platform is not 520, you may need an extra parameter `platform`, e.g. `platform=720` or `platform=530`.

Here we use the same input `input_data` which we used in section 3.3. And the `compile_result` is the one that generated with only LittleNet model.

As mentioned above, we do not provide any postprocess. In reality, you may want to have your own postprocess function in Python, too.

For nef file with mutiple models, we can specify the model with model ID:

```python
hw_results = ktc.kneron_inference(input_data, nef_file=compile_result, model_id=32769)
```

After getting the `hw_results` and post-process it, you may want to compare the result with the `fixed_results` which is generated in section 4.2 to see if the results match. If the results mismatch, please contact us direcly through forum <https://www.kneron.com/forum/>.

### 5.3. NEF Combine

This section is not part of the normal workflow. But it would be very useful when you already have multiple nef files, some of which might from different versions of the toolchain, and you want to combine them into one. Here we provide a python API to achieve it.

```python
ktc.combine_nef(nef_path_list, output_path = "/data1/combined")
```

Here the `nef_path_list` shall be a list of the `str` which are the path to the nef files you want to combine. It should not be empty. And the second argument is optional. It should be the output folder path of the combined nef. By default, it should be `/data1/combined`. The return value is the output folder path. The combined nef file would be under the output folder and be named as `models_<target>.def`. For example, if your target platform is 520, the result file name would be `models_520.nef` inside the output folder.

Here is an usage example. Suppose you have three 520 nef files: `/data1/model_32769.nef`, `/data1/model_32770.nef` and `/data1/model_32771.nef`. Then you can use the following code to combine them. The result is "/data1/combined/models_520.nef"

```python
ktc.combine_nef(['/data1/model_32769.nef', '/data1/model_32770.nef', '/data1/model_32771.nef'], output_path = "/data1/combined")
```
