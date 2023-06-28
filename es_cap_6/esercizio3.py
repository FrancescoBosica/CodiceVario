def count (parola,carattere):
    count = 0
    for index in parola:
        if index == carattere:
            count+= 1
    return count
#main
word = input("inserici la parola da controllare: ")
char = input("inserisci il carattere da con frontare: ")
x = count(word,char)
print(x)