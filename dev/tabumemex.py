#!/usr/bin/env python2
# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]

import random
import sys
import memproblem
import grasp
import explore

def tabumemex(p, NtMax):
    """Solves the memory allocation problem using tabu search.
    Keyword arguments:
    p -- memproblem object
    NtMax - number of iterations
    Returns a solution with a cost.
    """

    p = p.copy()
    grasp.construct(p, 0)
    results = []

    tabList = []

    NT = NtMax
    iter = 0
    while iter<NT:
        move = None

        if iter%2 == 0:
            move = explore.explore_neighbourhood_n1(p, tabList)
        else:
            move = explore.explore_neighbourhood_n2(p, tabList)

        if len(tabList) > 5:
            tabList = tabList[1:-1]

        if iter % 50 == 0:
            results.append(p.calculate_cost())

        iter += 1

    results.append(p.calculate_cost())
    return results