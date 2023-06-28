filename=input("inserisci il nome del file: ")
try:
    filed = "D:/studio/python/programmi/es_cap_7/"+ filename
    fileo= open(filed)
except:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    print("Nome del file non corretto o file inesistente")
    quit()
conteggio=0
for line in fileo:
    conteggio += 1
print('Ci sono:',conteggio,'righe all interno del file:',filename)