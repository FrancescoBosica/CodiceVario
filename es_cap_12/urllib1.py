#utilizzo della libreria urllib per poter leggere un file txt presente su un server
#la libreria urllib tratta la pagina web come un file presente sulla memoria secondaria
#la differenza rispetto a scoket e che non fa visualizzare l'intestazione del della pagina web
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#semplice loop per la scansione del testo presente nel file
for line in fhand:
	print(line.decode().strip())