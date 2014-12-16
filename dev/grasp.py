import memproblem
import sys
import random
import explore


def candidates(problem, i):
	candidates = []
	for j in range(0, len(problem.membanks)):
		remaining_capacity = problem.membanks[j]['capacity']
		for ai in range(0, len(problem.X)):
			if problem.X[ai][j] == True:
				remaining_capacity -= problem.datastructs[ai]['size']
		if remaining_capacity >= problem.datastructs[i]['size']:
			candidates.append(j)
	return candidates

def RCL(problem, candidates, alpha, i):
	costs = []
	min_cost = sys.maxint
	max_cost = 0 #Cost is never negative
	for j in candidates:
		cost = problem.cost(i, j)
		if min_cost > cost:
			min_cost = cost
		if max_cost < cost:
			max_cost = cost
		costs.append(cost)
	cut = min_cost + alpha * (max_cost - min_cost)
	return [x for (x, c) in zip(candidates, costs) if c <= cut]

def construct(problem, alpha):
	for i in range(0, len(problem.datastructs)):
		C = candidates(problem, i)
		rcl = RCL(problem=problem, candidates=C, alpha=alpha, i = i)
		j = rcl[random.randint(0, len(rcl)-1)]
		problem.X[i][j] = True
	problem.update_conflicts()

if __name__ == "__main__":
	prob = memproblem.read_problem('test.dat')
	construct(prob, 0)
	prob.print_solution()
	print explore.possible_moves(prob, 0)