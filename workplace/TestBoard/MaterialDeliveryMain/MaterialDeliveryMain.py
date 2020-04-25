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
from UARTTOIIC import Core

cache01 = [
    [b'#_\x00\xce\x00U\x00\xf6\x00\x8d\xccrt\x88\xb8v\\\x1dL\x03\xe8\x17p\x05\xdcN \x03\xbbEv\x05\xeaN \x00\xe5Ev\x01k$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x80\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00$'],
    [b'#\x00\x00\x00$'],
    [b'#\x98$'],
    [b'#\x1c\x1c~\xe0\x0c\x86#\xf6\x00\x01$'],
    [b'#\x00\x00\x00\x00$'],
    [b'#\x02$'],
    [b'#\x00$'],
    [b'#\x00@$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x00@$'],
    [b'#\x00\x00$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00$'],
    [b'#\x00$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\x00\x00\xff\xff$'],
    [b'#\xff$'],
    [b'#\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$']

]


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.cache = []
        self.remianwindow = Remindwindow()
        self.core = Core()
        self.core.opposition_data(cache01)
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
            self.serials = serial.Serial(str(self.com), 57600, timeout=0.5)
            self.serials.bytesize = 8
            self.serials.bytesize = serial.EIGHTBITS
        except Exception as e:
            self.remianwindow.remindshow('ERROR:' + e)
            self.pushButton_link_com.setText('连接失败')
        else:
            self.pushButton_link_com.setText('连接成功')
            self.remianwindow.remindshow(self.serials.name)
            print(self.serials.name)
        try:
            print(self.core.threshold_dict)
            self.lineEdit_Temp.setText(str(round(self.core.threshold_dict['Temperature'], 3)))
            self.lineEdit_VCC.setText(str(round(self.core.threshold_dict['Vcc'], 3)))
        except Exception as e:
            print(e)

    def write_register(self, data_register):
        """向寄存器中发送数据指令"""
        try:
            for i in data_register:
                data = [0x23, 0x07, 0x06, 0xA2, int(i), int(data_register[i]), 0x24]
                self.serials.write(data)
        except Exception as e:
            self.remianwindow.remindshow("数据发送失败" + str(e))

    def receive_register(self):
        """接收相应寄存器中返回数据"""
        try:
            self.receive_words = self.serials.readlines()
            self.cache.append(self.receive_words)
        except Exception as e:
            self.remianwindow.remindshow("数据接收失败" + str(e))

    def manage_receive_data(self):
        """调用UARTTOIIC进行数据处理"""
        self.core.opposition_data(cache01)
        pass

    def start_show(self):
        """Pushbutton开始数据处理并且进行记录"""
        self.write_register(self.register_a0_sfp)
        self.receive_register()

 
class Remindwindow(QtWidgets.QDialog, Ui_Remind):
    def __init__(self, parent=None):
        super(Remindwindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_exit_ERROR.clicked.connect(self.remindclose)
    
    def remindshow(self, value):
        """提示窗口，用于监察错误"""
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

