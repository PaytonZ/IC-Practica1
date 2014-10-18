 # -*- coding: utf-8 -

from globals import *
''' Define una clase Posicion para resolver el problema del A*.
Actualnode : define el nodo actual 
fathernode : define el nodo padre
is_open : define si esta abierto o nodo
g : define el valor de la funcion g : distancia del nodo actual al origen
h : define el valor de la funcion h : distancia del nodo actual a la meta
f : define el valor de la funcion f : suma de g y h
'''
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