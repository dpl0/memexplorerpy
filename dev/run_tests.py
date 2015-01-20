#!/usr/bin/env python2
import sys, time, timeit

sys.path.append("../dev/")
import brkga, grasp, memproblem, tabumemex

def get_grasp_code(filename, iters):
	"""Creates code templates."""
	command = "print grasp(problem,1,"+str(iters)+")"
	code = """ 
import memproblem
from grasp import grasp

problem = memproblem.read_problem('"""+filename+"""')
"""
	return command, code

def get_tabu_code(filename, iters):
	command = "print tabumemex.tabumemex(problem, "+str(iters)+")"
	code = """
import memproblem
import tabumemex

problem = memproblem.read_problem('"""+filename+"""')
"""
	return command, code

def get_brkga_code(filename, iters):
	command = """
n = problem.datastructs_n
s = time.time()
# 20 is population size.
brkgasolver = brkga.brkga(problem, brkga.decoder, n, 20, s)
for i in range("""+str(iters)+"""):
	brkgasolver.evolve()
print brkgasolver.bestSolution()[0]
"""

	code = """
import memproblem, brkga

problem = memproblem.read_problem('"""+filename+"""')
"""
	return command, code

class execute():
	"""Execute the problems with the different metaheuristics."""
	def set_problem(self, prob):
		self.problem = prob

	def __init__(self, iters, rep=4):
		self.iters = iters
		self.repeats = rep
		return
	
	def run_grasp(self, filename, prob=None):
		self.set_problem(prob)
		print("GRASP ("+filename+", "+str(self.iters)+")")
		command, code = get_grasp_code(filename, self.iters)
		exec_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(exec_time/self.repeats))
		return
	
	def run_tabu(self, filename, prob=None):
		self.set_problem(prob)
		print("Tabu Search ("+filename+", "+str(self.iters)+")")
		command, code = get_tabu_code(filename, self.iters)
		exec_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(exec_time/self.repeats))
		return
	
	def run_brkga(self, filename, prob=None):
		self.set_problem(prob)
		print("BRKGA ("+filename+", "+str(self.iters)+")")
		command, code = get_brkga_code(filename, self.iters)
		exec_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(exec_time/self.repeats))
		return


if __name__ == "__main__":
	iters = int(sys.argv[1])
	fnames = sys.argv[2:]

	executor = execute(iters)

	for fname in fnames:
		problem = memproblem.read_problem(fname)
		executor.run_grasp(fname, problem)
		executor.run_tabu(fname, problem)
		executor.run_brkga(fname, problem)
		print 
