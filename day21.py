import sys

def execinst(cpu, inst):
	code, a, b, c = inst
	if code=='addr':
		cpu[c]=cpu[a]+cpu[b]
	elif code=='addi':
		cpu[c]=cpu[a]+b
	elif code=='mulr':
		cpu[c]=cpu[a]*cpu[b]
	elif code=='muli':
		cpu[c]=cpu[a]*b
	elif code=='banr':
		cpu[c]=cpu[a]&cpu[b]		
	elif code=='bani':
		cpu[c]=cpu[a]&b
	elif code=='borr':
		cpu[c]=cpu[a]|cpu[b]		
	elif code=='bori':
		cpu[c]=cpu[a]|b
	elif code=='setr':
		cpu[c]=cpu[a]			
	elif code=='seti':
		cpu[c]=a
	elif code=='gtir':
		if a > cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif code=='gtri':
		if cpu[a] > b:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif code=='gtrr':
		if cpu[a] > cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif code=='eqir':
		if a == cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif code=='eqri':
		if cpu[a] == b:
			cpu[c] = 1
		else:
			cpu[c] = 0		
	elif code=='eqrr':
		if cpu[a] == cpu[b]:
			cpu[c] = 1
		else:
			cpu[c] = 0
	else:
		print "unknown instr", op	


ipreg = 0
program = []

reg = [0]*6

with open('input21.txt') as fp:
	line = fp.readline().strip()
	ipreg = int(line[-1])
	line = fp.readline().strip()
	while line:
		inst = line.split()
		program.append([inst[0]]+list(map(int,inst[1:])))
		line = fp.readline().strip()

# part 2
reg[0] = 1
print "registers: {}".format(reg)
#print ipreg
#print program

ip = 0

inf = 0

r4list = []

while 0 <= ip < len(program):

	inf+=1
	inst = program[ip]
	reg[ipreg]=ip 
	#out = "ip={} {}".format(ip-1, reg)
	#out += " {} {}".format(inst[0],' '.join(map(str,inst[1:])))
	execinst(reg,inst)
	#out += " {}".format(reg)
	if ip == 28:
		# not gonna optimize today, i found pypy :)
		if reg[4] in r4list:
			print "#2:", r4list[-1]
			break
		else:
			if not r4list:
				print "#1:", reg[4]
			r4list.append(reg[4])
			#print out
	#if inf > 10000000:
	#	print len(r4list)
	#	break
	ip = reg[ipreg]
	ip += 1	

print inf, reg


