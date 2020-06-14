# DME API

DME APIs are for setting up dynamic loaded model, and inference.

### Start DME

`int kdp_start_dme(int dev_idx, uint32_t model_size, char* data, int dat_size,
                  uint32_t* ret_size, char* img_buf, int buf_len);`

 * request for starting dynamic model execution
 * dev_idx: connected device ID. A host can connect several devices
 * model_size: size of inference model
 * data: firmware setup data
 * dat_size: setup data size
 * ret_size: returned model size
 * img_buf, buf_len: the model file buffer and file size
 * return 0 on succeed, error code on failure
 
### Configure DME

`int kdp_dme_configure(int dev_idx, char* data, int dat_size, uint32_t* ret_model_id);`

 * request for configuring dme
 * dev_idx: connected device ID. A host can connect several devices
 * data: inference setup data
 * dat_size: the size of setup data
 * ret_model_id: the return value of model id for this configuration
 * return 0 on succeed, error code on failure

### Inference

`int kdp_dme_inference(int dev_idx, char* img_buf, int buf_len, uint32_t* inf_size,
                      bool* res_flag, char* inf_res, uint16_t mode, uint16_t model_id);`

 * calling KL520 to do inference with provided model
 * dev_idx: connected device ID. A host can connect several devices
 * img_buf, buf_len: the image buffer and file size
 * inf_size: the size of inference result
 * res_flag: indicate whether result is requested and available
 * inf_res: contains the returned inference result
 * model: running mode: normal or async mode 
 * model_id: the model id for this configuration
 * before calling this API, host must call kdp_start_dme and kdp_dme_configure to configure the dme model.
 * return 0 on succeed, error code on failure

### Retrieve Result

`int kdp_dme_retrieve_res(int dev_idx, uint32_t addr, int len, char* inf_res);`

 * request for retrieving dme result
 * dev_idx: connected device ID. A host can connect several devices
 * addr: the ddr address to retrieve
 * len: the size of data to retrieve
 * inf_res: contains the retrieving result
 * return 0 on succeed, error code on failure

### Get Status

`int kdp_dme_get_status(int dev_idx, uint16_t *ssid, uint16_t *status, uint32_t* inf_size, char* inf_res);`

 * request for getting dme inference status
 * dev_idx: connected device ID. A host can connect several devices
 * ssid: ssid to get inference status
 * status: inference status, 0 for not ready, 1 for ready
 * inf_size: inference data size
 * inf_res: inference result data
 * return 0 on succeed, error code on failure

