import numpy as np
import random


def extend(arr: np.ndarray, size: int, fill=None) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError
    elif size < 1:
        raise ValueError
    else:
        length = arr.size
        len1 = length
        len2 = length
        summary = 0
        i = 0
        if np.issubdtype(arr.dtype, np.number) is True:
            while i < len1:
                summary += arr[i]
                i += 1
            mean = summary / i
        else:
            mean = "mean"
        arr1 = arr.copy()
        while len2 < size:
            arr1 = np.append(arr1, 0)
            len2 += 1
        while length < size:
            if fill is None:
                arr1[length] = random.randint(1, 100000000)
                length += 1
            elif fill == "mean":
                arr1[length] = mean
                length += 1
            else:
                arr1[length] = fill
                length += 1
        return arr1


print(extend(np.arange(4), 7))
print(extend(np.arange(4), 7, fill=0))
print(extend(np.arange(4), 7, fill="mean"))
print(extend(np.arange(4, dtype=float), 7, fill="mean"))
print(extend(np.array(["hello", "world"]), 5, "mean"))
