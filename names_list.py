# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'names_list.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NamesList(object):
    def setupUi(self, NamesList):
        NamesList.setObjectName("NamesList")
        NamesList.resize(392, 300)
        self.gridLayout = QtWidgets.QGridLayout(NamesList)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(NamesList)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(NamesList)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(NamesList)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(NamesList)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.retranslateUi(NamesList)
        QtCore.QMetaObject.connectSlotsByName(NamesList)

    def retranslateUi(self, NamesList):
        _translate = QtCore.QCoreApplication.translate
        NamesList.setWindowTitle(_translate("NamesList", "Names"))
        self.pushButton_2.setText(_translate("NamesList", "New"))
        self.pushButton.setText(_translate("NamesList", "Cancel"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("NamesList", "5"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("NamesList", "7"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("NamesList", "name"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("NamesList", "ewewg"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("NamesList", "456456"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

