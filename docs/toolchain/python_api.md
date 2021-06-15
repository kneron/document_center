# Toolchain Python API

We provide a Python package in the docker toolchain. The package name is `ktc`. You can simply start by having
`import ktc` in your Python script. We hope this python API could help you simplify the workflow. In the following
sections, we'll introduce the API and their usage. You can also find the usage using the python `help()` function.

The general workflow is the same as mentioned in the toolchain manual. Models shall be passed through the several
stages to get the result: ONNX optimization, model analysis, compilation and inference.

There is also an simple example called `/workspace/examples/test_python_api.py` in the docker. This might helps you
understand the Python API usage.

**Note that this package is only available in the docker due to the dependency issue.**

## 1 ONNX Optimizer and Editor

The ONNX optimizer and editor provide the following API.

### 1.1 Converters

#### Keras to ONNX

```python
ktc.onnx_optimizer.keras2onnx_flow(keras_model_path, optimize, input_shape)
```

Return the converted onnx object. Convert keras model to onnx object.

Args:

* keras_model_path (str): the input hdf5/h5 model path.
* optimize (int, optional): optimization level. Defaults to 0.
* input_shape (List, optional): change the input shape if set. Only single input model is supported. Defaults to None.

#### Caffe to ONNX

```python
ktc.onnx_optimizer.caffe2onnx_flow(caffe_model_path, caffe_weight_path)
```

Return the converted onnx object. Convert caffe model to onnx object.

Args:

* caffe_model_path (str): the input model definition (.prototxt).
* caffe_weight_path (str): the input weight file (.caffemodel).

#### TFLite to ONNX

```python
ktc.onnx_optimizer.tflite2onnx_flow(tflite_path, release_mode, bottom_nodes)
```

Return the converted onnx object. Convert tflite model to onnx object.

Args:

* tflite_path (str): the input tflite model path.
* release_mode (bool, optional): whether eliminate the transpose for channel first. Defaults to True.
* bottom_nodes (List, optional): nodes name in tflite model which is the bottom node of sub-graph. Defaults to [].

### 1.2 Optimizers

#### onnx version update

```python
ktc.onnx_optimizer.onnx1_4to1_6(model)
```

Return the updated onnx model. Update model ir_version from 4 to 6 and update opset from 9 to 11.

Args:

* model (onnx.ModelProto): input onnx model.

#### Pytorch exported onnx optimization.

```python
ktc.onnx_optimizer.torch_exported_onnx_flow(m, disable_fuse_bn=False):
```

Return the optimized model. Optimize the Pytorch exported onnx. Note that onnx2onnx_flow is still needed after
running this optimizaiton.

Args:

* m (ModelProto): the input onnx model
* disable_fuse_bn (bool, optional): do not fuse BN into Conv. Defaults to False.

#### General onnx optimization

```python
ktc.onnx_optimizer.onnx2onnx_flow(m, disable_fuse_bn=False, bn_on_skip=False, bn_before_add=False, bgr=False, norm=False, rgba2yynn=False, eliminate_tail=False)
```

Return the optimized model. Optimize the onnx model.

Args:

* m (ModelProto): the input onnx ModelProto
* disable_fuse_bn (bool, optional): do not fuse BN into Conv. Defaults to False.
* bn_on_skip (bool, optional): add BN operator on skip branches. Defaults to False.
* bn_before_add (bool, optional): add BN before Add node on every branches. Defaults to False.
* bgr (bool, optional): add an Conv layer to convert rgb input to bgr. Defaults to False.
* norm (bool, optional): add an Conv layer to add 0.5 tp the input. Defaults to False.
* rgba2yynn (bool, optional): add an Conv layer to convert rgb input to yynn . Defaults to False.
* eliminate_tail (bool, optional): remove the trailing NPU unsupported nodes. Defaults to False.

### 1.3 Editors

#### Delete specific nodes

```python
ktc.onnx_optimizer.delete_nodes(model, node_names)
```

Return the result onnx model. Delete nodes with the given names.

Args:

* model (onnx.ModelProto): the input onnx model.
* node_names (List[str]): a list of node names.

#### Delete specific inputs

```python
ktc.onnx_optimizer.delete_inputs(model, value_names)
```

Return the result onnx model. Delete specific inputs

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): inputs to delete.

#### Delete specific outputs

```python
ktc.onnx_optimizer.delete_outputs(model, value_names)
```

Return the result onnx model. Delete specific outputs

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): outputs to delete.

#### Cut the graph from the given node.

```python
ktc.onnx_optimizer.cut_graph_from_nodes(model, node_names)
```

Return the result onnx model. Cut the graph from the given node. The difference between this function and the
`delete_node` is that this function also delete all the following nodes after the specific nodes.

Args:

* model (onnx.ModelProto): the input onnx model.
* node_names (List[str]): a list of node names.

#### Cut the graph from the given operator type.

```python
ktc.onnx_optimizer.remove_nodes_with_types(model, type_names)
```

Return the result onnx model. Cut the graph from the nodes with specific operation types. Similar behaviour to
`cut_graph_from_nodes`.

Args:

