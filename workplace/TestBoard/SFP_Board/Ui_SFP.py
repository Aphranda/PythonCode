# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PythonCode\code\workplace\TestBoard\SFP_Board\SFP.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 702)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/maple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.COM_fram = QtWidgets.QFrame(self.centralwidget)
        self.COM_fram.setGeometry(QtCore.QRect(10, 10, 481, 61))
        self.COM_fram.setFrameShape(QtWidgets.QFrame.Box)
        self.COM_fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.COM_fram.setLineWidth(2)
        self.COM_fram.setObjectName("COM_fram")
        self.comboBox_com = QtWidgets.QComboBox(self.COM_fram)
        self.comboBox_com.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.comboBox_com.setFont(font)
        self.comboBox_com.setObjectName("comboBox_com")
        self.pushButton_link_com = QtWidgets.QPushButton(self.COM_fram)
        self.pushButton_link_com.setGeometry(QtCore.QRect(200, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_link_com.setFont(font)
        self.pushButton_link_com.setObjectName("pushButton_link_com")
        self.pushButton_sweep_com = QtWidgets.QPushButton(self.COM_fram)
        self.pushButton_sweep_com.setGeometry(QtCore.QRect(340, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_sweep_com.setFont(font)
        self.pushButton_sweep_com.setObjectName("pushButton_sweep_com")
        self.DDM_fram = QtWidgets.QFrame(self.centralwidget)
        self.DDM_fram.setGeometry(QtCore.QRect(10, 100, 481, 571))
        self.DDM_fram.setFrameShape(QtWidgets.QFrame.Box)
        self.DDM_fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DDM_fram.setLineWidth(2)
        self.DDM_fram.setObjectName("DDM_fram")
        self.lineEdit_Temp = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_Temp.setGeometry(QtCore.QRect(100, 40, 71, 31))
        self.lineEdit_Temp.setObjectName("lineEdit_Temp")
        self.lineEdit_VCC = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_VCC.setGeometry(QtCore.QRect(330, 40, 71, 31))
        self.lineEdit_VCC.setObjectName("lineEdit_VCC")
        self.label_temp = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp.setGeometry(QtCore.QRect(40, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_VCC = QtWidgets.QLabel(self.DDM_fram)
        self.label_VCC.setGeometry(QtCore.QRect(270, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_VCC.setFont(font)
        self.label_VCC.setObjectName("label_VCC")
        self.label_temp_3 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_3.setGeometry(QtCore.QRect(180, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_3.setFont(font)
        self.label_temp_3.setObjectName("label_temp_3")
        self.label_temp_4 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_4.setGeometry(QtCore.QRect(420, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_4.setFont(font)
        self.label_temp_4.setObjectName("label_temp_4")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.DDM_fram)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(30, 200, 281, 270))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_D = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_D.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_D.setObjectName("gridLayout_D")
        self.lineEdit_INIT = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_INIT.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_INIT.setObjectName("lineEdit_INIT")
        self.gridLayout_D.addWidget(self.lineEdit_INIT, 9, 3, 1, 1)
        self.label_temp_23 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_23.setFont(font)
        self.label_temp_23.setObjectName("label_temp_23")
        self.gridLayout_D.addWidget(self.label_temp_23, 5, 0, 1, 1)
        self.label_temp_43 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_43.setMaximumSize(QtCore.QSize(60, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_43.setFont(font)
        self.label_temp_43.setObjectName("label_temp_43")
        self.gridLayout_D.addWidget(self.label_temp_43, 2, 0, 1, 1)
        self.label_temp_22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_22.setFont(font)
        self.label_temp_22.setObjectName("label_temp_22")
        self.gridLayout_D.addWidget(self.label_temp_22, 6, 0, 1, 1)
        self.label_temp_24 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_24.setFont(font)
        self.label_temp_24.setObjectName("label_temp_24")
        self.gridLayout_D.addWidget(self.label_temp_24, 4, 0, 1, 1)
        self.label_temp_69 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_69.setMaximumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_temp_69.setFont(font)
        self.label_temp_69.setObjectName("label_temp_69")
        self.gridLayout_D.addWidget(self.label_temp_69, 1, 2, 1, 1)
        self.lineEdit_Temp_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Temp_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Temp_1.setObjectName("lineEdit_Temp_1")
        self.gridLayout_D.addWidget(self.lineEdit_Temp_1, 2, 1, 1, 1)
        self.lineEdit_TxP_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_TxP_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_TxP_2.setObjectName("lineEdit_TxP_2")
        self.gridLayout_D.addWidget(self.lineEdit_TxP_2, 5, 2, 1, 1)
        self.lineEdit_VCC_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_VCC_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_VCC_2.setObjectName("lineEdit_VCC_2")
        self.gridLayout_D.addWidget(self.lineEdit_VCC_2, 3, 2, 1, 1)
        self.lineEdit_Bias_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Bias_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Bias_3.setObjectName("lineEdit_Bias_3")
        self.gridLayout_D.addWidget(self.lineEdit_Bias_3, 4, 3, 1, 1)
        self.lineEdit_Bias_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Bias_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Bias_2.setObjectName("lineEdit_Bias_2")
        self.gridLayout_D.addWidget(self.lineEdit_Bias_2, 4, 2, 1, 1)
        self.label_temp_42 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_42.setMaximumSize(QtCore.QSize(36, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_42.setFont(font)
        self.label_temp_42.setObjectName("label_temp_42")
        self.gridLayout_D.addWidget(self.label_temp_42, 3, 0, 1, 1)
        self.label_temp_27 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_27.setFont(font)
        self.label_temp_27.setObjectName("label_temp_27")
        self.gridLayout_D.addWidget(self.label_temp_27, 7, 0, 1, 1)
        self.lineEdit_TxP_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_TxP_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_TxP_4.setObjectName("lineEdit_TxP_4")
        self.gridLayout_D.addWidget(self.lineEdit_TxP_4, 5, 4, 1, 1)
        self.lineEdit_Bias_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Bias_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Bias_4.setObjectName("lineEdit_Bias_4")
        self.gridLayout_D.addWidget(self.lineEdit_Bias_4, 4, 4, 1, 1)
        self.lineEdit_TxP_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_TxP_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_TxP_3.setObjectName("lineEdit_TxP_3")
        self.gridLayout_D.addWidget(self.lineEdit_TxP_3, 5, 3, 1, 1)
        self.label_temp_70 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_70.setMaximumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_temp_70.setFont(font)
        self.label_temp_70.setObjectName("label_temp_70")
        self.gridLayout_D.addWidget(self.label_temp_70, 1, 4, 1, 1)
        self.lineEdit_VCC_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_VCC_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_VCC_1.setObjectName("lineEdit_VCC_1")
        self.gridLayout_D.addWidget(self.lineEdit_VCC_1, 3, 1, 1, 1)
        self.lineEdit_VCC_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_VCC_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_VCC_4.setObjectName("lineEdit_VCC_4")
        self.gridLayout_D.addWidget(self.lineEdit_VCC_4, 3, 4, 1, 1)
        self.lineEdit_RxP_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_RxP_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_RxP_3.setObjectName("lineEdit_RxP_3")
        self.gridLayout_D.addWidget(self.lineEdit_RxP_3, 6, 3, 1, 1)
        self.lineEdit_VCC_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_VCC_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_VCC_3.setObjectName("lineEdit_VCC_3")
        self.gridLayout_D.addWidget(self.lineEdit_VCC_3, 3, 3, 1, 1)
        self.lineEdit_Temp_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Temp_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Temp_4.setObjectName("lineEdit_Temp_4")
        self.gridLayout_D.addWidget(self.lineEdit_Temp_4, 2, 4, 1, 1)
        self.lineEdit_RxP_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_RxP_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_RxP_4.setObjectName("lineEdit_RxP_4")
        self.gridLayout_D.addWidget(self.lineEdit_RxP_4, 6, 4, 1, 1)
        self.lineEdit_Temp_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Temp_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Temp_2.setObjectName("lineEdit_Temp_2")
        self.gridLayout_D.addWidget(self.lineEdit_Temp_2, 2, 2, 1, 1)
        self.lineEdit_RxP_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_RxP_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_RxP_2.setObjectName("lineEdit_RxP_2")
        self.gridLayout_D.addWidget(self.lineEdit_RxP_2, 6, 2, 1, 1)
        self.lineEdit_Bias_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Bias_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Bias_1.setObjectName("lineEdit_Bias_1")
        self.gridLayout_D.addWidget(self.lineEdit_Bias_1, 4, 1, 1, 1)
        self.label_temp_75 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_75.setMaximumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_temp_75.setFont(font)
        self.label_temp_75.setObjectName("label_temp_75")
        self.gridLayout_D.addWidget(self.label_temp_75, 1, 1, 1, 1)
        self.label_temp_71 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_71.setMaximumSize(QtCore.QSize(40, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_temp_71.setFont(font)
        self.label_temp_71.setObjectName("label_temp_71")
        self.gridLayout_D.addWidget(self.label_temp_71, 1, 3, 1, 1)
        self.lineEdit_Temp_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Temp_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_Temp_3.setObjectName("lineEdit_Temp_3")
        self.gridLayout_D.addWidget(self.lineEdit_Temp_3, 2, 3, 1, 1)
        self.lineEdit_RxP_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_RxP_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_RxP_1.setObjectName("lineEdit_RxP_1")
        self.gridLayout_D.addWidget(self.lineEdit_RxP_1, 6, 1, 1, 1)
        self.lineEdit_TxP_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_TxP_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_TxP_1.setObjectName("lineEdit_TxP_1")
        self.gridLayout_D.addWidget(self.lineEdit_TxP_1, 5, 1, 1, 1)
        self.label_temp_44 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_temp_44.setMaximumSize(QtCore.QSize(1000, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.label_temp_44.setFont(font)
        self.label_temp_44.setObjectName("label_temp_44")
        self.gridLayout_D.addWidget(self.label_temp_44, 9, 0, 1, 3)
        self.label_temp_26 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_26.setFont(font)
        self.label_temp_26.setObjectName("label_temp_26")
        self.gridLayout_D.addWidget(self.label_temp_26, 8, 0, 1, 1)
        self.lineEdit_OLT_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OLT_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OLT_1.setObjectName("lineEdit_OLT_1")
        self.gridLayout_D.addWidget(self.lineEdit_OLT_1, 7, 1, 1, 1)
        self.lineEdit_OLT_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OLT_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OLT_2.setObjectName("lineEdit_OLT_2")
        self.gridLayout_D.addWidget(self.lineEdit_OLT_2, 7, 2, 1, 1)
        self.lineEdit_OLT_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OLT_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OLT_3.setObjectName("lineEdit_OLT_3")
        self.gridLayout_D.addWidget(self.lineEdit_OLT_3, 7, 3, 1, 1)
        self.lineEdit_OLT_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OLT_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OLT_4.setObjectName("lineEdit_OLT_4")
        self.gridLayout_D.addWidget(self.lineEdit_OLT_4, 7, 4, 1, 1)
        self.lineEdit_OTC_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OTC_1.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OTC_1.setObjectName("lineEdit_OTC_1")
        self.gridLayout_D.addWidget(self.lineEdit_OTC_1, 8, 1, 1, 1)
        self.lineEdit_OTC_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OTC_2.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OTC_2.setObjectName("lineEdit_OTC_2")
        self.gridLayout_D.addWidget(self.lineEdit_OTC_2, 8, 2, 1, 1)
        self.lineEdit_OTC_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OTC_3.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OTC_3.setObjectName("lineEdit_OTC_3")
        self.gridLayout_D.addWidget(self.lineEdit_OTC_3, 8, 3, 1, 1)
        self.lineEdit_OTC_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_OTC_4.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_OTC_4.setObjectName("lineEdit_OTC_4")
        self.gridLayout_D.addWidget(self.lineEdit_OTC_4, 8, 4, 1, 1)
        self.lineEdit_green = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_green.setGeometry(QtCore.QRect(160, 500, 39, 24))
        self.lineEdit_green.setMaximumSize(QtCore.QSize(39, 24))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_green.setPalette(palette)
        self.lineEdit_green.setObjectName("lineEdit_green")
        self.lineEdit_white = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_white.setGeometry(QtCore.QRect(30, 500, 39, 24))
        self.lineEdit_white.setMaximumSize(QtCore.QSize(39, 24))
        self.lineEdit_white.setObjectName("lineEdit_white")
        self.lineEdit_red = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_red.setGeometry(QtCore.QRect(300, 500, 39, 24))
        self.lineEdit_red.setMaximumSize(QtCore.QSize(39, 24))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_red.setPalette(palette)
        self.lineEdit_red.setObjectName("lineEdit_red")
        self.label_2 = QtWidgets.QLabel(self.DDM_fram)
        self.label_2.setGeometry(QtCore.QRect(80, 510, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.DDM_fram)
        self.label_3.setGeometry(QtCore.QRect(210, 510, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.DDM_fram)
        self.label_4.setGeometry(QtCore.QRect(360, 510, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_temp_2 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_2.setGeometry(QtCore.QRect(40, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_2.setFont(font)
        self.label_temp_2.setObjectName("label_temp_2")
        self.lineEdit_Bias = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_Bias.setGeometry(QtCore.QRect(100, 90, 71, 31))
        self.lineEdit_Bias.setObjectName("lineEdit_Bias")
        self.label_temp_5 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_5.setGeometry(QtCore.QRect(190, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_5.setFont(font)
        self.label_temp_5.setObjectName("label_temp_5")
        self.label_VCC_2 = QtWidgets.QLabel(self.DDM_fram)
        self.label_VCC_2.setGeometry(QtCore.QRect(40, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_VCC_2.setFont(font)
        self.label_VCC_2.setObjectName("label_VCC_2")
        self.lineEdit_TxP = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_TxP.setGeometry(QtCore.QRect(100, 140, 71, 31))
        self.lineEdit_TxP.setObjectName("lineEdit_TxP")
        self.label_temp_6 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_6.setGeometry(QtCore.QRect(190, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_6.setFont(font)
        self.label_temp_6.setObjectName("label_temp_6")
        self.label_VCC_3 = QtWidgets.QLabel(self.DDM_fram)
        self.label_VCC_3.setGeometry(QtCore.QRect(270, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_VCC_3.setFont(font)
        self.label_VCC_3.setObjectName("label_VCC_3")
        self.lineEdit_RxP = QtWidgets.QLineEdit(self.DDM_fram)
        self.lineEdit_RxP.setGeometry(QtCore.QRect(330, 140, 71, 31))
        self.lineEdit_RxP.setObjectName("lineEdit_RxP")
        self.label_temp_7 = QtWidgets.QLabel(self.DDM_fram)
        self.label_temp_7.setGeometry(QtCore.QRect(420, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_temp_7.setFont(font)
        self.label_temp_7.setObjectName("label_temp_7")
        self.EXIT_fram = QtWidgets.QFrame(self.DDM_fram)
        self.EXIT_fram.setGeometry(QtCore.QRect(330, 200, 131, 271))
        self.EXIT_fram.setFrameShape(QtWidgets.QFrame.Box)
        self.EXIT_fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EXIT_fram.setLineWidth(2)
        self.EXIT_fram.setObjectName("EXIT_fram")
        self.pushButton_exit = QtWidgets.QPushButton(self.EXIT_fram)
        self.pushButton_exit.setGeometry(QtCore.QRect(10, 10, 111, 251))
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_com, self.pushButton_link_com)
        MainWindow.setTabOrder(self.pushButton_link_com, self.pushButton_sweep_com)
        MainWindow.setTabOrder(self.pushButton_sweep_com, self.lineEdit_Temp)
        MainWindow.setTabOrder(self.lineEdit_Temp, self.lineEdit_VCC)
        MainWindow.setTabOrder(self.lineEdit_VCC, self.lineEdit_Temp_1)
        MainWindow.setTabOrder(self.lineEdit_Temp_1, self.lineEdit_Temp_2)
        MainWindow.setTabOrder(self.lineEdit_Temp_2, self.lineEdit_Temp_3)
        MainWindow.setTabOrder(self.lineEdit_Temp_3, self.lineEdit_Temp_4)
        MainWindow.setTabOrder(self.lineEdit_Temp_4, self.lineEdit_VCC_1)
        MainWindow.setTabOrder(self.lineEdit_VCC_1, self.lineEdit_VCC_2)
        MainWindow.setTabOrder(self.lineEdit_VCC_2, self.lineEdit_VCC_3)
        MainWindow.setTabOrder(self.lineEdit_VCC_3, self.lineEdit_VCC_4)
        MainWindow.setTabOrder(self.lineEdit_VCC_4, self.lineEdit_INIT)
        MainWindow.setTabOrder(self.lineEdit_INIT, self.lineEdit_white)
        MainWindow.setTabOrder(self.lineEdit_white, self.lineEdit_green)
        MainWindow.setTabOrder(self.lineEdit_green, self.lineEdit_red)
        MainWindow.setTabOrder(self.lineEdit_red, self.pushButton_exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_link_com.setText(_translate("MainWindow", "链接设备"))
        self.pushButton_sweep_com.setText(_translate("MainWindow", "扫描设备"))
        self.label_temp.setText(_translate("MainWindow", "TEMP:"))
        self.label_VCC.setText(_translate("MainWindow", "VCC:"))
        self.label_temp_3.setText(_translate("MainWindow", "℃"))
        self.label_temp_4.setText(_translate("MainWindow", "V"))
        self.label_temp_23.setText(_translate("MainWindow", "TxP"))
        self.label_temp_43.setText(_translate("MainWindow", "Temp"))
        self.label_temp_22.setText(_translate("MainWindow", "RxP"))
        self.label_temp_24.setText(_translate("MainWindow", "Bias"))
        self.label_temp_69.setText(_translate("MainWindow", "Hw"))
        self.label_temp_42.setText(_translate("MainWindow", "VCC"))
        self.label_temp_27.setText(_translate("MainWindow", "OLT"))
        self.label_temp_70.setText(_translate("MainWindow", "La"))
        self.label_temp_75.setText(_translate("MainWindow", "Ha"))
        self.label_temp_71.setText(_translate("MainWindow", "Lw"))
        self.label_temp_44.setText(_translate("MainWindow", "Initialization complete"))
        self.label_temp_26.setText(_translate("MainWindow", "OTC"))
        self.label_2.setText(_translate("MainWindow", "未连接"))
        self.label_3.setText(_translate("MainWindow", "连接正常"))
        self.label_4.setText(_translate("MainWindow", "连接异常"))
        self.label_temp_2.setText(_translate("MainWindow", "Bisa:"))
        self.label_temp_5.setText(_translate("MainWindow", "MA"))
        self.label_VCC_2.setText(_translate("MainWindow", "TxP:"))
        self.label_temp_6.setText(_translate("MainWindow", "dbm"))
        self.label_VCC_3.setText(_translate("MainWindow", "RxP:"))
        self.label_temp_7.setText(_translate("MainWindow", "dbm"))
        self.pushButton_exit.setText(_translate("MainWindow", "开始测试"))
        self.label.setText(_translate("MainWindow", "DDM"))
