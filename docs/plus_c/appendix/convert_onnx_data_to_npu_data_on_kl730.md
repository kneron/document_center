## Convert ONNX & NPU Data on the KL730 Platform  

> **Note**: For the conversion C implementation please refer the `ex_common/helper_functions.c` and `src/kp_inference.c`.  
> **Note**: For the conversion Python implementation please refer the `python/example/utils/ExampleHelper.py`.  
> **Note**: For the KL730 NPU data layout information please refer the [Supported NPU Data Layout Format (KL730)](./supported_npu_data_layout_format_kl730.md).  

To manually convert ONNX/NPU data, we can utilize the helper functions (C-`helper_convert_onnx_data_to_npu_data`; Python-`convert_onnx_data_to_npu_data`) and the inference retrieve result functions (C-`kp_generic_inference_retrieve_fixed_node/kp_generic_inference_retrieve_float_node`; Python-`kp.generic_inference_retrieve_fixed_node/kp.generic_inference_retrieve_float_node`). However, in most model deployments, it's essential to enhance conversion efficiency and eliminate unnecessary processes significantly. This section briefly overviews the conversion process of ONNX/NPU data conversion.  

You can refer to the helper function's implementation to better understand the conversion process. Then, you can modify and optimize the code in the helper function to improve your conversion flow.  

### Conversion Flow  

The figure below illustrates the data conversion flow: (A) from ONNX input data to NPU inference input data and (B) from NPU inference output data to ONNX output data.  

![](../imgs/onnx_npu_data_conversion.jpg)  

#### Block A: From ONNX Input Data to NPU Inference Input Data  

* Step 1: Floating Point to Fixed Point Conversion  
Converts floating-point data to fixed-point data using a quantization formula with specified scale and radix settings.  

* Step 2: Re-layout to NPU Data  
Rearrange ONNX data into the required format for NPU processing.  

    1. Check the NPU data layout setting and rearrange in different process mechanisms:  
        * 8/16-bit data  
        * High/low 8-bit data format  
        * Outer channel group format  
    2. Calculate the ONNX and NPU data mapping index by npu_stride/onnx_stride information
        * The outer channel group format needs extra index calculations to transform the mapping index.
        * The High/low 8-bit data format must separate the 16-bit data into High/low 8-bit entries.

#### Block B: From NPU Inference Output Data to ONNX Output Data  

* Step 3: Re-layout to ONNX Data  
Rearrange NPU data into the ONNX data layout.  

    1. Check the NPU data layout setting and rearrange in different process mechanisms:  
        * 8/16-bit data  
        * High/low 8-bit data format  
        * Outer channel group format  
    2. Calculate the ONNX and NPU data mapping index by npu_stride/onnx_stride information
        * The outer channel group format needs extra index calculations to transform the mapping index.
        * The High/low 8-bit data format must combine the High/low 8-bit entries into 16-bit data.

* Step 4: Fixed Point to Floating Point Conversion  
Converts fixed-point data to floating-point data using a quantization formula with specified scale and radix settings.  

#### ONNX and NPU Data Mapping Index Calculation

We will explain how the ONNX and NPU data mapping index is calculated. To determine the mapping index between ONNX and NPU data, we need the stride values from the tensor information. These values represent the stride offsets for each axis step.  

