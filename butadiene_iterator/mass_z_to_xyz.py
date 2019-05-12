import sys
import xyz_matrix_maker
import shutil
import progressbar
import os

geom = sys.argv[1][:-2]
print "Converting {0} frames from z to xyz...".format(geom)
for frame in progressbar.progressbar(range(101)):
	source_file = 'iterations/{0}/{1}.z'.format(geom, frame)
	shutil.copy(source_file, '{0}.z'.format(geom))
	xyz_matrix_maker.main('{0}.z'.format(geom))
	shutil.move('results/{0}.xyz'.format(geom), 'iterations/{0}/{1}.xyz'.format(geom, frame))
os.remove('{0}.z'.format(geom))
