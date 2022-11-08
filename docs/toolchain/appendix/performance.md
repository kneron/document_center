# Kneron Hardware Performance

## Hardware Performance Tables

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
| Inception v3         | 224x224 |    86.2        | 11.6 ms        |        No        |
| Inception v4         | 299x299 |    20.4        | 49.0 ms        |        No        |
| Mobilenet v1         | 224x224 |    437         | 2.29 ms        |        No        |
| Mobilenet v2         | 224x224 |    677         | 1.48 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    310         | 3.22 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    55.6        | 18.0 ms        |        No        |
| OpenPose             | 256x256 |    5.30        | 187 ms         |        No        |
| SRCNN                | 384x384 |    134         | 7.48 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    151         | 6.61 ms        |        No        |
| YOLOv3               | 416x416 |    10.1        | 98.6 ms        |        No        |
| YOLOv5s              | 640x640 |    25.7        | 38.9 ms        |        No        |
| Centernet res101     | 512x512 |    2.84        | 352 ms         |        No        |
| Lite-HRNet           | 256x192 |    136         | 7.38 ms        |        No        |

*Performance simulation result on NPU KDP530:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    64.3        | 15.5 ms        |        No        |
| Inception v4         | 299x299 |    16.5        | 60.5 ms        |        No        |
| Mobilenet v1         | 224x224 |    289         | 3.46 ms        |        No        |
| Mobilenet v2         | 224x224 |    340         | 2.94 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    205         | 4.88 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    35.7        | 28.0 ms        |        No        |
| OpenPose             | 256x256 |    3.61        | 277 ms         |        No        |
| SRCNN                | 384x384 |    54.5        | 18.3 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    72.0        | 13.9 ms        |        No        |
| YOLOv3               | 416x416 |    5.93        | 169 ms         |        No        |
| YOLOv5s              | 640x640 |    16.9        | 59.3 ms        |        No        |
| Centernet res101     | 512x512 |    2.19        | 457 ms         |        No        |
| Unet                 | 384x384 |    0.950       | 1050 ms        |        No        |
| Lite-HRNet           | 256x192 |    52.7        | 19.0 ms        |        No        |

*Performance simulation result on NPU KDP630:*

| Model                | Size    | FPS (npu only) | Time(npu only) | Has CPU node(s)? |
| -------------------- | ------- | -------------- | -------------- | ---------------- |
| Inception v3         | 224x224 |    56.8        | 17.6 ms        |        No        |
| Inception v4         | 299x299 |    16.3        | 61.3 ms        |        No        |
| Mobilenet v1         | 224x224 |    222         | 4.51 ms        |        No        |
| Mobilenet v2         | 224x224 |    215         | 4.66 ms        |        No        |
| Mobilenet v2 ssdlite | 300x300 |    128         | 7.83 ms        |        No        |
| Resnet50 v1.5        | 224x224 |    25.4        | 39.3 ms        |        No        |
| OpenPose             | 256x256 |    5.33        | 187 ms         |        No        |
| SRCNN                | 384x384 |    70.5        | 14.2 ms        |        No        |
| Tiny YOLOv3          | 416x416 |    117         | 8.53 ms        |        No        |
| YOLOv3               | 416x416 |    5.56        | 180 ms         |        No        |
| YOLOv5s              | 640x640 |    19.1        | 52.4 ms        |        No        |
| Unet                 | 384x384 |    1.82        | 549 ms         |        No        |
| Lite-HRNet           | 256x192 |    19.3        | 51.7 ms        |        No        |


## Hardware Supported Operators

Table below shows the list of operators supports base on ONNX operators.

*The operators NPU supports*

