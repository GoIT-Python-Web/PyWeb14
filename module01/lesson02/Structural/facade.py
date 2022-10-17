from math import pi
from enum import Enum

"""
Фасад (Facade)
Паттерн проектирования, который предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.
"""


class ShapeType(Enum):
    CIRCLE = "circle"
    SQUARE = "square"


class Square:
    def __init__(self, side: float):
        self.side = side

    def area_of(self):
        return self.side**2


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area_of(self):
        return self.radius**2 * pi


class FacadeShape:
    def __init__(self, size: float):
        self.square = Square(size)
        self.circle = Circle(size)

    def area_of(self, type_figure: ShapeType):
        area_for_figure = {
            ShapeType.CIRCLE: self.circle.area_of(),
            ShapeType.SQUARE: self.square.area_of(),
        }
        return area_for_figure.get(type_figure, None)


if __name__ == "__main__":
    shape = FacadeShape(42)
    print(shape.area_of(ShapeType.SQUARE))
    print(shape.area_of(ShapeType.CIRCLE))
    print(shape.area_of("ellipse"))
