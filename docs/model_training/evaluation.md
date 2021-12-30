## Introduction

Different statistical functions (ex: object detection, regression, reid, ...) are built in different class. Please initialize the one you want as an evaluator to evaluate your results with providing GT. All of parameters could be changed in yaml files along with it, and you could also import the evaluation class to use it in your code. **Notice that you should be familiar with [public_field.py](http://59.125.118.185:8088/jenna/kneron_globalconstant/-/blob/master/public_field.py), and obey the data format in it.**

### pre-requiste

1. Make sure [kneron_globalconstant](http://59.125.118.185:8088/jenna/kneron_globalconstant/-/blob/master/) is included in utils folder.
```bash
git submodule init
git submodule update
```

2. Go to `kneron_eval` folder
```bash
cd kneron_eval
```

### Table of contents

* [Object detection](#objectdetection)
* [Regression](#regression)

### Object detection:

This evaluation is built based on [COCOAPI](https://github.com/cocodataset/cocoapi).
Notic that you should use `bbox` as key in your json.

```python
python object_detection.py --yaml yaml/object_detection.yaml --output output_objectDetection.txt
```
| Parameters | Descriptions |
| --- | --- |
| GT_json_path | Ground truth json path. Should be provided by testing team |
| inference_result | Inference json path. Should follow GT format |
| areaRng_type_table | size of interested for classes |
| mapping | detection mapping from public_field.py |
| subclass | subset of interested classes |

### Regression

Notic that you should use a key from public_field.py starting with **lmk** as key in your json. ex: `lmk_eye_7pts`, `lmk_coco_body_17pts`. Please follow the key in your GT.json. (**Notice that you should be familiar with [public_field.py](http://59.125.118.185:8088/jenna/kneron_globalconstant/-/blob/master/public_field.py), and obey the data format in it.**)

```python    
python regression.py --yaml yaml/regression.yaml --output output_regression.txt
```
| Parameters | Descriptions |
| --- | --- |
| GT_json_path | Ground truth json path. Should be provided by testing team |
| inference_result | Inference json path. Should follow GT format |
| landmark_points | landmark key from public_field.py |
| distance_metrics | should be l1 or l2 or MAE |