
import json

import sys
import pathlib

def get_config_path():
    config_path = pathlib.Path(sys.argv[0]).parent / "config.json"
    return config_path

def _get_config():
    config_path = get_config_path()
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
    for k, v in config_data.items():
        if not v:
            raise ValueError("You need to add some value in config.json for key \"{}\"".format(k))
    return config_data

def get_config():
    try:
        config_data = _get_config()
    except FileNotFoundError:
        raise FileNotFoundError("Have you created 'config.json' file?")