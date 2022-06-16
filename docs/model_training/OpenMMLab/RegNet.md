# Step 0. Environment

## Prerequisites

- Python 3.6+
- PyTorch 1.3+
- CUDA 9.2+ (If you built PyTorch from source, CUDA 9.0 is also compatible)
- (Optional, used to build from source) GCC 5+
- [mmcv-full](https://mmcv.readthedocs.io/en/latest/#installation) (Note: not `mmcv`!)

**Note:** You need to run `pip uninstall mmcv` first if you have `mmcv` installed.
If mmcv and mmcv-full are both installed, there will be `ModuleNotFoundError`.


## Install kneron-mmtracking

0. install extra dependencies for MOTChallenge evaluation:

    ```shell
    pip install git+https://github.com/JonathonLuiten/TrackEval.git
    ```

    (Note) python 3.7 sometimes fail to install this due to "`typing`" library, recommend you can try to:

    ```shell
    pip unstall typing
    ```

1. We recommend you installing mmcv-full with pip:

    ```shell
    pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
    ```

    Please replace `{cu_version}` and `{torch_version}` in the url to your desired one. For example, to install the `mmcv-full` with `CUDA 10.1` and `PyTorch 1.6.0`, use the following command:

    ```shell
    pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html
    ```

    See [here](https://github.com/open-mmlab/mmcv#install-with-pip) for different versions of MMCV compatible to different PyTorch and CUDA versions.

2. Clone the Kneron-version MMDetection (kneron-mmdetection) repository.

    ```bash
    git clone https://github.com/kneron/kneron-mmdetection
    cd kneron-mmdetection
    ```

3. Install required python packages for building kneron-mmdetection and then install kneron-mmdetection.

    ```shell
    pip install -r requirements/build.txt
    pip install -v -e .  # or "python setup.py develop"
    ```

4. Go back to the parent folder
    ```shell
    cd ..
    ```

4. Clone the Kneron-version MMTracking (kneron-mmtracking) repository.

    ```bash
    git clone https://github.com/kneron/kneron-mmtracking
    cd kneron-mmtracking
    ```

5. Install required python packages for building kneron-mmtracking and then install kneron-mmtracking.

    ```shell
    pip install -r requirements/build.txt
    pip install -v -e .  # or "python setup.py develop"
    ```

# Step 1: Train models on standard datasets 

MMTracking provides tracking models in [Model Zoo](https://github.com/open-mmlab/mmtracking/blob/master/docs/en/model_zoo.md)) and supports several standard datasets like MOT, CrowdHuman, etc. This note demonstrates how to perform common object detection tasks with these existing models and standard datasets, including:

- Use existing trained models to inference on given images.
- Evaluate existing trained models on standard datasets.
- Train models on standard datasets.

## Train Bytetrack on MOT and crowdhuman dataset

MMTracking provides out-of-the-box tools for training tracking models.
This section will show how to train models (under [configs](https://github.com/open-mmlab/mmtracking/tree/master/configs/mot)) on MOT and crowdhuman.

**Important**: You might need to modify the [config file](https://github.com/open-mmlab/mmtracking/blob/master/docs/en/tutorials/config_mot.md) according your GPUs resource (such as `samples_per_gpu`, `workers_per_gpu` ...etc due to your GPUs RAM limitation).
The default learning rate in config files is for 8 GPUs and 2 img/gpu (batch size = 8\*2 = 16).

### Step 1-1: Prepare MOT and crowdhuman dataset

[MOT](https://motchallenge.net/data/MOT17/), [crowdhuman](https://www.crowdhuman.org/) are available on official websites or mirrors.
We suggest that you download and extract the dataset to somewhere outside the project directory and symlink (`ln`) the dataset root to `$MMTRACKING/data` (`ln -s realpath/to/dataset $MMTracking/data/dataset`), as shown below:

```plain
mmtracking
├── mmtrack
├── tools
├── configs
├── data (this folder should be made beforehand)
│   ├── MOT17 (symlink)
│   │   ├── train
│   │   ├── test
│   ├── crowdhuman (symlink)
│   │   ├── train/val
│   │   │   ├── Images
...
```

It's recommended to *symlink* the dataset folder to mmtracking folder. However, if you place your dataset folder at different place and do not want to symlink, you have to change the corresponding paths in config files (absolute path is recommended).

### Step 1-2: Train Bytetrack on MOT and crowdhuman

[ByteTrack: Multi-Object Tracking by Associating Every Detection Box in 2021](https://arxiv.org/abs/2110.06864)

Before training, we need to prepare pretrained YoloX model as "`latest.pth`" in folder "`work_dirs`" due to our config will load pretrained weight here:
```bash
mkdir work_dirs
cd work_dirs
wget https://github.com/kneron/Model_Zoo/raw/main/mmdetection/yolox_s/latest.zip
unzip latest.zip
cd ..
```
Then, we only need the configuration file (which is provided in `configs/mot/bytetrack/`) to train Bytetrack: 
```python
python tools/train.py configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-train.py
```
* (Note) The whole training process might take several days, depending on your computational resource (number of GPUs, etc). If you just want to take a quick look at the deployment flow, we suggest that you download our trained model so you can skip the training process:
```bash
mkdir -p work_dirs
cd work_dirs
wget https://github.com/kneron/Model_Zoo/raw/main/mmtracking/bytetrack/latest.zip
unzip latest.zip
cd ..
```
* (Note) If you want to train a model on your custom dataset, it is recommended that you read [customize_dataset.md](https://github.com/open-mmlab/mmtracking/blob/master/docs/en/tutorials/customize_dataset.md).

# Step 2: Test trained pytorch model
`tools/test_kneron.py` is a script that generates inference results from test set with our pytorch model(or onnx model) and evaluates the results to see if our pytorch model(or onnx model) is well trained (if `--eval` argument is given). Note that it's always good to evluate our pytorch model before deploying it.

```python
python tools/test_kneron.py \
    configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-train.py \
    work_dirs/latest.pth \
    --eval bbox \
    --out results.pkl
```
* `configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-train.py` is your bytetrack training config
* `work_dirs/latest.pth` is your trained bytetrack model

The expected result of the command above will be something similar to the following text (the numbers may slightly differ):
```plain
...
+------------+--------+--------+--------+-------+
| class      | gts    | dets   | recall | ap    |
+------------+--------+--------+--------+-------+
| pedestrian | 161664 | 344382 | 0.881  | 0.838 |
+------------+--------+--------+--------+-------+
| mAP        |        |        |        | 0.838 |
+------------+--------+--------+--------+-------+
{'mAP': 0.838}
...
```

# Step 3: Export onnx
`tools/deployment/pytorch2onnx_kneron.py` is a script provided by Kneron to help user to convert our trained pth model to kneron-optimized onnx:
```python
python tools/deployment/pytorch2onnx_kneron.py \
    configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-deploy.py \
    work_dirs/latest.pth \
    --output-file work_dirs/latest.onnx \
    --skip-postprocess \
    --shape 448 800
```
* `configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-deploy.py` is your bytetrack deploy config
* `work_dirs/latest.pth` is your trained bytetrack model

The output onnx should be the same name as `work_dirs/latest.pth` with `.onnx` postfix in the same folder.

# Step 4: Test exported onnx model:
We use the same script(`tools/test_kneron.py`) in step 2 to test our exported onnx. The only difference is that instead of pytorch model, we use onnx model (`work_dirs/latest.onnx`).

```python
python tools/test_kneron.py \
    configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-deploy.py \
    --checkpoint work_dirs/latest.onnx \
    --eval bbox \
    --out results.pkl
```
* `configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-deploy.py` is your bytetrack deploy config
* `work_dirs/latest.onnx` is your exported bytetrack onnx model

The expected result of the command above will be something similar to the following text (the numbers may slightly differ):
```plain
...
+------------+--------+--------+--------+-------+
| class      | gts    | dets   | recall | ap    |
+------------+--------+--------+--------+-------+
| pedestrian | 161664 | 344382 | 0.881  | 0.838 |
+------------+--------+--------+--------+-------+
| mAP        |        |        |        | 0.838 |
+------------+--------+--------+--------+-------+
{'mAP': 0.838}
...
```

# Step 5: Convert onnx to [NEF](http://doc.kneron.com/docs/#toolchain/manual/#5-nef-workflow) model for Kneron platform
 
### Step 5-1: Install Kneron toolchain docker:
* Check [document](http://doc.kneron.com/docs/#toolchain/manual/#1-installation)

### Step 5-2: Mout Kneron toolchain docker 
* Mount a folder (e.g. '/mnt/hgfs/Competition') to toolchain docker container as `/data1`. The converted onnx in Step 3 should be put here. All the toolchain operation should happen in this folder.
```shell
sudo docker run --rm -it -v /mnt/hgfs/Competition:/data1 kneron/toolchain:latest
```

### Step 5-3: Import KTC and other required packages in python shell
* Here we demonstrate how to go through all Kneron Toolchain (KTC) flow through Python API:
```python
import ktc
import numpy as np
import os
import onnx
from PIL import Image
```

### Step 5-4: Optimize the onnx model
```python
onnx_path = '/data1/latest.onnx'
m = onnx.load(onnx_path)
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
onnx.save(m,'latest.opt.onnx')
```

### Step 5-5: Configure and load data necessary for ktc, and check if onnx is ok for toolchain
```python 
# npu (only) performance simulation
km = ktc.ModelConfig(20008, "0001", "720", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))
```

### Step 5-6: Quantize the onnx model
We [random sampled 50 images from voc dataset](https://www.kneron.com/forum/uploads/112/SMZ3HLBK3DXJ.7z) as quantization data, we have to
1. Download the data 
2. Uncompression the data as folder named `voc_data50"`
3. Put the `voc_data50` into docker mounted folder (the path in docker container should be `/data1/voc_data50`)

The following script will do some preprocess(should be the same as training code) on our quantization data, and put it in a list:
```python
import os
from os import walk

img_list = []
for (dirpath, dirnames, filenames) in walk("/data1/voc_data50"):
    for f in filenames:
        fullpath = os.path.join(dirpath, f)
        
        image = Image.open(fullpath)
        image = image.convert("RGB")
        image = Image.fromarray(np.array(image)[...,::-1])
        img_data = np.array(image.resize((800, 448), Image.BILINEAR)) / 256 - 0.5
        print(fullpath)
        img_list.append(img_data)
```

Then perform quantization. The BIE model will be generated at `/data1/output.bie`.

```python
# fixed-point analysis
bie_model_path = km.analysis({"input": img_list})
print("\nFixed-point analysis done. Saved bie model to '" + str(bie_model_path) + "'")
```

### Step 5-7: Compile
The final step is to compile the BIE model into an NEF model.
```python
# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Saved Nef file to '" + str(nef_model_path) + "'")
```

You can find the NEF file at `/data1/batch_compile/models_720.nef`. `models_720.nef` is the final compiled model.
