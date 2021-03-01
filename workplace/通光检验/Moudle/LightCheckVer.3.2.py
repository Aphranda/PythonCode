'''
Author: Dongli
Date: 2021-03-01 16:26:45
LastEditors: Dongli
LastEditTime: 2021-03-01 16:29:34
Description: 
'''
'''
Author: Dongli
Date: 2021-03-01 09:10:06
LastEditors: Dongli
LastEditTime: 2021-03-01 16:25:10
Description: 
'''
'''
Author: Dongli
Date: 2021-02-26 12:19:52
LastEditors: Dongli
LastEditTime: 2021-02-26 15:37:03
Description: 
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import xlrd, xlwt
from xlutils.copy import copy


import os, sys, time, datetime
from Ui_LightCheck import Ui_MainWindow
from PortConfiguration import Port
from PreConfiguration import Configuration
from FileConfiguration import File
from ErrorConfiguration import Logits
from DataConfiguration import MyTree
# from ServerConfiguration import MyServer
Logits = Logits()



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
       
        # 实例化外部类
        self.config = Configuration() # 实例化配置文件
        self.port = Port() # 实例化串口配置
        self.file = File()

        # 文件夹初始化
        self.file.create_file("Configuration") # 创建文件夹
        self.file.create_file("DataTemplate")
        self.root_path = self.file.back_file()
        
        self.tree = MyTree(self.root_path + "\\" +"Configuration")
        # try:
        #     self.server = MyServer()
        #     pass
        # except Exception as e:
        #     print(e)
        #     self.top_window("服务器没有连接，串口已经关闭")
        #     self.port.close_port()
        #     self.pushButton_portcom.setText("数据库错误")

        # 界面初始化
        self.textEdit_systemNews.setReadOnly(True) # topwindow初始化
        self.tableWidget_Excel.setColumnWidth(7, 240) # table初始化
        self.tableWidget_Excel.setColumnWidth(0, 220)
        self.tableWidget_Excel.setColumnWidth(1, 220)
        self.tableWidget_Excel.setColumnWidth(2, 220)

        self.lineEdit_count.setValidator(QtGui.QIntValidator(0,99))

        self.top_window("欢迎使用TS通光测试系统")
        self.port_add() # 界面添加串口
        self.administrators()

        # 按键初始化
        self.pushButton_portcom.setStyleSheet("background-color:steelblue")
        self.pushButton_up.clicked.connect(self.quicker_up)
        self.pushButton_down.clicked.connect(self.quicker_down)

        self.textEdit_preimport_branch.textChanged.connect(self.quicker_enter)

        # 配置初始化 （产品，极性，路径， 特殊产品标志位）
        self.pre_read_production_configuration()
        self.pre_read_polarity_configration()
        self.pre_read_path()
        self.count = 0
       
        # 界面切换产品配置
        self.comboBox_lightConfiguration.currentTextChanged.connect(self.exchange_show_production_configuration)

        # 界面切换极性配置
        self.comboBox_polarityConfiguration.currentTextChanged.connect(self.exchange_show_polarity_configration)
        
        # 获取路径
        self.pushButton_same_path.clicked.connect(lambda: self.data_path("self.lineEdit_same_filepath"))  # 储存路径设置
        self.pushButton_single_path.clicked.connect(lambda: self.data_path("self.lineEdit_single_filepath"))  # 储存路径设置

        # 机台号设置
        self.pushButton_machine.clicked.connect(self.machine_num)

        # 文件名切换
        self.lineEdit_production_SN.textChanged.connect(self.data_name)

        # 串口连接
        self.pushButton_portcom.clicked.connect(self.port_link)

        # 线程传送数据
        self.pushButton_lightCheck.clicked.connect(self.thread_start)

        # 增加产品信息
        self.pushButton_ok.clicked.connect(lambda: self.production_configuration("ok"))
        self.pushButton_modify.clicked.connect(lambda: self.production_configuration("modify"))
        self.pushButton_delete.clicked.connect(lambda: self.production_configuration("delete"))

        # 增加极性信息
        self.pushButton_polarity_ok.clicked.connect(lambda: self.polarity_configuration("ok"))
        self.pushButton_polarity_modify.clicked.connect(lambda: self.polarity_configuration("modify"))
        self.pushButton_polarity_delete.clicked.connect(lambda: self.polarity_configuration("delete"))

        # 学习产品极性
        self.pushButton_polarity_download.clicked.connect(self.production_polarity)

        # 按钮互斥
        self.checkBox_same.clicked.connect(lambda: self.checkBox_single.setChecked(False))
        self.checkBox_single.clicked.connect(lambda: self.checkBox_same.setChecked(False))
        self.checkBox_onceLight.clicked.connect(lambda: self.checkBox_moreLight.setChecked(False))
        self.checkBox_moreLight.clicked.connect(lambda: self.checkBox_onceLight.setChecked(False))

        # 数据库操作
        self.pushButton_data_ok.clicked.connect(lambda: self.sql_data(True))
        self.pushButton_data_delete.clicked.connect(lambda: self.sql_data(False))
        self.pushButton_data_download.clicked.connect(self.download_data)

        # Test
    @Logits
    def quicker_up(self, *args, **kwargs):
        """SN-焦点"""
        self.lineEdit_production_SN.clear()
        self.lineEdit_production_SN.setFocus()

    @Logits
    def quicker_down(self, *args, **kwargs):
        """branch-焦点"""
        self.textEdit_preimport_branch.clear()
        self.textEdit_preimport_branch.setFocus()

    @Logits
    def quicker_enter(self, *args, **kwargs):
        """enter 快捷键"""
        try:
            result_text = self.textEdit_preimport_branch.toPlainText()
            # result_num = result_text.count("\n")
            if result_text[-1] == "\n" and result_text[-2] == "\n":
                self.pushButton_lightCheck.setFocus()
        except Exception as e:
            print("quicker_enter-" + str(e))
            self.pushButton_lightCheck.setFocus()
    
    def time_news(self, *args, **kwargs):
        """界面时钟信息"""
        try:
            time_now = datetime.datetime.now()
            now_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
            return now_time
        except Exception as e:
            print("time_news--" + str(e))
    
    def message_waring(self, value):
        try:
            receive = QtWidgets.QMessageBox.warning(self, "提示", str(value), QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if receive == QtWidgets.QMessageBox.Yes:
                return True
            return False
        except Exception as e:
            print(e)

    @Logits
    def top_window(self, value):
        """将信息传送至界面"""
        self.textEdit_systemNews.append(value + "    -    " + f"[{self.time_news()}]")

    @Logits
    def administrators(self, *args, **kwargs):
        os.chdir(self.root_path)
        os.chdir("Configuration")
        self.config = Configuration()
        data = self.config.count_section("AimDataPath")
        try:
            data = self.config.search_option("AimDataPath", "admin")
            self.administrator = data[0][1]
        except Exception as e:
            print("administrators-" + str(e))
            self.top_window("请设置密码")

    @Logits
    def data_path(self, value:str):
        """获取文件储存位置"""
        os.chdir(self.root_path)
        os.chdir("Configuration")
        self.config = Configuration()
        openfile_name = QtWidgets.QFileDialog.getExistingDirectory()
        data = ["AimDataPath", value, {"path":openfile_name}]
        receive = self.config.add_section(data)
        if "已经存在" in receive:
            self.config.modify_section(data)
        eval(value).setText(openfile_name)
        os.chdir(self.root_path)

    @Logits
    def data_name(self, *args, **kwargs):
        """文件名称跟随"""
        if self.checkBox_single.isChecked():
            self.lineEdit_same_filename.setText(self.lineEdit_production_SN.text())
            self.lineEdit_single_filename.setText(self.lineEdit_production_SN.text())

    @Logits
    def pre_read_path(self, *args, **kwargs):
        """界面预读取数据储存位置"""
        os.chdir(self.root_path)
        os.chdir("Configuration")
        self.config = Configuration()
        data = self.config.count_section("AimDataPath")
        print(len(data))
        if len(data) < 4:
            self.top_window("请预设文件储存位置&机台号")
        else:
            data_01 = self.config.search_option("AimDataPath", "self.lineEdit_same_filepath")
            data_02 = self.config.search_option("AimDataPath", "self.lineEdit_single_filepath")
            data_03 = self.config.search_option("AimDataPath", "machine")
            self.lineEdit_same_filepath.setText(data_01[0][1])
            self.lineEdit_single_filepath.setText(data_02[0][1])
            self.lineEdit_machine.setText(data_03[0][1])

    @Logits
    def pre_read_production_configuration(self, *args, **kwargs):
        """界面预读取产品信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")
        self.config = Configuration() # 实例化配置文件
        data = self.config.count_section("LightCheckConfiguration")
        if len(data) == 0:
            self.top_window("请预设通光配置文件")
        else:
            for i in data:
                self.comboBox_lightConfiguration.addItem(i)
        
        self.exchange_show_production_configuration()
        del self.config
        os.chdir(self.root_path)

    @Logits
    def exchange_show_production_configuration(self, *args, **kwargs):
        """界面切换产品信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")

        self.config = Configuration() # 实例化配置文件
        data = self.config.search_option("LightCheckConfiguration", self.comboBox_lightConfiguration.currentText())
        self.lineEdit_productionNumber.setText(self.comboBox_lightConfiguration.currentText())
        self.lineEdit_productionItem.setText(data[0][1])
        self.lineEdit_productionCore.setText(data[1][1])
        os.chdir(self.root_path)
        
    @Logits
    def production_configuration(self, value:str):
        """从界面配置产品信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")

        self.config = Configuration() # 实例化配置文件
        configuration_name = "LightCheckConfiguration"
        section = self.lineEdit_productionNumber.text()
        item = self.lineEdit_productionItem.text()
        core = self.lineEdit_productionCore.text()
        data = [configuration_name, section, {"item":item, "core": core}]

        if len(item) != 0 and len(core) != 0 and len(section) != 0 and value == "ok" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.add_section(data))
        elif value == "delete" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.delete_section(data))
        elif value == "modify" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.modify_section(data))
        else:
            self.top_window("请输入管理员名称,并且完善通光配置信息")

        self.comboBox_lightConfiguration.clear()
        self.pre_read_production_configuration()
        os.chdir(self.root_path)

    @Logits
    def pre_read_polarity_configration(self, *args, **kwargs):
        """界面预读取极性信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")
        self.config = Configuration()
        data = self.config.count_section("PolarityConfiguration")
        if len(data) == 0:
            self.top_window("请预设极性配置文件")
        else:
            for i in data:
                self.comboBox_polarityConfiguration.addItem(i)
        self.exchange_show_polarity_configration()
        del self.config

        os.chdir(self.root_path)

    @Logits
    def exchange_show_polarity_configration(self, *args, **kwargs):
        """界面切换极性信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")

        self.config = Configuration()
        data = self.config.search_option("PolarityConfiguration", self.comboBox_polarityConfiguration.currentText())
        self.lineEdit_polarityName.setText(self.comboBox_polarityConfiguration.currentText())
        self.textEdit_polarityInput.setText(data[0][1])
        os.chdir(self.root_path)
      
    @Logits
    def polarity_configuration(self, value:str):
        """从界面配置极性信息"""
        os.chdir(self.root_path)
        os.chdir("Configuration")

        self.config = Configuration()
        configuration_name = "PolarityConfiguration"
        section = self.lineEdit_polarityName.text()
        polarity = self.textEdit_polarityInput.toPlainText()

        data = [configuration_name, section, {"polarity":polarity}]

        if len(section) != 0 and len(polarity) != 0 and value == "ok" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.add_section(data))
        elif value == "delete" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.delete_section(data))
        elif value == "modify" and self.lineEdit_operator.text() == self.administrator:
            self.top_window(self.config.modify_section(data))
        else:
            self.top_window("请输入管理员名称,并且完善极性配置信息")

        self.comboBox_polarityConfiguration.clear()
        self.pre_read_polarity_configration()
        os.chdir(self.root_path)

    @Logits
    def production_polarity(self, *args, **kwargs):
        """将产品极性进行读入--密码设置"""
        try:
            if self.lineEdit_operator.text()[0] == "#" and len(self.lineEdit_operator.text()) > 4 and self.lineEdit_operator.text()[-1] == "$":
                os.chdir(self.root_path)
                os.chdir("Configuration")
                self.config = Configuration()
                data = ["AimDataPath", "admin", {"administrator": self.lineEdit_operator.text()[1:-1]}]
                receive = self.config.add_section(data)
                if "已经存在" in receive:
                    self.config.modify_section(data)
                self.top_window("密码设置完成")
                os.chdir(self.root_path)
        except Exception as e:
            print("production_polarity" + str(e))
            production_polarity_num = self.spinBox_polarity.value()
            self.translate = Translate(self.port.port_write, production_polarity_num)
            self.translate.receive.connect(self.production_polarity_input)
            self.translate.start()

    @Logits
    def machine_num(self, *args, **kwargs):
        if self.lineEdit_operator.text() == self.administrator:
            os.chdir(self.root_path)
            os.chdir("Configuration")
            self.config = Configuration()
            data = ["AimDataPath", "machine", {"macheine_num": self.lineEdit_machine.text()}]
            receive = self.config.add_section(data)
            if "已经存在" in receive:
                self.config.modify_section(data)
            self.top_window("机器号设置完成")
            os.chdir(self.root_path)
        else:
            self.top_window("请输入管理员账号")

    @Logits
    def production_polarity_input(self, value):
        """产品极性导入输入栏"""
        polarity_input = ""
        self.lineEdit_polarityName.setText("New Polarity")
        for i in value:
            polarity_input = polarity_input + i + "\n"
        self.textEdit_polarityInput.setText(polarity_input)
        del self.translate

    @Logits
    def port_add(self, *args, **kwargs):
        """添加串口至界面"""
        com = self.port.auto_search()
        if len(com) > 0:
            for i in com:
                self.comboBox_portcheck.addItem(i)
        else:
            self.comboBox_portcheck.addItem("无可用串口")
            self.top_window("无可用串口")

    @Logits
    def port_link(self, *args, **kwargs):
        """串口连接，及其界面显示"""
        self.pushButton_lightCheck.setEnabled(True)
        com = self.comboBox_portcheck.currentText()
        self.port.open_port(com)
        if self.port.judge_port():
            self.pushButton_portcom.setStyleSheet("background-color:seagreen")
            self.pushButton_portcom.setText("连接成功")
            self.top_window("串口连接成功")
        else:
            self.pushButton_portcom.setStyleSheet("background-color:crimson")
            self.pushButton_portcom.setText("连接失败")
            self.top_window("串口连接失败")

    @Logits
    def thread_start(self, *args, **kwargs):
        """开启信号传送/接收线程"""
        # 极性数量抽取
        item_num = 100
        branch = self.textEdit_preimport_branch.toPlainText()
        if branch[-1] != "\n":
            self.textEdit_preimport_branch.setText(branch + "\n")
        else:
            self.pushButton_lightCheck.setEnabled(False)
        if branch[-1] == "\n":
            self.textEdit_preimport_branch.setText(branch[0:-1])
        else:
            self.pushButton_lightCheck.setEnabled(False)
        core_num = self.textEdit_preimport_branch.toPlainText().count("\n")
        polarity_num = self.textEdit_polarityInput.toPlainText().count("-")

        # 对于MTP/LC器件，进行后续补零操作
        if core_num == int(self.lineEdit_productionItem.text()) and core_num < polarity_num//int(self.lineEdit_productionCore.text()):
            self.textEdit_preimport_branch.setText(branch[0:-1] + "0\n"*(polarity_num//int(self.lineEdit_productionCore.text())-core_num))
            item_num = polarity_num//int(self.lineEdit_productionCore.text())
            print(self.textEdit_preimport_branch.toPlainText())
        else:
            item_num = int(self.lineEdit_productionItem.text())


        # 对于极性和item进行限制判断
        if core_num == int(self.lineEdit_productionItem.text()) or core_num == item_num and polarity_num == int(self.lineEdit_productionItem.text()) * int(self.lineEdit_productionCore.text()):
            self.translate = Translate(self.port.port_write, polarity_num)
            self.translate.receive.connect(self.collect_window_new)
            self.translate.start()
            self.item_num_g = item_num
        else:
            self.top_window(f"Core X Item = {int(self.lineEdit_productionItem.text()) * int(self.lineEdit_productionCore.text())}, 极性 = {polarity_num}")
            self.pushButton_lightCheck.setEnabled(True)
            
    def PreSn_check(self, *args, **kwargs):
        """对于组数和极性进行限制与检测"""
        try:
            core_box = []
            num_core = int(self.lineEdit_productionCore.text())
            num_item = self.item_num_g # 中继item_num
            pre_branch_content = self.textEdit_preimport_branch.toPlainText()
            pre_branch_num = pre_branch_content.count("\n")
            pre_branch_box = self.textEdit_preimport_branch.toPlainText().split("\n", pre_branch_num)[0:-1]*num_core
            for i in range(num_item):
                for j in range(num_core):
                    core_box.append(pre_branch_box[j*num_item + i])
            return core_box
        except Exception as e:
            print("PreSn_check-" + str(e))

    def Lcd_change(self):
        try:
            self.count += 1
            if self.count == int(self.lineEdit_count.text()):
                self.message_waring(f"{self.count}组测试完成")
                self.count = 0
            elif self.count == 999:
                self.count = 0
            num = self.count
            return num
        except Exception as e:
            print(e)
        
    @Logits
    def collect_window_new(self, value):
        """收集界面信息，进行信息控制"""
        self.pushButton_lightCheck.setEnabled(True)
        i_flag = 1
        r_flag = 0
        b_flag = 0
        content_data = []

        # 判断填写信息位置，并作出判断
        name = ["产品S/N", "产品P/N", "操作者名称", "储存路径"]
        if self.checkBox_same.isChecked():
            path = self.lineEdit_same_filepath.text()
        else:
            path = self.lineEdit_single_filepath.text()

        box = [self.lineEdit_production_SN.text(), self.lineEdit_production_PN.text(), self.lineEdit_operator.text(), path]
        for i, n  in enumerate(box):
            if len(n) == 0:
                self.top_window(f"请输入[{name[i]}]信息")
                i_flag *= len(n)
            else:
                i_flag *= len(n)

        # 产品SN，产品PN，操作者，时间戳，产品编号，产品组数，产品芯数
        production_sn = self.lineEdit_production_SN.text()
        production_pn = self.lineEdit_production_PN.text()
        operator_name = self.lineEdit_operator.text()
        light_check_time = self.time_news()
        production_number = self.lineEdit_productionNumber.text()
        production_item = self.lineEdit_productionItem.text()
        production_core = self.lineEdit_productionCore.text()
        
        # 信息进入table的颜色
        production_sn_color = "white"
        production_pn_color = "white"
        branch_sn_color = "white"
        operator_name_color = "white"
        polarity_result_color = "white"
        light_check_time_color = "white"
        production_number_color = "white"
        production_item_color = "white"
        production_core_color = "white"

        # 通光类型判断
        if self.checkBox_onceLight.isChecked():
            light_check_num = "一次通光"
            light_check_num_color = "white"
        elif self.checkBox_moreLight.isChecked():
            light_check_num = "返修通光"
            light_check_num_color = "darkgray"

        # 极性抽取至列表储存
        polarity_num = self.textEdit_polarityInput.toPlainText().count("-")
        polarity_config = self.textEdit_polarityInput.toPlainText().split("\n", polarity_num)

        for i, n in enumerate(polarity_config):
            polarity_result = n
            if n == value[i] or n.split("-", 1)[-1] == "0":
                r_flag += 1
                passcheck_result = value[i] + "pass"
                passcheck_result_color = "green"
            else:
                passcheck_result = value[i] + "fail"
                passcheck_result_color = "red"


            if value[i].split("-", 1)[-1] != "0":
                branch_sn = str(self.PreSn_check()[b_flag])
                b_flag += 1
            else:
                branch_sn = "0"

            result = [
                    [production_sn, production_sn_color],
                    [production_pn, production_pn_color],
                    [branch_sn, branch_sn_color],
                    [polarity_result, polarity_result_color],
                    [passcheck_result, passcheck_result_color],
                    [light_check_num, light_check_num_color],
                    [operator_name, operator_name_color],
                    [light_check_time, light_check_time_color],
                    [production_number, production_number_color],
                    [production_item, production_item_color],
                    [production_core, production_core_color]
                ]

            if i_flag:
                self.table_show(result, i)

                if r_flag == len(polarity_config):
                    self.lineEdit_passCheck.setStyleSheet("background-color:green")
                    self.lineEdit_passCheck.setText("pass")
                else:
                    self.lineEdit_passCheck.setStyleSheet("background-color:red")
                    self.lineEdit_passCheck.setText("fail")

        if self.lineEdit_passCheck.text() == "fail":
            self.port.close_port()
            self.port_link()
            self.port.port_write("@00WR03000020")
            self.port.port_write("@00WR03000002")

        for i in range(len(polarity_config)):
            content_data.append(self.deal_data(i))
        if self.lineEdit_passCheck.text() == "pass":
            self.save_data(content_data, path)
            self.lcdNumber.display(self.Lcd_change())
        elif self.lineEdit_passCheck.text() == "fail" and self.message_waring("保存提示"):
            self.save_data(content_data, path)
            self.lcdNumber.display(self.Lcd_change())

    @Logits
    def table_show(self, value:list, key:int):
        """tableWidget展示产品信息"""
        for i, n in enumerate(value):
            new_item = QtWidgets.QTableWidgetItem(n[0])
            new_item.setBackground(QtGui.QBrush(QtGui.QColor(n[1])))
            new_item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.tableWidget_Excel.setRowCount(10 + key)
            self.tableWidget_Excel.setItem(key,i,new_item)

    def deal_data(self, key):
        """储存tablewidget中的数据"""
        try:
            content_data = []
            num_column = self.tableWidget_Excel.columnCount()
            for i in range(num_column):
                content_column = self.tableWidget_Excel.item(key,i).text()
                content_data.append(content_column)
            return content_data
        except Exception as e:
            print("deal_data-" + str(e))

    def data_line(self, value, path):
        """获取现有文件的行数, 并返回EXcel表工作区"""
        try:
            file_path = path
            file_name = self.lineEdit_same_filename.text()
            myWorkplace = xlrd.open_workbook(f"{file_path}/{file_name}.xls")
            data = copy(myWorkplace)
            mySheet = myWorkplace.sheet_by_index(0)
            nRows = mySheet.nrows
            nCols = mySheet.ncols
            return [nRows, nCols, data]
        except Exception as e:
            print("data_line-" + str(e))
        
    @Logits
    def save_data(self, value, path):
        """文件储存"""
        nRows = 0
        file_path = path
        file_name = self.lineEdit_same_filename.text()
        file = f"{file_path}\\{file_name}.xls"

        # 数据库写入数据
        self.tree.create_table(file_name)
        file_data = [f"{file_name}"]
        inspection_data = [0, 1, 0, 0]
        macheine_data = [f"{self.lineEdit_machine.text()}"]
        for i in value:
            # data = file_data + i + inspection_data + macheine_data
            self.tree.add_data(file_name, i)
            # try:
            #     self.server.add_data(data)
            # except Exception as e:
            #     print(e)
            #     self.top_window("服务器数据储存错误")

        header_data = []
        num_column = self.tableWidget_Excel.columnCount()
        for i in range(num_column):
            header_column = self.tableWidget_Excel.horizontalHeaderItem(i).text()
            header_data.append(header_column)

        if os.path.exists(file) and self.checkBox_same.isChecked():
            nRows = self.data_line(value, path)[0] + 1
            workbook = self.data_line(value, path)[2]
            worksheet = workbook.get_sheet(0)
        else:
            workbook = xlwt.Workbook(encoding="gbk")
            worksheet = workbook.add_sheet("sheet")

        for i, n in enumerate(header_data):
            worksheet.write(0, i, n)

        for i, n in enumerate(value):
            for j, m in enumerate(n):
                worksheet.write(i + 1 + nRows, j, m)
        workbook.save(file)
        del self.translate

    @Logits
    def sql_data(self, value):
        """数据库操作"""
        table = self.lineEdit_table_name.text()

        productionSN = self.lineEdit_searchSN.text()
        productionPN = self.lineEdit_searchPN.text()
        operator = self.lineEdit_search_operator.text()
        lightCheckResult = self.lineEdit_search_result.text()
        if self.comboBox_checkAgain.currentText() == "否":
            lightCheckNum = "一次通光"
        else:
            lightCheckNum = "返修通光"
        time = self.lineEdit_data_time.text().replace("//", "-")
        key = [productionSN, productionPN, operator, lightCheckResult, lightCheckNum, time]
        if value == True:
            res = self.tree.search_data(table, key)
            self.textEdit_data_show.clear()
            for i in res:
                self.textEdit_data_show.append(str(i).replace("(", "").replace(")", ""))
            self.top_window("查找完毕" + f"     查找数量：{len(res)}")

        elif value == False:
            self.tree.delete_data(table, key)
            self.top_window("删除完毕")
        else:
            self.top_window("输入错误")
        print(key)
    
    @Logits
    def download_data(self, value): # TODO: Test download_data
        """数据下载功能"""
        name = self.lineEdit_table_name.text()
        data = self.textEdit_data_show.toPlainText()
        with open(f"{str(name)}-{str(self.time_news())[0:11]}.txt", mode="a+") as f:
            f.write(data)
        self.top_window("导出成功")




class Translate(QtCore.QThread):
    receive = QtCore.pyqtSignal(list)

    def __init__(self, write, value):
        super(Translate, self).__init__()
        # 输入
        self.write = write
        self.value = value

    def run(self):
        try:
            launch = ["@00WR0301", "@00WR0302"]
            self.write("@00SC02")
            self.write("@00WR03000001")
            time.sleep(0.2)
            if self.value <= 4:
                self.write_data(launch[0], ["000",""])
            elif self.value > 4 and self.value <= 8:
                self.write_data(launch[0], ["000",""])
                self.write_data(launch[0], ["00", "0"])
            elif self.value > 8 and self.value <= 12:
                self.write_data(launch[0], ["000",""])
                self.write_data(launch[0], ["00", "0"])
                self.write_data(launch[0], ["0", "00"])
            elif self.value > 12 and self.value <= 16:
                self.write_data(launch[0], ["000",""])
                self.write_data(launch[0], ["00", "0"])
                self.write_data(launch[0], ["0", "00"])
                self.write_data(launch[1], ["000", ""])
            elif self.value > 16 and self.value <= 20:
                self.write_data(launch[0], ["000",""])
                self.write_data(launch[0], ["00", "0"])
                self.write_data(launch[0], ["0", "00"])
                self.write_data(launch[1], ["000", ""])
                self.write_data(launch[1], ["00", "0"])
            elif self.value > 20 and self.value <= 24:
                self.write_data(launch[0], ["000",""])
                self.write_data(launch[0], ["00", "0"])
                self.write_data(launch[0], ["0", "00"])
                self.write_data(launch[1], ["000", ""])
                self.write_data(launch[1], ["00", "0"])
                self.write_data(launch[1], ["0", "00"])

            # 输出
            self.receive.emit(self.receive_data())
            self.write("@00WR03000002")
        except Exception as e:
            print("run-" + str(e))

    def write_data(self, value, key):
        try:
            for i in range(4):
                num = 2**i
                self.write(str(value) + f"{key[0]}{num}{key[1]}")
        except Exception as e:
            print("write_data-" + str(e))

    def receive_data(self):
        try:
            back = []
            backWords = []
            order = "@00RD00000024"
            data = str(self.write(order)[7:-2])[2:-1]
            for i in range(self.value):
                back.append([data[4*i:4*i+2], data[4*i+2:4*i+4]])
            back_dict = {
                    "01":"1", "02":"2", "03":"3", "04":"4", "05":"5", "06":"6", "07":"7", "08":"8", "":"0", "00":"0",
                    "09":"9", "0A":"10", "0B":"11", "0C":"12", "0D":"13", "0E":"14", "0F":"15", "10":"16",
                    "11":"17", "12":"18" ,"13": "19", "14":"20", "15":"21", "16":"22", "17":"23", "18":"24"
                    }
            for i in back:
                backWords.append(f"{back_dict[i[0]]}-{back_dict[i[1]]}")
            return backWords
        except Exception as e:
            print("receive_data-" + str(e))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exit(app.exec_())