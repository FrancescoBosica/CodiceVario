#Scrivi un programma che analizzi un log di posta, crei un istogramma
#utilizzando un dizionario per contare quanti messaggi sono arrivati da ciascun
#indirizzo di posta elettronica ed infine visualizzi il dizionario.
fname = "D:\studio\python\programmi\es_cap_9\mbox-short.txt"
lettura = open(fname)
istogramma = {}
for riga in lettura:
    if riga.startswith("From") == True:
        riga =  riga.split()
        if not "From:" in riga:
            if not riga[1] in istogramma:
                istogramma[riga[1]] = 1 
            else:
                istogramma[riga[1]] += 1
print(istogramma)
print("l'indirizzo:",max(istogramma),"ha inviato più e-mail di tutti.")#codice dell'esercizio 4