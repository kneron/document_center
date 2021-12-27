# Python API Support List

The following mapping table shows the **KP** supported Python API:  

* **Core API**  

    | Function Name                                                       | C         | Python    |
    | ------------------------------------------------------------------- | --------- | --------- |
    | kp\_scan\_devices                                                   | Yes       | Yes       |
    | kp\_connect\_devices                                                | Yes       | Yes       |
    | kp\_disconnect\_devices                                             | Yes       | Yes       |
    | kp\_set\_timeout                                                    | Yes       | Yes       |
    | kp\_reset\_device                                                   | Yes       | Yes       |
    | kp\_load\_firmware/kp\_load\_firmware\_from\_file                   | Yes       | Yes       |
    | kp\_load\_model/kp\_load\_model\_from\_file                         | Yes       | Yes       |
    | kp\_load\_encrypted\_models/kp\_load\_encrypted\_models\_from\_file | Yes (New) | Yes (New) |
    | kp\_enable\_firmware\_log                                           | Yes       | Yes       |
    | kp\_disable\_firmware\_log                                          | Yes       | Yes       |
    | kp\_get\_system\_info                                               | Yes       | Yes       |
    | kp\_get\_model\_info                                                | Yes       | Yes       |
    | kp\_load\_model\_from\_flash                                        | Yes       | Yes       |
    | kp\_install\_driver\_for\_windows                                   | Yes (New) | Yes (New) |
    | kp\_error\_string                                                   | Yes       |           |
    | kp\_get\_version                                                    | Yes       | Yes       |

* **Inference API**  

    | Function Name                                               | C         | Python |
    | ----------------------------------------------------------- | --------- | ------ |
    | kp\_inference\_configure                                    | Yes       | Yes    |
    | kp\_generic\_raw\_inference\_send                           | Yes       | Yes    |
    | kp\_generic\_raw\_inference\_receive                        | Yes       | Yes    |
    | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_send        | Yes       | Yes    |
    | kp\_generic\_raw\_inference\_bypass\_pre\_proc\_receive     | Yes       | Yes    |
    | kp\_generic\_inference\_retrieve\_raw\_fixed\_node          | Yes       |        |
    | kp\_generic\_inference\_retrieve\_fixed\_node               | Yes       | Yes    |
    | kp\_generic\_inference\_retrieve\_float\_node               | Yes       | Yes    |
    | kp\_customized\_inference\_send                             | Yes       |        |
    | kp\_customized\_inference\_receive                          | Yes       |        |
    | kp\_customized\_command\_send                               | Yes       |        |
    | kp\_dbg\_set\_enable\_checkpoints                           | Yes (New) |        |
    | kp\_dbg\_receive\_checkpoint\_data                          | Yes (New) |        |
    | kp\_profile\_set\_enable                                    | Yes (New) |        |
    | kp\_profile\_get\_statistics                                | Yes (New) |        |
    | kp\_app\_{app\_name}\_inference\_send                       | Remove    | Remove |
    | kp\_app\_{app\_name}\_inference\_receive                    | Remove    | Remove |
    | kp\_app\_yolo\_get\_v5\_post\_proc\_parameters (Only KL720) | Remove    | Remove |
    | kp\_app\_yolo\_set\_v5\_post\_proc\_parameters (Only KL720) | Remove    | Remove |
