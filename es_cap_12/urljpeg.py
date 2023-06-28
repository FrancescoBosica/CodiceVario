#simulazione di un web-browser per conneterci ad un server 
# e scaricare una immagine
import socket
import time

HOST =  'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((HOST,PORT)) #i dati rigardanti la connessione sono stati salvate nelle variabili e inserite come parametri attuali
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
	data = mysock.recv(5120) #usato per ricevere dati
	if len(data) < 1:break
	time.sleep(0.25)#rallenta la connessione in modo che priva alla prosima chiamata di reciv si può ricevere più dati dal server
	print(len(data),count)
	picture += data
mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length',pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
fhand =  open("stuff.jpg","wb")
fhand.write(picture)
fhand.close()