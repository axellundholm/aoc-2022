import numpy as np

def move_rope(head, tail, move, visited):

	for s in range(move[1]):

		if move[0] == 'U':
			head[1] += 1
		elif move[0] == 'D':
			head[1] -= 1
		elif move[0] == 'R':
			head[0] += 1
		elif move[0] == 'L':
			head[0] -= 1

		if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
			tail += np.sign(head - tail)
			visited.add(tuple(tail))

	return head, tail, visited

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[int(i) if i.isdigit() else i for i in x.strip().split()] for x in l]

	head = np.array([0, 0])
	tail = np.array([0, 0])
	visited = set()
	visited.add(tuple(tail))

	for move in l:
		head, tail, visited = move_rope(head, tail, move, visited)

	print("Answer to Part One: " + str(len(visited)))
	print("Answer to Part Two: " + str('N/A'))


if __name__=="__main__":
	main()


