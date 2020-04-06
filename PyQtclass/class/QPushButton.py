"""
QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PushBUttonDemo')
        self.resize(500, 400)

        layout = QVBoxLayout()

        self.button1 = QPushButton('第一个')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))  # 自己传参数
        self.button1.clicked.connect(self.buttonState)

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap(r'C:\Users\Administrator\Desktop\7595\7595\j22.ico')))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))

        self.button3 = QPushButton('不可按钮')
        self.button3.setEnabled(False)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def whichButton(self, btn):  # but = self.button1
        print('被单击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isCheckable():
            print('按钮一被选中')
        else:
            print('按钮一未被选中')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
