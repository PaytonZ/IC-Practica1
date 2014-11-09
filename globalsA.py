 # -*- coding: utf-8 -
''' 

Juan Luis Pérez Valbuena
Ingeniería del Conocimiento - Práctica 1 - Algoritmo A* 

'''

from node import Node

def upper_limit_x():
	global UPPER_LIMIT_X
	UPPER_LIMIT_X = 10
	return UPPER_LIMIT_X
def lower_limit_x():
	global LOWER_LIMIT_X
	LOWER_LIMIT_X = 0
	return LOWER_LIMIT_X
def upper_limit_y():
	global UPPER_LIMIT_Y
	UPPER_LIMIT_Y = 10
	return UPPER_LIMIT_Y
def lower_limit_y():
	global LOWER_LIMIT_Y
	LOWER_LIMIT_Y = 0
	return LOWER_LIMIT_Y

def set_origin(node):
	global origin 
	origin = node

def origin():
	global origin
	return origin

def set_finish(node):
	global finish 
	finish = node

def finish():
	global finish
	return finish




