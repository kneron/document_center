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
| Inception v3         | 224x224 |    84.99       | 11.76 ms        |        No        |
| Inception v4         | 299x299 |    21.11       | 47.36 ms        |        No        |
| Mobilenet v1         | 224x224 |    432.6       | 2.311 ms        |        No        |
| Mobilenet v2         | 224x224 |    683.1       | 1.463 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    314.9       | 3.175 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    54.89       | 18.21 ms        |        No        |
| OpenPose             | 256x256 |    5.111       | 195.6 ms        |        No        |
| SRCNN                | 384x384 |    133.8       | 7.468 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    155.2       | 6.441 ms        |        No        |
| YOLOv3               | 416x416 |    10.23       | 97.72 ms        |        No        |
| YOLOv5s              | 640x640 |    25.36       | 39.41 ms        |        No        |
| Centernet res101     | 512x512 |    2.876       | 347.6 ms        |        No        |
| Lite-HRNet           | 256x192 |    27.40       | 36.49 ms        |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    62.0        | 16.1  ms       |        No        |
| Inception v4         | 299x299 |    14.56       | 68.7  ms       |        No        |
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
| Inception v3         | 224x224 |    127.1       | 7.861 ms       |        No        |
| Inception v4         | 299x299 |    37.86       | 26.41 ms       |        No        |
| Mobilenet v1         | 224x224 |    609.4       | 1.640 ms       |        No        |
| Mobilenet v2         | 224x224 |    811.1       | 1.232 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    393.9       | 2.538 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    79.03       | 12.65 ms       |        No        |
| OpenPose             | 256x256 |    10.45       | 95.62 ms       |        No        |
| SRCNN                | 384x384 |    159.0       | 6.289 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    199.4       | 5.013 ms       |        No        |
| YOLOv3               | 416x416 |    16.70       | 59.85 ms       |        No        |
| YOLOv5s              | 640x640 |    50.79       | 19.68 ms       |        No        |
| Unet                 | 384x384 |    3.867       | 258.5 ms       |        No        |
| Lite-HRNet           | 256x192 |    201.0       | 4.974 ms       |        No        |
| CenterNet            | 512x512 |    6.529       | 153.1 ms       |        No        |
