# Kneron Model Zoo Inference Example - Classification

PLUS Inference Example with NEF model trained from
https://doc.kneron.com/docs/#model_training/classification/

---

Check 
- tutorial ( location: /workspace/ai_training/classification/tutorial/tutorial.ipynb ) 

in

- Kneron Toolchain docker (doc: https://doc.kneron.com/docs/#toolchain/manual_1_overview/)

to learn how to train a the example model, and check 

- https://doc.kneron.com/docs/#toolchain/manual_1_overview/
- https://doc.kneron.com/docs/#toolchain/appendix/yolo_example/

to learn how to convert the trained model to NEF model

Note: We built and run the examples below under OS Windows 10 (19041.1052), Keil uVision5 (5.27.1.0), MSYS2 MinGW 64-bit (20210419), and cmake version 3.20.2.

---

## How to:
### step 1. read document at [Getting_start](../getting_started.md) and make sure PLUS is ready
### step 2-1. run KL520 example:
```bash
    cd build/bin/
    ./kl520_kn-model-zoo_generic_inference_classification 
```
### step 2-2. run KL720 example:
```bash
    cd build/bin/
    ./kl720_kn-model-zoo_generic_inference_classification 
```

---

## Detail Infomation:

Platform      |  backbone  | FPS(npu only) | Input format |    Preprocess    |  Normalize  | 
--------------|:----------:|--------------:| ------------:| ----------------:| -----------:|
KL520         |  resnet18  | 20.4376       |    RGB565    | auto (on device) | Kneron mode |
KL720         |  resnet18  | 141.371       |    RGB565    | auto (on device) | Kneron mode |


