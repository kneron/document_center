<!-- kp documentation master file, created by
sphinx-quickstart on Tue May 18 15:28:42 2021.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# KneronPLUS python API documentation

## **KneronPLUS Core API**

### kp.core

The kp.core functions provide fundamental functionality like connection and firmware update.

### kp.inference

The kp.inference functions provide sophisticated functionally for different applications. Different set of inference APIs would need different models to make it work.

### kp value

Kneron PLUS objects.

### kp enum

Kneron PLUS enum values.

### kp exception

Kneron PLUS exception handler.

### kp.KPConstant

Kneron PLUS constant value.

### kp.v1 (Legacy Module)

Kneron PLUS V1.x legacy modules (inference, kp value).

### API Reference


* [kp.core](kp/core.md)


    * [`connect_devices()`](kp/core.md#kp.core.connect_devices)


    * [`connect_devices_without_check()`](kp/core.md#kp.core.connect_devices_without_check)


    * [`disable_firmware_log()`](kp/core.md#kp.core.disable_firmware_log)


    * [`disconnect_devices()`](kp/core.md#kp.core.disconnect_devices)


    * [`enable_firmware_log()`](kp/core.md#kp.core.enable_firmware_log)


    * [`get_model_info()`](kp/core.md#kp.core.get_model_info)


    * [`get_system_info()`](kp/core.md#kp.core.get_system_info)


    * [`get_version()`](kp/core.md#kp.core.get_version)


    * [`install_driver_for_windows()`](kp/core.md#kp.core.install_driver_for_windows)


    * [`load_encrypted_models()`](kp/core.md#kp.core.load_encrypted_models)


    * [`load_encrypted_models_from_file()`](kp/core.md#kp.core.load_encrypted_models_from_file)


    * [`load_firmware()`](kp/core.md#kp.core.load_firmware)


    * [`load_firmware_from_file()`](kp/core.md#kp.core.load_firmware_from_file)


    * [`load_model()`](kp/core.md#kp.core.load_model)


    * [`load_model_from_file()`](kp/core.md#kp.core.load_model_from_file)


    * [`load_model_from_flash()`](kp/core.md#kp.core.load_model_from_flash)


    * [`reset_device()`](kp/core.md#kp.core.reset_device)


    * [`scan_devices()`](kp/core.md#kp.core.scan_devices)


    * [`set_npu_timeout()`](kp/core.md#kp.core.set_npu_timeout)


    * [`set_timeout()`](kp/core.md#kp.core.set_timeout)


    * [`store_ddr_management_attributes()`](kp/core.md#kp.core.store_ddr_management_attributes)


* [kp.inference](kp/inference.md)


    * [`generic_data_inference_receive()`](kp/inference.md#kp.inference.generic_data_inference_receive)


    * [`generic_data_inference_send()`](kp/inference.md#kp.inference.generic_data_inference_send)


    * [`generic_image_inference_receive()`](kp/inference.md#kp.inference.generic_image_inference_receive)


    * [`generic_image_inference_send()`](kp/inference.md#kp.inference.generic_image_inference_send)


    * [`generic_inference_retrieve_fixed_node()`](kp/inference.md#kp.inference.generic_inference_retrieve_fixed_node)


    * [`generic_inference_retrieve_float_node()`](kp/inference.md#kp.inference.generic_inference_retrieve_float_node)


    * [`profile_get_statistics()`](kp/inference.md#kp.inference.profile_get_statistics)


    * [`profile_set_enable()`](kp/inference.md#kp.inference.profile_set_enable)


    * [`set_inference_configuration()`](kp/inference.md#kp.inference.set_inference_configuration)


* [kp value](kp/value.md)


    * [`DdrManageAttributes`](kp/value.md#kp.DdrManageAttributes)


    * [`DeviceDescriptor`](kp/value.md#kp.DeviceDescriptor)


    * [`DeviceDescriptorList`](kp/value.md#kp.DeviceDescriptorList)


    * [`DeviceGroup`](kp/value.md#kp.DeviceGroup)


    * [`FirmwareVersion`](kp/value.md#kp.FirmwareVersion)


    * [`GenericDataInferenceDescriptor`](kp/value.md#kp.GenericDataInferenceDescriptor)


    * [`GenericDataInferenceResult`](kp/value.md#kp.GenericDataInferenceResult)


    * [`GenericDataInferenceResultHeader`](kp/value.md#kp.GenericDataInferenceResultHeader)


    * [`GenericImageInferenceDescriptor`](kp/value.md#kp.GenericImageInferenceDescriptor)


    * [`GenericImageInferenceResult`](kp/value.md#kp.GenericImageInferenceResult)


    * [`GenericImageInferenceResultHeader`](kp/value.md#kp.GenericImageInferenceResultHeader)


    * [`GenericInputNodeData`](kp/value.md#kp.GenericInputNodeData)


    * [`GenericInputNodeImage`](kp/value.md#kp.GenericInputNodeImage)


    * [`GenericRawResultNDArray`](kp/value.md#kp.GenericRawResultNDArray)


    * [`HwPreProcInfo`](kp/value.md#kp.HwPreProcInfo)


    * [`InferenceConfiguration`](kp/value.md#kp.InferenceConfiguration)


    * [`InferenceCropBox`](kp/value.md#kp.InferenceCropBox)


    * [`InferenceFixedNodeOutput`](kp/value.md#kp.InferenceFixedNodeOutput)


    * [`InferenceFloatNodeOutput`](kp/value.md#kp.InferenceFloatNodeOutput)


    * [`ModelNefDescriptor`](kp/value.md#kp.ModelNefDescriptor)


    * [`ModelNefMetadata`](kp/value.md#kp.ModelNefMetadata)


    * [`NefSchemaVersion`](kp/value.md#kp.NefSchemaVersion)


    * [`NpuPerformanceMonitorStatistics`](kp/value.md#kp.NpuPerformanceMonitorStatistics)


    * [`PerformanceMonitorData`](kp/value.md#kp.PerformanceMonitorData)


    * [`ProfileData`](kp/value.md#kp.ProfileData)


    * [`ProfileModelStatistics`](kp/value.md#kp.ProfileModelStatistics)


    * [`QuantizationParameters`](kp/value.md#kp.QuantizationParameters)


    * [`QuantizationParametersV1`](kp/value.md#kp.QuantizationParametersV1)


    * [`QuantizedFixedPointDescriptor`](kp/value.md#kp.QuantizedFixedPointDescriptor)


    * [`Scale`](kp/value.md#kp.Scale)


    * [`SetupFileSchemaVersion`](kp/value.md#kp.SetupFileSchemaVersion)


    * [`SetupSchemaVersion`](kp/value.md#kp.SetupSchemaVersion)


    * [`SingleModelDescriptor`](kp/value.md#kp.SingleModelDescriptor)


    * [`SystemInfo`](kp/value.md#kp.SystemInfo)


    * [`TensorDescriptor`](kp/value.md#kp.TensorDescriptor)


    * [`TensorShapeInfo`](kp/value.md#kp.TensorShapeInfo)


    * [`TensorShapeInfoV1`](kp/value.md#kp.TensorShapeInfoV1)


    * [`TensorShapeInfoV2`](kp/value.md#kp.TensorShapeInfoV2)


* [kp enum](kp/enum.md)


    * [`ApiReturnCode`](kp/enum.md#kp.ApiReturnCode)


    * [`ChannelOrdering`](kp/enum.md#kp.ChannelOrdering)


    * [`DataType`](kp/enum.md#kp.DataType)


    * [`FixedPointDType`](kp/enum.md#kp.FixedPointDType)


    * [`ImageFormat`](kp/enum.md#kp.ImageFormat)


    * [`ModelTargetChip`](kp/enum.md#kp.ModelTargetChip)


    * [`ModelTensorDataLayout`](kp/enum.md#kp.ModelTensorDataLayout)


    * [`ModelTensorShapeInformationVersion`](kp/enum.md#kp.ModelTensorShapeInformationVersion)


    * [`NormalizeMode`](kp/enum.md#kp.NormalizeMode)


    * [`PaddingMode`](kp/enum.md#kp.PaddingMode)


    * [`ProductId`](kp/enum.md#kp.ProductId)


    * [`QuantizationParametersVersion`](kp/enum.md#kp.QuantizationParametersVersion)


    * [`ResetMode`](kp/enum.md#kp.ResetMode)


    * [`ResizeMode`](kp/enum.md#kp.ResizeMode)


    * [`UsbSpeed`](kp/enum.md#kp.UsbSpeed)


* [kp exception](kp/exception.md)


    * [`ApiKPException`](kp/exception.md#kp.ApiKPException)


* [kp.KPConstant](kp/const.md)


    * [`Const`](kp/const.md#kp.KPConstant.Const)


* [kp.v1.inference (Legacy Module)](kp/v1/inference.md)


    * [`generic_raw_inference_bypass_pre_proc_receive()`](kp/v1/inference.md#kp.v1.inference.generic_raw_inference_bypass_pre_proc_receive)


    * [`generic_raw_inference_bypass_pre_proc_send()`](kp/v1/inference.md#kp.v1.inference.generic_raw_inference_bypass_pre_proc_send)


    * [`generic_raw_inference_receive()`](kp/v1/inference.md#kp.v1.inference.generic_raw_inference_receive)


    * [`generic_raw_inference_send()`](kp/v1/inference.md#kp.v1.inference.generic_raw_inference_send)


* [kp.v1 value (Legacy Module)](kp/v1/value.md)


    * [`GenericRawBypassPreProcImageHeader`](kp/v1/value.md#kp.v1.GenericRawBypassPreProcImageHeader)


    * [`GenericRawBypassPreProcResult`](kp/v1/value.md#kp.v1.GenericRawBypassPreProcResult)


    * [`GenericRawBypassPreProcResultHeader`](kp/v1/value.md#kp.v1.GenericRawBypassPreProcResultHeader)


    * [`GenericRawImageHeader`](kp/v1/value.md#kp.v1.GenericRawImageHeader)


    * [`GenericRawResult`](kp/v1/value.md#kp.v1.GenericRawResult)


    * [`GenericRawResultHeader`](kp/v1/value.md#kp.v1.GenericRawResultHeader)

