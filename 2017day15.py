startA = 634
startB = 301

factorA = 16807
factorB = 48271

divideby = 2147483647

currA = startA
currB = startB

matches = 0
count = 0

while count < 40000000:
	count += 1
	currA = currA*factorA % divideby
	currB = currB*factorB % divideby	
	if currA & 0xFFFF == currB & 0xFFFF:
		matches += 1
print ("#1: {} ".format(matches))	

currA = startA
currB = startB

matches = 0
count = 0

while count < 5000000:
	count += 1
	currA = currA*factorA % divideby
	while currA % 4 != 0:
		currA = currA*factorA % divideby
	currB = currB*factorB % divideby	
	while currB % 8 != 0:
		currB = currB*factorB % divideby
	# print(currA, currB, bin(currA)[-16:])
	if currA & 0xFFFF == currB & 0xFFFF:
		matches += 1
print ("#2: {} ".format(matches))
