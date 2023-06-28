posta = "D:\studio\python\programmi\es_cap_8\mbox-short.txt"
lettura = open(posta)
conta = 0
for riga in lettura:
    if riga.startswith('From') == True:
        if not 'From:' in riga:
            dividi = riga.split()
            print(dividi[1])
            conta = conta + 1

print("All'interno del file ci sono ", conta, " righe che iniziano per From")    