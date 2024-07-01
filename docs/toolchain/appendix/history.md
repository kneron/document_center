# Toolchain Docker History

## Manual History Version

* [v0.20.2](https://github.com/kneron/document_center/releases/tag/v0.20.2)
* [v0.20.1](https://github.com/kneron/document_center/releases/tag/v0.20.1)
* [v0.20.0](https://github.com/kneron/document_center/releases/tag/v0.20.0)
* [v0.19.0](../history/manual_v0.19.0.pdf)
* [v0.18.2](../history/manual_v0.18.2.pdf)
* [v0.17.2](../history/manual_v0.17.2.pdf)
* [v0.16.0](../history/manual_v0.16.0.pdf)
* [v0.15.5](../history/manual_v0.15.5.pdf)
* [v0.14.2](../history/manual_v0.14.2.pdf)
* [v0.13.1](../history/manual_v0.13.1.pdf)
* [520 v0.12.1](../history/manual_520_v0.12.1.pdf)
* [720 v0.12.1](../history/manual_720_v0.12.1.pdf)
* [520 v0.11.0](../history/manual_520_v0.11.0.pdf)
* [720 v0.11.0](../history/manual_720_v0.11.0.pdf)
* [520 v0.10.0](../history/manual_520_v0.10.0.pdf)
* [720 v0.10.0](../history/manual_720_v0.10.0.pdf)
* [520 v0.9.0](../history/manual_520_v0.9.0.pdf)
* [720 v0.9.0](../history/manual_720_v0.9.0.pdf)
* [v0.7.0](../history/manual_v0.7.0.pdf)

## Toolchain Change log

* **[v0.25.0]**
    * **IP evaluator add arguments `weight_bandwidth` and `dma_bandwidth`.**
    * 730 toolchain full upgrade.
    * Optimize batch compiler efficiency.
    * Optimize batch compiler memory management algorithm.
    * Support fmap over 4D.
    * Support more operators (Abs, Log, Pow, Sign).
    * Support mix accuracy mode.
    * Update environment packages.
    * Fix bugs.
* **[v0.24.0]**
    * **`ktc.ModelConfig.analysis` rename 'fm_cut' to 'compiler_tiling'.**
    * `ktc.ModelConfig.analysis` change `datapath_bitwidth_mode` and `weight_bitwidth_mode` to support mix-bitwidth mode "mix light" and "mix balance". (exclude 520).
    * Support ONNX opset 18.
    * Optimize customized node support.
    * Support multiple output operators.
    * Support per-channel quantization
    * WebGUI Auto-detect model input node information, make convert onnx or tflite to nef more easier.
    * Docker update the parallel package version.
    * Fix known bugs and improve performance.
* **[v0.23.1]**
    * Compiler may raise error on unsupported CPU nodes.
    * Bug fixes for compiler, dynasty and ktc.
* **[v0.23.0]**
    * **`ktc.kneron_inference` now requires `input_names` which is optional previously.**
    * **`ktc.ModelConfig.evaluate()` now only generate html report instead of the previous txt report.**
    * **`bie` format update for better supporting new models. Due to this update, the previous generated `bie` files are no longer supported.**
    * **Batch compiler now support 730 hardware.**
    * Provide more information in IP evaluator report.
    * Optimize the quantization snr calculation.
    * Optimize the compiler for better on-chip performance.
    * Supporting latest models with loop node inside.
    * Bug fixes and other improvements.
* **[v0.22.0]**
    * `ktc.ModelConfig.evaluate`
      * **Change function parameter `output_folder` to `output_dir`.**
      * **Change default output location to `/data1/kneronflow`.**
    * `ktc.ModelConfig.analysis`
      * **Change function parameter `output_bie` to `output_dir`, which should be a folder path instead of the file path before. Defaults to `/data1/kneronflow`.**
      * **Remove deprecated parameters `bitwidth_mode`, `outlier` and `skip_verify`.**
      * Add parameters `model_in_bitwidth_mode`, `model_out_bitwidth_mode`, `datapath_bitwidth_mode` and `weight_bitwidth_mode`.
    * `ktc.ModelConfig`
      * Add `radix_json_path` to `ktc.ModelConfig.__init__` which provides `ktc.compile` ability to compile with onnx and a special json file. Defaults to `None`.
      * Add `debug` to `ktc.ModelConfig.__init__` to avoid removing debug output files. Defaults to `False`.
    * `ktc.compile`, `ktc.encrpyt_compile`
      * **Change default output location to `/data1/kneronflow`.**
      * Add `debug` parameter to avoid removing debug output files. Defaults to `False`.
    * Provided a function `ktc.convert_channel_last_to_first` to help converting channel last inputs to channel first(image only).
    * Remove unessential output files. Some functions add `debug` parameters to avoid removing debug output files. `ktc.kneron_inference` can use `dump` parameter avoid removing debug output files.
    * Bug fixes and performance improvements.
* **[v0.21.0]**
    * **Change input format from channel last to the same input shape of ONNX.**
    * **Change compiler generated `ioinfo.csv` into `ioinfo.json` for platforms other than 520.**
    * **Remove deprecated command line scripts, e.g. fpAnalyserCompilerIpevaluator_520.py, fpAnalyserBatchCompile_520.py.**
    * Add html report for `analysis` API.
    * Add helper utilities under compiler folder.
    * Add `parallel` and `w3m` into docker environment.
    * Bug fixes.
    * Documentation updates.
* **[v0.20.2]**
    * Fix combining nef error.
* **[v0.20.1]**
    * Update toolchain example to MobileNet v2.
    * Fix knerex bias adjustment.
    * Fix knerex shared weight with same name support.
    * Fix other bugs.
* **[v0.20.0]**
    * Support text procssing models.
    * Set flatbuffer as the default 720 compiling mode.
    * Refactor compiler and analyser inner structure.
    * **Due to the structure change, batch compiler do not backwark support previous bie files.**
    * Refactor toolchain manual.
    * Bug fixes.
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
