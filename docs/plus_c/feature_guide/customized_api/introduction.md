# Introduction

In order to run customized models on Kneron AI device, there are four stages are involved:

- **Model Development**

    This will not be introduced in this document.

- **PLUS Development**

    The software interface for sending requests to firmware and receiving results from firmware.

- **SCPU Firmware Development**

    The entry of the firmware. Which models should be run on NCPU Firmware and in what sequence should these models run are determined in SCPU Firmware.

- **NCPU Firmware Development**

    Where models actually run. Besides the model inference, the preprocess and the postprocess can be chosen to run on NCPU Firmware.

The diagram below demonstrates the inference flow for every models runnig on Kneron AI device, and how the PLUS, SCPU, and NCPU interact with each other.

![](../../imgs/customized_api_develop_flow.png)

**Note**: Multiple calls of `kp_customized_inference_send()` without any call of `kp_customized_inference_receive()` may cause the system stuck.
