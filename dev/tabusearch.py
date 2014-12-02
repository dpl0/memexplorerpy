# len(datastructs) = N
# len(membanks) = M
membanks = [30] * 4 + [0] # Last one = external mem
datastructs = [10, 20, 15, 25, 30, 40, 35, 45, 50 , 60]
accesscost = [4] * len(datastructs)

# List that contains the capacity used for each mem bank
cap_used = [0] * (len(membanks))
# Bool that is true of the datastruct is in the membank
X = [[0] * len(membanks)] * len(datastructs)

penalty = 16
# Conflicts: {cost, status}
conflicts = [[16, 0], [16, 1], [16, penalty], [16, penalty * 2]]

def TabuSearch(X, k, a, nTabu, nIterations):
	iterations = 0;
	tabuList = new TabuList(nTabu);
	while iterations < nIterations:
		no_op = 0;
		nIterations += 1;

