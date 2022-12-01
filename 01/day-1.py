def max_cals(c_ls, nbr):
	
	tot_cals = sorted([sum(c) for c in c_ls])

	return sum(tot_cals[-nbr:])


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	cals = [[int(e) for e in x] for x in [x.split(' ') for x in ' '.join([x.strip() for x in l]).split('  ')]]

	print("Answer to Part One: " + str(max_cals(cals, 1)))
	print("Answer to Part Two: " + str(max_cals(cals, 3)))