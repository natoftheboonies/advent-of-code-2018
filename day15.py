from collections import deque
import copy

board = []
def printBoard(game, gobs, elfs):
	for y in range(len(game)):
		rowgobs = [gob+['G'] for gob in gobs if gob[0]==y]
		rowelfs = [elf+['E'] for elf in elfs if elf[0]==y]
		#print (rowgobs+rowelfs)
		players = ','.join(player[3]+'('+str(player[2])+')' for player in sorted(rowgobs+rowelfs))
		print(''.join(game[y]), players)


def calcMove(game,player,enemies):
	view = copy.deepcopy(game)
	#calc in range
	for enemy in enemies:
		#print "enemy(y,x):",(enemy[0],enemy[1]),view[enemy[0]][enemy[1]]
		# up
		if enemy[0]>1 and view[enemy[0]-1][enemy[1]] == '.':
			view[enemy[0]-1][enemy[1]] = '?'
		# left
		if enemy[1]>1 and view[enemy[0]][enemy[1]-1] == '.':
			view[enemy[0]][enemy[1]-1] = '?'
		# down
		if enemy[0]<len(view) and view[enemy[0]+1][enemy[1]]=='.':
			view[enemy[0]+1][enemy[1]] = '?'
		# right
		if enemy[1]<len(view[enemy[0]]) and view[enemy[0]][enemy[1]+1]=='.':
			view[enemy[0]][enemy[1]+1] = '?'
	#printBoard(view)
	# https://stackoverflow.com/questions/47896461/get-shortest-path-to-a-cell-in-a-2d-array-python
	queue = deque([[(player[1],player[0])]])
	seen = set([(player[1],player[0])])
	bestPath = []
	while queue:
		path = queue.popleft()
		x, y = path[-1]
		if view[y][x]=='?':
			bestPath = path
			break
		# reading order: up, left, right, down
		for x2, y2 in [(x,y-1), (x-1,y), (x+1, y),(x,y+1)]:
			if 0 <= x2 < len(view[y]) and 0 <= y2 < len(view) and view[y2][x2] in '.?' and (x2,y2) not in seen:
				queue.append(path+[(x2,y2)])
				seen.add((x2,y2))
	if bestPath:
		return bestPath[1]		
	return None

def findAttackable(player, enemies):
	attackable = []
	for enemy in sorted(enemies):
		if player[0]==enemy[0] and (player[1]==enemy[1]-1 or player[1]==enemy[1]+1):
			#print("elf {} can already attack gob {}".format(player,gob))
			attackable.append(enemy)
		elif player[1]==enemy[1] and (player[0]==enemy[0]-1 or player[0]==enemy[0]+1):
			#print("elf {} can already attack gob {}".format(player,gob))
			attackable.append(enemy)
	return attackable


with open('input15.txt') as fp:
	line = fp.readline().strip()
	while line:
		board.append(list(line))
		line = fp.readline().strip()

boardSize = (len(board), len(board[0]))
print("board:",boardSize)

gobs = []
elfs = []
for y in range(len(board)):
	for x in range(len(board[y])):
		if board[y][x]=='E':
			elfs.append([y,x,200])
		elif board[y][x]=='G':
			gobs.append([y,x,200])

boardIn = board
elfsIn = elfs
gobsIn = gobs

# part1 is one round short and I don't know why.
part1 = False
part2 = not part1

elfpower = 3
elfDied = False

while part1 or part2:
	part1 = False
	board = copy.deepcopy(boardIn)
	elfs = copy.deepcopy(elfsIn)
	gobs = copy.deepcopy(gobsIn)

	for x in range(400):

		elfDied = False
		for player in sorted(elfs+gobs):
			#view = copy.deepcopy(board)
			if player in elfs:
				#print 'Elf'
				attackable = findAttackable(player,gobs)
				if not attackable:	
					move = calcMove(board,player,gobs)
					if move:
						played = 1
						board[player[0]][player[1]] = '.'
						player[0], player[1] = move[1], move[0]
						board[player[0]][player[1]] = 'E'
					attackable = findAttackable(player,gobs)
				# attack!
				#print("attackable", attackable)
				attack = None
				for gob in sorted(attackable):
					if not attack:
						attack = gob
					elif attack[2]>gob[2]:
						attack = gob
				if attack:
					played = 1
					#print("elf {} attacks gob {}".format(player,attack))				
					if attack[2]<=elfpower:
						# finish him!
						#print ("finish him!")
						board[attack[0]][attack[1]] = '.'
						gobs.remove(attack)
					else:
						attack[2]-=elfpower
			elif player in gobs:
				#print 'Goblin'
				# can attack?
				attackable = findAttackable(player,elfs)
				if not attackable:
					# otherwise move
					move = calcMove(board,player,elfs)
					if move:
						played = 1
						board[player[0]][player[1]] = '.'
						player[0], player[1] = move[1], move[0]
						board[player[0]][player[1]] = 'G'			
						#printBoard(board)
					attackable = findAttackable(player,elfs)
				# attack!
				#print("attackable", attackable)
				attack = None
				for elf in sorted(attackable):
					if not attack:
						attack = elf
					elif attack[2]>elf[2]:
						attack = elf
				if attack:
					#print("gob {} attacks elf {}".format(player,attack))
					played = 1
					if attack[2]<=3:
						# finish him!
						#print ("finish him!")
						board[attack[0]][attack[1]] = '.'
						elfs.remove(attack)
						elfDied = True
					else:
						attack[2]-=3

		#print("After {} rounds:".format(x+1))			
		#printBoard(board, gobs, elfs)
		if part2 and elfDied:
			break		
		if not gobs or not elfs:
			#print "game over"
			winners = gobs
			if not winners:
				winners = elfs
			sum = 0
			for player in winners:
				sum += player[2]
			print("Outcome: {} x {} = {}".format(x,sum,sum*(x)))
			#printBoard(board, gobs, elfs)
			#print("Or perhaps: {} x {} = {}".format(x+1,sum,sum*(x+1)))
			break
	if part2 and not elfDied:
		print "Elves won with power:",elfpower
		break
	elfpower+=1
