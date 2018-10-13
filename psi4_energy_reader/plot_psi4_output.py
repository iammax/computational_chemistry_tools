from matplotlib import pyplot as plt
import numpy as np

infile = open('psi4_output.txt', 'r')
lines = infile.readlines()
infile.close()
colors = ['', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

phidict = {}
popdict = {}
for q in range (1, 8):
	phidict[q] = []
	popdict[q] = []

numlines = len(lines)
counter = 0
while counter <numlines:
	line = lines[counter]
	if len(line) > 0:
		if line == ' # Orbital energies #\n':
			for q in range (1, 8):
				line = lines[counter+1+q]
				stuff = line.split()
				en = stuff[1]
				phidict[q].append(en)
		if line == ' # Orbital populations #\n':
			for q in range (1, 8):
				line = lines[counter+1+q]
				stuff = line.split()
				en = stuff[1]
				popdict[q].append(en)

	counter += 1

plt.rc('text', usetex=True)

numiters = len(phidict[1])
xs = np.arange(numiters)
plt.subplot(211)
for q in phidict:
	plt.plot(xs, phidict[q], label = "$\phi_{0}$".format(q), color = colors[q])
	plt.xlabel('Iteration')
	plt.ylabel('Orbital energy (hartree)')
plt.legend()
plt.subplot(212)
for q in popdict:
	plt.plot(xs, popdict[q], label = "$\phi_{0}$".format(q), color = colors[q])
	plt.xlabel('Iteration')
	plt.ylabel('Orbital population')

plt.legend()
print 'num iters: ', numiters
plt.show()
