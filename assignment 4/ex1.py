def fib(n: int) -> int:
    while True:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n < 0:
            return -1
        else:
            a = fib(n - 1) + fib(n - 2)
            return a



print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(7))
print(fib(-2))




