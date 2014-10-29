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
import random
import images_rc


start_set_x = -1
start_set_y = -1
finish_set_x = -1
finish_set_y = -1 

origin = Node(2,3,False,0)
finish = Node(5,0,False,0)

def handleTableClick(row,column):
	global start_set_x
	global start_set_y
	global finish_set_x
	global finish_set_y
	global origin
	global finish

	print "(%d, %d)" % (row , column)
	table = mySW.ui.mainboard
	#table.setItem(row, column, QtGui.QTableWidgetItem())
		
	if(start_set_x == -1 or start_set_y==-1):
		#table.item(row, column).setText("START")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/images/home.png"))
		table.item(row,column).setIcon(icon2)
		start_set_x = column
		start_set_y = row
		origin =  Node(start_set_x,start_set_y,False,0)
	else:
		if(finish_set_x == -1 or finish_set_y==-1):
			#table.item(row, column).setText("FINISH")
			icon2 = QtGui.QIcon()
			icon2.addPixmap(QtGui.QPixmap(":/images/finish.png"))
			table.item(row,column).setIcon(icon2)
			
			finish_set_x = column
			finish_set_y = row
			finish = Node(finish_set_x,finish_set_y,False,0)
		else: # Start and finished was set , reseting
			 clean_board()
			 paint_obstacles()
			 finish_set_x = -1 
			 finish_set_y = -1
			 #table.item(row, column).setText("START")
			 icon2 = QtGui.QIcon()
			 icon2.addPixmap(QtGui.QPixmap(":/images/home.png"))
			 table.item(row, column).setIcon(icon2)
			 start_set_x = column
			 start_set_y = row
			 origin =  Node(start_set_x,start_set_y,False,0) 

	#table.item(row, column).setBackground(QtGui.QColor(100,100,150))
	table.item(row, column).setSelected(False)
	table.item(row, column).setForeground(QtGui.QColor(255,255,255))

class ControlMainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(ControlMainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
	def customSetUp(self):
		
		initialize_map()
		

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
		self.ui.cleanButton.clicked.connect(action_clean_board)
		self.ui.randomButton.clicked.connect(create_random_map)
		QtCore.QObject.connect(self.ui.aboutASTAR, QtCore.SIGNAL('triggered()'), action_about_a_star)
		QtCore.QObject.connect(self.ui.actionNewMap, QtCore.SIGNAL('triggered()'), action_new_map)

		clean_board()

def create_random_map():
	global map1
	global obstacles
	initialize_map()
	clean_board()
	number_of_obstacles = int((upper_limit_x() * upper_limit_y())) / 2 ; # 50% of obstacles
 	for k in range(0,number_of_obstacles):
 		x = random.randrange(upper_limit_x())
 		y = random.randrange(upper_limit_y())
 		if (k % 2 == 0 ):
 			map1[x][y] = Node(x,y,False,0.8)
 		else:
 			put_obstacle( x , y ,map1,obstacles)
 	paint_obstacles()


def action_new_map():
	window = QtGui.QWidget(mySW.parent())
	form_layout = QtGui.QFormLayout()
	window.setLayout(form_layout)
	window.show()

def createMessagebox(title,msg):
	QtGui.QMessageBox.information(mySW, title, msg)

def action_clean_board():
	initialize_map()
	clean_board()

def clean_board():
	table = mySW.ui.mainboard
	for x in range(lower_limit_y(),upper_limit_x()):
		for y in range(lower_limit_y(),upper_limit_x()):
			table.setItem(y, x, QtGui.QTableWidgetItem())
			table.item(y, x).setBackground(QtGui.QColor(255,255,255))

def paint_obstacles():
	global map1
	table = mySW.ui.mainboard
	for o in obstacles:
			for j in o:
				if(isinstance(j,Node)):
					#table.setItem(j.y, j.x, QtGui.QTableWidgetItem())
					#table.item(j.y, j.x).setBackground(QtGui.QColor(255,0,0))
					item = QtGui.QTableWidgetItem()
					icon2 = QtGui.QIcon()
					icon2.addPixmap(QtGui.QPixmap(":/images/rocks.png"))
					table.item(j.y, j.x).setIcon(icon2)

	
	for x in range(lower_limit_y(),upper_limit_x()):
		for y in range(lower_limit_y(),upper_limit_x()):
			if(map1[x][y].penalty > 0):
				#table.setItem(y, x, QtGui.QTableWidgetItem())
				#table.item(y, x).setBackground(QtGui.QColor(175,175,175))
				icon2 = QtGui.QIcon()
				icon2.addPixmap(QtGui.QPixmap(":/images/rocks2.png"))
				table.item(y, x).setIcon(icon2)

def start_a_star():
	clean_board()
	paint_obstacles()
	table = mySW.ui.mainboard
	solve_a_star()
	#paint_obstacles()

def action_about_a_star():
	aboutmsg = "Program for solving the A Star problem \n"
	aboutmsg = aboutmsg +"Icons made by Situ Herrera ,OCHA , Freepik and ICONS8 from www.flaticon.com is licensed by" 
	aboutmsg = aboutmsg + " Creative Commons BY 3.0"
	createMessagebox("About A Star", aboutmsg)

''' Dada una solución , imprime por la interfaz la secuencia de pasos'''
def paint_solution(solution,list):
	table = mySW.ui.mainboard
	#table.setItem(solution.actualnode.y, solution.actualnode.x, QtGui.QTableWidgetItem())
	table.item(solution.actualnode.y, solution.actualnode.x).setBackground(QtGui.QColor(130,218,92))
	if(solution.actualnode != solution.fathernode):
		paint_solution(search_position_with_node(solution.fathernode,list),list)	
  
def initialize_map():
	global map1
	global obstacles
	map1 = [[0 for x in xrange(upper_limit_x())] for x in xrange(upper_limit_y())]
	obstacles = [[0 for x in xrange(upper_limit_x())] for x in xrange(upper_limit_y())]  	 
	for x in range(lower_limit_x(),upper_limit_x()):
		for y in range(lower_limit_y(),upper_limit_y()):
		#print ('%s + %s' % (x,y))
			map1[x][y]=Node(x,y,False,0)

def solve_a_star():
	
	''' 1. Colocar el nodo de comienzo en la lista ABIERTA y 
	calcular la función de coste f(n), siendo ahora g(n) = 0 y h(n) la distancia entre la posición actual y la meta.'''
	open_list = []
	
	origin_position = Position(origin,origin)
	origin_position.is_open = True
	open_list.append(origin_position)
	calculate_open_list(open_list)
	selected_node = select_successor_node(open_list)
	'''2. Los obstáculos se incluyen directamente en la lista CERRADA.'''
	
	for o in obstacles:
		for j in o:
			if (j is type(Node)):
				print j
				obs=Position(j,None)
				obs.is_open=False
				open_list.append(obs)

	print map1

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
		candidates = make_expansion(selected_node.actualnode,map1)
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
	if(selected_node is None):
		createMessagebox("Route Impossible", "The finish cannot be reached")
	else:
		paint_solution(selected_node,open_list)
		#print_solution(selected_node,open_list)
	

if __name__ == "__main__":
  	app = QtGui.QApplication(sys.argv)
	mySW = ControlMainWindow()
	mySW.customSetUp()
	mySW.show()
	sys.exit(app.exec_())
	
  	

  	
  	
