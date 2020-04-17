def score(dice):
	diceRoll = {}
	singles = [1,5]
	triples = [1,2,3,4,5,6]
	score = 0
	for d in dice:
		diceRoll[d] = dice.count(d)
	for r in diceRoll:
		if r in singles or r in triples:
			if diceRoll[r] > 3:
				if r in triples:
					score += 1000 if r == 1 else r*100
				if r in singles:
					score += (diceRoll[r]-3)*100 if r == 1 else (diceRoll[r]-3)*50
			print(score)
			if diceRoll[r] == 1 or diceRoll[r] == 2:
				if r in singles:
					score += diceRoll[r]*100 if r == 1 else diceRoll[r]*50
			
			elif diceRoll[r] == 3:
				if r in triples:
					if r == 1:
						score += 1000
					else:
						score += r*100
	return score