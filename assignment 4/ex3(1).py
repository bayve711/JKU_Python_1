def create_train_test_splits(data: list, train_size: float) -> tuple:
    amount = len(data)-int((train_size*100//10))
    lst_1 = data.copy()
    lst_2 = []
    res = ()
    for i in range(1,amount+1):
        lst_2.append(data[-i])
    lst_2.sort()
    for k in range(1, amount+1):
        del lst_1[-1]

    tpl = (lst_1, lst_2)
    return tpl

print(create_train_test_splits([], 0.5))
print(create_train_test_splits(list(range(10)), 0.5))
print(create_train_test_splits(list(range(10)), 0.67))

