# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_task.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newTaskDialog(object):
    def setupUi(self, newTaskDialog):
        newTaskDialog.setObjectName("newTaskDialog")
        newTaskDialog.setEnabled(True)
        newTaskDialog.resize(653, 498)
        newTaskDialog.setAcceptDrops(True)
        self.gridLayout = QtWidgets.QGridLayout(newTaskDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_4 = QtWidgets.QComboBox(newTaskDialog)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 4, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(newTaskDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(newTaskDialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(newTaskDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(newTaskDialog)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(newTaskDialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(newTaskDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(newTaskDialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(newTaskDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(newTaskDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(newTaskDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(newTaskDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(newTaskDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(newTaskDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(newTaskDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(newTaskDialog)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 6, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(newTaskDialog)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(newTaskDialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 9, 2, 1, 1)

        self.retranslateUi(newTaskDialog)
        QtCore.QMetaObject.connectSlotsByName(newTaskDialog)

    def retranslateUi(self, newTaskDialog):
        _translate = QtCore.QCoreApplication.translate
        newTaskDialog.setWindowTitle(_translate("newTaskDialog", "New Task"))
        self.comboBox_4.setItemText(0, _translate("newTaskDialog", "None"))
        self.label_8.setText(_translate("newTaskDialog", "Status"))
        self.pushButton.setText(_translate("newTaskDialog", "cancel"))
        self.comboBox_2.setItemText(0, _translate("newTaskDialog", "1"))
        self.comboBox_2.setItemText(1, _translate("newTaskDialog", "2"))
        self.comboBox_2.setItemText(2, _translate("newTaskDialog", "3"))
        self.label.setText(_translate("newTaskDialog", "Header:"))
        self.label_2.setText(_translate("newTaskDialog", "Category:"))
        self.label_3.setText(_translate("newTaskDialog", "Importance:"))
        self.label_4.setText(_translate("newTaskDialog", "Id of super task:"))
        self.label_5.setText(_translate("newTaskDialog", "Worker"))
        self.pushButton_2.setText(_translate("newTaskDialog", "Ok"))
        self.label_7.setText(_translate("newTaskDialog", "Deadline"))
        self.comboBox_3.setItemText(0, _translate("newTaskDialog", "Open"))
        self.comboBox_3.setItemText(1, _translate("newTaskDialog", "Closed"))
        self.dateEdit.setDisplayFormat(_translate("newTaskDialog", "dd.MM.yyyy"))
        self.pushButton_3.setText(_translate("newTaskDialog", "Delete"))

