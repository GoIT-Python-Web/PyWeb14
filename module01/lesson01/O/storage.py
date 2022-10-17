import json
import yaml
from abc import abstractmethod, ABC


class IStorage(ABC):
    @abstractmethod
    def get_value(self, key) -> str:
        pass


class JSONStorage(IStorage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key) -> str:
        with open(self.filename, "r") as f:
            data = json.load(f)
            return data.get(key, None)


class YamlStorage(IStorage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key) -> str:
        with open(self.filename, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data.get(key, None)
