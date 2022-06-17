## Kneron PLUS 1.X and Kneron PLUS 2 APIs Mapping Table

---

## For Migrate to Kneron PLUS 2

### Inference API  

| Inference Data Type | Kneron PLUS 1.x (kp)                                               | Kneron PLUS 2 (kp)                                                    |
| ------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Image               | kp.inference.generic\_raw\_inference\_send()                       | kp.inference.generic\_image\_inference\_send()                        |
| Image               | kp.inference.generic\_raw\_inference\_receive()                    | kp.inference.generic\_image\_inference\_receive()                     |
| Raw Data            | kp.inference.generic\_raw\_inference\_bypass\_pre\_proc\_send()    | kp.inference.generic\_data\_inference\_send()                         |
| Raw Data            | kp.inference.generic\_raw\_inference\_bypass\_pre\_proc\_receive() | kp.inference.generic\_data\_inference\_receive()                      |  

### Inference Object  

| Inference Data Type | Kneron PLUS 1.x (kp)                   | Kneron PLUS 2 (kp)                        |
| ------------------- | -------------------------------------- | ----------------------------------------- |
| Image               | N/A                                    | kp.GenericInputNodeImage                  |
| Image               | kp.GenericRawImageHeader               | kp.GenericImageInferenceDescriptor        |
| Image               | kp.GenericRawResultHeader              | kp.GenericImageInferenceResultHeader      |
| Image               | kp.GenericRawResult                    | kp.GenericImageInferenceResult            |
| Raw Data            | N/A                                    | kp.GenericInputNodeData                   |
| Raw Data            | kp.GenericRawBypassPreProcImageHeader  | kp.GenericDataInferenceDescriptor         |
| Raw Data            | kp.GenericRawBypassPreProcResultHeader | kp.GenericDataInferenceResultHeader       |
| Raw Data            | kp.GenericRawBypassPreProcResult       | kp.GenericDataInferenceResult             |  

---

## For Compatible with Kneron PLUS 2

### Inference API Compat V1.x  

| Inference Data Type | Kneron PLUS 1.x (kp)                                               | Kneron PLUS 2 - Compat (kp.v1)                                        |
| ------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Image               | kp.inference.generic\_raw\_inference\_send()                       | kp.v1.inference.generic\_raw\_inference\_send()                       |
| Image               | kp.inference.generic\_raw\_inference\_receive()                    | kp.v1.inference.generic\_raw\_inference\_receive()                    |
| Raw Data            | kp.inference.generic\_raw\_inference\_bypass\_pre\_proc\_send()    | kp.v1.inference.generic\_raw\_inference\_bypass\_pre\_proc\_send()    |
| Raw Data            | kp.inference.generic\_raw\_inference\_bypass\_pre\_proc\_receive() | kp.v1.inference.generic\_raw\_inference\_bypass\_pre\_proc\_receive() |  

### Inference Object Compat V1.x  

| Inference Data Type | Kneron PLUS 1.x (kp)                   | Kneron PLUS 2 - Compat (kp.v1)            |
| ------------------- | -------------------------------------- | ----------------------------------------- |
| Image               | kp.GenericRawImageHeader               | kp.v1.GenericRawImageHeader               |
| Image               | kp.GenericRawResultHeader              | kp.v1.GenericRawResultHeader              |
| Image               | kp.GenericRawResult                    | kp.v1.GenericRawResult                    |
| Raw Data            | kp.GenericRawBypassPreProcImageHeader  | kp.v1.GenericRawBypassPreProcImageHeader  |
| Raw Data            | kp.GenericRawBypassPreProcResultHeader | kp.v1.GenericRawBypassPreProcResultHeader |
| Raw Data            | kp.GenericRawBypassPreProcResult       | kp.v1.GenericRawBypassPreProcResult       |  
