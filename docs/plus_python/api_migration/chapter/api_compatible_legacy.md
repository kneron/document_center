## Compatible with Kneron PLUS 3  

The Kneron PLUS 3 provides `kp.v1` for temporary backward compatibility with V1.x APIs. The legacy code can be easily migrated to Kneron PLUS 3 by **kp.v1** module.  

For example, the V1.x basic include header can be rewritten like the following code block. (For more examples, please reference sample code in kneron_plus/python/example_legacy)  

- V1.x

    ```c
    ...

    """
    prepare app generic inference config
    """
    generic_raw_image_header = kp.GenericRawImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
        padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
        normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
        inference_number=0
    )

    """
    starting inference work
    """
    kp.inference.generic_raw_inference_send(device_group=device_group,
                                            generic_raw_image_header=generic_raw_image_header,
                                            image=img_bgr565,
                                            image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)

    generic_raw_result = kp.inference.generic_raw_inference_receive(device_group=device_group,
                                                                    generic_raw_image_header=generic_raw_image_header,
                                                                    model_nef_descriptor=model_nef_descriptor)

    ...
    ```

- V2 and V3

    ```c
    ...

    """
    prepare generic raw inference image descriptor
    """
    generic_raw_image_header = kp.v1.GenericRawImageHeader(
        model_id=model_nef_descriptor.models[0].id,
        resize_mode=kp.ResizeMode.KP_RESIZE_ENABLE,
        padding_mode=kp.PaddingMode.KP_PADDING_CORNER,
        normalize_mode=kp.NormalizeMode.KP_NORMALIZE_KNERON,
        inference_number=0
    )

    """
    starting inference work
    """
    kp.v1.inference.generic_raw_inference_send(device_group=device_group,
                                               generic_raw_image_header=generic_raw_image_header,
                                               image=img_bgr565,
                                               image_format=kp.ImageFormat.KP_IMAGE_FORMAT_RGB565)

    generic_raw_result = kp.v1.inference.generic_raw_inference_receive(device_group=device_group,
                                                                       generic_raw_image_header=generic_raw_image_header,
                                                                       model_nef_descriptor=model_nef_descriptor)

    ...
    ```
