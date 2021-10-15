# File Structure
The whole SDK package is composed of device firmware, the folder design is described below

```txt
.
├── common                              # common interface between SCPU/NCPU
├── example_projects
│   ├── kdp2_companion_user_ex          # Keil project for Kneron PLUS user example
│   ├── tiny_yolo_v3_host               # Keil project for host mode(Standalone) firmware example
│   └── tiny_yolo_v3_host_usbout        # Keil project for host mode with outputing result vis usb
├── ncpu
│   ├── device                          # device configurations
│   ├── drivers                         # drivers used by ncpu
│   ├── lib                             # folder for libraries
│   └── project
│       └── tiny_yolo_v3                # ncpu project
├── scpu
│   ├── board                           # for device board configurations
│   ├── config                          # for device board configurations
│   ├── device                          # device memory address configurations
│   ├── drivers                         # drivers
│   ├── framework                       # framework layer code
│   ├── kdev                            # device driver code
│   ├── kl520                           # kl520 drivers
│   ├── kmdw                            # middleware
│   ├── lib                             # folder for libraries
│   └── project
│       └── tiny_yolo_v3                 
│           ├── host                    # Keil project for host mode firmware example
│           └── host_usbout             # Keil project for host mode with outputing result vis usb
├── ncpu_kdp2
│   ├── lib_app                         # folder for kdp2-ncpu-app.lib
│   ├── lib_sdk                         # folder for kdp2-ncpu-sdk.lib
│   └── project
│       └── ncpu_companion_user_ex      # Keil project for Kneron PLUS user example
├── scpu_kdp2
│   ├── app                             # application layer code for Kneron PLUS firmware example
│   ├── lib_sdk                         # kdp2_scpu_sdk.lib folder
│   └── project
│       └── scpu_companion_user_ex      # Keil project for Kneron PLUS example
├── models
│   └── tiny_yolo_v3                    # model file for demo
├── sdkexamples                         # driver examples
└── utils                               # firmware/model utilities
```

