'''
Author: Dongli
Date: 2021-02-03 10:09:11
LastEditors: Dongli
LastEditTime: 2021-02-22 15:31:43
Description: 
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from DataConfiguration import MyTree
from FileConfiguration import File
from Ui_PackageCheck import Ui_Form
import sys




class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.branch_sn = []
        self.flag = 1

        # 实例化数据库
        self.file = File()
        self.root_path = self.file.back_file()
        self.tree = MyTree(self.root_path)

        # 确认开始
        self.pushButton_check.clicked.connect(self.show_data)
        self.pushButton_check.clicked.connect(self.focus_change)

        self.checkBox_main.clicked.connect(lambda: self.checkBox_branch.setChecked(False))
        self.checkBox_branch.clicked.connect(lambda: self.checkBox_main.setChecked(False))

    def table_name(self):
        try:
            productionSN = self.lineEdit_fileName.text()
            return productionSN
        except Exception as e:
            print(e)

    def search_sn(self):
        try:
            table = self.table_name()
            key = [f"{self.lineEdit_fileSN.text()}", "", "", "", "", ""]
            res = self.tree.search_data(table, key)
            return res
        except Exception as e:
            print(e)

    def show_data(self):
        try:
            self.pushButton_check.setEnabled(False)
            data = self.search_sn()
            if len(data) < 1:
                self.lineEdit_check.setText("Fail")
                self.lineEdit_check.setStyleSheet("background-color:red")
                self.textEdit_data_show.clear()
                for i in data:
                    self.textEdit_data_show.append(str(i).replace(")", "").replace("(", ""))
            else:
                self.lineEdit_check.setText("ok")
                self.lineEdit_check.setStyleSheet("background-color:green")
                self.textEdit_data_show.clear()
            if len(self.lineEdit_fileSN.text()) >= 1:
                for i in data:
                    self.textEdit_data_show.append(str(i).replace(")", "").replace("(", ""))
                    self.branch_sn.append(i)
            if len(self.lineEdit_fileSN_2.text()) >= 1:
                self.textEdit_data_show.clear()
                for j in data:
                    if self.lineEdit_fileSN_2.text() in j[3]:
                        self.textEdit_data_show.append(str(j).replace(")", "").replace("(", ""))
            self.pushButton_check.setEnabled(True)
        except Exception as e:
            self.pushButton_check.setEnabled(True)
            print(e)
    
    def focus_change(self):
        if self.checkBox_main.isChecked():
            num = self.flag % 2
        else:
            num = self.flag % 1
        if num == 1:
            self.lineEdit_fileSN.clear()
            self.lineEdit_fileSN.setFocus()
        elif num == 0:
            self.lineEdit_fileSN_2.clear()
            self.lineEdit_fileSN_2.setFocus()
        self.flag += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exit(app.exec_())