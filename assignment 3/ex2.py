fnames = ["file7.txt", "file1.png", "file3.txt", "file2.txt",
          "file7.txt", "file1.txt", "file3.txt", "file4.png",
          "file4.png", "file5.txt", "file0.txt", "file7.dat"]
new_list = []
for file in fnames:
    if file.endswith("txt"):
        if file not in new_list:
            new_list.append(file)
new_list.sort()
print(new_list)
