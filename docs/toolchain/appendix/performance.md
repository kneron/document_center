# Kneron Hardware Performance

 *Performance simulation result on NPU KDP520:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    6.177       | 161.879  ms      |        No        |
| Inception v4         | 299x299 |    1.454       | 687.693  ms      |        No        |
| Mobilenet v1         | 224x224 |    56.809       | 17.603 ms       |        Yes        |
| Mobilenet v2         | 224x224 |    54.181       | 18.457 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    28.479       | 35.114 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    6.925       | 144.4  ms      |        No        |
| OpenPose             | 256x256 |    0.637       | 1569.45 ms        |        No        |
| SRCNN                | 384x384 |    11.001       | 90.9 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    21.809       | 45.852 ms       |        Yes       |
| YOLOv3               | 416x416 |    1.444       | 692.755  ms      |        Yes       |
| YOLOv5s              | 640x640 |    3.653       | 273.714  ms      |        Yes       |
| Lite-HRNet           | 256x192 |    9.234       | 108.296  ms      |        Yes       |

*Performance simulation result on NPU KDP720:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    84.993       | 11.766 ms       |        No        |
| Inception v4         | 299x299 |    21.113       | 47.364 ms       |        No        |
| Mobilenet v1         | 224x224 |    432.636       | 2.311 ms       |        No        |
| Mobilenet v2         | 224x224 |    683.161       | 1.464 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    314.926       | 3.175 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    54.895       | 18.217 ms       |        No        |
| OpenPose             | 256x256 |    5.112       | 195.62 ms       |        No        |
| SRCNN                | 384x384 |    133.892       | 7.469 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    155.236       | 6.442 ms       |        No        |
| YOLOv3               | 416x416 |    10.233       | 97.722 ms       |        No        |
| YOLOv5s              | 640x640 |    25.368       | 39.419 ms       |        No        |
| Centernet res101     | 512x512 |    2.877       | 347.644 ms       |        No        |
| Lite-HRNet           | 256x192 |    27.4       | 36.496 ms       |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    62.007       | 16.127  ms      |        No        |
| Inception v4         | 299x299 |    14.56       | 68.68  ms      |        No        |
| Mobilenet v1         | 224x224 |    284.705       | 3.512  ms       |        No        |
| Mobilenet v2         | 224x224 |    342.302       | 2.921  ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    202.578       | 4.936  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    36.794       | 27.178 ms       |        No        |
| OpenPose             | 256x256 |    3.622       | 276.127 ms       |        No        |
| SRCNN                | 384x384 |    61.521       | 16.255 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    72.59       | 13.776 ms       |        No        |
| YOLOv3               | 416x416 |    5.983       | 167.127 ms       |        No        |
| YOLOv5s              | 640x640 |    18       | 55.556 ms       |        No        |
| Centernet res101     | 512x512 |    2.287       | 437.202 ms       |        No        |
| Unet                 | 384x384 |    0.875       | 1142.75  ms       |        No        |
| Lite-HRNet           | 256x192 |    52.496       | 19.049 ms       |        No        |
| CenterNet            | 512x512 |    2.287       | 437.202 ms       |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    47.951       | 20.855 ms       |        No        |
| Inception v4         | 299x299 |    12.474       | 80.166 ms       |        No        |
| Mobilenet v1         | 224x224 |    219.659       | 4.553  ms       |        No        |
| Mobilenet v2         | 224x224 |    218.907       | 4.568 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    130.035       | 7.69  ms       |        No        |
| Resnet50 v1.5        | 224x224 |    22.915       | 43.64 ms       |        No        |
| OpenPose             | 256x256 |    4.035       | 247.822 ms       |        No        |
| SRCNN                | 384x384 |    62.844       | 15.912 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    100.357       | 9.964 ms       |        No        |
| YOLOv3               | 416x416 |    5.144       | 194.418 ms       |        No        |
| YOLOv5s              | 640x640 |    16.825       | 59.436 ms       |        No        |
| Unet                 | 384x384 |    1.803       | 554.658 ms       |        No        |
| Lite-HRNet           | 256x192 |    17.419       | 57.41 ms       |        No        |

*Performance simulation result on NPU KDP730:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    136.068       | 7.349 ms       |        No        |
| Inception v4         | 299x299 |    45.911       | 21.781 ms       |        No        |
| Mobilenet v1         | 224x224 |    675.998       | 1.479 ms       |        No        |
| Mobilenet v2         | 224x224 |    866.036       | 1.155 ms       |        No        |
| Mobilenet v2 ssdlite | 300x300 |    416.73       | 2.4 ms       |        No        |
| Resnet50 v1.5        | 224x224 |    87.01       | 11.493 ms       |        No        |
| OpenPose             | 256x256 |    13.421       | 74.509 ms       |        No        |
| SRCNN                | 384x384 |    196.732       | 5.083 ms       |        No        |
| Tiny YOLOv3          | 416x416 |    254.681       | 3.926 ms       |        No        |
| YOLOv3               | 416x416 |    20.676       | 48.365 ms       |        No        |
| YOLOv5s              | 640x640 |    60.613       | 16.498 ms       |        No        |
| Unet                 | 384x384 |    4.767       | 209.778 ms       |        No        |
| Lite-HRNet           | 256x192 |    245.761       | 4.069 ms       |        No        |
| CenterNet            | 512x512 |    7.752       | 128.999 ms       |        No        |
