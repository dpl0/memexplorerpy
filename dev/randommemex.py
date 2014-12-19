# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]

import random
import sys
import memproblem

def randommemex(p):
	cost = 0
	for i in range(0, p.datastructs_n):
		j = 0
		while p.cap_used[i] + p.datastructs[i]['size'] > p.membanks[j]['capacity']:
			j = random.randint(0, p.membanks_n)
		p.X[i][j] = True
		if j <= len(p.cap_used):
			p.cap_used[j] += p.datastructs[i]['size']
		# Calculate cost (not for conflicts).
		cost += p.calculate_cost()
	return cost



if __name__ == '__main__':
    # [number, maximum]
    # seed, datastructs, membanks, conflicts 
    problem = memproblem.read_problem("./test.dat")
    cost = randommemex(problem)
    print(cost)
