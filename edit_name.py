# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_name.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditName(object):
    def setupUi(self, EditName):
        EditName.setObjectName("EditName")
        EditName.resize(400, 178)
        self.gridLayout = QtWidgets.QGridLayout(EditName)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(EditName)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(EditName)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(EditName)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(EditName)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(EditName)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(EditName)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(EditName)
        QtCore.QMetaObject.connectSlotsByName(EditName)

    def retranslateUi(self, EditName):
        _translate = QtCore.QCoreApplication.translate
        EditName.setWindowTitle(_translate("EditName", "new name"))
        self.pushButton_3.setText(_translate("EditName", "Delete"))
        self.label.setText(_translate("EditName", "Name"))
        self.pushButton.setText(_translate("EditName", "Cancel"))
        self.pushButton_2.setText(_translate("EditName", "OK"))