* General NPU Data Layout  
    The main steps involve performing the inner product on the specified ONNX data index, using the stride values from both ONNX and NPU. This process allows us to obtain the index that connects the flattened ONNX and NPU data.  

    * Pseudo code in C style  
        ```C
        /**
         * calculate mapping index
         */
        uint32_t onnx_data_index    = 0;
        uint32_t npu_data_index     = 0;

        for (int32_t axis = 0; axis < shape_len; axis++) {
            onnx_data_index    += onnx_data_shape_index[axis] * stride_onnx[axis];
            npu_data_index     += onnx_data_shape_index[axis] * stride_npu[axis];
        }

        /**
         * onnx_data_buffer is flatten ONNX data buffer
         * npu_data_buffer is flatten NPU data buffer
         * 
         * onnx_data_buffer[onnx_data_index] corresponds to npu_data_buffer[npu_data_index]
         */
        ```

    * Pseudo code in Python style  
        ```Python
        """
        calculate mapping index
        """
        onnx_data_index = onnx_data_shape_index.dot(stride_onnx)
        npu_data_index = onnx_data_shape_index.dot(stride_npu)

        """
        onnx_data_buffer is flatten ONNX data buffer
        npu_data_buffer is flatten NPU data buffer

        onnx_data_buffer[onnx_data_index] corresponds to npu_data_buffer[npu_data_index]
        """
        ```

* For Outer Channel Group Format NPU Data Layout (1W16C8B and 1W16C8BHL)  

    > Note: Each channel group aligns 16 channel size.  

    The outer channel group format refers to a specific NPU data layout, where the stride information is reserved for a single channel group. To calculate the mapping index, the channel group stride must be determined. This stride can be found by calculating the maximum value obtained from the element-wise multiplication of the shape with the NPU stride.

    * Pseudo code in C style  
        ```C
        /**
         * find the channel group stride
         */
        uint32_t npu_channel_group_stride_tmp   = 0;
        uint32_t npu_channel_group_stride       = 0;
        uint32_t channel_idx                    = 0;

        for (int axis = 0; axis < (int)shape_len; axis++) {
            if (1 == stride_npu[axis]) {
                channel_idx = axis;
                continue;
            }

            npu_channel_group_stride_tmp = stride_npu[axis] * shape[axis];
            if (npu_channel_group_stride_tmp > npu_channel_group_stride)
                npu_channel_group_stride = npu_channel_group_stride_tmp;
        }

        /**
         * refine the npu_channel_group_stride for reuse
         */
        npu_channel_group_stride -= 16;

        /**
         * calculate mapping index
         */
        uint32_t onnx_data_index    = 0;
        uint32_t npu_data_index     = 0;

        for (int32_t axis = 0; axis < shape_len; axis++) {
            onnx_data_index    += onnx_data_shape_index[axis] * stride_onnx[axis];
            npu_data_index     += onnx_data_shape_index[axis] * stride_npu[axis];
        }

        /**
         * formula: npu_data_index = single_channel_group_npu_index + channel_group_index * channel_group_stride
         * code: npu_data_index += (onnx_data_shape_index[channel_idx] / 16) * npu_channel_group_stride;
         */
        npu_data_index += (onnx_data_shape_index[channel_idx] >> 4) * npu_channel_group_stride;
        ```

    * Pseudo code in Python style  
        ```Python
        """
        find the channel group stride
        """
        channel_idx = np.where(stride_npu == 1)[0][0]
        dimension_stride = stride_npu * shape
        dimension_stride[channel_idx] = 0
        npu_channel_group_stride = np.max(dimension_stride.flatten()) - 16

        """
        refine the npu_channel_group_stride for reuse
        """
        npu_channel_group_stride -= 16

        """
        calculate mapping index
        """
        onnx_data_index = onnx_data_shape_index.dot(stride_onnx)
        npu_data_index = onnx_data_shape_index.dot(stride_npu)

        """
        formula: npu_data_index = single_channel_group_npu_index + channel_group_index * channel_group_stride
        code: npu_data_index += (onnx_data_shape_index[channel_idx] / 16) * npu_channel_group_stride
        """
        npu_data_index += (onnx_data_shape_index[channel_idx] >> 4) * npu_channel_group_stride
        ```

