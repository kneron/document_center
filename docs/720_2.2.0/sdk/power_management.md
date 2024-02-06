# Power Management

The Power Management chapter provides functions to allow developers control the power states switching. Two functions to handle power management.

## 1. kdrv_power_set_wakeup_src
```
/**
 * @brief       set wake-up source
 *
 * @param[in]   wakeup_src_
 * @return      kdrv_status_t   see @ref kdrv_status_t
 */

kdrv_status_t kdrv_power_set_wakeup_src(uint32_t wakeup_src_);
```
There are four wake up source can be configured in project.h as below.
```
#define WKUP_SRC_RTC                        1
#define WKUP_SRC_EXT_BUT                    1
#define WKUP_SRC_USB_HIGH_SPEED             1
#define WKUP_SRC_USB_SUPER_SPEED            1
```


## 2. kdrv_power_sleep
```
/**
 * @brief       Set power mode into sleep
 *
 * @return      kdrv_status_t   see @ref kdrv_status_t
 */
kdrv_status_t kdrv_power_sleep(void);
```

Apply this function if system need to enter low power mode. During low power state, CPU clock stops and waiting for wake up event occur.
