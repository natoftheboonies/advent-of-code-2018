
players = 419
last = 71052 # *100
board = [0]
cursor = 0
scores = {}

# guessed, wrong: 418507

for i in range(1,last+1):
	p = (i-1)%players+1
	if i%23==0:
		cursor = (cursor-7)%len(board)
		x = board.pop(cursor)
		if p in scores.keys():
			scores[p]+=(i+x)
		else:
			scores[p]=(i+x)
		#print ("win", i, x)
		cursor = cursor%len(board)
		continue

	insert = (cursor+2) % len(board)
	#print ("insert at {} of {}".format(insert, len(board)))
	board.insert(insert,i)
	cursor = insert
	
	#print("[p{}]".format(p))		
	#print(board, cursor)
#print (scores)
print (max(scores.values()))
