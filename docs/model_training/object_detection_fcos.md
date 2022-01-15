<h1 align="center">  Object Detection </h1>
Object Detection task with fcos model.  

This document contains the explanations of arguments of each script. 


You can find the tutorial for finetuning a pretrained model on custom dataset under the `tutorial` folder, `tutorial/README.md`. 


The ipython notebook tutorial is also prepared under the `tutorial` folder as `tutorial/tutorial.ipynb`. You may upload and run this ipython notebook on Google colab.

# Prerequisites
- Python = 3.6 or 3.7

# Installation
To install the dependencies, run
```
$ pip install -U pip
$ pip install -r requirements.txt
$ python setup.py build_ext --inplace
```

# Dataset & Preparation

## Standard Datasets
Our traning script accepts standard PASCAL VOC dataset and MS COCO dataset. You may download the dataset using the following link:

- Download [2012 PASCAL VOC Dataset](http://host.robots.ox.ac.uk/pascal/VOC/) 
- Download [2017 MS COCO Dataset](https://cocodataset.org/#download) 

## Custom Datasets
You can also train the model on a custom dataset. The custom dataset is expected to follow the YOLO format. You may visit yolov5 document for more details. 

### Annotation Tools
You can use [makesense.ai](https://www.makesense.ai) to create bounding boxes and labels for your images. For more details, you may visit [makesense.ai](https://www.makesense.ai) and check their documents. An example of using [makesense.ai](https://www.makesense.ai) to annotate custom data is also provided in the tutorial document. 

### dataset.yaml
For COCO dataset, you need to prepare the yaml file and save it under `./data/coco.yaml`. The yaml file is expected to have the following format:

```shell
data_root: path to coco dataset dirtory 

# type of dataset
dataset_type: coco

val_set_name: val2017
train_set_name: train2017
train_annotations_path: path to coco training annotations path   
val_annotations_path: path to coco training validation path

```

For Pascal VOC dataset, you need to prepare the yaml file and save it under `./data/pascal.yaml`. The yaml file is expected to have the following format:

```shell
data_root: path_to_voc_dataset/VOCdevkit/VOC2012
train: 'trainval'
val: 'val'

# type of dataset
dataset_type: pascal

```

For custom dataset, you need to prepare the yaml file and save it under `./data/`. The yaml file is expected to have the following format (same as yolov5):

```shell
train: path to training dataset directory 
val: path to validation dataset directory   

nc: number of class

names: list of class names
```

# Train 

All outputs (log files and checkpoints) will be saved to the snapshot directory,
which is specified by `--snapshot-path`. For training, execute the following command in `fcos` directory:
```shell
python train.py --backbone backbone_model_name --snapshot path_to_pretrained_model --freeze-backbone --batch-size 4 --gpu 0 --data path_to_data_yaml_file 
```

`--backbone` Which backbone model to use. 

`--snapshot` The path to pretrained model
 
`--freeze-backbone` Whether freeze the backbone when the pretrained model is used (True/False)

`--gpu` Which gpu to run. (-1 if cpu)

`--batch-size` Batch size. (Default: 4)

`--epochs` Number of epochs to train. (Default: 100)

`--steps` Number of steps per epoch. (Default: 5000)

`--lr` Learning rate. (Default: 1e-4)

`--fpn` The type of fpn model. Options: bifpn, dla, fpn, pan, simple (Default: simple) (Recommend: simple or pan)

`--reg-func` The type of regression function. Options: exp, simple (Default: simple)

`--stage` The num of stages. Options: 3, 5 (Default: 3)

`--head-type` The type of head. Options: ori, simple (Default: simple) 

`--centerness-pos` Centerness branch position. Options: cls, reg (Default: reg) 

`--snapshot-path` Path to store snapshots of models during training (Default: 'snapshots/{}'.format(today))

`--input-size` Input size of the model (Default: (512, 512))

`--data` The path to data yaml file

When the validation mAP stops increasing for 5 epochs, the early stopping will be triggered and the training process will be terminated. 

# Inference 

For model infernce on a single image:

```bash
python inference.py --snapshot path_to_pretrained_model --input-shape model_input_size --gpu 0  --class-id-path path_to_class_id_mapping_file --img-path path_to_image --save-path path_to_saved_image
```

`--snapshot` the path to pretrained model

`--gpu` which gpu to run. (-1 if cpu) (Default: -1)

`--input-shape` Input shape of the model (Default: (512, 512))

`--class-id-path` Path to the class id mapping file.

`--img-path` Path to the image.

`--save-path` Path to draw and save the image with bbox.

`--save-preds-path` Path to save the inference bbox results.

`--class-id-path` Path to the class id mapping file. (Default: COCO class id mapping)

`--max-objects` The maximum number of objects in the image. (Default: 100)

`--score-thres` The score threshold of bounding boxes. (Default: 0.6)

`--iou-thres` the iou threshold for NMS. (Default: 0.5) 

`--max-objects` Whether use Non-maximum Suppression (Default: 1)

You could find preprocessing and postprocessing processes in `fcos/utils/fcos_det_preprocess.py` and `fcos/utils/fcos_det_postprocess.py`.

# Convert to ONNX

Pull the latest [ONNX converter](https://github.com/kneron/ONNX_Convertor/tree/master/keras-onnx) from github. You may read the latest document from Github for converting ONNX model. Execute commands in the folder `ONNX_Convertor/keras-onnx`:

```shell
python generated_onnx.py -o outputfile.onnx inputfile.h5
```

# Evaluation 

## Evaluation Metric
We will use mean Average Precision (mAP) for evaluation. You can find the script for computing mAP in `utils/eval.py`.

`mAP`: mAP is the average of Average Precision (AP). AP summarizes a precision-recall curve as the weighted mean of precisions achieved at each threshold, with the increase in recall from the previous threshold used as the weight:

<img src="https://latex.codecogs.com/svg.image?AP&space;=&space;\sum_n&space;(R_n-R_{n-1})P_n&space;" title="AP = \sum_n (R_n-R_{n-1})P_n " />

where <img src="https://latex.codecogs.com/svg.image?R_n" title="R_n" />  and <img src="https://latex.codecogs.com/svg.image?P_n" title="P_n" /> are the precision and recall at the nth threshold. The mAP compares the ground-truth bounding box to the detected box and returns a score. The higher the score, the more accurate the model is in its detections.

## Evaluation on a Dataset
For evaluating the trained model on dataset:
```shell
python utils/eval.py --snapshot path_to_pretrained_model --gpu 0 --input-shape model_input_size --data path_to_data_yaml_file
```

`--snapshot` Path to pretrained model

`--gpu` Which gpu to run. (-1 if cpu) (Default: -1)

`--input-shape` Input shape of the model (Default: (512, 512))

`--class-id-path` Path to the class id mapping file.

`--data` The path to data yaml file

## End-to-End Evaluation
If you would like to perform an end-to-end test with an image dataset, you can use `inference_e2e.py` under the directory `fcos` to obtain the prediction results.
You have to prepare an initial parameter yaml file for the inference runner. You may check `utils/init_params.json` for the format.

```bash
python inference_e2e.py --img-path path_to_dataset_folder --params path_to_init_params_file --save-path path_to_save_json_file
```
`--img-path` Path to the dataset directory

`--params` Path to initial parameter yaml file for the inference runner

`--save-path` Path to save the prediction to a json file

`--gpu` GPU id  (-1 if cpu) (Default: -1)

The predictions will be saved into a json file that has the following structure:
```bash
[
    {'img_path':image_path_1
    'bbox': [[l,t,w,h,score,class_id], [l,t,w,h,score,class_id]]
    },
    {'img_path':image_path_2
    'bbox': [[l,t,w,h,score,class_id], [l,t,w,h,score,class_id]]
    },
    ...
]
```

# Models

Backbone | Input Size | FPN Type | FPS on 520 | FPS on 720 | Model Size
--- | --- | --- |:---:|:---: |:---:
darknet53s | 512 | simple | 5.96303 | 36.6844 | 25.3M
[darknet53s](https://github.com/kneron/Model_Zoo/tree/main/detection/fcos) | 416 | pan | 7.27369 | 48.8437 | 33.9M
darknet53ss | 416 | simple | 20.6361 | 136.093 | 6.9M
darknet53ss | 320 | simple | 33.9502 | 252.713 | 6.9M
resnet18 | 512 | simple | 5.75156 | 33.9144 | 25.2M
resnet18 | 416 | simple | 8.04252 | 52.9392 | 25.2M 
resnet18 | 320 | simple | 13.0232 | 94.5782 | 25.2M
resnet18 | 512 | pan | 4.88634 | 30.1866 | 33.8M
resnet18 | 416 | pan | 6.8977 | 46.9993 | 33.8M
resnet18 | 320 | pan | 10.9281 | 82.4277 | 33.8M

 \ | darknet53s | 
--- |:---:
mAP | 44.8% |
