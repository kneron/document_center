## Supported NPU Data Layout Format (KL730)

> **Symbol Description**: P *n* CH *m* G *o* is *m*-th channel in *n*-th pixel, *o*-th channel group.  

To infer by Kneron NPU, the input/output data must be re-layout by the following uniform feature map format.  

- Input Data Layout  
    - 8-Bits Data
        - **4W4C8B** - 4 Column 4 Channel 8-Bits Feature Map Format  
            Using 4-channel format to store RGB input image to save memory space. This format cannot be an output format. Only use as input format.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P3CH3       | P3CH2       | P3CH1       | P3CH0      | P2CH3     | P2CH2     | P2CH1     | P2CH0     | P1CH3     | P1CH2     | P1CH1     | P1CH0     | P0CH3     | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | P7CH3       | P7CH2       | P7CH1       | P7CH0      | P6CH3     | P6CH2     | P6CH1     | P6CH0     | P5CH3     | P5CH2     | P5CH1     | P5CH0     | P4CH3     | P4CH2     | P4CH1    | P4CH0   |
            | Entry #2 | P11CH3      | P11CH2      | P11CH1      | P11CH0     | P10CH3    | P10CH2    | P10CH1    | P10CH0    | P9CH3     | P9CH2     | P9CH1     | P9CH0     | P8CH3     | P8CH2     | P8CH1    | P8CH0   |  

        - **1W16C8B_CH_COMPACT** - 1 Column 16 Channel 8-Bits Feature Map Format in Inner Channel Group Mode  
            For some input data with non-image dimensions, the data layout format will be 1W16C8B_CH_COMPACT.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P0CH15G0    | P0CH14G0    | P0CH13G0    | P0CH12G0   | P0CH11G0  | P0CH10G0  | P0CH9G0   | P0CH8G0   | P0CH7G0   | P0CH6G0   | P0CH5G0   | P0CH4G0   | P0CH3G0   | P0CH2G0   | P0CH1G0  | P0CH0G0  |
            | Entry #1 | P0CH15G1    | P0CH14G1    | P0CH13G1    | P0CH12G1   | P0CH11G1  | P0CH10G1  | P0CH9G1   | P0CH8G1   | P0CH7G1   | P0CH6G1   | P0CH5G1   | P0CH4G1   | P0CH3G1   | P0CH2G1   | P0CH1G1  | P0CH0G1  |
            | Entry #2 | P1CH15G0    | P1CH14G0    | P1CH13G0    | P1CH12G0   | P1CH11G0  | P1CH10G0  | P1CH9G0   | P1CH8G0   | P1CH7G0   | P1CH6G0   | P1CH5G0   | P1CH4G0   | P1CH3G0   | P1CH2G0   | P1CH1G0  | P1CH0G0  |
            | Entry #3 | P1CH15G1    | P1CH14G1    | P1CH13G1    | P1CH12G1   | P1CH11G1  | P1CH10G1  | P1CH9G1   | P1CH8G1   | P1CH7G1   | P1CH6G1   | P1CH5G1   | P1CH4G1   | P1CH3G1   | P1CH2G1   | P1CH1G1  | P1CH0G1  |  

        - **16W1C8B** - 16 Column 1 Channel 8-Bits Feature Map Format  
            For single channel input data, the data layout format will be 1W16C8B.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |  

        - **1W16C8B** 1 Column 16 Channel 8-Bits Feature Map Format in Outer Channel Group Mode  
            For some input data with non-image dimensions, the data layout format will be 1W16C8B.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P0CH15G0    | P0CH14G0    | P0CH13G0    | P0CH12G0   | P0CH11G0  | P0CH10G0  | P0CH9G0   | P0CH8G0   | P0CH7G0   | P0CH6G0   | P0CH5G0   | P0CH4G0   | P0CH3G0   | P0CH2G0   | P0CH1G0  | P0CH0G0  |
            | Entry #1 | P1CH15G0    | P1CH14G0    | P1CH13G0    | P1CH12G0   | P1CH11G0  | P1CH10G0  | P1CH9G0   | P1CH8G0   | P1CH7G0   | P1CH6G0   | P1CH5G0   | P1CH4G0   | P1CH3G0   | P1CH2G0   | P1CH1G0  | P1CH0G0  |
            | Entry #2 | P0CH15G1    | P0CH14G1    | P0CH13G1    | P0CH12G1   | P0CH11G1  | P0CH10G1  | P0CH9G1   | P0CH8G1   | P0CH7G1   | P0CH6G1   | P0CH5G1   | P0CH4G1   | P0CH3G1   | P0CH2G1   | P0CH1G1  | P0CH0G1  |
            | Entry #3 | P1CH15G1    | P1CH14G1    | P1CH13G1    | P1CH12G1   | P1CH11G1  | P1CH10G1  | P1CH9G1   | P1CH8G1   | P1CH7G1   | P1CH6G1   | P1CH5G1   | P1CH4G1   | P1CH3G1   | P1CH2G1   | P1CH1G1  | P1CH0G1  |  

        - **RAW_8B** Sequence 8-Bits Feature Map Format  
            > Assume the ONNX data is in shape 1x3x4x4 (BxCxHxW)   

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0    |
            | Entry #1 | P15CH1      | P14CH1      | P13CH1      | P12CH1     | P11CH1    | P10CH1    | P9CH1     | P8CH1     | P7CH1     | P6CH1     | P5CH1     | P4CH1     | P3CH1     | P2CH1     | P1CH1    | P0CH1    |
            | Entry #2 | P15CH2      | P14CH2      | P13CH2      | P12CH2     | P11CH2    | P10CH2    | P9CH2     | P8CH2     | P7CH2     | P6CH2     | P5CH2     | P4CH2     | P3CH2     | P2CH2     | P1CH2    | P0CH2    |  

        - **HW4C8B_KEEP_A** - Flexible Column 4 Channel 8-Bits Feature Map Format  
            This format utilizes a 4-channel structure to store RGBA input images, optimizing memory usage. Note that this format is intended solely for input and cannot be used as an output format.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P3CH3       | P3CH2       | P3CH1       | P3CH0      | P2CH3     | P2CH2     | P2CH1     | P2CH0     | P1CH3     | P1CH2     | P1CH1     | P1CH0     | P0CH3     | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | P7CH3       | P7CH2       | P7CH1       | P7CH0      | P6CH3     | P6CH2     | P6CH1     | P6CH0     | P5CH3     | P5CH2     | P5CH1     | P5CH0     | P4CH3     | P4CH2     | P4CH1    | P4CH0   |
            | Entry #2 | P11CH3      | P11CH2      | P11CH1      | P11CH0     | P10CH3    | P10CH2    | P10CH1    | P10CH0    | P9CH3     | P9CH2     | P9CH1     | P9CH0     | P8CH3     | P8CH2     | P8CH1    | P8CH0   |  

        - **HW4C8B_DROP_A** - Flexible Column 4-Channel 8-Bit Feature Map Format  
            This format utilizes four channels to store RGB input images without an alpha channel, thereby optimizing memory usage. Please note that this format is intended solely for input and cannot be used for output.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|---------|
            | Entry #0 | 0           | P3CH2       | P3CH1       | P3CH0      | 0         | P2CH2     | P2CH1     | P2CH0     | 0         | P1CH2     | P1CH1     | P1CH0     | 0         | P0CH2     | P0CH1    | P0CH0   |
            | Entry #1 | 0           | P7CH2       | P7CH1       | P7CH0      | 0         | P6CH2     | P6CH1     | P6CH0     | 0         | P5CH2     | P5CH1     | P5CH0     | 0         | P4CH2     | P4CH1    | P4CH0   |
            | Entry #2 | 0           | P11CH2      | P11CH1      | P11CH0     | 0         | P10CH2    | P10CH1    | P10CH0    | 0         | P9CH2     | P9CH1     | P9CH0     | 0         | P8CH2     | P8CH1    | P8CH0   |  

        - **HW1C8B** - Flexible Column 1 Channel 8-Bits Feature Map Format  
            Using 1-channel format to store grayscale input image to save memory space. This format cannot be an output format. Only use as input format.  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |  

    - 16-Bits Data  
        - **8W1C16B** - 8 Column 1 Channel 16-Bits Feature Map Format  

            | Bits     | \[127:112\] | \[111:96\] | \[95:80\] | \[79:64\] | \[63:48\] | \[47:32\] | \[31:16\] | \[15:0\]  |
            |----------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
            | Entry #0 | P7CH0       | P6CH0      | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0     | P0CH0     |
            | Entry #1 | P15CH0      | P14CH0     | P13CH0    | P12CH0    | P11CH0    | P10CH0    | P9CH0     | P8CH0     |
            | Entry #2 | P23CH0      | P22CH0     | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0    | P16CH0    |  

        - **4W4C8BHL** - 4 Column 4 Channel 16-Bits High Low Feature Map Format  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P3CH3L      | P3CH2L      | P3CH1L      | P3CH0L     | P2CH3L    | P2CH2L    | P2CH1L    | P2CH0L    | P1CH3L    | P1CH2L    | P1CH1L    | P1CH0L    | P0CH3L    | P0CH2L    | P0CH1L   | P0CH0L   |
            | Entry #1 | P3CH3H      | P3CH2H      | P3CH1H      | P3CH0H     | P2CH3H    | P2CH2H    | P2CH1H    | P2CH0H    | P1CH3H    | P1CH2H    | P1CH1H    | P1CH0H    | P0CH3H    | P0CH2H    | P0CH1H   | P0CH0H   |
            | Entry #2 | P7CH3L      | P7CH2L      | P7CH1L      | P7CH0L     | P6CH3L    | P6CH2L    | P6CH1L    | P6CH0L    | P5CH3L    | P5CH2L    | P5CH1L    | P5CH0L    | P4CH3L    | P4CH2L    | P4CH1L   | P4CH0L   |
            | Entry #3 | P7CH3H      | P7CH2H      | P7CH1H      | P7CH0H     | P6CH3H    | P6CH2H    | P6CH1H    | P6CH0H    | P5CH3H    | P5CH2H    | P5CH1H    | P5CH0H    | P4CH3H    | P4CH2H    | P4CH1H   | P4CH0H   |  

        - **1W16C8BHL** - 1 Column 16 Channel 16-Bits Feature Map Format in Outer Channel Group Mode  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]   |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|-----------|
            | Entry #0 | P0CH15G0L   | P0CH14G0L   | P0CH13G0L   | P0CH12G0L  | P0CH11G0L | P0CH10G0L | P0CH9G0L  | P0CH8G0L  | P0CH7G0L  | P0CH6G0L  | P0CH5G0L  | P0CH4G0L  | P0CH3G0L  | P0CH2G0L  | P0CH1G0L | P0CH0G0L  |
            | Entry #1 | P0CH15G0H   | P0CH14G0H   | P0CH13G0H   | P0CH12G0H  | P0CH11G0H | P0CH10G0H | P0CH9G0H  | P0CH8G0H  | P0CH7G0H  | P0CH6G0H  | P0CH5G0H  | P0CH4G0H  | P0CH3G0H  | P0CH2G0H  | P0CH1G0H | P0CH0G0H  |
            | Entry #2 | P1CH15G0L   | P1CH14G0L   | P1CH13G0L   | P1CH12G0L  | P1CH11G0L | P1CH10G0L | P1CH9G0L  | P1CH8G0L  | P1CH7G0L  | P1CH6G0L  | P1CH5G0L  | P1CH4G0L  | P1CH3G0L  | P1CH2G0L  | P1CH1G0L | P1CH0G0L  |
            | Entry #3 | P1CH15G0H   | P1CH14G0H   | P1CH13G0H   | P1CH12G0H  | P1CH11G0H | P1CH10G0H | P1CH9G0H  | P1CH8G0H  | P1CH7G0H  | P1CH6G0H  | P1CH5G0H  | P1CH4G0H  | P1CH3G0H  | P1CH2G0H  | P1CH1G0H | P1CH0G0H  |
            | Entry #4 | P0CH15G1L   | P0CH14G1L   | P0CH13G1L   | P0CH12G1L  | P0CH11G1L | P0CH10G1L | P0CH9G1L  | P0CH8G1L  | P0CH7G1L  | P0CH6G1L  | P0CH5G1L  | P0CH4G1L  | P0CH3G1L  | P0CH2G1L  | P0CH1G1L | P0CH0G1L  |
            | Entry #5 | P0CH15G1H   | P0CH14G1H   | P0CH13G1H   | P0CH12G1H  | P0CH11G1H | P0CH10G1H | P0CH9G1H  | P0CH8G1H  | P0CH7G1H  | P0CH6G1H  | P0CH5G1H  | P0CH4G1H  | P0CH3G1H  | P0CH2G1H  | P0CH1G1H | P0CH0G1H  |
            | Entry #6 | P1CH15G1L   | P1CH14G1L   | P1CH13G1L   | P1CH12G1L  | P1CH11G1L | P1CH10G1L | P1CH9G1L  | P1CH8G1L  | P1CH7G1L  | P1CH6G1L  | P1CH5G1L  | P1CH4G1L  | P1CH3G1L  | P1CH2G1L  | P1CH1G1L | P1CH0G1L  |
            | Entry #7 | P1CH15G1H   | P1CH14G1H   | P1CH13G1H   | P1CH12G1H  | P1CH11G1H | P1CH10G1H | P1CH9G1H  | P1CH8G1H  | P1CH7G1H  | P1CH6G1H  | P1CH5G1H  | P1CH4G1H  | P1CH3G1H  | P1CH2G1H  | P1CH1G1H | P1CH0G1H  |  

        - **16W1C8BHL** - 16 Column 1 Channel 16-Bits Feature Map Format  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P15CH0L     | P14CH0L     | P13CH0L     | P12CH0L    | P11CH0L   | P10CH0L   | P9CH0L    | P8CH0L    | P7CH0L    | P6CH0L    | P5CH0L    | P4CH0L    | P3CH0L    | P2CH0L    | P1CH0L   | P0CH0L   |
            | Entry #1 | P15CH0H     | P14CH0H     | P13CH0H     | P12CH0H    | P11CH0H   | P10CH0H   | P9CH0H    | P8CH0H    | P7CH0H    | P6CH0H    | P5CH0H    | P4CH0H    | P3CH0H    | P2CH0H    | P1CH0H   | P0CH0H   |
            | Entry #2 | P31CH0L     | P30CH0L     | P29CH0L     | P28CH0L    | P27CH0L   | P26CH0L   | P25CH0L   | P24CH0L   | P23CH0L   | P22CH0L   | P21CH0L   | P20CH0L   | P19CH0L   | P18CH0L   | P17CH0L  | P16CH0L  |
            | Entry #3 | P31CH0H     | P30CH0H     | P29CH0H     | P28CH0H    | P27CH0H   | P26CH0H   | P25CH0H   | P24CH0H   | P23CH0H   | P22CH0H   | P21CH0H   | P20CH0H   | P19CH0H   | P18CH0H   | P17CH0H  | P16CH0H  |  

        - **1W16C8BHL_CH_COMPACT** - 1 Column 16 Channel 16-Bits Feature Map Format in Inner Channel Group Mode  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]   |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|-----------|
            | Entry #0 | P0CH15G0L   | P0CH14G0L   | P0CH13G0L   | P0CH12G0L  | P0CH11G0L | P0CH10G0L | P0CH9G0L  | P0CH8G0L  | P0CH7G0L  | P0CH6G0L  | P0CH5G0L  | P0CH4G0L  | P0CH3G0L  | P0CH2G0L  | P0CH1G0L | P0CH0G0L  |
            | Entry #1 | P0CH15G0H   | P0CH14G0H   | P0CH13G0H   | P0CH12G0H  | P0CH11G0H | P0CH10G0H | P0CH9G0H  | P0CH8G0H  | P0CH7G0H  | P0CH6G0H  | P0CH5G0H  | P0CH4G0H  | P0CH3G0H  | P0CH2G0H  | P0CH1G0H | P0CH0G0H  |
            | Entry #2 | P0CH15G1L   | P0CH14G1L   | P0CH13G1L   | P0CH12G1L  | P0CH11G1L | P0CH10G1L | P0CH9G1L  | P0CH8G1L  | P0CH7G1L  | P0CH6G1L  | P0CH5G1L  | P0CH4G1L  | P0CH3G1L  | P0CH2G1L  | P0CH1G1L | P0CH0G1L  |
            | Entry #3 | P0CH15G1H   | P0CH14G1H   | P0CH13G1H   | P0CH12G1H  | P0CH11G1H | P0CH10G1H | P0CH9G1H  | P0CH8G1H  | P0CH7G1H  | P0CH6G1H  | P0CH5G1H  | P0CH4G1H  | P0CH3G1H  | P0CH2G1H  | P0CH1G1H | P0CH0G1H  |
            | Entry #4 | P1CH15G0L   | P1CH14G0L   | P1CH13G0L   | P1CH12G0L  | P1CH11G0L | P1CH10G0L | P1CH9G0L  | P1CH8G0L  | P1CH7G0L  | P1CH6G0L  | P1CH5G0L  | P1CH4G0L  | P1CH3G0L  | P1CH2G0L  | P1CH1G0L | P1CH0G0L  |
            | Entry #5 | P1CH15G0H   | P1CH14G0H   | P1CH13G0H   | P1CH12G0H  | P1CH11G0H | P1CH10G0H | P1CH9G0H  | P1CH8G0H  | P1CH7G0H  | P1CH6G0H  | P1CH5G0H  | P1CH4G0H  | P1CH3G0H  | P1CH2G0H  | P1CH1G0H | P1CH0G0H  |
            | Entry #6 | P1CH15G1L   | P1CH14G1L   | P1CH13G1L   | P1CH12G1L  | P1CH11G1L | P1CH10G1L | P1CH9G1L  | P1CH8G1L  | P1CH7G1L  | P1CH6G1L  | P1CH5G1L  | P1CH4G1L  | P1CH3G1L  | P1CH2G1L  | P1CH1G1L | P1CH0G1L  |
            | Entry #7 | P1CH15G1H   | P1CH14G1H   | P1CH13G1H   | P1CH12G1H  | P1CH11G1H | P1CH10G1H | P1CH9G1H  | P1CH8G1H  | P1CH7G1H  | P1CH6G1H  | P1CH5G1H  | P1CH4G1H  | P1CH3G1H  | P1CH2G1H  | P1CH1G1H | P1CH0G1H  |  

        - **RAW_16B** Sequence 16-Bits Feature Map Format  

            > Assume the ONNX data is in shape 1x3x2x4 (BxCxHxW)   

            | Bits     | \[127:112\] | \[111:96\] | \[95:80\] | \[79:64\] | \[63:48\] | \[47:32\] | \[31:16\] | \[15:0\]  |
            |----------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
            | Entry #0 | P7CH0       | P6CH0      | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0     | P0CH0     |
            | Entry #1 | P15CH1      | P14CH1     | P13CH1    | P12CH1    | P11CH1    | P10CH1    | P9CH1     | P8CH1     |
            | Entry #2 | P23CH2      | P22CH2     | P21CH2    | P20CH2    | P19CH2    | P18CH2    | P17CH2    | P16CH2    |  

        - **HW1C16B_LE** - Flexible Column 1 Channel 16-Bits Feature Map Format (Store in Little-Endian)  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|---------|
            | Entry #0 | P7CH0H      | P7CH0L      | P6CH0H      | P6CH0L     | P5CH0H    | P5CH0L    | P4CH0H    | P4CH0L    | P3CH0H    | P3CH0L    | P2CH0H    | P2CH0L    | P1CH0H    | P1CH0L    | P0CH0H   | P0CH0L  |
            | Entry #1 | P15CH0H     | P15CH0L     | P14CH0H     | P14CH0L    | P13CH0H   | P13CH0L   | P12CH0H   | P12CH0L   | P11CH0H   | P11CH0L   | P10CH0H   | P10CH0L   | P9CH0H    | P9CH0L    | P8CH0H   | P8CH0L  |
            | Entry #2 | P23CH0H     | P23CH0L     | P22CH0H     | P22CH0L    | P21CH0H   | P21CH0L   | P20CH0H   | P20CH0L   | P19CH0H   | P19CH0L   | P18CH0H   | P18CH0L   | P17CH0H   | P17CH0L   | P16CH0H  | P16CH0L |  

        - **HW1C16B_BE** - Flexible Column 1 Channel 16-Bits Feature Map Format (Store in Big-Endian)  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|---------|
            | Entry #0 | P7CH0L      | P7CH0H      | P6CH0L      | P6CH0H     | P5CH0L    | P5CH0H    | P4CH0L    | P4CH0H    | P3CH0L    | P3CH0H    | P2CH0L    | P2CH0H    | P1CH0L    | P1CH0H    | P0CH0L   | P0CH0H  |
            | Entry #1 | P15CH0L     | P15CH0H     | P14CH0L     | P14CH0H    | P13CH0L   | P13CH0H   | P12CH0L   | P12CH0H   | P11CH0L   | P11CH0H   | P10CH0L   | P10CH0H   | P9CH0L    | P9CH0H    | P8CH0L   | P8CH0H  |
            | Entry #2 | P23CH0L     | P23CH0H     | P22CH0L     | P22CH0H    | P21CH0L   | P21CH0H   | P20CH0L   | P20CH0H   | P19CH0L   | P19CH0H   | P18CH0L   | P18CH0H   | P17CH0L   | P17CH0H   | P16CH0L  | P16CH0H |  

