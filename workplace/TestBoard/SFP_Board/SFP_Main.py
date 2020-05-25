from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

# 导入系统操作库
import time
import sys
import serial
import serial.tools.list_ports

# 导入界面
from Ui_SFP import *
from RemindUI import *
from SFP_Core import *

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


class WorkThread(QtCore.QThread):
    receiver_data = QtCore.pyqtSignal()
    show_data = QtCore.pyqtSignal()
    delete_data = QtCore.pyqtSignal()

    def run(self):
        try:
            while True:
                self.receiver_data.emit()
                self.msleep(860)
                self.show_data.emit()
                # break
        except Exception as e:
            print(e)


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.remianwindow  = Remindwindow()
        self.workThread = WorkThread()
        self.core = Core()
        self.cache = []
        # self.core.opposition_data(cache01)
        self.oppsition = 0
        self.pushButton_sweep_com.clicked.connect(self.on_pushbutton_sweep)
        self.pushButton_link_com.clicked.connect(self.on_pushbutton_link)
        self.pushButton_exit.clicked.connect(self.on_pushbutton_exit)
        # 一次测试流
        # self.pushButton_link_com.clicked.connect(lambda: self.write_register_a2(self.core.register_a2_sfp))
        # self.pushButton_exit.clicked.connect(self.digital)
        # 线程测试流
        # self.workThread.receiver_data.connect(lambda: self.write_register_a2(self.core.register_a2_sfp))
        try:
            self.workThread.receiver_data.connect(lambda: self.write_register(self.core.register_a2_sfp))
            self.workThread.show_data.connect(self.digital)
            self.pushButton_OK.clicked.connect(self.work)
        except Exception as e:
            print(e)

    def on_pushbutton_exit(self):
        """窗口关闭"""
        self.close()

    def write_register(self, data_register):
        """向寄存器中发送数据指令"""
        try:
            for i in data_register:
                data = [0x23, 0x07, 0x06, 0xA2, int(i), int(data_register[i]), 0x24]
                self.serials.write(data)
                self.receive_words = self.serials.readlines()
                # print(data)
                self.cache.append(self.receive_words)
        except Exception as e:
            self.remianwindow.remindshow("数据发送失败" + str(e))
        self.core.opposition_data(self.cache)

    def test(self):
        self.core.opposition_data(cache01)

    def on_pushbutton_sweep(self):
        """扫描端口"""
        self.pushButton_sweep_com.setText('正在扫描')
        port_list = serial.tools.list_ports.comports()
        for i in port_list:
            self.comboBox_com.addItem(str(i)[0:4])
        self.pushButton_sweep_com.setText('扫描完成')

    def on_pushbutton_link(self):
        """连接端口"""
        try:
            self.com = self.comboBox_com.currentText()
            self.serials = serial.Serial(str(self.com), 57600, timeout=0.05)
            self.serials.bytesize = 8
            self.serials.bytesize = serial.EIGHTBITS
        except Exception as e:
            self.remianwindow.remindshow('ERROR:' + str(e))
            self.pushButton_link_com.setText('连接失败')
        else:
            self.pushButton_link_com.setText('连接成功')
            self.remianwindow.remindshow(self.serials.name)
            print(self.serials.name)

    def digital(self):
        try:
            # print('温度：' + str(self.core.threshold_dict['Temperature']))
            # print('电压' + str(self.core.threshold_dict['Vcc']))
            # print('电流' + str(self.core.threshold_dict['Bias']))
            # print('TXP' + str(self.core.threshold_dict['TX Power']))
            # print('RXP' + str(self.core.threshold_dict['RX Power']))
            print(self.core.threshold_dict)
            self.lineEdit_Temp.setText(str(round(self.core.threshold_dict['Temperature'], 3)))
            self.lineEdit_VCC.setText(str(round(self.core.threshold_dict['Vcc'], 3)))
            self.lineEdit_Bias.setText(str(round(self.core.threshold_dict['Bias'], 3)))
            self.lineEdit_TxP.setText(str(round(self.core.threshold_dict['TX Power'], 3)))
            self.lineEdit_RxP.setText(str(round(self.core.threshold_dict['RX Power'], 3)))
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        # 温度门限颜色显示
        try:
            if self.core.threshold_dict['Temperature'] < self.core.threshold_dict['Temp High Alarm']:
                self.lineEdit_Temp_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Temp_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Temperature'] < self.core.threshold_dict['Temp High Warning']:
                self.lineEdit_Temp_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Temp_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Temperature'] > self.core.threshold_dict['Temp Low Alarm']:
                self.lineEdit_Temp_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Temp_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Temperature'] > self.core.threshold_dict['Temp Low Warning']:
                self.lineEdit_Temp_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Temp_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            # self.remianwindow.remindshow(str(e))

        # VCC门限颜色显示
        try:
            if self.core.threshold_dict['Vcc'] < self.core.threshold_dict['Voltage High Alarm']:
                self.lineEdit_VCC_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_VCC_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Vcc'] < self.core.threshold_dict['Voltage High Warning']:
                self.lineEdit_VCC_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_VCC_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Vcc'] > self.core.threshold_dict['Voltage Low Alarm']:
                self.lineEdit_VCC_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_VCC_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Vcc'] > self.core.threshold_dict['Voltage Low Warning']:
                self.lineEdit_VCC_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_VCC_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            # self.remianwindow.remindshow(str(e))
        
        # Bias门限颜色
        try:
            if self.core.threshold_dict['Bias'] < self.core.threshold_dict['Bias High Alarm']:
                self.lineEdit_Bias_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Bias_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Bias'] < self.core.threshold_dict['Bias High Warning']:
                self.lineEdit_Bias_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Bias_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Bias'] > self.core.threshold_dict['Bias Low Alarm']:
                self.lineEdit_Bias_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Bias_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['Bias'] > self.core.threshold_dict['Bias Low Warning']:
                self.lineEdit_Bias_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_Bias_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        try:
            if self.core.threshold_dict['TX Power'] < self.core.threshold_dict['TX Power High Alarm']:
                self.lineEdit_TxP_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_TxP_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['TX Power'] < self.core.threshold_dict['TX Power High Warning']:
                self.lineEdit_TxP_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_TxP_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['TX Power'] > self.core.threshold_dict['TX Power Low Alarm']:
                self.lineEdit_TxP_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_TxP_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['TX Power'] > self.core.threshold_dict['TX Power Low Warning']:
                self.lineEdit_TxP_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_TxP_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        try:
            if self.core.threshold_dict['RX Power'] < self.core.threshold_dict['RX Power High Alarm']:
                self.lineEdit_RxP_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_RxP_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['RX Power'] < self.core.threshold_dict['RX Power High Warning']:
                self.lineEdit_RxP_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_RxP_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['RX Power'] > self.core.threshold_dict['RX Power Low Alarm']:
                self.lineEdit_RxP_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_RxP_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['RX Power'] > self.core.threshold_dict['RX Power Low Warning']:
                self.lineEdit_RxP_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_RxP_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        try:
            if self.core.threshold_dict['OLT'] <= self.core.threshold_dict['Optional Laser Temp High Alarm']:
                self.lineEdit_OLT_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OLT_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OLT'] <= self.core.threshold_dict['Optional Laser Temp High Warning']:
                self.lineEdit_OLT_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OLT_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OLT'] >= self.core.threshold_dict['Optional Laser Temp Low Alarm']:
                self.lineEdit_OLT_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OLT_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OLT'] >= self.core.threshold_dict['Optional Laser Temp Low Warning']:
                self.lineEdit_OLT_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OLT_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        try:
            if self.core.threshold_dict['OTC'] <= self.core.threshold_dict['Optional TEC Current High Alarm']:
                self.lineEdit_OTC_1.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OTC_1.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OTC'] <= self.core.threshold_dict['Optional TEC Current High Warning']:
                self.lineEdit_OTC_2.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OTC_2.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OTC'] >= self.core.threshold_dict['Optional TEC Current Low Alarm']:
                self.lineEdit_OTC_3.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OTC_3.setStyleSheet("background-color:red")
            if self.core.threshold_dict['OTC'] >= self.core.threshold_dict['Optional TEC Current Low Warning']:
                self.lineEdit_OTC_4.setStyleSheet("background-color:green")
                self.oppsition += 1
            else:
                self.lineEdit_OTC_4.setStyleSheet("background-color:red")
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        try:
            if self.oppsition == 28:
                self.lineEdit_INIT.setStyleSheet("background-color:green")
            elif self.oppsition == 26:
                self.lineEdit_INIT.setStyleSheet("background-color:yellow")
            else:
                self.lineEdit_INIT.setStyleSheet("background-color:red")
            self.oppsition = 0
        except Exception as e:
            print(e)
            #  self.remianwindow.remindshow(str(e))

        del self.core.threshold_0_39[:]
        del self.core.threshold_40_55[:]
        del self.core.present_96_105[:]
        del self.core.optional_106_109[:]
        del self.cache[:]
        self.core.threshold_dict = {}

    def work(self):
        self.workThread.start()


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