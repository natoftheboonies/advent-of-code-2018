import re
from collections import deque

def printdirt(dirt):
	seq='0123456789'
	width = len(dirt[0])+4
	h = ''
	for j in range(len(dirt[0])):
		h += seq[j%10]
	k = ''
	for i in range(10,len(dirt[0])):
		k += seq[i//10%10]
	m = ''
	for n in range(100,len(dirt[0])):
		m += seq[n//100%10]
	print(m.rjust(width))
	print(k.rjust(width))	
	print(h.rjust(width))		
	l = 0
	for row in dirt:
		print("{:>3} {}".format(l, ''.join(row)))
		l+=1
	print


def flow(dirt,y,x):
	# https://stackoverflow.com/questions/47896461/get-shortest-path-to-a-cell-in-a-2d-array-python
	queue = deque([[(x,y)]])
	seen = set([(x,y)])
	while queue:
		path = queue.popleft()
		#print path
		x, y = path[-1]
		# flowing order: down, then left, right
		#print "cond",x,y
		if (y+1)<len(dirt) and dirt[y+1][x] in '.|':
			#print "if",x,y
			queue.append(path+[(x,y+1)])
			seen.add((x,y+1))
		elif (y+1)<len(dirt):
			# left/right
			#print "else",x,y
			for x2, y2 in [(x-1,y), (x+1,y)]:
				if 0 <= x2 < len(dirt[y]) and 0 <= y2 < len(dirt) and dirt[y2][x2] in '.|' and (x2,y2) not in seen:
					queue.append(path+[(x2,y2)])
					seen.add((x2,y2))
	return seen	


clay = []

with open('./input17.txt') as fp:
	line = fp.readline().strip()
	while line:
		x = map(int, re.split(r'\.\.',re.search(r'x=(\d+(\.\.)?\d*)', line).group(1)))
		if len(x) == 1:
			x.append(x[0])
		y = map(int, re.split(r'\.\.',re.search(r'y=(\d+(\.\.)?\d*)', line).group(1)))
		if len(y) == 1: 
			y.append(y[0])
		clay.append((y, x))
		line = fp.readline().strip()


print("y range: {}..{}").format(min(y[0][0] for y in clay), max(y[0][1] for y in clay))
print("x range: {}..{}").format(min(x[1][0] for x in clay), max(x[1][1] for x in clay))

# y = 3 .. 1903
# x = 368 .. 623

# sample y = 1..13, x = 495..506
#offset = 495-1
#height = 14
#width = 506-offset+2 

# input y = 3..1903, x = 368..623
offset = 368-1
height = 1904
width = 623-offset+2

dirt = [['.'] * (width) for _ in range(height)]
dirt[0][500-offset] = '+'

for yline, xline in clay:
	#print yline, xline
	for y in range(yline[0],yline[1]+1):
		for x in range(xline[0]-offset,xline[1]-offset+1):
			dirt[y][x]='#'

#printdirt(dirt)

#printdirt(dirt)

for _ in range(1000):
	y,x = 1,500-offset
	for coord in flow(dirt,y,x):
		x, y = coord
		dirt[y][x] = '|'
	# flow to water
	for y in range(len(dirt)):
		for x in range(len(dirt[y])):
			if dirt[y][x]=='|':
				if y < len(dirt)-1 and dirt[y+1][x] in '#~' and dirt[y][x-1] in '#~':
					settle = False
					for x2 in range(x,len(dirt[y])):
						if dirt[y+1][x2] in '.|':
							break
						if dirt[y][x2+1] in '~#':
							settle = True
							break
					#print settle,x,x2
					if settle:
						for s in range(x,x2+1):
							dirt[y][s]='~'


#printdirt(dirt)
f = open("day17out.txt", "w")
for row in dirt:
   f.write(''.join(row) + '\n')

count = 0
count2 = 0
for row in dirt[3:]:
	for x in range(len(row)):
		if row[x] == '~':
			count+=1
		if row[x] == '|':
			count2+=1

print("#1: {}".format(count+count2))
print("#2: {}".format(count))


