def flatten(nested: list) -> list:
    def iterate(a: list):
        for b in range(len(a)):
            if isinstance(a[b], list) is False:
                result.append(a[b])
            else:
                iterate(a[b])

    result = []
    our = nested
    for i in range(len(our)):
        if isinstance(our[i], list) is False:
            result.append(our[i])
        else:
            iterate(our[i])

    return result

print(flatten([1, 2, 4, [5, [6, 7, 9]], 8, 9]))
print(flatten([[], [], [1], [], [1, [], [4, 5, [[[6]]]], 2, 3]]))
print(flatten([[]]))
print(flatten([1, 2, [4, [8, 9, [11, 12], 10], 5], 3, [6, 7]]))