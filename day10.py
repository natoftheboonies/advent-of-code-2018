import re

def distance(sky, time):
	distance = 0
	for x in sky:
		xTime = (x[0][0]+x[1][0]*time, x[0][1]+x[1][1]*time)
		#print xTime
		for y in sky:
			yTime = (y[0][0]+y[1][0]*time, y[0][1]+y[1][1]*time)
			#print yTime
			distance += (abs(xTime[0]-yTime[0])+abs(xTime[1]-yTime[1]))
	return distance


def printSky(sky, time):
	for x in sky:
		x[0][0] = x[0][0]+x[1][0]*time
		x[0][1] = x[0][1]+x[1][1]*time
	toPlot = [x[0] for x in sky]
	minX = min(x[0] for x in toPlot)
	minY = min(x[1] for x in toPlot)
	maxX = max(x[0] for x in toPlot)
	maxY = max(x[1] for x in toPlot)

	grid = [['.'] * (maxX-minX+1) for _ in range(maxY-minY+1)]

	for p in toPlot:
		#print "plot", p, "at", p[0]-minX, p[1]-minY
		grid[p[1]-minY][p[0]-minX] = '#'
	for r in grid:
		print (' '.join(r))
	#print "mins",minX,minY
	#print "max", maxX, maxY


d = []
with open('./input10.txt') as fp:
	line = fp.readline().strip()
	while line:
		x = list(map(int,re.findall('(-?\d+)', line)))
		d.append((x[:2],tuple(x[2:])))
		line = fp.readline().strip()

#print d

# smallest dist for input at 
# determined manually by adjusting range & step :)
lastDist = distance(d,0)
time = 0
for time in range(10390,10395, 1):
	dist =  distance(d,time)
	if dist < lastDist:
		lastDist = dist
	else:
		break

print("#1: ")
printSky(d, time-1)

print("#2: {}".format(time-1))



