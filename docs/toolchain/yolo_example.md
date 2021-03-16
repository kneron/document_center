# YOLOv3 Step by Step

In this document, we provide a step by step example on how to utilize our tools to compile and test with a newly downloaded YOLOv3 model.

## Step 0: Prepare environment and data

We need to download the latest toolchain docker image which contains all the tools we need. The following command helps you get the latest toolchain image. If you already have it locally, you can also use the same command to update the toolchain. Our toolchain will be updated monthly with new feature and important bug fixes. Note that for linux user, you may need `sudo` before the `docker` commands.

```bash
docker pull kneron/toolchain:latest
```

The following command start the docker with a local folder mounted into the docker:

```bash
docker run --rm -it -v /home/ps/docker_mount:/docker_mount kneron/toolchain:520
```

And after that, we go to our mounted folder and download a public keras based YOLOv3 model from Github <https://github.com/qqwweee/keras-yolo3>

```bash
cd /docker_mount && git clone https://github.com/qqwweee/keras-yolo3.git
```

## Step 1: Convert and optimize the downloaded model

First, we follow the model's document to save the model as an `h5` model:

```bash
cd keras-yolo3
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights /docker_mount/yolo.h5
```

We now have `yolo.h5` under our mounted folder `/docker_mount`.

You can check it with [Netron](https://netron.app/) to see it network structure.

We could find this model has no input shape. Thus, this cannot be done through the simplify `converter.py` mentioned in the toolchain manual. We need to specify the input shape while doing the conversion. This could be achieved using the `keras-onnx` tool under our `ONNX_Converter` with `-I` flag specify the input size (in this example, 1 224 224 3). The onnx file will be generated under the mounted folder.

```bash
python /workspace/libs/ONNX_Convertor/keras-onnx/generate_onnx.py /data1/yolo.h5 -o /data1/yolo.onnx -I 1 224 224 3
```

To finish this step, we should optimize it with `onnx2onnx.py` tool to make it compatible and efficient for our hardware.

```bash
python /workspace/libs/ONNX_Convertor/optimizer_scripts/onnx2onnx.py /data1/yolo.onnx -o /data1/yolo.opt.onnx -t
```

Now, we have `/data1/yolo.opt.onnx`. This is the model which we would use in the following steps.

## Step 2: Quantize and batch compile

Follow the toolchain manual document (<http://doc.kneron.com/docs/#toolchain/manual_520/>) section 3.2. Kneron Toolchain need `input_params.json`.

For the preprocess method, we can check the original project. From <https://github.com/qqwweee/keras-yolo3/blob/master/yolo.py>, we can find the following code.

<div align="center">
<img src="../imgs/yolo_example/keras_2_preprocess.png">
<p><span style="font-weight: bold;">Figure 2.1.</span> Original model preprocess</p>
</div>

From the manual section FAQ question 1, we know we should use `yolo` as the preprocess method and `7` for the radix. Then, here we have the json file:

```json
{
    "model_info": {
        "input_onnx_file": "/data1/yolov5s_e.onnx",
        "model_inputs": [{
            "model_input_name": "input_1_o0" ,
            "input_image_folder": "/data1/100_image/yolov5",
        }],
        "quantize_mode": "default"
    },
    "preprocess": {
        "img_preprocess_method": "yolo",
        "img_channel": "RGB",
        "radix": 7
    }
}
```

Then do quantization and compiling with 4 threads.

```bash
python /workspace/scripts/fpAnalyserCompilerIpevaluator_520.py -c /data1/input_params.json -t 4
```

## Step 3: Batch compile

https://www.kneron.com/forum/discussion/53/example-keras-kl520-how-to-convert-and-compile-tiny-yolo-v3-from-github-project#latest

## Step 4: Using the E2E Simulator

Now, we will go over a specific example on how to port a model that you have into the E2E Simulator to be run. Specifically, it is the yolov3 model found here https://github.com/qqwweee/keras-yolo3.

## 0. Initialization
You want to start the docker image to access the e2e-simulator. 
```
docker run --rm -it -v /mnt/docker:/docker_mount kneron/toolchain:latest
```

You will also want to be in e2e-simulator directory for this tutorial.
```
cd E2E_Simulator
```

## 1. Setup
First, we need to setup our application.

### 1.1 Application
Copy the template app and name it anything you would like. For this example, let's call it yolo.
```
cp -r app/template_app app/yolo
```

### 1.2 Yolo data
Clone the public yolov3 model repo to get the preprocess and postprocess functions that we need. We rename the cloned directory to allow for valid Python imports later.
```
cd app/yolo && git clone https://github.com/qqwweee/keras-yolo3.git && cd ../.. && mv app/yolo/keras-yolo3 app/yolo/keras_yolo3
```

## 2. Model files
In this tutorial, we will be running Dynasty float as our inferencer. To do so, we need to get the ONNX file to use as input. We first get the h5 Keras model.
```
cd app/yolo/keras_yolo3 && wget https://pjreddie.com/media/files/yolov3.weights && python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```

Now, we use the converter to convert the Keras model into an ONNX model.
```
python /workspace/libs/ONNX_Convertor/keras-onnx/generate_onnx.py model_data/yolo.h5 -o yolo.onnx -O --duplicate-shared-weights -I 1 416 416 3
```

Now, we use the optimizer to get the ONNX model to use as our input. We will save it in the base folder of our application for our test.
```
python /workspace/libs/ONNX_Convertor/optimizer_scripts/onnx2onnx.py yolo.onnx -o ../yolo.onnx -t && cd ..
```

## 3. Process functions
Now, we need to setup our preprocess and postprocess functions to be called. The preprocess and postprocess code are in the public yolo repository, but to call it, it must follow the E2E Simulator API.

### 3.1 Preprocess
The preprocess code can be found in lines 105-117 in "app/yolo/keras_yolo3/yolo.py". Let us copy this into our template preprocess Python file in our preprocess function. Additionally, we will need to add some imports to make the code work.
```
import numpy as np
from keras_yolo3.yolo3.utils import letterbox_image
from PIL import Image
```

We will also need to cleanup the variables being called to match the API. There is no predefined image size, so we can remove the if/else statement. Additionally, the image is passed through the config as a Pathlib path to the image, so we also need to load the image ourselves. Our returned value should be the preprocessed data in a list, and a dictionary to be passed to the postprocess if necessary. The preprocess function should look like the following:
```
def preprocess(config, prev_output):
    image = Image.open(config["flow"]["image_file"][0])
    new_image_size = (416, 416)  # to match our model input size when converting above
    boxed_image = letterbox_image(image, new_image_size)
    image_data = np.array(boxed_image, dtype='float32')

    print(image_data.shape)
    image_data /= 255.
    image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

    post_dict = {
        "image_shape": [image.size[1], image.size[0]]
    }
    return [image_data], post_dict
```

<div align="center">
<img src="../imgs/yolo_example/preprocess.png">
<p><span style="font-weight: bold;">Figure 1.</span> preprocess.py</p>
</div>

### 3.2 Postprocess
The postprocess function we will use can be found in the yolo_eval function in "app/yolo/keras_yolo3/yolo3/model.py". We will need to prepare the inputs and call the function in our postprocess function.

First, let us set up the imports and the environment. We will need to add the public yolo repository that we cloned into our path for the imports to their function calls to work.
```
import pathlib
import sys
import numpy as np
import tensorflow as tf
sys.path.append(str(pathlib.Path("app/yolo/keras_yolo3").resolve()))
from yolo3.model import yolo_eval
```

Next, we modify the postprocess function itself. First, we need to get the model inference results. Since the input to their postprocess function is a list of tensors, we need to convert our NumPy results into tensors.
```
    new_data = [tf.convert_to_tensor(data, dtype=tf.float32) for data in inf_results]
```

Next, let's prepare the anchors. We will load them in the same way as in the get_anchors function in "app/yolo/keras_yolo3/yolo.py".
```
    anchors_path = "app/yolo/keras_yolo3/model_data/yolo_anchors.txt"
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    anchors = np.array(anchors).reshape(-1, 2)
```

Finally, we need to get the number of classes and the image size. In their code, they load the number of classes from their text file. It is a static value, so, for simplicity, let us simply set the value. We can get the image size from our input dictionary passed from the result of our preprocess function.
```
    num_classes = 80
    image_shape = pre_data["image_shape"]
```

Now, we can feed it all into the postprocess function and get the results.
```
    boxes, scores, classes = yolo_eval(new_data, anchors, num_classes, image_shape)
    with tf.Session() as sess:
        boxes = boxes.eval()
        scores = scores.eval()
        classes = classes.eval()
    
    return boxes, scores, classes
```

<div align="center">
<img src="../imgs/yolo_example/postprocess.png">
<p><span style="font-weight: bold;">Figure 2.</span> postprocess.py</p>
</div>

## 4. Input JSONs
Next, we will need to prepare the input JSON to configure our testing environment. Navigate to the app/yolo/input_jsons folder, and you will notice a JSON file called example.json. You may rename it as you wish, but we will leave it as example.json for this example.

### 4.1 Pre and post
First, we will need to fill in the [pre][pre_type] and [post][post_type] parameters. These should be relative Python imports using the 'yolo' folder as the working directory. In our case, the preprocess function was called preprocess at (preprocess.py, and the postprocess function was called postprocess at postprocess.py. Set the [pre][pre_type] and [post][post_type] to the following:
```
"pre_type": "preprocess.preprocess"
"post_type": "postprocess.postprocess"
```

### 4.2 Emu
Now, we need to configure the inferencer we wish to call. As mentioned earlier, we are using the Dynasty float inferencer for this tutorial, so let's set the emu_mode to "float". Let's also set the model_type to "yolo" to match the model we are testing.
```
"emu_mode": "float"
"model_type": "yolo"
```

Now, we only need to modify the section related to the "float" inferencer. First, we need to fill in "onnx_file" with the path to the model we saved earlier in step 2. For the Dynasty inferencer to work, we also need to find the input node names for this model. You can use something like [Netron](https://netron.app/) to check this. After doing so, we can see that the input node name is input_1_o0.
```
"onnx_file": "yolo.onnx"
"onnx_input": ["input_1_o0"]
```

It will look like this in the end:
<div align="center">
<img src="../imgs/yolo_example/json.png">
<p><span style="font-weight: bold;">Figure 3.</span> example.json</p>
</div>

## 5.0 Flow.py
The last step is modifying "flow.py" to setup the testing flow.

### 5.1 Adding JSON files
For the simulator to know about the JSON file we configured earlier, we set the path in the "user_config" dictionary. The key should be anything you want to access the corresponding JSON file; let's call our key "yolo_json". The path value should be relative to the base of the app folder, "yolo/", or an absolute path. You will also need to remove the example key, as it will check for the existence of the value file.

Add the following key, value pair to user_config:
```
    "yolo_json": "input_jsons/example.json"
```

### 5.2 Modifying flow function
Let's first modify the function name into something more descriptive; this is also our last command line argument to run the test. Call it "test_yolo".
```
def test_yolo(file_names, user_config):
```

Now, we need to modify the function itself. For each model in the testing flow, you will need to call "flow.run_simulator" once. In this tutorial, we are only testing the yolo model, so we call it once. Any additional computations can be done here if necessary, but let us just print our results from the postprocess function. In addition, the optional returned dictionary will be saved into a file, so let us save the boxes, scores, and classes.
```
    my_result = flow.run_simulator(user_config["yolo_json"], file_names)
    print(my_result)
    return {
        "boxes": my_result[0],
        "scores": my_result[1],
        "classes": my_result[2]
    }
```

<div align="center">
<img src="../imgs/yolo_example/flow.png">
<p><span style="font-weight: bold;">Figure 4.</span> flow.py</p>
</div>

## 6.0 Running the test
Now, everything is prepared, and we can run the test. We have prepared a test dataset of one image for example usage; it can be found at app/test_image_folder/yolo. To run the command, we need three inputs: the path to your app, the path to the image directory, and the name of the function in flow.py to run. In this example, the inputs are app/yolo, app/test_image_folder/yolo, and test_yolo. Be sure that you are in the base directory of the e2e-simulator to run the test. Put it all together in a call to simulator.py, and you get:
```
python3 simulator.py app/yolo app/test_image_folder/yolo test_yolo -d
```

### 6.1 Viewing dumps
We can now view all of the files dumped as a result of the test. To find them, we just need to follow the same path as our test image directory under the bin/out folder. Thus, we can find our results at bin/out/test_image_folder/yolo/000000350003.jpg/. Here, for your reference, you can find various binary or text files used as input. You will also notice a file called "result.json"; this will have the dictionary you returned in the flow function saved in JSON format.

