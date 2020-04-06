"""
setAlignment(): 设置文本对齐

setIndent(): 设置文本缩进

text(): 获取文本内容

setBuddy(): 设置伙伴关系

setText(); 设置文本内容

selectedText(): 返回所选择的字符

setWordWrap(): 设置是否运行换行

linkHovered ：鼠标滑过
linkActivated: 鼠标点击
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap

class QlableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText("<font color=yellow>这是一个文本编辑框</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)

        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('图片标签')
        label3.setPixmap(QPixmap('F:\Aphrodite\picture\disi第四印象 604期\yoyo8.jpg'))
        label4.setOpenExternalLinks(False)
        label4.setText("<a href='http://www.nenmp.com/2000/500'>漂不漂亮啊？")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('超级连接')

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(layout)
        self.setWindowTitle('QLabel演示')
        self.setWindowIcon(QIcon('E:\music\down.ico'))
    def linkHovered(self):
        print('当鼠标滑过label2')

    def linkClicked(self):
        print('鼠标单击label4')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlableDemo()
    main.show()
    sys.exit(app.exec_())