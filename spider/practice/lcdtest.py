# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcdtest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



import sys
import os
import time
import parsel
import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 30, 251, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 241, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sum)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确认"))

    def sum(self):
        a = 0
        for i in range(0, 10):
            time.sleep(0.5)
            a += 1
            self.lcdNumber.display(a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
