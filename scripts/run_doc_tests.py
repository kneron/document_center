import argparse
import os
import subprocess
import logging
import shutil

from config_parser import parse_config
from code_generator import generate_test_file, TEST_FOLDER

def run_test_file(test_folder, docker):
    test_folder = os.path.join(os.getcwd(), test_folder)
    commands = ['docker', 'run', '--rm',
        '-v', test_folder + ':/data1',
        docker, '/bin/bash',
        '-i', '-c', 'conda activate && /bin/bash /data1/run.sh']
    p = subprocess.run(commands)
    return p.returncode == 0


if __name__ == '__main__':
    # Parse argument
    arg_parser = argparse.ArgumentParser(description="Test toolchain document.")
    arg_parser.add_argument('toolchain', help="toolchain docker image tag")
    arg_parser.add_argument('-c', dest='config_file', default="config.json", type=str, help="specify configuration file. Defaults to config.json")
    args = arg_parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    # Parse config.
    configs = parse_config(args.config_file)
    # Prepare outer folder
    if os.path.isdir(TEST_FOLDER):
        logging.warning(f"{TEST_FOLDER} is found and removed.")
        shutil.rmtree(TEST_FOLDER)
    os.mkdir(TEST_FOLDER)
    # Prepare test files
    for config in configs:
        test_folder = generate_test_file(config)
        if run_test_file(test_folder, args.toolchain):
            logging.info(f"{config['id']}: passed.")
        else:
            logging.error(f"{config['id']}: failed. Please check {test_folder}/console_output.txt for details.")
