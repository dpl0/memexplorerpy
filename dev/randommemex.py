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

# *************** BOTAS PICUUDAS WOOOOOOOOOOO *****************
#        ,---.
#       |:  ,+--.
#       |: |:  \|
#       |: |: >=|
#       |: |:  /|
#       |`.|:  _(
#       (_ |`._)``.
#        `=(_      `.________
#           `=='`------------'     hjw
#**************************************************************

import random
import sys

# len(datastructs) = N
# len(membanks) = M
membanks = [80] * 4 + [sys.maxint] # Last one = external mem
# [space, access cost]
datastructs = [[60, 4], [40, 4],
			   [35, 4], [25, 4],
			   [30, 4], [40, 4],
			   [35, 4], [45, 4],
			   [50, 4], [60, 4]]

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks))
# Bool that is true of the datastruct is in the membank
X = [[False] * len(membanks)] * len(datastructs)

penalty = 16
# Conflicts: {cost, conflict status}
conflicts = [[16, 0], 
			 [16, 1], 
			 [16, penalty],
			 [16, penalty * 2]]

def randomMememex():
	j = 0 # Random variable
	f = 0 # Total cost of allocation
	for i in range(0, len(datastructs)):
		while True:
			j = random.randint(0, len(membanks)-1)
			if (cap_used[j] + datastructs[i][0] <= membanks[j]):
				break
		X[i][j] = True
		cap_used[j] += datastructs[i][0]
		# Calculate cost[i][j]
		if j <= len(membanks) - 2:
			f += datastructs[j][1]
		# in external mem
		if i == len(membanks) - 1:
			f += datastructs[j][1] * penalty
		print(f, i, j)
	print("Total cost so far: ", f)
	# Calculate conflicts cost
	for i in range(0, len(conflicts)):
		f += conflicts[i][0] * conflicts[i][1]
	return f 


if __name__ == '__main__':
	cost = randomMememex()
	print(cost)
