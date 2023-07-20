result = dict()
string = str(input("Enter string: "))
low_string = string.lower()
for let in low_string:
    result[let] = result.get(let, 0) + 1
print(result)
