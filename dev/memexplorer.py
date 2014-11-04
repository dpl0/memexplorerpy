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

N = 200 # data structures
M = 300 # mem banks
O =  4 # conflicts

u = [0]*(M+1) # u_j >  capacity used <list>
s = [0]*(N) # s_i  capacity of data structure
c = [0]*(M+1) # c_i  capacity of memory bank
X = [[0]*(M+1)]*N # x_ij > list of lists 
g = [[0]*(M+1)]*N # g_ij > Cost


def randomMememex():
	f = 0 # Total cost of allocation
	j = 0 # Random variable
	lu = len(u)
	lc = len(c)
	for i in s:
		while True:
			#j = random.randint(1, M+1)
			for j in range(1, M+2):
				print "size %d %d   length: %d %d "%(i,j,lu,lc)
				
				if (u[j] + i <= c[j]):
					continue
					break
		X[i][j] = 1
		u[j] += s[i]
		#XXX Calculate g[i][j] (cost)
		f += g[i][j]
	return f


if __name__ == '__main__':
	print("Running!")
	randomMememex()
