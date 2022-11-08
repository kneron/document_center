# Toolchain Docker History

## Manual History Version

* [v0.18.2](history/manual_v0.18.2.pdf)
* [v0.17.2](history/manual_v0.17.2.pdf)
* [v0.16.0](history/manual_v0.16.0.pdf)
* [v0.15.5](history/manual_v0.15.5.pdf)
* [v0.14.2](history/manual_v0.14.2.pdf)
* [v0.13.1](history/manual_v0.13.1.pdf)
* [520 v0.12.1](history/manual_520_v0.12.1.pdf)
* [720 v0.12.1](history/manual_720_v0.12.1.pdf)
* [520 v0.11.0](history/manual_520_v0.11.0.pdf)
* [720 v0.11.0](history/manual_720_v0.11.0.pdf)
* [520 v0.10.0](history/manual_520_v0.10.0.pdf)
* [720 v0.10.0](history/manual_720_v0.10.0.pdf)
* [520 v0.9.0](history/manual_520_v0.9.0.pdf)
* [720 v0.9.0](history/manual_720_v0.9.0.pdf)
* [v0.7.0](history/manual_v0.7.0.pdf)

## Toolchain Change log

* **[v0.19.0]**
    * Add 730 hardware support.
    * Minor bug fixes.
* **[v0.18.2]**
    * ktc: Add `mode`, `optimize`, `export_dynasty_dump` argument to analysis.
    * ktc: Set `skip_verify` in analysis as deprecated.
    * regression: Add optimize option for optimization level selection.
    * regression: Fix interface to asure platform is integer.
    * converter: Add 720 batch process with `--opt-720` flag.
    * converter: Add enable shared weight duplication flag `-d`. By default, shared weights are no longer duplicated.
    * converter: Remove `-s` flag since it is now the default behavious.
    * converter: Optimize debug output.
    * compiler: Fix RDMA not correctly executed.
    * E2E simulator: Change dynasty library fetching method.
    * Minor bug fixes.
* **[v0.18.1]**
    * docker: Update numpy from 1.18.5 to 1.21.
    * ktc: Add `km_cut` argument to analysis.
    * converter: Add operator checking before optimizaiton.
    * E2E simulator: Change dynasty library fetching method.
    * Minor bug fixes.
* **[v0.18.0]**
    * ONNX is updated to 1.7.0.
    * Introduce WebGUI.
    * Adjust 720 and 530 IP Evaluator default hardware specification.
    * Add more analysis options.
* **[v0.17.0]**
    * Optimize analysis API. Now we verify the model while analysing the fixed point performance.
    * E2E simulator no longer requires `radix` parameter.
* **[v0.16.0]**
    * Introduce 530 toolchain.
    * Optimizer supports pixel modification for wider input range adjustment.
    * FP analysis supports `mmse` mode.
    * Compiler supports `hardware_cut_opt` option.
    * Compiler supports combining nef files.
* **[v0.15.0]**
    * Document now is written for Python API. The original script document can be found in [Command Line Script Tools](http://doc.kneron.com/docs/toolchain/command_line/).
    * Compiler now support weight compress option.
* **[v0.14.0]**
    * ONNX is updated to 1.6.0
    * Pytorch is updated to 1.7.1
    * Introduce toolchain Python API.
* **[v0.13.0]**
    * 520 toolchain and 720 toolchain now is combined into one. But the scripts names and paths are the same as before. You don't need to learn it again.
    * E2E simulator has been updated to a new version. Usage changed. Please check its document.
* **[v0.12.0]** Introduce `convert_model.py` which simplify the conversion process.
* **[v0.11.0]** Batch compile now generate `.nef` files to simplify the output.
* **[v0.10.0]**
    * `input_params.json` and `batch_input_params.json` have been simplified a lot. Please check the document for details.
    * `simulator.sh`, `emulator.sh` and draw yolo image scripts are no longer available from `/workspace/scripts`. They have been moved to E2E simulator. Please check its document.
* **[v0.9.0]** In the example, the mount folder `/docker_mount` is separated from the interactive folder `/data1` to avoid
unexpected file changes. Users need to copy data between the mount folder and the interactive folder. Of course you can
still mount on `/data1`. But please be careful that the results folder under `/data1` may be overwritten.
