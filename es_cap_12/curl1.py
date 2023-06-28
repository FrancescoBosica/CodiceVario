import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('https://i.ytimg.com/vi/HeBY-4RjtZ0/hqdefault.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()