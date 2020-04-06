"""
A ASCII字母字符必须输入(A-Z, a-z)
a ASCII字母字符是允许输入的，但不是必须的(A-Z, a-z)
N ASCII字母字符必须输入(A-Z, a-z, 0-9)
n ASCII字母字符是允许输入的，但不是必须的(A-Z, a-z, 0-9)
X 任何字符都是必须输入的
x 任何字符都是允许输入，但不是必须的
9 ASCII数字字符必须输入(0-9)
0 ASCII数字字符是允许输入的，但不是必须的(0-9)
D ASCII数字字符必须输入(1-9)
d ASCII数字字符是允许输入的，但不是必须的(1-9)
H 十六进制字母字符必须输入(A-Z, a-z, 0-9)
h 十六进制字母字符是允许输入的，但不是必须的(A-Z, a-z, 0-9)
B 二进制字符必须输入(0-1)
b 二进制字符是允许输入的，但不是必须的(0-1)
# ASCII数字字符或者加减符号是允许输入的，但不是必须的
> 所有字母字符都大写
< 所有字母字符都大写
! 关闭大小写转换
\ 使用"\"转义上面列出的字符
"""



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('掩码限制')
        formlayout = QFormLayout()

        iplineEdit = QLineEdit()
        maclineEdit = QLineEdit()
        datalineEdit = QLineEdit()
        licenselineEdit = QLineEdit()

        iplineEdit.setInputMask('000.000.000.000;_')
        maclineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        datalineEdit.setInputMask('0000-00-00')
        licenselineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')

        formlayout.addRow('数字掩码', iplineEdit)
        formlayout.addRow('Mac掩码', maclineEdit)
        formlayout.addRow('日期掩码', datalineEdit)
        formlayout.addRow('许可证掩码', licenselineEdit)

        self.setLayout(formlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())