| Node                          | 520 | 720 | 530 | 630 |
| ----------------------------- | --- | --- | --- | --- |
| Add                           |  Y  |  Y  |  Y  |  Y  |
| AveragePool<sup>1</sup>       |  Y  |  Y  |  Y  |  Y  |
| BatchNormalization            |  Y  |  Y  |  Y  |  Y  |
| BitShift                      |  N  |  N  |  N  |  N  |
| Cast                          |  N  |  N  |  N  |  N  |
| Clip<sup>2</sup>              |  Y  |  Y  |  Y  |  Y  |
| Concat                        |  Y  |  Y  |  Y  |  Y  |
| Conv                          |  Y  |  Y  |  Y  |  Y  |
| ConvTranspose<sup>3</sup>     |  N  |  Y  |  Y  |  Y  |
| DepthToSpace<sup>4</sup>      |  N  |  N  |  Y  |  Y  |
| Div                           |  N  |  N  |  N  |  N  |
| Dropout                       |  Y  |  Y  |  Y  |  Y  |
| Elu                           |  N  |  N  |  Y  |  Y  |
| Erf                           |  N  |  N  |  Y  |  Y  |
| Exp                           |  N  |  N  |  Y  |  Y  |
| Expand<sup>5</sup>            |  N  |  N  |  Y  |  Y  |
| Flatten<sup>6</sup>           |  Y  |  Y  |  Y  |  Y  |
| Floor                         |  N  |  N  |  N  |  N  |
| Gather                        |  N  |  N  |  N  |  N  |
| GatherElements                |  N  |  N  |  N  |  N  |
| GatherND                      |  N  |  N  |  N  |  N  |
| Gemm                          |  Y  |  Y  |  Y  |  Y  |
| GlobalAveragePool<sup>7</sup> |  Y  |  Y  |  Y  |  Y  |
| GlobalLpPool                  |  N  |  N  |  N  |  N  |
| GlobalMaxPool                 |  Y  |  Y  |  Y  |  Y  |
| GRU                           |  N  |  Y  |  Y  |  Y  |
| Hardmax                       |  N  |  N  |  N  |  N  |
| HardSigmoid                   |  Y  |  Y  |  Y  |  Y  |
| InstanceNormalization         |  N  |  N  |  N  |  N  |
| LeakyRelu                     |  Y  |  Y  |  Y  |  Y  |
| LpNormalization               |  N  |  N  |  N  |  N  |
| LRN                           |  N  |  N  |  N  |  N  |
| LSTM                          |  N  |  Y  |  Y  |  Y  |
| MatMul                        |  Y  |  Y  |  Y  |  Y  |
| MaxPool<sup>8</sup>           |  Y  |  Y  |  Y  |  Y  |
| MaxRoiPool                    |  N  |  Y  |  Y  |  Y  |
| MaxUnpool                     |  N  |  N  |  N  |  N  |
| Mean                          |  Y  |  Y  |  Y  |  Y  |
| Min                           |  N  |  N  |  N  |  N  |
| Mod                           |  N  |  N  |  N  |  N  |
| Mul                           |  N  |  Y  |  Y  |  Y  |
| Multinomial                   |  N  |  N  |  N  |  N  |
| Neg                           |  Y  |  Y  |  Y  |  Y  |
| NonMaxSuppression             |  N  |  N  |  N  |  N  |
| NonZero                       |  N  |  N  |  N  |  N  |
| Not                           |  N  |  N  |  N  |  N  |
| OneHot                        |  N  |  N  |  N  |  N  |
| Or                            |  N  |  N  |  N  |  N  |
| Pad<sup>9</sup>               |  Y  |  Y  |  Y  |  Y  |
| Pow<sup>10</sup>              |  N  |  Y  |  Y  |  Y  |
| PRelu                         |  Y  |  Y  |  Y  |  Y  |
| RandomUniformLike             |  N  |  N  |  N  |  N  |
| ReduceLogSum                  |  N  |  N  |  N  |  N  |
| ReduceLogSumExp               |  N  |  N  |  Y  |  Y  |
| ReduceMax                     |  N  |  N  |  N  |  N  |
| ReduceMean<sup>11</sup>       |  Y  |  Y  |  Y  |  Y  |
| ReduceSum                     |  Y  |  Y  |  Y  |  Y  |
| ReduceSumSquare               |  N  |  Y  |  Y  |  Y  |
| Relu                          |  Y  |  Y  |  Y  |  Y  |
| Reshape                       |  N  |  N  |  Y  |  Y  |
| Resize<sup>12</sup>           |  N  |  Y  |  Y  |  Y  |
| RNN                           |  N  |  Y  |  Y  |  Y  |
| RoiAlign                      |  N  |  Y  |  Y  |  Y  |
| Selu                          |  N  |  N  |  N  |  N  |
| Shrink                        |  N  |  N  |  N  |  N  |
| Sigmoid                       |  N  |  Y  |  Y  |  Y  |
| Slice                         |  N  |  Y  |  Y  |  Y  |
| Softmax                       |  N  |  N  |  Y  |  Y  |
| Softplus                      |  N  |  N  |  Y  |  Y  |
| Softsign                      |  N  |  N  |  Y  |  Y  |
| SpaceToDepth<sup>13</sup>     |  N  |  N  |  Y  |  Y  |
| Split                         |  N  |  Y  |  Y  |  Y  |
| Squeeze                       |  N  |  N  |  N  |  N  |
| Sub                           |  Y  |  Y  |  Y  |  Y  |
| Sum                           |  Y  |  Y  |  Y  |  Y  |
| Tanh                          |  N  |  Y  |  Y  |  Y  |
| ThresholdedRelu               |  N  |  N  |  N  |  N  |
| Tile                          |  N  |  N  |  N  |  N  |
| Transpose                     |  N  |  N  |  Y  |  Y  |
| Unsqueeze                     |  N  |  N  |  N  |  N  |
| Upsample<sup>14</sup>         |  N  |  Y  |  Y  |  Y  |

Notes:

1. For AveragePool kernel size, 520 and 720 support square kernel up to 3x3. while 530 and 630 also support non-square kernel up to 3x3.
2. All hardware only support Clip with min set to 0.
3. 720 only supports ConvTranspose with stride set to 2.
4. 530 and 630 only support DepthToSpace with blocksize set to 2 or 4.
5. 530 and 630 only support Expand on channel or column and row.
6. 520 and 720 only support Flatten before Gemm.
7. 520 only supports GlobalAveragePool on input within 256 pixels while other hardware support up 16384 pixels.
8. For MaxPool kernel size, 520 and 720 support square kernel up to 3x3. while 530 and 630 also support non-square kernel up to 3x3.
9. NPUs only support constant pad mode and constant value set to 0.
10. NPUs only support power set to 2.
11. NPUs only support ReduceMean nodes that behave the same as GlobalAveragePool. And it has the same limitation, too.
12. 720 only supports Resize nodes which work as upsampleing. Same limitation as the Upsample.
13. 530 and 630 only support SpaceToDepth with blocksize set to 2 or 4.
14. 720 only supports Upsample with mode set to bilinear or nearest.
