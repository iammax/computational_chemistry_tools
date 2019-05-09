import numpy as np
from eri_reader import main as eri_reader

enuc = 8.002367061810450

#function to read in diagonal matrices
def matrix_read(file_name, numfuncs):
	matrix = np.zeros([numfuncs, numfuncs])
	infile = open(file_name, 'r')
	lines = infile.readlines()
	infile.close()
	for line in lines:
		i, j, value = line.split()
		i = int(i)-1
		j = int(j)-1
		value = float(value)
		matrix[i][j] = value
		matrix[j][i] = value
	return matrix

def matrix_print(matrix):
	numrows = len(matrix)
	for i in range (numrows):
		line = ''
		for j in range (numrows):
			line += str(matrix[i][j]) + ' '
		print line

def G_maker(D, ERIs):
	matrix = np.zeros([numfuncs, numfuncs])
	for mu in range (numfuncs):
		for nu in range (numfuncs):
			total = 0
			for l in range (numfuncs):
				for sigma in range (numfuncs):
					J = ERIs[mu][nu][l][sigma]
					K = ERIs[mu][l][nu][sigma]
					Dpart = D[l][sigma]
					total += (Dpart*(J + J - K))
			matrix[mu][nu] = total
	return matrix
numfuncs = 7
num_occupied = 5
S = matrix_read("S.dat", numfuncs)
T = matrix_read("T.dat", numfuncs)
V = matrix_read("V.dat", numfuncs)
H = T + V
ERIs = eri_reader(numfuncs, "ERIs.dat")

eigenvalues, eigenvectors = np.linalg.eig(S)

diag_eigenvalues = np.diag(eigenvalues**-.5)

X = eigenvectors.dot(diag_eigenvalues).dot(eigenvectors.T)

guess_fock = X.T.dot(H).dot(X)
e, ortho_C = np.linalg.eig(guess_fock)
order = e.argsort()
e = e[order]
ortho_C = ortho_C[:,order]
C = X.dot(ortho_C)
D = np.zeros([numfuncs, numfuncs])

for mu in range (numfuncs):
	for nu in range (numfuncs):
		total = 0
		for m in range (num_occupied):
			total += (C[mu][m]*C[nu][m])
		D[mu][nu] = total

eelec = 0
for mu in range (numfuncs):
	for nu in range (numfuncs):
		eelec += (D[mu][nu]* (H[mu][nu]*2))

etotal = eelec + enuc

print "Initial scf electronic energy: ", eelec

converged = False
iter_count = 0
max_iters = 500


print "iter              etotal"
while converged == False:
	previous_energy = etotal
	G = G_maker(D, ERIs)
	F = H + G
#	matrix_print(F)
	Fprime = X.T.dot(F).dot(X)
	e, ortho_C = np.linalg.eig(Fprime)
	order = e.argsort()
	e = e[order]
	ortho_C = ortho_C[:,order]
	C = X.dot(ortho_C)
	D = np.zeros([numfuncs, numfuncs])
	for mu in range (numfuncs):
		for nu in range (numfuncs):
			total = 0
			for m in range (num_occupied):
				total += (C[mu][m]*C[nu][m])
			D[mu][nu] = total

	eelec = 0
	for mu in range (numfuncs):
		for nu in range (numfuncs):
			eelec += (D[mu][nu]* (H[mu][nu]+F[mu][nu]))
	etotal = eelec + enuc
	iter_count += 1
	print "{0}               {1}".format(iter_count, etotal)
	if abs(etotal - previous_energy) < 10e-8:
		converged = True
		print "Converged!"
	if iter_count == max_iters:
		converged = True
		print "Max iters"
