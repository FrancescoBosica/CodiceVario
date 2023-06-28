orario = {}
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From"):
        if "From:" not in line:
            line = line.split()
            word = line[5]
            word = word.split(":")
            hr = word[0]
            if hr not in orario:
                orario[hr] = 1
            else:
                orario[hr] += 1
lst = list()   
for key,value in orario.items():
    lst.append((key, value))
lst.sort()
for key,value in lst:
    print(key,value)