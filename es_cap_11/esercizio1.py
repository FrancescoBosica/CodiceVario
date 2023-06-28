import re
fname = "D:\studio\python\programmi\es_cap_7\mbox.txt"
testo = open(fname)
ricerca = input("inserisci l'espressione regolare: ")
conta = 0 
for riga in testo:
    if re.search(ricerca,riga):
        conta = conta + 1

print(" ",fname[36:],"ha",conta," linee che contengono",ricerca)