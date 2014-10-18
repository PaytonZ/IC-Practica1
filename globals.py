 # -*- coding: utf-8 -
''' 

Juan Luis Pérez Valbuena
Ingeniería del Conocimiento - Práctica 1 - Algoritmo A* 

'''

from node import Node

UPPER_LIMIT_X = 6
LOWER_LIMIT_X = 0
UPPER_LIMIT_Y = 6
LOWER_LIMIT_Y = 0

global origin
global finish

origin = Node(2,3,False,0)
finish = Node(5,0,False,0)
