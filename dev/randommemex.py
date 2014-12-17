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
		while p.cap_used[j] + p.datastructs[i][0] > problem.membanks[j]:
			j = random.randint(0, p.membanks_n - 1)
		p.X[i][j] = True
		p.cap_used[j] += p.datastructs[i][0]
		# Calculate cost[i][j]
		if j <= len(p.membanks) - 2:
			f += p.datastructs[j][1]
		# in external mem
		if i == len(p.membanks) - 1:
			f += p.datastructs[j][1] * p.penalty
	# Calculate conflicts cost
	for i in range(0, conflicts_n):
		f += p.conflicts[i][0] * p.conflicts[i][1]
	return f

if __name__ == '__main__':
	# [number, maximum]
	# seed, datastructs, membanks, conflicts 
	problem = memproblem.read_problem("./test.dat")
	cost = randomMememex(problem)
	print(cost)
