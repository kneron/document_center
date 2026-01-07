# Kneron Hardware Performance

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.177       | 161.9  ms      |        No        |
| Inception v4         | 299x299 |    1.454       | 687.7  ms      |        No        |
| Mobilenet v1         | 224x224 |    56.80       | 17.60 ms       |        No        |
| Mobilenet v2         | 224x224 |    54.18       | 18.46 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    28.48       | 35.11 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    6.925       | 144.4  ms      |        No        |
| OpenPose             | 256x256 |    0.637       | 1569 ms        |        No        |
| SRCNN                | 384x384 |    11.00       | 90.90 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    21.80       | 45.85 ms       |        Yes       |
| YOLOv3               | 416x416 |    1.443       | 692.7  ms      |        Yes       |
| YOLOv5s              | 640x640 |    3.653       | 273.7  ms      |        Yes       |
| Lite-HRNet           | 256x192 |    9.233       | 108.2  ms      |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    84.99       | 11.76 ms       |        No        |
| Inception v4         | 299x299 |    21.11       | 47.36 ms       |        No        |
| Mobilenet v1         | 224x224 |    432.6       | 2.311 ms       |        No        |
| Mobilenet v2         | 224x224 |    683.1       | 1.463 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    314.9       | 3.175 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    54.89       | 18.21 ms       |        No        |
| OpenPose             | 256x256 |    5.111       | 195.6 ms       |        No        |
| SRCNN                | 384x384 |    133.9       | 7.469 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    155.2       | 6.441 ms       |        No        |
| YOLOv3               | 416x416 |    10.23       | 97.72 ms       |        No        |
| YOLOv5s              | 640x640 |    25.36       | 39.41 ms       |        No        |
| Centernet res101     | 512x512 |    2.877       | 347.6 ms       |        No        |
| Lite-HRNet           | 256x192 |    27.40       | 36.49 ms       |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    62.00       | 16.12  ms      |        No        |
| Inception v4         | 299x299 |    14.56       | 68.68  ms      |        No        |
| Mobilenet v1         | 224x224 |    284.7       | 3.51  ms       |        No        |
| Mobilenet v2         | 224x224 |    342.3       | 2.92  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    202.6       | 4.94  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    36.79       | 27.18 ms       |        No        |
| OpenPose             | 256x256 |    3.621       | 276.1 ms       |        No        |
| SRCNN                | 384x384 |    61.52       | 16.25 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    72.59       | 13.77 ms       |        No        |
| YOLOv3               | 416x416 |    5.983       | 167.1 ms       |        No        |
| YOLOv5s              | 640x640 |    17.99       | 55.56 ms       |        No        |
| Centernet res101     | 512x512 |    2.287       | 437.2 ms       |        No        |
| Unet                 | 384x384 |    0.875       | 1142  ms       |        No        |
| Lite-HRNet           | 256x192 |    52.49       | 19.04 ms       |        No        |
| CenterNet            | 512x512 |    2.287       | 437.2 ms       |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    47.95       | 20.85 ms       |        No        |
| Inception v4         | 299x299 |    12.47       | 80.16 ms       |        No        |
| Mobilenet v1         | 224x224 |    219.6       | 4.55  ms       |        No        |
| Mobilenet v2         | 224x224 |    218.9       | 4.568 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    130.0       | 7.69  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    22.91       | 43.63 ms       |        No        |
| OpenPose             | 256x256 |    4.035       | 247.8 ms       |        No        |
| SRCNN                | 384x384 |    62.84       | 15.91 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    100.3       | 9.964 ms       |        No        |
| YOLOv3               | 416x416 |    5.143       | 194.4 ms       |        No        |
| YOLOv5s              | 640x640 |    16.82       | 59.43 ms       |        No        |
| Unet                 | 384x384 |    1.802       | 554.6 ms       |        No        |
| Lite-HRNet           | 256x192 |    17.41       | 57.40 ms       |        No        |

*Performance simulation result on NPU KDP730:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    127.2       | 7.860 ms       |        No        |
| Inception v4         | 299x299 |    37.85       | 26.42 ms       |        No        |
| Mobilenet v1         | 224x224 |    610.0       | 1.640 ms       |        No        |
| Mobilenet v2         | 224x224 |    812.5       | 1.230 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    392.2       | 2.549 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    79.03       | 12.65 ms       |        No        |
| OpenPose             | 256x256 |    10.46       | 95.59 ms       |        No        |
| SRCNN                | 384x384 |    163.2       | 6.127 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    201.9       | 4.951 ms       |        No        |
| YOLOv3               | 416x416 |    16.78       | 59.58 ms       |        No        |
| YOLOv5s              | 640x640 |    51.82       | 19.30 ms       |        No        |
| Unet                 | 384x384 |    3.903       | 256.1 ms       |        No        |
| Lite-HRNet           | 256x192 |    200.8       | 4.980 ms       |        No        |
| CenterNet            | 512x512 |    6.657       | 150.2 ms       |        No        |

