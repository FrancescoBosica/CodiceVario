#Riscrivi lo script del capitolo precedente creando una funzione chiamata computegrade che accetta un punteggio come parametro 
# e restituisce un voto sotto forma di stringa.
def computegrade(punteggio):
    if punteggio > 0.0 and punteggio<= 1.0:
        if punteggio >= 0.9:
            grade= "A"
        elif punteggio >= 0.8:
            grade = "B"
        elif punteggio >= 0.7:
            grade = "C"
        elif punteggio >= 0.6:
            grade = "D"
        else:
            grade = "F"
    else:
        return "range di valutazione sbagliata"
    return grade
#main
punteggio = input("insrisci il punteggio: ")
punteggio = float(punteggio)
print(computegrade(punteggio))