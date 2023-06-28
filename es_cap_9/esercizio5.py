#Scrivi uno script che registri il nome di dominio (anziché l’indirizzo)
#da cui è stato inviato il messaggio anziché il mittente (ovvero, l’intero indirizzo
#email). Alla fine fai in modo che il programma visualizzi i contenuti del dizionario
fname = "D:\studio\python\programmi\es_cap_9\mbox-short.txt"
lettura = open(fname)
istogramma = {}
for riga in lettura:
    if riga.startswith("From") == True:
        riga =  riga.split()
        a = riga[1].split("@")
        if not "From:" in riga:
            if not a[1] in istogramma:
                istogramma[a[1]] = 1 
            else:
                istogramma[a[1]] += 1

print(istogramma)