*More Performance simulation result on NPU KDP730 (default 8bit settings):*
| Model                                                  | Size                               | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| ------------------------------------------------------ | ---------------------------------- | -------------- | -------------- | ---------------- |
| baai_bert_en.opt                                       | 384, 384, 384                      | 16.9512        | 58.9928        | Yes              |
| baai_small-en-v1.5.opt                                 | 384, 384, 384                      | 17.0124        | 58.7807        | Yes              |
| bert_opset11_with_weight_041823_kneron                 | 384, 384                           | 18.2599        | 54.7649        | Yes              |
| centernet_res18_pytorch_3c_512w_512h                   | 3x512x512                          | 18.6832        | 53.524         | No               |
| conformer-tiny-p16_8xb128_in1k_kneron_optimized        | 3x224x224                          | 52.9233        | 18.8953        | No               |
| decoder_modified_2                                     | 1024x512,1024x512,1024x1024,1024   | 5.19971        | 192.318        | No               |
| deeplabv3plus_mobv2_1x0_keras_3c_512w_512h             | 3x512x512                          | 40.1408        | 24.9123        | No               |
| deit-tiny_pt-4xb256_in1k_kneron_optimized              | 3x224x224                          | 181.023        | 5.52417        | No               |
| efficientnet_lite4_rw_pytorch_3c_300w_300h             | 3x300x300                          | 180.42         | 5.54263        | No               |
| Facedetection_SSD_without_BN                           | 3x200x200                          | 928.681        | 1.0768         | No               |
| Facelandmark_kneron_shufflenet_68                      | 3x240x240                          | 1850.3         | 0.540452       | No               |
| inception_resnetv2_pytorch_3c_299w_299h                | 3x299x299                          | 36.7164        | 27.2358        | No               |
| inceptionv3_pytorch_3c_299w_299h                       | 3x299x299                          | 92.9287        | 10.7609        | No               |
| inceptionv4_keras_3c_299w_299h                         | 3x299x299                          | 46.2884        | 21.6037        | No               |
| mlp-mixer-base-p16_64xb64_in1k_kneron_optimized        | 3x224x224                          | 27.7357        | 36.0546        | No               |
| mobilenetv2_100_rw_pytorch_3c_224w_224h                | 3x224x224                          | 894.72         | 1.11767        | No               |
| mobilenetv3_large_minimalistic_x1_0_keras_3c_224w_224h | 3x224x224                          | 883.495        | 1.13187        | No               |
| model_704_nocut                                        | 3x256x640                          | 158.468        | 6.31042        | No               |
| model_706_nocut                                        | 48x64x160                          | 86.0932        | 11.6153        | No               |
| model_707_nocut                                        | 256x640,3x256x640                  | 59.2393        | 16.8807        | No               |
| model_9096_nocut                                       | 80x3000                            | 0.689647       | 1450.02        | No               |
| model_9096_nocut_layer0                                | 1500x768                           | 14.3383        | 69.7431        | No               |
| model_9097_nocut                                       | 1500x768,4x768,4x768,4x4           | 10.97          | 91.158         | No               |
| model_9232_nocut                                       | 12x223x64,12x223x64,12x1500x64,... | 18.664         | 53.5792        | No               |
| openclip_vit_base_patch_16_SigLIP_vision_encoder.opt   | 3x224x224                          | 21.6036        | 46.2887        | No               |
| resnet101_pytorch_3c_224w_224h                         | 3x224x224                          | 59.7392        | 16.7394        | No               |
| resnet50_80_224x224-pytorch                            | 3x224x224                          | 94.1109        | 10.6258        | No               |
| retinanet_pvt-t_fpn_1x_coco_kneron_optimized           | 3x224x224                          | 41.2293        | 24.2546        | No               |
| retinanet_pvtv2-b0_fpn_1x_coco_kneron_optimized        | 3x224x224                          | 54.5772        | 18.3227        | No               |
| retinanet_swin-t-p4-w7_fpn_1x_coco_kneron_optimized    | 3x224x224                          | 24.7706        | 40.3704        | No               |
| shufflenetv2_x1_0_pytorch_3c_224w_224h                 | 3x224x224                          | 869.66         | 1.14987        | No               |
| swin-cut                                               | 3136x96                            | 553.717        | 1.80598        | No               |
| swin-tiny_16xb64_in1k_kneron_optimized                 | 3x224x224                          | 38.646         | 25.8759        | No               |
| swin_tiny_classify_head                                | 3x224x224                          | 28.3665        | 35.2529        | No               |
| swinv2_tiny_classify_head                              | 3x256x256                          | 15.9521        | 62.6876        | Yes              |
| t2t-vit-t-14_8xb64_in1k_kneron_optimized               | 3x224x224                          | 26.0946        | 38.3221        | Yes              |
| tiny_yolov3_keras_3c_608w_608h                         | 3x608x608                          | 130.218        | 7.67941        | No               |
| tnt-s-p16_16xb64_in1k_kneron_optimized                 | 3x224x224                          | 23.1818        | 43.1373        | Yes              |
| vit-base-p16_pt-64xb64_in1k-224_kneron_optimized       | 3x224x224                          | 21.6917        | 46.1007        | No               |
| vit_base_classify_head_kneron                          | 3x224x224                          | 19.5094        | 51.2575        | No               |
| wenet_u2_decoder                                       | 100x512,99x512,99x512              | 95.2782        | 10.4956        | No               |
| wenet_u2_encoder                                       | 100x80                             | 42.3604        | 23.607         | No               |
| yolo11m_640x640.opt                                    | 3x640x640                          | 11.5716        | 86.4183        | No               |
| yolo11n_640x640.opt                                    | 3x640x640                          | 64.921         | 15.4033        | No               |
| yolov3_keras_3c_416w_416h                              | 3x416x416                          | 21.498         | 46.5159        | No               |
| yolov4_keras_3c_416w_416h                              | 3x416x416                          | 23.9978        | 41.6705        | No               |
| yolov5s_pytorch_12c_336w_336h                          | 12x336x336                         | 61.9733        | 16.136         | No               |
| yolov7_640x640.opt                                     | 3x640x640                          | 10.4601        | 95.6015        | No               |
| yolov8m_640x640.opt                                    | 3x640x640                          | 14.9085        | 67.0759        | No               |
| yolov8n_640x640.opt                                    | 3x640x640                          | 69.8148        | 14.3236        | No               |
| yolov9m_640x640.opt                                    | 3x640x640                          | 12.801         | 78.1191        | No               |
| yolov9t_640x640.opt                                    | 3x640x640                          | 64.4753        | 15.5098        | No               |

