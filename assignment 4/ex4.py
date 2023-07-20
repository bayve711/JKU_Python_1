def round_(number, ndigits: int = None):
    lst_num = []
    res = ""
    for i in str(number):
        try:
            lst_num.append(int(i))
        except:
            lst_num.append(str(i))
    k = lst_num.index('.')

    if ndigits is None:
        if lst_num[k + 1] > 5:
            lst_num[k - 1] += 1
        elif lst_num[k + 1] < 5:
            lst_num[k - 1] = lst_num[k - 1]
        else:
            if lst_num[k - 1] % 2 == 0:
                lst_num[k - 1] = lst_num[k - 1]
            else:
                lst_num[k - 1] += 1
        a = lst_num[:k]
        for val in a:
            res+=str(val)
        return res
    if ndigits == 0:
        if lst_num[k + 1] > 5:
            lst_num[k - 1] += 1
        elif lst_num[k + 1] < 5:
            lst_num[k - 1] = lst_num[k - 1]
        else:
            if lst_num[k - 1] % 2 == 0:
                lst_num[k - 1] = lst_num[k - 1]
            else:
                lst_num[k - 1] += 1
        lst_num[k + 1] = 0
        a = lst_num[:k + 2]
        for val in a:
            res+=str(val)
        return res
    elif ndigits >= len(lst_num[k+1:]):
        return number
    elif len(lst_num[:k]) == -ndigits:
        if lst_num[k + ndigits] > 5:
            lst_num[k + ndigits - 1] += 1
        elif lst_num[k + ndigits ] < 5:
            lst_num[k + ndigits - 1] = lst_num[k - 1 + ndigits]
        else:
            if lst_num[k + ndigits -1] % 2 == 0:
                lst_num[k + ndigits -1 ] = lst_num[k + ndigits -1]
            else:
                lst_num[k +ndigits] += 1
        lst_num[k +1] = 0
        if lst_num [k+ndigits] >= 5:
            for i in range(-1 * ndigits):
                lst_num[k - i - 1] = 0
            a = lst_num[:k + 2]
            a.insert(0, 1)
        else:
            for i in range(-1 * ndigits):
                lst_num[k - i - 1] = 0
            a = lst_num[:k + 2]

        for val in a:
            res += str(val)

        return res
    elif len(lst_num[:k]) < -ndigits:
        return 0.0
    elif ndigits < 0:
        if lst_num[k + ndigits] > 5:
            lst_num[k + ndigits - 1] += 1
        elif lst_num[k + ndigits ] < 5:
            lst_num[k + ndigits - 1] = lst_num[k - 1 + ndigits]
        else:
            if lst_num[k + ndigits -1] % 2 == 0:
                lst_num[k + ndigits -1 ] = lst_num[k + ndigits -1]
            else:
                lst_num[k +ndigits] += 1
        lst_num[k +1] = 0
        for i in range(-1*ndigits):
            lst_num[k - i - 1] = 0
        a = lst_num[:k + 2]
        for val in a:
            res += str(val)
        return res
    else:
        if lst_num[k + 1 + ndigits] > 5:
            lst_num[k + ndigits] += 1
        elif lst_num[k + ndigits + 1] < 5:
            lst_num[k + ndigits ] = lst_num[k + ndigits]
        else:
            if lst_num[k + ndigits] % 2 == 0:
                lst_num[k + ndigits] = lst_num[k + ndigits]
            else:
                lst_num[k + ndigits] += 1
        a = lst_num[:k + 1 + ndigits]
        for val in a:
            res += str(val)
        return res

print(round_(0))
print(round_(777.777, 0))
print(round_(777.777, 1))
print(round_(777.777,2))
print(round_(777.777,3))
print(round_(777.777,4))
print(round_(777.777, -1))
print(round_(777.777,-2))
print(round_(777.777, -3))
print(round_(777.777, -4))
