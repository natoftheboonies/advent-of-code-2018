from string import ascii_uppercase
import re

d = []
with open('./input7.txt') as fp:
	line = fp.readline().strip()
	while line:
		d.append(re.findall('[Ss]tep ([A-Z])',line))
		line = fp.readline().strip()
#print ("read: {}".format((inst)))

# find unblocked
seq = ''
inst = list(d)
while True:
	c = []
	for x in inst:
		if x[0] not in [b[1] for b in inst]:
			 c.append(x[0])
	seq += min(c)
	if len(inst)==1:
		seq += inst[0][1]
	inst = [x for x in inst if x[0] != min(c)]
	if not inst:
		break
print("#1: {}".format(seq))

#2
inst = list(d)
seq = ''
worker = [['', 0] for _ in range(5)]
#print worker
# worker[1] = ['A',3]
time = 0
while True:
	time += 1
	print( "time {} assignments: {}".format(time,[w[0] for w in worker]))

	c = []
	# workers be workin'

	for w in worker:
		if w[0] and w[1]>0:
			w[1]-=1
			if w[1]==0:
				print ("worker {} finished {}".format(worker.index(w),w[0]))
				seq += w[0]
				# unlock last job
				if len(inst)==1:
					print ("takes last job {}".format(inst[0][1]))
					w[0] = inst[0][1]
					w[1] = ascii_uppercase.index(inst[0][1])+1+60
					inst.remove(inst[0])
				else:
					inst = [x for x in inst if x[0] != w[0]]
					w[0] = ''
				

	# is everyone busy?
	if all(w[0]!='' for w in worker):
		print("all {} workers busy".format(len(worker)))
		continue
	
	# find jobs	
	
	for x in inst:
		if x[0] not in [b[1] for b in inst]:
			 if x[0] not in [w[0] for w in worker]:
			 	c.append(x[0])

	c = set(c)
	#assign jobs:
	#print("avail: {}".format(c))
	for w in worker:
 		if w[0] == '':
 			if not c:
 				break
 			w[0] = min(c)
 			w[1] = ascii_uppercase.index(min(c))+1+60
 			print("assigned {} to w{} for {} sec".format(w[0],worker.index(w),w[1]))
 			c = [v for v in c if v != w[0]]

	#inst = [x for x in inst if x[0] not in [w[0] for w in worker]]
	if not inst and all(w[0] == '' for w in worker):
		break
print("#2: {}, {}".format(time-1, seq))



