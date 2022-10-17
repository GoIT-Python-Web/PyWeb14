from math import pi
from abc import abstractmethod, ABC
from typing import List


class IShape(ABC):
    @abstractmethod
    def area_of(self):
        pass


class Rect(IShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Square(IShape):
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2


class Circle(IShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


class AreaCalculator:
    def __init__(self, shapes: list[IShape]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum_ = 0
        for shape in self.shapes:
            sum_ += shape.area_of()
        return sum_


ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Circle(20), Rect(3, 3), Square(10)])
area = ar_sh.total_area()
print(area)
