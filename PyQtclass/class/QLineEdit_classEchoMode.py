"""
QLineEdit控件与回显模式
基本功能：输入单行文本 EchoMode（回显模式）
四种回显模式：

1. Normal(普通输入模式）
2. NoEcho(不回显）
3. Password(输入回显*******）
4. PasswordEchoEdit(即时显示，然后变成*****）

"""
from PyQt5.QtWidgets import *
import sys

class QLineEditMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框回显')

        formlayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoONEdit = QLineEdit()

        formlayout.addRow('Normal', normalLineEdit)
        formlayout.addRow('noEcho', noEchoLineEdit)
        formlayout.addRow('password', passwordLineEdit)
        formlayout.addRow('passwordEchoON', passwordEchoONEdit)

        # placeholdertext 文本输入框提示

        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoONEdit.setPlaceholderText('PasswordEchoON')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoONEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout) # 启动表单布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMode()
    main.show()
    sys.exit(app.exec_())
