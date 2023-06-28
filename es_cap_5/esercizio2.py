maggiore = None
while True :
    valore = input("inserisci il numero: ")
    try:
        if valore != "done" :
            valore = int(valore)
            if maggiore is None or valore > maggiore :
                maggiore = valore
        if valore == "done" :
            break
    except:
        print("input errato")
print("il numero maggiore è :",maggiore)