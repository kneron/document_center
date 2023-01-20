import re
import os
import logging


TEST_FOLDER='generated_tests'


def parse_python_code(filename):
    # Load file
    f_str = ''
    with open(os.path.join('..', 'docs', filename), 'r') as f:
        f_str = f.read()
    # Regex parse
    pattern = re.compile(r'^```python.*?^```', re.MULTILINE | re.DOTALL)
    raw_code_blocks = pattern.findall(f_str)
    # Remove code block starter and \n
    code_blocks = []
    for raw_code in raw_code_blocks:
        code = raw_code[len('```python') + 1:-len('```')]
        if code.startswith('#['):
            # This should be special code block.
            continue
        code_blocks.append(code)
    return code_blocks


def generate_test_file(config):
    # Prepare base directory
    base_dir = os.path.join(TEST_FOLDER, config["id"])
    os.mkdir(base_dir)

    # Prepare test files
    run_code = "#!/bin/bash\n\n"
    end_of_command = " >> /data1/console_output.txt 2>&1\n"

    # Prepare preprocess if any.
    if "preprocess" in config:
        logging.error("Currently, preprocess is not supported.")
        exit(1)
    # Prepare test file for code block.
    if config["mode"] == "single file":
        full_code = ""
        for file in config["files"]:
            code_blocks = parse_python_code(file)
            if len(code_blocks) == 0:
                continue
            full_code += "\n\n#"
            full_code += "=" * 40
            full_code += f"\n# [Manual Tester] {file} generated codes\n"
            for code in code_blocks:
                full_code += code
        with open(os.path.join(base_dir, 'main.py'), 'w', newline='\n') as f:
            f.write(full_code)
        run_code += "echo \"[main.py]\"" + end_of_command
        run_code += "python /data1/main.py" + end_of_command
    else:
        logging.error("Currently, multiple files mode is not supported yet.")
        exit(1)
    # Prepare postprocess is any
    if "postprocess" in config:
        logging.error("Currently, postprocess files mode is not supported.")
        exit(1)
    # Prepare run.sh.
    with open(os.path.join(base_dir, 'run.sh'), 'w', newline='\n') as f:
        f.write(run_code)
    return base_dir

if __name__ == '__main__':
    results = parse_python_code('toolchain/manual_1_overview.md')
    print(results)
