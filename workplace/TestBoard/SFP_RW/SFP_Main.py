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

change = False

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
    delete_data = QtCore.pyqtSignal()

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

        # 线程连接代码，刷新测试数据
        try:
            self.workThread.receiver_data.connect(lambda: self.color_read(self.core.register_a2_sfp))
            self.workThread.show_data.connect(self.digital)
            self.signalThread.signal_begin.connect(self.signal_colors)
            self.pushButton_OK.clicked.connect(self.work)
            self.pushButton_link_com.clicked.connect(self.signal_work)
            self.pushButton_sweep_auto_W.clicked.connect(self.signal_work)
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

        # 误码仪启动
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_start)

        # 误码仪停止
        self.pushButton_WMA__STOP.clicked.connect(self.ter_wan_stop)

        # Tx Rx Pattern 模式写入
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_pattern)

        # Tx Rx 传输速度写入
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_speed)

        # 时钟频率写入
        self.pushButton_WMA__START.clicked.connect(self.ter_clock_speed)

        # 振幅写入
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_amp)

        # 插入误码写入
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_error)

        # 补偿写入
        self.pushButton_WMA__START.clicked.connect(self.ter_wan_compensate)

        # ter_show线程实例化
        self.ter_show_thread = Ter_show()

        # 线程链接
        self.ter_show_thread.bit_show.connect(self.ter_wan_show)
        self.pushButton_WMA__START.clicked.connect(self.bit_work)

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

    def write_bit_error(self):
        """向误码仪中写入数据"""
        pass

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
        pass

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

    def ter_wan_start(self):
        """误码仪启动"""
        try:
            key_words = "0xff"
            trans_data = [0x7e, 0x10, 0x80, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            receive_data = self.write_data_wm(trans_data)
            print("启动返回值", receive_data)
            if key_words in str(receive_data) or len(receive_data) == 0:
                print("启动设置失败")
            else:
                print("启动设置成功")
        except Exception as e:
            print("start", e)
        
    def ter_wan_stop(self):
        """误码仪停止"""
        try:
            key_words = "0xff"
            trans_data = [0x7e, 0x10, 0x80, 0x00, 0x03, 0x01, 0x00, 0x01, 0x00, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            receive_data = self.write_data_wm(trans_data)
            print("停止返回值", receive_data)
            if key_words in str(receive_data) or len(receive_data) == 0:
                self.remind_window.remindshow("停止设置失败")
            else:
                self.remind_window.remindshow("停止设置成功")
        except Exception as e:
            print("stop", e)
     
    def ter_wan_pattern(self):
        """误码仪Pattern类型"""
        try:
            example = {
                "PRBS07": 0x00,
                "PRBS09": 0x01,
                "PRBS11": 0x02,
                "PRBS15": 0x03,
                "PRBS23": 0x04,
                "PRBS31": 0x05,
                "PRBSSW": 0x06,
            }
            pattern_data_key = self.comboBox_WMA_Pattern.currentText()
            pattern_data_value = example[pattern_data_key]
            key_words = "0xff"
            trans_data = [0x7e, 0x10, 0x82, 0x00, 0x03, 0x01, 0x00, pattern_data_value, 0x00, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            print("模式", trans_data)
            receive_data = self.write_data_wm(trans_data)
            print("模式返回值", receive_data)
            if key_words in str(receive_data) or len(receive_data) == 0:
                print("模式设置失败")
            else:
                print("模式设置成功")
        except Exception as e:
            print("pattern" + str(e))

    def ter_wan_speed(self):
        try:
            example = {
                "9.95G": 0x00,
                "10.31G": 0x01,
                "11.31G": 0x02,
                "12.16G": 0x03,
                "14.02G": 0x04,
                "22.77G": 0x05,
                "24.33G": 0x06,
                "25.78G": 0x07,
                "27.95G": 0x08,
                "28.05G": 0x09,
            }
            pattern_data_key = self.comboBox_WMA_Pattern_V.currentText()
            pattern_data_value = example[pattern_data_key]
            key_words = "0xff"
            trans_data = [0x7e, 0x10, 0x84, 0x00, 0x03, 0x01, 0x00, pattern_data_value, 0x00, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            print("速度", trans_data)
            receive_data = self.write_data_wm(trans_data)
            print("速度返回值", receive_data)
            if key_words in str(receive_data) or len(receive_data) == 0:
                print("速度设置失败")
            else:
                print("速度设置成功")
        except Exception as e:
            print("pattern" + str(e))
    
    def ter_clock_speed(self):
        try:
            example = {
                "8bit": 0x00,
                "16bit": 0x01,
                "off": 0x02
            }
            pattern_data_key = self.comboBox_WMA_Pattern_HM.currentText()
            pattern_data_value = example[pattern_data_key]
            key_words = "0xff"
            trans_data = [0x7e, 0x10, 0x88, 0x00, 0x03, 0x01, 0x00, pattern_data_value, 0x00, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            print("时钟", trans_data)
            receive_data = self.write_data_wm(trans_data)
            print("时钟返回值", receive_data)
            if key_words in str(receive_data) or len(receive_data) == 0:
                print("时钟设置失败")
            else:
                print("时钟设置成功")
        except Exception as e:
            print("pattern" + str(e))

    def ter_wan_amp(self):
        try:
            example = {
                "0mV": 0x00,
                "250mV": 0x01,
                "500mV": 0x02,
                "750mV": 0x03,
                "1000mV": 0x04
            }
            key_words = "0xff"
            pattern_data_CH1 = self.comboBox_WMA_ZF_CH1.currentText()
            pattern_data_value_CH1 = example[pattern_data_CH1]
            trans_data_CH1 = [0x7e, 0x10, 0x8A, 0x00, 0x03, 0x01, 0x00, pattern_data_value_CH1, 0x00, 0x7e]

            pattern_data_CH2 = self.comboBox_WMA_ZF_CH2.currentText()
            pattern_data_value_CH2 = example[pattern_data_CH2]
            trans_data_CH2 = [0x7e, 0x10, 0x8A, 0x00, 0x03, 0x01, 0x01, pattern_data_value_CH2, 0x00, 0x7e]

            pattern_data_CH3 = self.comboBox_WMA_ZF_CH3.currentText()
            pattern_data_value_CH3 = example[pattern_data_CH3]
            trans_data_CH3 = [0x7e, 0x10, 0x8A, 0x00, 0x03, 0x01, 0x02, pattern_data_value_CH3, 0x00, 0x7e]

            pattern_data_CH4 = self.comboBox_WMA_ZF_CH4.currentText()
            pattern_data_value_CH4 = example[pattern_data_CH4]
            trans_data_CH4 = [0x7e, 0x10, 0x8A, 0x00, 0x03, 0x01, 0x03, pattern_data_value_CH4, 0x00, 0x7e]

            trans_data = [trans_data_CH1, trans_data_CH2, trans_data_CH3, trans_data_CH4]
            for i in trans_data:
                trans_len = sum(i[1:-2])
                i[-2] = trans_len
                print("振幅", i)
                receive_data = self.write_data_wm(i)
                print("振幅返回值", receive_data)
                if key_words in str(receive_data) or len(receive_data) == 0:
                    print(f"CH{i[6] + 1}设置失败")
                else:
                    print(f"CH{i[6] + 1}设置成功")
        except Exception as e:
            print("pattern" + str(e))
    
    def ter_wan_error(self):
        try:
            example = {
                "0": 0x00,
                "1": 0x01
            }
            key_words = "0xff"
            pattern_data_CH1 = self.comboBox_WMA_ERROR_CH1.currentText()
            pattern_data_value_CH1 = example[pattern_data_CH1]
            trans_data_CH1 = [0x7e, 0x10, 0x88, 0x00, 0x03, 0x01, 0x00, pattern_data_value_CH1, 0x00, 0x7e]

            pattern_data_CH2 = self.comboBox_WMA_ERROR_CH2.currentText()
            pattern_data_value_CH2 = example[pattern_data_CH2]
            trans_data_CH2 = [0x7e, 0x10, 0x88, 0x00, 0x03, 0x01, 0x01, pattern_data_value_CH2, 0x00, 0x7e]

            pattern_data_CH3 = self.comboBox_WMA_ERROR_CH3.currentText()
            pattern_data_value_CH3 = example[pattern_data_CH3]
            trans_data_CH3 = [0x7e, 0x10, 0x88, 0x00, 0x03, 0x01, 0x02, pattern_data_value_CH3, 0x00, 0x7e]

            pattern_data_CH4 = self.comboBox_WMA_ERROR_CH4.currentText()
            pattern_data_value_CH4 = example[pattern_data_CH4]
            trans_data_CH4 = [0x7e, 0x10, 0x88, 0x00, 0x03, 0x01, 0x03, pattern_data_value_CH4, 0x00, 0x7e]

            trans_data = [trans_data_CH1, trans_data_CH2, trans_data_CH3, trans_data_CH4]
            for i in trans_data:
                trans_len = sum(i[1:-2])
                i[-2] = trans_len
                print("误码", i)
                receive_data = self.write_data_wm(i)
                if key_words in str(receive_data) or len(receive_data) == 0:
                    print(f"CH{i[6] + 1}设置失败")
                else:
                    print(f"CH{i[6] + 1}设置成功")
        except Exception as e:
            print("pattern" + str(e))

    def ter_wan_compensate(self):
        try:
            example = {
                "-1.0dB": 0x00,
                "-0.5dB": 0x01,
                "0dB": 0x02,
                "0.5dB": 0x03,
                "1.0dB": 0x04,
                "1.5dB": 0x05,
                "2.0dB": 0x06,
                "2.5dB": 0x07,
            }
            key_words = "0xff"
            pattern_data_CH1 = self.comboBox_WMA_BC_CH1.currentText()
            pattern_data_value_CH1 = example[pattern_data_CH1]
            trans_data_CH1 = [0x7e, 0x10, 0x8C, 0x00, 0x03, 0x01, 0x00, pattern_data_value_CH1, 0x00, 0x7e]

            pattern_data_CH2 = self.comboBox_WMA_BC_CH2.currentText()
            pattern_data_value_CH2 = example[pattern_data_CH2]
            trans_data_CH2 = [0x7e, 0x10, 0x8C, 0x00, 0x03, 0x01, 0x01, pattern_data_value_CH2, 0x00, 0x7e]

            pattern_data_CH3 = self.comboBox_WMA_BC_CH3.currentText()
            pattern_data_value_CH3 = example[pattern_data_CH3]
            trans_data_CH3 = [0x7e, 0x10, 0x8C, 0x00, 0x03, 0x01, 0x02, pattern_data_value_CH3, 0x00, 0x7e]

            pattern_data_CH4 = self.comboBox_WMA_BC_CH4.currentText()
            pattern_data_value_CH4 = example[pattern_data_CH4]
            trans_data_CH4 = [0x7e, 0x10, 0x8C, 0x00, 0x03, 0x01, 0x03, pattern_data_value_CH4, 0x00, 0x7e]

            trans_data = [trans_data_CH1, trans_data_CH2, trans_data_CH3, trans_data_CH4]
            for i in trans_data:
                trans_len = sum(i[1:-2])
                i[-2] = trans_len
                print("补偿", i)
                receive_data = self.write_data_wm(i)
                print(receive_data)
                if key_words in str(receive_data) or len(receive_data) == 0:
                    print(f"CH{i[6] + 1}设置失败")
                else:
                    print(f"CH{i[6] + 1}设置成功")
        except Exception as e:
            print("pattern" + str(e))       

    def ter_wan_lock(self):
        try:
            trans_data = [0x7e, 0x10, 0x02, 0x00, 0x00, 0x12, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            receive_data = self.write_data_wm(trans_data)
            print("lock", receive_data)
            return receive_data
        except Exception as e:
            print("lock", e)

    def ter_wan_exist(self):
        try:
            trans_data = [0x7e, 0x10, 0x06, 0x00, 0x00, 0x16, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            receive_data = self.write_data_wm(trans_data)
            print("lock", receive_data)
            return receive_data
        except Exception as e:
            print("lock", e)      

    def ter_wan_rate(self):
        try:
            trans_data = [0x7e, 0x10, 0x08, 0x00, 0x00, 0x18, 0x7e]
            trans_len = sum(trans_data[1:-2])
            trans_data[-2] = trans_len
            receive_data = self.write_data_wm(trans_data)
            print("rate", receive_data)
            return receive_data
        except Exception as e:
            print("rate", e) 

    def ter_wan_show(self):
        a = self.ter_wan_lock()
        b = self.ter_wan_exist()
        c = self.ter_wan_rate()
        print("A" + str(a) + "\n" + "B" + str(b) + "\n" + "C" + str(c))


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