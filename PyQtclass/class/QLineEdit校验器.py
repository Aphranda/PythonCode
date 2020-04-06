"""
校验器
如限制只能输入数字，浮点数或者满足一定条件字符串

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QIcon
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('效验器')

        # 创建表单布局
        formlayout = QFormLayout()
        self.setWindowIcon(QIcon('E:\down\love.ico'))

        intlineEdit = QLineEdit()
        doublelineEdit = QLineEdit()
        validatorlineEdit = QLineEdit()

        formlayout.addRow('整型', intlineEdit)
        formlayout.addRow('浮点型', doublelineEdit)
        formlayout.addRow('数字和字母', validatorlineEdit)

        intlineEdit.setPlaceholderText('整型')
        doublelineEdit.setPlaceholderText('浮点型')
        validatorlineEdit.setPlaceholderText('字母和数字')

        # 整数校验器 [1, 99]
        intvalidator = QIntValidator(self)
        intvalidator.setRange(1, 99)
        # 浮点型校验器 [-300, 300] 精度小数点后两位
        doublevalidator = QDoubleValidator(self)
        doublevalidator.setRange(-300, 300)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)  # 标准的表示法
        doublevalidator.setDecimals(2)  # 设置精度
        # 正则表达
        reg = QRegExp('[a-zA-Z0-9]+$')  # 创建正则表达式
        validator = QRegExpValidator(self)  # 创建正则表达式计算器
        validator.setRegExp(reg)  # 绑定表达式与计算器

        # 设置效验器
        intlineEdit.setValidator(intvalidator)
        doublelineEdit.setValidator(doublevalidator)
        validatorlineEdit.setValidator(validator)

        self.setLayout(formlayout)  #启用布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())





