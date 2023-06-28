fname = "D:\studio\python\programmi\es_cap_9\mbox-short.txt"
lettura = open(fname)
istogramma = {}
for riga in lettura:
    if riga.startswith("From") == True:
        riga =  riga.split()
        if not "From:" in riga:
            a = riga[5].split(":")
            if not a[0] in istogramma:
                istogramma[a[0]] = 1 
            else:
                istogramma[a[0]] += 1
                
a = list()
for ora,cont in istogramma.items():
    a.append((ora,cont))
    
a.sort()

for ora,cont in a:
    print(ora,cont)