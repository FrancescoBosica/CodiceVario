fname = "D:\studio\python\programmi\es_cap_7\mbox.txt"
lettura = open(fname)
istogramma={}
for riga in lettura:
    if riga.startswith("From") == True:
        riga =  riga.split()
        if not "From:" in riga:
            if not riga[1] in istogramma:
                istogramma[riga[1]] = 1 
            else:
                istogramma[riga[1]] += 1

a = list()
for key,value in istogramma.items():
    a.append((value,key))
a.sort(reverse = True)
x,y= max(a)
print(y,x)