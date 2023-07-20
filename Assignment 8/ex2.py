import math
import os
class Reader:
    def __init__(self, path: str):
        self.path = path
        if os.path.isfile(path) is True:
            self.handle = open(path, "rb")
        else:
            raise ValueError
    def close(self):
        self.handle.close()
    def __len__(self):
        file_size = os.stat(self.path)    #alternative - return os.path.getsize(self.path)
        return file_size.st_size
    def __getitem__(self, key):
        if isinstance(key, int):
            if key >= 0 and key < Reader.__len__(self):
                self.handle.seek(key)                    #sets the file's current position at the offset
                return self.handle.read(1)               #seek relative to the current position
            elif key < 0 and key >= -(Reader.__len__(self)):
                key += Reader.__len__(self)
                self.handle.seek(key)
                return self.handle.read(1)
            else:
                raise IndexError("Reader index out of range")
        else:
            raise TypeError(f"indexing expects 'int', not '{type(key).__name__}'")


# r    =    Reader("ex2_data.txt")
# print(r[0])
# print(r[1])
# print(r[-1])
# try:
#     r["hi"]
# except    TypeError    as    e:
#     print(f"{type(e).__name__}: {e}")
# try:
#     r[100]
# except    IndexError    as    e:
#     print(f"{type(e).__name__}: {e}")