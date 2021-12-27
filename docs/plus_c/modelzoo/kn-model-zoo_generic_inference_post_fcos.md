# Kneron Model Zoo Inference Example - Detection(FCOS)

PLUS Inference Example with NEF model trained from
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

Note: We built and run the examples below under OS Windows 10 (19041.1052), Keil uVision5 (5.27.1.0), MSYS2 MinGW 64-bit (20210419), and cmake version 3.20.2.

---

## How to:
### step 1. read document at [Getting_start](http://doc.kneron.com/docs/#plus/getting_start/) and make sure PLUS is ready
### step 2-1. run KL520 example:
```bash
    cd build/bin/
    ./kl520_kn-model-zoo_generic_inference_post_fcos 
```
### step 2-2. run KL720 example:
```bash
    cd build/bin/
    ./kl720_kn-model-zoo_generic_inference_post_fcos 
```

---

## Detail Infomation:

Platform      |            backbone        |  FPS(npu only) | Input format |    Preprocess    |  Normalize  | 
--------------|:--------------------------:|---------------:| ------------:| ----------------:| -----------:|
KL520         |  Darknet53s(FPN type: pan) | 7.27369        |    RGB565    | auto (on device) | Kneron mode |
KL720         |  Darknet53s(FPN type: pan) | 48.8437        |    RGB565    | auto (on device) | Kneron mode |
