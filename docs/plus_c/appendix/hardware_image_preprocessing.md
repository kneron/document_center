## Hardware Image Preprocessing  

Most vision-related inference flows necessitate general image preprocessing to align with the model's input requirement. In Kneron devices, we've not only recognized this necessity but also integrated high-efficiency image preprocessing hardware. This hardware significantly speeds up the vision model inference flow, ensuring a smooth and efficient process.  

The significant features include:  

- Resize  
    - Specify whether to do or not to do the resize.  
- Cropping  
    - Setting the cropping areas. (At most five cropping areas)  
- Padding  
    - Specify whether to do or not to do the padding.
    - Setting the padding mechanism:  
        - Corner padding: content placed at left/top corner and padding right/bottom.  
        - Symmetric padding: content placed at the center and padding right/left/top/bottom.  
- Color space conversion  
    - Convert the platform-supported color space to an RGBA8888 or Grayscale image.  

The Kneron's unique features:  

- Normalization  
    - Hardware normalization is a crucial aspect of Kneron's hardware. It is intricately linked to the NPU model quantization factor, and we have carefully integrated the normalization formula and the quantization factor to design the hardware operations.  
        - Hardware operations:  
            - SUB128:  
                $$
                x - 128,\quad \text{where } x \in [-128, 127]
                $$  
            - DIV2:
                $$
                \left\lfloor \frac{x}{2} \right\rfloor,\quad \text{where } x \in [-128, 127]
                $$
            - SUB128_DIV2:  
                $$
                \left\lfloor \frac{x - 128}{2} \right\rfloor,\quad \text{where } x \in [-128, 127]
                $$
        - We support the following normalization formula template:  
            - $RGB/256 - 0.5,\quad \text{where } RGB \in [0, 255]$  
                - Quantization factor: Radix=8, Scale=1.0  
                - Hardware operation: SUB128  
            - $RGB/128 - 1.0,\quad \text{where } RGB \in [0, 255]$  
                - Quantization factor: Radix=7, Scale=1.0  
                - Hardware operation: SUB128  
            - $RGB/256,\quad \text{where } RGB \in [0, 255]$  
                - Quantization factor: Radix=7, Scale=1.0  
                - Hardware operation: DIV2  
- Limited NPU format conversion  
    - The Kneron NPU is a hardware accelerator designed specifically for neural networks, enabling efficient data processing that aligns with the hardware's preferred data layout and bit width. In Kneron devices, we offer limited conversions for NPU data layouts to optimize the speed of inference for vision models.  

### **Limitation**  

For the KL520/KL630/KL720, the hardware image preprocessing supports image models with either 3 or 4-channel input in a `4W4C8B` NPU format. It also supports a single-channel input in a `16W1C8B` format (The [C - Model Information](../introduction/run_examples.md#18-get-model-information-example)/[Python - Model Information](../../plus_python/introduction/run_examples.md#10-get-model-information-example) tool can quickly probe the NEF metadata for you). This allows users to leverage the image inference API for easy image pre-processing and NPU data conversion.  

In the case of KL730, we provide a more comprehensive list of supported NPU formats in the following table:  

| NPU Format                    | 16W1C8B | 4W4C8B | 1W16C8B | HW1C8B | HW4C8B_DROP_A | HW4C8B_KEEP_A |
|-------------------------------|---------|--------|---------|--------|---------------|---------------|
| Channel Number of Image Model |         |        |         |        |               |               |
| 1                             | V       | V      | V       | V      |               |               |
| 3                             |         | V      | V       |        | V             | V             |
| 4                             |         | V      | V       |        |               | V             |  

---

### **Note**

For any non-image or unsupported model input formats, please refer to following sections  
for guidance on converting the input data within the software.  

- For KneronPLUS  
    - [Generic Data Inference API - C Language](./../feature_guide/generic_inference.md#3-generic-data-inference-api)  
    - [Generic Data Inference API - Python Language](./../../plus_python/feature_guide/chapter/generic_inference.md#3-generic-data-inference-api)  

- For Firmware SDK  
    - KL520/KL630/KL720  
        - [Supported NPU Data Layout Format](./supported_npu_data_layout_format.md)  
    - KL730  
        - [Supported NPU Data Layout Format (KL730)](./supported_npu_data_layout_format_kl730.md)  
        - [Convert ONNX & NPU Data on the KL730 Platform](./convert_onnx_data_to_npu_data_on_kl730.md)  
        - [Create KL730 Single Model with Software NPU Format Convert Example](../feature_guide/customized_api/create_kl730_single_model_with_sw_npu_format_convert_example.md)  
