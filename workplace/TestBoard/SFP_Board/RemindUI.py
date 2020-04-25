# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PythonCode\code\workplace\TestBoard\MaterialDeliveryMain\remind.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Remind(object):
    def setupUi(self, Remind):
        Remind.setObjectName("Remind")
        Remind.resize(393, 300)
        self.pushButton_exit_ERROR = QtWidgets.QPushButton(Remind)
        self.pushButton_exit_ERROR.setGeometry(QtCore.QRect(10, 220, 371, 71))
        self.pushButton_exit_ERROR.setMinimumSize(QtCore.QSize(371, 71))
        font = QtGui.QFont()
        font.setFamily("SWTxt")
        font.setPointSize(24)
        self.pushButton_exit_ERROR.setFont(font)
        self.pushButton_exit_ERROR.setObjectName("pushButton_exit_ERROR")
        self.frame = QtWidgets.QFrame(Remind)
        self.frame.setGeometry(QtCore.QRect(10, 10, 371, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 351, 181))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Remind)
        QtCore.QMetaObject.connectSlotsByName(Remind)

    def retranslateUi(self, Remind):
        _translate = QtCore.QCoreApplication.translate
        Remind.setWindowTitle(_translate("Remind", "Remind"))
        self.pushButton_exit_ERROR.setText(_translate("Remind", "ok"))
