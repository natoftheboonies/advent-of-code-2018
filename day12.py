import re



food = []
state = []
offset = []
with open('./input12.txt') as fp:
	line = fp.readline()[15:].strip()
	print (line)
	state.append(list(map(lambda x:1 if x=="#" else 0,list(line))))
	offset.append(0)
	line = fp.readline().strip()
	line = fp.readline().strip()	
	while line:
		if line[-1]=="#":
			i = list(map(lambda x:'1' if x=="#" else '0',list(line[:5])))
			food.append(int(''.join(i),2))
		line = fp.readline().strip()
#state.append([1,2,3,4,5])


for loop in range(1,121):
	prev = loop-1
	curr = []
	#print("effective left",effLeft)
	# check -1
	head = int(''.join(list(map(str,state[prev][0:1]))),2)
	head2 = int(''.join(list(map(str,state[prev][0:2]))),2)
	if head in food:
		curr.append(1)
		if head2 in food:
			curr.append(1)
		else:
			curr.append(0)
		offset.append(offset[loop-1]+2)
	elif head2 in food:
		curr.append(1)
		offset.append(offset[loop-1]+1)
	else:
		offset.append(offset[loop-1])

	#for x in range(len(left[]))
	for x in range(len(state[prev])):
		prior = ''
		if x == 0:
			prior = state[prev][0:3]
		elif x == 1:
			prior = state[prev][0:4]
		elif x==len(state[prev])-2:
			prior = state[prev][x-2:]+[0]
		elif x==len(state[prev])-1:
			prior = state[prev][x-2:]+[0,0]
		else:
			prior = state[prev][x-2:x+3]
		if int(''.join(list(map(str,prior))),2) in food:
			curr.append(1)
		else:
			curr.append(0)
	# add to the right side
	tail = int(''.join(list(map(str,state[prev][-2:]+[0,0,0]))),2)
	tail2 = int(''.join(list(map(str,state[prev][-1:]+[0,0,0,0]))),2) 
	if tail2 in food:
		if tail in food:
			curr+=[1,1]
		else:
			curr+=[0,1]
	elif tail in food:
		curr+=[1]
	print ("{}:".format(loop),''.join(list(map(lambda x:'#' if x==1 else '.',curr))), len(curr), offset[loop])
	state.append(curr)
	

for j in range(0,21):
	sum = 0	
	gen = state[j]
	for i in range(len(gen)):
		if gen[i] == 1:

			sum+=(i-offset[j])
	#print (j, sum)

print ("#1: {}".format(sum))

# 2, look for a pattern
# aha, beginning 120 just shifting to the right.

target = 50000000000

for j in range(120,121):
	sum = 0	
	gen = state[j]
	adjust = target-j
	for i in range(len(gen)):
		if gen[i] == 1:
			sum+=(adjust+i-offset[j])
	print ("#2: ", sum)

