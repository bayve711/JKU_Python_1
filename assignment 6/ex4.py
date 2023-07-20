import os
def chunks(path: str, size: int, **kwargs):
    if os.path.isfile(path) is True:
        if size < 1:
            raise ValueError
        handle = open(path, "r")
        str_joined = ""
        for line in handle:
            res = line.replace("\n", "\*")
            str_joined+= res
        count = 0
        for i in range(len(str(str_joined))):
            if i % 25 == 0 and not i == 0:
                yield "b'"+(str_joined[count*25:i].replace("\*", "\\r\\n"))+"'"
                count += 1
            if i % 25 > 0 and i == len(str_joined)-1:
                yield "b'"+str_joined[count*25:].replace("\*", "\\r\\n")+"'"



    else:
        raise ValueError

for i, c in enumerate(chunks("ex1_data.txt", 25, mode = "rb")):
    print(f"Chunk {i} = {c}")




