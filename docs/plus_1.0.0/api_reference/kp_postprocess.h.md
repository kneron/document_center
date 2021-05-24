# Kneron PLUS post process APIs


Post process functions for application examples are provided
 
 




**Include Header File:**  kp_postprocess.h

- Defines
    - YOLO_GOOD_BOX_MAX
- Structs
    - [kp_yolo_result_t](#kp_yolo_result_t)
- Functions
    - [kp_post_process_yolo_v3](#kp_post_process_yolo_v3)
    - [kp_post_process_yolo_v5](#kp_post_process_yolo_v5)


---




## Defines
| Define | Value | Description |
|:---|:---|:---|
|YOLO_GOOD_BOX_MAX|100 | maximum number of bounding boxes for Yolo models |


---




## Structs
### kp_yolo_result_t
typedef struct **kp_yolo_result_t** {...}
> describe a yolo output result after post-processing

|Members| |
|:---|:--- |
|uint32_t class_count;| total class count |
|uint32_t box_count;| boxes of all classes |
|kp_bounding_box_t boxes[YOLO_GOOD_BOX_MAX];| box information |


---




## Functions
### kp_post_process_yolo_v3
> YOLO V3 post-processing function.

```c
int kp_post_process_yolo_v3(
	kp_inf_float_node_output_t *node_output[]
	int num_output_node
	int img_width
	int img_height
	float thresh_value
	kp_yolo_result_t *yoloResult
)
```
**Parameters:**

<pre>
<em>node_output</em>               floating-point output node arrays, it should come from kp_generic_inference_retrieve_node().
<em>num_output_node</em>           total number of output node.
<em>img_width</em>                 image width.
<em>img_height</em>                image height.
<em>thresh_value</em>              range from 0 ~ 1
<em>yoloResult</em>                this is the yolo result output, users need to prepare a buffer of 'kp_yolo_result_t' for this.
                          
</pre>
**Returns:**

return 0 means sucessful, otherwise failed.


---
### kp_post_process_yolo_v5
> YOLO V5 post-processing function.

```c
int kp_post_process_yolo_v5(
	kp_inf_float_node_output_t *node_output[]
	int num_output_node
	int img_width
	int img_height
	float thresh_value
	kp_yolo_result_t *yoloResult
)
```
**Parameters:**

<pre>
<em>node_output</em>               floating-point output node arrays, it should come from kp_generic_inference_retrieve_node().
<em>num_output_node</em>           total number of output node.
<em>img_width</em>                 image width.
<em>img_height</em>                image height.
<em>thresh_value</em>              range from 0 ~ 1
<em>yoloResult</em>                this is the yolo result output, users need to prepare a buffer of 'kp_yolo_result_t' for this.
                          
</pre>
**Returns:**

return 0 means sucessful, otherwise failed.


---
