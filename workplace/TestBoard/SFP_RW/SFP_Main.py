from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

# 导入系统操作库
import time
import os
import sys
import serial
import serial.tools.list_ports

# 导入界面
from Ui_SFP import *
from RemindUI import *
from SFP_Core import *

# 导入dll
import TeraDll

change = False

cache01 = [
    [b'#!\x00\x00\x00m\xec\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\r\x1f\r\x1b\r\x13\r\x10)P)C)*) $'], 
    [b'#U\x00\xf6\x00F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8c\xa0qH\x88\xb8y\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x180\x0ea\x15\xb7b\x1f\x00\x9eC\xe2\x01<\x1dL\x00\x00\x17p\x03\xe8b\x1f\x03gC\xe2\x06\xca$']
    ]

class Ter_show(QtCore.QThread):
    bit_show = QtCore.pyqtSignal()

    def run(self):
        try:
            while True:
                self.bit_show.emit()
                self.msleep(500)
        except Exception as e:
            print(e)


class Signal(QtCore.QThread):
    """自定义信号"""
    signal_begin = QtCore.pyqtSignal()

    def run(self):
        try:
            while True:
                self.signal_begin.emit()
                self.msleep(1000)
        except Exception as e:
            print(e)


class WorkThread(QtCore.QThread):
    """自定义信号"""
    receiver_data = QtCore.pyqtSignal()
    show_data = QtCore.pyqtSignal()

    def run(self):
        """线程运行，执行代码"""
        global change
        try:
            while True:
                self.receiver_data.emit()
                self.msleep(860)
                self.show_data.emit()
                if change is True:
                    break
        except Exception as e:
            print(e)


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 实例化警告窗口
        self.remind_window = Remindwindow()

        # 实例化线程
        self.workThread = WorkThread()
        self.signalThread = Signal()

        # 实例化核心算法
        self.core = Core()

        # 模拟缓存区设置
        self.cache = []

        # 门限累加
        self.opposition = 0

        # 串口连接按键
        try:
            self.serials_num = 0
            self.pushButton_sweep_com.clicked.connect(self.on_pushbutton_sweep)
            self.pushButton_link_com.clicked.connect(self.on_pushbutton_link)
            self.pushButton_sweep_auto_W.clicked.connect(self.on_pushbutton_link)
            self.pushButton_exit.clicked.connect(self.finish)
        except Exception as e:
            print(e)

        # 串口自动连接按钮


        # 线程连接代码，刷新测试数据
        try:
            self.workThread.receiver_data.connect(lambda: self.color_read(self.core.register_a2_sfp))
            self.workThread.show_data.connect(self.digital)
            self.signalThread.signal_begin.connect(self.signal_colors)
            self.pushButton_OK.clicked.connect(self.work)
            self.pushButton_link_com.clicked.connect(self.signal_work)
            self.pushButton_sweep_auto_W.clicked.connect(self.signal_work)

            self.pushButton_OK_Q.clicked.connect(self.color_qsfp)
            self.pushButton_OK_Q.clicked.connect(self.digital_qsfp)
        except Exception as e:
            print(e)

        # 密码写入寄存器
        self.passWord = {}
        self.pushButton_PassWord.clicked.connect(self.finish)
        self.pushButton_PassWord.clicked.connect(self.password_register)

        # 高128，低128位显示
        self.radioButton_data_A0.toggled.connect(self.page_show)
        self.radioButton_data_A0.toggled.connect(self.finish)
        self.radioButton_data_A2.toggled.connect(self.page_show)
        self.radioButton_data_A2.toggled.connect(self.finish)

        # 选择文件夹
        self.pushButton_load.clicked.connect(self.file_choose)

        # 数据写入模块寄存器
        self.files = []
        self.i = 0
        self.pushButton_Write.clicked.connect(self.data_register)

        # 信息读取
        self.pushButton_R.clicked.connect(lambda: self.product_info(self.core.register_a0_sfp))

        # 模板复写
        self.pushButton_W.clicked.connect(self.product_write)

        # ter_show线程实例化
        self.ter_show_thread = Ter_show()

        # 线程链接
        # 工程师模式
        self.pushButton_SFPR.clicked.connect(self.version_read_A0)

    def on_pushbutton_exit(self):
        """窗口关闭"""
        self.close()

    def on_pushbutton_sweep(self):
        """扫描端口"""
        self.pushButton_sweep_com.setText('正在扫描')
        port_list = serial.tools.list_ports.comports()
        for i in port_list:
            self.comboBox_com.addItem(str(i).split(" ", 1)[0])
        self.pushButton_sweep_com.setText('扫描完成')

    def on_pushbutton_link(self):
        """连接端口"""
        try:
            self.serials_num += 1
            self.com = self.comboBox_com.currentText()
            if self.serials_num % 2:
                self.serials_board = serial.Serial(str(self.com), 57600, timeout=0.05)
            elif self.serials_num % 2 + 1:
                self.serials_error = serial.Serial(str(self.com), 115200, timeout=0.1)
        except Exception as e:
            if self.serials_board.isOpen():
                self.remind_window.remindshow('ERROR:' + str(e) + "\n" + "\n" + "串口已经连接")
            else:
                self.pushButton_link_com.setText('连接失败')
        else:
            try:
                if self.serials_board.isOpen():
                    self.pushButton_link_com.setText('连接成功')
                if self.serials_error.isOpen():
                    self.pushButton_sweep_auto_W.setText('连接成功')
            except Exception as e:
                print(e)
            self.remind_window.remindshow(self.com)
            print(self.com)

    # def auto_connect(self):
    #      """打开并检测端口，依据返回值进行排序整合"""
    #     # 测试板系统
    #     check_data = {
    #         "B": [0x23, 0x07, 0x06, 0xA2, 0x00, 0x01, 0x24]
    #     }
    #     port_list = serial.tools.list_ports.comports()
    #     for i in port_list:
    #         port_sign.append(str(i).split("-", 1)[0].replace(" ", ""))
    #     print(port_sign)

    #     for j in port_sign:
    #         self.serials_01 = serial.Serial(j, 9600, timeout=1)
    #         self.serials_01.write(check_data["B"])
    #         words = self.serials_01.read(size=10)
    #         print(words)
    #         if "#" not in str(words[0:5]):
    #             self.serials_01.close()
    #         else:
    #             port_sign.remove(j)
        
    #     for k in port_sign:
    #         self.serials_02 = serial.Serial(k, 9600, timeout=1)
    #         self.serials_02.write(check_data["B"])
    #         words = self.serials_02.read(size=10)
    #         print(words)
    #         if "#" not in str(words[0:5]):
    #             self.serials_02.close()
    #         else:
    #             port_sign.remove(k)

    #     # 误码仪系统
    #     teradll = TeraDll.ErrorBit()
    #     teradll.connect_apis()

    def signal_colors(self):
        """端口通讯提示灯条"""
        try:
            if self.serials_board.isOpen():
                self.lineEdit_xm_A.setStyleSheet("background-color:green")
            if self.serials_error.isOpen():
                self.lineEdit_wm_A.setStyleSheet("background-color:green")
        except Exception as e:
            print(e)

    def write_register_a2(self, value):
        """向寄存器A2中发送数据指令"""
        try:
            for i in value:
                data = [0x23, 0x07, 0x06, 0xA2, int(i), int(value[i]), 0x24]
                self.serials_board.write(data)
                self.receive_words = self.serials_board.readlines()
                self.cache.append(self.receive_words)
        except Exception as e:
            self.remind_window.remindshow("数据发送失败" + str(e))

    def write_register_a0(self, value: dict):
        """向寄存器A0中发送数据指令"""
        try:
            for i in value:
                data = [0x23, 0x07, 0x06, 0xA0, int(i), int(value[i]), 0x24]
                self.serials_board.write(data)
                self.receive_words = self.serials_board.readlines()
                print(self.receive_words)
                self.cache.append(self.receive_words)
        except Exception as e:
            self.remind_window.remindshow("数据发送失败" + str(e))
    
    def write_register_qsfp(self, value: dict):
        """向寄存器A0中发送数据指令"""
        data_127 = [0x23, 0x07, 0x07, 0xA0, 0x7f, 0x03, 0x24]
        self.serials_board.write(data_127)
        key = self.serials_board.readlines()
        print(key)
        try:
            for i in value:
                data = [0x23, 0x07, 0x06, 0xA0, int(i), int(value[i]), 0x24]
                self.serials_board.write(data)
                self.receive_words = self.serials_board.readlines()
                print(self.receive_words)
                self.cache.append(self.receive_words)
        except Exception as e:
            self.remind_window.remindshow("数据发送失败" + str(e)) 

    def write_data(self, value: list, key:str):
        """向模块芯片中写入信息"""
        try:
            data = [0x23, 0x07, 0x07, int(value[1]), int(value[0])]
            for i in value[2:]:
                data.append(i)
            data.append(0x24)
            data[1] = len(data)
            print(data)
            self.serials_board.write(data)
            back_words = self.serials_board.read(50)
            self.remind_window.remindshow(str(back_words) + "\n" + "写入成功" + "\n" + key)
        except Exception as e:
            print(e)

    def write_data_wm(self, value: list):
        """向误码仪中发送数据"""
        try:
            self.serials_error.write(value)
            receive_data = self.serials_error.read(size=100)
            return receive_data
        except Exception as e:
            print(e)


    def color_read(self, value: list):
        """门限颜色显示"""
        try:
            self.write_register_a2(value)
            self.core.opposition_data(self.cache)
        except Exception as e:
            print(e)

    def info_read(self, value: list):
        """信息显示"""
        self.write_register_a2(value)

    def digital(self):
        """颜色显示"""
        try:
            print(self.core.threshold_dict)
            self.lineEdit_Temp.setText(str(round(self.core.threshold_dict['Temperature'], 3)))
            self.lineEdit_VCC.setText(str(round(self.core.threshold_dict['Vcc'], 3)))
            self.lineEdit_Bias.setText(str(round(self.core.threshold_dict['Bias'], 3)))
            self.lineEdit_TxP.setText(str(round(self.core.threshold_dict['TX Power'], 3)))
            self.lineEdit_RxP.setText(str(round(self.core.threshold_dict['RX Power'], 3)))
        except Exception as e:
            print(e)
        line_edit = [
            "self.lineEdit_Temp", "self.lineEdit_VCC", "self.lineEdit_Bias", "self.lineEdit_TxP", "self.lineEdit_RxP", "self.lineEdit_OLT", "self.lineEdit_OTC"
            ]

        line_threshold = [
            ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning', 'Temp Low Warning'],
            ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
            ['Bias High Alarm', 'Bias Low Alarm', 'Bias High Warning', 'Bias Low Warning'],
            ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning'],
            ['RX Power High Alarm', 'RX Power Low Alarm', 'RX Power High Warning', 'RX Power Low Warning'],
            ['Optional Laser Temp High Alarm', 'Optional Laser Temp Low Alarm', 'Optional Laser Temp High Warning', 'Optional Laser Temp Low Warning'],
            ['Optional TEC Current High Alarm', 'Optional TEC Current Low Alarm', 'Optional TEC Current High Warning', 'Optional TEC Current Low Warning']
            ]
        line_color = [
            "background-color:green", "background-color:red"
        ]
        line_data = [
            'Temperature', "Vcc", 'Bias', 'TX Power', 'RX Power', 'OLT', 'OTC'
        ]

        try:
            item = self.core.classify(line_data, line_threshold, self.core.threshold_dict, line_edit, line_color)
            for i in item:
                eval(i).setStyleSheet(item[i])
        except Exception as e:
            print(e)

        del self.core.threshold_0_39[:]
        del self.core.threshold_40_55[:]
        del self.core.present_96_105[:]
        del self.core.optional_106_109[:]
        del self.cache[:]
        del self.receive_words
        self.core.threshold_dict = {}

    def color_qsfp(self):
        # self.cache = cache01
        try:
            data = self.core.opposition_qsfp(self.cache)
            print(data)
        except Exception as e:
            print(e)
        
    def digital_qsfp(self):
        try:
            self.lineEdit_Temp_Q.setText(str(round(self.core.threshold_qsfp['Temperature'], 2)))
            self.lineEdit_VCC_Q.setText(str(round(self.core.threshold_qsfp['Vcc'], 2)))

            self.lineEdit_TX1_Bias.setText(str(round(self.core.threshold_qsfp['TX1 Bias'], 2)))
            self.lineEdit_TX2_Bias.setText(str(round(self.core.threshold_qsfp['TX2 Bias'], 2)))
            self.lineEdit_TX3_Bias.setText(str(round(self.core.threshold_qsfp['TX3 Bias'], 2)))
            self.lineEdit_TX4_Bias.setText(str(round(self.core.threshold_qsfp['TX4 Bias'], 2)))

            self.lineEdit_TX1_Power.setText(str(round(self.core.threshold_qsfp['TX1 Power'], 2)))
            self.lineEdit_TX2_Power.setText(str(round(self.core.threshold_qsfp['TX2 Power'], 2)))
            self.lineEdit_TX3_Power.setText(str(round(self.core.threshold_qsfp['TX3 Power'], 2)))
            self.lineEdit_TX4_Power.setText(str(round(self.core.threshold_qsfp['TX4 Power'], 2)))

            self.lineEdit_RX1_Power.setText(str(round(self.core.threshold_qsfp['RX1 Power'], 2)))
            self.lineEdit_RX2_Power.setText(str(round(self.core.threshold_qsfp['RX2 Power'], 2)))
            self.lineEdit_RX3_Power.setText(str(round(self.core.threshold_qsfp['RX3 Power'], 2)))
            self.lineEdit_RX4_Power.setText(str(round(self.core.threshold_qsfp['RX4 Power'], 2)))

        except Exception as e:
            print(e)
        line_edit = [
            'self.lineEdit_Temp_Q_1', 'self.lineEdit_Temp_Q_2', 'self.lineEdit_Temp_Q_3', 'self.lineEdit_Temp_Q_4', 
            'self.lineEdit_VCC_Q_1', 'self.lineEdit_VCC_Q_2', 'self.lineEdit_VCC_Q_3', 'self.lineEdit_VCC_Q_4',
            'self.lineEdit_Bias_Q_CH1_1', 'self.lineEdit_Bias_Q_CH2_1', 'self.lineEdit_Bias_Q_CH3_1', 'self.lineEdit_Bias_Q_CH4_1', 
            'self.lineEdit_Bias_Q_CH1_2', 'self.lineEdit_Bias_Q_CH2_2', 'self.lineEdit_Bias_Q_CH3_2', 'self.lineEdit_Bias_Q_CH4_2', 
            'self.lineEdit_Bias_Q_CH1_3', 'self.lineEdit_Bias_Q_CH2_3', 'self.lineEdit_Bias_Q_CH3_3', 'self.lineEdit_Bias_Q_CH4_3', 
            'self.lineEdit_Bias_Q_CH1_4', 'self.lineEdit_Bias_Q_CH2_4', 'self.lineEdit_Bias_Q_CH3_4', 'self.lineEdit_Bias_Q_CH4_4',
            'self.lineEdit_TXP_Q_CH1_1', 'self.lineEdit_TXP_Q_CH2_1', 'self.lineEdit_TXP_Q_CH3_1', 'self.lineEdit_TXP_Q_CH4_1', 
            'self.lineEdit_TXP_Q_CH1_2', 'self.lineEdit_TXP_Q_CH2_2', 'self.lineEdit_TXP_Q_CH3_2', 'self.lineEdit_TXP_Q_CH4_2', 
            'self.lineEdit_TXP_Q_CH1_3', 'self.lineEdit_TXP_Q_CH2_3', 'self.lineEdit_TXP_Q_CH3_3', 'self.lineEdit_TXP_Q_CH4_3', 
            'self.lineEdit_TXP_Q_CH1_4', 'self.lineEdit_TXP_Q_CH2_4', 'self.lineEdit_TXP_Q_CH3_4', 'self.lineEdit_TXP_Q_CH4_4',
            'self.lineEdit_RXP_Q_CH1_1', 'self.lineEdit_RXP_Q_CH2_1', 'self.lineEdit_RXP_Q_CH3_1', 'self.lineEdit_RXP_Q_CH4_1', 
            'self.lineEdit_RXP_Q_CH1_2', 'self.lineEdit_RXP_Q_CH2_2', 'self.lineEdit_RXP_Q_CH3_2', 'self.lineEdit_RXP_Q_CH4_2', 
            'self.lineEdit_RXP_Q_CH1_3', 'self.lineEdit_RXP_Q_CH2_3', 'self.lineEdit_RXP_Q_CH3_3', 'self.lineEdit_RXP_Q_CH4_3', 
            'self.lineEdit_RXP_Q_CH1_4', 'self.lineEdit_RXP_Q_CH2_4', 'self.lineEdit_RXP_Q_CH3_4', 'self.lineEdit_RXP_Q_CH4_4'
            ]
        line_color = [
            "background-color:green", "background-color:red"
        ]
        line_data = [
            ['Temperature'], 
            ['Vcc'], 
            ['TX1 Bias', 'TX2 Bias', 'TX3 Bias', 'TX4 Bias'], 
            ['TX1 Power', 'TX2 Power', 'TX3 Power', 'TX4 Power'], 
            ['RX1 Power', 'RX2 Power', 'RX3 Power', 'RX4 Power'], 
        ]
        line_threshold = [
            ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning' , 'Temp Low Warning'],
            ['Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning'],
            ['Bias High Alarm' , 'Bias Low Alarm' , 'Bias High Warning' , 'Bias Low Warning'],
            ['RX Power High Alarm' , 'RX Power Low Alarm', 'RX Power High Warning' , 'RX Power Low Warning'],
            ['TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning']
        ]
        try:
            item = self.core.classify_qsfp(line_data, line_threshold, self.core.threshold_qsfp, line_edit, line_color)
            for i in item:
                eval(i).setStyleSheet(item[i])
        except Exception as e:
            print(e)

        del self.core.qsfp_22_57[:]
        del self.core.qsfp_128_200[:]
        del self.cache[:]
        self.core.threshold_qsfp = {}

    def signal_work(self):
        """指示灯线程"""
        self.signalThread.start()

    def work(self):
        """门限线程"""
        global change
        change = False
        self.workThread.start()

    def bit_work(self):
        """ter显示线程"""
        self.ter_show_thread.start()

    def finish(self):
        """线程关闭"""
        # self.workThread.finished()
        global change
        change = True

    def password_register(self):
        """密码写入"""
        self.password_data = []  # 格式[ 地址 长度 A0/A2 数据 ]
        if self.checkBox_Cus.isChecked():
            try:
                cus_data_01 = self.core.hex_decode(self.lineEdit_Cus_1.text())
                self.password_data.append(cus_data_01)
                if self.radioButton_psw_A0.isChecked():
                    self.password_data.append(160)
                else:
                    self.password_data.append(162)
            except Exception as e:
                self.remind_window.remindshow("输入错误" + str(e))
        else:
            try:
                key_words_01 = self.comboBox_password_register.currentText().split(" ", 1)[1].split("-", 1)[0]
                main_hex_data = self.core.hex_decode(key_words_01)
                self.password_data.append(main_hex_data)
                self.password_data.append(162)
            except Exception as e:
                self.remind_window.remindshow("错误提示" + str(e))
        try:
            psw_num = self.lineEdit_PassWord.text().replace(" ", "")[1:12].split("-", 3)
            for j in psw_num:
                k = self.core.hex_decode(j)
                self.password_data.append(k)
            print(self.password_data)
            self.write_data(self.password_data, str(self.password_data))
            del self.password_data[:]
        except Exception as e:
            self.remind_window.remindshow("请输入密码" + "\n" + "错误语法提示：" + str(e))

    def page_show(self):
        """下拉栏写入"""
        if self.radioButton_data_A0.isChecked():
            self.comboBox_choose_register.clear()
            self.comboBox_read_register.clear()
            self.comboBox_choose_register.addItem("Low  128")
            self.comboBox_choose_register.addItem("High 128")
            self.comboBox_choose_register.addItem("ALL  256")
            self.comboBox_read_register.addItem("Low  128")
            self.comboBox_read_register.addItem("High 128")
            self.comboBox_read_register.addItem("ALL  256")
        elif self.radioButton_data_A2.isChecked():
            self.comboBox_choose_register.clear()
            self.comboBox_read_register.clear()
            self.comboBox_choose_register.addItem("Low  128")
            self.comboBox_choose_register.addItem("High 128")
            self.comboBox_read_register.addItem("Low  128")
            self.comboBox_read_register.addItem("High 128")

    def file_choose(self):
        """文件选择"""
        try:
            file = str(QtWidgets.QFileDialog.getExistingDirectory())
            print(file)
            for file_info in os.walk(file):
                self.files = file_info
                print(self.files[-1], type(self.files[-1]))
            self.lineEdit_file_name.setText(self.files[-1][0])
        except Exception as e:
            print(e)

    def data_register(self):
        """数据写入"""
        # del self.password_data[:]
        data_file = []
        position = self.comboBox_choose_register.currentText()
        print(position)
        try:
            if self.checkBox_selfwrite.isChecked():
                self.lineEdit_file_name.setText(self.files[-1][self.i+1])
                with open(self.files[0] + "//" + self.files[-1][self.i], mode="rb") as f:
                    data = f.read(128)
                    print(data)
                print(self.files[-1][self.i])
                self.i += 1
            else:
                with open(self.files[0] + "//" + str(self.lineEdit_file_name.text()), mode="rb") as f:
                    data = f.read(128)
            if self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "High 128":
                password_data = [0x80, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "Low  128":
                password_data = [0x00, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "ALL  256":
                password_data = [0x00, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A2.isChecked() and self.comboBox_choose_register.currentText() == "Low  128":
                password_data = [0x00, 0xA2]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A2.isChecked() and self.comboBox_choose_register.currentText() == "High 128":
                password_data = [0x80, 0xA2]
                data_file = self.core.data_setup(data, password_data)
            else:
                print("ERROR")
            self.write_data(data_file, str(self.files[-1][self.i-1]))
        except Exception as e:
            print(e)
            self.lineEdit_file_name.setText(f"文件写完，{self.i}")
            self.i = 0

    def product_info(self, value: dict):
        """信息读取"""
        try:
            self.write_register_a0(value)
            data = self.core.opposition_info(self.cache)
            self.lineEdit_Vendor_Name.setText(data["Name"])
            self.lineEdit_Vendor_OUI.setText(data["OUI"])
            print(data["OUI"], data["OUI"].encode("gbk"))
            self.lineEdit_Vendor_PN.setText(data["PN"])
            self.lineEdit_Vendor_SN.setText(data["SN"])
            self.lineEdit_Vendor_REV.setText(data["Version"])
            self.lineEdit_Vendor_Date.setText(data["Date"])
            del self.cache[:]
        except Exception as e:
            print(e)

    def product_write(self):
        """数据码复写"""
        data_file = []
        right_words = [
            [3, 4, 33, 16, 0, 0, 0, 0, 0, 0, 0, 6, 103, 0, 0, 0, 30, 30, 0, 0, 70, 83, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 0, 36, 0, 0, 83, 70, 80, 80, 45, 65, 79, 49, 48, 32, 32, 32, 32, 32, 32, 32, 49,
             46, 48, 32, 3, 82, 0, 153, 0, 26, 0, 0, 67, 50, 48, 48, 52, 49, 55, 50, 51, 49, 53, 32, 32, 32, 32, 32, 50,
             48, 52, 50, 52, 32, 32, 32, 104, 240, 1, 171, 0, 0, 17, 205, 224, 42, 190, 222, 180, 216, 227, 89, 111, 57,
             43, 21, 33, 100, 211, 0, 0, 0, 0, 0, 0, 0, 0, 0, 236, 170, 220, 67]
        ]
        try:
            name = self.lineEdit_Vendor_Name.text()
            oui = self.lineEdit_Vendor_OUI.text()
            pn = self.lineEdit_Vendor_PN.text()
            rev = self.lineEdit_Vendor_REV.text()
            sn = self.lineEdit_Vendor_SN.text()
            date = self.lineEdit_Vendor_Date.text()
            print(name, oui, pn, rev, sn, date)
            right_words[0][20: 37] = self.core.data_encode(name)
            key_words37_40 = self.core.data_encode(oui)
            print("3740：", key_words37_40)
            if key_words37_40[0:4] == [92, 120, 48, 48]:
                right_words[0][37: 40] = [36, 0, 0]
            else:
                right_words[0][37: 40] = self.core.data_encode(oui)
            right_words[0][40: 52] = self.core.data_encode(pn)
            right_words[0][56: 60] = self.core.data_encode(rev)
            right_words[0][68: 84] = self.core.data_encode(sn)
            right_words[0][84: 73] = self.core.data_encode(date)
            data = right_words[0]
            if self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "High 128":
                password_data = [0x80, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "Low  128":
                password_data = [0x00, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A0.isChecked() and self.comboBox_choose_register.currentText() == "ALL  256":
                password_data = [0x00, 0xA0]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A2.isChecked() and self.comboBox_choose_register.currentText() == "Low  128":
                password_data = [0x00, 0xA2]
                data_file = self.core.data_setup(data, password_data)
            elif self.radioButton_data_A2.isChecked() and self.comboBox_choose_register.currentText() == "High 128":
                password_data = [0x80, 0xA2]
                data_file = self.core.data_setup(data, password_data)
            else:
                print("ERROR")
            # print(data_file)
            self.write_data(data_file, "写入成功")
        except Exception as e:
            print(e)
    
    def version_read_A0(self):
        """工程师显示模式"""
        try:
            data = {
                "0": "128",
                "128": "128"
            }
            if self.radioButton_A0R.isChecked():
                self.write_register_a0(data)
                print("A0")
            elif self.radioButton_A2R.isChecked():
                self.write_register_a2(data)
                print("A2")
            version_A0_value = self.cache[1][0][1:129] + self.cache[1][1][1:129]
            version_A0_key = [
                'self.lineEdit_00R', 'self.lineEdit_01R', 'self.lineEdit_02R', 'self.lineEdit_03R', 'self.lineEdit_04R', 'self.lineEdit_05R', 'self.lineEdit_06R', 'self.lineEdit_07R', 'self.lineEdit_08R', 'self.lineEdit_09R', 'self.lineEdit_0AR', 'self.lineEdit_0BR', 'self.lineEdit_0CR', 'self.lineEdit_0DR', 'self.lineEdit_0ER', 'self.lineEdit_0FR', 
                'self.lineEdit_10R', 'self.lineEdit_11R', 'self.lineEdit_12R', 'self.lineEdit_13R', 'self.lineEdit_14R', 'self.lineEdit_15R', 'self.lineEdit_16R', 'self.lineEdit_17R', 'self.lineEdit_18R', 'self.lineEdit_19R', 'self.lineEdit_1AR', 'self.lineEdit_1BR', 'self.lineEdit_1CR', 'self.lineEdit_1DR', 'self.lineEdit_1ER', 'self.lineEdit_1FR', 
                'self.lineEdit_20R', 'self.lineEdit_21R', 'self.lineEdit_22R', 'self.lineEdit_23R', 'self.lineEdit_24R', 'self.lineEdit_25R', 'self.lineEdit_26R', 'self.lineEdit_27R', 'self.lineEdit_28R', 'self.lineEdit_29R', 'self.lineEdit_2AR', 'self.lineEdit_2BR', 'self.lineEdit_2CR', 'self.lineEdit_2DR', 'self.lineEdit_2ER', 'self.lineEdit_2FR', 
                'self.lineEdit_30R', 'self.lineEdit_31R', 'self.lineEdit_32R', 'self.lineEdit_33R', 'self.lineEdit_34R', 'self.lineEdit_35R', 'self.lineEdit_36R', 'self.lineEdit_37R', 'self.lineEdit_38R', 'self.lineEdit_39R', 'self.lineEdit_3AR', 'self.lineEdit_3BR', 'self.lineEdit_3CR', 'self.lineEdit_3DR', 'self.lineEdit_3ER', 'self.lineEdit_3FR', 
                'self.lineEdit_40R', 'self.lineEdit_41R', 'self.lineEdit_42R', 'self.lineEdit_43R', 'self.lineEdit_44R', 'self.lineEdit_45R', 'self.lineEdit_46R', 'self.lineEdit_47R', 'self.lineEdit_48R', 'self.lineEdit_49R', 'self.lineEdit_4AR', 'self.lineEdit_4BR', 'self.lineEdit_4CR', 'self.lineEdit_4DR', 'self.lineEdit_4ER', 'self.lineEdit_4FR', 
                'self.lineEdit_50R', 'self.lineEdit_51R', 'self.lineEdit_52R', 'self.lineEdit_53R', 'self.lineEdit_54R', 'self.lineEdit_55R', 'self.lineEdit_56R', 'self.lineEdit_57R', 'self.lineEdit_58R', 'self.lineEdit_59R', 'self.lineEdit_5AR', 'self.lineEdit_5BR', 'self.lineEdit_5CR', 'self.lineEdit_5DR', 'self.lineEdit_5ER', 'self.lineEdit_5FR', 
                'self.lineEdit_60R', 'self.lineEdit_61R', 'self.lineEdit_62R', 'self.lineEdit_63R', 'self.lineEdit_64R', 'self.lineEdit_65R', 'self.lineEdit_66R', 'self.lineEdit_67R', 'self.lineEdit_68R', 'self.lineEdit_69R', 'self.lineEdit_6AR', 'self.lineEdit_6BR', 'self.lineEdit_6CR', 'self.lineEdit_6DR', 'self.lineEdit_6ER', 'self.lineEdit_6FR', 
                'self.lineEdit_70R', 'self.lineEdit_71R', 'self.lineEdit_72R', 'self.lineEdit_73R', 'self.lineEdit_74R', 'self.lineEdit_75R', 'self.lineEdit_76R', 'self.lineEdit_77R', 'self.lineEdit_78R', 'self.lineEdit_79R', 'self.lineEdit_7AR', 'self.lineEdit_7BR', 'self.lineEdit_7CR', 'self.lineEdit_7DR', 'self.lineEdit_7ER', 'self.lineEdit_7FR', 
                'self.lineEdit_80R', 'self.lineEdit_81R', 'self.lineEdit_82R', 'self.lineEdit_83R', 'self.lineEdit_84R', 'self.lineEdit_85R', 'self.lineEdit_86R', 'self.lineEdit_87R', 'self.lineEdit_88R', 'self.lineEdit_89R', 'self.lineEdit_8AR', 'self.lineEdit_8BR', 'self.lineEdit_8CR', 'self.lineEdit_8DR', 'self.lineEdit_8ER', 'self.lineEdit_8FR', 
                'self.lineEdit_90R', 'self.lineEdit_91R', 'self.lineEdit_92R', 'self.lineEdit_93R', 'self.lineEdit_94R', 'self.lineEdit_95R', 'self.lineEdit_96R', 'self.lineEdit_97R', 'self.lineEdit_98R', 'self.lineEdit_99R', 'self.lineEdit_9AR', 'self.lineEdit_9BR', 'self.lineEdit_9CR', 'self.lineEdit_9DR', 'self.lineEdit_9ER', 'self.lineEdit_9FR', 
                'self.lineEdit_A0R', 'self.lineEdit_A1R', 'self.lineEdit_A2R', 'self.lineEdit_A3R', 'self.lineEdit_A4R', 'self.lineEdit_A5R', 'self.lineEdit_A6R', 'self.lineEdit_A7R', 'self.lineEdit_A8R', 'self.lineEdit_A9R', 'self.lineEdit_AAR', 'self.lineEdit_ABR', 'self.lineEdit_ACR', 'self.lineEdit_ADR', 'self.lineEdit_AER', 'self.lineEdit_AFR', 
                'self.lineEdit_B0R', 'self.lineEdit_B1R', 'self.lineEdit_B2R', 'self.lineEdit_B3R', 'self.lineEdit_B4R', 'self.lineEdit_B5R', 'self.lineEdit_B6R', 'self.lineEdit_B7R', 'self.lineEdit_B8R', 'self.lineEdit_B9R', 'self.lineEdit_BAR', 'self.lineEdit_BBR', 'self.lineEdit_BCR', 'self.lineEdit_BDR', 'self.lineEdit_BER', 'self.lineEdit_BFR', 
                'self.lineEdit_C0R', 'self.lineEdit_C1R', 'self.lineEdit_C2R', 'self.lineEdit_C3R', 'self.lineEdit_C4R', 'self.lineEdit_C5R', 'self.lineEdit_C6R', 'self.lineEdit_C7R', 'self.lineEdit_C8R', 'self.lineEdit_C9R', 'self.lineEdit_CAR', 'self.lineEdit_CBR', 'self.lineEdit_CCR', 'self.lineEdit_CDR', 'self.lineEdit_CER', 'self.lineEdit_CFR', 
                'self.lineEdit_D0R', 'self.lineEdit_D1R', 'self.lineEdit_D2R', 'self.lineEdit_D3R', 'self.lineEdit_D4R', 'self.lineEdit_D5R', 'self.lineEdit_D6R', 'self.lineEdit_D7R', 'self.lineEdit_D8R', 'self.lineEdit_D9R', 'self.lineEdit_DAR', 'self.lineEdit_DBR', 'self.lineEdit_DCR', 'self.lineEdit_DDR', 'self.lineEdit_DER', 'self.lineEdit_DFR', 
                'self.lineEdit_E0R', 'self.lineEdit_E1R', 'self.lineEdit_E2R', 'self.lineEdit_E3R', 'self.lineEdit_E4R', 'self.lineEdit_E5R', 'self.lineEdit_E6R', 'self.lineEdit_E7R', 'self.lineEdit_E8R', 'self.lineEdit_E9R', 'self.lineEdit_EAR', 'self.lineEdit_EBR', 'self.lineEdit_ECR', 'self.lineEdit_EDR', 'self.lineEdit_EER', 'self.lineEdit_EFR', 
                'self.lineEdit_F0R', 'self.lineEdit_F1R', 'self.lineEdit_F2R', 'self.lineEdit_F3R', 'self.lineEdit_F4R', 'self.lineEdit_F5R', 'self.lineEdit_F6R', 'self.lineEdit_F7R', 'self.lineEdit_F8R', 'self.lineEdit_F9R', 'self.lineEdit_FAR', 'self.lineEdit_FBR', 'self.lineEdit_FCR', 'self.lineEdit_FDR', 'self.lineEdit_FER', 'self.lineEdit_FFR'
            ]
            if self.radioButton_DEC.isChecked():
                for i in range(1, 256):
                    eval(version_A0_key[i]).setText(str(version_A0_value[i]))
            elif self.radioButton_HEX.isChecked():
                for i in range(256):
                    eval(version_A0_key[i]).setText(hex(int(str(version_A0_value[i]))))
            self.textEdit_R.setText(str(self.cache[1][0][1:129]) + "\n" + str(self.cache[1][1][1:129]))
            del self.cache[:]
        except Exception as e:
            print(e)


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