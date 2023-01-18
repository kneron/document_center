## Kneron ModelZoo

The **Kneron ModelZoo** provides verified model architecture and training code for user to easily retrain model and put it on Kneron hardware platform. You can convert the retrained model to NEF model by our toolchain provided in section **Kneron Toolchain Docker**

In addition, the  **Kneron PLUS** provides `Generic Image Inference`  and `Generic Data Inference`APIs for you to quickly build the prototype application. You can learn how to leverage `Generic Image Inference` and `Generic Data Inference` APIs to do `inference`, `pre-processing` and `post-processing` by the following ModelZoo examples.

(*Note) There are two type of examples (Verified category/models, Legacy), recommend user can try ` Verified category/models` first,  `Legacy` version is planned to be removed.

### Verified category/models:
|  Category |  Model Type & Document |  PLUS example  | 
|---|---|---|
|  kneron-mmdetection  |  [YoloX](../../model_training/OpenMMLab/YoloX.md) |  [Python example](./chapter/YoloX.md) |  
|  kneron-mmpose | [RSN18](../../model_training/OpenMMLab/RSN18.md)   |  [Python example](./chapter/RSN18.md) |
|  kneron-mmsegmentation  | [STDC](../../model_training/OpenMMLab/STDC.md)  |  [Python example](./chapter/STDC.md) |
|  kneron-mmtracking  | [ByteTrack](../../model_training/OpenMMLab/ByteTrack.md)  |  [Python example](./chapter/ByteTrack.md) |
|  kneron-mmclassification | [RegNet](../../model_training/OpenMMLab/RegNet.md)  |  [Python example](./chapter/RegNet.md) |
|

### Legacy:

|  Category |  Model Type & Document |  PLUS example  | 
|---|---|---|
|  Popular Object  Detection|  [YoloV5s](../../model_training/object_detection_yolov5.md) | [Python example](./chapter/kn-model-zoo_generic_inference_post_yolov5.md)   |
|   | [FCOS](../../model_training/object_detection_fcos.md)  |  [Python example](./chapter/kn-model-zoo_generic_inference_post_fcos.md)  |
| Popular Classification  | [Popular backbones](../../model_training/classification.md)  | [Python example](./chapter/kn-model-zoo_generic_inference_classification.md)   |
|

### Reference

- [Toolchain Docker](https://doc.kneron.com/docs/#toolchain/manual_1_overview/)
- [Model Training](https://doc.kneron.com/docs/#model_training/)
