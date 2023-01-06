# SOC Peripheral Drivers

This chapter describes the peripherals prototypes for application programming reference.

```txt
├───firmware
│   ├───platform
│   │   ├───kl520
│   │	│	├───scpu
│   │   │	│	├───drv        <--------
│   │   │	│	├───rtos
│   │   │	│	├─── ...
```

Some simple examples are provided to show how to use peripherals such as, I2C, PWM, DMA, GPIO...

```txt
├───firmware
│   ├───build
│   │   ├───example_**         <--------
│   │   ├───lib
│   │   ├───solution_xxx
```

We hope that the peripheral examples can help user to test it on your board and hopefully base it to desgign your application.   
User can also refer to kdrv usage from the middleware(mdw) folder.

```txt
├───firmware
│   ├───mdw                    <--------
│   ├─── ...
```

## Peripheral Name Description

| Name                  | Description                                           |
| --------------------- | ----------------------------------------------------- |
| kdrv_clock            | Driver - Clock                                        |
| kdrv_gdma             | Driver - Generic  Direct Memory Access                |
| kdrv_gpio             | Driver - General Purpose Input/Output                 |
| kdrv_i2c              | Driver - Inter-integrated Circuit                     |
| kdrv_ipc              | Driver - Inter-Process Communication                  |
| kdrv_mpu              | Driver - Memory Protection Unit                       |
| kdrv_ncpu             | Driver - Neuro Control Process Unit                   |
| kdrv_pinmux           | Driver - Pin Multiplexing Configuration               |
| kdrv_power            | Driver - Power                                        |
| kdrv_pwm              | Driver - Pulse Width Modulation Timer                 |
| kdrv_sdc              | Driver - Sd Card Host Controller                      |
| kdrv_spif             | Driver - SPI Flash Controller for NOR Flash           |
| kdrv_system           | Driver - System                                       |
| kdrv_timer            | Driver - Timer/Counter                                |
| kdrv_uart             | Driver - Universal Asynchronous Receiver/Transmitter  |
| kdrv_usbd             | Driver - USB2 Device                                  |
| kdrv_usbd2            | Driver - USB2 Device                                  |
| kdrv_usbd2v           | Driver - USB2 Device                                  |
| kdrv_wdt              | Driver - Watchdog                                     |

---

