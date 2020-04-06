import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QRadioButtonDemo(QDialog):
    def __int__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        # layout = QHBoxLayout()
        # self.button1 = QRadioButton('单选按钮1')
        # self.button1.setChecked(True)
        # self.button1.toggled.connect(self.buttonState)
        # layout.addWidget(self.button1)
        # self.button2 = QRadioButton('单选按钮2')
        # self.button2.toggled.connect(self.buttonState)
        # layout.addWidget(self.button2)
        # self.setLayout(layout)

    def buttonState(self):
        radiobutton = self.sender()
        if radiobutton.text() == '单选按钮1':
            if radiobutton.isChecked() == True:
                print('<' + radiobutton.text() + '>被选中')
            else:
                print('<' + radiobutton.text() + '>被取消选中状态')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())