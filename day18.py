import copy
from collections import Counter

land = []

with open('input18.txt') as fp:
	line = fp.readline().strip()
	while line:
		#print line
		land.append(list(line))
		line = fp.readline().strip()


print len(land),len(land[3])

lastt = 0
lasty = 0
show = False
for m in range(1,700):
	nextland = copy.deepcopy(land)
	for y in range(len(land)):
		for x in range(len(land[y])):
			treecount = 0
			yardcount = 0
			for x2,y2 in [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x-1,y+1)]:
				if 0<=y2<len(land) and 0<=x2<len(land[y]):
					if land[y2][x2] == '|':
						treecount += 1
					elif land[y2][x2]=='#':
						yardcount += 1
			if land[y][x] == '.' and treecount >= 3:
				nextland[y][x] = '|'
			elif land[y][x] == '|' and yardcount >= 3:
				nextland[y][x] = '#'
			elif land[y][x]== '#' and (yardcount < 1 or treecount < 1):
				nextland[y][x] =  '.'

	land = nextland

#for row in land:
#	print ''.join(row) 

	treecount = sum(row.count('|') for row in land)
	yardcount = sum(row.count('#') for row in land)

	if m==10:
		print("#1: {}".format(treecount*yardcount))
	elif m==601+7:
		print("#2: {}".format(treecount*yardcount))
		break
	if show:
		print("#1", m, treecount*yardcount, treecount, yardcount, treecount-lastt, yardcount-lasty)
	if treecount == 538 and yardcount == 337:
		print "loop at",m
		#show = True
		# looping every 28 after 601
		# 601+28*35714264+7
	lastt = treecount 
	lasty = yardcount

