def round_(number, ndigits: int = None):
    if ndigits is None:
        n_int = format(number, ".0f")
        return int(n_int)
    elif ndigits == 1:
        return format (number, ".1f")
    else:
        n_tmp = number * (10**ndigits)
        n_float = float(format (n_tmp, ".0f"))
        return n_float * (10**-ndigits)

print(round_(777.777))
print(round_(777.777, 0))
print(round_(777.777, 1))
print(round_(777.777, 2))
print(round_(777.777,3))
print(round_(777.777,4))
print(round_(777.777, -1))
print(round_(777.777,-2))
print(round_(777.777, -3))
print(round_(777.777, -4))