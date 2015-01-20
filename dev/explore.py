import random


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


def possible_moves_break(problem):
	current = current_state(problem)
	possibles = []
	for i in range(0, len(problem.datastructs)):
		for j in range(0, len(problem.membanks)):
			if problem.X[i][j] == False:
				possibles.append({'i': i, 'j': j, 'h': current[i]})
	return possibles

def possible_moves_fix(problem, h):
	current = current_state(problem)
	possibles = []
	broken_cap = 0
	for i in range(0, len(problem.datastructs)):
		if problem.X[i][h] == True:
			broken_cap += problem.datastructs[i]['size']

	for i in range(0, len(problem.datastructs)):
		if problem.X[i][h] == True:
			for j in range(0, len(problem.membanks)):
				if problem.X[i][j] == False:
					remaining_capacity = problem.membanks[j]['capacity']
					for ai in range(0, len(problem.datastructs)):
						if problem.X[ai][j] == True:
							remaining_capacity -= problem.datastructs[ai]['size']

					fixed_cap = broken_cap - problem.datastructs[i]['size']
					if remaining_capacity >= problem.datastructs[i]['size'] and fixed_cap <= problem.membanks[h]['capacity']:
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

def find_broken(problem):
	#Find broken j
	for j in range(0, len(problem.membanks)):
		remaining_capacity = problem.membanks[j]['capacity']
		for i in range(0, len(problem.datastructs)):
			if problem.X[i][j] == True:
				remaining_capacity -= problem.datastructs[i]['size']
		if remaining_capacity < 0:
			return j
	return None

def repair(problem):
	j = find_broken(problem)
	if j is not None:
		return possible_moves_fix(problem, j)
	else:
		return None

def best_move_v2(problem, possibles, tabList):	

	best = None
	for move in possibles:
		if not str(move['i'])+"-"+str(move['j']) in tabList:
			if best is None: original_cost = problem.cost(move['i'], move['h'])
			else: original_cost = best['cost']
			cost = problem.cost(move['i'], move['j'])
			if cost < original_cost:
				best = {'move': move, 'cost': cost }
	if best is not None:
		tabList.append(str(best['move']['i'])+"-"+str(best['move']['j']))
		return best['move']
	else:
		return None

def best_move_v3(problem, possibles):

	best = None
	for move in possibles:
		if best is None:
			best = {'move': move, 'cost': problem.cost(move['i'], move['j'])}
		else: 
			original_cost = best['cost']
			cost = problem.cost(move['i'], move['j'])
			if cost < original_cost:
				best = {'move': move, 'cost': cost }
	if best is not None:
		return best['move']
	else:
		return None

def explore_neighbourhood_n0(problem):
	return best_move(problem, prune(problem, possible_moves(problem)))

def explore_neighbourhood_n2(problem, tabList):
	move = best_move_v2(problem, prune(problem, possible_moves(problem)), tabList)
	if move is None:
		return None

	problem.X[move['i']][move['h']] = False
	problem.X[move['i']][move['j']] = True
	problem.update_conflicts()

def explore_neighbourhood_n1(problem, tabList):
	pos = [move for move in prune(problem, possible_moves_break(problem)) if not str(move['i'])+"-"+str(move['j']) in tabList]
	move = pos[random.randint(0, len(pos)-1)] 
	if move is None:
		return None
	problem.X[move['i']][move['h']] = False
	problem.X[move['i']][move['j']] = True
	problem.update_conflicts()

	pos = repair(problem)
	if pos is None:
		return None
	move = best_move_v3(problem, pos)
	if move is None:
		return None

	problem.X[move['i']][move['h']] = False
	problem.X[move['i']][move['j']] = True
	problem.update_conflicts()
