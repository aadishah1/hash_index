import yaml
import os


class Config:
    def __init__(self, config_path="./config.yml"):
        self.config = dict()
        if os.path.exists(config_path):
            with open(config_path, "r") as config_file:
                try: 
                    self.config = yaml.safe_load(config_file)
                except yaml.YAMLError as exc:
                    print("Error occurred in reading config...")
                    exit(1)

    
    def get_key_from_config(self, key):
        return self.config.get(key, None)
