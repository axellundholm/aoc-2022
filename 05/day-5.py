import numpy as np

def cleanup_input(lst):
		
	stacks = []

	for x in reversed(lst[0:lst.index('')][:-1]):
		stacks.append([*x[1:-1:4]])

	stacks = np.array(stacks).T.tolist()
	
	for s in stacks:
		while s[-1] == ' ':
			s.pop()

	inst = [[int(i) for i in x.split() if i.isdigit()] for x in lst[lst.index('') + 1:]]

	return stacks, inst

def move_crates(stacks, inst, model):
	
	for i in inst:
		if model == '9000':
			for r in range(i[0]):
				stacks[i[2] - 1].append(stacks[i[1] - 1].pop())

		elif model == '9001':
			crane = []
			
			for r in range(i[0]):
				crane.append(stacks[i[1] - 1].pop())
			for c in reversed(crane):
				stacks[i[2] - 1].append(c)

	return ''.join([x.pop() for x in stacks])

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip('\n') for x in l]

	stacks, inst = cleanup_input(l)
	print("Answer to Part One: " + str(move_crates(stacks, inst, '9000')))
	stacks, inst = cleanup_input(l)
	print("Answer to Part Two: " + str(move_crates(stacks, inst, '9001')))


if __name__=="__main__":
	main()


