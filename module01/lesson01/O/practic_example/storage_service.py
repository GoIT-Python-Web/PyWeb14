from storage import JSONStorage, YamlStorage

"""
Более практический пример для принципа Open-closed. Разные хранилища для хранения данных.
"""


class StorageService:
    def __init__(self, storage: JSONStorage | YamlStorage):
        self.storage = storage

    def get(self, key: str) -> str:
        return self.storage.get_value(key)


if __name__ == '__main__':
    storage_json = StorageService(JSONStorage('data.json'))
    storage_yaml = StorageService(YamlStorage("data.yaml"))
    print(storage_json.get("username"))
    print(storage_yaml.get("username"))
