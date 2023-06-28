fname = "D:\studio\python\programmi\es_cap_9\mbox-short.txt"
lettura = open(fname)
x = 0
giornicont = dict()
for riga in lettura:
   if riga.startswith("From") == True:
       if not 'From:' in riga:
        riga = riga.split()
        key = str(riga[2])
        if not key in giornicont:
            giornicont[key] = 1
        else:
            giornicont[key] += 1
        
        
        
print(giornicont)        