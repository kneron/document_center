# Kneron Model Zoo PLUS Inference Example - RegNet  (Classification)

NEF model trained from
http://doc.kneron.com/docs/#model_training/OpenMMLab/RegNet.md

---

Check  

- [document](../../../model_training/OpenMMLab/RegNet.md )  

to learn how to train a the example model, and convert the trained model to NEF model  

---

## How to:  

### step 1. read document at [Getting_start](../../getting_start.md) and make sure PLUS is ready  

### step 2-1. run KL720 example:  

```bash
    cd python/example_model_zoo
    python KL720KnModelZooGenericDataInferenceMMClsRegNetX.py 
```

---

## Detail Information:  

Platform      |  backbone  | FPS(npu only)  | Input format |         Preprocess       |  Normalize  |  
--------------|:---------:|----------------:| ------------:| ------------------------:| -----------:|  
KL720         |  RegNet  |     N/A    |    raw    |     bypass (on host)     | bypass mode |  
