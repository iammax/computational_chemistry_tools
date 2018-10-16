#gets s0, s1, s2 from outfile energy extractor.py and plots them. relies on outfile being named "out".



import outfile_energy_extractor as oee
import sys

filename = sys.argv[1]

from matplotlib import pyplot as plt
s0, s1, s2 = oee.main(filename)
xs = [q for q in range (0, len(s0))]
plt.plot(xs, s0, c = 'r')
plt.plot(xs, s1, c = 'b')
plt.plot(xs, s2, c = 'g')
plt.ticklabel_format(useOffset=False)
plt.legend(['s0', 's1', 's2'])
plt.xlabel('Frame #')
plt.ylabel('Energy')
plt.xlim(None, None)
plt.show()
