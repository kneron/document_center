# Step 1: Environment

## Step 1-1: Prerequisites

- Python 3.6+
- PyTorch 1.3+ (We recommend you installing PyTorch using Conda following the [Official PyTorch Installation Instruction](https://pytorch.org/))
- (Optional) CUDA 9.2+ (If you installed PyTorch with cuda using Conda following the [Official PyTorch Installation Instruction](https://pytorch.org/), you can skip CUDA installation)
- (Optional, used to build from source) GCC 5+
- [mmcv-full](https://mmcv.readthedocs.io/en/latest/#installation) (Note: not `mmcv`!)

**Note:** You need to run `pip uninstall mmcv` first if you have `mmcv` installed.
If mmcv and mmcv-full are both installed, there will be `ModuleNotFoundError`.

## Step 1-2: Install kneron-mmsegmentation

### Step 1-2-1: Install PyTorch

You can follow [Official PyTorch Installation Instruction](https://pytorch.org/) to install PyTorch using Conda:

```shell
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch -y
```

### Step 1-2-2: Install mmcv-full

We recommend you installing mmcv-full using pip:

```shell
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html
```

Please replace `cu113` and `torch1.11.0` in the url to your desired one. For example, to install the `mmcv-full` with `CUDA 11.1` and `PyTorch 1.9.0`, use the following command:

```shell
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html
```

If you see error messages while installing mmcv-full, please check if your installation instruction matches your installed version of PyTorch and Cuda, and see [MMCV pip Installation Instruction](https://github.com/open-mmlab/mmcv#install-with-pip) for different versions of MMCV compatible to different PyTorch and CUDA versions.

### Step 1-2-3: Clone kneron-mmsegmentation Repository

```shell
git clone https://github.com/kneron/kneron-mmsegmentation.git
cd kneron-mmsegmentation
```

### Step 1-2-4: Install Required Python Libraries for Building and Installing kneron-mmsegmentation

```shell
pip install -r requirements_kneron.txt
pip install -v -e .  # or "python setup.py develop"
```

# Step 2: Training Models on Standard Datasets 

kneron-mmsegmentation provides many existing and existing semantic segmentation models in [Model Zoo](https://mmsegmentation.readthedocs.io/en/latest/model_zoo.html), and supports several standard datasets like CityScapes, Pascal Context, Coco Stuff, ADE20K, etc. Here we demonstrate how to train *STDC-Seg*, a semantic segmentation algorithm, on *CityScapes*, a well-known semantic segmentation dataset.

## Step 2-1: Download CityScapes Dataset

1. Go to [CityScapes Official Website](https://www.cityscapes-dataset.com) and click *Download* link on the top of the page. If you're not logged in, it will navigate you to login page.
2. If it is the first time you visiting CityScapes website, to download CityScapes dataset, you have to register an account.
3. Click the *Register* link and it will navigate you to the registeration page.
4.  Fill in all the *required* fields, accept the terms and conditions, and click the *Register* button. If everything goes well, you will see *Registration Successful* on the page and recieve a registration confirmation mail in your email inbox.
5.  Click on the link provided in the confirmation mail, login with your newly registered account and password, and you should be able to download the CityScapes dataset.
6. Download *leftImg8bit_trainvaltest.zip* (images) and *gtFine_trainvaltest.zip* (labels) and place them onto your server.

## Step 2-2: Dataset Preparation

We suggest that you extract the zipped files to somewhere outside the project directory and symlink (`ln`) the dataset root to `kneron-mmsegmentation/data` so you can use the dataset outside this project, as shown below:

```shell
# Replace all "path/to/your" below with where you want to put the dataset!

# Extracting Cityscapes
mkdir -p path/to/your/cityscapes
unzip leftImg8bit_trainvaltest.zip -d path/to/your/cityscapes
unzip gtFine_trainvaltest.zip -d path/to/your/cityscapes

# symlink dataset to kneron-mmsegmentation/data  # where "kneron-mmsegmentation" is the repository you cloned in step 0-4
mkdir -p kneron-mmsegmentation/data
ln -s $(realpath path/to/your/cityscapes) kneron-mmsegmentation/data

# Replace all "path/to/your" above with where you want to put the dataset!
```

Then, we need *cityscapesScripts* to preprocess the CityScapes dataset. If you completely followed our [Step 1-2-4](#step-1-2-4-install-required-python-libraries-for-building-and-installing-kneron-mmsegmentation), you should have python library *cityscapesScripts* installed (if no, execute `pip install cityscapesScripts` command).

```shell
# Replace "path/to/your" with where you want to put the dataset!
export CITYSCAPES_DATASET=$(realpath path/to/your/cityscapes)
csCreateTrainIdLabelImgs
```

Wait several minutes and you'll see something like this:

```plain
Processing 5000 annotation files
Progress: 100.0 %
```

The files inside the dataset folder should be something like:

```plain
kneron-mmsegmentation/data/cityscapes
├── gtFine
│   ├── test
│   │   ├── ...
│   ├── train
│   │   ├── ...
│   ├── val
│   │   ├── frankfurt
│   │   │   ├── frankfurt_000000_000294_gtFine_color.png
│   │   │   ├── frankfurt_000000_000294_gtFine_instanceIds.png
│   │   │   ├── frankfurt_000000_000294_gtFine_labelIds.png
│   │   │   ├── frankfurt_000000_000294_gtFine_labelTrainIds.png
│   │   │   ├── frankfurt_000000_000294_gtFine_polygons.png
│   │   │   ├── ...
│   │   ├── ...
├── leftImg8bit
│   ├── test
│   │   ├── ...
│   ├── train
│   │   ├── ...
│   ├── val
│   │   ├── frankfurt
│   │   │   ├── frankfurt_000000_000294_leftImg8bit.png
│   │   ├── ...
...
```

It's recommended that you *symlink* the dataset folder to mmdetection folder. However, if you place your dataset folder at different place and do not want to symlink, you have to change the corresponding paths in the config file.

Now the dataset should be ready for training.


## Step 2-3: Train STDC-Seg on CityScapes

Short-Term Dense Concatenate Network (STDC network) is a light-weight network structure for convolutional neural network. If we apply this network structure to semantic segmentation task, it's called STDC-Seg. It's first introduced in [Rethinking BiSeNet For Real-time Semantic Segmentation
](https://arxiv.org/abs/2104.13188). Please check the paper if you want to know the algorithm details.

We only need a configuration file to train a deep learning model in either the original MMSegmentation or kneron-mmsegmentation. STDC-Seg is provided in the original MMSegmentation repository, but the original configuration file needs some modification due to our hardware limitation so that we can apply the trained model to our Kneron dongle. 

To make a configuration file compatible with our device, we have to:

* Change the mean and std value in image normalization to `mean=[128., 128., 128.]` and `std=[256., 256., 256.]`.
* Shrink the input size during inference phase. The original CityScapes image size is too large (2048(w)x1024(h)) for our device; 1024(w)x512(h) might be good for our device.

To achieve this, you can modify the `img_scale` in `test_pipeline` and `img_norm_cfg` in the configuration file `configs/_base_/datasets/cityscapes.py`. 

Luckily, here in kneron-mmsegmentation, we provide a modified STDC-Seg configuration file (`configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py`) so we can easily apply the trained model to our device.

To train STDC-Seg compatible with our device, just execute:

```shell
cd kneron-mmsegmentation
python tools/train.py configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py
```

kneron-mmsegmentation will generate `work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes` folder and save the configuration file and all checkpoints there.

# Step 3: Test Trained Model
`tools/test.py` is a script that generates inference results from test set with our pytorch model and evaluates the results to see if our pytorch model is well trained (if `--eval` argument is given). Note that it's always good to evluate our pytorch model before deploying it.

```shell
python tools/test.py \
    work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py \
    work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.pth \
    --eval mIoU
```
* `kn_stdc1_in1k-pre_512x1024_80k_cityscapes/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py` can be your training config.
* `kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.pth` can be your model checkpoint.

The expected result of the command above should be something similar to the following text (the numbers may slightly differ):
```
...
+---------------+-------+-------+
|     Class     |  IoU  |  Acc  |
+---------------+-------+-------+
|      road     | 97.49 | 98.59 |
|    sidewalk   | 80.17 | 88.71 |
|    building   | 89.52 | 95.25 |
|      wall     | 57.92 | 66.99 |
|     fence     |  55.5 | 70.15 |
|      pole     | 38.93 | 47.51 |
| traffic light | 49.95 | 59.97 |
|  traffic sign |  62.1 | 70.05 |
|   vegetation  | 89.02 | 95.27 |
|    terrain    | 60.18 | 72.26 |
|      sky      | 91.84 | 96.34 |
|     person    | 68.98 | 84.35 |
|     rider     | 47.79 | 60.98 |
|      car      | 91.63 | 96.48 |
|     truck     | 74.31 | 83.52 |
|      bus      | 80.24 | 86.83 |
|     train     | 66.45 | 76.78 |
|   motorcycle  | 48.69 | 58.18 |
|    bicycle    | 65.81 | 81.68 |
+---------------+-------+-------+
Summary:

+------+-------+-------+
| aAcc |  mIoU |  mAcc |
+------+-------+-------+
| 94.3 | 69.29 | 78.42 |
+------+-------+-------+
```

**NOTE: The training process might take some time, depending on your computation resource. If you just want to take a quick look at the deployment flow, you can download our pretrained model so you can skip Step 1, 2, and 3:**
```
# If you don't want to train your own model:
mkdir -p work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes
pushd work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes
wget https://github.com/kneron/Model_Zoo/raw/main/mmsegmentation/stdc_1/latest.zip
unzip latest.zip
popd
```

# Step 4: Export ONNX and Verify

## Step 4-1: Export ONNX

`tools/pytorch2onnx_kneron.py` is a script provided by kneron-mmsegmentation to help users to convert our trained pytorch model to ONNX:
```shell
python tools/pytorch2onnx_kneron.py \
    configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py \
    --checkpoint work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.pth \
    --output-file work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.onnx \
    --verify
```
* `configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py` can be your training config.
* `work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.pth` can be your model checkpoint.
* `work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.onnx` can be any other path. Here for convenience, the ONNX file is placed in the same folder of our pytorch checkpoint.

## Step 4-2: Verify ONNX

`tools/deploy_test_kneron.py` is a script provided by kneron-mmsegmentation to help users to verify if our exported ONNX generates similar outputs with what our PyTorch model does:
```shell
python tools/deploy_test_kneron.py \
    configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py \
    work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.onnx \
    --eval mIoU
```
* `configs/stdc/kn_stdc1_in1k-pre_512x1024_80k_cityscapes.py` can be your training config.
* `work_dirs/kn_stdc1_in1k-pre_512x1024_80k_cityscapes/latest.pth` can be your exported ONNX file.

The expected result of the command above should be something similar to the following text (the numbers may slightly differ):

```
...
+---------------+-------+-------+
|     Class     |  IoU  |  Acc  |
+---------------+-------+-------+
|      road     | 97.52 | 98.62 |
|    sidewalk   | 80.59 | 88.69 |
|    building   | 89.59 | 95.38 |
|      wall     | 58.02 | 66.85 |
|     fence     | 55.37 | 69.76 |
|      pole     |  44.4 | 52.28 |
| traffic light | 50.23 | 60.07 |
|  traffic sign | 62.58 | 70.25 |
|   vegetation  |  89.0 | 95.27 |
|    terrain    | 60.47 | 72.27 |
|      sky      | 90.56 | 97.07 |
|     person    |  70.7 | 84.88 |
|     rider     | 48.66 | 61.37 |
|      car      | 91.58 | 95.98 |
|     truck     | 73.92 | 82.66 |
|      bus      | 79.92 | 85.95 |
|     train     | 66.26 | 75.92 |
|   motorcycle  | 48.88 | 57.91 |
|    bicycle    |  66.9 |  82.0 |
+---------------+-------+-------+
Summary:

+------+-------+-------+
| aAcc |  mIoU |  mAcc |
+------+-------+-------+
| 94.4 | 69.75 | 78.59 |
+------+-------+-------+
```

Note that the ONNX results may differ from the PyTorch results due to some implementation differences between PyTorch and ONNXRuntime.

# Step 5: Convert ONNX File to [NEF](http://doc.kneron.com/docs/#toolchain/manual/#5-nef-workflow) Model for Kneron Platform
 
## Step 5-1: Install Kneron toolchain docker:

* Check [Kneron Toolchain Installation Document](http://doc.kneron.com/docs/#toolchain/manual/#1-installation)

## Step 5-2: Mount Kneron toolchain docker

* Mount a folder (e.g. '/mnt/hgfs/Competition') to toolchain docker container as `/data1`. The converted ONNX in Step 3 should be put here. All the toolchain operation should happen in this folder.
```
sudo docker run --rm -it -v /mnt/hgfs/Competition:/data1 kneron/toolchain:latest
```

## Step 5-3: Import KTC and the required libraries in python

```python
import ktc
import numpy as np
import os
import onnx
from PIL import Image
```

## Step 5-4: Optimize the onnx model

```python
onnx_path = '/data1/latest.onnx'
m = onnx.load(onnx_path)
m = ktc.onnx_optimizer.onnx2onnx_flow(m)
onnx.save(m,'latest.opt.onnx')
```

## Step 5-5: Configure and load data needed for ktc, and check if onnx is ok for toolchain
```python 
# npu (only) performance simulation
km = ktc.ModelConfig((&)model_id_on_public_field, "0001", "720", onnx_model=m)
eval_result = km.evaluate()
print("\nNpu performance evaluation result:\n" + str(eval_result))
```

## Step 5-6: Quantize the onnx model
We [sampled 3 images from Cityscapes dataset](https://www.kneron.com/tw/support/education-center/?folder=OpenMMLab%20Kneron%20Edition/misc/&download=41) (3 images) as quantization data. To test our quantized model:
1. Download the [zip file](https://www.kneron.com/tw/support/education-center/?folder=OpenMMLab%20Kneron%20Edition/misc/&download=41)
2. Extract the zip file as a folder named `cityscapes_minitest`
3. Put the `cityscapes_minitest` into docker mounted folder (the path in docker container should be `/data1/cityscapes_minitest`)

The following script will preprocess (should be the same as training code) our quantization data, and put it in a list:

```python
import os
from os import walk

img_list = []
for (dirpath, dirnames, filenames) in walk("/data1/cityscapes_minitest"):
    for f in filenames:
        fullpath = os.path.join(dirpath, f)
        
        image = Image.open(fullpath)
        image = image.convert("RGB")
        image = Image.fromarray(np.array(image)[...,::-1])
        img_data = np.array(image.resize((1024, 512), Image.BILINEAR)) / 256 - 0.5
        print(fullpath)
        img_list.append(img_data)
```

Then perform quantization. The generated BIE model will put generated at `/data1/output.bie`.

```python
# fixed-point analysis
bie_model_path = km.analysis({"input": img_list})
print("\nFixed-point analysis done. Save bie model to '" + str(bie_model_path) + "'")
```

## Step 5-7: Compile

The final step is compile the BIE model into an NEF model.
```python
# compile
nef_model_path = ktc.compile([km])
print("\nCompile done. Save Nef file to '" + str(nef_model_path) + "'")
```

You can find the NEF file at `/data1/batch_compile/models_720.nef`. `models_720.nef` is the final compiled model.
