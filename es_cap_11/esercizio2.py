import re
fname = "D:\studio\python\programmi\es_cap_9\mbox-short.txt"
testo = open(fname)
a = 0
f = 0
for riga in testo:
    riga = riga.rstrip()
    if re.findall("^New Revision:",riga):
        y = re.findall("[0-9]+",riga)
        for i in range(len(y)):
            a = a + float(y[i])
        f = f+ len(y)
print(a/f)