import json
import os

class ConfigUtility:
    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            return {}

    def write_config(self, config):
        with open(self.config_file, 'w') as f:
            json.dump(config, f)

    def get_key(self, key):
        config = self.read_config()
        return config.get(key)

    def set_key(self, key, value):
        config = self.read_config()
        config[key] = value
        self.write_config(config)

