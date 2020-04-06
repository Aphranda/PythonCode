# https://zmister.com
from PyQt5 import QtWidgets
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        status = self.statusBar()
        status.showMessage("状态栏")   # 底部显示状态栏

        # view_toolbar = self.addToolBar('view')
        # view_toolbar.addAction("打开")
        # view_toolbar.addAction("保存")
        # view_toolbar.addAction("撤回")
        # file_menu = QtWidgets.QMenuBar(self)  # 实例化菜单栏
        # file_menu.setFixedWidth(200)  # 设置菜单栏宽度
        # file_menu.setFixedHeight(25)
        # file_menu.addMenu('文件')  # 增加菜单按钮
        # file_menu.addMenu('编辑')  # 增加菜单按钮
        # file_menu.addMenu('关于')  # 增加菜单按钮


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = App()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()