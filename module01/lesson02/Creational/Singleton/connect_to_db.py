from dataclasses import dataclass

# Пример применения синглтона -> подключение к БД из любого места программы


class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


# Показать dataclass
@dataclass
class Settings(metaclass=MetaSingleton):
    db: str = "MySQL"
    port: int = 3306


if __name__ == '__main__':

    connect = Settings()

    connect_other = Settings()

    print(connect_other.port)
    connect.port = 5634
    print(connect_other.port)
