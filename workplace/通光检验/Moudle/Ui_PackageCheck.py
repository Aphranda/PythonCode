# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PythonCode\PythonCode\workplace\通光检验\Static\PackageCheck.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(888, 735)
        self.frame_11 = QtWidgets.QFrame(Form)
        self.frame_11.setGeometry(QtCore.QRect(10, 10, 871, 521))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_11.setLineWidth(2)
        self.frame_11.setObjectName("frame_11")
        self.textEdit_data_show = QtWidgets.QTextEdit(self.frame_11)
        self.textEdit_data_show.setGeometry(QtCore.QRect(10, 10, 851, 501))
        self.textEdit_data_show.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_data_show.setObjectName("textEdit_data_show")
        self.frame_12 = QtWidgets.QFrame(Form)
        self.frame_12.setGeometry(QtCore.QRect(10, 540, 871, 161))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_12.setLineWidth(2)
        self.frame_12.setObjectName("frame_12")
        self.label = QtWidgets.QLabel(self.frame_12)
        self.label.setGeometry(QtCore.QRect(10, 14, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_fileSN = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_fileSN.setGeometry(QtCore.QRect(160, 60, 541, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_fileSN.setFont(font)
        self.lineEdit_fileSN.setObjectName("lineEdit_fileSN")
        self.lineEdit_check = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_check.setGeometry(QtCore.QRect(740, 10, 113, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_check.setFont(font)
        self.lineEdit_check.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.lineEdit_check.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_check.setObjectName("lineEdit_check")
        self.lineEdit_fileName = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_fileName.setGeometry(QtCore.QRect(160, 10, 571, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_fileName.setFont(font)
        self.lineEdit_fileName.setObjectName("lineEdit_fileName")
        self.label_2 = QtWidgets.QLabel(self.frame_12)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_check = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_check.setGeometry(QtCore.QRect(740, 60, 111, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_check.setFont(font)
        self.pushButton_check.setObjectName("pushButton_check")
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_fileSN_2 = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_fileSN_2.setGeometry(QtCore.QRect(160, 100, 541, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_fileSN_2.setFont(font)
        self.lineEdit_fileSN_2.setObjectName("lineEdit_fileSN_2")
        self.checkBox_main = QtWidgets.QCheckBox(self.frame_12)
        self.checkBox_main.setGeometry(QtCore.QRect(710, 68, 16, 21))
        self.checkBox_main.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(9)
        self.checkBox_main.setFont(font)
        self.checkBox_main.setMouseTracking(True)
        self.checkBox_main.setText("")
        self.checkBox_main.setTristate(False)
        self.checkBox_main.setObjectName("checkBox_main")
        self.checkBox_branch = QtWidgets.QCheckBox(self.frame_12)
        self.checkBox_branch.setGeometry(QtCore.QRect(710, 110, 16, 21))
        self.checkBox_branch.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(9)
        self.checkBox_branch.setFont(font)
        self.checkBox_branch.setMouseTracking(True)
        self.checkBox_branch.setText("")
        self.checkBox_branch.setTristate(False)
        self.checkBox_branch.setObjectName("checkBox_branch")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "文件名："))
        self.lineEdit_check.setText(_translate("Form", "Check"))
        self.label_2.setText(_translate("Form", "查询主SN："))
        self.pushButton_check.setText(_translate("Form", "查询"))
        self.pushButton_check.setShortcut(_translate("Form", "Return"))
        self.label_3.setText(_translate("Form", "查询分支SN："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
