from ex3 import Shape
from ex4 import Rectangle
from ex5 import Circle
class Square(Rectangle):
    def __init__(self, x: int, y: int, length: int):
        super().__init__(x, y, length, length)
        self.length = length
    def to_string(self) -> str:
        return super().to_string()
    def area(self):
        return super().area()


# s    =    Shape(4,    9)
# print(s.to_string())
# r    =    Rectangle(1,    2,    3,    4)
# print(r.to_string())
# print("Rectangle    area:",    r.area())
# c    =    Circle(5,    2,    2)
# print(c.to_string())
# print("Circle    area:",    c.area())
# s    =    Square(0,    0,    10)
# print(s.to_string())
# print("Square    area:",    s.area())