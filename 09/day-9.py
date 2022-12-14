import numpy as np

def move_rope(moves, knots):

	rope = [np.array([0, 0]) for i in range(knots)]

	visited = {tuple(rope[-1])}

	for move in moves:
		for s in range(move[1]):

			if move[0] == 'U':
				rope[0][1] += 1
			elif move[0] == 'D':
				rope[0][1] -= 1
			elif move[0] == 'R':
				rope[0][0] += 1
			elif move[0] == 'L':
				rope[0][0] -= 1

			for ki in range(len(rope) - 1):
				if abs(rope[ki][0] - rope[ki + 1][0]) > 1 or abs(rope[ki][1] - rope[ki + 1][1]) > 1:
					rope[ki + 1] += np.sign(rope[ki] - rope[ki + 1])

					if ki == len(rope) - 2:
						visited.add(tuple(rope[ki + 1]))

	return len(visited)

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[int(i) if i.isdigit() else i for i in x.strip().split()] for x in l]
	
	print("Answer to Part One: " + str(move_rope(l, 2)))
	print("Answer to Part Two: " + str(move_rope(l, 10)))


if __name__=="__main__":
	main()


