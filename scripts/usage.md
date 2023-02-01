# Manual Runner

## How to use

1. Change directory under `scripts`.
2. Run `run_doc_test.py` with python3 and the environment docker.

## How prepare your manual

1. For all the code blocks you want to run the tests. The code block should be python code block.
2. If you don't want to include a python code block, add `#[` at the start just at the first line beginning inside the code block. For example, `#[Note]`.
3. Edit `config.json`.

## Configuration

The configuraion is a json file with a list at the outer most level. Each object has the following attribute:

* **id**: *Required*. An unique string to identify the test. It is used as the test file name so please avoid using special characters.
* **files**: *Required*. A non-empty list of paths from the document root. The document to be included in the test.
* **mode**: *Optional*. A string indicate the way to treat code blocks. Available modes: "single file", "multiple files". In single file mode, all code blocks are combined into one file. In multiple files mode, each code block is saved as a seperate file. Defaults to "single file".
* **preprocess**: *Optional*. A List of string where each string is a command to be run before running the generated scripts. Defaults to [].
* **postprocess**: *Optional*. A List of string where each string is a command to be run after running the generated scripts. Defaults to [].
