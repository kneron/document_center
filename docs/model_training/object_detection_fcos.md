<h1 align="center">  Object Detection </h1>
Object Detection task with fcos model.  

This document contains the explanations of arguments of each script. 


You can find the tutorial for finetuning a pretrained model on custom dataset under the `tutorial` folder, `tutorial/README.md`. 


The ipython notebook tutorial is also prepared under the `tutorial` folder as `tutorial/tutorial.ipynb`. You may upload and run this ipython notebook on Google colab.

# Prerequisites
- Python >= 3.6

# Installation
To install the dependencies, run
```
pip install -r requirements.txt
python setup.py build_ext --inplace
```

# Dataset & Preparation

## Standard Datasets
Our traning script accepts standard PASCAL VOC dataset and MS COCO dataset. You may download the dataset using the following link:

- Download [2012 PASCAL VOC Dataset](http://host.robots.ox.ac.uk/pascal/VOC/) 
- Download [2017 MS COCO Dataset](https://cocodataset.org/#download) 

## Custom Datasets
You can also train the model on a custom dataset. The CSV files will be used to store the data annotations. To define your own datasets, two CSV files should be used: one file containing annotations and one file containing a class name to ID mapping.

### Annotations format
The CSV file with annotations should contain one annotation per line. The header can be defined as:
```
img_id,xmin,ymin,xmax,ymax,class_id
```
Images with multiple bounding boxes should use one row per bounding box. Note that indexing for pixel values starts at 0. The expected format of each line is:
```
path/to/image.jpg,x1,y1,x2,y2,class_name
```
By default the CSV generator will look for images relative to the directory of the annotations file.

Some images may not contain any labeled objects.
To add these images to the dataset as negative examples,
you can define an annotation where `x1`, `y1`, `x2`, `y2` and `class_name` are all empty:
```
path/to/image.jpg,,,,,
```
A full example:
```
img_id,xmin,ymin,xmax,ymax,class_id
img_001.jpg,171.0,208.0,134.0,285.0,dog
img_002.jpg,268.0,183.0,259.0,263.0,cat
img_002.jpg,537.0,187.0,484.0,244.0,person
img_003.jpg,,,,,
```
This defines a dataset with 3 images.
`img_001.jpg` contains a dog.
`img_002.jpg` contains a cat and a person.
`img_003.jpg` contains no interesting objects/animals.

### Class mapping format
The class name to ID mapping file should contain one mapping per line.
Each line should use the following format:
```
class_name,id
```

Indexing for classes starts at 0.
Do not include a background class as it is implicit.

For example:
```
cow,0
cat,1
bird,2
```

### Annotation Tools
You can use [labelme](https://github.com/wkentaro/labelme) to create bounding boxes and labels for your images. For more details, you may visit [labelme](https://github.com/wkentaro/labelme) and check their documents. `csv_preprocess.py` could be used to preprocess and randomly split the data. 


# Train 

For training on Pascal VOC, run:
```shell
python train.py --backbone backbone_model_name --batch-size 8 --gpu 0 pascal path_to_voc_dataset/VOCdevkit/VOC2012 --val-annotations-path val
```

For training on MS COCO, run:
```shell
python train.py --backbone backbone_model_name --batch-size 8 --gpu 0 coco path_to_coco_dataset/
```

For training on a custom dataset, run:
```shell
python train.py --backbone backbone_model_name --snapshot path_to_pretrained_model --freeze-backbone --batch-size 4 --gpu 0 csv path_to_image_folder --annotations-path path_to_train_annotation_file --classes-path path_to_class_mapping_file --val-annotations-path path_to_val_annotation_file
```

`--backbone` Which backbone model to use. 

`--snapshot` The path to pretrained model
 
`--freeze-backbone` Whether freeze the backbone when the pretrained model is used 

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

When the validation mAP stops increasing for 5 epochs, the early stopping will be triggered and the training process will be terminated. 

# Inference 

For infernce the model on a single image:
```shell
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

For evaluating the trained model on MS COCO dataset:
```shell
python utils/eval.py --snapshot path_to_pretrained_model --gpu 0 --input-shape model_input_size coco --annotations-path path_to_annotation_file --set-name train/val/test --data-dir path_to_data_directory
```

For evaluating the trained model on a custom dataset:
```shell
python utils/eval.py --snapshot path_to_pretrained_model --gpu 0 --input-shape model_input_size csv --annotations-path path_to_annotation_file --classes-path path_to_class_id_mapping_file --data-dir path_to_data_directory
```

`--snapshot` Path to pretrained model

`--gpu` Which gpu to run. (-1 if cpu) (Default: -1)

`--input-shape` Input shape of the model (Default: (512, 512))

`--class-id-path` Path to the class id mapping file.

`--data-dir` Path to the image data directory.

`--annotations-path` Path to the annotation file.

`--set-name` Train, validation or test folder. (for evaluating on COCO)


For evaluating the a pre-computed bboxes json file (end-to-end testing) on custom dataset:
```shell
python utils/eval.py --detections-path path_to_detection_result_file e2e --annotations-path path_to_annotation_file --classes-path path_to_class_id_mapping_file --data-dir path_to_data_directory
```

`--detections-path` Path to the detection bboxes file.

`--input-shape` Input shape of the model (Default: (512, 512))

`--class-id-path` Path to the class id mapping file.

`--data-dir` Path to the image data directory.

`--annotations-path` Path to the annotation file (ground truth).

`--score-thres` The score threshold of bounding boxes. (Default: 0.1)

`--iou-thres` the iou threshold. (Default: 0.35) 

The evaluation statistics will be saved in `mAP_result.txt`. You may check the format in tutorial. 


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

Backbone | darknet53s | darknet53ss  | resnet18
--- | --- | --- | ---
Accuracy | medium~high | low | medium
