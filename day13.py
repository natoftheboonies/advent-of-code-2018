
def printgame(mine,carts):
	seq='0123456789'
	width = len(mine[len(mine)-1])+len(str(len(mine)))
	h = ''
	for j in range(len(mine[0])):
		h += seq[j%10]
	k = ''
	for i in range(10,len(mine[0])):
		k += seq[i//10%10]
	m = ''
	for n in range(100,len(mine[0])):
		m += seq[n//100%10]
	print m.rjust(width)	
	print k.rjust(width)	
	print h.rjust(width)
	for y in range(len(mine)):
		row = str(y)
		for x in range(len(mine[y])):
			found = False
			for c in carts:
				if not found and c[1]==(x,y):
					row+=c[0]
					found = True
					break
			if not found:
				row+=mine[y][x]
		print row.rjust(width)
	print

mine = []
with open('./input13.txt') as fp:
	line = fp.readline()
	while line:
		mine.append(list(line[:-1]))
		print len(line)
		line = fp.readline()

# cart, (x,y), turn
carts = []
for y in range(len(mine)):
	for x in range(len(mine[y])):
		if mine[y][x] in '<^>v':
			carts.append([mine[y][x],(x,y), 0])
			if mine[y][x] in '<>':
				mine[y][x] = '-'
				#print mine[y][x-1:x+2]
			elif mine[y][x] in '^v':
				mine[y][x] = '|'				
				#print mine[y-1][x]
				#print mine[y][x]
				#print mine[y+1][x]

#printgame(mine,[])

sorted(carts, key=lambda cart: cart[1][::-1])

#print("{} carts: {}".format(len(carts),carts))

printgame(mine,carts)

t=0
while True:
	t+=1
	# aaaaak, gotta sort each loop!
	carts = sorted(carts, key=lambda cart: cart[1][::-1])
	for c in carts:
		if c[0]=='X':
			continue
		# move
		if c[0] == '>':
			c[1] = (c[1][0]+1,c[1][1])
		elif c[0] == '<':
			c[1] = (c[1][0]-1,c[1][1])
		elif c[0] == '^':
			c[1] = (c[1][0],c[1][1]-1)
		elif c[0] == 'v':
			c[1] = (c[1][0],c[1][1]+1)
		else:
			print "whodat? {} ".format(c[0])
		# junction
		if mine[c[1][1]][c[1][0]]=='+':
			#left
			if c[2]==2:
				if c[0]=='>':
					c[0]='v'
				elif c[0]=='v':
					c[0]='<'
				elif c[0]=='<':
					c[0]='^'
				elif c[0]=='^':
					c[0]='>'
			if c[2]==0:
				if c[0]=='>':
					c[0]='^'
				elif c[0]=='^':
					c[0]='<'	
				elif c[0]=='<':
					c[0]='v'
				elif c[0]=='v':
					c[0]='>'
			#print "junct", c[2], (c[2]+1)%3
			c[2]=(c[2]+1)%3
		# corner
		elif mine[c[1][1]][c[1][0]] == '\\':
			if c[0]=='>':
				c[0] = 'v'
			elif c[0]=='^':
				c[0] = '<'
			elif c[0]=='<':
				c[0] = '^'
			elif c[0]=='v':
				c[0] = '>'				
			else:
				print "wha? {} for \\".format(c[0])
		elif mine[c[1][1]][c[1][0]] == '/':
			if c[0]=='<':
				c[0] = 'v'
			elif c[0]=='^':
				c[0] = '>'
			elif c[0]=='>':
				c[0] = '^'
			elif c[0]=='v':
				c[0] = '<'								
			else:
				print "wha? {} for /".format(c[0])				
		# detect crashes
		for d in carts:
			if d==c or d[0]=='X':
				continue
			elif d[1]==c[1]:
				print "crash at {} at tick {}".format(c[1], t)
				c[0] = 'X'
				d[0] = 'X'
				#printgame(mine,carts)
				break
	uncrashed = [c for c in carts if c[0] != 'X']
	if len(uncrashed)==1:
		last = uncrashed[0]
		print("last cart at {} at tick {}".format(last[1], t))
		break

