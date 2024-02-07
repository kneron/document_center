## API Support List

The following mapping table shows the **Kneron PLUS** supported C/Python API:  

* **Core API**  

    | Function Name                                               | C   | Python |
    | ----------------------------------------------------------- | --- | ------ |
    | kp_scan_devices                                             | Yes | Yes    |
    | kp_connect_devices                                          | Yes | Yes    |
    | kp_connect_devices_without_check                            | Yes | Yes    |
    | kp_disconnect_devices                                       | Yes | Yes    |
    | kp_set_timeout                                              | Yes | Yes    |
    | kp_reset_device                                             | Yes | Yes    |
    | kp_load_firmware/kp_load_firmware_from_file                 | Yes | Yes    |
    | kp_load_model/kp_load_model_from_file                       | Yes | Yes    |
    | kp_load_encrypted_models/kp_load_encrypted_models_from_file | Yes | Yes    |
    | kp_enable_firmware_log                                      | Yes | Yes    |
    | kp_disable_firmware_log                                     | Yes | Yes    |
    | kp_get_system_info                                          | Yes | Yes    |
    | kp_get_model_info                                           | Yes | Yes    |
    | kp_load_model_from_flash                                    | Yes | Yes    |
    | kp_install_driver_for_windows                               | Yes | Yes    |
    | kp_store_ddr_manage_attr                                    | Yes | Yes    |
    | kp_error_string                                             | Yes |        |
    | kp_get_version                                              | Yes | Yes    |

* **Inference API**  

    | Function Name                                | C   | Python |
    |----------------------------------------------|-----|--------|
    | kp_inference_configure                       | Yes | Yes    |
    | kp_generic_image_inference_send              | Yes | Yes    |
    | kp_generic_image_inference_receive           | Yes | Yes    |
    | kp_generic_data_inference_send               | Yes | Yes    |
    | kp_generic_data_inference_receive            | Yes | Yes    |
    | kp_generic_inference_retrieve_raw_fixed_node | Yes |        |
    | kp_generic_inference_retrieve_fixed_node     | Yes | Yes    |
    | kp_generic_inference_retrieve_float_node     | Yes | Yes    |
    | kp_customized_inference_send                 | Yes |        |
    | kp_customized_inference_receive              | Yes |        |
    | kp_customized_command_send                   | Yes |        |
    | kp_dbg_set_enable_checkpoints                | Yes |        |
    | kp_dbg_receive_checkpoint_data               | Yes |        |
    | kp_profile_set_enable                        | Yes | Yes    |
    | kp_profile_get_statistics                    | Yes | Yes    |

* **Inference API V1.x (Legacy)**  

    | Function Name                                    | C   | Python |
    | ------------------------------------------------ | --- | ------ |
    | kp_generic_raw_inference_send                    | Yes | Yes    |
    | kp_generic_raw_inference_receive                 | Yes | Yes    |
    | kp_generic_raw_inference_bypass_pre_proc_send    | Yes | Yes    |
    | kp_generic_raw_inference_bypass_pre_proc_receive | Yes | Yes    |
