import urllib, urllib.error,urllib.request,urllib.response

url = input("insersci l'indirzzo web: ")

fhand = urllib.request.urlopen(url)
conteggio = 0 
for a in fhand:
    s = a.decode().rstrip()
    print(s)
    for i in range(len(s)):
        for a in s[i].split():
            conteggio = conteggio+1
            if conteggio == 3000:
                quit()
    