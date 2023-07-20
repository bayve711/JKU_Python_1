def read_numbers(path: str) -> list:
    handle = open(path, "r")
    nums = []
    for line in handle:
        ind = 0
        for i in range(len(line)):
                if line[i] != " " and line[i] != "\n":
                    continue
                else:
                    try:
                        nums.append(int(line[ind:i]))
                        ind = i + 1
                    except:
                        try:
                            nums.append(float(line[ind:i]))
                            ind = i + 1
                        except:
                            ind = i + 1

    return nums

# print(read_numbers("ex1_data.txt"))