* model (onnx.ModelProto): the input onnx model.
* type_names (List[str]): operator types to cut from.

#### Change input/output shapes

```python
ktc.onnx_optimizer.change_input_output_shapes(model, input_shape_mapping=None, output_shape_mapping=None)
```

Return the result onnx model. Change input shapes and output shapes.

Args:

* model (onnx.ModelProto): input onnx model.
* input_shape_mapping (Dict, optional): mapping from input names to the shapes to change. Defaults to None.
* output_shape_mapping (Dict, optional): mapping from output names to the shapes to change. Defaults to None.

#### Add do-nothing Conv nodes after specific values

```python
ktc.onnx_optimizer.add_conv_after(model, value_names)
```

Return the result onnx model. Add a do-nothing Conv node after the specific value.

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): values after which we add Conv.

#### Add do-nothing BN nodes after specific values

```python
ktc.onnx_optimizer.add_bn_after(model, value_names)
```

Return the result onnx model. Add a do-nothing BN node after the specific value.

Args:

* model (onnx.ModelProto): input onnx model.
* value_names (List[str]): values after which we add BN.

#### Rename an output

```python
ktc.onnx_optimizer.rename_output(model, old_name, new_name)
```

Return the result onnx model. Rename the specific output

Args:

* model (onnx.ModelProto): input onnx model.
* old_name (str): old output name.
* new_name (str): new output name.

## 2 Toolchain Utilities

This section mainly contains the API manual of analyser, compiler and IP evaluator.

### 2.1 Model Config

To start using the the toolchain utilities, one must first initilize an `ModelConfig` object.

```python
class ktc.ModelConfig(self, id, version, platform, onnx_model=None, onnx_path=None, bie_path=None)
```

Create an Kneron model config object. One of these three parameters is required: onnx_model, onnx_path, bie_path.

Args:

* id (int): model ID
* version (str): version number which should be a four digit hex, e.g. "0a2f"
* platform (str): hardware platform, should be "520" or "720"
* onnx_model (ModelProto, optional): loaded onnx model. Defaults to None.
* onnx_path (str, optional): onnx file path. Defaults to None.
* bie_path (str, optional): bie file path. Defaults to None.


### 2.2 Model Analysis

`analysis` is a public class function of class `ModelConfig`.

```python
classmethod analysis(input_mapping, output_bie=None, threads=4, quantize_mode="default")
```

Fix point analysis for the model. If the object is initialized with an onnx. This step is required before compiling. The result bie path will be returned.

Args:

* input_mapping (Dict): Dictionary of mapping input data to a specific input. Input data should be a list of numpy array.
* output_bie (str, optional): path to the output bie file. Defaults to "/data1/output.bie".
* threads (int, optional): multithread setting. Defaults to 4.
* quantize_mode (str, optional): quantize_mode setting. Currently support default and post_sigmoid. Defaults to "default".
* outlier (float, optional): remove outliers when calculating max & min. It should be between 0 and 1.0. Defaults to 0.999.

### 2.3 Model Evaluation

`evaluate` is a public class function of class `ModelConfig`.

```python
classmethod evaluate()
```

Return the evaluation result as `str`. The IP evaluator gives an estimation of the model running performance. It can run
with either onnx or bie. In other words, One can run it without running `analysis(...)`.

### 2.4 Compiler

The compile functions serve the same purpose as the batch compiler in the toolchain manual. The nef file path will be
returned from both function

```python
ktc.compile(model_list, output_dir=None, dedicated_output_buffer=True)
```

Compile the models and generate the nef file. The nef path will be returned.

Args:

* model_list (List[ModelConfig]): a list of models need to be compile. Models with onnx should run analysis() before compilation.
* output_dir (str, optional): output directory. Defaults to None.
* dedicated_output_buffer (bool, optional): dedicated output buffer. Defaults to True.

```python
ktc.encrypt_compile(model_list, output_dir=None, dedicated_output_buffer=True, mode=None, key="", key_file="", encryption_efuse_key="")
```
Compile the models, generate an encrypted nef file. The nef path will be returned.

Args:

* model_list (List[ModelConfig]): a list of models need to be compile. Models with onnx should run analysis() before compilation.
* output_dir (str, optional): output directory. Defaults to None.
* dedicated_output_buffer (bool, optional): dedicated output buffer. Defaults to True.
* mode (int, optional): There are two modes: 1, 2. Defaults to None, which is no encryption and acts the same as `ktc.compile`.
* key (str, optional): a hex code. Required in mode 1 Defaults to "".
* key_file (str, optional): key file path. Required in mode 1. Defaults to "".
* encryption_efuse_key (str, optional): a hex code. Required in mode 2 and optional in mode 1. Defaults to "".


## 3 Inferencer

Inferencer can be called through `ktc.kneron_inference(...)`. The usage is the same as in the E2E simulator. Please check its document for details.

By the way, for one who wondering what the radix should be, we provide a function to get radix from the input files.

#### Get radix

```python
ktc.get_radix(inputs)
```

Get the radix value from the given inputs.

Args:

* inputs (List): a list of numpy arrays which could be the inputs of the target model.

Raises:
* `ValueError`: raise if the input values are out of range
