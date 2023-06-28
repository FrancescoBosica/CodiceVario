filename=input("inserisci il nome del file: ")
media = 0
number = 0
conteggio =0
try:
    filed = "D:/Documenti/studio/python/programmi/es_cap_7/"+ filename
    fileo= open(filed)
except:
    print("Nome del file non corretto o file inesistente")
    quit()
conteggio=0
for line in fileo:
    if line.startswith("X-DSPAM-Confidence: **0.8475**"):
        number = line[22:28]
        number = float(number)
        conteggio += 1
    media = number / conteggio

print(media)
        