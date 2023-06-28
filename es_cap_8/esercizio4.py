filename = "D:/studio/python/programmi/es_cap_8/romeo.txt"
paragrafo = open(filename)
elenco = [ ]
#Scrivi un programma che lo apra e 
# lo legga riga per riga. 
# Dividi la riga in un elenco
#di parole usando la funzione split.
for riga in paragrafo:
    
    riga = riga.strip()
    word = riga.split()
    #Controlla se ogni parola 
    # è già presente in un elenco.
    #Se la parola non è nell’elenco,
    #aggiungila. 
    for x in range(len(word)):
        if not word[x] in elenco:
            elenco.append(word[x])    
#ordina e visualizza in ordine alfabetico le
#parole risultanti.
elenco.sort()
print(elenco)