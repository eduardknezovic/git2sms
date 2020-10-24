
import json

import sys
import pathlib

def _get_config_path():
    config_path = pathlib.Path(sys.argv[0]).parent / "config.json"
    return config_path

def _get_config():
    config_path = _get_config_path()
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
    return config_data

def _validate_config(config_data):
    for k, v in config_data.items():
        if not v:
            raise ValueError("You need to add some value in config.json for key \"{}\"".format(k))

def get_config():
    try:
        config_data = _get_config()
        _validate_config(config_data)
    except FileNotFoundError:
        raise FileNotFoundError("Have you created 'config.json' file?")
    return config_data
