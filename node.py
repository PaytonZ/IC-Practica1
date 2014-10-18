 # -*- coding: utf-8 -
import math
''' Clase Nodo :
x : posicion x del nodo
y : posicion y del nodo
forbidden : indica si esta prohibido el paso o no
penality : indica el nivel de penalización por el paso por este nodo
'''
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
