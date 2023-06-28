str = 'X-DSPAM-Confidence:0.8475'
primaparte = str.find(':')
newstr = str[primaparte+1:]
print(float(newstr))