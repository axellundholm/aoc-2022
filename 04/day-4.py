def find_pairs(assignments):

	fc_pairs = 0
	o_pairs = 0

	for a in assignments:
		fi_lo = a[0][0]
		fi_hi = a[0][1]
		se_lo = a[1][0]
		se_hi = a[1][1]

		fc_pairs += 1 if fi_lo >= se_lo and fi_hi <= se_hi or se_lo >= fi_lo and se_hi <= fi_hi else 0
		o_pairs += 1 if fi_hi >= se_lo and fi_lo <= se_hi else 0

	return fc_pairs, o_pairs

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[[int(i) for i in e.split('-')] for e in x.strip().split(',')] for x in l]

	fully_contained, overlaps = find_pairs(l)

	print("Answer to Part One: " + str(fully_contained))
	print("Answer to Part Two: " + str(overlaps))


if __name__=="__main__":
	main()


