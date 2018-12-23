import re

nanobot = []
king = None

with open('input23.txt') as fp:
	line = fp.readline().strip()
	while line:
		x = list(map(int,re.findall('(-?\d+)', line)))
		nanobot.append((tuple(x[:3]), x[3]))
		if not king or x[3]>king[1]:
			king = (tuple(x[:3]), x[3])
		line = fp.readline().strip()

#print(nanobot)
print(king)

count = 0
for bot in nanobot:
	#if bot == king: continue
	dist = abs(bot[0][0]-king[0][0])+abs(bot[0][1]-king[0][1])+abs(bot[0][2]-king[0][2])
	if dist <= king[1]: count += 1

print("#1:", count)

print(len(nanobot))

stats = []

for i in range(3):
	stats.append(("xyz"[i], 
		min(x[0][i] for x in nanobot), 
		sum(x[0][i] for x in nanobot)//len(nanobot), 
		max(x[0][i] for x in nanobot),  
		max(x[0][i] for x in nanobot)-min(x[0][i] 
			for x in nanobot)))
# axis, min, avg, max, range
print(stats)
ranges = stats

# x is biggest
step = 416757602
last = (0, (0,0,0))

# best (161, (15799263, -575999, 5048066)) 104189400
#step//=4
#best (683, (-10248087, 25471351, 31095416)) 26047350
#step//=2
# best (773, (15799263, 25471351, 18071741)) 13023675
#step//=2
# best (865, (15799247, 18959504, 18071732)) 6511837
#step//=2
#best (865, (15799215, 18959485, 18071714)) 3255918
#step//=2
#best (880, (17427174, 18959485, 16443755)) 1627959
#step//=2
#best (882, (17427173, 18959484, 15629775)) 813979
#step//=2
#best (882, (17020183, 18959483, 15629774)) 406989

# this is dumb:
# best (899, (16890988, 18959484, 15578902)) 3

#last = (882, (17427173, 18959484, 15629775))

while step > 1:
	ranges = (('x',last[1][0]-step,0,last[1][0]+step),
		('y',last[1][1]-step,0,last[1][1]+step),
		('z',last[1][2]-step,0,last[1][2]+step))
	step//=2
	best = None
	#print(range(ranges[0][1], ranges[0][3]+1, step))
	for x in range(ranges[0][1]-1, ranges[0][3]+1, step):
		for y in range(ranges[1][1]-1, ranges[1][3]+1, step):
			for z in range(ranges[2][1]-1, ranges[2][3]+1, step):
				count = 0
				for bot in nanobot:
					dist = abs(bot[0][0]-x)+abs(bot[0][1]-y)+abs(bot[0][2]-z)
					if dist <= bot[1]: count += 1			
				#print((x,y,z),count)
				if not best or best[0] < count:
					best = (count, (x,y,z))
	print("best", best, step)
	last = best


print("#2:",sum(best[1]))
#not 53505228
