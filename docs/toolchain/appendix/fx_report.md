# How to Interpret Fixed-Point Report

After running the fixed-point analysis step described in the toolchain manual, you would find `model_fx_report.html`.
This document describes how to interpret the report. The report is divided into two sections: summary and node
information table.

## Summary

The summary will show the ip evaluator information.

<div align="center">
<img src="../../imgs/fx_report/summary.png">
<p><span style="font-weight: bold;">Figure 1.</span> Summary </p>
</div>

## Node information table

<div align="center">
<img src="../../imgs/fx_report/table_1.png">
<p><span style="font-weight: bold;">Figure 2.</span> Table left side </p>
</div>

* Node: the frontend node name in decomposed onnx.
* SNR: snr for this frontend node, if calculated. (Note: To see all layer’s SNR, the per-layer dump must turned on. However, the process time will be much longer)
* Node origin: the corresponding node name in origin.onnx provided by user.
* Type: NPU or CPU.
* Bw in / bw out / bw weight: the bitwidth used for the input / output / weight of this node.
* Node backend: the name of corresponding backend nodes.

<div align="center">
<img src="../../imgs/fx_report/table_2.png">
<p><span style="font-weight: bold;">Figure 3.</span> Table right side </p>
</div>

* CMD_node_idx: run in which command node
* MAC_cycle: how many mac cycles for this backend node.
* MAC_runtime(ms): how many miliseconds used in this backend node.
* RDMA_amount (Byte): RDMA amount for this backend node.
* WDMA_amount (Byte): WDMA amount for this backend node.
* Weight_amount (Byte): weight amount for this backend node.
* Runtime (ms): operator runtime.
* in_fmt / out_fmt: input/output data formats. If only one input/output or multiple inputs/outputs with same format, the only format will be shown. If multiple formats for this node, then the details will be listed as “FORMAT1:IN1,IN2 \\ FORMAT2:IN3”.
