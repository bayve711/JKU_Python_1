from ex1 import Complex


def add(self, other: "Complex"):
    if isinstance(other, Complex) is True:
        self.real += other.real
        self.imaginary += other.imaginary
    else:
        raise TypeError("TypeError: Not an instance of 'Complex'")


Complex.add = add


def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
    if isinstance(comp, Complex) and (all(isinstance(a, Complex) for a in comps)) is True:
        obj = Complex(0.0, 0.0)
        Complex.add(obj, comp)
        for el in comps:
            Complex.add(obj, el)
        return obj
    else:
        raise TypeError("TypeError: Not an instance of 'Complex'")


Complex.add_all = add_all

# c1 = Complex(1.0, -2.0)
# c1.print()
# c2 = Complex(9.0,    100.0)
# c1.add(c2)
# c1.print()
# c_sum = Complex.add_all(c1,  c1,  c2,  Complex(33.75, -14.25))
# c_sum.print()
# c1.print()
# will_fail = Complex.add_all(100)
