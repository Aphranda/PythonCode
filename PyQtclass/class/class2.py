import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont


class FirstWindow(QMainWindow):
    def __init__(self, parent=None):
        """控件类"""
        super(FirstWindow, self).__init__(parent)
        self.initUI()
        self.control()

    def initUI(self):
        self.setGeometry(500, 200, 400, 400)
        self.setWindowIcon(QIcon('E:\music\down.ico'))
        self.setWindowTitle('下载')

    def control(self):
        self.button = QtWidgets.QPushButton("退出")
        self.lineEdit = QtWidgets.QLineEdit()
        self.LED = QtWidgets.QLCDNumber()
        self.LED.setFixedSize(40, 20)
        self.button.setFixedSize(70, 20)
        self.button.clicked.connect(self.over)
        self.button.clicked.connect(self.one)
        # 构建水平布局，将button放入
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.LED)
        layout.addWidget(self.lineEdit)
        # 创建Frame，并将水平布局放入Frame
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)
        self.status = self.statusBar()
        self.status.showMessage('只显示5秒消息', 5000)

    def over(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        a = 0
        for i in range(0, 3):
            a += 1
            time.sleep(1)
            print(a)
            self.LED.display(666)
        app = QApplication.instance()
        app.quit()

    def one(self):
        print('one')
        print('widget.x() = %d' % QWidget.x(self))
        print('widget.y() = %d' % QWidget.y(self))
        print('widget.width() = %d' % QWidget.width(self))
        print('widget.height() = %d' % QWidget.height(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstWindow()
    main.show()
    sys.exit(app.exec_())

