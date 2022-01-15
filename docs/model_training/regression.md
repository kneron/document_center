# Lite-HRNet: A Lightweight High-Resolution Network

## Introduction
Pose estimation task with Lite-HRNet model.  

## Prerequisites
- Python 3.6 or above
- PyTorch 1.3 or above
- CUDA 9.2 or above 
- GCC 5+

**Important:** Please note that CUDA training is not supported in Kneron docker. You are expected to use your own GPUs and have correct cuda version installed. 

## Installation
For installing [Pytorch](https://pytorch.org), you have to check your CUDA version and select the correct [Pytorch version](https://pytorch.org/get-started/previous-versions/).
You can check your CUDA version by executing `nvidia-smi` in your terminal. For example, install Pytorch 1.7.0 with CUDA 11.0:

```bash
$ conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=11.0 -c pytorch
```

Install all necessary packages in the `requirements.txt`:

```bash
$ pip install -r requirements.txt
```

Install [mmcv](https://github.com/open-mmlab/mmcv) with the version 1.3.3:

```bash
$ pip install mmcv-full==1.3.3 -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
```

Replace `{cu_version}` and `{torch_version}` in the url to your desired versions. For example, to install mmcv-full==1.3.3 with CUDA 10.2 and PyTorch 1.6.0, use the following command:

```bash
pip install mmcv-full==1.3.3 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.6.0/index.html
```

See [here](https://github.com/open-mmlab/mmcv) for different versions of MMCV compatible to different PyTorch and CUDA versions.
**Important:** You need to run `pip uninstall mmcv` first if you have mmcv installed. If mmcv and mmcv-full are both installed, there will be `ModuleNotFoundError`.

## Dataset & Preparation

It is recommended to symlink the dataset root to `litehrnet/data`. To create symlink, run:

```bash
ln -s source_file symbolic_link
```

Replace `source_file` with the name of the existing file for which you want to create the symbolic link and `symbolic_link` with the name of the symbolic link.

If your folder structure is different, you may need to change the corresponding paths in config files.

**For COCO data**, please download from [COCO download](http://cocodataset.org/#download), 2017 Train/Val is needed for COCO keypoints training and validation. 
[HRNet-Human-Pose-Estimation](https://github.com/HRNet/HRNet-Human-Pose-Estimation) provides person detection result of COCO val2017 to reproduce the multi-person pose estimation results. Please download from [OneDrive](https://1drv.ms/f/s!AhIXJn_J-blWzzDXoz5BeFl8sWM-)
Download and extract them under `litehrnet/data`, and make them look like this:

```
lite_hrnet
├── configs
├── models
├── tools
`── data
    │── coco
        │-- annotations
        │   │-- person_keypoints_train2017.json
        │   |-- person_keypoints_val2017.json
        |-- person_detection_results
        |   |-- COCO_val2017_detections_AP_H_56_person.json
        │-- train2017
        │   │-- 000000000009.jpg
        │   │-- 000000000025.jpg
        │   │-- 000000000030.jpg
        │   │-- ...
        `-- val2017
            │-- 000000000139.jpg
            │-- 000000000285.jpg
            │-- 000000000632.jpg
            │-- ...

```

**For MPII data**, please download from [MPII Human Pose Dataset](http://human-pose.mpi-inf.mpg.de/).
The original annotation files have been converted into json format, please download them from [mpii_annotations](https://openmmlab.oss-cn-hangzhou.aliyuncs.com/mmpose/datasets/mpii_annotations.tar).
Extract them under `$LITE_HRNET/data`, and make them look like this:

```
lite_hrnet
├── configs
├── models
├── tools
`── data
    │── mpii
        |── annotations
        |   |── mpii_gt_val.mat
        |   |── mpii_test.json
        |   |── mpii_train.json
        |   |── mpii_trainval.json
        |   `── mpii_val.json
        `── images
            |── 000001163.jpg
            |── 000003072.jpg

```

## Modify MMPose for Kneron PPP

To use Kneron pre-post-processing during training and testing, you have to replace some files in the `mmpose` package in your python/anaconda env. You can use `python -m site` to check you env. Specific files are:

- `site-packages/mmpose/core/post_processing/post_transforms.py`
- `site-packages/mmpose/datasets/pipelines/top_down_transform.py`
- `site-packages/mmpose/datasets/pipelines/loading.py`
- `site-packages/mmpose/datasets/pipelines/shared_transform.py`

You may replace these files by the cooresponding files in the `mmpose_replacement` folder.

Moreover, you need copy and paste `prepostprocess/kneron_preprocessing/` to your python/anaconda env `site-packages`. 

## Train

A configuration file is needed for training of Lite-HRNet. We prepared several config files in `/litehrnet/configs/top_down/lite_hrnet` for different settings.

All outputs (log files and checkpoints) will be saved to the working directory, which is specified by `work_dir` as an optional argument (default: `/litehrnet/work_dirs/`).

By default, we evaluate the model on the validation set after each epoch, you can change the evaluation interval by modifying the `interval` argument in the config file `CONFIG_FILE`.

```bash
# train with a signle GPU
python train.py ${CONFIG_FILE} [optional arguments]
```

Optional arguments are:

- `CONFIG_FILE` (**required**) Path to config file.
- `--no-validate`: Not perform evaluation at every k epochs during the training.
- `--work-dir ${WORK_DIR}`: Override the working directory specified in the config file.
- `--gpus ${GPU_NUM}`: Number of gpus to use.
- `--gpu-ids`: IDs of gpus to use.
- `--deterministic`: If specified, it will set deterministic options for CUDNN backend.

Difference between `resume-from` and `load-from` in `CONFIG_FILE`:
`resume-from` loads both the model weights and optimizer status, and the epoch is also inherited from the specified checkpoint. It is usually used for resuming the training process that is interrupted accidentally.
`load-from` only loads the model weights and the training epoch starts from 0. It is usually used for finetuning.

## Convert to ONNX
To export onnx model, we have to modify a forward function in the `mmpose` package. 
The specific file is `site-packages/mmpose/models/detectors/top_down.py` in your python/anaconda env. You can use `python -m site` to check you env.
Change the `forward` function in line 81 from:

```bash
def forward(self,
            img,
            target=None,
            target_weight=None,
            img_metas=None,
            return_loss=True,
            return_heatmap=False,
            **kwargs):
    """Calls either forward_train or forward_test depending on whether
    return_loss=True. Note this setting will change the expected inputs.
    When `return_loss=True`, img and img_meta are single-nested (i.e.
    Tensor and List[dict]), and when `resturn_loss=False`, img and img_meta
    should be double nested (i.e.  List[Tensor], List[List[dict]]), with
    the outer list indicating test time augmentations.

    Note:
        batch_size: N
        num_keypoints: K
        num_img_channel: C (Default: 3)
        img height: imgH
        img width: imgW
        heatmaps height: H
        heatmaps weight: W

    Args:
        img (torch.Tensor[NxCximgHximgW]): Input images.
        target (torch.Tensor[NxKxHxW]): Target heatmaps.
        target_weight (torch.Tensor[NxKx1]): Weights across
            different joint types.
        img_metas (list(dict)): Information about data augmentation
            By default this includes:
            - "image_file: path to the image file
            - "center": center of the bbox
            - "scale": scale of the bbox
            - "rotation": rotation of the bbox
            - "bbox_score": score of bbox
        return_loss (bool): Option to `return loss`. `return loss=True`
            for training, `return loss=False` for validation & test.
        return_heatmap (bool) : Option to return heatmap.
    
    Returns:
        dict|tuple: if `return loss` is true, then return losses.
          Otherwise, return predicted poses, boxes, image paths
              and heatmaps.
    """
    if return_loss:
        return self.forward_train(img, target, target_weight, img_metas,
                                  **kwargs)
    return self.forward_test(
        img, img_metas, return_heatmap=return_heatmap, **kwargs)
```

to

```bash
def forward(self,
            img,
            target=None,
            target_weight=None,
            img_metas=None,
            return_loss=True,
            return_heatmap=False,
            **kwargs):
    """Calls either forward_train or forward_test depending on whether
    return_loss=True. Note this setting will change the expected inputs.
    When `return_loss=True`, img and img_meta are single-nested (i.e.
    Tensor and List[dict]), and when `resturn_loss=False`, img and img_meta
    should be double nested (i.e.  List[Tensor], List[List[dict]]), with
    the outer list indicating test time augmentations.

    Note:
        batch_size: N
        num_keypoints: K
        num_img_channel: C (Default: 3)
        img height: imgH
        img width: imgW
        heatmaps height: H
        heatmaps weight: W

    Args:
        img (torch.Tensor[NxCximgHximgW]): Input images.
        target (torch.Tensor[NxKxHxW]): Target heatmaps.
        target_weight (torch.Tensor[NxKx1]): Weights across
            different joint types.
        img_metas (list(dict)): Information about data augmentation
            By default this includes:
            - "image_file: path to the image file
            - "center": center of the bbox
            - "scale": scale of the bbox
            - "rotation": rotation of the bbox
            - "bbox_score": score of bbox
        return_loss (bool): Option to `return loss`. `return loss=True`
            for training, `return loss=False` for validation & test.
        return_heatmap (bool) : Option to return heatmap.

    Returns:
        dict|tuple: if `return loss` is true, then return losses.
          Otherwise, return predicted poses, boxes, image paths
              and heatmaps.
    """
    return self.forward_dummy(img)
```

Then, execute the following command under the directory `litehrnet`:

```bash
python export2onnx.py ${CONFIG_FILE} ${CHECKPOINT_FILE}
```

Next, pull the latest [ONNX converter](https://github.com/kneron/ONNX_Convertor/tree/master/optimizer_scripts) from github. You may read the latest document from Github for converting ONNX model. Execute commands in the folder `ONNX_Convertor/optimizer_scripts`:
(reference: https://github.com/kneron/ONNX_Convertor/tree/master/optimizer_scripts)

```bash
python pytorch2onnx.py input.pth output.onnx
```


## Inference

Before model inference, we assume that the model has been converted to onnx model as in the previous section.
Create yaml files containing the initial parameter information. Some yaml files are provided in `utils` folder. 
For model inference on a single image, execute commands under the folder `litehrnet`:

```bash
python inference.py --img-path ${IMAGE_PATH} --yolov5_params ${YOLOV5_INIT_PARAMS} --rsn_affine_params ${RSN_AFFINE_INIT_PARAMS} --lite_hrnet_params ${LITEHRNET_INIT_PARAMS}
```

## Evaluation
You can use the following commands to test a dataset.

```bash
# single-gpu testing
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [--out ${RESULT_FILE}] [--eval ${EVAL_METRIC}] [--average_clips ${AVG_TYPE}] 
```

Optional arguments:

- `CONFIG_FILE` (**required**) Path to config file.
- `CHECKPOINT_FILE` (**required**) Path to pretrained model.
- `RESULT_FILE`: Filename of the output results. If not specified, the results will not be saved to a file.
- `EVAL_METRIC`: Items to be evaluated on the results. Allowed values depend on the dataset, e.g., "mAP" for MSCOCO.
- `NUM_PROC_PER_GPU`: Number of processes per GPU. If not specified, only one process will be assigned for a single gpu.
- `AVG_TYPE`: Items to average the test clips. If set to `prob`, it will apply softmax before averaging the clip scores. Otherwise, it will directly average the clip scores.

## End-to-End Evaluation
If you would like to perform an end-to-end test with an image dataset, you can use `inference_e2e.py` under the directory `litehrnet` to obtain the prediction results. 
Here, yolov5 is used for detecting person bbox. You have to prepare an initial parameter yaml file for each model runner. You may check `utils/yolov5_init_params.yaml` for the format.

```bash
python inference_e2e.py --img-path ${IMAGE_PATH} --yolov5_params ${YOLOV5_INIT_PARAMS} --rsn_affine_params ${RSN_AFFINE_INIT_PARAMS} --lite_hrnet_params ${LITEHRNET_INIT_PARAMS} --save-path ${OUTPUT_JSON_FILE}
```

The predictions will be saved into a json file that has the following structure:

```bash
[
    {'img_path':image_path_1
    'lmk_coco_body_17pts': [...]
    },
    {'img_path':image_path_2
    'lmk_coco_body_17pts': [...]
    },
    ...
]
```

Note that your image path has to be the same as the image path in ground truth json. 

# Model

Backbone | Input Size |  FPS on 520 | FPS on 720  | Model Size | mAP
--- | --- |:---:|:---:|:---:|:---:
[litehrnet_no_shuffle_no_avgpool.py](https://github.com/kneron/Model_Zoo/blob/main/regression/litehrnet/lite_hrnet_no_shuffle_no_pool.pth) | 256x192 | 8.81063 | 119.38 | 8M | 87.4%