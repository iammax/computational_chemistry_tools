import numpy as np


def main(numfuncs,filename):
	print_level = 0
	infile = open(filename, 'r')
	tensor = np.zeros([numfuncs, numfuncs, numfuncs, numfuncs])
	lines = infile.readlines()
	for line in lines:
		stuff = line.split()
		i,j,k,l = map(int, stuff[0:4])
		i -=1
		j -=1
		k -= 1
		l -= 1
		val = float(stuff[-1])
		if print_level == 1:
			print i,j,k,l,val	
			print 'perms: '
		perms = [[i,j,k,l],[j,i,k,l],[i,j,l,k],[j,i,l,k],[k,l,i,j],[l,k,i,j],[k,l,j,i],[l,k,j,i]]
		for perm in perms:
			if print_level == 1:
				print perm[0],perm[1],perm[2],perm[3]
			tensor[perm[0]][perm[1]][perm[2]][perm[3]] = val
	return tensor
