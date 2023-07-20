matrix = []
max_rows = 0
row = [item for item in input("Enter the list items : ").split()]
while row[0] != "x":
    if len(row) > max_rows:
        max_rows = len(row)
    if len(row) < max_rows:
        row.append("0 "*(max_rows - len(row)))
    res = ' '.join(row)
    matrix.append(res)
    row = [item for item in input("Enter the list items : ").split()]
res1= '\n'.join(matrix)
print(f"[{res1}]")