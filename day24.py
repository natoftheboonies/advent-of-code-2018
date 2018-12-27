import re

army = ['System', 'Infection']
attack = ['fire', 'slashing', 'radiation', 'bludgeoning', 'cold']

class Squad(object):
	"""docstring for Squad"""
	def __init__(self, army, id, units, hp, immunity, weakness, damage, attack, initiative):
		super(Squad, self).__init__()
		self.army = army
		self.id = id
		self.units = units
		self.hp = hp
		self.immunity = immunity
		self.weakness = weakness
		self.damage = damage
		self.attack = attack
		self.initiative = initiative
	
	def eff_power(self):
		return self.units*self.damage	

	def damage2(self, defender):
		if defender.immunity and self.attack in defender.immunity:
			return 0
		base = self.eff_power()
		if defender.weakness and self.attack in defender.weakness:
			return base*2
		return base

	def __str__(self):
		return army[self.army]+" group "+str(self.id)


#squad = namedtuple('Squad', ['army', 'id', 'units', 'hp', 'immunity', 'weakness', 'damage', 'attack', 'initiative'])

def parse_line(line):
	units = int(re.search(r"([\d]+) units", line).group(1))
	hp = int(re.search(r"([\d]+) hit points", line).group(1))
	immune = None
	immune_match = re.search(r"immune to ([\w, ]+)", line)
	if immune_match: immune = immune_match.group(1).split(", ")
	weak = None 
	weak_match = re.search(r"weak to ([\w, ]+)", line)
	if weak_match: weak = weak_match.group(1).split(", ") 
	attack_match = re.search(r"with an attack that does ([\d]+) ([\w]+) damage", line)
	damage, attack = int(attack_match.group(1)), attack_match.group(2)
	initiative = int(re.search(r"at initiative ([\d]+)", line).group(1))
	return units, hp, immune, weak, damage, attack, initiative

igin = []
with open('input24.txt') as fp:
	line = fp.readline().strip()
	count = 0
	if army[0] in line:
		line = fp.readline().strip()
		while line:
			count += 1
			units, hp, immune, weak, damage, attack, initiative = parse_line(line)
			us = Squad(0, count, units, hp, immune, weak, damage, attack, initiative)
			#print(0, count, units, hp, immune, weak, damage, attack, initiative)
			igin.append(us)
			line = fp.readline().strip()
	line = fp.readline().strip()
	count = 0
	if army[1] in line:
		line = fp.readline().strip()
		while line:
			count += 1
			units, hp, immune, weak, damage, attack, initiative = parse_line(line)
			us = Squad(1, count, units, hp, immune, weak, damage, attack, initiative)
			#print(1, count, units, hp, immune, weak, damage, attack, initiative)
			igin.append(us)
			line = fp.readline().strip()
	line = fp.readline().strip()		
# group has: team, units, hit points, immunity, (weakness), attack, damage, initiative

#Immune System:
#17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
#989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

#ig.append((0,17, 5390, None, (2,3), 0,4507,2)) 
#ig.append((0,989, 1274, 0, (1,3), 1,25,3))

#801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
#4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4 

#ig.append((1,801, 4706, None, [2], 3, 116, 1))
#ig.append((1,4485, 2961, 3, (0,4), 1, 12, 4))

def battle(input, boost):
	ig = []
	for g in input:
		damage = g.damage
		if g.army==0: damage += boost
		ig.append(Squad(g.army, g.id, g.units, g.hp, g.immunity, g.weakness, damage, g.attack, g.initiative))
	loop = 0
	while True:
	#for _ in range(1):
		loop+=1
		ig = [g for g in ig if g.units > 0]
		#for g in ig:
		#	print("{} contains {} units".format(g, g.units))

		if 0 not in [g.army for g in ig]: break
		elif 1 not in [g.army for g in ig]: break	

		target_selection = sorted(ig, key=lambda g: (g.eff_power(), g.initiative), reverse=True)

		selected = []
		attacks = {}

		for team in target_selection:
			#print ("{} has base power {}".format(team, team.eff_power()))
			opponents = [group for group in ig if group.army != team.army and group not in selected]
			select = None
			for enemy in opponents:
				#print("{} would deal defending group {} {} damage".format(team, enemy.id, team.damage2(enemy)))
				if team.damage2(enemy) == 0: continue
				if not select or team.damage2(enemy) > team.damage2(select):
					#print("selecting based on damage")
					select = enemy
				elif team.damage2(enemy)==team.damage2(select):
					if enemy.eff_power()>select.eff_power():
						#print("selecting {} based on power {} vs.".format(enemy.id, enemy.eff_power()), select.id, select.eff_power())
						select = enemy
					# it chooses the defending group with the highest initiative!!!
					elif enemy.eff_power()==select.eff_power() and enemy.initiative > select.initiative:
						#print("selecting based on initiative")
						select = enemy
			if select:
				#print ("defending group {} receives {} damage".format(select.id, team.damage2(select)))
				selected.append(select)
				attacks[(team.army, team.id)] = select

		#print()
		attacking = sorted(ig, key=lambda g: g.initiative, reverse=True)
		stalemate = True
		for attacker in attacking:
			if attacker.units == 0: continue
			if (attacker.army, attacker.id) not in attacks.keys(): continue
			defender = attacks[(attacker.army, attacker.id)]
			killed = min(attacker.damage2(defender)//defender.hp, defender.units)
			if killed > 0: stalemate = False
			#print("{}: {} group {} attacks defending group {}, killing {} units".format(attacker.initiative, army[attacker.army], attacker.id, defender.id, killed))
			defender.units -= killed

		#print()
		if stalemate: 
			print ("Stalemate!")
			break
	return ig


result = battle(igin, 0)
print ("#1:",result[0].army, sum([g.units for g in result]))

boost = 1
while True:
	result = battle(igin, boost)
	if all([g.army==0 for g in result]): 
		print ("#2: {} at boost {}".format(sum([g.units for g in result if g.army==0]), boost))
		break
	else:
		print ("tried boost:", boost)
	
	boost += 1
	if boost > 1000: break

# wrong: 8694
