from PyQt5 import QtWidgets
import sys


class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()


def main_windows():
    app = QtWidgets.QApplication(sys.argv)
    windows = mywindow()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_windows()
