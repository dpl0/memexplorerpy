#!/usr/bin/env python2
import sys, time, timeit

sys.path.append("../dev/")
import brkga, grasp, memproblem, tabumemex

def get_code(mh, filename, iters, pars):
	"""Creates code templates using parameters."""
	if mh == 'grasp':
		command = "print grasp(problem,1,"+str(iters)+")"
		code = """ 
import memproblem
from grasp import grasp

problem = memproblem.read_problem('"""+filename+"""')
"""
		return command, code

	elif mh == 'tabu':
		command = "print cost"
		code = """
import memproblem
import tabumemex

problem = memproblem.read_problem('"""+filename+"""')
cost = tabumemex.tabumemex(problem, 100)
"""
		return command, code

	elif mh == 'brkga':
		command = "print brk.bestSolution(problem,1,"+str(iters)+").results"
		command = "print brkgasolver.bestSolution()"
		code = """
import memproblem, brkga

problem = memproblem.read_problem('"""+filename+"""')
brkgasolver = brkga.brkga(n=problem.datastructs_n, p=20, s=time.time(), dec=brkga.decoder)
for i in range("""+str(iters)+"""):
	brkgasolver.evolve()
"""
		return command, code

	else:
		return None, None

class execute():
	"""Execute the problems with the different metaheuristics."""
	def __init__(self, problem, iters):
		self.iters = iters
		self.problem = problem
		self.repeats = 4
		return
	
	def run_grasp(self, filename, pars=None):
		print("GRASP ("+str(self.iters)+")")

		command, code = get_code('grasp', filename, self.iters, pars)

		grasp_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(grasp_time/self.repeats))
		return
	
	def run_tabu(self, filename, pars=None):
		print("Tabu Search ("+str(self.iters)+")")

		command, code = get_code('tabu', filename, self.iters, pars)
		tabu_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(tabu_time/self.repeats))
		return
	
	def run_brkga(self, filename, pars=None):
		print("BRKGA ("+str(self.iters)+")")

		command, code = get_code('grasp', filename, self.iters, pars)
		brkga_time = timeit.timeit(command, code, number=self.repeats)
		print("Avg execution time: "+str(brkga_time/self.repeats))
		return


if __name__ == "__main__":
	fname = sys.argv[1]
	problem = memproblem.read_problem(fname)
	# Iters: iterations for GRASP, tabu memex, brkga. 
	iters = int(sys.argv[2])
	executor = execute(problem, iters)
	
	executor.run_grasp(fname)
	executor.run_tabu(fname)
	executor.run_brkga(fname)
