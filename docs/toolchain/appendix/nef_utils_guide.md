# Kneron NEF Utils Guide

## 0. Usage

```shell
./kneron_nef_utils <section> <options>

  section list:
    EXTRACT_NEF     : -X(--extract) <nef_file_path> -l(--keep_all) -s(--parse_setup_bin)
    GEN_NEF         : -G(--gen) [-h(--header) <fw_info_path> -m(--model) <all_models_path>]|[-e(--kne) <kne_path>] -t(--target) "target"
    DUMP_DATA       : -I(--info) <nef_file_path>
    READ_NEF        : -R(--read) <nef_file_path> -k(--header_key) "info_key"
    COMBINE_NEF     : -c(--combine_nef) NEF_1 NEF_2 NEF_3...
    POST_ENC        : -E(--enc) <nef_file_path> -n(--KN) "kn_number"; [Linux Only]

  options:
    -o, --output    : output file name prefix, defautl is "model_(target)"
    -O, --folder    : output folder, defautl is "output/"
    -V, --version   : show version number
    -H, --help      : show this message

---
```

## 1. Extract NEF

* **Extract NEF to get fw_info.bin & all_models.bin or modes_730.kne**

    Command Line:

    ```shell
    ./kneron_nef_utils --extract path/to/file.nef
    ```

    Result:

    ```shell
    NEFv0 or NEFv1:
    ├── all_models.bin
    └── fw_info.bin

    NEFv2:
    └── NEF_0x25F8D591_models_730.kne
    ```

* **Extract NEF to get all models.bin or models.kne**

    Command Line:

    ```shell
    ./kneron_nef_utils --extract path/to/file.nef --keep_all
    ```

    Result:

    ```shell
    NEFv0 or NEFv1:
    ├── all_models.bin
    ├── fw_info.bin
    ├── NEF_0xF6D172C6_modelid_32771_command.bin
    ├── NEF_0xF6D172C6_modelid_32771_setup.bin
    ├── NEF_0xF6D172C6_modelid_32771_test.conf
    ├── NEF_0xF6D172C6_modelid_32771_weight.bin
    ├── NEF_0xF6D172C6_modelid_32772_command.bin
    ├── NEF_0xF6D172C6_modelid_32772_setup.bin
    ├── NEF_0xF6D172C6_modelid_32772_test.conf
    └── NEF_0xF6D172C6_modelid_32772_weight.bin

    NEFv2:
    ├── NEF_0x25F8D591_model_211.kne
    └── NEF_0x25F8D591_models_730.kne
    ```

* **Extract NEF to get all models.bin or models.kne and parse it.**

    Command Line:

    ```shell
    ./kneron_nef_utils --extract path/to/file.nef --keep_all -s
    ```

    Result:

    ```shell
    NEFv0 or NEFv1:
    ├── all_models.bin
    ├── fw_info.bin
    ├── NEF_0xF6D172C6_modelid_32771_command.bin
    ├── NEF_0xF6D172C6_modelid_32771_setup.bin
    ├── NEF_0xF6D172C6_modelid_32771_setup.bin.json
    ├── NEF_0xF6D172C6_modelid_32771_test.conf
    ├── NEF_0xF6D172C6_modelid_32771_weight.bin
    ├── NEF_0xF6D172C6_modelid_32772_command.bin
    ├── NEF_0xF6D172C6_modelid_32772_setup.bin
    ├── NEF_0xF6D172C6_modelid_32772_setup.bin.json
    ├── NEF_0xF6D172C6_modelid_32772_test.conf
    └── NEF_0xF6D172C6_modelid_32772_weight.bin

    NEFv2:
    ├── NEF_0x25F8D591_model_211.kne
    ├── NEF_0x25F8D591_model_211.kne.no_binary.json
    └── NEF_0x25F8D591_models_730.kne
    ```

## 2. Generated NEF

* **Generated NEF by fw_info.bin & all_models.bin or modes_730.kne**

    Command Line:

    ```shell
    NEFv0 or NEFv1:
    ./kneron_nef_utils --gen \
                       --header path/to/fw_info.bin \
                       --model path/to/all_models.bin \
                       --target "target"

    NEFv2:
    ./kneron_nef_utils --gen --kne path/to/modes_730.kne --target 730
    ```

    Result:

    ```shell
    NEFv0 or NEFv1:
    └── output/models_720.nef

    NEFv2:
    └── output/models_730.nef
    ```

## 3. Combine NEF

* **Combine Multiple NEF into Single NEF**

    Command Line:

    ```shell
    ./kneron_nef_utils --combine_nef path/to/file_A.nef path/to/file_B.nef
    ```

    Result:

    ```shell
    NEFv0 or NEFv1:
    └── output/models_720.nef

    NEFv2:
    └── output/models_730.nef
    ```

## 4. Dump NEF Information

* **Dump all NEF header information**

    Command Line:

    ```shell
    ./kneron_nef_utils --info path/to/file.nef
    ```

    Result:

    ```shell
    NEF Header:
    platform:
    target: 720
    crc: 0x4EB30A7D
    kn_number: 0x0
    encryption_mode: NONE
    compiler_version: v0.9.1(e9ab1ffd6)
    toolchain_version: kneron/toolchain:v0.20.1

    schema_version: v1.0.0
    uuid: 0x4EB30A7D
    solution_id:
    solution_tag:

    ---------------------------

    NEF Model Info:
    ++++++++++++++++++++++
    Model_ID: 32771
    Model_Name: resnet50_opt.bie
    Model_Version: 0x1
    ===========================
    ```

## 5. Read NEF Header by Header Key

* **Read single header value form giving NEF file**

    Command Line:

    ```shell
    ./kneron_nef_utils --read path/to/file.nef --header_key schema_version
    ```

    Result:

    ```shell
    v2.0.1
    ```

## 6. Post Encrypt NEF

* **Post encrypt NEF with KN number**

    Command Line:

    ```shell
    ./kneron_nef_utils --enc path/to/file.nef --KN c506203c
    ```

    Result:

    ```shell
    Output file path:
    └── output/models_720.enc.nef

    NEF Header:
    ...
    target: 720
    crc: 0x3C52218D
    kn_number: 0xC506203C
    encryption_mode: KN_Number
    ...

    ---------------------------
    ```
