import math


class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def print(self):
        if self.imaginary < 0:
            sign = "-"
        else:
            sign = "+"
        print(f"{self.real} {sign} {abs(self.imaginary)}i")

    def abs(self) -> float:
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

# c1=Complex(1.2, -5.4)
# c1.print()
# c2 = Complex(3.0, 4.0)
# c2.print()
# print(c2.abs())
