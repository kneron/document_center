# Kneron Hardware Performance

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.17        | 162  ms         |        No        |
| Inception v4         | 299x299 |    1.45        | 687  ms         |        No        |
| Mobilenet v1         | 224x224 |    56.8        | 17.6 ms        |        No        |
| Mobilenet v2         | 224x224 |    54.1        | 18.4 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    28.5        | 35.1 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    6.94        | 144  ms         |        No        |
| OpenPose             | 256x256 |    0.637       | 1569 ms        |        No        |
| SRCNN                | 384x384 |    11.0        | 90.9 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    21.8        | 45.9 ms        |        Yes       |
| YOLOv3               | 416x416 |    1.44        | 693  ms         |        Yes       |
| YOLOv5s              | 640x640 |    3.65        | 274  ms         |        Yes       |
| Lite-HRNet           | 256x192 |    9.23        | 108  ms         |        Yes       |

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

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    60.4        | 15.9 ms        |        No        |
| Inception v4         | 299x299 |    14.45       | 60.5 ms        |        No        |
| Mobilenet v1         | 224x224 |    277.6       | 3.6  ms        |        No        |
| Mobilenet v2         | 224x224 |    336.6       | 2.97 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    200.6       | 4.98 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    36.1        | 27.6 ms        |        No        |
| OpenPose             | 256x256 |    3.61        | 277  ms        |        No        |
| SRCNN                | 384x384 |    61.5        | 16.2 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    72.7        | 13.8 ms        |        No        |
| YOLOv3               | 416x416 |    6.0         | 167  ms        |        No        |
| YOLOv5s              | 640x640 |    18.8        | 53.2 ms        |        No        |
| Centernet res101     | 512x512 |    2.29        | 437  ms        |        No        |
| Unet                 | 384x384 |    0.859       | 1162 ms        |        No        |
| Lite-HRNet           | 256x192 |    52.69       | 18.9 ms        |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    44.85       | 22.29 ms       |        No        |
| Inception v4         | 299x299 |    12.66       | 78.98 ms       |        No        |
| Mobilenet v1         | 224x224 |    207.40      | 4.82  ms       |        No        |
| Mobilenet v2         | 224x224 |    212.85      | 4.69  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    125.60      | 7.96  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    21.27       | 47.00 ms       |        No        |
| OpenPose             | 256x256 |    4.03        | 248.1 ms       |        No        |
| SRCNN                | 384x384 |    62.84       | 15.91 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    97.63       | 10.24 ms       |        No        |
| YOLOv3               | 416x416 |    5.10        | 196.0 ms       |        No        |
| YOLOv5s              | 640x640 |    16.59       | 60.24 ms       |        No        |
| Unet                 | 384x384 |    1.72        | 581.39 ms      |        No        |
| Lite-HRNet           | 256x192 |    17.38       | 57.52 ms       |        No        |



