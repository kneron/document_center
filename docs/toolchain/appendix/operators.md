# Hardware Supported Operators

Table below shows the list of operators supports base on ONNX operators.

*The operators NPU supports*

| Node | 520 | 720 | 530 | 630 | 730 |
| --- | --- | --- | --- | --- | --- |
| Abs | N | N | N | N | Y |
| Acos | N | N | N | N | N |
| Acosh | N | N | N | N | N |
| Add | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y |
| And | N | N | N | N | N |
| ArgMax | N | N | N | N | N |
| ArgMin | N | N | N | N | N |
| Asin | N | N | N | N | N |
| Asinh | N | N | N | N | N |
| Atan | N | N | N | N | N |
| Atanh | N | N | N | N | N |
| AveragePool | Y<sub>2</sub> | Y<sub>3</sub> | Y<sub>3</sub> | Y<sub>3</sub> | Y<sub>4</sub> |
| BatchNormalization | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> |
| Bernoulli | N | N | N | N | N |
| BitShift | N | N | N | N | N |
| BitwiseAnd | N | N | N | N | N |
| BitwiseNot | N | N | N | N | N |
| BitwiseOr | N | N | N | N | N |
| BitwiseXor | N | N | N | N | N |
| BlackmanWindow | N | N | N | N | N |
| CastLike | N | N | N | N | N |
| Cast | N | N | N | N | N |
| Ceil | N | N | N | N | N |
| Celu | N | N | N | N | N |
| CenterCropPad | N | N | N | N | N |
| Clip | Y<sub>5</sub> | Y<sub>5</sub> | Y<sub>5</sub> | Y<sub>5</sub> | Y<sub>5</sub> |
| Col2lm | N | N | N | N | N |
| Compress | N | N | N | N | N |
| ConcatFromSequence | N | N | N | N | N |
| Concat | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y |
| ConvInteger | N | N | N | N | N |
| Conv | Y<sub>6</sub> | Y<sub>7</sub> | Y<sub>8</sub> | Y<sub>8</sub> | Y<sub>8</sub> |
| ConvTranspose | N | Y<sub>9</sub> | Y<sub>10</sub> | Y<sub>10</sub> | Y |
| Cos | N | N | N | N | N |
| Cosh | N | N | N | N | N |
| CumSum | N | N | N | N | N |
| DFT | N | N | N | N | N |
| DepthToSpace | Y<sub>11</sub> | Y<sub>11</sub> | Y<sub>12</sub> | Y<sub>12</sub> | Y<sub>12</sub> |
| DequantizeLinear | N | N | N | N | N |
| Det | N | N | N | N | N |
| Div | N<sub>13</sub> | N<sub>13</sub> | Y | Y | Y |
| Dropout | N | N | N | N | N |
| DynamicQuantizeLinear | N | N | N | N | N |
| Einsum | N | N | N | N | N |
| Elu | N | N | Y | Y | Y |
| Equal | N | N | N | N | N |
| Erf | N | N | Y | Y | Y |
| Exp | N | Y<sub>14</sub> | Y | Y | Y |
| Expand | N | Y<sub>15</sub> | Y<sub>16</sub> | Y<sub>16</sub> | Y<sub>16</sub> |
| EyeLike | N | N | N | N | N |
| Flatten | N | Y<sub>17</sub> | Y<sub>17</sub> | Y<sub>17</sub> | Y<sub>17</sub> |
| Floor | N | N | N | N | N |
| GRU | N | N | N | N | N |
| GatherElements | N | N | N | N | N |
| GatherND | N | N | N | N | N |
| Gather | Y<sub>18</sub> | Y<sub>18</sub> | Y<sub>18</sub> | Y<sub>18</sub> | Y<sub>18</sub> |
| Gemm | Y | Y | Y | Y | Y |
| GlobalAveragePool | Y<sub>19</sub> | Y<sub>20</sub> | Y<sub>20</sub> | Y<sub>20</sub> | Y<sub>20</sub> |
| GlobalLpPool | N | N | N | N | N |
| GlobalMaxPool | Y<sub>21</sub> | Y | Y | Y | Y |
| Greater | N | N | N | N | N |
| GreaterOrEqual | N | N | N | N | N |
| GridSample | N | N | N | N | N |
| GroupNormalization | N | N | N | N | N |
| HammingWindow | N | N | N | N | N |
| HannWindow | N | N | N | N | N |
| HardSigmoid | N | N | Y | Y | Y |
| HardSwish | N | N | N | N | N |
| Hardmax | N | N | N | N | N |
| Identity | N | N | N | N | N |
| InstanceNormalization | N | N | N | N | Y |
| IsInf | N | N | N | N | N |
| IsNaN | N | N | N | N | N |
| LRN | N | N | N | N | N |
| LSTM | N | N | N | N | N |
| LayerNormalization | N | N | N | N | Y |
| LeakyRelu | Y | Y | Y | Y | Y |
| Less | N | N | N | N | N |
| LessOrEqual | N | N | N | N | N |
| Log | N | N | N | N | Y |
| LogSoftmax | N | N | N | N | N |
| Loop | N | N | N | N | Y |
| LpNormalization | N | N | N | N | N |
| LpPool | N | N | N | N | N |
| MatMulInteger | N | N | N | N | N |
| MatMul | N | Y<sub>22</sub> | Y<sub>22</sub> | Y<sub>22</sub> | Y<sub>23</sub> |
| Max | N | N | N | N | Y |
| MaxPool | Y<sub>24</sub> | Y<sub>24</sub> | Y<sub>25</sub> | Y<sub>25</sub> | Y<sub>25</sub> |
| MaxRoiPool | N | Y | Y | Y | Y |
| MaxUnpool | N | N | N | N | N |
| Mean | N | N | N | N | N |
| MeanVarianceNormalization | N | N | N | N | N |
| MelWeightMatrix | N | N | N | N | N |
| Min | N | N | N | N | N |
| Mish | N | N | N | N | N |
| Mod | N | N | N | N | N |
| Mul | N | Y<sub>1</sub> | Y<sub>1</sub> | Y<sub>1</sub> | Y |
| Multinomial | N | N | N | N | N |
| Neg | Y | Y | Y | Y | Y |
| NegativeLogLikelihoodLoss | N | N | N | N | N |
| NonMaxSuppression | N | N | N | N | N |
| NonZero | N | N | N | N | N |
| Not | N | N | N | N | N |
| OneHot | N | N | N | N | N |
| Or | N | N | N | N | N |
| PRelu | Y | Y | Y | Y | Y |
| Pad | Y<sub>26</sub> | Y<sub>26</sub> | Y<sub>26</sub> | Y<sub>26</sub> | Y<sub>27</sub> |
| Pow | N<sub>28</sub> | Y<sub>29</sub> | Y<sub>29</sub> | Y<sub>29</sub> | Y<sub>29</sub> |
| QLinearConv | N | N | N | N | N |
| QLinearMatMul | N | N | N | N | N |
| QuantizeLinear | N | N | N | N | N |
| RandomNormalLike | N | N | N | N | N |
| RandomNormal | N | N | N | N | N |
| RandomUniformLike | N | N | N | N | N |
| RandomUniform | N | N | N | N | N |
| Range | N | N | N | N | N |
| Reciprocal | N | N | Y | Y | Y |
| ReduceL1 | N | N | N | N | N |
| ReduceL2 | N | N | N | N | N |
| ReduceLogSumExp | N | N | N | N | N |
| ReduceLogSum | N | N | N | N | N |
| ReduceMax | Y<sub>30</sub> | Y<sub>30</sub> | Y<sub>30</sub> | Y<sub>30</sub> | Y<sub>30</sub> |
| ReduceMean | N | Y<sub>31</sub> | Y<sub>31</sub> | Y<sub>31</sub> | Y<sub>31</sub> |
| ReduceMin | N | N | N | N | Y |
| ReduceProd | N | N | N | N | N |
| ReduceSum | Y<sub>32</sub> | Y<sub>33</sub> | Y<sub>33</sub> | Y<sub>33</sub> | Y |
| ReduceSumSquare | N | N | N | N | N |
| Relu | Y | Y | Y | Y | Y |
| Reshape | N | Y | Y | Y | Y |
| Resize | Y<sub>34</sub> | Y<sub>35</sub> | Y<sub>36</sub> | Y<sub>36</sub> | Y<sub>36</sub> |
| ReverseSequence | N | N | N | N | N |
| RNN | N | N | N | N | N |
| RoiAlign | N | N | N | N | N |
| Round | N | N | N | N | N |
| STFT | N | N | N | N | N |
| ScatterElements | N | N | N | N | N |
| ScatterND | N | N | N | N | N |
| Scatter | N | N | N | N | N |
| Selu | N | N | N | N | N |
| SequenceAt | N | N | N | N | N |
| SequenceConstruct | N | N | N | N | N |
| SequenceEmpty | N | N | N | N | N |
| SequenceErase | N | N | N | N | N |
| SequenceInsert | N | N | N | N | N |
| SequenceLength | N | N | N | N | N |
| Shape | N | N | N | N | N |
| Shrink | N | N | N | N | N |
| Sigmoid | N | Y | Y | Y | Y |
| Sign | N | N | N | N | Y |
| Sin | N | N | N | N | N |
| Sinh | N | N | N | N | N |
| Size | N | N | N | N | N |
| SliceHeader | N | N | N | N | N |
| Slice | N | Y<sub>37</sub> | Y<sub>37</sub> | Y<sub>37</sub> | Y<sub>38</sub> |
| SliceTail | N | N | N | N | N |
| SoftmaxCrossEntropyLoss | N | N | N | N | N |
| Softmax | N | N<sub>39</sub> | Y<sub>40</sub> | Y<sub>40</sub> | Y<sub>40</sub> |
| Softplus | N | N | N | N | N |
| Softsign | N | N | N | N | N |
| SpaceToDepth | N | N | Y<sub>41</sub> | Y<sub>41</sub> | Y<sub>41</sub> |
| Split | N | N | N | N | Y |
| Sqrt | N | N | Y | Y | Y |
| Squeeze | N | N | N | N | N |
| Sub | Y | Y | Y | Y | Y |
| Sum | N | N | N | N | N |
| Tan | N | N | N | N | N |
| Tanh | N | Y | Y | Y | Y |
| ThresholdedRelu | N | N | N | N | N |
| Tile | N | N | N | N | N |
| TopK | N | N | N | N | N |
| Transpose | N | Y<sub>42</sub> | Y<sub>43</sub> | Y<sub>43</sub> | Y |
| Trilu | N | N | N | N | N |
| Unique | N | N | N | N | N |
| Unsqueeze | N | N | N | N | N |
| Upsample | Y<sub>44</sub> | Y<sub>45</sub> | Y<sub>46</sub> | Y<sub>46</sub> | Y<sub>46</sub> |
| Where | N | N | N | N | N |
| Xor | N | N | N | N | N |

