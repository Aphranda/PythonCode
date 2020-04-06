from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QToolTip
import sys
from threading import Timer
import random
import serial
import serial.tools.list_ports


class Ui_Form(object):
    def setupUi(self, Form):
        """控件位置"""
        Form.setObjectName("Form")
        Form.resize(299, 241)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 277, 78))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 160, 56))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 160, 56))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 110, 51, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """控件数据"""
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登陆界面"))
        self.label.setText(_translate("Form", "端口："))
        self.comboBox_2.setItemText(0, _translate("Form", "COM1"))
        self.comboBox_2.setItemText(1, _translate("Form", "COM2"))
        self.comboBox_2.setItemText(2, _translate("Form", "COM3"))
        self.comboBox_2.setItemText(3, _translate("Form", "COM4"))
        self.comboBox_2.setItemText(4, _translate("Form", "COM5"))
        self.comboBox_2.setItemText(5, _translate("Form", "COM6"))
        self.comboBox_2.setItemText(6, _translate("Form", "COM7"))
        self.comboBox_2.setItemText(7, _translate("Form", "COM8"))
        self.comboBox_2.setItemText(8, _translate("Form", "COM9"))
        # combobox_port = self.comboBox_2
        # combobox_port.activated(str).connect()
        self.label_2.setText(_translate("Form", "波特率："))
        self.comboBox.setItemText(0, _translate("Form", "1200"))
        self.comboBox.setItemText(1, _translate("Form", "2400"))
        self.comboBox.setItemText(2, _translate("Form", "4800"))
        self.comboBox.setItemText(3, _translate("Form", "9600"))
        self.comboBox.setItemText(4, _translate("Form", "19200"))
        self.comboBox.setItemText(5, _translate("Form", "38400"))
        # combobox_bundrate = self.comboBox
        # combobox_bundrate.activated(str).connect()
        self.label_3.setText(_translate("Form", "姓名："))
        self.label_4.setText(_translate("Form", "工号："))
        self.label_6.setText(_translate("Form", "单号："))
        self.label_5.setText(_translate("Form", "时间："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton.clicked.connect(self.store_data)
        self.pushButton.clicked.connect(self.start_port)
        self.pushButton.clicked.connect(self.read_port)
        # self.pushButton.clicked.connect(self.store_data)
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton_2.clicked.connect(QCoreApplication.quit)
        combobox_port = self.comboBox_2
        combobox_port.currentIndexChanged.connect(self.tie_port)
        combobox_rate = self.comboBox
        combobox_rate.currentIndexChanged.connect(self.tie_port)
        content_port = combobox_port.currentText()
        content_rate = combobox_rate.currentText()
        print(content_port, content_rate)


    def tie_port(self):
        """暂存串口资料"""
        self.serialport = self.comboBox_2.currentText()
        self.bundrate = self.comboBox.currentText()
        print(self.serialport, self.bundrate)

    def start_port(self):
        """接入串口"""
        serialport = self.serialport
        bundrate = self.bundrate
        print(serialport, bundrate)
        self.ser = serial.Serial(serialport, bundrate, timeout=0.5)

    def read_port(self):
        """定时读取串口信息"""
        # a = self.ser.read(size=50)
        # b = a.decode('utf-8')
        # number = random.randint(1, 100)
        # print('发送数据:', number)
        # self.ser.write('BB')
        # print('接收数据：', b)  # 可以接受中文
        # t = Timer(1, self.read_port)
        # t.start()
        pass

    # while 1:
        #     str = input("请输入要发送的数据：")
        #     ser.write((str + '\n').encode())
        #     a = ser.read(size=50)
        #     b = a.decode('utf-8')
        #     print('接收数据：', b)  # 可以接受中文

    def store_data(self):
        self.name = self.lineEdit.text()
        self.number = self.lineEdit_2.text()
        self.order = self.lineEdit_3.text()
        self.date = self.lineEdit_4.text()
        print(self.name, self.number, self.order, self.date)


def star_program():
    app = QtWidgets.QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    app.exit(app.exec_())


#  获取端口列表
def get_port(none_list):
    port_list = list(serial.tools.list_ports.comports())
    port_list.append(1)
    a = none_list
    for port in port_list:
        # print(port)
        port_num = str(port)
        # print(port_num)
        # 获取端口名称
        last = port_num.split(' - ', 1)[0]
        if len(a) != len(port_list)-1:
            a.append(last)
            # print(a)
        else:
            return a




if __name__ == '__main__':
    none_list = list()
    all_port = get_port(none_list)
    print(all_port)
    star_program()