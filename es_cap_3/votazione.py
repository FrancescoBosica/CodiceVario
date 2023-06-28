punteggio=input("inserisci il punteggio: ")
punteggio = float(punteggio)
if punteggio >0.0 and punteggio < 1.0:
    if punteggio >= 0.9:
        print("A")
    elif punteggio >= 0.8:
        print("B")
    elif punteggio >= 0.7:
        print("C")
    elif punteggio >= 0.6:
        print("D")
    elif punteggio < 0.6:
        print("F")
else:
    print("punteggio sbagliato")
