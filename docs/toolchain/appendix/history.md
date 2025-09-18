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

* **[v0.31.0]**
    * **Introduce `quan_config` for `ModelConfig.analysis` for more detailed quantization configuration.**
    * **Add `ktc.opt_and_eval` command for quick onnx optimization and evaluation.**
    * **Remove deprecated `compilerIpevaluator_730.sh` and add warning messages to other depecated scritps.**
    * Add `compiler_tiling` option for IP evaluator.
    * Add `--clear-shapes` and `--replace-avgpool-with-conv` flags to kneronnxopt.
    * Add `--seperate` flag to kneronnxopt.onnx_vs_onnx for detailed output comparison.
    * Update knerex shared weight combination logic.
    * Update knerex and dynasty to support empty Constant nodes.
    * Update compiler for better message logging.
    * Update dynasty and compiler for `softmax` support.
    * Update regression for longer timeout setting.
    * Improve `model_fx_report.html` readability.
    * Speed up compilerfor large model.
    * Fix the ktc error message for not supported special characters in model path.
    * Fix the ktc bug that logging module not imported.
    * Fix the kneronnxopt bug that flip nodes are eliminated incorrectly.
    * Fix the kneronnxopt bug that replacing Add/Sub/Mul/Div with BatchNormalization node incorrectly.
    * Fix the nef utility bug that 520 nef combination generates invalid nef files.
    * Other bug fixes and performance improvements.
* **[v0.30.0]**
    * **Introduce `input_fmt` for `ModelConfig` to specify the input format of the model.**
    * **`bie` files may not be compatible with previous versions.**
    * Fix kneronnxopt to duplicate shared weights for not supported cases.
    * Update knerex to support alpha&beta hardsigmoid.
    * Update webgui to support conda environment selection.
    * Bug fixes and performance improvements.
* **[v0.29.0]**
    * **Introduce `mixbw` for fixed-point analysis, an automated quantization mode that optimizes 8/16-bit configurations for Conv nodes, balancing accuracy (SNR) and speed   (FPS).**
    * Add onnx_vs_onnx command line entrance for kneronnxopt to compare two onnx models.
    * Optimize log printing for ktc.
    * Optimize compiler runtime based on partial graph comparison.
    * Fix the bug that knerex could not handle last nodes properly in some cases.
    * Fix the bug that knerex could not handle Add constant node input properly.
    * Fix other known bugs.
* **[v0.28.2]**
    * Fix the batch compiler bug that nef files do not contain version information.
    * Optimize kneronnxopt for processing large models.
    * Fix other bugs.
* **[v0.28.1]**
    * Change default miniconda channel due to the license issue.
* **[v0.28.0]**
    * **Change conda environment due to license issue.**
    * **Remove caffe support.**
    * Add `--opt-matmul` flag to kneronnxopt for kneron hardware matmul optimization.
    * Add `--overwrite-input-shapes` and `--skip-fuse-qkv` flags to kneronnxopt large model processing.
    * Support GRU, LSTM, and RNN operators defusion in kneronnxopt.
    * Fix bugs.
* **[v0.27.0]**
    * Adjust batch compiler internal behavior to improve robustness.
    * Optimize compiler to improve feature map cut search speed.
    * Optimize data converter to improve speed.
    * Fix bugs.
* **[v0.26.0]**
    * Optimize compiler for 730 graph cutting.
    * Supports the flash attention model.
    * Add producer name in kneronnxopt.
    * Fix bugs.
* **[v0.25.1]**
    * ktc supports non-str platform conversion.
    * Fix kneronnxopt argument name.
    * Update conda environment
        * base:
            - numpy-1.21.0
            - pandas-1.2.0
        * onnx1.13:
            - numpy-1.26.4
            - pandas-2.2.2
    * Fix bugs.
* **[v0.25.0]**
    * **IP evaluator add arguments `weight_bandwidth` and `dma_bandwidth`.**
    * 730 toolchain full upgrade.
    * Optimize batch compiler efficiency.
    * Optimize batch compiler memory management algorithm.
    * Support fmap over 4D.
    * Support more operators (Abs, Log, Pow, Sign).
    * Support mix accuracy mode.
    * Update environment packages.
    * Change default environment to `onnx1.13`.
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
