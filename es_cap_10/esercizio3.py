import string
string.punctuation
leggi = "D:\Documenti\studio\python\programmi\es_cap_9\words.txt"
fname = open(leggi)
f = {}
print(type(f))
for word in fname:
    word = word.translate(word.maketrans("","",string.punctuation))
    word = word.lower()
    a = word.split()
    for i in range(len(a)):
        b = a[i]
        for j in b:
            if not j in f:
                f[j] = 1
            else:
                f[j] +=1

n = list()

for key,value in f.items():
    n.append((value,key))

n.sort(reverse=True)

for x,y in n:
    print(y,x)