Notes:

1. Conditions: rank <= 4D
2. AveragePool 520:
    - decompose conditions:
        - ceil_mode=0, count_include_pad=0, kernel is nxn, stride is nxn where n is power of 2 and n > 3
        - ceil_mode=0, dilations={1,1}, kernel = 1 and stride > 1 (Pure DonwSampling)
        - ceil_mode=0, count_include_pad=0, stride is sxs where s > 3 (DonwSampling)
    - directly support conditions:
        - 2D pool, dilation == 1, kernel is kxk & stride is sxs where k <= 3 and s <= k
3. AveragePool 720/530/630:
    - decompose conditions:
        - ceil_mode=0, count_include_pad=0, kernel is nxn, stride is nxn where n is power of 2 and n > 3
        - ceil_mode=0, dilations={1,1}, kernel = 1 and stride > 1 (Pure DonwSampling)
        - ceil_mode=0, count_include_pad=0, stride is sxs where s > 3 (DonwSampling)
    - directly support conditions:
        - 2D pool, dilation == 1, kernel is kxk & stride is sxs where k and s <= 3 or kernel_w & stride_w are 1 and kernel_h & stride_h <= 3 or kernel_h & stride_h are 1 and kernel_w = stride_w <= 3
4. AveragePool 730:
    - decompose conditions:
        - ceil_mode=0, count_include_pad=0, kernel is nxn and stride is nxn where n is power of 2 and n > 3
        - ceil_mode=0, count_include_pad=0, dilation = 1, kernel = 1 and stride > 1 (Pure DownSampling)
        - ceil_mode=0, count_include_pad=0, stride is sxs and s > 3 (DownSampling)
    - directly support conditions:
        - 1D/2D pool, dilation == 1, kernel is kxk & stride is sxs where k and s <= 3 or kernel is kx1 & stride is sx1 where k and s <= 3 or kernel is 1xn & stride is 1xn where n <= 3

