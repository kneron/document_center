# Hardware Supported Operators

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
| Reshape                       |  N  |  Y  |  Y  |  Y  |
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

