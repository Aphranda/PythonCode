

import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

# import others
import parsel
import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Python练习作品")
        Form.resize(523, 483)
        Form.setWindowIcon(QIcon('E:\down\love.ico'))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 531, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pictureframe = QtWidgets.QFrame(self.tab)
        self.pictureframe.setGeometry(QtCore.QRect(20, 10, 341, 441))
        self.pictureframe.setFrameShape(QtWidgets.QFrame.Box)
        self.pictureframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pictureframe.setObjectName("pictureframe")
        self.labelpicture = QtWidgets.QLabel(self.pictureframe)
        self.labelpicture.setGeometry(QtCore.QRect(20, 30, 300, 400))
        self.labelpicture.setObjectName("labelpicture")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(380, 10, 141, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 122, 103))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(380, 140, 141, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 121, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_P1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_P1.setObjectName("label_P1")
        self.gridLayout.addWidget(self.label_P1, 0, 0, 1, 1)
        self.label_P2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_P2.setObjectName("label_P2")
        self.gridLayout.addWidget(self.label_P2, 0, 1, 1, 1)
        self.label_P3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_P3.setObjectName("label_P3")
        self.gridLayout.addWidget(self.label_P3, 1, 0, 1, 1)
        self.label_P4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_P4.setObjectName("label_P4")
        self.gridLayout.addWidget(self.label_P4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(20, 150, 491, 100)
        self.pushButton_3.setText('退出')
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(20, 260, 491, 50)
        self.label_4.setText("下载时，稍等片刻")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 491, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 451, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Python练习作品——下载图片"))
        self.labelpicture.setText(_translate("Form", ""))
        self.label_1.setText(_translate("Form", "文件名称："))
        self.label_2.setText(_translate("Form", "数字标签："))
        self.label_3.setText(_translate("Form", "图片名字："))
        self.pushButton.setText(_translate("Form", "确认"))
        self.pushButton.clicked.connect(self.dir_name)
        self.pushButton.clicked.connect(self.url)
        self.pushButton.clicked.connect(self.preview)
        self.pushButton.clicked.connect(self.look)
        self.label_P1.setText(_translate("Form", ""))
        self.label_P2.setText(_translate("Form", ""))
        self.label_P3.setText(_translate("Form", ""))
        self.label_P4.setText(_translate("Form", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "预览"))
        self.pushButton_2.setText(_translate("Form", "确认下载"))
        self.pushButton_3.clicked.connect(window.close)
        self.pushButton_2.clicked.connect(self.download)
        # self.pushButton_3.clicked.connect(self.remove)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "储存"))

    def url(self):
        self.page = self.lineEdit_2.text()
        if type(self.page) is type(1):
            self.labelpicture.setText('错误标签')
        else:
            self.labelpicture.setText('right')
        self.urle = 'http://www.nenmp.com/' + '1' + '/' + str(self.page) + '.html'
        print(self.urle)
        response = requests.get(self.urle)
        response.encoding = 'utf-8'
        self.html = response.text
        # print(html)
        sel = parsel.Selector(self.html)
        self.img_s = sel.css('body > div:nth-child(2) > div > div.col-md-9 > div > img')
        a = 1
        self.urla_s = list()
        for img in self.img_s:
            self.urla = img.css('img::attr(src)').extract_first()
            self.name = img.css('img::attr(alt)').extract_first()
            self.urla_s.append(self.urla)
            # print(self.urla_s)
            # print(self.urla, self.name)

    def preview(self):
        os.chdir('C:\picture\{}'.format(str(self.dirname)))
        self.preview_urls = self.urla_s[0:50:9]
        # print(self.preview_urls)
        a = 0
        if not os.path.exists('preview'):
            os.makedirs('preview')
            os.chdir('preview')
        else:
            os.chdir('preview')
        self.res = list()
        for self.preview_url in self.preview_urls:
            a += 1
            self.preview_picture = requests.get(self.preview_url)
            self.picture_name =self.lineEdit_3.text()
            self.re = self.picture_name + str(a) + '.jpg'
            self.res.append(self.re)
            # print(self.res)
            with open(self.re, mode='wb')as f:
                f.write(self.preview_picture.content)

    def look(self):
        # print(self.res[0])
        im = Image.open(str(self.res[0]))
        (x, y) = im.size  # read image size
        x_s = 300  # define standard width
        y_s = y * x_s // x  # calc height based on standard width
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(str(self.res[0]))
        self.labelpicture.setPixmap(QPixmap('C:\picture\{}\preview\{}'.format(str(self.dirname), str(self.picture_name + '1' + '.jpg'))))
        for self.rel in self.res[1:5]:
            im = Image.open(str(self.rel))
            (x, y) = im.size  # read image size
            x_s = 65  # define standard width
            y_s = y * x_s // x  # calc height based on standard width
            out = im.resize((x_s, y_s), Image.ANTIALIAS)
            out.save(str(self.rel))
            self.label_P1.setPixmap(QPixmap('C:\picture\{}\preview\{}'.format(str(self.dirname), str(self.picture_name + '2' + '.jpg'))))
            self.label_P2.setPixmap(QPixmap('C:\picture\{}\preview\{}'.format(str(self.dirname), str(self.picture_name + '3' + '.jpg'))))
            self.label_P3.setPixmap(QPixmap('C:\picture\{}\preview\{}'.format(str(self.dirname), str(self.picture_name + '4' + '.jpg'))))
            self.label_P4.setPixmap(QPixmap('C:\picture\{}\preview\{}'.format(str(self.dirname), str(self.picture_name + '5' + '.jpg'))))

    def download(self):
        os.chdir('C:\picture\{}'.format(str(self.dirname)))
        a = 0
        for img in self.img_s:
            self.urld = img.css('img::attr(src)').extract_first()
            self.nameo = img.css('img::attr(alt)').extract_first()
            print(self.urld, self.nameo)
            picture = requests.get(self.urld)
            a += 1
            self.lcdNumber.display(a)
            QApplication.processEvents()
            self.label_4.setText('文件位置：C:\picture\{} 下载数量:{}'.format(self.dirname, a))
            with open(self.re + self.nameo + str(a) + '.' + 'jpg', mode='wb') as f:
                f.write(picture.content)

    # def remove(self):
    #     if os.path.exists('C:\picture\{}'.format(str(self.dirname))):
    #         os.chdir('C:\picture\{}'.format(str(self.dirname)))
    #     else:
    #         return
    #     if not os.path.exists('preview'):
    #         pass
    #     else:
    #         os.removedirs('preview')


    def dir_name(self):
        os.chdir('C:\picture')
        self.dirname = self.lineEdit_1.text()
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
            os.chdir(self.dirname)
        else:
            os.chdir(self.dirname)



if __name__ == '__main__':
    if not os.path.exists('C:\picture'):
        os.makedirs('C:\picture')
        os.chdir('C:\picture')
    else:
        os.chdir('C:\picture')
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())