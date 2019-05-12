v0 = 0 
import sys
import linecache
import time
import os
import shutil
import progressbar

def main(filename):
	print 'Iterating {0}...'.format(filename)
 	con = filename
	conf = filename[:-2]
	confile = '{0}.z'.format(con)
	numatoms = int(linecache.getline('base_geometries/fc.z', 1))
	#print 'This many atoms: ', numatoms
	for n in progressbar.progressbar(range(101)):
		outfile = open('iterations/{0}/{1}.z'.format(conf, n), 'w')
		outfile.write(str(numatoms) + '\n')
		outfile.write(confile + '\n')
		for l in range (3, numatoms + 3): #Loops through all the lines in the geometry file
			fcline = linecache.getline('base_geometries/fc.z', l)
			conicline = linecache.getline('base_geometries/{0}'.format(con), l)
			outfile.write(fcline.split()[0] + ' ')
			inx = 0
			outx = 0
			diffx = 0
			if l > 3:
				inr = fcline.split()[1]
				inx = float(fcline.split()[2])
				outx = float(conicline.split()[2])
				diffx = inx + n*((outx - inx)/100)
				outfile.write(str(inr) + ' '+ str(diffx) + ' ' )
			if l > 4: 
				intheta = fcline.split()[3]
				iny = float(fcline.split()[4])
				outy = float(conicline.split()[4])
				diffy = iny + n*((outy - iny)/100)
				outfile.write(str(intheta) + ' ' + str(diffy) + ' ')
			if l > 5:
				inphi = fcline.split()[5]
				inz = float(fcline.split()[6])
				outz = float(conicline.split()[6])
				diffz = inz + n*((outz - inz)/100)
				outfile.write(str(inphi) + ' ' + str(diffz) + ' ' )
			if v0 == 1:
				print 'atom no: ', l-2
				print 'inx: ', inx
				print 'outx: ', outx
				print 'diffx: ', diffx
			outfile.write('\n')
		outfile.close()

filename = sys.argv[1]
main(filename)