5. conditions: min == 0 && max >= 0
6. conditions: rank <= 4 && kernel <= 12 && stride_w <= 16 && stride_h <= 4
7. conditions: rank <= 4 && stride_w <= 16 && stride_h <= 4
8. conditions: rank <= 4
9. condition: stride is sxs where s = 2
10. condition: stride is sxs
11. decompose contidion: in_shape = 1x4x?x? && out_shape = 1x1x?x? && mode = CRD && blocksize = 2
12. conditions: blocksize == 2 or 4
13. decompose to reciprocal or kneron_inv_sqrt
14. decompose to constant + log2 + mul + pow2
15. conditions: expend on column or row
16. conditions: expend on channel or column or row
17. conditions: axis == 1
18. conditions: single index
19. conditions: rank <= 4 && row * col <= 256
20. conditions: rank <= 4 && row * col <= 16384
21. decompose condition: row > 3
22. conditions:
    - if second input is const
        - const input shape must be WxV or 1x1xWxV
    - else
        - rank = 4
23. conditions:
    - if second input is const
        - const input shape must be WxV or 1x1xWxV
    - else
        - 3 <= rank <= 5
24. Maxpool
    - decompose conditions:
        - 1. ceil_mode=0, dilations={1,1}, kernel = 1 and stride > 1 (Pure DonwSampling)
        - 2. ceil_mode=0, dilations={1,1}, kernel_h=kernel_w=stride_h=stride_w=K where K is power of 2 and K > 3 (DonwSampling)
        - 3. ceil_mode=0, kernel > 3
    - directly support conditions:
        - 2D pool, dilation == 1, kernel is kxk & stride is sxs where 2 <= k <= 3 and s <= k
