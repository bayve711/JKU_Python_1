def f(x: int):
    try:
        g(x)
        print("f1")
    except TypeError:
        print("f2")
        raise SyntaxError
    except ValueError:
        print("f3")
    except SyntaxError:
        print('done')
    else:
        print("f4")
    print("f5")

def g(x: int):
    try:
        h(x)
        print("g1")
    except TypeError:
        print("g2")
        if x < -10:
            raise SyntaxError
        print("g3")
    finally:
        print("g4")
def h(x: int):
    try:
        if x < 0:
            raise TypeError
        if x > 10:
            raise ValueError
    finally:
        print("h1")

    print("h2")

#ErrorA - TypeError
#ErrorB - ValueError
#ErrorC - SyntaxError


f(-15)