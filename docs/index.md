# Kneron AI Documentations



Kneron AI is a full development stack for AI inference with Kneron AI Chip.
It is composed of tools, control libraries and example references.

![](./imgs/kneronAI_arch.png)

Kneron AI consists the following components:

1. **Kneron AI Development Kit - Kneron PLUS**
	It is Platform Libraries Unified Software to control Kneron Chip via USB interface
	*KL520 SDK v1.6.0 / KL720 SDK v1.4.1 / KL630 SDK v2.5.2 / KL730 SDK v1.0.0, or higher version is required*

2. **Kneron AI Development Kit - Firmware SDK**
	Open source for peripheral drivers, middleware and application code can be optimized to meet the needs for different applications
        - KL520 SDK
        - KL720 SDK
        - KL630 SDK
        - KL730 SDK

3. **Kneron AI Development Kit - Kneron Model Toolchain**
	A series of utilities for Kneron AI model creation
        - ONNX converter
        - Compiler
        - Quantizer
        - Evaluator
        - Simulator

4. **Kneron AI Model Zoo**
	A set of structure pre-optimized models used for demo and also open for re-training

5. **Kneron AI Chips**
        - KL520: Dongle, 96board, M.2 board
        - KL720: Dongle, 96board
        - KL630: 96board
        - KL730: 96board

---
## Compatibility Table

Versions                 | KL520 SDK version | KL720 SDK version | KL630 SDK version (NNM version) | KL730 SDK version
:------------------------|:------------------|:------------------|:------------------------------- | :----------------
Kneron PLUS v3.1.0       | 2.2.x             | 2.2.x             | 2.5.7 (1.3.x)                   | 1.2.0
Kneron PLUS v3.0.0       | 2.2.x             | 2.2.x             | 2.5.5 (1.2.x)                   | 1.0.0
Kneron PLUS v2.3.x-alpha | 2.2.x             | 2.2.x             | 2.5.5 (1.2.x)                   | 1.0.0-alpha
Kneron PLUS v2.2.x       | 2.2.x             | 2.2.x             | 2.5.5 (1.2.x)                   | Not supported
Kneron PLUS v2.1.x       | 2.1.x             | 2.1.x             | 2.5.2 (1.0.x)                   | Not supported
Kneron PLUS v2.0.x       | 2.0.x             | 2.0.x             | Not supported                   | Not supported
Kneron PLUS v1.3.x       | 1.7.x             | 1.5.x             | Not supported                   | Not supported
Kneron PLUS v1.2.x       | 1.6.x             | 1.4.x             | Not supported                   | Not supported
host_lib    v1.0.0       | 1.5.0.0           | 1.3.0             | Not supported                   | Not supported
host_lib    v0.9.x       | 1.4.0.x           | Not supported     | Not supported                   | Not supported

**Notes:**
	**Host API v1.0.0(host_lib)** *stays with [KL520 SDK v1.5.0.0](./520_1.5.0.0/getting_start.md) / [KL720 SDK v1.3.0](./720_1.3.0/getting_start_720.md) and deprecated from KL520 SDK v1.6.0/KL720 SDK v1.4.1*

---
## First Touch

**Kneron PLUS** provides low barrier AI inference experience to touch AI.

Please see [Kneron PLUS-C - Getting Started](./plus_c/getting_started.md) \(or [Python - Getting Started](./plus_python/getting_start.md)\) as a start

---
## References

 - [Kneron PLUS-C](./plus_c/introduction/introduction.md) / [Kneron PLUS-Python](./plus_python/introduction/index.md)
 - [Firmware KL520 SDK](./520_2.2.0/introduction.md)
 - [Firmware KL720 SDK](./720_2.2.0/introduction.md)
 - [Kneron Model Toolchain](./toolchain/manual_1_overview.md)
 - [Model Zoo - C-examples](./plus_c/modelzoo/index.md) / [Python-examples](./plus_python/modelzoo/index.md)
 - [Model Zoo - retraining](./model_training/classification.md)
