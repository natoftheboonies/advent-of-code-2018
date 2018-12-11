
fuel = []

serial = 3613

for r in range(300):
	fuel.append([])
	for c in range(300):
		x, y = c+1, r+1
		f =((((x+10)*y+serial)*(x+10))//100)%10-5
		fuel[r].append(f)

coords = (0,0,0)
maxFuel = 0

for y in range(300-3):
	for x in range(300-3):
		cFuel = 0
		# sum([row[r:r+3] for row in fuel[c:c+3]])
		for row in fuel[y:y+3]:
			cFuel += sum(row[x:x+3])
		#print(cFuel)
		if cFuel > maxFuel:
			maxFuel = cFuel
			coords = (x+1, y+1)

print("#1: coords = {} fuel = {} ".format(coords, maxFuel))

coords = (0,0,0)
maxFuel = 0

# debug stuff
#r = 251-1
#c = 232-1
#
#for a in range(r,r+4):
#	print('\t'.join(list(map(str,fuel[a][c:c+4]))))
#
#cFuel = fuel[r][c]
#for s in range(1,4):
#	print ("s is",s)
#	print("add row {} cols {} to {}".format(r+s,c,c+s+1))
#	# add the next row
#	print("add",fuel[r+s][c:c+s+1])
#	cFuel+=sum(fuel[r+s][c:c+s+1])
#	print ("result",cFuel)
#	# add the next column
#	print("add column {} rows {} to {}".format(c+s, r, r+s-1))
#	for r2 in range(r,r+s):
#		print("add [{}]".format(fuel[r2][c+s]))
#		cFuel += fuel[r2][c+s] 
#	print("sum",cFuel)
#	if cFuel > maxFuel:
#		maxFuel = cFuel
#		coords = (r+1, c+1, s)


for y in range(300-30):
	for x in range(300-30):
		cFuel = fuel[y][x]
		for s in range(1,30):
			cFuel+=sum(fuel[y+s][x:x+s+1])
			for y2 in range(y,y+s):
				cFuel += fuel[y2][x+s] 
			#print(cFuel)
			if cFuel > maxFuel:
				maxFuel = cFuel
				coords = (x+1, y+1, s+1)


print("#2: coords = {} fuel = {} ".format(coords, maxFuel))


# wrong guess:  93,233,12

# serial = 57
#print (fuel[79-1][122-1])
# serial = 39
#print(fuel[196-1][217-1])
# serial = 71
#print(fuel[153-1][101-1])

