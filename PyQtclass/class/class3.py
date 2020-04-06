import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('黑体, 12'))
        self.setToolTip('今天是<b>birthday<b>')
        self.setGeometry(500, 200, 400, 400)
        self.setWindowTitle('remind')
        self.button = QPushButton('开心')
        self.button.setToolTip('收到了礼物')
        self.button.setFixedSize(90, 20)
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
