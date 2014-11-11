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

# len(datastructs) >>> N
# len(membanks) >>> M
membanks = [30] * 4
datastructs = [10, 20, 15, 25, 30, 40, 35, 45, 50 , 60]
accesscost = [4] * len(datastructs)
penalty = 16
conflictcost = 16

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks) + 1)
# Bool that is true of the datastruct is in the membank
X = [[0] * (len(membanks)  +1)] * len(datastructs)


def randomMememex():
	cost = [[0] * (len(membanks)  +1)] * len(datastructs)
	j = 0 # Random variable
	f = 0 # Total cost of allocation
	for i in range(0, len(membanks)):
		while True:
			j = random.randint(0, len(membanks)-1)
			if (cap_used[j] + i <= membanks[j]):
				break
		X[i][j] = 1
		cap_used[j] += datastructs[i]
		#XXX Calculate cost[i][j]
		f += cost[i][j]
	return f


if __name__ == '__main__':
	randomMememex()
