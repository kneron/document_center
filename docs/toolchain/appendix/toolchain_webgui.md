# Kneron Toolchain WebGUI

## 0. Overview

Since `kneron/toolchain:v0.18.0`, we provide a web GUI of the docker toolchain. In this document, you will learn
how to start the webgui service and how to use it to generate nef file for the Kneron hardware.

## 1. Installation

The installation is the same as in the [toolchain manual](http://doc.kneron.com/docs/#toolchain/manual/).
If you already have the kneron toolchain docker later than v0.18.0. You can just skip this section.

**Review the system requirements below before start installing and using the toolchain.**

### 1.1 System requirements

1. **Hardware**: Minimum quad-core CPU, 4GB RAM and 6GB free disk space.
2. **Operating system**: Window 10 x64 version 1903 or higher with build 18362 or higher. Ubuntu 16.04 x64 or higher.
Other OS which can run docker later than 19.03 may also work. But they are not tested. Please take the risk yourself.
3. **Docker**: Docker Desktop later than 19.03. Here is a [link](https://www.docker.com/products/docker-desktop) to
download Docker Desktop.

> **TIPS:**
>
> For Windows 10 users, we recommend using docker with wsl2, which is Windows subsystem Linux provided by Microsoft.
> Here is [how to install wsl2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and
> [how to install and run docker with wsl2](https://docs.docker.com/docker-for-windows/wsl/). Also, you might to want to
> adjust the resources docker use to ensure the tools' normal usage. Please check the FAQ at the end of this document on
> how to do that.

Please double-check whether the docker is successfully installed and callable from the console before going on to the
next section. If there is any problem about the docker installation, please search online or go to the docker community
for further support. The questions about the docker is beyond the reach of this document.

### 1.2 Pull the latest toolchain image

All the following steps are on the command line. Please make sure you have the access to it.

> TIPS:
>
> You may need `sudo` to run the docker commands, which depends on your system configuration.


You can use the following command to pull the latest toolchain docker.

```bash
docker pull kneron/toolchain:latest
```

Note that this document is compatible with toolchain v0.18.0. You can find the version of the toolchain in
`/workspace/version.txt` inside the docker.

## 2. Start the service

After pulling the desired toolchain, now we can start the service.

```bash
docker run -t -d -p 8180:8180 --name toolchain_webgui -w /workspace kneron/toolchain:latest /workspace/webgui/runWebGUI.sh
```

If you are under the linux environment, you may need to add `sudo` before your command. Here are the brief explanations
for the flags. For detailed explanations, please visit [docker documents](https://docs.docker.com/engine/reference/run/).

* `-t`: allocate a pseudo-tty.
* `-d`: start a container in detached mode, which means running at background as a service.
* `-p`: mapping port inside docker to the host. The web GUI uses the 8180 port. Thus, we map this port to the host.
* `--name`: specify a name for the docker container for ease of management.
* `-w`: specify the working directory.

After running the command above successfully, you can access the web GUI at <http://127.0.0.1:8180/>.

## 3. Web GUI introduction

Here is a brief introduction on how to use the web GUI.

<div align="center">
<img src="../imgs/webgui/webgui_0.png">
</div>

Notes:

1. Users' model IDs must be larger than 32767. Model IDs within 32767 are reserved for Kneron internal usage.
2. Version number is a 4-digit hex code.
3. The preprocess function signature should not be modified.
4. **Currently, the web GUI only support single input models.**

## 4. Run IP Evaluator only mode

If you only want to evaluate the model to a estimation of the model performance,
you can turn on the `Run Onnx Flow & IP Evaluator only` switch above the preprocess code seciton.
Then you can press run directly. The evaluation result would be shown on the right side `Console Output` section.

## 5. Stop, restart and remove the service

Below is the command to stop and to restart the docker service:

```bash
# Stop the service
docker stop toolchain_webgui
# Restart the service
docker start toolchain_webgui
```

When you want to update the service and restart the a branch new container, you may need the following command to delete
the current docker container.

```bash
# Delete the service container.
docker container rm toolchain_webgui
```
