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
#******************************************************************
import random

datastructs = [10, 20, 15, 25, 30, 40, 35, 45, 50 , 60]
accesscost = [4] * len(datastructs)
capacity = [30] * 4
penalty = 16
conflictcost = 16

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks) + 1)
# Bool that is true of the datastruct is in the membank
X = [[0] * (len(membanks)  +1)] * len(datastructs)

def randomMememex():
	f = 0 # Total cost of allocation
	j = 0 # Random variable
	lu = len(cap_used)
	lc = len(cap_mb)
	for i in cap_ds:
		while True:
			#j = random.randint(1, M+1)
			for j in range(1, membanks + 2):
				if (cap_used[j] + i <= cap_mb[j]):
					break
		X[i][j] = 1
		cap_total[j] += cap_ds[i]
		#XXX Calculate cost[i][j]
		f += cost[i][j]
	return f


if __name__ == '__main__':
	randomMememex()
