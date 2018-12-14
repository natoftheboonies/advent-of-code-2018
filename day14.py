
r = [3,7,1,0]
e = [0,1]

n = 380621
nseq = map(int,list(str(n)))

i = 0
while True:
	i+=1
	new = r[e[0]]+r[e[1]]
	r+=map(int,list(str(new)))
	if len(r) > n+10 and len(r) < n+12:
		print ("#1: {}".format(''.join(list(map(str,r[n:n+10])))))
	if r[i:i+len(nseq)] == nseq:
		print ("#2: {}".format(i))
		break
	e1 = e[0]+r[e[0]]+1
	e2 = e[1]+r[e[1]]+1
	e[0]=e1%len(r)
	e[1]=e2%len(r)
	#print r, e
n = 5
print r[n:n+10]
n = 18
print r[n:n+10]
n = 2018
print r[n:n+10]

