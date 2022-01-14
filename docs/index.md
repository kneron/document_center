# Kneron AI Documentations



Kneron AI is a full development stack for AI inference with Kneron AI Chip.
It is composed of tools, control libraries and example references.

![](./imgs/kneronAI_arch.png)

Kneron AI consists the following components:  

1. **Kneron AI Development Kit - Kneron PLUS**  
	It is Platform Libraries Unified Software to control Kneron Chip via USB interface  
	*KL520 SDK v1.6.0 / KL720 SDK v1.4.1, or higher verion is required*

2. **Kneron AI Development Kit - Firmware SDK**  
	Open source for peripheral drivers, middleware and application code can be optimized to meet the needs for different applications  
        - KL520 SDK  
        - KL720 SDK  

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

---
## Compatibility Table

Versions           | KL520 SDK version | KL720 SDK version 
:------------------|:------------------|:--------------
Kneron PLUS v1.3.x | 1.7.x             | 1.5.x         
Kneron PLUS v1.2.x | 1.6.x             | 1.4.x         
host_lib    v1.0.0 | 1.5.0.0           | 1.3.0         
host_lib    v0.9.x | 1.4.0.x           | Not supported

**Notes:**  
	**Host API v1.0.0(host_lib)** *stays with [KL520 SDK v1.5.0.0](./520_1.5.0.0/getting_start.md) / [KL720 SDK v1.3.0](./720_1.3.0/getting_start_720.md) and deprecated from KL520 SDK v1.6.0/KL720 SDK v1.4.1*

---
## First Touch 

**Kneron PLUS** provides low barrier AI inference experience to touch AI.

Please see [Kneron PLUS-C - Getting Started](./plus_c/getting_started.md) \(or [Python - Getting Started](./plus_python/getting_start.md)\) as a start

---
## References

 - [Kneron PLUS-C](./plus_c/introduction/introduction.md) / [Kneron PLUS-Python](./plus_python/introduction/index.md) 
 - [Firmware KL520 SDK](./520_1.7.0/introduction.md)
 - [Firmware KL720 SDK](./720_1.5.0/introduction.md)
 - [Kneron Model Toolchain](./toolchain/manual.md)
 - [Model Zoo - C-examples](./plus_c/modelzoo/index.md) / [Python-examples](./plus_python/modelzoo/index.md)
 - [Model Zoo - retraining](./model_training/classification.md)


