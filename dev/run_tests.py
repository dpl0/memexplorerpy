import sys
import memproblem
import timeit
from grasp import grasp


if __name__ == "__main__":
	
		iters = int(sys.argv[2])
		problem = memproblem.read_problem(sys.argv[1])

		print "Executing grasp {iterations} times, printing results...".format(iterations=iters)

		grasp_time = timeit.timeit('grasp(problem, 1, 1000)','''
from grasp import grasp
import memproblem

problem = memproblem.read_problem(sys.argv[1])
''', number=iters)
		print "Average execution time: {time}".format(time=grasp_time/iters)

		best_solution = sys.maxint
		worst_solution = 0
		solutions = [0] * 21
		for j in range(0, iters):
			sol = grasp(problem, 1, 1000)
			for i in range(0, len(solutions)):
				solutions[i] += sol[i]
				if best_solution > sol[-1]:
					best_solution = sol[-1]
				if worst_solution < sol[-1]:
					worst_solution = sol[-1]

		for i in range(0, len(solutions)):
			solutions[i] /= iters

		print solutions
		
		