# Build Kneron PLUS

**Note**: If you are using Windows, please execute all the instruction below in MSYS2 MinGW 64-bit.

**Note**: To execute **MSYS2 MinGW 64-bit**, please use the shortcut or `c:\msys64\msys2_shell.cmd -mingw64` instead of `c:\msys64\mingw64.exe`.

**Note**: Some examples may cause warnings during cmake process due to the length of the paths. You can rename these examples to shorter names to avoid these warnings.

## 1. Download Kneron PLUS

1. If you are a regular user:

    - Download the latest **kneron_plus_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS** section.

    - Decompress the **kneron_plus_vXXX.zip**

        ```bash
        $ unzip kneron_plus_vX.X.X.zip
        ```

2. If you are an enterprise user:

    - Download the latest **kneron_plus_enterprise_vXXX.zip** into Ubuntu from <https://www.kneron.com/tw/support/developers/>. It is located at **Kneron PLUS - enterprise** section.

    - Decompress the **kneron_plus_enterprise_vXXX.zip**

        ```bash
        $ unzip kneron_plus_enterprise_vX.X.X.zip
        ```

## 2. Build Code

During the process of building the library of Kneron PLUS, Few examples will also be built together.

Kneron PLUS has provided three kinds of examples:

- General Examples
    - Examples which teach you how to use Kneron PLUS APIs.

- OpenCV Examples
    - Examples which show you how to use web camera to process inference.

- DFUT_console
    - A tool which helps you upgrade devices if **Kneron DFUT** is not available for you.
    - Only provided in Kneron PLUS v1.3.0 and above.

During **cmake** process, different combinations of these examples will be built based on the parameter you gave.

The library file of Kneron PLUS and executables of examples will be locate at **build/bin/**.

### 2.1 Build with General Examples

1. If you are using Ubuntu:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j
    ```

2. If you are using MSYS2 MinGW 64-bit in Windows:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake .. -G"MSYS Makefiles"
    $ make -j
    ```

### 2.2 Build with OpenCV Examples

1. If you are using Ubuntu:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake -DWITH_OPENCV=ON ..
    $ make -j
    ```

2. If you are using MSYS2 MinGW 64-bit in Windows:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake -DWITH_OPENCV=ON .. -G"MSYS Makefiles"
    $ make -j
    ```

### 2.3 Build with DFUT_console

1. If you are using Ubuntu:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake -DWITH_DFUT=ON ..
    $ make -j
    ```

2. If you are using MSYS2 MinGW 64-bit in Windows:

    ```bash
    $ cd kneron_plus/
    $ mkdir build
    $ cd build
    $ cmake -DWITH_DFUT=ON .. -G"MSYS Makefiles"
    $ make -j
    ```

## 3. Check if PLUS examples are built successfully.

```bash
$ ls bin/

    kl520_demo_customize_inf_multiple_models
    kl520_demo_customize_inf_single_model
    kl520_demo_generic_image_inference
    ...
```