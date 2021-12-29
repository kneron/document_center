# Kneron Model Zoo Inference 520 Example - Detection(FCOS)

KL520 Inference Example with NEF model trained from
http://doc.kneron.com/docs/#model_training/detection/fcos

---

Check  

- tutorial ( location: /workspace/ai_training/detection/fcos/tutorial/tutorial.ipynb ) 

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
    python KL520KnModelZooGenericInferenceFcos.py 
```
### step 2-2. run KL720 example:  

```bash
    cd python/example_model_zoo
    python KL720KnModelZooGenericInferenceFcos.py 
```

---

## Detail Information:  

Platform      |            backbone        |  FPS(npu only) | Input format |    Preprocess    |  Normalize  |  
--------------|:--------------------------:|---------------:| ------------:| ----------------:| -----------:|  
KL520         |  Darknet53s(FPN type: pan) | 7.27369        |    RGB565    | auto (on device) | Kneron mode |  
KL720         |  Darknet53s(FPN type: pan) | 48.8437        |    RGB565    | auto (on device) | Kneron mode |  
