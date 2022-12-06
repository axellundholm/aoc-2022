
def find_start_marker(lst, nbr):

	for x in range(len(lst) - nbr - 1):
		if len(set(lst[x:x + nbr])) == nbr:
			return x + nbr

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l][0]

	print("Answer to Part One: " + str(find_start_marker(l, 4)))
	print("Answer to Part Two: " + str(find_start_marker(l, 14)))


if __name__=="__main__":
	main()


