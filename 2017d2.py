d = open("input2017d2.txt").read().strip().split('\n')
d = map(lambda s: map(int, s.split('\t')), d)
print("#1: {}".format(sum(map(lambda s: max(s)-min(s), d))))

r = []
for x in d:
	for a in x:
		for b in x:
			if a > b and a%b==0:
				r.append(a/b)
				break
print ("#2: {}".format(sum(r)))

# whoa!
print sum(a/b for x in d for a in x for b in x if a > b and a % b == 0)

