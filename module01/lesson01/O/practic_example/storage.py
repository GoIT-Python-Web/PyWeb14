import json
import yaml


class Storage:

    def get_value(self, key) -> str:
        raise NotImplementedError


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key) -> str:
        with open(self.filename, "r") as f:
            data = json.load(f)
            return data.get(key, None)


class YamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key) -> str:
        with open(self.filename, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data.get(key, None)
