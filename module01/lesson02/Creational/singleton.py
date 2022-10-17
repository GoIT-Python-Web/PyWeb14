class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class InheritSingleton(Singleton):
    pass


# Проблема с наследованием стандартного синглтон
sg1 = Singleton()
sg2 = Singleton()
inhsg = InheritSingleton()
print(sg1 == sg2)
print(sg1 == inhsg)


# Переход к Meta для избавления (наследуемый не является тем же экземпляром)
class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class InheritMetaSingleton(metaclass=MetaSingleton):
    pass


class InheritInheritMetaSingleton(InheritSingleton):
    pass


sg1 = InheritMetaSingleton()
sg2 = InheritMetaSingleton()
inhsg = InheritInheritMetaSingleton()
print(sg1 == sg2)
print(sg1 == inhsg)
