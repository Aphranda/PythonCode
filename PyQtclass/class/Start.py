import sys
import class1
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = class1.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exit(app.exec_())