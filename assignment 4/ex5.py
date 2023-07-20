def sort(elements: list, ascending: bool = True):
    if ascending is True:
        for i in range(len(elements)):
            for j in range(i + 1, len(elements)):
                if elements[i] > elements[j]:
                    elements[i], elements[j] = elements[j], elements[i]
        print(elements)
    else:
        for k in range(len(elements)):
            for h in range(k + 1, len(elements)):
                if elements[k] < elements[h]:
                    elements[k], elements[h] = elements[h], elements[k]
        print(elements)

some_list = [1, 3, 0, 4, 5]
sort(some_list)
sort(some_list, ascending = False)