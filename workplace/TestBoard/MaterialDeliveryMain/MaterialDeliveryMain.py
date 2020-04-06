# 导入PyQt库
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

# 导入系统操作库
import time
import sys
import serial
import serial.tools.list_ports

# 导入界面
from MaterialDeliveryMainUI import *
from MaterialDeliveryremindUI import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.remianwindow = Remindwindow()
        # self.port_list = serial.tools.list_ports.comports()
        
        # 信号发出区域
        self.pushButton_exit.clicked.connect(self.on_pushbutton_exit)         #退出信号
        self.pushButton_sweep_com.clicked.connect(self.on_pushbutton_sweep)   #搜索串口
        self.pushButton_link_com.clicked.connect(self.on_pushbutton_link)     #连接串口

    def on_pushbutton_exit(self):
        """窗口关闭"""
        self.close()

    def on_pushbutton_sweep(self):
        """扫描端口"""
        self.pushButton_sweep_com.setText('正在扫描')
        port_list = serial.tools.list_ports.comports()
        for i in port_list:
            self.comboBox_com.addItem(str(i)[0:4])
        self.pushButton_sweep_com.setText('扫描完成')

    def on_pushbutton_link(self):
        """连接端口"""
        self.com = self.comboBox_com.currentText()
        try:
            serials = serial.Serial(str(self.com), 57600, timeout=0.5)
        except Exception as e:
            self.remianwindow.remindshow('ERROR:' + e)
            self.pushButton_link_com.setText('连接失败')
        else:
            self.pushButton_link_com.setText('连接成功')
            self.remianwindow.remindshow(serials.name)
            print(serials.name)

 
class Remindwindow(QtWidgets.QDialog, Ui_Remind):
    def __init__(self, parent=None):
        super(Remindwindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_exit_ERROR.clicked.connect(self.remindclose)
    
    def remindshow(self, value):
        self.remindwindow = Remindwindow()
        self.remindwindow.textBrowser.setText(value)
        self.remindwindow.show()

    def remindclose(self):
        self.close()

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exit(app.exec_())

