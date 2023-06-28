totale = 0
conteggio = 0
media = 0
valore = None
while True :
    valore = input("inserisci il numero: ")
    try:
        if valore != "done" :
            valore = int(valore)
            totale = totale + valore
            conteggio = conteggio + 1
            media = totale / conteggio    
        if valore == "done" :
            break
    except:
        print("input errato")
print(totale, conteggio,media)