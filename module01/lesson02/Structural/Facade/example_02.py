from math import pi
from enum import Enum

"""
Ця реалізація надає простий та уніфікований інтерфейс (клас FacadeShape) для доступу до методів обчислення площі класів 
Square та Circle. Клієнтський код може використовувати клас FacadeShape для обчислення площі квадрата або кола, 
не турбуючись про деталі реалізації окремих класів. Використання перечислення для ShapeType робить код більш 
читабельним і менш схильним до помилок, оскільки клієнтський код може передавати тільки допустимі значення для 
типу фігури.
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
