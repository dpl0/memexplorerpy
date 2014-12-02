# N = # Data structures
# M = # Mem Banks
# Si = Size of DS i
# Cj = Capacity of MV
# Ei = Access cost if in memory bank
# Ei*p = access cost if in external mem
# O = # conflicts
# Dk = cost of conflict k
# Dk*p cost of conflict if in external memory
# Yk = State of conflict can be:
#		0 - If a and b DA are in different MB
#		1 - If a and b DA are in the same MB
#		p - If one is in EM
#		2p - If both are in EM
# Xij = Boolean 1 if i in MB j
#
# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]

import random
import sys
import memproblem

def randomMememex(p):
	j = 0 # Random variable
	f = 0 # Total cost of allocation
	for i in range(0, p.datastructs_n):
		while True:
			j = random.randint(0, p.membanks_n - 1)
			if (p.cap_used[j] + p.datastructs[i][0] <= problem.membanks[j]):
				break
		p.X[i][j] = True
		p.cap_used[j] += p.datastructs[i][0]
		# Calculate cost[i][j]
		if j <= len(p.membanks) - 2:
			f += p.datastructs[j][1]
		# in external mem
		if i == len(p.membanks) - 1:
			f += p.datastructs[j][1] * p.penalty
		print(f, i, j)
	print("Total cost so far: ", f)
	# Calculate conflicts cost
	for i in range(0, conflicts_n):
		f += p.conflicts[i][0] * p.conflicts[i][1]
	return f 


if __name__ == '__main__':
	# [number, maximum]
	# seed, datastructs, membanks, conflicts 
	problem = MemProblem(42, [50, 50], [60, 50], [34, 3])
	cost = randomMememex(problem)
	print(cost)
