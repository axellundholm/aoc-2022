import string

def common_compartments(backpacks):

	comp_list = [[x[0:len(x)//2], x[len(x)//2:]] for x in backpacks]
	com_comp = []

	for comp in comp_list:
		com_comp.append(list(set(comp[0]) & set(comp[1]))[0])

	return calc_prio_sum(com_comp)

def common_groups(backpacks):

	grp_list = []
	com_grp = []

	for i in range(len(backpacks)//3):
		grp_list.append([backpacks.pop(0), backpacks.pop(0), backpacks.pop(0)])

	for grp in grp_list:
		com_grp.append(list(set(grp[0]) & set(grp[1]) & set(grp[2]))[0])

	return calc_prio_sum(com_grp)

def calc_prio_sum(prio_list):

	prio_sum = 0
	score_map = string.ascii_lowercase + string.ascii_uppercase

	for i in prio_list:
		prio_sum += score_map.index(i) + 1

	return prio_sum

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	print("Answer to Part One: " + str(common_compartments(l)))
	print("Answer to Part Two: " + str(common_groups(l)))


if __name__=="__main__":
	main()


