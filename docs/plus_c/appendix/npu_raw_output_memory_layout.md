## NPU Raw Output Memory Layout

**Note**: For more information of *NPU data layout formate*, please reference [Supported NPU Data Layout Format](./../appendix/supported_npu_data_layout_format.md)

---

In **KL520**, the data values are in (height, channel, width_align) format, where width_align is the width aligned to the nearest 16 bytes (NPU data layout format: 16W1C8B).

In **KL630**, the data values are in (channel, height, width_align) format, where width_align is the width aligned to the nearest 16 bytes (NPU data layout format: 16W1C8B).

In **KL720**, the data values are in (channel, height, width_align) format, where width_align is the width aligned to the nearest 16 bytes (NPU data layout format: 16W1C8B).

- For example, assume the output node shape is 1x4x12x12 (BxCxHxW). The NPU raw output node data will be arranged as:
    ![](../imgs/customized_api_post_proc_mem_layout.png)

**Note**: The converting NPU data to ONNX data for **KL730**, please refer the source code of the API **kp_generic_inference_retrieve_fixed_node** in kneron_plus/src/kp_inference.c.
