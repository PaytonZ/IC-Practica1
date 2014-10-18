 # -*- coding: utf-8 -
from utils import *

''' Realiza el calculo de la lista. Calcula tanto G como H como F y ordena la lista por menor F.'''
def calculate_open_list():
	for p in open_list:
		if p.is_open:
			p.function_g()
			p.function_h()
			p.function_f()
	quicksort(open_list)

'''Dada una lista ordenada por F' elige el primer nodo no cerrado con F menor'''
def select_successor_node(list):
	for c in list:
		if(c.is_open):
			return c
'''Busca la posicion cuyo nodo sea el pasado por paramétro'''
def search_position_with_node(node):
	for c in open_list:
		if(c.actualnode == node):
			return c
''' Realiza la expansion del nodo hacia todas las direcciones posibles.
No considera los nodos no acessibles ''' 
def make_expansion(node):
	candidates = []
	for x in range(-1,2):
		for y in range(-1,2):
			new_x = node.x+x;
			new_y = node.y+y;
			if (new_x >= LOWER_LIMIT_X and new_x < UPPER_LIMIT_X) and (new_y >= LOWER_LIMIT_Y and new_y < UPPER_LIMIT_Y) and (mapa[new_x][new_y].forbidden==False):
				candidates.append(mapa[new_x][new_y])
	return candidates
''' Dada una solución , imprime por consola la secuencia de pasos'''
def print_solution(solution):
	print solution.actualnode
	if(solution.actualnode != solution.fathernode):
		print_solution(search_position_with_node(solution.fathernode))
