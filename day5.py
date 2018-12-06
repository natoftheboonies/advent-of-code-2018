import re
from datetime import datetime, timedelta
from string import ascii_lowercase


def reduce(chars):
    x=1
    startLen = len(chars)
    if startLen < 2:
        return chars

    while True:
        #print x, chars
        if chars[x] != chars[x-1] and chars[x].lower() == chars[x-1].lower():
            #print (chars[x-1], chars[x])
            del chars[x]
            del chars[x-1]
            x-=2
        else:
            x+=1
        if x>=len(chars) or x<1:
            break
    if len(chars)<startLen:
        return reduce(chars)
    else:
        return chars
        

with open('./input5.txt') as fp:
    input = fp.read().strip()
#input = 'dabAcCaCBAcCcaDA'
#input = 'abBA'
chars = list(input)
result = reduce(chars)
print ('#1: {}'.format(len(result)))
rs = {}

for c in ascii_lowercase:
    newChars = list(chars)
    while c in newChars:
        newChars.remove(c)
    while c.upper() in newChars:
        newChars.remove(c.upper())
    rs[c]=len(reduce(newChars))
    #print(c,rs[c])
print ('#2: {} -> {}'.format(min(rs, key=rs.get), rs[min(rs, key=rs.get)]))

#print ('result', "".join(result))
