import collections

# coords are (x,y)

# sample
depth = 510
target = (10,10)

# mine
depth = 4845
target = (6,770)

mouth = (0,0)

geo = {
	mouth: 0,
	target: 0
}

cave = {
	mouth: 0,
	target: 0	
}

risk = 0

# keep expanding x range until #2 stops going down :)
for x in range(1,target[0]+50):
	geo[(x,0)] = 16807*x
	ero = (16807*x+depth)%20183
	if x <= target[0]: risk += ero%3
	cave[(x,0)] = ero%3

for y in range(1,target[1]+15):
	geo[(0,y)] = 48271*y
	ero = (48271*y+depth)%20183
	if y <= target[1]: risk += ero%3	
	cave[(0,y)] = ero%3

for x in range(1,target[0]+50):
	for y in range(1,target[1]+15):
		if (x,y) in geo.keys(): continue
		eroLeft = (geo[(x-1,y)]+depth)%20183
		eroUp = (geo[x,y-1]+depth)%20183
		geo[(x,y)] = eroLeft*eroUp
		ero = (eroLeft*eroUp+depth)%20183
		if x <= target[0] and y <= target[1]: risk += ero%3
		cave[(x,y)] = ero%3

#erosion = (geo+depth)%20183

print("#1:",risk)
# wrong: 5401


# rocky, wet, narrow = 0,1,2
# rocky: gear or torch
# wet: gear or none
# narrow: torch or none

nodes = []
distances = {}
for region in cave.keys():
	x, y = region
	if cave[region] == 0: # rocky
		nodes.append(tuple((x, y, 'gear')))
		nodes.append(tuple((x, y, 'torch')))
		distances[(x,y,'gear')] = {
			(x,y,'torch'):7
		}
		distances[(x,y,'torch')] = {
			(x,y,'gear'):7
		}
		for x2, y2 in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
			if (x2,y2) in cave.keys() and cave[(x2,y2)]==0: # rocky->rocky
				distances[(x,y,'gear')][(x2,y2,'gear')] = 1
				distances[(x,y,'torch')][(x2,y2,'torch')] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==1: # rocky -> wet
				distances[(x,y,'gear')][(x2,y2,'gear')] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==2: # rocky -> narrow
				distances[(x,y,'torch')][(x2,y2,'torch')] = 1
	elif cave[region] == 1: # wet
		nodes.append(tuple((x, y, 'gear')))
		nodes.append(tuple((x, y, None)))
		distances[(x,y,'gear')] = {
			(x,y,None):7
		}
		distances[(x,y,None)] = {
			(x,y,'gear'):7
		}
		for x2, y2 in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
			if (x2,y2) in cave.keys() and cave[(x2,y2)]==1: # wet->wet
				distances[(x,y,'gear')][(x2,y2,'gear')] = 1
				distances[(x,y,None)][(x2,y2,None)] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==0: # wet -> rocky
				distances[(x,y,'gear')][(x2,y2,'gear')] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==2: # wet -> narrow
				distances[(x,y,None)][(x2,y2,None)] = 1				 
	elif cave[region] == 2: # narrow
		nodes.append(tuple((x, y, 'torch')))
		nodes.append(tuple((x, y, None)))
		distances[(x,y,'torch')] = {
			(x,y,None):7
		}
		distances[(x,y,None)] = {
			(x,y,'torch'):7
		}
		for x2, y2 in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
			if (x2,y2) in cave.keys() and cave[(x2,y2)]==2: # narrow->narrow
				distances[(x,y,'torch')][(x2,y2,'torch')] = 1
				distances[(x,y,None)][(x2,y2,None)] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==0: # narrow -> rocky
				distances[(x,y,'torch')][(x2,y2,'torch')] = 1
			elif (x2,y2) in cave.keys() and cave[(x2,y2)]==1: # narrow -> wet
				distances[(x,y,None)][(x2,y2,None)] = 1	

for reg in distances.keys():
	for reg2 in distances[reg]:
		if reg2 not in distances.keys():
			distances[reg2] = {
				reg: distances[reg][reg2]
			}
		elif reg not in distances[reg2].keys():
			distances[reg2][reg] = distances[reg][reg2]



#print (nodes)		
#nodes = ero.keys()
#distances = {}


#nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
#distances = {
#    'B': {'A': 5, 'D': 1, 'G': 2},
#    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
#    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
#    'G': {'B': 2, 'D': 1, 'C': 2},
#    'C': {'G': 2, 'E': 1, 'F': 16},
#    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
#    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = (0,0,'torch')
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print("#2:",visited[(target[0],target[1],'torch')])
