# Kneron Hardware Performance

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.27        | 160 ms         |        No        |
| Inception v4         | 299x299 |    1.45        | 687 ms         |        No        |
| Mobilenet v1         | 224x224 |    57.3        | 17.4 ms        |        No        |
| Mobilenet v2         | 224x224 |    54.7        | 18.3 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    28.5        | 35.1 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    6.94        | 144 ms         |        No        |
| OpenPose             | 256x256 |    0.637       | 1569 ms        |        No        |
| SRCNN                | 384x384 |    11.0        | 90.9 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    21.8        | 45.9 ms        |        Yes       |
| YOLOv3               | 416x416 |    1.44        | 693 ms         |        Yes       |
| YOLOv5s              | 640x640 |    3.67        | 272 ms         |        Yes       |
| Lite-HRNet           | 256x192 |    8.82        | 113 ms         |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    86.4        | 11.6 ms        |        No        |
| Inception v4         | 299x299 |    21.67       | 46.1 ms        |        No        |
| Mobilenet v1         | 224x224 |    448         | 2.22 ms        |        No        |
| Mobilenet v2         | 224x224 |    682         | 1.46 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    317         | 3.15 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    56.1        | 17.8 ms        |        No        |
| OpenPose             | 256x256 |    5.11        | 195 ms         |        No        |
| SRCNN                | 384x384 |    134         | 7.48 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    155         | 6.45 ms        |        No        |
| YOLOv3               | 416x416 |    10.23       | 97.8 ms        |        No        |
| YOLOv5s              | 640x640 |    25.7        | 38.9 ms        |        No        |
| Centernet res101     | 512x512 |    2.86        | 350 ms         |        No        |
| Lite-HRNet           | 256x192 |    28          | 35.7 ms        |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    64.3        | 15.5 ms        |        No        |
| Inception v4         | 299x299 |    16.5        | 60.5 ms        |        No        |
| Mobilenet v1         | 224x224 |    291         | 3.44 ms        |        No        |
| Mobilenet v2         | 224x224 |    340         | 2.94 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    205         | 4.88 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    35.9        | 27.8 ms        |        No        |
| OpenPose             | 256x256 |    3.61        | 277 ms         |        No        |
| SRCNN                | 384x384 |    61.5        | 16.2 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    72.0        | 13.9 ms        |        No        |
| YOLOv3               | 416x416 |    5.93        | 169 ms         |        No        |
| YOLOv5s              | 640x640 |    18.7        | 53.4 ms        |        No        |
| Centernet res101     | 512x512 |    2.33        | 429 ms         |        No        |
| Unet                 | 384x384 |    0.970       | 1030 ms        |        No        |
| Lite-HRNet           | 256x192 |    52.7        | 19.0 ms        |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    56.8        | 17.6 ms        |        No        |
| Inception v4         | 299x299 |    16.3        | 61.3 ms        |        No        |
| Mobilenet v1         | 224x224 |    222         | 4.51 ms        |        No        |
| Mobilenet v2         | 224x224 |    216.2       | 4.62 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    128         | 7.83 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    25.4        | 39.3 ms        |        No        |
| OpenPose             | 256x256 |    5.33        | 187 ms         |        No        |
| SRCNN                | 384x384 |    74.73       | 13.3 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    117         | 8.53 ms        |        No        |
| YOLOv3               | 416x416 |    5.70        | 175 ms         |        No        |
| YOLOv5s              | 640x640 |    19.1        | 52.4 ms        |        No        |
| Unet                 | 384x384 |    2.01        | 497 ms         |        No        |
| Lite-HRNet           | 256x192 |    19.3        | 51.7 ms        |        No        |



