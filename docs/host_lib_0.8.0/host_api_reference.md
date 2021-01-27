# Host API Reference

Host API is the API to setup communication channels between host (such as PC, Embedded Chips) and KL520. Users can use Host API to write programs that utilize low power and high performance KL520 to accelarate their deep learning model application. There are three types of APIs:

* Application specific API: These APIs are specific to certain applications (RGB Face Recognition, and Light Weight 3D Face Recognition).
* DME Mode API: These APIs are for setting up dynamic loaded model, and inference.
* ISI Mode API: These APIs are for setting up image streaming interface, and inference.
* System API: These APIs are used to monitor KL520 system, update firmware and models in flash. 

## KL520 Host API Overview

[The System API](host_api/system.md)

[The Application API](host_api/app_api.md)

[The DME API](host_api/dme_api.md)

[The ISI API](host_api/isi_api.md)

