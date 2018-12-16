import re

def evalsample(sample):

	possible = []
	before, inst, after = sample

	# before has 4 registers
	# inst has code, A, B, C
	code, a, b, c = inst

	# addr
	result = list(before)
	result[c]=result[a]+result[b]
	if result == after:
		possible.append('addr')

	# addi
	result = list(before)
	result[c] = result[a]+b
	if result == after:
		possible.append('addi')

	# mulr
	result = list(before)
	result[c] = result[a]*result[b]
	if result == after:
		possible.append('mulr')

	# muli
	result = list(before)
	result[c] = result[a]*b
	if result == after:
		possible.append( 'muli'	)

	# banr
	result = list(before)
	result[c] = result[a]&result[b]
	if result == after:
		possible.append( 'banr')

	# bani
	result = list(before)
	result[c] = result[a]&b
	if result == after:
		possible.append( 'bani'	)		

	# borr
	result = list(before)
	result[c] = result[a]|result[b]
	if result == after:
		possible.append( 'borr')

	# bori
	result = list(before)
	result[c] = result[a]|b
	if result == after:
		possible.append( 'bori'	)

	# setr
	result = list(before)
	result[c] = result[a]
	if result == after:
		possible.append( 'setr')
	
	# seti
	result = list(before)
	result[c] = a
	if result == after:
		possible.append( 'seti')

	# gtir
	result = list(before)
	if a > result[b]:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'gtir'	)	

	# gtri
	result = list(before)
	if result[a] > b:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'gtri'	)

	# gtrr
	result = list(before)
	if result[a] > result[b]:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'gtrr'	)

	# eqir
	result = list(before)
	if a == result[b]:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'eqir'	)	

	# eqri
	result = list(before)
	if result[a] == b:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'eqri'	)

	# eqrr
	result = list(before)
	if result[a] == result[b]:
		result[c] = 1
	else:
		result[c] = 0
	if result == after:
		possible.append( 'eqrr'	)

	return possible

samples = []
program = []
with open('./input16.txt') as fp:
	line = fp.readline().strip()
	while line and line[:7] == "Before:":
		before = map(int,re.findall('\d+', line))
		inst = map(int,fp.readline().strip().split())
		after = map(int,re.findall('\d+', fp.readline().strip()))
		x = fp.readline()
		samples.append((before, inst, after))
		line = fp.readline().strip()
	while not line:
		line = fp.readline().strip()
	while line:
		program.append(map(int,line.split()))
		line = fp.readline().strip()
	print program[:3]

print "samples:",len(samples)

codes = {}
count = 0
for sample in samples:
	code = sample[1][0]
	poss = evalsample(sample)
	if code in codes:
		codes[code] = [inst for inst in poss if inst in codes[code]]
	else:
		codes[code] = poss

	if len(poss) >= 3:
		count += 1

print("#1",count)

# determine program by process of elimination
known = {}	

while codes:
	for code in codes:
		if len(codes[code])==1:
			known[code] = codes[code][0]
	for code in codes:
		codes[code] = [inst for inst in codes[code] if inst not in known.values()]
	codes = {k:v for (k,v) in codes.items() if v != []}

#known = dict((v,k) for k,v in known.items())


print len(program)

for k in known:
	print k, known[k]

cpu = [0,0,0,0]
for inst in program:
	op, a, b, c = inst
	#print known[op]
	if known[op]=='addr':
		cpu[c]=cpu[a]+cpu[b]
	elif known[op]=='addi':
		cpu[c]=cpu[a]+b
	elif known[op]=='mulr':
		cpu[c]=cpu[a]*cpu[b]
	elif known[op]=='muli':
		cpu[c]=cpu[a]*b
	elif known[op]=='banr':
		cpu[c]=cpu[a]&cpu[b]		
	elif known[op]=='bani':
		cpu[c]=cpu[a]&b
	elif known[op]=='borr':
		cpu[c]=cpu[a]|cpu[b]		
	elif known[op]=='bori':
		cpu[c]=cpu[a]|b
	elif known[op]=='setr':
		cpu[c]=cpu[a]			
	elif known[op]=='seti':
		cpu[c]=a
	elif known[op]=='gtir':
		if a > cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif known[op]=='gtri':
		if cpu[a] > b:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif known[op]=='gtrr':
		if cpu[a] > cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif known[op]=='eqir':
		if a == cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif known[op]=='eqri':
		if cpu[a] == b:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif known[op]=='eqrr':
		if cpu[a] == cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0
	else:
		print "unknown instr", op		

print "#2:", cpu			

