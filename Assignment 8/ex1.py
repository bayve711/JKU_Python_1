import math
class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary
    def __eq__(self, other):
        if isinstance(other, Complex) is True:
            if self.real == other.real and self.imaginary == other.imaginary:
                return True
            else:
                return False
        else:
            return NotImplemented
    def __repr__(self):
        return str(f"Complex(real={self.real}, imaginary={self.imaginary})")
    def __str__(self):
        if self.imaginary < 0:
            sign = "-"
        else:
            sign = "+"
        return str(f"{self.real} {sign} {abs(self.imaginary)}i")
    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)
    def __add__(self, other):
        if isinstance(other, Complex) is True:
            real2 = self.real + other.real
            imag2 = self.imaginary + other.imaginary
            return Complex(real2, imag2)
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, Complex) is True:
            self.real += other.real
            self.imaginary += other.imaginary
            return Complex.__str__(self)
        else:
            return NotImplemented
    @staticmethod
    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        real3 = comp.real
        imag3 = comp.imaginary
        for el in comps:
            real3 += el.real
            imag3 += el.imaginary
        return Complex(real3, imag3)

# c1    =    Complex(-1,    -2)
# c2 = Complex(2, 4)
# c3 = Complex(1, 2)
# print(c1    ==    c3,    c1    +    c2    ==    c3)
# print(repr(c1))
# print(c1)
# print(abs(c1))
# print(c1    +    c2)
# c1    +=    c3
# print(c1)
# print(Complex.add_all(c2,    c2,    c3))
# try:
#     c1    +    1
# except    TypeError as e:
#     print(f"{type(e).__name__}: {e}")


