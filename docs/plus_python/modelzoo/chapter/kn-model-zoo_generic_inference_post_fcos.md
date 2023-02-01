# Kneron Model Zoo Inference 520 Example - Detection(FCOS)

KL520 Inference Example with NEF model trained from
https://doc.kneron.com/docs/#model_training/object_detection_fcos/

---

Check  

- tutorial ( location: /workspace/ai_training/detection/fcos/tutorial/tutorial.ipynb ) 

in  

- Kneron Toolchain docker (doc: https://doc.kneron.com/docs/#toolchain/manual_1_overview/)

to learn how to train a the example model, and check  

- https://doc.kneron.com/docs/#toolchain/manual_1_overview/
- https://doc.kneron.com/docs/#toolchain/appendix/yolo_example/

to learn how to convert the trained model to NEF model  

---

## How to:  

### step 1. read document at [Getting_start](../../getting_start.md) and make sure PLUS is ready  

### step 2-1. run KL520 example:  

```bash
    cd python/example_model_zoo
    python KL520KnModelZooGenericImageInferenceFcos.py 
```
### step 2-2. run KL720 example:  

```bash
    cd python/example_model_zoo
    python KL720KnModelZooGenericImageInferenceFcos.py 
```

---

## Detail Information:  

Platform      |            backbone        |  FPS(npu only) | Input format |    Preprocess    |  Normalize  |  
--------------|:--------------------------:|---------------:| ------------:| ----------------:| -----------:|  
KL520         |  Darknet53s(FPN type: pan) | 7.27369        |    RGB565    | auto (on device) | Kneron mode |  
KL720         |  Darknet53s(FPN type: pan) | 48.8437        |    RGB565    | auto (on device) | Kneron mode |  