25. Maxpool
    - decompose conditions:
        - 1. ceil_mode=0, dilations={1,1}, kernel = 1 and stride > 1 (Pure DonwSampling)
        - 2. ceil_mode=0, dilations={1,1}, kernel_h=kernel_w=stride_h=stride_w=K where K is power of 2 and K > 3 (DonwSampling)
        - 3. ceil_mode=0, kernel > 3
    - directly support conditions:
        - 2D pool,
        - dilation == 1,
        - kernel is kxk & stride is sxs where n and s <= 3 or
        - kernel_w & stride_w are 1 and kernel_h & stride_h <= 3 or
        - kernel_h & stride_h are 1 and kernel_w = stride_w <= 3
26. conditions: not pad in batch && any pad in spacial < 32 && constant mode with 0 const_val
27. conditions: not pad in batch && any of pad < 32 && constant mode with 0 const_val
28. power is 2 will be decomposed to KneronSquareNode but npu still not support
29. conditions: power is 2
30. conditions: keepdims = 1 will be decomposed to MaxPool
31. decompose conditions: keepdims = 1 will be decomposed to ReduceSum + KneronScale
32. decompose contitions: keepdims = 1 && reduce in ch will be decomposed to Conv
33. ReduceSum:
    - decompose contitions: keepdims = 1 && reduce in ch will be decomposed to Conv
    - direct support conditions: keepdims = 1 && reduce not in batch
34. Resize:
    - decompose conditions: mode != cubic && extrapolation_value is 0 will be decomposed to KneronResizeNode
    - supported KneronResizeNode: mode = nearest && near_mode = floor
35. Resize:
    - decompose conditions: mode != cubic && extrapolation_value is 0 will be decomposed to KneronResizeNode
    - supported KneronResizeNode: delta_v <= 1 && delta_h <= 1 && not both delta_v and delta_h != 1
36. Resize:
    - decompose conditions: mode != cubic && extrapolation_value is 0 will be decomposed to KneronResizeNode
37. conditions: rank <= 4 && all of steps are 1
38. conditions: all of steps are 1
39. will be decompose to ReduceSum + Div + Exp 
40. will be decompose to ReduceSum + Div + Neg + Add + Exp 
41. conditions: blocksize is 2 or 4
42. conditions: row_col_transpose && ch_row_transpose
43. conditions: transpose not in batch
44. Upsample
    - conditions: mode is nearest or linear or bilinear or align_corner will be decompose to KneronResizeNode
    - supported KneronResizeNode: mode = nearest && near_mode = floor
45. Upsample
    - conditions: mode is nearest or linear or bilinear or align_corner will be decompose to KneronResizeNode
    - supported KneronResizeNode: delta_v <= 1 && delta_h <= 1 && not both delta_v and delta_h != 1
