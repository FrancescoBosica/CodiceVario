parola = input("inserisci la parola: ")
index = len(parola)
print(parola)
while index > 0:
    index = index - 1
    lettera = parola[index]
    print("lettera in posizione:",index,lettera)