- Output Data Layout  
    - 8-Bits Data  
        - **1W16C8B_CH_COMPACT** - 1 Column 16 Channel 8-Bits Feature Map Format in Inner Channel Group Mode  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P0CH15G0    | P0CH14G0    | P0CH13G0    | P0CH12G0   | P0CH11G0  | P0CH10G0  | P0CH9G0   | P0CH8G0   | P0CH7G0   | P0CH6G0   | P0CH5G0   | P0CH4G0   | P0CH3G0   | P0CH2G0   | P0CH1G0  | P0CH0G0  |
            | Entry #1 | P0CH15G1    | P0CH14G1    | P0CH13G1    | P0CH12G1   | P0CH11G1  | P0CH10G1  | P0CH9G1   | P0CH8G1   | P0CH7G1   | P0CH6G1   | P0CH5G1   | P0CH4G1   | P0CH3G1   | P0CH2G1   | P0CH1G1  | P0CH0G1  |
            | Entry #2 | P1CH15G0    | P1CH14G0    | P1CH13G0    | P1CH12G0   | P1CH11G0  | P1CH10G0  | P1CH9G0   | P1CH8G0   | P1CH7G0   | P1CH6G0   | P1CH5G0   | P1CH4G0   | P1CH3G0   | P1CH2G0   | P1CH1G0  | P1CH0G0  |
            | Entry #3 | P1CH15G1    | P1CH14G1    | P1CH13G1    | P1CH12G1   | P1CH11G1  | P1CH10G1  | P1CH9G1   | P1CH8G1   | P1CH7G1   | P1CH6G1   | P1CH5G1   | P1CH4G1   | P1CH3G1   | P1CH2G1   | P1CH1G1  | P1CH0G1  |  

        - **16W1C8B** - 16 Column 1 Channel 8-Bits Feature Map Format  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\] |
            | -------- | ----------- | ----------- | ----------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | -------- | ------- |
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0   |
            | Entry #1 | P31CH0      | P30CH0      | P29CH0      | P28CH0     | P27CH0    | P26CH0    | P25CH0    | P24CH0    | P23CH0    | P22CH0    | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0   | P16CH0  |
            | Entry #2 | P47CH0      | P46CH0      | P45CH0      | P44CH0     | P43CH0    | P42CH0    | P41CH0    | P40CH0    | P39CH0    | P38CH0    | P37CH0    | P36CH0    | P35CH0    | P34CH0    | P33CH0   | P32CH0  |  

        - **1W16C8B** 1 Column 16 Channel 8-Bits Feature Map Format in Outer Channel Group Mode  

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P0CH15G0    | P0CH14G0    | P0CH13G0    | P0CH12G0   | P0CH11G0  | P0CH10G0  | P0CH9G0   | P0CH8G0   | P0CH7G0   | P0CH6G0   | P0CH5G0   | P0CH4G0   | P0CH3G0   | P0CH2G0   | P0CH1G0  | P0CH0G0  |
            | Entry #1 | P1CH15G0    | P1CH14G0    | P1CH13G0    | P1CH12G0   | P1CH11G0  | P1CH10G0  | P1CH9G0   | P1CH8G0   | P1CH7G0   | P1CH6G0   | P1CH5G0   | P1CH4G0   | P1CH3G0   | P1CH2G0   | P1CH1G0  | P1CH0G0  |
            | Entry #2 | P0CH15G1    | P0CH14G1    | P0CH13G1    | P0CH12G1   | P0CH11G1  | P0CH10G1  | P0CH9G1   | P0CH8G1   | P0CH7G1   | P0CH6G1   | P0CH5G1   | P0CH4G1   | P0CH3G1   | P0CH2G1   | P0CH1G1  | P0CH0G1  |
            | Entry #3 | P1CH15G1    | P1CH14G1    | P1CH13G1    | P1CH12G1   | P1CH11G1  | P1CH10G1  | P1CH9G1   | P1CH8G1   | P1CH7G1   | P1CH6G1   | P1CH5G1   | P1CH4G1   | P1CH3G1   | P1CH2G1   | P1CH1G1  | P1CH0G1  |  

        - **RAW_8B** Sequence 8-Bits Feature Map Format  
            > Assume the ONNX data is in shape 1x3x4x4 (BxCxHxW)   

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P15CH0      | P14CH0      | P13CH0      | P12CH0     | P11CH0    | P10CH0    | P9CH0     | P8CH0     | P7CH0     | P6CH0     | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0    | P0CH0    |
            | Entry #1 | P15CH1      | P14CH1      | P13CH1      | P12CH1     | P11CH1    | P10CH1    | P9CH1     | P8CH1     | P7CH1     | P6CH1     | P5CH1     | P4CH1     | P3CH1     | P2CH1     | P1CH1    | P0CH1    |
            | Entry #2 | P15CH2      | P14CH2      | P13CH2      | P12CH2     | P11CH2    | P10CH2    | P9CH2     | P8CH2     | P7CH2     | P6CH2     | P5CH2     | P4CH2     | P3CH2     | P2CH2     | P1CH2    | P0CH2    |  

    - 16-Bits Data  
        - **8W1C16B** - 8 Column 1 Channel 16-Bits Feature Map Format  

            | Bits     | \[127:112\] | \[111:96\] | \[95:80\] | \[79:64\] | \[63:48\] | \[47:32\] | \[31:16\] | \[15:0\]  |
            |----------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
            | Entry #0 | P7CH0       | P6CH0      | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0     | P0CH0     |
            | Entry #1 | P15CH0      | P14CH0     | P13CH0    | P12CH0    | P11CH0    | P10CH0    | P9CH0     | P8CH0     |
            | Entry #2 | P23CH0      | P22CH0     | P21CH0    | P20CH0    | P19CH0    | P18CH0    | P17CH0    | P16CH0    |  

        - **4W4C8BHL** - 4 Column 4 Channel 16-Bits High Low Feature Map Format  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P3CH3L      | P3CH2L      | P3CH1L      | P3CH0L     | P2CH3L    | P2CH2L    | P2CH1L    | P2CH0L    | P1CH3L    | P1CH2L    | P1CH1L    | P1CH0L    | P0CH3L    | P0CH2L    | P0CH1L   | P0CH0L   |
            | Entry #1 | P3CH3H      | P3CH2H      | P3CH1H      | P3CH0H     | P2CH3H    | P2CH2H    | P2CH1H    | P2CH0H    | P1CH3H    | P1CH2H    | P1CH1H    | P1CH0H    | P0CH3H    | P0CH2H    | P0CH1H   | P0CH0H   |
            | Entry #2 | P7CH3L      | P7CH2L      | P7CH1L      | P7CH0L     | P6CH3L    | P6CH2L    | P6CH1L    | P6CH0L    | P5CH3L    | P5CH2L    | P5CH1L    | P5CH0L    | P4CH3L    | P4CH2L    | P4CH1L   | P4CH0L   |
            | Entry #3 | P7CH3H      | P7CH2H      | P7CH1H      | P7CH0H     | P6CH3H    | P6CH2H    | P6CH1H    | P6CH0H    | P5CH3H    | P5CH2H    | P5CH1H    | P5CH0H    | P4CH3H    | P4CH2H    | P4CH1H   | P4CH0H   |  

        - **1W16C8BHL** - 1 Column 16 Channel 16-Bits Feature Map Format in Outer Channel Group Mode  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]   |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|-----------|
            | Entry #0 | P0CH15G0L   | P0CH14G0L   | P0CH13G0L   | P0CH12G0L  | P0CH11G0L | P0CH10G0L | P0CH9G0L  | P0CH8G0L  | P0CH7G0L  | P0CH6G0L  | P0CH5G0L  | P0CH4G0L  | P0CH3G0L  | P0CH2G0L  | P0CH1G0L | P0CH0G0L  |
            | Entry #1 | P0CH15G0H   | P0CH14G0H   | P0CH13G0H   | P0CH12G0H  | P0CH11G0H | P0CH10G0H | P0CH9G0H  | P0CH8G0H  | P0CH7G0H  | P0CH6G0H  | P0CH5G0H  | P0CH4G0H  | P0CH3G0H  | P0CH2G0H  | P0CH1G0H | P0CH0G0H  |
            | Entry #2 | P1CH15G0L   | P1CH14G0L   | P1CH13G0L   | P1CH12G0L  | P1CH11G0L | P1CH10G0L | P1CH9G0L  | P1CH8G0L  | P1CH7G0L  | P1CH6G0L  | P1CH5G0L  | P1CH4G0L  | P1CH3G0L  | P1CH2G0L  | P1CH1G0L | P1CH0G0L  |
            | Entry #3 | P1CH15G0H   | P1CH14G0H   | P1CH13G0H   | P1CH12G0H  | P1CH11G0H | P1CH10G0H | P1CH9G0H  | P1CH8G0H  | P1CH7G0H  | P1CH6G0H  | P1CH5G0H  | P1CH4G0H  | P1CH3G0H  | P1CH2G0H  | P1CH1G0H | P1CH0G0H  |
            | Entry #4 | P0CH15G1L   | P0CH14G1L   | P0CH13G1L   | P0CH12G1L  | P0CH11G1L | P0CH10G1L | P0CH9G1L  | P0CH8G1L  | P0CH7G1L  | P0CH6G1L  | P0CH5G1L  | P0CH4G1L  | P0CH3G1L  | P0CH2G1L  | P0CH1G1L | P0CH0G1L  |
            | Entry #5 | P0CH15G1H   | P0CH14G1H   | P0CH13G1H   | P0CH12G1H  | P0CH11G1H | P0CH10G1H | P0CH9G1H  | P0CH8G1H  | P0CH7G1H  | P0CH6G1H  | P0CH5G1H  | P0CH4G1H  | P0CH3G1H  | P0CH2G1H  | P0CH1G1H | P0CH0G1H  |
            | Entry #6 | P1CH15G1L   | P1CH14G1L   | P1CH13G1L   | P1CH12G1L  | P1CH11G1L | P1CH10G1L | P1CH9G1L  | P1CH8G1L  | P1CH7G1L  | P1CH6G1L  | P1CH5G1L  | P1CH4G1L  | P1CH3G1L  | P1CH2G1L  | P1CH1G1L | P1CH0G1L  |
            | Entry #7 | P1CH15G1H   | P1CH14G1H   | P1CH13G1H   | P1CH12G1H  | P1CH11G1H | P1CH10G1H | P1CH9G1H  | P1CH8G1H  | P1CH7G1H  | P1CH6G1H  | P1CH5G1H  | P1CH4G1H  | P1CH3G1H  | P1CH2G1H  | P1CH1G1H | P1CH0G1H  |  

        - **16W1C8BHL** - 16 Column 1 Channel 16-Bits Feature Map Format  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]  |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|
            | Entry #0 | P15CH0L     | P14CH0L     | P13CH0L     | P12CH0L    | P11CH0L   | P10CH0L   | P9CH0L    | P8CH0L    | P7CH0L    | P6CH0L    | P5CH0L    | P4CH0L    | P3CH0L    | P2CH0L    | P1CH0L   | P0CH0L   |
            | Entry #1 | P15CH0H     | P14CH0H     | P13CH0H     | P12CH0H    | P11CH0H   | P10CH0H   | P9CH0H    | P8CH0H    | P7CH0H    | P6CH0H    | P5CH0H    | P4CH0H    | P3CH0H    | P2CH0H    | P1CH0H   | P0CH0H   |
            | Entry #2 | P31CH0L     | P30CH0L     | P29CH0L     | P28CH0L    | P27CH0L   | P26CH0L   | P25CH0L   | P24CH0L   | P23CH0L   | P22CH0L   | P21CH0L   | P20CH0L   | P19CH0L   | P18CH0L   | P17CH0L  | P16CH0L  |
            | Entry #3 | P31CH0H     | P30CH0H     | P29CH0H     | P28CH0H    | P27CH0H   | P26CH0H   | P25CH0H   | P24CH0H   | P23CH0H   | P22CH0H   | P21CH0H   | P20CH0H   | P19CH0H   | P18CH0H   | P17CH0H  | P16CH0H  |  

        - **1W16C8BHL_CH_COMPACT** - 1 Column 16 Channel 16-Bits Feature Map Format in Inner Channel Group Mode  
            In high-low NPU format, 16-bit data will be stored in high 8-bits and low 8-bits.

            | Bits     | \[127:120\] | \[119:112\] | \[111:104\] | \[103:96\] | \[95:88\] | \[87:80\] | \[79:72\] | \[71:64\] | \[63:56\] | \[55:48\] | \[47:40\] | \[39:32\] | \[31:24\] | \[23:16\] | \[15:8\] | \[7:0\]   |
            |----------|-------------|-------------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|-----------|
            | Entry #0 | P0CH15G0L   | P0CH14G0L   | P0CH13G0L   | P0CH12G0L  | P0CH11G0L | P0CH10G0L | P0CH9G0L  | P0CH8G0L  | P0CH7G0L  | P0CH6G0L  | P0CH5G0L  | P0CH4G0L  | P0CH3G0L  | P0CH2G0L  | P0CH1G0L | P0CH0G0L  |
            | Entry #1 | P0CH15G0H   | P0CH14G0H   | P0CH13G0H   | P0CH12G0H  | P0CH11G0H | P0CH10G0H | P0CH9G0H  | P0CH8G0H  | P0CH7G0H  | P0CH6G0H  | P0CH5G0H  | P0CH4G0H  | P0CH3G0H  | P0CH2G0H  | P0CH1G0H | P0CH0G0H  |
            | Entry #2 | P0CH15G1L   | P0CH14G1L   | P0CH13G1L   | P0CH12G1L  | P0CH11G1L | P0CH10G1L | P0CH9G1L  | P0CH8G1L  | P0CH7G1L  | P0CH6G1L  | P0CH5G1L  | P0CH4G1L  | P0CH3G1L  | P0CH2G1L  | P0CH1G1L | P0CH0G1L  |
            | Entry #3 | P0CH15G1H   | P0CH14G1H   | P0CH13G1H   | P0CH12G1H  | P0CH11G1H | P0CH10G1H | P0CH9G1H  | P0CH8G1H  | P0CH7G1H  | P0CH6G1H  | P0CH5G1H  | P0CH4G1H  | P0CH3G1H  | P0CH2G1H  | P0CH1G1H | P0CH0G1H  |
            | Entry #4 | P1CH15G0L   | P1CH14G0L   | P1CH13G0L   | P1CH12G0L  | P1CH11G0L | P1CH10G0L | P1CH9G0L  | P1CH8G0L  | P1CH7G0L  | P1CH6G0L  | P1CH5G0L  | P1CH4G0L  | P1CH3G0L  | P1CH2G0L  | P1CH1G0L | P1CH0G0L  |
            | Entry #5 | P1CH15G0H   | P1CH14G0H   | P1CH13G0H   | P1CH12G0H  | P1CH11G0H | P1CH10G0H | P1CH9G0H  | P1CH8G0H  | P1CH7G0H  | P1CH6G0H  | P1CH5G0H  | P1CH4G0H  | P1CH3G0H  | P1CH2G0H  | P1CH1G0H | P1CH0G0H  |
            | Entry #6 | P1CH15G1L   | P1CH14G1L   | P1CH13G1L   | P1CH12G1L  | P1CH11G1L | P1CH10G1L | P1CH9G1L  | P1CH8G1L  | P1CH7G1L  | P1CH6G1L  | P1CH5G1L  | P1CH4G1L  | P1CH3G1L  | P1CH2G1L  | P1CH1G1L | P1CH0G1L  |
            | Entry #7 | P1CH15G1H   | P1CH14G1H   | P1CH13G1H   | P1CH12G1H  | P1CH11G1H | P1CH10G1H | P1CH9G1H  | P1CH8G1H  | P1CH7G1H  | P1CH6G1H  | P1CH5G1H  | P1CH4G1H  | P1CH3G1H  | P1CH2G1H  | P1CH1G1H | P1CH0G1H  |  

        - **RAW_16B** Sequence 16-Bits Feature Map Format  

            > Assume the ONNX data is in shape 1x3x2x4 (BxCxHxW)   

            | Bits     | \[127:112\] | \[111:96\] | \[95:80\] | \[79:64\] | \[63:48\] | \[47:32\] | \[31:16\] | \[15:0\]  |
            |----------|-------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
            | Entry #0 | P7CH0       | P6CH0      | P5CH0     | P4CH0     | P3CH0     | P2CH0     | P1CH0     | P0CH0     |
            | Entry #1 | P15CH1      | P14CH1     | P13CH1    | P12CH1    | P11CH1    | P10CH1    | P9CH1     | P8CH1     |
            | Entry #2 | P23CH2      | P22CH2     | P21CH2    | P20CH2    | P19CH2    | P18CH2    | P17CH2    | P16CH2    |  
