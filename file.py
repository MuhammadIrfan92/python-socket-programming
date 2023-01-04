def readfile(path):
    with open(path, 'r') as  file:
        data = file.readlines()
    return data

data = readfile('file1.txt')
for i in data:
    print(i)


print(type(data))
print(len(data))