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

datastructs = 200 # data structures
membanks = 300 # mem banks
conflicts =  4 # conflicts

cap_used = [0] * (membanks + 1)		# u_j >  capacity used <list>
cap_ds = [0] * datastructs			# s_i  capacity of data structure
cap_mb = [0] * (membanks + 1)		# c_i  capacity of memory bank
X = [[0] * (membanks  +1)] * datastructs	# x_ij > list of lists 
cost = [[0]  * (membanks + 1)] * datastructs	# g_ij > Cost


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
	print("Running!")
	randomMememex()
