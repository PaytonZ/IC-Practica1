 # -*- coding: utf-8 -
import math
import random

UPPER_LIMIT_X = 6
LOWER_LIMIT_X = 0
UPPER_LIMIT_Y = 6
LOWER_LIMIT_Y = 0

class Node(object):
	def __init__(self,x,y,forbidden,penality):
		self.x = x 
		self.y = y
		self.forbidden = forbidden
		self.penality = penality
	def euclidean_distance(self,nodo):
		return float(math.sqrt(pow(self.x-nodo.x,2)+pow(self.y-nodo.y,2)))
	def __str__(self):
		return "({0},{1})".format(self.x,self.y)
	def __unicode__(self):
		return self.__str__()
	def __repr__(self):
		return self.__str__()
	def __eq__(self,other):
		return self.x == other.x and self.y == other.y
	def __ne__(self,other):
		return self.x != other.x or self.y != other.y

open_list = []
'''http://en.literateprograms.org/Quicksort_(Python)'''

def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] >= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    return first
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


def checkSorted(a):
    for i in xrange(1, len(a) - 1):
        if a[i] < a[i-1]:
            return False
    return True

def calculate_open_list():
	for p in open_list:
		if p.is_open:
			p.function_g()
			p.function_h()
			p.function_f()

	quicksort(open_list)


mapa = [[0 for x in xrange(6)] for x in xrange(6)] 
for x in range(LOWER_LIMIT_X,UPPER_LIMIT_X):
	for y in range(LOWER_LIMIT_Y,UPPER_LIMIT_Y):
		#print ('%s + %s' % (x,y))
		mapa[x][y]=Node(x,y,False,0)


origin = Node(2,3,False,0)
finish = Node(4,5,False,0)

class Position(object):
	def __init__(self,actualnode,fathernode):
		self.actualnode=actualnode
		self.fathernode=fathernode
		self.is_open = True
		self.g = 0.0
		self.h = 0.0
		self.f = 0.0
	def function_g(self):
		self.g = float(self.actualnode.euclidean_distance(origin))
		return self.g
	def function_h(self):
		self.h = float(self.actualnode.euclidean_distance(finish))
		return self.h
	def function_f(self):
		self.f = self.function_g() + self.function_h() 
		return self.f
	def __lt__(self,other):
		return self.f < other.f
	def __le__(self,other):
		return self.f <= other.f
	def __eq__(self,other):
		return self.f == other.f
	def __ne__(self,other):
		return self.f != other.f
	def __gt__(self,other):
		return self.f > other.f
	def __ge__(self,other):
		return self.f >= other.f
	def __str__(self):
		return "Actual Node: %s Father Node: %s G: %f H: %f F: %f \n is_open: %s" %( self.actualnode.__str__() , self.fathernode.__str__() , self.g , self.h , self.f , self.is_open)
	def __unicode__(self):
		return self.__str__()
	def __repr__(self):
		return self.__str__()



def make_expansion(node):
	candidates = []
	for x in range(-1,1):
		for y in range(-1,1):
			new_x = node.x+x;
			new_y = node.y+y;
			if (new_x >= LOWER_LIMIT_X and new_x < UPPER_LIMIT_X) and (new_y >= LOWER_LIMIT_Y and new_y < UPPER_LIMIT_Y) and (mapa[new_x][new_y].forbidden==False):
				candidates.append(mapa[new_x][new_y])
	return candidates



def main():
	
	''' 1. Colocar el nodo de comienzo en la lista ABIERTA y 
	calcular la función de coste f(n), siendo ahora g(n) = 0 y h(n) la distancia entre la posición actual y la meta.'''
	origin_position = Position(origin,origin)
	origin_position.is_open = True
	open_list.append(origin_position)
	calculate_open_list()
	father = open_list[0]
	'''2. Los obstáculos se incluyen directamente en la lista CERRADA.'''

	candidates = make_expansion(origin)
		
	'''3. 
	Realizar expansion.
	Eliminar de la lista ABIERTA el nodo con la función de coste de mínimo valor 
	y colocarla en CERRADA. Este es el nodo n. Si se produce empate entre dos nodos elegir uno de ellos aleatoriamente.
	Si uno de los nodos en ABIERTA es el nodo meta, entonces seleccionarlo, recuperar los punteros de los antecesores y generar la solución. 
	Actualizar el coste para alcanzar el nodo padre con el fin de poder calcular posteriormente la nueva función de coste h(n). 
	En caso contrario continuar en el punto 4.'''

	for c in candidates:
		exist_node = False
		for p in open_list:
			if(p.actualnode == p.actualnode):
				exist_node = True
		if(exist_node):
			position_candidate = Position(c,father.actualnode)
			open_list.append(position_candidate)
	calculate_open_list()
	for i in range(len(open_list)):
		print ("ID: %d Position->%s" %(i , open_list[i] ))

	'''4. Determinar todos los nodos sucesores de n y calcular la función de coste para cada sucesor que NO está en la lista CERRADA.'''

	'''5.Asociar con cada sucesor que NO está ni en ABIERTA ni CERRADA el coste calculado, f(n), 
	y poner esos sucesores en la lista ABIERTA. Asignar punteros a n (n es el nodo padre).'''

	'''6.Con cualquiera de los sucesores que ya estaban en ABIERTA 
	calcular el menor coste de entre el que ya tenía y el recién calculado: min(nuevo f(n), viejo f(n)).'''


	'''Ir al paso 3'''

if __name__ == "__main__":
   main()
