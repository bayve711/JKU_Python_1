print("Welcome to Powerlifting Data Collector!")
loop = True
names = dict()
while loop is True:
    print("\n"
         "Available actions:\n"
         "a - Add lifter\n"
         "r - Remove lifter\n"
         "u - Update lifter\n"
         "v - View lifters\n"
         "x - Exit the program")
    action = input("Enter action: ")
    if str(action) == "a":
        a = input("Enter new lifter name: ")
        if a not in names:
            names[a] = {"squat": [],
                 "bench press": [],
                 "deadlift": []}
            continue
        elif a in names:
            print(f"Lifter '{a}' already exists!")
            continue
    if str(action) == "r":
        b = input("Enter lifter name to remove: ")
        if b in names.keys():
            del names[b]
            continue
        else:
            print(f"Lifter '{b}' does not exist!")
            continue
    if str(action) == "u":
        c = input("Enter lifter name to update: ")
        if c not in names.keys():
            print(f"Lifter '{c}' does not exist!")
            continue
        else:
            stat = input("Enter lift (one of 'squat', 'bench press', 'deadlift'): ")
            if str(stat) == "squat":
                sq = list(map(float, input("Enter weight(s): ").split()))
                names[c]["squat"].append(sq)
            if str(stat) == "bench press":
                sq = list(map(float, input("Enter weight(s): ").split()))
                names[c]["bench press"].append(sq)
            if str(stat) == "deadlift":
                sq = list(map(float, input("Enter weight(s): ").split()))
                names[c]["deadlift"].append(sq)
            continue

    if str(action) == "v":
        if len(names) > 0:
            for val in names:
                print("-"*30)
                print("Name: %s\nsquat: %s\nbench press: %s\ndeadlift: %s" % (
        val, str(names[val]['squat']).replace("'", "").replace("[", "", 1).replace("]", "", 1),
        str(names[val]['bench press']).replace("'", "").replace("[", "", 1).replace("]", "", 1),
        str(names[val]['deadlift']).replace("'", "").replace("[", "", 1).replace("]", "", 1)))
        continue
    if str(action) == "x":
        print("Bye!")
        loop = False
        continue
    else:
        print(f"Invalid action '{str(action)}'. Try again!")









