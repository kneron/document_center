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
| YOLOv5s              | 640x640 |    3.65        | 274 ms         |        Yes       |
| Lite-HRNet           | 256x192 |    8.82        | 113 ms         |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    86.4        | 11.6 ms        |        No        |
| Inception v4         | 299x299 |    21.67       | 46.1 ms        |        No        |
| Mobilenet v1         | 224x224 |    432         | 2.31 ms        |        No        |
| Mobilenet v2         | 224x224 |    682         | 1.46 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    317         | 3.15 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    56.1        | 17.8 ms        |        No        |
| OpenPose             | 256x256 |    5.11        | 195 ms         |        No        |
| SRCNN                | 384x384 |    134         | 7.48 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    155         | 6.45 ms        |        No        |
| YOLOv3               | 416x416 |    10.24       | 97.7 ms        |        No        |
| YOLOv5s              | 640x640 |    25.7        | 38.9 ms        |        No        |
| Centernet res101     | 512x512 |    2.86        | 350 ms         |        No        |
| Lite-HRNet           | 256x192 |    28          | 35.7 ms        |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    64.3        | 15.5 ms        |        No        |
| Inception v4         | 299x299 |    16.5        | 60.5 ms        |        No        |
| Mobilenet v1         | 224x224 |    284.7       | 3.51 ms        |        No        |
| Mobilenet v2         | 224x224 |    340         | 2.94 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    205         | 4.88 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    36.2        | 27.6 ms        |        No        |
| OpenPose             | 256x256 |    3.61        | 277 ms         |        No        |
| SRCNN                | 384x384 |    61.5        | 16.2 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    72.7        | 13.8 ms        |        No        |
| YOLOv3               | 416x416 |    6.0         | 167 ms         |        No        |
| YOLOv5s              | 640x640 |    18.8        | 53.2 ms        |        No        |
| Centernet res101     | 512x512 |    2.29        | 437 ms         |        No        |
| Unet                 | 384x384 |    0.970       | 1030 ms        |        No        |
| Lite-HRNet           | 256x192 |    54.3        | 18.4 ms        |       No         |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    57.8        | 17.3 ms        |        No        |
| Inception v4         | 299x299 |    16.7        | 59.9 ms        |        No        |
| Mobilenet v1         | 224x224 |    221.1       | 4.52 ms        |        No        |
| Mobilenet v2         | 224x224 |    218.7       | 4.57 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    128         | 7.83 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    26.0        | 38.4 ms        |        No        |
| OpenPose             | 256x256 |    5.46        | 183.1 ms       |        No        |
| SRCNN                | 384x384 |    74.73       | 13.3 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    118.8       | 8.42 ms        |        No        |
| YOLOv3               | 416x416 |    5.77        | 173.3 ms       |        No        |
| YOLOv5s              | 640x640 |    19.25       | 51.9 ms        |        No        |
| Unet                 | 384x384 |    2.01        | 497 ms         |        No        |
| Lite-HRNet           | 256x192 |    19.68       | 50.8 ms        |        No        |



