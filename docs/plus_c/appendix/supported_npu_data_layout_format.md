## Supported NPU Data Layout Format

**Symbol Description**: P *n* CH *m* is *m*-th channel in *n*-th pixel.  

---

To infer by Kneron NPU, the input/output data must be re-layout by the following uniform feature map format.  

1. **KL520**  

    - Input Data Layout  
        - **4W4C8B** - 4 Column 4 Channel 8-Bit Feature Map Format  
            Using 4-channel format to store RGB input image to save memory space. This format cannot be an output format. Only use as input format.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P3CH3       | P3CH2       | P3CH1       | P3CH0      | P2CH3     | P2CH2     | P2CH1     | P2CH0     | P1CH3     | P1CH2     | P1CH1     | P1CH0     | P0CH3     | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | P7CH3       | P7CH2       | P7CH1       | P7CH0      | P6CH3     | P6CH2     | P6CH1     | P6CH0     | P5CH3     | P5CH2     | P5CH1     | P5CH0     | P4CH3     | P4CH2     | P4CH1    | P4CH0   |
            | Entry #2 | P11CH3      | P11CH2      | P11CH1      | P11CH0     | P10CH3    | P10CH2    | P10CH1    | P10CH0    | P9CH3     | P9CH2     | P9CH1     | P9CH0     | P8CH3     | P8CH2     | P8CH1    | P8CH0   |  

    - Output Data Layout  
        - **16W1C8B** - 16 Column 1 Channel 8-Bit Feature Map Format  
            For the output layer, the feature map is represented in 16W1C8B for parsing easily.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |

2. **KL630, KL720 and KL630**  

    - Input Data Layout  
        - **4W4C8B** - 4 Column 4 Channel 8-Bit Feature Map Format  
            Using 4-channel format to store RGB input image to save memory space. This format cannot be an output format. Only use as input format.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P3CH3       | P3CH2       | P3CH1       | P3CH0      | P2CH3     | P2CH2     | P2CH1     | P2CH0     | P1CH3     | P1CH2     | P1CH1     | P1CH0     | P0CH3     | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | P7CH3       | P7CH2       | P7CH1       | P7CH0      | P6CH3     | P6CH2     | P6CH1     | P6CH0     | P5CH3     | P5CH2     | P5CH1     | P5CH0     | P4CH3     | P4CH2     | P4CH1    | P4CH0   |
            | Entry #2 | P11CH3      | P11CH2      | P11CH1      | P11CH0     | P10CH3    | P10CH2    | P10CH1    | P10CH0    | P9CH3     | P9CH2     | P9CH1     | P9CH0     | P8CH3     | P8CH2     | P8CH1    | P8CH0   |  

        - **1W16C8B**  
            For some input data with non-image dimensions, the data layout format will be 1W16C8B.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P0CH15      | P0CH14      | P0CH13      | P0CH12     | P0CH11    | P0CH10    | P0CH9     | P0CH8     | P0CH7     | P0CH6     | P0CH5     | P0CH4     | P0CH3     | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | P1CH15      | P1CH14      | P1CH13      | P1CH12     | P1CH11    | P1CH10    | P1CH9     | P1CH8     | P1CH7     | P1CH6     | P1CH5     | P1CH4     | P1CH3     | P1CH2     | P1CH1    | P1CH0   |
            | Entry #2 | P2CH15      | P2CH14      | P2CH13      | P2CH12     | P2CH11    | P2CH10    | P2CH9     | P2CH8     | P2CH7     | P2CH6     | P2CH5     | P2CH4     | P2CH3     | P2CH2     | P2CH1    | P2CH0   |  

        - **16W1C8B** - 16 Column 1 Channel 8-Bit Feature Map Format  
            For single channel input data, the data layout format will be 1W16C8B.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |  

    - Output Data Layout  
        - **16W1C8B** - 16 Column 1 Channel 8-Bit Feature Map Format  
            For the output layer, the feature map is represented in 16W1C8B for parsing easily.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |  
