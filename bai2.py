
f = open("files.txt", "r")
file = tuple(f)
print(file[-10:-1])
f.close()
