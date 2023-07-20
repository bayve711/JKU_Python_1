def write_dict(d: dict, path: str, encoding: str = "utf-8"):
    handle = open(path, "w")
    for key, value in d.items():
        handle.write(str(key) + " " + str(value) + "\n")

def read_dict(path: str, encoding: str = "utf-8") -> dict:
    handle1 = open(path, "r")
    dict_new = dict()
    for line in handle1:
        our_list = str(line).split()
        try:
            dict_new.update({our_list[0]: int(our_list[1])})
        except:
            try:
                dict_new.update({our_list[0]: float(our_list[1])})
            except:
                dict_new.update({our_list[0]: str(our_list[1])})

    return dict_new


# txt_ex2 = "ex2_data.txt"
# dict_ex2 = {"key": 7, "value": 18}
# write_dict(dict_ex2, "ex2_data.txt")
# print(read_dict(txt_ex2))
# new_dict = read_dict(txt_ex2)
# if (dict_ex2 == new_dict):
#     print("True")