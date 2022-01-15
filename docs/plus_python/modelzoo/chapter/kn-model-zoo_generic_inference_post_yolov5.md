# Kneron Model Zoo Inference 520 Example - Detection(Yolov5)

KL520 Inference Example with NEF model trained from
http://doc.kneron.com/docs/#model_training/detection/yolov5

---

Check  

- tutorial ( location: /workspace/ai_training/detection/yolov5/tutorial/tutorial.ipynb )  

in  

- Kneron Toolchain docker (doc: http://doc.kneron.com/docs/#toolchain/manual/#2-toolchain-docker-overview)  

to learn how to train a the example model, and check  

- http://doc.kneron.com/docs/#toolchain/manual/#2-toolchain-docker-overview  
- http://doc.kneron.com/docs/#toolchain/yolo_example/  

to learn how to convert the trained model to NEF model  

---

## How to:  

### step 1. read document at "python/doc/markdown/getting_start.md" and make sure PLUS is ready  

### step 2-1. run KL520 example:  

```bash
    cd python/example_model_zoo
    python KL520KnModelZooGenericInferenceYolov5.py 
```

### step 2-2. run KL720 example:  

```bash
    cd python/example_model_zoo
    python KL720KnModelZooGenericInferenceYolov5.py 
```

---

## Detail Information:  

Platform      |  backbone  | FPS(npu only)  | Input format |         Preprocess       |  Normalize  |  
--------------|:---------:|----------------:| ------------:| ------------------------:| -----------:|  
KL520         |  YOLOv5s  |     4.91429     |    RGB565    |     auto (on device)     | Kneron mode |  
KL720         |  YOLOv5s  |     24.4114     |    RGB565    |     auto (on device)     | Kneron mode |  