* For High/Low 8-bit NPU Data Layout (4W4C8BHL, 1W16C8BHL, 1W16C8BHL_CH_COMPACT and 16W1C8BHL)  

    > Note: The offset between high/low 8-bit data entities is fixed with 128-bits (16 bytes).  

    To calculate the index for the high and low 8-bit NPU data layout mapping, we first need to determine the head address of the low 8-bit data entity. Given that the offset between high and low 8-bit data entities is fixed at 128 bits (or 16 bytes), we can use the following formula for address calculation:  

    `npu_data_index = (npu_data_index / 16) * 32 + (npu_data_index % 16)`  

    Using this formula, we can find the address of the low 8-bit data entity (npu_data_index) and the high 8-bit data entity (npu_data_index + 16). Finally, we can separate the 16-bit data into high and low 8-bit entities. The high 8 bits are extracted from bits 15 to 8 of the 16-bit data, while the low 8 bits are extracted from bits 7 to 1.  

    * Pseudo code in C style  
        ```C
        /**
         * calculate mapping index
         */
        uint32_t onnx_data_index            = 0;
        uint32_t npu_data_index             = 0;
        uint32_t npu_data_high_bit_offset   = 16;
        uint16_t npu_data_element_u16b      = 0;
        uint16_t npu_data_element_i16b      = 0;
        uint8_t npu_data_element_high_u8b   = 0;
        uint8_t npu_data_element_low_u8b    = 0;

        for (int32_t axis = 0; axis < shape_len; axis++) {
            onnx_data_index    += onnx_data_shape_index[axis] * stride_onnx[axis];
            npu_data_index     += onnx_data_shape_index[axis] * stride_npu[axis];
        }

        /**
         * find the head index of the low 8-bit data entity
         * npu_data_index = (npu_data_index / 16) * 32 + (npu_data_index % 16);
         */
        npu_data_index = ((npu_data_index >> 4) << 5) + (npu_data_index & 15u);

        /**
         * separate 16-bit data to high/low 8-bit data entities
         */
        npu_data_element_i16b                                                   = (int16_t)onnx_data_buf[onnx_data_index];
        npu_data_element_u16b                                                   = ((*((uint16_t *)(&npu_data_element_i16b))) >> 1);
        npu_data_element_low_u8b                                                = (uint8_t)(npu_data_element_u16b & 0x007fu);
        npu_data_element_high_u8b                                               = (uint8_t)((npu_data_element_u16b >> 7) & 0x00ffu);

        /**
         * re-layout high/low 8-bit data entities
         */
        ((uint8_t *)*npu_data_buf)[npu_data_index]                              = npu_data_element_low_u8b;
        ((uint8_t *)*npu_data_buf)[npu_data_index + npu_data_high_bit_offset]   = npu_data_element_high_u8b;
        ```

    * Pseudo code in Python style  
        ```Python
        """
        calculate mapping index
        """
        onnx_data_index = onnx_data_shape_index.dot(stride_onnx)
        npu_data_index = onnx_data_shape_index.dot(stride_npu)
        npu_data_high_bit_offset = 16

        """
        find the head index of the low 8-bit data entity
        npu_data_index = (npu_data_index / 16) * 32 + (npu_data_index % 16)
        """
        npu_data_index = ((npu_data_index >> 4) << 5) + (npu_data_index & 15)

        """
        separate 16-bit data to high/low 8-bit data entities
        """
        npu_data_element_u16b = np.frombuffer(buffer=onnx_quantized_data_flatten[onnx_data_buf_offset].tobytes(), dtype=np.uint16)
        npu_data_element_u16b = (npu_data_element_u16b >> 1)
        npu_data_element_low_u8b = (npu_data_element_u16b & 0x007f).astype(dtype=np.uint8)
        npu_data_element_high_u8b = ((npu_data_element_u16b >> 7) & 0x00ff).astype(dtype=np.uint8)

        """
        re-layout high/low 8-bit data entities
        """
        npu_data_flatten[npu_data_index] = npu_data_element_low_u8b
        npu_data_flatten[npu_data_index + npu_data_high_bit_offset] = npu_data_element_high_u8b
        ```

