file = open("E-Sys_20230209_162559.log" , "r")

# file.seek(19)
print(file.tell())
print(file.readline())
print(file.tell())

print(file.readline())
print(file.tell())

file.close()