46. Upsample: conditions: mode is nearest or linear or bilinear or align_corner will be decompose to KneronResizeNode


# 以下为原文. 审核后删除.

| Node                          | 520 | 720 | 530 | 630 | 730 |
| ----------------------------- | --- | --- | --- | --- |-----|
| Add                           |  Y<sup>16</sup>  |  Y<sup>16</sup>  |  Y<sup>16</sup>  |  Y<sup>16</sup>  |  Y  |
| AveragePool<sup>1</sup>       |  Y  |  Y  |  Y  |  Y  |  Y  |
| BatchNormalization            |  Y  |  Y  |  Y  |  Y  |  Y  |
| BitShift                      |  N  |  N  |  N  |  N  |  N  |
| Cast                          |  N  |  N  |  N  |  N  |  N  |
| Clip<sup>2</sup>              |  Y  |  Y  |  Y  |  Y  |  Y  |
| Concat                        |  Y  |  Y  |  Y  |  Y  |  Y  |
| Conv                          |  Y  |  Y  |  Y  |  Y  |  Y  |
| ConvTranspose<sup>3</sup>     |  N  |  Y  |  Y  |  Y  |  Y  |
| DepthToSpace<sup>4</sup>      |  N  |  N  |  Y  |  Y  |  Y  |
| Div                           |  N  |  N  |  N  |  N  |  Y  |
| Dropout                       |  Y  |  Y  |  Y  |  Y  |  Y  |
| Elu                           |  N  |  N  |  Y  |  Y  |  Y  |
| Erf                           |  N  |  N  |  Y  |  Y  |  Y  |
| Exp                           |  N  |  N  |  Y  |  Y  |  Y  |
| Expand<sup>5</sup>            |  N  |  N  |  Y  |  Y  |  Y  |
| Flatten<sup>6</sup>           |  Y  |  Y  |  Y  |  Y  |  Y  |
| Floor                         |  N  |  N  |  N  |  N  |  N  |
| Gather                        |  N  |  N  |  N  |  N  |  N  |
| GatherElements                |  N  |  N  |  N  |  N  |  N  |
| GatherND                      |  N  |  N  |  N  |  N  |  N  |
| Gemm                          |  Y  |  Y  |  Y  |  Y  |  Y  |
| GlobalAveragePool<sup>7</sup> |  Y  |  Y  |  Y  |  Y  |  Y  |
| GlobalLpPool                  |  N  |  N  |  N  |  N  |  N  |
| GlobalMaxPool                 |  Y  |  Y  |  Y  |  Y  |  Y  |
| GRU                           |  N  |  Y  |  Y  |  Y  |  Y  |
| Hardmax                       |  N  |  N  |  N  |  N  |  N  |
| HardSigmoid                   |  Y  |  Y  |  Y  |  Y  |  Y  |
| InstanceNormalization         |  N  |  N  |  N  |  N  |  N  |
| LeakyRelu                     |  Y  |  Y  |  Y  |  Y  |  Y  |
| LpNormalization               |  N  |  N  |  N  |  N  |  N  |
| LRN                           |  N  |  N  |  N  |  N  |  N  |
| LSTM                          |  N  |  N  |  N  |  N  |  Y  |
| MatMul                        |  N  |  Y  |  Y  |  Y  |  Y  |
| MaxPool<sup>8</sup>           |  Y  |  Y  |  Y  |  Y  |  Y  |
| MaxRoiPool                    |  N  |  Y  |  Y  |  Y  |  Y  |
| MaxUnpool                     |  N  |  N  |  N  |  N  |  N  |
| Mean                          |  Y  |  Y  |  Y  |  Y  |  Y  |
| Min                           |  N  |  N  |  N  |  N  |  N  |
| Mod                           |  N  |  N  |  N  |  N  |  N  |
| Mul                           |  N  |  Y  |  Y  |  Y  |  Y  |
| Multinomial                   |  N  |  N  |  N  |  N  |  N  |
| Neg                           |  Y  |  Y  |  Y  |  Y  |  Y  |
| NonMaxSuppression             |  N  |  N  |  N  |  N  |  N  |
| NonZero                       |  N  |  N  |  N  |  N  |  N  |
| Not                           |  N  |  N  |  N  |  N  |  N  |
| OneHot                        |  N  |  N  |  N  |  N  |  N  |
| Or                            |  N  |  N  |  N  |  N  |  N  |
| Pad<sup>9</sup>               |  Y  |  Y  |  Y  |  Y  |  Y  |
| Pow<sup>10</sup>              |  N  |  Y  |  Y  |  Y  |  Y  |
| PRelu                         |  Y  |  Y  |  Y  |  Y  |  Y  |
| RandomUniformLike             |  N  |  N  |  N  |  N  |  N  |
| Reciprocal                    |  N  |  Y  |  Y  |  Y  |  Y  |
| ReduceLogSum                  |  N  |  N  |  N  |  N  |  N  |
| ReduceLogSumExp               |  N  |  N  |  N  |  N  |  N  |
| ReduceMax                     |  N  |  N  |  N  |  N  |  Y  |
| ReduceMean<sup>11</sup>       |  Y  |  Y  |  Y  |  Y  |  Y  |
| ReduceSum                     |  Y  |  Y  |  Y  |  Y  |  Y  |
| ReduceSumSquare               |  N  |  Y  |  Y  |  Y  |  Y  |
| Relu                          |  Y  |  Y  |  Y  |  Y  |  Y  |
| Reshape                       |  N  |  Y  |  Y  |  Y  |  Y  |
| Resize<sup>12</sup>           |  N  |  Y  |  Y  |  Y  |  Y  |
| RNN                           |  N  |  Y  |  Y  |  Y  |  Y  |
| RoiAlign                      |  N  |  Y  |  Y  |  Y  |  Y  |
| Selu                          |  N  |  N  |  N  |  N  |  N  |
| Shrink                        |  N  |  N  |  N  |  N  |  N  |
| Sigmoid                       |  N  |  Y  |  Y  |  Y  |  Y  |
| Slice                         |  N  |  Y  |  Y  |  Y  |  Y  |
| Softmax                       |  N  |  N  |  N  |  N  |  Y  |
| Softplus                      |  N  |  N  |  Y  |  Y  |  Y  |
| Softsign                      |  N  |  N  |  Y  |  Y  |  Y  |
| SpaceToDepth<sup>13</sup>     |  N  |  N  |  Y  |  Y  |  Y  |
| Split                         |  Y  |  Y  |  Y  |  Y  |  Y  |
| Squeeze                       |  N  |  N  |  N  |  N  |  N  |
| Sub                           |  Y  |  Y  |  Y  |  Y  |  Y  |
| Sum                           |  Y  |  Y  |  Y  |  Y  |  Y  |
| Tanh                          |  N  |  Y  |  Y  |  Y  |  Y  |
| ThresholdedRelu               |  N  |  N  |  N  |  N  |  N  |
| Tile                          |  N  |  N  |  N  |  N  |  N  |
| Transpose                     |  N  |  Y  |  Y  |  Y  |  Y  |
| Unsqueeze                     |  N  |  N  |  N  |  N  |  N  |
| Upsample<sup>14</sup>         |  N  |  Y  |  Y  |  Y  |  Y  |

