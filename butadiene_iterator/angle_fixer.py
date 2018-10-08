import linecache
import os
import sys


def main(filename):
	print 'Fixing angles for {0} ...'.format(filename)
	tfc = open('basegeo/tfc.z', 'w')
	tci = open('basegeo/tci.z', 'w')
	n = filename
	for l in range (0, 13):
		infcd = linecache.getline('basegeo/fc.z', l)
		inccd = linecache.getline('basegeo/{0}'.format(n), l)
		if l > 5: 
			infcdi = float(infcd.split()[6])
			inccdi = float(inccd.split()[6])
			templine = ''
	#		print 'conformation: ', n[0:-2]
	#		print 'line number: ', l
	#		print 'FC dihedral: ', infcdi
	#		print 'Conical dihedral: ', inccdi
			diff = inccdi - infcdi
	#		print 'Difference: ', diff
			if diff < -180:
	#			print 'Rotating the long way, lowering fc!'
				infcdi = infcdi - 360
	#			print 'Now, fc dihedral: ', infcdi
	#			print 'Now, conical dihedral: ', inccdi
				diff = inccdi - infcdi
	#			print 'Now, diff: ', diff
				for word in range(0, len(infcd.split())-1):
					templine += infcd.split()[word] + ' ' 
	#			print 'pre templine: ', templine
				templine = templine + ' ' + str(infcdi)
	#			print 'templine: ', templine
				infcd = templine + '\n'
			if diff > 180:
	#			print 'Rotating the long way, lowering CI!'
				inccdi = inccdi - 360
	#			print 'Now, fc dihedral: ', infcdi
	#			print 'Now, conical dihedral: ', inccdi
				diff = inccdi - infcdi
	#			print 'Now, diff: ', diff	
				for word in range (0,len(inccd.split())-1):
					templine += inccd.split()[word] + ' ' 	
				templine = templine + ' ' + str(inccdi)	
	#			print 'templine: ', templine
				inccd = templine + '\n'
	#		print '\n'		 
	#	print 'infcd: ', infcd
	#	print 'inccd: ', inccd
		tfc.write(infcd)
		tci.write(inccd)
	tfc.close()
	tci.close()
	os.remove('basegeo/{0}'.format(n))
	os.remove('basegeo/fc.z')
	os.rename('basegeo/tfc.z', 'basegeo/fc.z')
	os.rename('basegeo/tci.z', 'basegeo/{0}'.format(n))

filename = sys.argv[1]
main(filename)
