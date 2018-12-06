from collections import defaultdict
import sys

register = defaultdict(int)
lastSound = None
x=0

def regval(arg):
	try:
		return int(arg)
	except ValueError:	
		return register[arg]

def set(arg):
	register[arg[0]]=regval(arg[1])

def add(arg):
	register[arg[0]]+=regval(arg[1])

def mul(arg):
	register[arg[0]]*=regval(arg[1])

def snd(arg):
	global lastSound
	lastSound = register[arg[0]]
	print ("sound: {}".format(lastSound))

def mod(arg):
	register[arg[0]]%=regval(arg[1])

def rcv(arg):
	if register[arg[0]] != 0:
		print("exit singing: {}".format(lastSound))
		sys.exit()
	else:
		print("rcv skip")

def jgz(arg):
	if register[arg[0]]!=0:
		print "jgz {}".format(regval(arg[1]))
		return regval(arg[1])
	else:
		print("jgz skip")

funcs = {
	'set':set,
	'add':add,
	'mul':mul,
	'snd':snd,
	'mod':mod,
	'rcv':rcv,
	'jgz':jgz
}

inst = []
with open('./input2017d18.txt') as fp:
	line = fp.readline().strip()
	while line:
		inst.append(line.split(' '))
		line = fp.readline().strip()


count = 0

while x < len(inst):
	print inst[x]
	result = funcs[inst[x][0]](inst[x][1:])
	if result:
		print ("x was {}, is now {}".format(x, x+result))
		x += result
	else:
		x+=1
	count += 1
	if count > 2000:
		print("!!!abort!!!")
		break

