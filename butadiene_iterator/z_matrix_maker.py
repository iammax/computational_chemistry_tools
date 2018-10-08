#Input your cartesian xyz file from command line. This script will read from zmatconfig.txt to determine angles if it exists. Outputs to (cartesian's name).z in results/ folder.

import sys
import numpy as np
from periodic import periodic

class atom:
	def __init__(self, name, mass, x, y, z, bond = None, angle= None, torsion= None):
		self.name = name
		self.mass = mass
		self.x = x
		self.y = y
		self.z = z
		self.bond = bond
		self.torsion = torsion
		self.angle = angle

def bondlength(i, j): #bond length
	return np.sqrt( (i.x-j.x)**2 + (i.y - j.y)**2 + (i.z-j.z)**2)

def bondangle(i, j, k): #bond angle; j is vertex
	eji = unitvector(j, i)
	ejk = unitvector(j, k)
	dot = np.dot(eji, ejk)
	return np.degrees(np.arccos(dot))

def unitvector(i, j):
	Rij = bondlength(i, j)
	x = (i.x-j.x)/Rij
	y = (i.y-j.y)/Rij
	z = (i.z-j.z)/Rij
	return np.array([-x, -y, -z])		

def torsional(i, j, k, l): #http://azevedolab.net/resources/dihedral_angle.pdf #angle between ijk and jkl
	q1 = unitvector(i, j)
	q2 = unitvector(j, k)
	q3 = unitvector(k, l)
	firstcross = np.cross(q1, q2)
	secondcross = np.cross(q2, q3)
	n1 = firstcross/np.linalg.norm(firstcross)
	n2 = secondcross/np.linalg.norm(secondcross)
	u1 = n2
	u3 = q2/np.linalg.norm(q2)
	u2 = np.cross(u3, u1)
	cos_theta = np.dot(n1,u1)
	sin_theta = np.dot(n1,u2)
	theta = -np.arctan2(sin_theta,cos_theta) # it is different from Fortran math.atan2(y,x)
	theta_deg = np.degrees(theta)
	return -theta_deg

def atomlistmaker(infile):
	try:
		infile = open(infile, 'r')
	except:
		print	'No infile supplied, looking for test.xyz...'
		try: 
			infile = open('test.xyz', 'r')
		except: 
			print 'No test.xyz either! Quitting...'
			quit()
	lines = infile.readlines()
	try: 
		numatoms = int(lines[0])
	except:
		print 'Invalid number of atoms in xyz file'
		quit()
	numlines = len(lines)
	if numlines < 3:
		print 'Bad xyz file'
		quit()
	atomlist = []
	try:
		specify_config = int(sys.argv[2])
	except:
		specify_config = 1
	if specify_config == 1:
		zmatconfig = np.genfromtxt('zmatconfig.txt')
		if len(zmatconfig) != numatoms:
			print 'config lines: ', len(zmatconfig)
			print 'num atoms: ', numatoms
			print 'Config file has different length than # of atoms'
			quit()
	else:
		zmatconfig = [[q, 1, 2, 3] for q in range (0, numatoms)]
	counter = 0
	for line in lines[2: numatoms+3]:
		stuff = line.split()
		name = stuff[0]
		x, y, z = map(float, stuff[1:])
		bond, angle, torsion = map(int,zmatconfig[counter][1:])
		newatom = atom(name, periodic(name), x, y, z, bond, angle, torsion)
		atomlist.append(newatom)	
		counter += 1
	return atomlist


def dihedral_all():
	atomlist = atomlistmaker(sys.argv[1])
	numatoms = len(atomlist)
	for i in range (0, numatoms):
		for j in range(0, numatoms):
			for k in range (0, numatoms):
				for l in range (0, numatoms):
					atomi = atomlist[i]
					atomj = atomlist[j]
					atomk = atomlist[k]
					atoml = atomlist[l]
					torsiona = torsional(atomi, atomj, atomk, atoml)
					if np.isclose(torsiona, 179):
						print 'i, j, k, l, torsion: ', i+1, j+i, k+1, l+1, torsiona
def main():
	zmatrix = []
	atomlist = atomlistmaker(sys.argv[1])
	for r in range (0, len(atomlist)):
		q = atomlist[r]
		if r == 0:
			newline = [q.name+ ' ']
		elif r == 1:
			bl = bondlength(q, atomlist[q.bond-1])
			newline = map(str, [q.name, q.bond, bl])
			newline.append('')
		elif r == 2:
			bl = bondlength(q, atomlist[q.bond-1])
			ba = bondangle(q, atomlist[q.bond-1], atomlist[q.angle-1])
			newline = map(str, [q.name, q.bond, bl, q.angle, ba])
		elif r > 2:
			i = q
			j = atomlist[q.bond-1]
			k = atomlist[q.angle-1]
			l = atomlist[q.torsion-1]
			bl = bondlength(q, atomlist[q.bond-1])
			ba = bondangle(i, j, k)
#			da = torsional(q, atomlist[q.bond-1], atomlist[q.angle-1], atomlist[q.torsion-1])	
#			da = torsional(k, j, i, j)
			i = q
			j = atomlist[q.bond-1]
			k = atomlist[q.angle-1]
			l = atomlist[q.torsion-1]
			da = torsional(i, j, k, l)
#			da = quicktorsional(r+1, q.bond, q.angle, q.torsion)
			newline = map(str, [q.name, q.bond, bl, q.angle, ba, q.torsion, da])
		zmatrix.append(newline)
#	for line in zmatrix:
#		newline = ' '.join(line)
#		print newline	
#	dihedral_all()
	outfile = open('results/{0}.z'.format(sys.argv[1][:-4]), 'w')
	outfile.write('{0}\n{1}\n'.format(len(atomlist), sys.argv[1][:-4]))
	for line in zmatrix:
		newline = ' '.join(map(str, line)) + '  ' + '\n'
		outfile.write(newline)
	outfile.close()
main()

