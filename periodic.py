def periodic(name):
	table = {'c':12, 'C':12, 'h': 1, 'H': 1, 'o': 16, 'O': 16, 'n': 14, 'N': 14}
	if name in table:
		return table[name]
	else:
		print 'Unknown element for mass: {0}'.format(name)
