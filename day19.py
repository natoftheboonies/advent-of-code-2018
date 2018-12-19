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

with open('input19.txt') as fp:
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

while 0 <= ip < len(program):
	if inf > 1000:
		None #break
	inf+=1
	if ip == 2:
		print reg
		for x in range(1,reg[5]+1):
			if reg[5]%x==0:
				reg[0]+=x
		#while (reg[4]<=reg[5]):
		#	reg[2] = 1
		#	while (reg[2]<=reg[5]):
		#		if reg[2]*reg[4]==reg[5]:
		#			reg[0]+=reg[4]
		#		reg[2]+=1
		#	reg[4]+=1
		#reg[2] = reg[5]
		ip = 16
	inst = program[ip]
	reg[ipreg]=ip 
	#out = "ip={} {}".format(ip, reg)
	#out += " {} {}".format(inst[0],' '.join(map(str,inst[1:])))
	execinst(reg,inst)
	#out += " {}".format(reg)
	#if inf > 7700000:
	#	print out
	#if inf > 7703000:
	#	break
	ip = reg[ipreg]
	ip += 1	

print reg



"""
if ip == 2 and R4 != 0:
	do:
		R2 = 1
		do:
	  		if R4*R2==R5:
	  			R0 += R4
	  		R2 += 1  			
		while (R2 <= R5)
	R4+=1
	while (R4<=R5)


 ### outer loop
2:  seti 1 7 2 R2 = 1
 ### inner loop is
3:  mulr 4 2 1 R1 = R4*R2 
4:  eqrr 1 5 1 if R1 == R5: R1 = 1, else 0
5:  addr 1 3 3 R3 += R1 # exit, jump to 7
6:  addi 3 1 3 R3 += 1 # no exit, jump to 8
7:  addr 4 0 0 R0 += R4 # store R4 for end
8:  addi 2 1 2 R2 += 1 # increment R2
9:  gtrr 2 5 1 if R2 > R5: R1 = 1, else 0 # if R2 > R5 exit
10: addr 3 1 3 R3 += R1 # exit, jump to 12
11: seti 2 6 3 R3 = 2 # no exit, jump to 3
12: addi 4 1 4 R4 += 1 # increment R4
13: gtrr 4 5 1 R1 = 1 if R4 > R5 else 0
14: addr 1 3 3 R3 += R1 # if exit, jump to 16 
15: seti 1 3 3 R3 = 1 # no exit, jump to 2
"""




