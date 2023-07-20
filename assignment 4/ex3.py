def create_train_test_splits(data: list, train_size: float) -> tuple:
    size2 = int(len(data) - ((train_size * 100 // 10)))
    size1 = int(len(data) - size2)
    lst1 = data.copy()[:size1]
    lst2 = data.copy()[size1:]
    result = (lst1, lst2)
    return result

print(create_train_test_splits([], 0.5))
print(create_train_test_splits(list(range(10)), 0.5))
print(create_train_test_splits(list(range(10)), 0.67))
