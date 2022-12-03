
def define_rounds(strat_guide, enc=False):

	move_map = [['A', 'B', 'C'], ['X', 'Y', 'Z']]
	rounds = []

	for m in strat_guide:
		rounds.append([move_map[0].index(i) if i in move_map[0] else move_map[1].index(i) for i in m])

	if enc:
		rounds = decrypt(rounds)

	return rounds

def play_game(s_g, enc=False):

	rs = define_rounds(s_g, enc)
	score = 0

	for r in rs:
		score += calc_score(r)
	
	return score

def calc_score(round):

	win = 6
	draw = 3 
	loss = 0
	
	if (round[0] + 1) % 3 == round[1]:
		return win + (round[1] + 1)
	elif (round[0] == round[1]):
		return draw + (round[1] + 1)
	else:
		return loss + (round[1] + 1)

def decrypt(rounds):

	for m in rounds:
		if m[1] == 2:
			m[1] = (m[0] + 1) % 3
		elif m[1] == 1:
			m[1] = m[0]
		else:
			m[1] = (m[0] - 1) % 3

	return rounds

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split(' ') for x in l]

	print("Answer to Part One: " + str(play_game(l)))
	print("Answer to Part Two: " + str(play_game(l, True)))


if __name__=="__main__":
	main()


