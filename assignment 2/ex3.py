num = int(input("Enter number to guess: "))
a = True
while a is True:
    x = input("Enter number: ")
    try:
        if int(x) < num:
            print("Your number is smaller")
        if int(x) > num:
            print("Your number is bigger")
        if int(x) == num:
            print("Congratulations")
            a = False
    except:
        if str(x) == "exit":
            print("You lost!")
            a = False
