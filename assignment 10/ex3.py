import numpy as np


def create_data(setups: list[dict], seed=None) -> dict:
    np.random.seed(seed)
    result = dict()
    for i in setups:
        class_name = i["id"]
        n = i["n"]
        a = i["a"]
        b = i["b"]
        result.update({class_name: np.random.uniform(a, b, n)})
    return result


for id_, arr in create_data([
    {"id": "classA", "n": 10, "a": 0, "b": 1.5},
    {"id": "classB", "n": 20, "a": 3, "b": 4},
    {"id": "classC", "n": (5, 10), "a": 0, "b": 10}
], 0).items():
    print(id_, arr.shape)
    print(arr)
