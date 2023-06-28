leggi = "D:\studio\python\programmi\es_cap_9\words.txt"
lettura = open(leggi)
words = {}
x = 0
for riga in lettura:
    a = riga.split()
    a = str(a)
    words[a] = x
    x = x + 1
lettura = open(leggi)
for riga in lettura:
    a = riga.split()
    a = str(a)
    print(riga)
    if a in words:
        print("la parola:", a, "è presente")