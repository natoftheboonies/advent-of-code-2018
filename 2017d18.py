from collections import defaultdict

def regval(arg):
	try:
		return int(arg)
	except ValueError:	
		return register[arg]

inst = []
with open('./input2017d18.txt') as fp:
	line = fp.readline().strip()
	while line:
		inst.append(line.split(' '))
		line = fp.readline().strip()

register = defaultdict(int)
lastSound = None
x=0

while x < len(inst):
	print inst[x]
	arg = inst[x][1:]
	if inst[x][0] == 'set':
		register[arg[0]]=regval(arg[1])
	elif inst[x][0] == 'add':
		register[arg[0]]+=regval(arg[1])
	elif inst[x][0] == 'mul':
		register[arg[0]]*=regval(arg[1])
	elif inst[x][0] == 'snd':
		lastSound = register[arg[0]]
	elif inst[x][0] == 'mod':
		register[arg[0]]%=regval(arg[1])
	elif inst[x][0] == 'rcv':
		if register[arg[0]] != 0:
			print("exit singing: {}".format(lastSound))
			break
	elif inst[x][0] == 'jgz':
		if regval(arg[0])!=0:
			print "jgz {}".format(regval(arg[1]))
			x+= regval(arg[1])
			x-=1 # because always increment
	x+=1		

