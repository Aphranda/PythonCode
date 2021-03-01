from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import serial
import serial.tools.list_ports

import sys
import os
import time, datetime
import xlrd, xlwt
from xlutils.copy import copy
import configparser
import PreConfiguration
from Ui_LightCheck import *



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.administrator = "1"

        self.textEdit_systemNews.setReadOnly(True)
        self.init_window("欢迎使用TS通光测试系统")  # 初始化系统实时显示

        self.tableWidget_Excel.setColumnWidth(7, 240)
        self.tableWidget_Excel.setColumnWidth(0, 220)
        self.tableWidget_Excel.setColumnWidth(1, 220)
        self.tableWidget_Excel.setColumnWidth(2, 220)

        self.port_com = []  # 储存串口号
        self.auto_search()  # 搜索串口
        self.back = []

        self.production_news = {}

        self.pushButton_portcom.clicked.connect(self.open_port)  # 打开串口
        self.pushButton_portcom.clicked.connect(self.port_check)  # 验证串口

        self.pushButton_lightCheck.clicked.connect(self.thread_start) # 储存数据

        self.pushButton_same_path.clicked.connect(lambda: self.data_path("self.lineEdit_same_filepath"))  # 储存路径设置
        self.pushButton_single_path.clicked.connect(lambda: self.data_path("self.lineEdit_single_filepath"))  # 储存路径设置

        self.pushButton_ok.clicked.connect(lambda: self.pre_configure("ok"))
        self.pushButton_delete.clicked.connect(lambda: self.pre_configure("delete"))
        self.pushButton_modify.clicked.connect(lambda: self.pre_configure("modify"))
        self.read_configure()
        self.show_configure()
        self.comboBox_lightConfiguration.currentTextChanged.connect(self.show_configure)

        self.pushButton_polarity_ok.clicked.connect(lambda: self.pre_polarity("ok"))
        self.pushButton_polarity_delete.clicked.connect(lambda: self.pre_polarity("delete"))
        self.pushButton_polarity_modify.clicked.connect(lambda: self.pre_polarity("modify"))
      
        self.read_polarity()
        self.show_polarity()
        self.comboBox_polarityConfiguration.currentTextChanged.connect(self.show_polarity)

        self.checkBox_same.clicked.connect(lambda: self.checkBox_single.setChecked(False))
        self.checkBox_single.clicked.connect(lambda: self.checkBox_same.setChecked(False))
        self.checkBox_onceLight.clicked.connect(lambda: self.checkBox_moreLight.setChecked(False))
        self.checkBox_moreLight.clicked.connect(lambda: self.checkBox_onceLight.setChecked(False))

        self.lineEdit_production_SN.textChanged.connect(self.data_name)


    def messageDialog(self, value):
        """错误信息提示"""
        QtWidgets.QMessageBox.warning(self, "错误提示", str(value), QtWidgets.QMessageBox.Yes)
        filename = value.__traceback__.tb_frame.f_globals["__file__"]
        errorline = value.__traceback__.tb_lineno
        with open("report.txt", mode="a+") as f:
            f.write(f"{filename}  {errorline}  {value}  [{self.time_check()}]\n")

    def thread_start(self):
        """线程开启"""
        polarity_num = self.textEdit_polarityInput.toPlainText().count("-")
        polarity_config = self.textEdit_polarityInput.toPlainText().split("\n", polarity_num)
        polarity_config_num = int(polarity_config[-1].split("-", 2)[0])

        self.translate = Translate(polarity_config_num)
        self.translate.receive.connect(self.operate_table)
        self.translate.start()
 
    def omron_bbc(self, value):
        """逐位异或校验"""
        res = 0
        for i in value:
            num = ord(i)
            res = res ^ num
        omron_res = value + hex(res)[-2:].upper()+ "*" + "\r" + "\n"
        return omron_res

    def time_check(self):
        """时间戳获取"""
        time_now = datetime.datetime.now()
        now_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
        return now_time

    def init_window(self, value):
        """处理需要显示的信息"""
        self.textEdit_systemNews.append(value + "-" + f"[{self.time_check()}]")

    def auto_search(self):
        """串口自动搜索------测试完成ok"""
        self.comboBox_portcheck.clear()
        port_list = serial.tools.list_ports.comports()
        for i in port_list:
            name = str(i).split(" ", 1)[0]
            self.comboBox_portcheck.addItem(name)
            self.port_com.append(name)
            self.port_com = list(set(self.port_com))
        self.pushButton_portcom.setStyleSheet("background-color:steelblue")
        print(self.port_com)

    def open_port(self):
        """打开串口"""
        self.close_port()
        com = self.comboBox_portcheck.currentText()
        try:
            self.ser = serial.Serial(com, baudrate=115200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=0.5)
        except Exception as e:
            self.messageDialog(e)

    def close_port(self):
        """关闭串口，以及无串口连接时的错误处理"""
        try:
            self.ser.close()
        except Exception as e:
            print(e)
            
    def port_check(self):
        """串口连接检查"""
        try:
            if self.ser.is_open:
                self.pushButton_portcom.setStyleSheet("background-color:seagreen")
                self.pushButton_portcom.setText("连接成功")
                self.init_window("串口连接成功")
            else:
                self.pushButton_portcom.setStyleSheet("background-color:darkred")
                self.pushButton_portcom.setText("连接失败")
        except Exception as e:
            self.messageDialog(e)

    def port_write(self, value):
        """命令写入"""
        try:
            self.ser.write(self.omron_bbc(value.encode("UTF-8")))
            data = self.ser.readline()
            return data
        except Exception as e:
            self.messageDialog(e)
    
    def light_control(self, value):
        """输出界面所需命令格式"""
        backWords = []
        launch = ["@00WR0301", "@00WR0302"]
        self.port_write("@00SC02")
        if value <= 4:
            self.choice_module(launch[0], ["000",""])
        elif value > 4 and value <= 8:
            self.choice_module(launch[0], ["000",""])
            self.choice_module(launch[0], ["00", "0"])
        elif value > 8 and value <= 12:
            self.choice_module(launch[0], ["000",""])
            self.choice_module(launch[0], ["00", "0"])
            self.choice_module(launch[0], ["0", "00"])
        elif value > 12 and value <= 16:
            self.choice_module(launch[0], ["000",""])
            self.choice_module(launch[0], ["00", "0"])
            self.choice_module(launch[0], ["0", "00"])
            self.choice_module(launch[1], ["000", ""])
        elif value > 16 and value <= 20:
            self.choice_module(launch[0], ["000",""])
            self.choice_module(launch[0], ["00", "0"])
            self.choice_module(launch[0], ["0", "00"])
            self.choice_module(launch[1], ["000", ""])
            self.choice_module(launch[1], ["00", "0"])
        elif value > 20 and value <= 24:
            self.choice_module(launch[0], ["000",""])
            self.choice_module(launch[0], ["00", "0"])
            self.choice_module(launch[0], ["0", "00"])
            self.choice_module(launch[1], ["000", ""])
            self.choice_module(launch[1], ["00", "0"])
            self.choice_module(launch[1], ["0", "00"])

        back_dict = {
            "01":"1", "02":"2", "03":"3", "04":"4", "05":"5", "06":"6", "07":"7", "08":"8", "00":"0",
            "09":"9", "0A":"10", "0B":"11", "0C":"12", "0D":"13", "0E":"14", "0F":"15", "10":"16",
            "11":"17", "12":"18" ,"13": "19", "14":"20", "15":"21", "16":"22", "17":"23", "18":"24"
            }
        for i in self.back:
            backWords.append(f"{back_dict[i[0]]}-{back_dict[i[1]]}")

        # backWords = ["1-12", "2-11", "3-10", "4-9", "5-8", "6-7", "7-6", "8-5", "9-4","10-3", "11-2", "12-1"]
        # for i in backWords:
        #     time.sleep(0.5)
        #     print(i)

        return backWords

    def choice_module(self, value, key):
        """1-24亮灯命令执行"""
        try:
            for i in range(4):
                hexEnd = 2**i
                self.port_write(value + f"{key[0]}{hexEnd}{key[1]}")
                data = self.port_write("@00RD00000002")
                self.back.append([str(data[7:9])[-3:-1], str(data[9:11])[-3:-1]])
                self.light_clear()
                self.init_window("完成单条检测")
        except Exception as e:
            self.messageDialog(e)
    
    def light_clear(self):
        """循环复位"""
        self.port_write("@00WR03000001")
        self.port_write("@00WR03000002")

    def pre_configure(self, value:str):
        """通光配置文件预设定"""
        try:
            self.config = PreConfiguration.Configuration()
            configuration_name = "LightCheckConfiguration"
            section = self.lineEdit_productionNumber.text()
            item = self.lineEdit_productionItem.text()
            core = self.lineEdit_productionCore.text()
            data = [configuration_name, section, {"item":item, "core": core}]

            if len(item) != 0 and len(core) != 0 and len(section) != 0 and value == "ok" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.add_section(data))
            elif value == "delete" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.delete_section(data))
            elif value == "modify" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.modify_section(data))
            else:
                self.init_window("请输入管理员名称,并且完善通光配置信息")

            self.comboBox_lightConfiguration.clear()
            self.read_configure()
        except Exception as e:
            self.messageDialog(e)

    def read_configure(self):
        """读取预设定文件至下拉栏"""
        try:
            self.config = PreConfiguration.Configuration()
            data = self.config.count_section("LightCheckConfiguration")
            if len(data) == 0:
                self.init_window("请预设通光配置文件")
            else:
                for i in data:
                    self.comboBox_lightConfiguration.addItem(i)
            del self.config
        except Exception as e:
            self.messageDialog(e)
    
    def show_configure(self):
        """展示配置文件"""
        try:
            self.config = PreConfiguration.Configuration()
            data = self.config.search_option("LightCheckConfiguration", self.comboBox_lightConfiguration.currentText())
            self.lineEdit_productionNumber.setText(self.comboBox_lightConfiguration.currentText())
            self.lineEdit_productionItem.setText(data[0][1])
            self.lineEdit_productionCore.setText(data[1][1])
        except Exception as e:
            self.messageDialog(e)

    def pre_polarity(self, value):
        """预设定极性"""
        try:
            self.config = PreConfiguration.Configuration()
            configuration_name = "PolarityConfiguration"
            section = self.lineEdit_polarityName.text()
            polarity = self.textEdit_polarityInput.toPlainText()

            data = [configuration_name, section, {"polarity":polarity}]

            if len(section) != 0 and len(polarity) != 0 and value == "ok" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.add_section(data))
            elif value == "delete" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.delete_section(data))
            elif value == "modify" and self.lineEdit_operator.text() == self.administrator:
                self.init_window(self.config.modify_section(data))
            else:
                self.init_window("请输入管理员名称,并且完善极性配置信息")

            self.comboBox_polarityConfiguration.clear()

            self.read_polarity()

        except Exception as e:
            self.messageDialog(e)
    
    def read_polarity(self):
        """读取极性文件至下拉栏"""
        try:
            self.config = PreConfiguration.Configuration()
            data = self.config.count_section("PolarityConfiguration")
            if len(data) == 0:
                self.init_window("请预设极性配置文件")
            else:
                for i in data:
                    self.comboBox_polarityConfiguration.addItem(i)
            del self.config
        except Exception as e:
            self.messageDialog(e)

    def show_polarity(self):
        """展示极性配置文件"""
        try:
            self.config = PreConfiguration.Configuration()
            data = self.config.search_option("PolarityConfiguration", self.comboBox_polarityConfiguration.currentText())
            self.lineEdit_polarityName.setText(self.comboBox_polarityConfiguration.currentText())
            self.textEdit_polarityInput.setText(data[0][1])
        except Exception as e:
            self.messageDialog(e)

    def path_configure(self):
        """储存文件路径"""
        pass

    def operate_table(self, key):
        """搜集界面信息"""
        try:
            i_flag = 1
            r_flag = 0
            content_data = []

            production_sn_color = "white"
            production_pn_color = "white"
            branch_sn_color = "white"
            operator_name_color = "white"
            polarity_result_color = "white"
            light_check_time_color = "white"
            production_number_color = "white"
            production_item_color = "white"
            production_core_color = "white"

            name = ["产品S/N", "产品P/N", "操作者名称", "储存路径"]
            if self.checkBox_same.isChecked():
                path = self.lineEdit_same_filepath.text()
            else:
                path = self.lineEdit_single_filepath.text()

            box = [self.lineEdit_production_SN.text(), self.lineEdit_production_PN.text(), self.lineEdit_operator.text(), path]
            for i, n  in enumerate(box):
                if len(n) == 0:
                    self.init_window(f"请输入[{name[i]}]信息")
                    i_flag *= len(n)
                else:
                    i_flag *= len(n)


            if len(self.lineEdit_branch_SN.text()) == 0 or self.lineEdit_branch_SN.text() == "-":
                self.lineEdit_branch_SN.setText(self.lineEdit_production_SN.text() + "-")
            
            polarity_num = self.textEdit_polarityInput.toPlainText().count("-")
            polarity_config = self.textEdit_polarityInput.toPlainText().split("\n", polarity_num)
        
            production_sn = self.lineEdit_production_SN.text()
            production_pn = self.lineEdit_production_PN.text()
            operator_name = self.lineEdit_operator.text()
            light_check_time = self.time_check()
            production_number = self.lineEdit_productionNumber.text()
            production_item = self.lineEdit_productionItem.text()
            production_core = self.lineEdit_productionCore.text()
                

            if self.checkBox_onceLight.isChecked():
                light_check_num = "一次通光"
                light_check_num_color = "white"
            elif self.checkBox_moreLight.isChecked():
                light_check_num = "返修通光"
                light_check_num_color = "darkgray"
            for i, n in enumerate(polarity_config):
                print(n, i)
                polarity_result = n
                if n == key[i]:
                    r_flag += 1
                    passcheck_result = key[i] + "pass"
                    passcheck_result_color = "green"
                else:
                    passcheck_result = key[i] + "fail"
                    passcheck_result_color = "red"
                    
                if "-" in self.lineEdit_branch_SN.text()[-1]:
                    branch_sn = self.lineEdit_branch_SN.text() + n.split("-", 2)[0]
                else:
                    branch_sn = self.lineEdit_branch_SN.text() + "-" + n.split("-", 2)[0]

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

            for i in range(len(polarity_config)):
                content_data.append(self.deal_data(i))
            self.save_data(content_data, path)
            del self.back[:]
        except Exception as e:
            self.messageDialog(e)

    def table_show(self, value:list, key:int):
        """tableWidget展示产品信息"""
        for i, n in enumerate(value):
            new_item = QtWidgets.QTableWidgetItem(n[0])
            new_item.setBackground(QtGui.QBrush(QtGui.QColor(n[1])))
            new_item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.tableWidget_Excel.setRowCount(10 + key)
            self.tableWidget_Excel.setItem(key,i,new_item)

    def data_path(self, value:str):
        """获取文件储存位置"""
        openfile_name = QtWidgets.QFileDialog.getExistingDirectory()
        eval(value).setText(openfile_name)

    def data_name(self):
        """显示文件储存位置"""
        self.lineEdit_same_filename.setText(self.lineEdit_production_SN.text())
        self.lineEdit_single_filename.setText(self.lineEdit_production_SN.text())

    def deal_data(self, key):
        """储存tablewidget中的数据"""
        content_data = []
        num_column = self.tableWidget_Excel.columnCount()
        for i in range(num_column):
            content_column = self.tableWidget_Excel.item(key,i).text()
            content_data.append(content_column)
        return content_data

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
            print(e)
        
       
    def save_data(self, value, path):
        """文件储存"""
        nRows = 0
        file_path = path
        file_name = self.lineEdit_same_filename.text()
        file = f"{file_path}\\{file_name}.xls"

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
        
class Translate(QtCore.QThread):
    receive = QtCore.pyqtSignal(list)

    def __init__(self, value):
        super(Translate, self).__init__()
        self.windows = MyWindow()
        self.value = value

    def run(self):
        try:
            data = self.windows.light_control(self.value)
            self.receive.emit(data)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exit(app.exec_())