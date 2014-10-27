 # -*- coding: utf-8 -
''' 

Juan Luis Pérez Valbuena
Ingeniería del Conocimiento - Práctica 1 - Algoritmo A* 

'''

import math
from globalsA import *
from node import *
from utils import *
from position import *
from aStarUtils import *
from gui import Ui_MainWindow
from PySide import QtCore, QtGui
import sys




def handleTableClick(row,column):
	print "(%d, %d)" % (row , column)

class ControlMainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(ControlMainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
	def customSetUp(self):
		
		table = self.ui.mainboard
		table.setRowCount(upper_limit_x())
		table.setColumnCount(upper_limit_y())
	 	table.setHorizontalHeaderLabels(('0', '1', '2' , '3' , '4' ,'5'))
		table.setVerticalHeaderLabels(('0', '1', '2' , '3' , '4' ,'5'))
		table.cellClicked.connect(handleTableClick)

		#(y,x)
		#table.setItem(origin.y, origin.x, QtGui.QTableWidgetItem())
		#table.item(origin.y, origin.x).setBackground(QtGui.QColor(100,100,150))

		#table.setItem(finish.y, finish.x, QtGui.QTableWidgetItem())
		#table.item(finish.y, finish.x).setBackground(QtGui.QColor(100,100,150))

		self.ui.solveButton.clicked.connect(start_a_star)
		self.ui.cleanButton.clicked.connect(clean_board)

		QtCore.QObject.connect(self.ui.aboutASTAR, QtCore.SIGNAL('triggered()'), action_about_a_star)

def createMessagebox(title,msg):
	
	QtGui.QMessageBox.information(mySW, title, msg)

def clean_board():
	table = mySW.ui.mainboard
	for x in range(lower_limit_y(),upper_limit_x()):
		for y in range(lower_limit_y(),upper_limit_x()):
			table.setItem(y, x, QtGui.QTableWidgetItem())
			table.item(y, x).setBackground(QtGui.QColor(255,255,255))

def start_a_star():
	clean_board()
	solve_a_star()

def action_about_a_star():
	aboutmsg = "Program for solving the A Star problem \n"
	aboutmsg = aboutmsg +"Icons made by Situ Herrera from www.flaticon.com is licensed by" 
	aboutmsg = aboutmsg + " Creative Commons BY 3.0"
	
	createMessagebox("About A Start", aboutmsg)


''' Dada una solución , imprime por la interfaz la secuencia de pasos'''
def paint_solution(solution,list):

	table = mySW.ui.mainboard
	table.setItem(solution.actualnode.y, solution.actualnode.x, QtGui.QTableWidgetItem())
	table.item(solution.actualnode.y, solution.actualnode.x).setBackground(QtGui.QColor(100,100,150))
	for o in obstacles:
			for j in o:
				if(isinstance(j,Node)):
					table.setItem(j.y, j.x, QtGui.QTableWidgetItem())
					table.item(j.y, j.x).setBackground(QtGui.QColor(255,0,0))
	if(solution.actualnode != solution.fathernode):
		paint_solution(search_position_with_node(solution.fathernode,list),list)	
    	

def solve_a_star():
	
	''' 1. Colocar el nodo de comienzo en la lista ABIERTA y 
	calcular la función de coste f(n), siendo ahora g(n) = 0 y h(n) la distancia entre la posición actual y la meta.'''
	open_list = []

	map = [[0 for x in xrange(upper_limit_x())] for x in xrange(upper_limit_y())] 
	for x in range(lower_limit_y(),upper_limit_x()):
		for y in range(lower_limit_y(),upper_limit_x()):
		#print ('%s + %s' % (x,y))
			map[x][y]=Node(x,y,False,0)

	origin_position = Position(origin,origin)
	origin_position.is_open = True
	open_list.append(origin_position)
	calculate_open_list(open_list)
	selected_node = select_successor_node(open_list)
	'''2. Los obstáculos se incluyen directamente en la lista CERRADA.'''
	put_obstacle(3,0,map,obstacles)
	put_obstacle(3,1,map,obstacles)
	put_obstacle(3,2,map,obstacles)
	put_obstacle(3,3,map,obstacles)
	put_obstacle(3,4,map,obstacles)
	

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
		candidates = make_expansion(selected_node.actualnode,map)
		for c in candidates:
			exist_node = False
			for p in open_list:
				if(p.actualnode == c):
					exist_node = True
			if(not exist_node):
				position_candidate = Position(c,selected_node.actualnode)
				open_list.append(position_candidate)
		selected_node.is_open = False
		calculate_open_list(open_list)
		selected_node = select_successor_node(open_list)
		#for i in range(len(open_list)):
			#print ("ID: %d Position->%s" %(i , open_list[i] ))

	paint_solution(selected_node,open_list)


	#print_solution(selected_node,open_list)

	

if __name__ == "__main__":
  	app = QtGui.QApplication(sys.argv)
	mySW = ControlMainWindow()
	mySW.customSetUp()
	mySW.show()
	sys.exit(app.exec_())
	
  	

  	
  	
