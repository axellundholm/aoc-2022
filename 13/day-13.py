import json

def compare(l, r):

	if isinstance(l, list) and isinstance(r, list):
		for i in range(max(len(l), len(r))):
			if i == len(l) and i != len(r):
				return '<'
			elif i != len(l) and i == len(r):
				return '>'
			elif i == len(l) and i == len(r):
				return '='
			else:
				rel = compare(l[i], r[i])
				if rel != '=':
					return rel

	elif isinstance(l, list) and isinstance(r, int):
		return compare(l, [r])

	elif isinstance(l, int) and isinstance(r, list):
		return compare([l], r)

	elif isinstance(l, int) and isinstance(r, int):
		if l == r:
			return '='
		elif l < r:
			return '<'
		else:
			return '>'
	
	return '='

def decode(lst, div_pack):

	sort_lst = [] 

	for x in lst + div_pack:
		if len(sort_lst) == 0:
			sort_lst.append(x)

		else:
			for i in range(len(sort_lst)):
				if compare(x, sort_lst[i]) == '<':
					sort_lst.insert(i, x)
					break
					
				elif i == len(sort_lst) - 1:
					sort_lst.append(x)

	return (sort_lst.index(div_pack[0]) + 1) * (sort_lst.index(div_pack[1]) + 1)

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [json.loads(x.strip()) for x in l if x != '\n']

	pairs = [[l[x], l[x + 1]] for x in range(0,len(l),2)]
	div_pack = [[[2]], [[6]]]

	cor_pairs = [compare(pair[0], pair[1]) for pair in pairs]
	ind_sum = sum([i + 1 for i in range(len(cor_pairs)) if cor_pairs[i] == '<'])
	dec_key = decode(l, div_pack)

	print("Answer to Part One: " + str(ind_sum))
	print("Answer to Part Two: " + str(dec_key))


if __name__=="__main__":
	main()


