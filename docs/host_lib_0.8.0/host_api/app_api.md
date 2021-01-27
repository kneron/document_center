# Application API

APIs are specific to certain applications. User can add more 

## RGB Face Recognition

### Start SFID mode

`int kdp_start_sfid_mode(int dev_idx, uint32_t* img_size, float thresh,
                        uint16_t width, uint16_t height, uint32_t format);`

 * start the user sfid mode with specified threshold, image format
 * dev_idx: connected device ID. A host can connect several devices
 * img_size: the required image file size will be returned.
 * thresh:  the threshold used to match face recognition result.
            if 0, the default threshold is used.
 * img_width: the width of input image
 * img_height: the height of input image
 * format: the input image format
 * return 0 on succeed, error code on failure

### Face Recognition with User ID

`int kdp_verify_user_id_generic(int dev_idx, uint16_t* user_id, char* img_buf, int buf_len,
                               uint16_t* mask, char* res);`

 * extract the face feature from input image, and compare it with DB,
 * return the matched user ID, and face analysis related result.
 * dev_idx: connected device ID. A host can connect several devices
 * user_id: matched user ID in DB will be returned.
 * img_buf, buf_len: the image buffer and file size
 * mask: indicate the requested and responsed flags
 * bit 0 - FD result
 * bit 1 - LM data
 * bit 2 - FM feature map
 * bit 3 - liveness
 * res: contains all the related result
 * FD/LM/FR/LV result size: please refer to model_res.h
 * return 0 on succeed, error code on failure

### Face Recognition with Feature Map

`int kdp_extract_feature_generic(int dev_idx, char* img_buf, int buf_len, uint16_t* mask, char* res);`

 * extract face feature from inut image and save it in device,
 * returns face detection, face recoginition result.
 * dev_idx: connected device ID. A host can connect several devices
 * img_buf, buf_len: the image buffer and file size
 * mask: indicate the requested and responsed flags
   bit 0 - FD result
   bit 1 - LM data
   bit 2 - FM feature map
   bit 3 - liveness
 * res: contains all the related result
 * FD/LM/FR/LV result size: please refer to model_res.h
 * return 0 on succeed, error code on failure

### Get Result Size 

`uint32_t kdp_get_res_size(bool fd, bool lm, bool fr, bool liveness);`

 * @brief get result size
 * @return result size

### Get FDR Result Mask

`uint16_t kdp_get_res_mask(bool fd, bool lm, bool fr, bool liveness);`

 * @brief get FDR result mask
 * @return mask 

### Start Register Mode

`int kdp_start_reg_user_mode(int dev_idx, uint16_t usr_id, uint16_t img_idx);`

 * start the user register mode
 * dev_idx: connected device ID. A host can connect several devices
 * user_id: the user id that will be registered.
 * img_idx: the image idx that will be saved. (a user could have 5 images)
 * return 0 on succeed, -1 else

### Register New User

`int kdp_register_user(int dev_idx, uint32_t user_id);`

 * register the face features to device DB
 * dev_idx: connected device ID. A host can connect several devices
 * user_id: the user id that be registered. must be same as the kdp_start_reg_user_mode.
 * before calling this API, host must have called kdp_extract_feature
 * at least once successfully, otherwise, no features could be saved.
 * return 0 on succeed, error code on failure

### Delete User

`int kdp_remove_user(int dev_idx, uint32_t user_id);`

 * remove user from device DB
 * It needs to be called after start lw3d mode or start verify mode
 * dev_idx: connected device ID. A host can connect several devices
 * user_id: the user to be removed. 0 for all users
 * return 0 on succeed, error code on failure

### Compare Two Feature Map

`float kdp_fm_compare(float *user_fm_a, float *user_fm_b, size_t fm_size);`

 * @brief Calculate similarity of two feature points
 * @param user_fm_a buffer A of user feature map data
 * @param user_fm_b buffer B of user feature map data
 * @param fm_size   size of user feature map data
 * @return similarity score,smaller score are more similar
 *         errcode -1:parameter error
 * @note  user must ensure buffer A and B are the same size


## Light Weight 3D Face Recognition

### Start LW3D Mode

`int kdp_start_lw3d_mode(int dev_idx, uint32_t* rgb_size, uint32_t* nir_size,
                        float rgb_thresh, float nir_thresh, uint16_t rgb_width, 
                        uint16_t rgb_height, uint16_t nir_width, uint16_t nir_height, 
                        uint32_t rgb_fmt, uint32_t nir_fmt);`

 * start the light weight 3D mode  with specified threshold, img format
 * dev_idx: connected device ID. A host can connect several devices
 * rgb_size: the required rgb image file size will be returned.
 * nir_size: the required nir image file size will be returned.
 * rgb_thresh:  the threshold used to match rgb face recognition result.
            if 0, the default threshold is used.
 * nir_thresh:  the threshold used to match nir face recognition result.
            if 0, the default threshold is used.
 * rgb_width: the width of rgb image
 * rgb_height: the height of rgb image
 * nir_width: the width of nir image
 * nir_height: the height of nir image
 * rgb_fmt:   the format of rgb image
 * nir_fmt:  the format of nir image
 * return 0 on succeed, error code on failure

### LW3D Inference with User ID

`int kdp_verify_lw3D_image_generic(int dev_idx, uint16_t* user_id, char* img_buf,
	 int buf_len, char* img_buf_nir, int buf_len_nir, uint16_t* mask, char* res);`

 * extract the face feature from input rgb/nir image, and compare it with DB,
 * return the matched user ID, and face analysis related result.
 * dev_idx: connected device ID. A host can connect several devices
 * user_id: matched user ID in DB will be returned.
 * img_buf, buf_len: the rgb image buffer and file size
 * img_buf_nir, buf_len_nir: the nir image buffer and file size

 * mask: indicate the requested and responsed flags
   bit 0 - FD result
   bit 1 - FM feature map
   bit 2 - LM data
   bit 4 - NIR FD result
   bit 5 - NIR feature map
   bit 6 - NIR LM data
   bit 8 - Final liveness
 * res: contains all the related result
 * FD/LM/FR/LV result size: please refer to model_res.h
 * return 0 on succeed, error code on failure

### LW3D Inference with User Feature Map

`int kdp_extract_lw3D_feature_generic(int dev_idx, char* img_buf, int buf_len,
                                     char* img_buf_nir, int buf_len_nir, uint16_t* mask, char* res);`

 * extract the face feature from input rgb/nir image, and save it in device,
 * return the face analysis related result if required.
 * dev_idx: connected device ID. A host can connect several devices
 * img_buf, buf_len: the rgb image buffer and file size
 * img_buf_nir, buf_len_nir: the nir image buffer and file size

 * mask: indicate the requested and responsed flags
   bit 0 - FD result
   bit 1 - FM feature map
   bit 2 - LM data
   bit 4 - NIR FD result
   bit 5 - NIR feature map
   bit 6 - NIR LM data
   bit 8 - Final liveness
 * res: contains all the related result
 * FD/LM/FR/LV result size: please refer to model_res.h
 * return 0 on succeed, error code on failure

### LW3D Result Mask

`uint16_t kdp_get_lw3D_res_mask(bool fd, bool lm, bool fr, bool nir_fd, bool nir_lm, bool nir_fr, bool liveness);`

 * @brief get lw3D result mask
 * @return mask

### LW3D Result Size

`uint32_t kdp_get_lw3D_res_size(bool fd, bool lm, bool fr, bool nir_fd, bool nir_lm, bool nir_fr, bool liveness);`

 * @brief get lw3D result size
 * @return result size







