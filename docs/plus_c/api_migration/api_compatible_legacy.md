## Compatible with Kneron PLUS 2  

The Kneron PLUS 2 provides `include/legacy/kp_inference_v1.h` and `include/legacy/kp_struct_v1.h` for temporary backward compatibility with V1.x APIs. The legacy code can be easily migrated to Kneron PLUS 2 by changing the **include header**.  

For example, the V1.x basic include header can be rewritten like the following code block. (For more examples, please reference sample code in kneron_plus/examples_legacy)  

- V1.x

    ```c
    ...

    #include "kp_core.h"
    #include "kp_inference.h"
    #include "helper_functions.h"

    ...
    ```

- V2

    ```c
    ...

    #include "kp_core.h"
    #include "legacy/kp_inference_v1.h"
    #include "helper_functions.h"

    ...
    ```
