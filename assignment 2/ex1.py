age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age <= 7:
    print("Child ticket: 10$")
elif age>=8 and age<=17:
    print("Teenager ticket: 15$")
else:
    sal = int(input("Enter salary: "))
    if sal < 0:
        print("Invalid salary")
    elif sal <= 1000:
        print("Reduced adult ticket 1: 20$")
    elif sal >= 1001 and sal <= 2000:
        print("Reduced adult ticket 2: 25$")
    else:
        print("Adult ticket: 30$")
