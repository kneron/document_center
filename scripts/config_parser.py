import json
import logging
import os

def invalid_config(msg):
    logging.error("Invalid configuration file. " + msg)
    exit(1)

def parse_config(config_path):
    # Load config file
    if not os.path.isfile(config_path):
        logging.error(f"Cannot find input config file {config_path}")
        exit(1)
    with open(config_path, 'r') as f:
        config_object = json.load(f)

    # Check config file
    if type(config_object) != type(list()):
        invalid_config("The outer most structure should be a list.")
    ids = set()
    required_keys = ['id', "files"]
    for config in config_object:
        if type(config) != type(dict()):
            invalid_config("The config should be a list of dictionary.")
        for key in required_keys:
            if key not in config:
                invalid_config(f"'{key}' is required but not found.")
        # Check id.
        if type(config['id']) != type(str()):
            invalid_config("'id' should be a string.")
        if len(config['id']) == 0:
            invalid_config("'id' is empty.")
        if config['id'] in ids:
            invalid_config(f"'id' should be unique. But there are at least two '{config['id']}'.")
        ids.add(config['id'])
        # Check files
        if type(config['files']) != type(list()):
            invalid_config(f"Test {config['id']}: 'files' should be a list.")
        if len(config['files']) == 0:
            invalid_config(f"Test {config['id']}: 'files' should not be empty.")
        for path in config['files']:
            if type(path) != type(str()):
                invalid_config(f"Test {config['id']}: 'files' should be a list of string.")
            if len(path) == 0:
                invalid_config(f"Test {config['id']}: empty path is found in 'files'.")
            relative_path = os.path.join("..", "docs", path)
            if not os.path.isfile(relative_path):
                invalid_config(f"Test {config['id']}: file {path} is not found.")
        # Check mode.
        if "mode" not in config:
            config["mode"] = "single file"
        else:
            if config["mode"] not in ["single file", "multiple files"]:
                invalid_config(f"Test {config['id']}: unknown mode {config['mode']}.")
        # Check preprocess
        if "preprocess" in config:
            if type(config['preprocess']) != type(list()):
                invalid_config(f"Test {config['id']}: 'preprocess' should be a list.")
            for command in config["preprocess"]:
                if type(command) != type(str()):
                    invalid_config(f"Test {config['id']}: 'preprocess' should be a list of string.")
        # Check postprocess
        if "postprocess" in config:
            if type(config['postprocess']) != type(list()):
                invalid_config(f"Test {config['id']}: 'postprocess' should be a list.")
            for command in config["postprocess"]:
                if type(command) != type(str()):
                    invalid_config(f"Test {config['id']}: 'postprocess' should be a list of string.")
    return config_object
