lower = []
upper = []
other = []
unique = []
sent = str(input("Enter string: "))
for elem in sent:
    if elem not in unique:
        unique.append(elem)
    if elem.isupper() is True:
        upper.append(elem)
        continue
    if elem.islower() is True:
        lower.append(elem)
        continue
    else:
        other.append(elem)

print(f"lowercase: {lower}\n"
      f"uppercase: {upper}\n"
      f"other: {other}\n"
      f"unique: {unique}")
