# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(834, 500)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.newTask = QtWidgets.QPushButton(self.centralwidget)
        self.newTask.setObjectName("newTask")
        self.gridLayout.addWidget(self.newTask, 1, 2, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        self.treeWidget.header().setDefaultSectionSize(110)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 27))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.newTask.setText(_translate("Main", "New Task"))
        self.treeWidget.headerItem().setText(0, _translate("Main", "id"))
        self.treeWidget.headerItem().setText(1, _translate("Main", "date"))
        self.treeWidget.headerItem().setText(2, _translate("Main", "header"))
        self.treeWidget.headerItem().setText(3, _translate("Main", "category"))
        self.treeWidget.headerItem().setText(4, _translate("Main", "worker"))
        self.treeWidget.headerItem().setText(5, _translate("Main", "status"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Main", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Main", "Categories"))
        self.pushButton.setText(_translate("Main", "Workers"))

