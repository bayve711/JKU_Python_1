def binary_search(elements: list, x) -> bool:
    res = elements.copy()
    num = x

    try:
        if len(res)%2 != 0:
            index1 = (len(res)+1)//2
        else:
            index1 = (len(res))//2
        if len(res) > 2:
            lst1 = res[:index1]
            lst2 = res[index1 + 1:]
        else:
            if res[0] == x:
                return True
            elif res[1] == x:
                return True
            else:
                return False

        if res[index1] == num:
            return True
        elif x < res[index1]:
            return binary_search(lst1, num)
        elif x > res[index1]:
            return binary_search(lst2, num)
    except:
        return False

my_sorted_list = [1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
print(binary_search(my_sorted_list, 1))
print(binary_search(my_sorted_list, 20))
print(binary_search(my_sorted_list, 21))
print(binary_search(my_sorted_list, "hello"))





