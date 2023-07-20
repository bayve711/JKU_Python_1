import math
from ex3 import Shape


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def to_string(self) -> str:
        return str(f"{type(self).__name__}: x={self.x}, y={self.y}, radius={self.radius}")

    def area(self) -> float:
        return pow(self.radius, 2) * math.pi
