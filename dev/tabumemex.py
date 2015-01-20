#!/usr/bin/env python2
# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]

import random
import sys
import memproblem
from greedyMemex import greedymemex 
from randommemex import randommemex

def initialmemex(p ,A ):
    """Decides on an initial solution for the tabu memex
    Choose between GreedyMemex or Random Memex
    Keyword arguments:
    p -- memproblem object
    a -- bool deciding randomMemex
    Returns a solution with a cost.
    """
    if A:
        return randommemex(p)
    else:
        return greedymemex(p)
    pass


def tabumemex(p, NtMax):
    """Solves the memory allocation problem using tabu search.
    Keyword arguments:
    p -- memproblem object
    NtMax - number of iterations
    Returns a solution with a cost.
    """
    tabList = []
    A = random.randint(0,1)
    # f = current solution cost
    f = ftab = initialmemex( p, A) # initial cost in allocation
    #ftab = sys.float_info.max # f* proposed solution 
    NT = NtMax
    fillTabuList(p.X, tabList)
    Xtab = None # current iteration best solution
    Xbest = None # best solution overall
    iter = 0
    while iter<NT and f>0:
        i, h, j = explore_neighborhood_0(p, tabList)
        f = p.calculate_cost()
        if f < ftab:
            ftab = f
            Xbest =p.X
            tabList.append(str(i)+str(j))
        iter += 1
    return f


def explore_neighborhood_0(p, tabList):
    """Explores the neighborhood of the current solution
    Keyword arguments:
    X -- current solution to expand
    tabList -- current tabu list
    Returns a solution with a cost.
    """
    candidate = "" # candidate to add to the tabu list
    h = None # Current membank for datastruct i
    for i in range(len(p.X)):
        for j in range(len(p.X[i])):
            candidate = str(i)+str(j)
            if not candidate in tabList:
                if p.cap_used[i] + p.datastructs[i]['size'] <= p.membanks[j]['capacity']:
                    h = getCurrentMembank(p.X,i,j)
                    p.X[i][h] = False
                    p.X[i][j] = True
                    p.cap_used[j] += p.datastructs[i]['size']
                    p.cap_used[h] -= p.datastructs[i]['size']
                    return i, h, j
                    pass
                pass
    return i, -1, j

def getCurrentMembank(X, i, j):
    for h in range(len(X[i])):
        if X[i][h] == True:
            return h

def fillTabuList(X, tabList):
    """Fills the tabu list with strings of the current allocations.
    
    Keyword arguments:
    X -- current solution

    Updates the tabu list
    """
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j]==True:
                tabList.append(str(i)+str(j))
            pass
    pass

if __name__ == '__main__':
    for i in range(1,20):
        problem = memproblem.read_problem(sys.argv[1])
        cost = tabumemex(problem, 100)
        print(cost)
