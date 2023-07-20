def clip(*args, min_=0, max_=1) -> list:
    if args is None:
        return []
    else:
        res = []
        for elem in args:
            if elem < min_:
                res.append(min_)
            elif elem > max_:
                res.append(max_)
            else:
                res.append(elem)
        return res

print(clip())
print(clip(1, 2, 0.1, 0))
print(clip(-1, 0.5))
print(clip(-1, 0.5, min_=-2))
print(clip(-1, 0.5, max_=0.3))
print(clip(-1, 0.5, min_=2, max_=3))