v0 = 0 
import sys
import linecache
import time
import os
import shutil

def main_1(filename): #for Me+ and Me-
	print 'Iterating {0}...'.format(filename)
 	con = filename
	conf = filename[:-2]
	confile = '{0}.z'.format(con)
	numatoms = int(linecache.getline('basegeo/fc.z', 1))
	#print 'This many atoms: ', numatoms
	for n in range (0, 101):
		outfile = open('itergeo/{0}/{1}.z'.format(conf, n), 'w')
		outfile.write(str(numatoms) + '\n')
		outfile.write(confile + '\n')
		for l in range (3, numatoms + 3):
			fcline = linecache.getline('basegeo/fc.z', l)
			conicline = linecache.getline('basegeo/{0}'.format(con), l)
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

def main_2(filename): # for Transoid
	print 'Iterating {0}...'.format(filename)
	confile = filename
	temp = open('temp.txt', 'w')
	temp.write(confile)
	con = confile[0:-2]
	numatoms = int(linecache.getline('basegeo/fc.z', 1))
	#print 'This many atoms: ', numatoms
	for n in range (0, 101):
		outfile = open('itergeo/{0}/{1}.z'.format(con, n), 'w')
		outfile.write(str(numatoms) + '\n')
		outfile.write(confile + '\n')
		for l in range (3, numatoms + 1):
			fcline = linecache.getline('basegeo/fc.z', l)
			conicline = linecache.getline('basegeo/{0}'.format(confile), l)
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
	#		print 'n first loop: ', n
	#		print 'diffx first loop: ', diffx
			outfile.write('\n')
	for n in range (0, 101):
		outfile = open('itergeo/{0}/{1}.z'.format(con, n), 'a')
		for o in range (numatoms + 1, numatoms + 2):
	#####
			fcline1 = linecache.getline('basegeo/fc.z', o)
			conicline1 = linecache.getline('basegeo/{0}'.format(confile), o)
			fcline2 = linecache.getline('basegeo/fc.z', o+1)
			conicline2 = linecache.getline('basegeo/{0}'.format(confile), o+1)
			inatom1 = fcline1.split()[0]
			inatom2 = fcline2.split()[0]
			inr1 = fcline1.split()[1]
			inr2 = fcline2.split()[1]
			intheta1 = fcline1.split()[3]
			intheta2 = fcline2.split()[3]
			inphi1 = fcline1.split()[5]
			inphi2 = fcline2.split()[5]
			fcx1 = float(fcline1.split()[2])
			fcx2 = float(fcline2.split()[2])
			fcy1 = float(fcline1.split()[4])
			fcy2 = float(fcline2.split()[4])
			fcz1 = float(fcline1.split()[6])
			fcz2 = float(fcline2.split()[6])
			cix1 = float(conicline1.split()[2])
			cix2 = float(conicline2.split()[2])
			ciy1 = float(conicline1.split()[4])
			ciy2 = float(conicline2.split()[4])
			ciz1 = float(conicline1.split()[6])
			ciz2 = float(conicline2.split()[6])
			absdiffz1 = ciz2 - fcz1
			absdiffz2 = ciz1 - fcz2
			diffx1 = fcx1 + n*((cix2-fcx1)/100)
			diffx2 = fcx2 + n*((cix1-fcx2)/100)
			diffy1 = fcy1 + n*((ciy2-fcy1)/100)
			diffy2 = fcy2 + n*((ciy1-fcy2)/100)
			diffz1 = fcz1 + n*((ciz2-fcz1)/100)
			if absdiffz1 > 180:
				ciz2 = ciz2 - 360
				diffz1 = fcz1 + n*((ciz2-fcz1)/100)
			if absdiffz1 < -180:
				ciz2 = ciz2 + 360
				diffz1 = fcz1 + n*((ciz2-fcz1)/100)
			diffz2 = fcz2 + n*((ciz1-fcz2)/100)
			if absdiffz2 > 180:
				ciz1 = ciz1 - 360
				diffz2 = fcz2 + n*((ciz1-fcz2)/100)			
			if absdiffz2 < -180:
				ciz1 = ciz1 + 360
				diffz2 = fcz2 + n*((ciz1-fcz2)/100)
			line1 = inatom1 + ' ' + inr1 + ' ' + str(diffx1) + ' ' + intheta1 + ' ' + str(diffy1) + ' ' + inphi1 + ' ' + str(diffz1) + '\n'
			line2 = inatom2 + ' ' + inr2 + ' ' + str(diffx2) + ' ' + intheta2 + ' ' + str(diffy2) + ' ' + inphi2 + ' ' + str(diffz2) + '\n'
			outfile.write(line1)
			outfile.write(line2)
	#		print 'line1: ', line1
	#		print 'line2: ', line2

	#####
		outfile.close()

filename = sys.argv[1]
if filename == 'Transoid.z':
	main_2(filename)
else:
	main_1(filename)


