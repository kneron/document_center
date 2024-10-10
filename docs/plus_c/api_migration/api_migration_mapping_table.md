## Kneron PLUS 1.X and Kneron PLUS 2 / 3 APIs Mapping Table

### Inference API

| Inference Data Type | Kneron PLUS 1.x (kp\_inference.h)                         | Kneron PLUS 2 / 3 (kp\_inference.h)                           |
| ------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| Image               | kp\_generic\_raw\_inference\_send()                       | kp\_generic\_image\_inference\_send()                     |
| Image               | kp\_generic\_raw\_inference\_receive()                    | kp\_generic\_image\_inference\_receive()                  |
| Raw Data            | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_send()    | kp\_generic\_data\_inference\_send()                      |
| Raw Data            | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_receive() | kp\_generic\_data\_inference\_receive()                   |

### Inference API Compat V1.x

| Inference Data Type | Kneron PLUS 1.x (kp\_inference.h)                         | Kneron PLUS 2 / 3 - Compat (legacy/kp\_inference\_v1.h)       |
| ------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| Image               | kp\_generic\_raw\_inference\_send()                       | kp\_generic\_raw\_inference\_send()                       |
| Image               | kp\_generic\_raw\_inference\_receive()                    | kp\_generic\_raw\_inference\_receive()                    |
| Raw Data            | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_send()    | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_send()    |
| Raw Data            | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_receive() | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_receive() |

### Struct

| Inference Data Type | Kneron PLUS 1.x (kp\_struct.h)                         | Kneron PLUS 2 / 3 (kp\_struct.h)                           |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| Image               | N/A                                                    | kp\_generic\_input\_node\_image\_t                     |
| Image               | kp\_generic\_raw\_image\_header\_t                     | kp\_generic\_image\_inference\_desc\_t                 |
| Image               | kp\_generic\_raw\_result\_header\_t                    | kp\_generic\_image\_inference\_result\_header\_t       |
| Raw Data            | N/A                                                    | kp\_generic\_input\_node\_data\_t                      |
| Raw Data            | kp\_generic\_raw\_bypass\_pre\_proc\_image\_header\_t  | kp\_generic\_data\_inference\_desc\_t                  |
| Raw Data            | kp\_generic\_raw\_bypass\_pre\_proc\_result\_header\_t | kp\_generic\_data\_inference\_result\_header\_t        |

### Struct Compat V1.x

| Inference Data Type | Kneron PLUS 1.x (kp\_struct.h)                         | Kneron PLUS 2 / 3 - Compat (legacy/kp\_struct\_v1.h)       |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| Image               | kp\_generic\_raw\_image\_header\_t                     | kp\_generic\_raw\_image\_header\_t                     |
| Image               | kp\_generic\_raw\_result\_header\_t                    | kp\_generic\_raw\_result\_header\_t                    |
| Raw Data            | kp\_generic\_raw\_bypass\_pre\_proc\_image\_header\_t  | kp\_generic\_raw\_bypass\_pre\_proc\_image\_header\_t  |
| Raw Data            | kp\_generic\_raw\_bypass\_pre\_proc\_result\_header\_t | kp\_generic\_raw\_bypass\_pre\_proc\_result\_header\_t |
