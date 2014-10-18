 # -*- coding: utf-8 -
import math
from globals import *
from node import Node
from utils import *
from position import Position


open_list = []


mapa = [[0 for x in xrange(6)] for x in xrange(6)] 
for x in range(LOWER_LIMIT_X,UPPER_LIMIT_X):
	for y in range(LOWER_LIMIT_Y,UPPER_LIMIT_Y):
		#print ('%s + %s' % (x,y))
		mapa[x][y]=Node(x,y,False,0)



obstacles = [[0 for x in xrange(6)] for x in xrange(6)]

def put_obstacle(x,y):
	obstacles[x][y] = mapa[x][y] = Node(x,y,True,0)

put_obstacle(3,0)
put_obstacle(3,1)
put_obstacle(3,2)
put_obstacle(3,3)
put_obstacle(3,4)






def main():
	
	''' 1. Colocar el nodo de comienzo en la lista ABIERTA y 
	calcular la función de coste f(n), siendo ahora g(n) = 0 y h(n) la distancia entre la posición actual y la meta.'''
	origin_position = Position(origin,origin)
	origin_position.is_open = True
	open_list.append(origin_position)
	calculate_open_list()
	selected_node = select_successor_node(open_list)
	'''2. Los obstáculos se incluyen directamente en la lista CERRADA.'''
	for o in obstacles:
		for j in o:
			if (j is type(Node)):
				print j
				obs=Position(j,None)
				obs.is_open=False
				open_list.append(obs)
	
	'''3. 
	Realizar expansion.
	Eliminar de la lista ABIERTA el nodo con la función de coste de mínimo valor 
	y colocarla en CERRADA. Este es el nodo n. Si se produce empate entre dos nodos elegir uno de ellos aleatoriamente.
	Si uno de los nodos en ABIERTA es el nodo meta, entonces seleccionarlo, recuperar los punteros de los antecesores y generar la solución. 
	Actualizar el coste para alcanzar el nodo padre con el fin de poder calcular posteriormente la nueva función de coste h(n). 
	En caso contrario continuar en el punto 4.'''
	'''4. Determinar todos los nodos sucesores de n y calcular la función de coste para cada sucesor que NO está en la lista CERRADA.'''

	'''5.Asociar con cada sucesor que NO está ni en ABIERTA ni CERRADA el coste calculado, f(n), 
	y poner esos sucesores en la lista ABIERTA. Asignar punteros a n (n es el nodo padre).'''

	'''6.Con cualquiera de los sucesores que ya estaban en ABIERTA 
	calcular el menor coste de entre el que ya tenía y el recién calculado: min(nuevo f(n), viejo f(n)).'''
	'''Ir al paso 3'''

	while selected_node is not None and selected_node.actualnode != finish  :
		candidates = make_expansion(selected_node.actualnode)
		for c in candidates:
			exist_node = False
			for p in open_list:
				if(p.actualnode == c):
					exist_node = True
			if(not exist_node):
				position_candidate = Position(c,selected_node.actualnode)
				open_list.append(position_candidate)
		selected_node.is_open = False
		calculate_open_list()
		selected_node = select_successor_node(open_list)
		for i in range(len(open_list)):
			print ("ID: %d Position->%s" %(i , open_list[i] ))

	print_solution(selected_node)


if __name__ == "__main__":
   main()
