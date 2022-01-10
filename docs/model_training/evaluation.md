## Introduction

Different statistical functions (ex: object detection, regression, reid, ...) are built in different class. Please initialize the one you want as an evaluator to evaluate your results with providing GT. All of parameters could be changed in yaml files along with it, and you could also import the evaluation class to use it in your code. **Notice that you should be familiar with public_field.py(evaluation/kneron_eval/utils/public_field.py), and obey the data format in it.** Note that all the paths in this document are under /workspace/ai_training inside the docker.

### pre-requiste

Go to `kneron_eval` folder
```bash
cd kneron_eval
```

### Table of contents

- [Introduction](#introduction)
  - [pre-requiste](#pre-requiste)
  - [Table of contents](#table-of-contents)
  - [Object detection:](#object-detection)
  - [Regression](#regression)
  - [Classification](#classification)
  - [ReID](#reid)

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

Notic that you should use a key from public_field.py starting with **lmk** as key in your json. ex: `lmk_eye_7pts`, `lmk_coco_body_17pts`. Please follow the key in your GT.json. (**Notice that you should be familiar with public_field.py(evaluation/kneron_eval/utils/public_field.py), and obey the data format in it.**)

```python    
python regression.py --yaml yaml/regression.yaml --output output_regression.txt
```

| Parameters | Descriptions |
| --- | --- |
| GT_json_path | Ground truth json path. Should be provided by testing team |
| inference_result | Inference json path. Should follow GT format |
| landmark_points | landmark key from public_field.py |
| distance_metrics | should be l1 or l2 or MAE |

### Classification

Notic that you should use a key from public_field.py starting with **class** as key in your json. ex: `class1`, `class2`. Please follow the key in your GT.json. (**Notice that you should be familiar with public_field.py(evaluation/kneron_eval/utils/public_field.py), and obey the data format in it.**)

```python    
python classification.py --yaml yaml/classification.yaml --output output_classification.txt
```

| Parameters | Descriptions |
| --- | --- |
| GT_json_path | Ground truth json path. Should be provided by testing team |
| inference_result | Inference json path. Should follow GT format |
| class_format | The dimension of the class |
| mapping | should be l1 or l2 or MAE |
| subclass | subclass from mapping |
| scan_threshold | boolean value. Whether or not scan the scores from 0.0 to 1.0 to get the best threshold |
| overall_top1_accuracy | Set true if you are running multi-class classification |

### ReID

Notic that you should use a key from public_field.py: **track_id** as key in your json. Please follow the key in your GT.json. (**Notice that you should be familiar with public_field.py(evaluation/kneron_eval/utils/public_field.py), and obey the data format in it.**)

```python    
python reid.py --yaml yaml/reid.yaml --output output_reid.txt
```

| Parameters | Descriptions |
| --- | --- |
| GT_json_path | Ground truth json path. Should be provided by testing team |
| inference_result | Inference json path. Should follow GT format |
| max_IoU | IoU for person bbox |
| skip_rate | skip frame rate |