*More Performance simulation result on NPU KDP730 (input 8 bit，output 16bit， data mixlight, weight 8bit):*

| Model                                                  | Size                               | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| ------------------------------------------------------ | ---------------------------------- | -------------- | -------------- | ---------------- |
| baai_bert_en.opt                                       | 384, 384, 384                      | 12.8872        | 77.5966        | Yes              |
| baai_small-en-v1.5.opt                                 | 384, 384, 384                      | 15.8069        | 63.2637        | Yes              |
| bert_opset11_with_weight_041823_kneron                 | 384, 384                           | 13.158         | 75.9992        | Yes              |
| centernet_res18_pytorch_3c_512w_512h                   | 3x512x512                          | 17.0192        | 58.7572        | No               |
| conformer-tiny-p16_8xb128_in1k_kneron_optimized        | 3x224x224                          | 35.8217        | 27.9161        | No               |
| decoder_modified_2                                     | 1024x512,1024x512,1024x1024,1024   | 4.85533        | 205.959        | No               |
| deeplabv3plus_mobv2_1x0_keras_3c_512w_512h             | 3x512x512                          | 36.7646        | 27.2001        | No               |
| deit-tiny_pt-4xb256_in1k_kneron_optimized              | 3x224x224                          | 156.979        | 6.37026        | No               |
| efficientnet_lite4_rw_pytorch_3c_300w_300h             | 3x300x300                          | 162.867        | 6.13998        | No               |
| Facedetection_SSD_without_BN                           | 3x200x200                          | 849.861        | 1.17666        | No               |
| Facelandmark_kneron_shufflenet_68                      | 3x240x240                          | 1536.22        | 0.650948       | No               |
| inception_resnetv2_pytorch_3c_299w_299h                | 3x299x299                          | 29.2921        | 34.1389        | No               |
| inceptionv3_pytorch_3c_299w_299h                       | 3x299x299                          | 76.0408        | 13.1508        | No               |
| inceptionv4_keras_3c_299w_299h                         | 3x299x299                          | 36.4444        | 27.439         | No               |
| mlp-mixer-base-p16_64xb64_in1k_kneron_optimized        | 3x224x224                          | 18.9444        | 52.7859        | No               |
| mobilenetv2_100_rw_pytorch_3c_224w_224h                | 3x224x224                          | 663.951        | 1.50613        | No               |
| mobilenetv3_large_minimalistic_x1_0_keras_3c_224w_224h | 3x224x224                          | 689.478        | 1.45037        | No               |
| model_704_nocut                                        | 3x256x640                          | 76.2507        | 13.1146        | No               |
| model_706_nocut                                        | 48x64x160                          | 48.9827        | 20.4154        | No               |
| model_707_nocut                                        | 256x640,3x256x640                  | 27.0065        | 37.0282        | No               |
| model_9096_nocut                                       | 80x3000                            | 0.595831       | 1678.33        | No               |
| model_9096_nocut_layer0                                | 1500x768                           | 11.5566        | 86.5305        | No               |
| model_9097_nocut                                       | 1500x768,4x768,4x768,4x4           | 7.33319        | 136.366        | No               |
| model_9232_nocut                                       | 12x223x64,12x223x64,12x1500x64,... | 18.436         | 54.2416        | No               |
| openclip_vit_base_patch_16_SigLIP_vision_encoder.opt   | 3x224x224                          | 14.276         | 70.0475        | No               |
| resnet101_pytorch_3c_224w_224h                         | 3x224x224                          | 47.4349        | 21.0815        | No               |
| resnet50_80_224x224-pytorch                            | 3x224x224                          | 71.9074        | 13.9068        | No               |
| retinanet_pvt-t_fpn_1x_coco_kneron_optimized           | 3x224x224                          | 38.2791        | 26.1239        | No               |
| retinanet_pvtv2-b0_fpn_1x_coco_kneron_optimized        | 3x224x224                          | 50.7597        | 19.7007        | No               |
| retinanet_swin-t-p4-w7_fpn_1x_coco_kneron_optimized    | 3x224x224                          | 22.2134        | 45.018         | No               |
| shufflenetv2_x1_0_pytorch_3c_224w_224h                 | 3x224x224                          | 573.333        | 1.74419        | No               |
| swin-cut                                               | 3136x96                            | 341.628        | 2.92716        | No               |
| swin-tiny_16xb64_in1k_kneron_optimized                 | 3x224x224                          | 31.8914        | 31.3564        | No               |
| swin_tiny_classify_head                                | 3x224x224                          | 29.5016        | 33.8965        | No               |
| swinv2_tiny_classify_head                              | 3x256x256                          | 16.3202        | 61.2736        | Yes              |
| t2t-vit-t-14_8xb64_in1k_kneron_optimized               | 3x224x224                          | 20.0674        | 49.832         | Yes              |
| tiny_yolov3_keras_3c_608w_608h                         | 3x608x608                          | 117.58         | 8.50487        | No               |
| tnt-s-p16_16xb64_in1k_kneron_optimized                 | 3x224x224                          | 19.3189        | 51.7628        | Yes              |
| vit-base-p16_pt-64xb64_in1k-224_kneron_optimized       | 3x224x224                          | 13.9005        | 71.9398        | No               |
| vit_base_classify_head_kneron                          | 3x224x224                          | 15.2754        | 65.4649        | No               |
| wenet_u2_decoder                                       | 100x512,99x512,99x512              | 80.2259        | 12.4648        | No               |
| wenet_u2_encoder                                       | 100x80                             | 37.5957        | 26.5988        | No               |
| yolo11m_640x640.opt                                    | 3x640x640                          | 9.59189        | 104.255        | No               |
| yolo11n_640x640.opt                                    | 3x640x640                          | 53.7206        | 18.6148        | No               |
| yolov3_keras_3c_416w_416h                              | 3x416x416                          | 19.4           | 51.5464        | No               |
| yolov4_keras_3c_416w_416h                              | 3x416x416                          | 21.4122        | 46.7023        | No               |
| yolov5s_pytorch_12c_336w_336h                          | 12x336x336                         | 50.6076        | 19.7599        | No               |
| yolov7_640x640.opt                                     | 3x640x640                          | 8.60255        | 116.245        | No               |
| yolov8m_640x640.opt                                    | 3x640x640                          | 12.6344        | 79.1488        | No               |
| yolov8n_640x640.opt                                    | 3x640x640                          | 54.9075        | 18.2125        | No               |
| yolov9m_640x640.opt                                    | 3x640x640                          | 11.0915        | 90.1591        | No               |
| yolov9t_640x640.opt                                    | 3x640x640                          | 50.1821        | 19.9274        | No               |
