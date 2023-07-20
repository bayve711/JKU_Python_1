list1 = []
max_len = 0
while True:
    cout1 = input("enter numbers").split()
    if cout1[0] == 'x':
        break
    else:
        cout1 = [int(item) for item in cout1]
        max_len = len(cout1) if len(cout1) > max_len else max_len
        list1.append(cout1)

for el in list1:
    while len(el) < max_len:
        el.append(0)

for el in list1:
    print(el)