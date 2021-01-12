# ISI API

ISI APIs are for setting up image streaming interface, and inference. 

### Start ISI Mode 

`int kdp_start_isi_mode(int dev_idx, uint32_t app_id, uint32_t return_size, uint16_t width, uint16_t height, uint32_t format, uint32_t* rsp_code, uint32_t* buf_size);`

 * start the user isi mode with specified app id and return data size
 * dev_idx: connected device ID. A host can connect several devices
 * buf_size: the depth of the image buffer will be returned.
 * img_width: the width of input image
 * img_height: the height of input image
 * format: the input image format
 * return 0 on succeed, error code on failure

### Start ISI Mode with ISI Configuration

`int kdp_start_isi_mode_ext(int dev_idx, char* isi_cfg, int cfg_size, uint32_t* rsp_code, uint32_t* buf_size);`

 * start the user isi mode with isi configuration and return buffer size
 * dev_idx: connected device ID. A host can connect several devices
 * isi_cfg: isi configuration data
 * cfg_size: isi configuration data size
 * rsp_code: response code from device
 * buf_size: the depth of the image buffer will be returned.
 * return 0 on succeed, error code on failure

### ISI Inference

`int kdp_isi_inference(int dev_idx, char* img_buf, int buf_len, uint32_t img_id,
                       uint32_t* rsp_code, uint32_t* img_buf_available);`

 * start an inference with an image
 * dev_idx: connected device ID. A host can connect several devices
 * img_buf, buf_len: the image buffer and file size
 * img_id: the sequence id of the image
 * img_buf_available: the number of image buffer still available for input
 * before calling this API, host must call kdp_start_isi to configure the isi application.
 * return 0 on succeed, error code on failure

### ISI Retrieve Result

`int kdp_isi_retrieve_res(int dev_idx, uint32_t img_id, uint32_t* rsp_code,
                          uint32_t* r_size, char* r_data);`

 * request for getting an inference results
 * dev_idx: connected device ID. A host can connect several devices
 * img_id: sequence id to get inference results of an image with the specified id
 * inf_size: inference data size
 * inf_res: inference result data
 * return 0 on succeed, error code on failure








