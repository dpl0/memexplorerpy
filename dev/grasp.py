#!/usr/bin/env python2
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

def local(problem):
	move = explore.explore_neighbourhood_n0(problem)
	while move is not None:
		problem.X[move['i']][move['h']] = False
		problem.X[move['i']][move['j']] = True
		problem.update_conflicts()
		move = explore.explore_neighbourhood_n0(problem)


def grasp(problem, alpha, maxiter):
	solutions = []
	cost = sys.maxint
	best_solution = problem
	for i in range(0, maxiter):
		current_problem = problem.copy()
		construct(current_problem, alpha)
		local(current_problem)
		current_cost = current_problem.calculate_cost()
		if cost > current_cost:
			cost = current_cost
			best_solution = current_problem
		if i%50 == 0:
			solutions.append(cost);
	solutions.append(cost)
	return solutions


if __name__ == "__main__":
	prob = memproblem.read_problem(sys.argv[1])
	print grasp(prob, 1, 10)
