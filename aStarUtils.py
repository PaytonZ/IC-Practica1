 # -*- coding: utf-8 -
''' 

Juan Luis Pérez Valbuena
Ingeniería del Conocimiento - Práctica 1 - Algoritmo A* 

'''

from utils import *
from globalsA import *
from node import Node


''' Realiza el calculo de la lista. Calcula tanto G como H como F y ordena la lista por menor F.'''
def calculate_open_list(open_list):
	for p in open_list:
		if p.is_open:
			p.function_g(open_list)
			p.function_h()
			p.function_f()
	quicksort(open_list)

'''Dada una lista ordenada por F' elige el primer nodo no cerrado con F menor'''
def select_successor_node(list):
	for c in list:
		if(c.is_open):
			return c

'''Busca la posicion cuyo nodo sea el pasado por paramétro'''
def search_position_with_node(node,list):
	for c in list:
		if(c.actualnode == node):
			return c

''' Realiza la expansion del nodo hacia todas las direcciones posibles.
No considera los nodos no acessibles ''' 
def make_expansion(node,map):
	candidates = []
	for x in range(-1,2):
		for y in range(-1,2):
			new_x = node.x+x;
			new_y = node.y+y;
			if (new_x >= lower_limit_x() and new_x < upper_limit_x()) and (new_y >= lower_limit_y() and new_y < upper_limit_y()) and (map[new_x][new_y].forbidden==False):
				candidates.append(map[new_x][new_y])
	return candidates

''' Dada una solución , imprime por consola la secuencia de pasos'''
def print_solution(solution,list):
	print solution.actualnode
	if(solution.actualnode != solution.fathernode):
		print_solution(search_position_with_node(solution.fathernode,list),list)

''' Define un obstaculo inatravesable en la posicion (x,y)'''
def put_obstacle(x,y,map_list,obstacle_list):
	obstacle_list[x][y] = map_list[x][y] = Node(x,y,True,0)
