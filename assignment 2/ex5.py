print("Welcome to Data Statistics!")
loop = True
sum = 0
count=0
n=0
while loop is True:
    print("\n"
         "Available actions:\n"
         "a - Add numbers\n"
         "v - View statistics\n"
         "x - Exit the program")
    action = input("Enter action: ")
    if str(action) == "a":
        a = input("Enter number or 'x' when you are done: ")
        try:
            try_min = int(a)
            try_max = int(a)
        except:
            continue
        while str(a) != "x":
            count+=1
            sum+=int(a)
            n+=1
            avg = sum/n
            if int(a) < try_min:
                min = int(a)
            else:
                min = try_min

            if int(a)>try_max:
                max = int(a)
            a = input("Enter number or 'x' when you are done: ")
        continue
    if str(action) == "v":
        if count != 0:
            print(f"Count: {count}\n"
                  f"Sum: {sum}\n"
                  f"Avg: {avg}\n"
                  f"Min: {min}\n"
                  f"Max: {max}")
            continue
        else:
            print("No numbers have been added yet!")
            continue
    if str(action) == "x":
        print("Bye!")
        loop = False
    else:
        print(f"Invalid action '{str(action)}'. Try again!")









