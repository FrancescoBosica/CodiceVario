#lettura di un file plain text risiedente su un server
#creazione di comunicazione simile al web-browser
import socket

#modifca del programma(es1)
url=input("Inserisci URL: ")
host = url.split("/")
host = host[2]

#-----------------------------------------------------------------
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#mysock.connect(('data.pr4e.org',80))

#modifica del programma(es1)
mysock.connect((host,80))
cmd = 'GET ' 
cmd = cmd + url
cmd = cmd +' HTTP/1.0\r\n\r\n'
CMD = cmd.encode()
#---------------------------------------------------------------------

#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#modifica del programma(es1)
mysock.send(CMD)

#----------------------------------------------------------
#modifica del programma(es2)
conteggio=0
#-------------------------------------------------------
while True:
	data = mysock.recv(5120) #ricezione dei dati in blocchi di 512 caratteri
	if len(data) < 1:#se recv restituisce una stringa vuota vuol dire che non c'è più nienete da leggere
		break 
	#modifica del programma(es2)
	conteggio = conteggio +len(data)
	if conteggio == 3000:
		break
	#-----------------------------------------
	print(data.decode(),end='')

#modifica del programma(es2)
print(conteggio)
#----------------------------
mysock.close()