Notes:

1. For AveragePool kernel size, 520 and 720 support square kernel up to 3x3. while 530 and 630 also support non-square kernel up to 3x3.
2. All hardware only support Clip with min set to 0.
3. 720 only supports ConvTranspose with stride set to 2.
4. 530 and 630 only support DepthToSpace with blocksize set to 2 or 4.
5. 530 and 630 only support Expand on channel or column and row.
6. 520 and 720 only support Flatten before Gemm.
7. For GlobalAveragePool, 520 and 530 support up to 524888 pixels (input and output together, 8 bit, same for the platforms following). 630 supports up to 262144 pixels. 720 supports up to 1048576 pixels. 
8. For MaxPool kernel size, 520 and 720 support square kernel up to 3x3. while 530 and 630 also support non-square kernel up to 3x3.
9. NPUs only support constant pad mode and constant value set to 0.
10. NPUs only support power set to 2.
11. NPUs only support ReduceMean nodes that behave the same as GlobalAveragePool. And it has the same limitation, too.
12. 720 only supports Resize nodes which work as upsampleing. Same limitation as the Upsample.
13. 530 and 630 only support SpaceToDepth with blocksize set to 2 or 4.
14. 720 only supports Upsample with mode set to bilinear or nearest.
15. LSTM, GRU and RNN currently are only supported in onnx opset 13 after using ONNX Converter conversion.
16. conditions: rank <= 4D