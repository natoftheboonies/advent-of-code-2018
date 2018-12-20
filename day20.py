
sample1 = "^WNE$"
sample2 = "^ENWWW(NEEE|SSE(EE|N))$"
sample3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
sample4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
sample5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

with open('input20.txt') as fp:
	input = fp.readline().strip()

#input = sample5

#print len(input),input

pos = lastpos = (0,0)
#visited = [pos]
paths = {pos:[]}
options = []

for x in input[1:-1]:
	lastpos = pos
	if x in 'NSEW':
		if x == 'N':
			pos = (pos[0],pos[1]-1)
		elif x == 'S':
			pos = (pos[0],pos[1]+1)
		elif x == 'E':
			pos = (pos[0]+1,pos[1])
		elif x == 'W':
			pos = (pos[0]-1,pos[1])
		#visited.append(pos)
		nextpath = paths[lastpos]+[pos]
		# if longer path, ignore
		if pos in paths and len(nextpath) > len(paths[pos]):
			continue
		else: paths[pos] = nextpath
	elif x == '(':
		options.append(pos)
	elif x == ')':
		options.pop()
	elif x == '|':
		# resume from prior option
		pos = options[-1]
	else:
		print "where am i?",x

#print visited
#print paths
#for x in paths.keys():
#	print x, paths[x]

maxpath = 0
count1000 = 0
for path in paths.values():
	if len(path)>=1000:
		count1000+=1
	if len(path)>maxpath:
		maxpath = len(path)

print "#1:",maxpath
print "#2:",count1000