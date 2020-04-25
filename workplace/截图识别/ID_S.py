import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_S import *
from identical import *

class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.vs = Visual()
        self.vs.row = 1
        self.pushButton_OK.clicked.connect(self.on_pushbutton_ok)
        self.pushButton_OK.clicked.connect(self.count)
        self.pushButton_file.clicked.connect(self.on_pushbutton_file)
    
    def count(self):
        self.vs.row += 1
        
    def on_pushbutton_ok(self):
        self.x = self.horizontalSlider.value()*15
        self.y = self.horizontalSlider_2.value()*15
        self.l = self.horizontalSlider_3.value()*15
        self.h = self.horizontalSlider_4.value()*15
        try:
            self.vs.bbox = (self.x, self.y, self.l, self.h)
            print(self.vs.bbox)
            self.vs.screenshot()
            self.vs.identify()
            self.vs.read_data()
        except:
            self.textBrowser.setText("图片尺寸错误")

        self.label.setText(str(self.x))
        self.label_2.setText(str(self.y))
        self.label_3.setText(str(self.l))
        self.label_4.setText(str(self.h))
        try:
            self.vs.date_file = self.path[0]
            self.vs.read_data()
            self.textBrowser.setText("储存成功"+ str(self.vs.row))
        except:
            self.textBrowser.setText("储存失败")

    def on_pushbutton_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName()
        self.textBrowser.setText(str(self.path[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exit(app.exec_())