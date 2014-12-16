def possible_moves(problem, i):
	possibles = []
	for j in range(0, len(problem.membanks)):
		if problem.X[i][j] == False:
			remaining_capacity = problem.membanks[j]['capacity']
			for ai in range(0, len(problem.datastructs)):
				if problem.X[ai][j] == True:
					remaining_capacity = problem.datastructs[ai]['size']
			if remaining_capacity >= problem.datastructs[i]['size']:
				possibles.append(j)
	return possibles

def explore_neighbourhood_n0(problem):
	None