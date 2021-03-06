# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]
#	gij = [[]]
#	b
#	h big index to save the best solution for j so far.

import random
import sys
import memproblem

def greedymemex(p):
    f = 0 # total cost in allocation
    g = 0
    a = random.sample(range(0,p.datastructs_n), p.datastructs_n)
    # <g_ij> cost of allocating data a_i in membank_js
    g = [[g for x in xrange(p.membanks_n+1)] for y in xrange(p.datastructs_n)]
    for i in range(0, p.datastructs_n):
        b = 0 # save best j for i
        h= sys.float_info.max
        for j in range(0,p.membanks_n):
            if p.cap_used[j] + p.datastructs[a[i]]['size'] < p.membanks[j]['capacity']:
                g[i][j] = p.cost(i,j)#cost of allocating this datastruct
                if g[i][j] < h:
                   b = j
                   h = g[i][j]
                pass
            pass
        pass
        p.X[a[i]][b] = True
        p.cap_used[b] = p.cap_used[b] + p.datastructs[a[i]]['size']
        f = f + h
    return f


if __name__ == '__main__':
    problem = memproblem.read_problem("./test.dat")
    cost = greedymemex(problem)
    print(cost)