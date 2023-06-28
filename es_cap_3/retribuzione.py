ore = input("inserisci le ore di lavoro: ")
paga = input("inserisci la paga: ")
try: 
    ore=int(ore)
    paga=float(paga)
except:
    print("non puoi inserire delle parole, devi inserire solo numeri")
    quit()
pagamento = ore * paga
if ore > 40 :
    pagamento += (ore - 40) * (paga * 0.5) 
print("pagamento:",pagamento)