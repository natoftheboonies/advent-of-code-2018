from string import ascii_lowercase

def flatten(seq, idx):
	max = 0
  	for el in seq:
		if max < int(el[idx]):
			max = int(el[idx])
	return max

names=ascii_lowercase
labels = list(names)+[x+'2' for x in list(names)]

inst = []
with open('./input6.txt') as fp:
	line = fp.readline().strip()
	while line:
		inst.append(map(int,line.split(',')))
		line = fp.readline().strip()
print ("size: {}".format(len(inst)))
gridsize = [flatten(inst, 0), flatten(inst, 1)]
print ("grid: {}".format(gridsize))

fabric = [[0]*(gridsize[0]+2) for i in range(gridsize[1]+1)]  

#print inst

# plot the points
for i in inst:
	#print ("plotting ",i)
	index = inst.index(i)
	#print index
	fabric[i[1]][i[0]]=labels[index].upper()


# fill the rest of the grid
for r in xrange(len(fabric)):
	for c in xrange(len(fabric[r])):
	  	if fabric[r][c]==0:
	  		closest = None
	  		cdist = 999
	  		for i in inst:
	  			dist = abs(r-i[1])+abs(c-i[0])	  			
	  			if dist < cdist:
	  				closest = i
	  				cdist = dist
	  		dupe = 0
	  		for i in inst:
	  			dist = abs(r-i[1])+abs(c-i[0])
	  			if cdist == dist:
	  				dupe += 1
	  		if dupe < 2:
	  			fabric[r][c] = labels[inst.index(closest)]
	  		else:
	  			fabric[r][c] = "."

# exclude infinites
vitem = list(inst)
for i in inst:
	search = labels[inst.index(i)]
	for r in range(len(fabric)):
		if fabric[r][0].lower() == search or fabric[r][len(fabric[r])-1].lower() == search:
			vitem.remove(i)
			print("{} is infinite".format(search.upper()))
			break

# calc area
maxarea = 0
maxindex = None
for i in vitem:
	area = 0
	search = labels[inst.index(i)]
	for r in xrange(len(fabric)):
		for c in xrange(len(fabric[r])):
			if fabric[r][c].lower() == search:
				area += 1
	#print("{} area is {}".format(search, area))
	if area > maxarea:
		maxarea = area
		maxindex = search
print("#1: index {} has area {}".format(maxindex,maxarea))

#part 2

regionSize = 0
for r in xrange(len(fabric)):
	for c in xrange(len(fabric[r])):
		totalDist = 0
		for i in inst:
			dist = abs(r-i[1])+abs(c-i[0])
			totalDist += dist
		if totalDist < 10000:
			regionSize += 1
print("#2: {}".format(regionSize))

#for x in fabric:
	#print('\t'.join(map(str, x)))  