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

# len(datastructs) = N
# len(membanks) = M
membanks = [30] * 4 + [0] # Last one = external mem
datastructs = [10, 20, 15, 25, 30, 40, 35, 45, 50 , 60]
accesscost = [4] * len(datastructs)

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks))
# Bool that is true of the datastruct is in the membank
X = [[0] * len(membanks)] * len(datastructs)

# Conflicts
penalty = 16
con = [16, 16, 16, 16]
confictstatus = [0, 1, penalty, penalty * 2]


def randomMememex():
	j = 0 # Random variable
	f = 0 # Total cost of allocation
	for i in range(0, len(membanks)):
		cost = 0 # cost per iteration
		while True:
			j = random.randint(0, len(membanks)-1)
			if (cap_used[j] + i <= membanks[j]):
				break
		X[i][j] = 1
		cap_used[j] += datastructs[i]
		# Calculate cost[i][j]
		if i <= len(membanks) - 2:
			cost = accesscost[i]
		f += cost
	# Calculate conflicts cost
	# Calculate external mem cost
	return f


if __name__ == '__main__':
	cost = randomMememex()
	print(cost)
