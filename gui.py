# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GUI.ui'
#
# Created: Tue Oct 21 13:16:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 654)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 0, 16, 631))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 221, 16))
        self.label_2.setObjectName("label_2")
        self.mainboardwidget = QtGui.QWidget(self.centralwidget)
        self.mainboardwidget.setGeometry(QtCore.QRect(0, 80, 531, 531))
        self.mainboardwidget.setObjectName("mainboardwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.mainboardwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainboard = QtGui.QTableWidget(self.mainboardwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainboard.sizePolicy().hasHeightForWidth())
        self.mainboard.setSizePolicy(sizePolicy)
        self.mainboard.setMinimumSize(QtCore.QSize(2000, 2000))
        self.mainboard.setMaximumSize(QtCore.QSize(256, 16777215))
        self.mainboard.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainboard.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainboard.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustIgnored)
        self.mainboard.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.mainboard.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.mainboard.setObjectName("mainboard")
        self.mainboard.setColumnCount(0)
        self.mainboard.setRowCount(0)
        self.verticalLayout.addWidget(self.mainboard)
        self.optionbarwidget = QtGui.QWidget(self.centralwidget)
        self.optionbarwidget.setGeometry(QtCore.QRect(540, 0, 120, 611))
        self.optionbarwidget.setObjectName("optionbarwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Juan Luis Pérez", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ingeniería del Conocimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))

