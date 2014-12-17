# ##
# AMMM Project
# Greedy Memex
# 
# Memory allocation Problem.
# 
# 
# ##
# A = [1...N] #Permutation of the set {1..N} that models data structures, 
# used for generating different solutions.
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
##### *************** BOTAS PICUUDAS WOOOOOOOOOOO *****************
#        ,---.
#       |:  ,+--.
#       |: |:  \|
#       |: |: >=|
#       |: |:  /|
#       |`.|:  _(
#       (_ |`._)``.
#        `=(_      `.________
#           `=='`------------'     hjw
#*****************************************************************

import random
from random import shuffle # used to permutate for A
from sys import float_info # used to generate a very large number



# len(datastructs) = N
# len(membanks) = M
membanks = [30] * 4 + [0] # Last one = external mem
datastructs = [10, 20, 15, 25, 30, 40, 35, 45, 50 , 60]
accesscost = [4] * len(datastructs)

#input
inputA = datastructs
shuffle(inputA)
#print inputA

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks)) # U_j
# Bool that is true of the datastruct is in the membank
X = [[0] * len(membanks)] * len(datastructs)

# Conflicts
penalty = 16
con = [16, 16, 16, 16]
confictstatus = [0, 1, penalty, penalty * 2]

def greedyMememex():
	j = 0 # Random variable
	f = 0 # Total cost of allocation
	h = float_info.max #auxiliary variable for the partial greedy solution
	
	for i in range(0, len(datastructs)-1):
		cost = 0 # cost per iteration
		for j in range(0, len(membanks)):
			#j = random.randint(0, len(membanks)-1)
			if (cap_used[j] + inputA[i] <= membanks[j]):
				# Calculate cost[i][j]
				# there are several types of costs
				# depending on what where is our data structure, is the difference on what we're having as a cost, cost J.
				cost = accesscost[i]
				
				if 
				
		X[i][j] = 1
		cap_used[j] += datastructs[i]
		f += cost + h
	# Calculate conflicts cost
	# Calculate external mem cost
	return f


if __name__ == '__main__':
	cost = randomMememex()
	print(cost)
