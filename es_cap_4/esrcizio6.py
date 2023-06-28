#Riscrivi il calcolo della tua retribuzione con gli straordinari pagati il
#50% in più creando una funzione chiamata computepay che richieda i due parametri
#hours e rate.
def computepay(hours,rate):
    pagamento = hours * rate
    pagamento += (hours - 40)*((rate*50)/100)
    return pagamento
#main
print(computepay(45,10))