import random
import sys

# Class containing the whole problem set.
# We can set up the maximum number of elements, and its maximum value.
class MemProblem():
	# [capacitu].
	membanks_max = 0
	membanks_n = 0
	membanks = [0] + [sys.maxint]

	# [[capacity required, access cost]].
	datastructs_max = 0
	datastructs_maxn = 0
	datastructs = []

	# [a, b, cost, conflict status].
	# Status can be any of: {0, 1, penalty, 2*penalty}.
	conflicts_max = 0
	conflicts_n = 0
	conflicts = []

	# Set by the user.
	penalty = -1
	# List that contains the capacity used for each mem bank (optimization).
	cap_used = []
	# Bool that is true if the datastruct is in the membank.
	# [membank][datastruct]
	X = []

	# Class needs the number of datastructs, membanks, and conflicts.
	def __init__(self, seed, dss, mbs, cs):
		self.datastructs_n = dss[0]  
		self.datastructs_max = dss[1]  

		self.membanks_n = mbs[0]
		self.membanks_max = mbs[1]

		self.conflicts_n = cs[0]
		self.conflicts_max = cs[1]

		random.seed(seed)
		self.random_problem()

	# Create a random problem.
	def random_problem(self):
		# We need a value for the penalty.
		if self.penalty == -1:
			self.penalty = random.randint(0, self.membanks_max)
		conflictstatus = [0, 1, self.penalty, self.penalty * 2]

		# Create random membanks.
		self.membanks = [0] * self.membanks_n + [sys.maxint]
		for i in range(0, self.membanks_n):
			self.membanks[i] = { 'capacity': random.randint(0, self.membanks_max) }

		# Create random datastructs.
		self.datastructs = [0] * self.datastructs_n
		for i in range(0, self.datastructs_n):
			self.datastructs[i] = { 'capacity': random.randint(0, self.datastructs_max), 'cost': random.randint(0, self.datastructs_max)] }
			# Access cost.
			self.datastructs[i][1] = random.randint(0, self.datastructs_max)

		# Create random conflicts
		self.conflicts = [0] * self.conflicts_n
		for i in range(0, self.conflicts_n):
			self.conflicts[i] = [0, 0]
			# Conflict cost.
			self.conflicts[i][0] = random.randint(0, self.conflicts_max)
			# Conflict status.
			j = random.randint(0, 3)
			self.conflicts[i][1] = conflictstatus[j]

		self.cap_used = [0] * (len(self.membanks))
		self.X = [[False] * len(self.membanks)] * len(self.datastructs)
	
	# Print solution
	def print_solution(self):
		for row in self.X:
			print row

	# XXX We still need to check it
	def calculate_cost(self):
		cost = 0
		# Data structs cost
		for i in range(0, len(datastructs)):
			for j in range(0, len(X)-2):
				if X[j][i] == True:
					cost += datastructs[i][1]
		# Conflicts cost
		for conf in self.conflicts:
			cost = cost + conf[0] * conf[1]
		# External storage cost
		for i in range(0, len(X[-1])):
			if X[-1][i] == True:
				cost += penalty * datastructs[i]
		return cost

	def cost(self, i, j):
		cost = self.datastructs[i][1] #Access cost of i
		if j == self.membanks_n+1:
			cost *= penalty

		#Loop conflits


#prob = MemProblem(2, [3,5], [4,10], [5,2])
#print "Solution:"
#prob.print_solution()
#print
#print "Memory banks:"
#print prob.membanks
#print "Data structures:"
#print prob.datastructs
#print "Conflicts:"
#print prob.conflicts
#print
