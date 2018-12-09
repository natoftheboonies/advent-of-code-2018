
# help from: https://dbader.org/blog/python-linked-list

class Marble(object):
	"""docstring for Marble"""
	def __init__(self, arg, next=None, prev=None):
		super(Marble, self).__init__()
		self.arg = arg
		if next:
			self.next = next
			next.prev = self
		if prev:
			self.prev = prev
			prev.next = self

	def pop(self):
		self.prev.next = self.next
		self.next.prev = self.prev
		return self.prev

	def __repr__(self):
		nodes = [self.arg]
		next = self.next
		while next != self:
			nodes.append(next.arg)
			next = next.next
		return '['+','.join(map(str,nodes))+']'


players = 419
last = 71052*100

scores = {}

current = Marble(0)
current.next = current
current.prev = current

for i in range(1,last+1):
	p = (i-1)%players+1
	if i%23==0:
		popme = current.prev.prev.prev.prev.prev.prev.prev
		if p in scores.keys():
			scores[p]+=(i+popme.arg)
		else:
			scores[p]=(i+popme.arg)
		#print("score",i,popme.arg)
		current = popme.pop().next
		continue
	current = Marble(i, current.next.next, current.next)
	#print (current)

print ("#1: ",max(scores.values()))
		
