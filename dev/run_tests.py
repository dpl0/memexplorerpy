import sys
import memproblem
import timeit
from grasp import grasp


if __name__ == "__main__":
	
	if sys.argv[1] == "create":
	
		make_seed = lambda: int(round(time.time() * 1000)) 
		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=5, 
			mem_min=1, 
			mem_max=10, 
			mem_n=4, 
			c_min=1, 
			c_max=5, 
			c_n=8, 
			p_min=1, 
			p_max=1).write_file('memex_small_problem_small_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=5, 
			mem_min=1, 
			mem_max=10, 
			mem_n=4, 
			c_min=1, 
			c_max=5, 
			c_n=8, 
			p_min=20, 
			p_max=50).write_file('memex_small_problem_big_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=5, 
			mem_min=1, 
			mem_max=10, 
			mem_n=4, 
			c_min=1, 
			c_max=5, 
			c_n=8, 
			p_min=5, 
			p_max=20).write_file('memex_small_problem_med_p.dat')

	#Med problems

		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=20, 
			mem_min=1, 
			mem_max=10, 
			mem_n=8, 
			c_min=1, 
			c_max=5, 
			c_n=16, 
			p_min=1, 
			p_max=1).write_file('memex_med_problem_small_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=20, 
			mem_min=1, 
			mem_max=10, 
			mem_n=8, 
			c_min=1, 
			c_max=5, 
			c_n=16, 
			p_min=20, 
			p_max=50).write_file('memex_med_problem_big_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=20, 
			mem_min=1, 
			mem_max=10, 
			mem_n=8, 
			c_min=1, 
			c_max=5, 
			c_n=16, 
			p_min=5, 
			p_max=20).write_file('memex_med_problem_med_p.dat')

	#Big problems

		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=50, 
			mem_min=1, 
			mem_max=10, 
			mem_n=20, 
			c_min=1, 
			c_max=5, 
			c_n=40, 
			p_min=1, 
			p_max=1).write_file('memex_big_problem_small_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=50, 
			mem_min=1, 
			mem_max=10, 
			mem_n=20, 
			c_min=1, 
			c_max=5, 
			c_n=40, 
			p_min=20, 
			p_max=50).write_file('memex_big_problem_big_p.dat')


		memproblem.random_problem(seed=make_seed(), 
			dss_min=1, 
			dss_max=5, 
			dsc_min=1, 
			dsc_max=10, 
			ds_n=50, 
			mem_min=1, 
			mem_max=10, 
			mem_n=20, 
			c_min=1, 
			c_max=5, 
			c_n=40, 
			p_min=5, 
			p_max=20).write_file('memex_big_problem_med_p.dat')

	else:
		iters = int(sys.argv[2])
		problem = memproblem.read_problem(sys.argv[1])

		print "Executing grasp {iterations} times, printing results...".format(iterations=iters)

		grasp_time = timeit.timeit('resultsFile.write("{result}".format(result=grasp(problem, 1, 100).results()))','''
from grasp import grasp
import memproblem

problem = memproblem.read_problem(sys.argv[1])
resultsFile = open("/home/obzzidian/results.data", "a")
''', number=iters)
		print "Average execution time: {time}".format(time=grasp_time/iters)
