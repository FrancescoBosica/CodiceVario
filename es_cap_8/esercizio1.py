def chop(t):
    del t[0]
    del t[len(t)-1]
    return None
def middle(t):
    chop(t)
    a = t
    return a
#main
t = ['a','b','c','d','e']
print(middle(t))