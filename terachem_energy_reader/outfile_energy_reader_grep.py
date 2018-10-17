#call this as python outfile_energy_reader_grep.py (name_of_your_output_file)

import subprocess
import sys

def main(filename):
	done = False
	statelist = []
	statenum = 1
	while not done:
		newlist = []
		try: 
			for line in subprocess.check_output('grep "Singlet state *{0}" {1}'.format(statenum, filename), shell=True)[:-1].split('\n'):
				newlist.append(float(line.split()[-1]))
			statenum += 1
			statelist.append(newlist)
		except:
			done = True
	return statelist
