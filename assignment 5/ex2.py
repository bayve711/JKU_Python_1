def gen_range(start: int, stop: int, step: int = 1):
    if isinstance(start, int) is False or isinstance(stop, int) is False or isinstance(step, int) is False:
        raise TypeError
    if step == 0:
        raise ValueError
    if step > 0:
       i = start
       while i <= stop:
            yield i
            i += 1*step
    else:
        i = start
        while i >= stop:
            yield i
            i += 1 * step

print(list(gen_range(0, 10)))
print(list(gen_range(0, 10, 3)))
print(list(gen_range(0, 10, -1)))
print(list(gen_range(10, 0)))
print(list(gen_range(10, 0, -2)))
print(list(gen_range(-10, -3, 2)))
print(list(gen_range(0.0, 10)))
print(list(gen_range(0, 10, 0)))
