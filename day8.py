from string import ascii_uppercase
import re

sample = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
d = []
with open('./input8.txt') as fp:
	sample = fp.read().strip()

input = list(map(int,sample.split()))
input.append(1)

#print (input)

def child(i, c0, m0):
	chx = 0
	chx2 = 0
	#print ("eval {},{} children".format(c0,m0))
	mt = {}
	for k in range(c0):
		c = input[i]
		m = input[i+1]
		i += 2		
		i, qq, qq2 = child(i, c, m)	
		mt[k] = qq2
		chx += qq
		#print("qq2",qq2)
	#print("eval {},{} metadata at {}:".format(c0,m0, i),input[i:i+m0])	
	chx+=sum(input[i:i+m0])
	if c0 == 0:
		chx2 += sum(input[i:i+m0])
		print("sum",chx2)
	else:
		print ("mt:",mt)
		for f in input[i:i+m0]:
			print("look for child",f)
			if f-1 in mt.keys():
				chx2+=mt[f-1]
				print("found child:",f)	
			else:
				print("not found", f)		
	i+=m0
	return (i, chx, chx2)		

i, chx, chx2 = child(0,1,1)

print("#1: {}".format(chx))
print("#2: {}".format(chx2))

	




#print ("read: {}".format((inst)))

