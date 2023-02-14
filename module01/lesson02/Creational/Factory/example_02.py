"""
Паттерн "Фабрика" позволяет создавать объекты без указания конкретных классов создаваемых объектов. 
Вместо этого, клиентский код запрашивает создание объектов через фабричный метод. 
Пример кода ниже показывает использование паттерна "Фабрика" для создания объектов различных типов автомобилей:
"""


class Car:
    def __init__(self):
        self._type = None

    def get_type(self):
        return self._type


class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self._type = "Sports car"


class FamilyCar(Car):
    def __init__(self):
        super().__init__()
        self._type = "Family car"


class CarFactory:
    def __init__(self):
        self._cars = {}

    def register_car(self, car_type, car_class):
        self._cars[car_type] = car_class

    def create_car(self, car_type):
        if car_type not in self._cars:
            raise ValueError(f"Invalid car type: {car_type}")
        return self._cars[car_type]()


if __name__ == '__main__':
    factory = CarFactory()
    factory.register_car("sports", SportsCar)
    factory.register_car("family", FamilyCar)

    car = factory.create_car("sports")
    print(car.get_type())  # Output: Sports car
    car = factory.create_car("family")
    print(car.get_type())  # Output: Family car
