import memproblem
import random
from math import floor

# 1 - Generate p chromosomes of solution.
# 2 - Decode them and test fitness.
# 3 - If the stopping rule is given, return best solution.
# 4 - Sort by fitness.
# 5 - Classify by fitness.
# 6 - Copy elite solutions to next population.
# 7 - Generat mutant solutions.
# 8 - Crossover
# 9 - Goto 2
class brkga:
	# Number of genes in each chromosome.
	n = 0
	# Number of elements in each population.
	p = 0
	# Percent of elite items into each population.
	pe = 0
	# Percent of mutants introduced at each generation into the population.
	pm = 0
	# Probability that an offspring inherits the allele of its elite parent.
	rhoe = 0
	# Seed for PRNG.
	seed = 0
	# Decoder function.
	dec = 0

	# Populations
	previous = []
	current = []

	# Auxiliar function.
	def clear_rank(self, pop):
		return [i[1] for i in pop]
		

	def __init__(self, dec, n=100, p=1000, pe=0.20, pm=0.10, rhoe=0.70, s=0):
		self.n = n
		self.p = p
		self.pe = pe
		self.pm = pm 
		self.rhoe =rhoe 
		self.decoder = dec 
		self.seed = s
		
		self.current = self.create_population(p, n)
		self.previous = list(self.current)
		return

	# Creates the whole set of population.
	def create_population(self, p, n):
		return sorted([self.create_chromosome(n) for i in range(p)])
	
	# Each chromosome is a list of random bits.
	# They have to be correct.
	def create_chromosome(self, n):
		while True:
			number = random.getrandbits(n)
			chrom = [True if i == '1' else False for i in bin(number)[2:]]
			while len(chrom) < n:
				chrom = [False] + chrom

			rankedchrom = (self.decoder(chrom), chrom)
			if rankedchrom[0] != False:
				return rankedchrom

	# Evolve the current population.
	def evolve(self):
		elite, nonelite = self.getElite()
		mutants = self.mutate()

		cossoverelem = self.p - len(elite) - len(mutants)
		crossover = self.crossover(elite, nonelite, cossoverelem)

		self.current = sorted(elite + crossover + mutants)
		self.previous = list(self.current)
		return

	# return elite, nonelite
	def getElite(self):
		eltotake = int(self.n * self.pe)
		elite = self.previous[:eltotake]
		nonelite = self.previous[eltotake:]
		return elite, nonelite

	# Mutate p% elements of pop at random.
	def mutate(self):
		mutants = []
		for i in range(self.p):
			if random.random() < self.pm:
				mutants.append(self.create_mutant(i))
		return mutants
	
	def create_mutant(self, index):
		while True:
			mutant = []
			for v in self.previous[index][1]:
				if random.random() <= 0.5:
					mutant.append(not v)
				else: mutant.append(v)

			ret = (self.decoder(mutant), mutant)
			# Check correctness of chromosome.
			if ret[0] != False:
				return ret

	# Crossover the specified number of elements.
	# Returns the created elements.
	def crossover(self, elite, nonelite, elems):
		ret = []
		for i in range(elems):
			while True:
				ei = random.randint(0, len(elite)-1)
				ni = random.randint(0, len(nonelite)-1)

				newelem = []
				for i in range(self.n):
					if random.random() <= self.rhoe:
						newelem.append(elite[ei][1][i])
					else: newelem.append(nonelite[ni][1][i])
				rankedelem = (self.decoder(newelem), newelem)
				if rankedelem[0] != False:
					ret.append(rankedelem)
					break
		return ret

	def bestSolution(self):
		return self.current[0]

# Takes a chromosome as input.
# Returns False if the solution is unfeasible, or its cost.
def decoder(ch):
	matrixlen = len(problem.X)
	rowlen = len(problem.X[0])

	#matrix = [[ch[i*rowlen+j] for j in range(rowlen)] for i in range(matrixlen)]
	matrix = []
	for i in range(matrixlen):
		row = []
		for j in range(rowlen):
			row.append(ch[i*rowlen + j])
		matrix.append(row)

	problem.X = matrix
	if problem.is_correct():
		return problem.calculate_cost()
	else: return False

def matrix_len(matrix):
	a = 0
	for i in matrix:
		for j in i:
			a += 1
	return a


# Problem object is needed by the decoder.
problem = memproblem.read_problem("./test.dat")

if __name__ == "__main__":
	generations = 500

	brkgasolver = brkga(dec=decoder, n=matrix_len(problem.X), p=10)

	for i in range(generations):
		brkgasolver.evolve()
	print brkgasolver.bestSolution()

