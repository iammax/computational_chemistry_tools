# reads from a file in the working directory named "out".

def main(filename): #for a 3 state FOMO CASCI

	infile = open(filename, 'r')
	lines = infile.readlines()
	counter = 0
	s0 = []
	s1 = []
	s2 = []
	for line in lines:
		stuff = line.split()
		if len(stuff) > 0:
			if stuff[0] == 'Root' and stuff[1] == 'Mult.':
				#print line
				#print 'This is line #: ', counter
				templist = []			
				for q in range (2, 5):
					templist.append(float(lines[counter+q].split()[2]))
				#print templist
				s0.append(templist[0])
				s1.append(templist[1])
				s2.append(templist[2])
		counter += 1
	return s0, s1, s2

def main2(filename): #for a 1 state DFT
	infile = open(filename, 'r')
	lines = infile.readlines()
	energies = []
	for line in lines:
		stuff = line.split()
		if len(stuff) > 0:
			if stuff[0] == 'FINAL':
				energies.append(float(stuff[2]))
	return energies

def main3(filename): #for bottom 2 states
	infile = open(filename, 'r')
	lines = infile.readlines()
	counter = 0
	s0 = []
	s1 = []
	for line in lines:
		stuff = line.split()
		if len(stuff) > 0:
			if stuff[0] == 'Root' and stuff[1] == 'Mult.':
				#print line
				#print 'This is line #: ', counter
				templist = []			
				for q in range (2, 4):
					templist.append(float(lines[counter+q].split()[2]))
				#print templist
				s0.append(templist[0])
				s1.append(templist[1])
		counter += 1
	return s0, s1

