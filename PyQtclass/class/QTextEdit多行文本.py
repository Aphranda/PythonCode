from PyQt5.QtWidgets import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit演示')

        self.resize(300, 200)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')

        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)
        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello World, 你好世界！')  # 设置普通文本

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml(r'<font color="blue" size="5"><b><i>Hello World<i><b></font>')

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())