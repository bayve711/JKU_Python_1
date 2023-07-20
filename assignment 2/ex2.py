text = str(input("Enter text: "))
sum = 0
for let in text:
    if let.isupper() is True:
        sum+=1
if sum == 1:
    print(f"The input text contains {sum} uppercase character.")
else:
    print(f"The input text contains {sum} uppercase characters.")
