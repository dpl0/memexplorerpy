import sys, time, timeit
import memproblem

import grasp, brkga, tabumemex

class execute():
	"""Execute the problems with the different metaheuristics."""
	def __init__(self, problem, iters):
		self.iters = iters
		self.problem = problem
		return
	
	def run_grasp(self, pars=None):
		print("GRASP ("+str(self.iters)+")")
		grasp_time = timeit.timeit('resultsFile.write("{result}".format(result=grasp(problem, 1, 100).results()))','''
import memproblem
from grasp import grasp

problem = memproblem.read_problem(sys.argv[1])
resultsFile = open("./results.data", "a")
''', number=self.iters)
		print "Average execution time: {time}".format(time=grasp_time/self.iters)
		return
	
	def run_tabu(self, pars=None):
		print("Tabu Search ("+str(self.iters)+")")
		return
	
	def run_brkga(self, pars=None):
		print("BRKGA ("+str(self.iters)+")")

		brkga_time = timeit.timeit("print", """
import memproblem, brkga

problem = memproblem.read_problem(sys.argv[1])
brkgasolver = brkga.brkga(n=problem.datastructs_n, p=20, s=time.time(), dec=brkga.decoder)
for i in range("""+str(self.iters)+"""):
	brkgasolver.evolve()
	print brkgasolver.bestSolution()""", number=1)
		return


if __name__ == "__main__":
	# Iters = iterations for GRASP, iterations for tabu memex, evolutions
	# for BRKGA.
	iters = int(sys.argv[2])
	problem = memproblem.read_problem(sys.argv[1])
	executor = execute(problem, iters)
	
	executor.run_grasp()
	executor.run_tabu()
	param = {'n':problem.datastructs_n,
			'p':20, 's':time.time(),
			'dec':brkga.decoder}
	executor.run_brkga()
