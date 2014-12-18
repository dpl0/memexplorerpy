def possible_moves(problem):
	current = current_state(problem)
	possibles = []
	for i in range(0, len(problem.datastructs)):
		for j in range(0, len(problem.membanks)):
			if problem.X[i][j] == False:
				remaining_capacity = problem.membanks[j]['capacity']
				for ai in range(0, len(problem.datastructs)):
					if problem.X[ai][j] == True:
						remaining_capacity -= problem.datastructs[ai]['size']
				if remaining_capacity >= problem.datastructs[i]['size']:
					possibles.append({'i': i, 'j': j, 'h': current[i]})
	return possibles

def current_state(problem):
	current = [0] * len(problem.datastructs)
	for i in range(0, len(problem.datastructs)):
		for j in range(0, len(problem.membanks)):
			if problem.X[i][j] == True:
				current[i] = j
	return current

def prune(problem, possibles):
	return [move for move in possibles if problem.cost(move['i'], move['h']) > problem.cost(move['i'], move['j'])]
		
def best_move(problem, possibles):	

	best = None
	for move in possibles:
		if best is None: original_cost = problem.cost(move['i'], move['h'])
		else: original_cost = best['cost']
		cost = problem.cost(move['i'], move['j'])
		if cost < original_cost:
			best = {'move': move, 'cost': cost }
	if best is None: return best
	return best['move']

def explore_neighbourhood_n0(problem):
	return best_move(problem, prune(problem, possible_moves(problem)))