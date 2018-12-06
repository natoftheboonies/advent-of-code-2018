from collections import defaultdict

message = [[],[]]


class Machine(object):
	"""docstring for Machine"""
	def __init__(self, id):
		super(Machine, self).__init__()
		self.id = id
		self.register = defaultdict(int)
		self.register['p']=self.id
		self.x=0
		self.stuck = False
		self.done = False
		self.sentCount = 0

	def regval(self, arg):
		try:
			return int(arg)
		except ValueError:	
			return self.register[arg]

	def run(self):
		while self.x < len(inst):
			#print inst[x]
			todo = inst[self.x][0]
			arg = inst[self.x][1:]
			if todo == 'set':
				self.register[arg[0]]=self.regval(arg[1])
			elif todo == 'add':
				self.register[arg[0]]+=self.regval(arg[1])
			elif todo == 'mul':
				self.register[arg[0]]*=self.regval(arg[1])
			elif todo == 'snd':
				global message
				#print("machine {} sending {} to {}".format(self.id, self.regval(arg[0]),(self.id+1)%2))
				message[1-self.id].append(self.regval(arg[0]))
				self.sentCount+=1
			elif todo == 'mod':
				self.register[arg[0]]%=self.regval(arg[1])
			elif todo == 'rcv':
				#print("machine {} receive {} from {}".format(self.id, arg[0], message[self.id]))
				global message
				if message[self.id]:
					recd = message[self.id].pop(0)
					self.register[arg[0]] = recd
				else:
					#print("machine {} stuck at {}".format(self.id, self.x))
					self.stuck = True
					break
			elif todo == 'jgz':
				if self.regval(arg[0])>0:
					#print "jgz {}".format(self.regval(arg[1]))
					self.x+= self.regval(arg[1])
					self.x-=1 # because always increment
			self.x+=1
			self.stuck = False
		if not self.stuck:
			self.done = True
			print("machine {} done".format(self.id))	

	def done(self):
		return self.done


inst = []
with open('./input2017d18.txt') as fp:
	line = fp.readline().strip()
	while line:
		inst.append(line.split(' '))
		line = fp.readline().strip()


m0 = Machine(0)
m1 = Machine(1)
while True:
	m1.run()
	m0.run()
	if m0.done and m1.done or message == [[],[]]: break


#print(message)
print("#2: {}".format(m1.sentCount))
