filename = input("inserisci il nome del file: ")
try:
    fhand = open(filename)
except:
    print("nome del file non corretto o non esistente")
    quit()
for line in fhand:
    line = line.upper()
    print(line.strip())
fhand.close()
print("finito")