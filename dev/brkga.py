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
	ranking = []

	def __init__(self, dec, n=100, p=1000, pe=0.20, pm=0.10, rhoe=0.70, s=0):
		self.n = n
		self.p = p
		self.pe = pe
		self.pm = pm 
		self.rhoe =rhoe 
		self.dec = dec 
		self.seed = s
		
		self.previous = self.create_population(p, n)
		self.ranking = self.rank_solutions(self.previous)
		return

	# Creates the whole set of population.
	def create_population(self, p, n):
		pop = []
		for i in range(p):
			chrom = self.create_chromosome(n)
			pop.append(chrom)
		return pop
	
	# Each chromosome is a list of random bits.
	def create_chromosome(self, n):
		while True:
			number = random.getrandbits(n)
			chromosome = [True if i == '1' else False for i in bin(number)[2:]]
			while len(chromosome) < n:
				chromosome = [False] + chromosome

			if self.dec(chromosome) != False: return chromosome
		return chromosome

	def rank_solutions(self, pop):
		rank = [(self.dec(p), p) for p in pop]
		rank = sorted(rank)
		return rank

	# Evolve the current population.
	def evolve(self):
		# 6 - Copy elite solutions to next population.
		elite, nonelite = self.getElite(self.pe, len(self.ranking))
		# 7 - Generate mutant solutions.
		mutants = self.mutate(self.pm, self.previous)
		# 8 - Crossover
		crossover = self.crossover(self.rhoe, elite, nonelite, self.p-len(elite)-len(mutants))
		self.previous = elite + crossover + mutants
		self.ranking = self.rank_solutions(self.previous)
		return

	# return elite, nonelite
	def getElite(self, pe, poplen):
		eltotake = int(poplen * pe)
		elite = self.ranking[:eltotake]
		nonelite = self.ranking[eltotake:]
		
		# Take out of rank.
		cleanelite = [i[1] for i in elite]
		cleannonelite = [i[1] for i in nonelite]
		return cleanelite, cleannonelite

	# Mutate p% elements of pop.
	def mutate(self, p, pop):
		mutants = []
		for i in range(len(pop)):
			if random.random() <= p:
				while True:
					for j in pop[i]:
						for k in pop[j]:
							if random.random() <= 0.5:
								rand = random.random()
								if rand <= 0.5:
									pop[j][k] = False
								else: pop[j][k] = True
					if self.dec(pop[i]) != False: break
				mutants.append(pop[i])
		return mutants

	# Crossover the specified number of elements.
	# Returns the created elements.
	def crossover(self, rhoe, elite, nonelite, elems):
		ret = []
		for i in range(elems):
			while True:
				ei = random.randint(0, len(elite)-1)
				ni = random.randint(0, len(nonelite)-1)
				newm= []
				for i in range(len(elite[ei])):
					if random.random() <= rhoe: newm.append(elite[ei][i])
					else: newm.append(nonelite[ni][i])
				if self.dec(newm) != False:
					ret.append(newm)
					break
		return ret
	
	def bestSolution(self):
		return self.ranking[0]


# Takes a chromosome as input.
# Returns it fitness (cost of the problem).
def decoder(ch):
	matrixlen = len(problem.X)
	rowlen = len(problem.X[0])

	matrix = [[ch[i*rowlen+j] for j in range(rowlen)] for i in range(matrixlen)]

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
	generations = 1000

	brkgasolver = brkga(dec=decoder, n=matrix_len(problem.X))

	for i in range(generations):
		brkgasolver.evolve()
	a = brkgasolver.bestSolution()
	print a

