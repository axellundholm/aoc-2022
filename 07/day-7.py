
def calc_disk_space(cmds):

	size_dict = {}
	path = []

	for cmd in cmds:

		dir_name = cmd[-1]

		if cmd[1] == 'cd':

			if cmd[2] == '..':
				path.pop(-1)

			else:
				name = ''.join(path) + dir_name
				path.append(name)
				size_dict[name] = 0

		elif cmd[0].isdigit():
			size_dir = int(cmd[0])

			for x in path:
				size_dict[x] += size_dir  

	size_sum = 0
	size_lst = []
	
	for i in size_dict:
		size_lst.append(size_dict[i])

		if size_dict[i] <= 100000:
			size_sum += size_dict[i]
			
	min_del = min([x for x in size_lst if x >= -(70000000 - 30000000 - max(size_lst))])

	return size_sum, min_del

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split() for x in l]

	s, min_del = calc_disk_space(l)

	print("Answer to Part One: " + str(s))
	print("Answer to Part Two: " + str(min_del))


if __name__=="__main__":
	main()


