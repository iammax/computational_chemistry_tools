import numpy as np
from periodic import periodic

class atom:
	def __init__(self, name, mass, r, theta, phi, bond, angle, torsion): #copied from z matrix file. x, y, z mean the length, angle, torsion that are in the z matrix file. bond, angle, torsion (as inputted into this function) means which atom the input atom is bonded to (given in the z matrix). 
		self.name = name
		self.mass = mass
		self.r = r
		self.theta = np.radians(theta)
		self.phi = np.radians(phi)
		self.bond = int(bond)
		self.torsion = int(torsion)
		self.angle = int(angle)

def vector(i, j):
	return np.array([j[0]-i[0], j[1]-i[1], j[2]-i[2]])

def dist_from_center(atom): #bond length
	a =  np.sqrt(atom[0]**2 + atom[1]**2 + atom[2]**2)
#	print a
	return a

def xyzgiver(i, xyzmatrix):
	return np.array([xyzmatrix[i][0], xyzmatrix[i][1], xyzmatrix[i][2]])

def atomlistmaker(infilename):	
	infile = open(infilename, 'r')
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
	counter = 0
	for line in lines[2: numatoms+3]:
		stuff = line.split()
		name = stuff[0]
		if len(stuff) == 1:
			bond, r, angle, theta, torsion, phi = [99, 99, 99, 99, 99, 99]
		elif len(stuff) == 3:
			bond, r, angle, theta, torsion, phi = [float(stuff[1]), float(stuff[2]), 88, 88, 88, 88]
		elif len(stuff) == 5:
			bond, r, angle, theta, torsion, phi = [float(stuff[1]), float(stuff[2]), float(stuff[3]), float(stuff[4]), 77, 77]
		elif len(stuff) == 7:
			bond, r, angle, theta, torsion, phi = map(float, stuff[1:])
		else:
			print 'unknown line: ', line
			quit()
		newatom = atom(name, periodic(name), r, theta, phi, bond, angle, torsion)
		atomlist.append(newatom)	
		counter += 1
	outfile = open('results/{0}.xyz'.format(infilename[:-2]), 'w')
	outfile.write(str(len(atomlist))+'\n' + '{0}'.format(infilename[:-2]) + '\n')
	outfile.close()
	return atomlist

def main(infile):
	pl = 0
	try:
		infilename = infile
	except:
		print	'No infile supplied...'
		quit()
	atomlist = atomlistmaker(infile)
#	for atom in atomlist:
#		print atom.name, atom.bond, atom.x, atom.angle, atom.y, atom.torsion, atom.z
	xyzmatrix = []
	for q in range (0, len(atomlist)): #loops through the atoms
		inatom = atomlist[q]
		if q == 0:
			x = 0.00000000; y = 0.00000000; z = 0.00000000
		elif q == 1:
			x = inatom.r; y = 0.00000000; z = 0.00000000
		elif q == 2:
			x = atomlist[1].r - inatom.r*np.cos(inatom.theta); y = inatom.r*np.sin(inatom.theta); z = 0.0000000
		else: #i, j, k are q.bond, q.angle, q.torsion
			#first, find x, y, z in the artificial coordinate system, called C
			r = inatom.r; theta = inatom.theta; phi = inatom.phi
			cx = r*np.cos(theta)
			cy = r*np.sin(theta)*np.cos(phi)
			cz = r*np.sin(theta)*np.sin(phi)
			cxyz = np.array([[cx], [cy], [cz]])			
			#now make the rotation and translation matrix
			i, j, k = inatom.bond -1, inatom.angle-1, inatom.torsion-1
			ixyz = xyzgiver(i, xyzmatrix)
			jxyz = xyzgiver(j, xyzmatrix)
			kxyz = xyzgiver(k, xyzmatrix)
			un_normalized_i = vector(ixyz, jxyz)
			vik = vector(ixyz, kxyz)
			un_normalized_k = np.cross(un_normalized_i, vik)
			norm_i = (un_normalized_i/np.linalg.norm(un_normalized_i))
			norm_k = (un_normalized_k/np.linalg.norm(un_normalized_k))
			norm_j = np.cross(norm_k, norm_i)
			rotation_matrix = np.vstack([norm_i, norm_j, norm_k]).T
			translation_matrix = np.array([[ixyz[0]], [ixyz[1]], [ixyz[2]]])
			if pl == 1:
				print 'for atom #: ', q+1
				print 'its input: ', inatom.r, np.degrees(inatom.theta), np.degrees(inatom.phi)
				print 'i: ', norm_i
				print 'j: ', norm_j
				print 'k: ', norm_k
				print 'rot: ', rotation_matrix
				print 'trans: ', translation_matrix
			#last, transform the points
			rotated_points = np.dot(rotation_matrix, cxyz)
			xyz = rotated_points + translation_matrix
			if pl == 1:
				print 'rotated points: ', rotated_points
				print 'xyz: ', xyz
			x = xyz[0][0]
			y = xyz[1][0]
			z = xyz[2][0]	
		xyzmatrix.append([x, y, z])	
		newline = ' '.join(map(str,[inatom.name, x, y, z]))
		dummy_newline = newline #just for printing with distance
#		dummy_newline += ' ' + str(dist
#		print dummy_newline
	outfile = open('results/{0}.xyz'.format(infilename[:-2]), 'a')
	for q in range (0, len(xyzmatrix)):
		newline = ' '.join(map(str, [atomlist[q].name, xyzmatrix[q][0], xyzmatrix[q][1], xyzmatrix[q][2]])) + '\n'
		outfile.write(newline)
	outfile.close()
