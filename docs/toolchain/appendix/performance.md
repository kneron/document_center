# Kneron Hardware Performance

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.17        | 162  ms        |        No        |
| Inception v4         | 299x299 |    1.45        | 687  ms        |        No        |
| Mobilenet v1         | 224x224 |    56.8        | 17.6 ms        |        No        |
| Mobilenet v2         | 224x224 |    54.1        | 18.4 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    28.5        | 35.1 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    6.92        | 144  ms        |        No        |
| OpenPose             | 256x256 |    0.637       | 1569 ms        |        No        |
| SRCNN                | 384x384 |    11.0        | 90.9 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    21.8        | 45.9 ms        |        Yes       |
| YOLOv3               | 416x416 |    1.44        | 693  ms        |        Yes       |
| YOLOv5s              | 640x640 |    3.65        | 274  ms        |        Yes       |
| Lite-HRNet           | 256x192 |    9.23        | 108  ms        |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    84.9        | 11.6 ms        |        No        |
| Inception v4         | 299x299 |    21.11       | 47.3 ms        |        No        |
| Mobilenet v1         | 224x224 |    432         | 2.31 ms        |        No        |
| Mobilenet v2         | 224x224 |    682         | 1.46 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    314.9       | 3.17 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    54.8        | 18.2 ms        |        No        |
| OpenPose             | 256x256 |    5.11        | 195  ms         |        No        |
| SRCNN                | 384x384 |    134         | 7.48 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    155         | 6.45 ms        |        No        |
| YOLOv3               | 416x416 |    10.24       | 97.7 ms        |        No        |
| YOLOv5s              | 640x640 |    25.7        | 38.9 ms        |        No        |
| Centernet res101     | 512x512 |    2.86        | 350  ms        |        No        |
| Lite-HRNet           | 256x192 |    27.55       | 36.3 ms        |        No        |
| CenterNet            | 512x512 |    2.88        | 347.6 ms       |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    60.5        | 16.5  ms       |        No        |
| Inception v4         | 299x299 |    14.45       | 69.2  ms       |        No        |
| Mobilenet v1         | 224x224 |    277.6       | 3.6   ms       |        No        |
| Mobilenet v2         | 224x224 |    336.7       | 2.97  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    200.7       | 4.98  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    36.1        | 27.6  ms       |        No        |
| OpenPose             | 256x256 |    3.62        | 277   ms       |        No        |
| SRCNN                | 384x384 |    61.5        | 16.2  ms       |        No        |
| Tiny YOLOv3          | 416x416 |    72.6        | 13.8  ms       |        No        |
| YOLOv3               | 416x416 |    6.0         | 167   ms       |        No        |
| YOLOv5s              | 640x640 |    18          | 55.6  ms       |        No        |
| Centernet res101     | 512x512 |    2.29        | 437   ms       |        No        |
| Unet                 | 384x384 |    0.859       | 1162  ms       |        No        |
| Lite-HRNet           | 256x192 |    52.69       | 18.9  ms       |        No        |
| CenterNet            | 512x512 |    2.27        | 440.9 ms       |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    44.86       | 22.29 ms       |        No        |
| Inception v4         | 299x299 |    12.66       | 78.98 ms       |        No        |
| Mobilenet v1         | 224x224 |    207.40      | 4.82  ms       |        No        |
| Mobilenet v2         | 224x224 |    212.85      | 4.69  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    125.60      | 7.96  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    21.27       | 47.00 ms       |        No        |
| OpenPose             | 256x256 |    4.03        | 248.1 ms       |        No        |
| SRCNN                | 384x384 |    62.84       | 15.91 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    97.63       | 10.24 ms       |        No        |
| YOLOv3               | 416x416 |    4.92        | 203.0 ms       |        No        |
| YOLOv5s              | 640x640 |    16.59       | 60.24 ms       |        No        |
| Unet                 | 384x384 |    1.72        | 581.4 ms       |        No        |
| Lite-HRNet           | 256x192 |    17.38       | 57.52 ms       |        No        |

*Performance simulation result on NPU KDP730:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    158.67      | 6.30  ms       |        No        |
| Inception v4         | 299x299 |    39.93       | 25.04 ms       |        No        |
| Mobilenet v1         | 224x224 |    706.27      | 1.42  ms       |        No        |
| Mobilenet v2         | 224x224 |    1076.2      | 0.93  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    440.18      | 2.27  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    87.74       | 11.40 ms       |        No        |
| OpenPose             | 256x256 |    10.30       | 97.11 ms       |        No        |
| SRCNN                | 384x384 |    164.4       | 6.08  ms       |        No        |
| Tiny YOLOv3          | 416x416 |    196.3       | 5.093 ms       |        No        |
| YOLOv3               | 416x416 |    16.20       | 61.69 ms       |        No        |
| YOLOv5s              | 640x640 |    50.67       | 19.73 ms       |        No        |
| Unet                 | 384x384 |    3.77        | 265.0 ms       |        No        |
| Lite-HRNet           | 256x192 |    206.4       | 4.845 ms       |        No        |
| CenterNet            | 512x512 |    5.98        | 167.1 ms       |        No        |
