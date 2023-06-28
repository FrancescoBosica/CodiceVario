elenco = []
print("per terminare il programa devi inserire la parola done")
while True:
    numero = input("inserici il numero: ")
    try:
        if numero == "done":
            break
        numero = float(numero)
        elenco.append(numero)
    except:
        print("input non valido") 
print("il numero massimo è:",max(elenco), "\nil numero minore è:", min(elenco))