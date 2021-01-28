# Post processing API


A few post-processing functions are implemented here for specifc models.
 




**Include Header File:**  kdp2_postprocess.h

- Functions
    - [kdp2_post_process_yolo_v3](#kdp2_post_process_yolo_v3)


---




## Functions
### kdp2_post_process_yolo_v3
> YOLO V3 post-processing function.

```c
int kdp2_post_process_yolo_v3(
	kdp2_node_output_t *node_output[]
	int num_output_node
	int img_width
	int img_height
	kdp2_yolo_result_t *yoloResult
)
```
**Parameters:**

<pre>
<em>node_output</em>               floating-point output node arrays, it should come from kdp2_raw_inference_retrieve_node().
<em>num_output_node</em>           total number of output node.
<em>img_width</em>                 image width.
<em>img_height</em>                image height.
<em>yoloResult</em>                this is the yolo result output, users need to prepare a buffer of 'kdp2_yolo_result_t' for this.
</pre>
**Returns:**

return 0 means sucessful, otherwise failed.


---
