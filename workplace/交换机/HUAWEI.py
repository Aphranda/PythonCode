import serial
import serial.tools.list_ports
import time
import os
import datetime
import threading


class Exchange(object):

    def __init__(self):
        self.box = []
        self.res = ["1"]
        self.file = "QC"
        self.filedir = 'QC'  # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
        os.chdir("C:\\Users\\Aphanda\\Desktop\\test")
        if not os.path.exists(self.filedir):
            os.makedirs(self.filedir)
        pass

    @staticmethod
    def show_menu():
        print(
            """
        #========操作界面=========#

             0.退出测试程序 
             1.登录测试程序
             2.10G环路拼包                     
             3.其他环路拼包    
             4.查看测试DDM
             5.文件名称创建
             6.订单单号输入
             7.开启读取线程
             8.退出拼包

        #=========================#
            """
        )
        return input("请输入选择序号：")

    @staticmethod
    def choice_port():
        # print(".......端口搜索中....... " + "\n" + "......请稍等......" )
        # port_list = serial.tools.list_ports.comports()
        # port_box = {}
        # if len(port_list) == 0:
        #     print("无端口可用")
        # else:
        #     n = 0
        #     for i in port_list:
        #         n += 1
        #         port_box[str(n)] = str(i)
        #         print(str(n) + ":-----" + str(i) + "------")
        # port_name = str(input('输入数字选择端口：'))
        # final_com = port_box[port_name][0:4]
        # return final_com
        return 'COM7'

    def open_port(self):
        com = self.choice_port()
        try:
            self.ser = serial.Serial(com, 9600, timeout=0.5)
            print(
                f"===========打开{com}===========" + '\n'
                                                   f"===========打开{com}==========="
            )
        except Exception as e:
            print(
                """
                ===========出现异常===========
                ===========端口断连===========
                ===========出现异常===========
                ===========端口断连===========
                """
            )

    def close_port(self):
        self.ser.close()

    def order_data(self):
        """指令集分类"""
        huawei = {
            "1":
                [
                    '\n',
                    r'N',
                    r'N',
                    r'N'
                ],
            "2":
                [
                    # 10G 环路拼包
                    '\n',
                    r'N',
                    r'system-view',
                    r'interface',
                    r'port mode 10G',
                    r'Y',
                    r'undo portswitch',
                    r'ip address 192.168.3.2 24',
                    r'commit',
                    r'ping -c 135 192.168.3.2'
                ],
            "3":
                [
                    # 25G 环路拼包
                    '\n',
                    r'N',
                    r'system-view',
                    r'interface',
                    r'undo portswitch',
                    r'ip address 192.168.4.2 24',
                    r'commit',
                    r'ping -c 135 192.168.4.2'
                ],
            "4":
                [
                    '\n',
                    r'N',
                    r'display interface transceiver verbose'
                ],
            "7":
                [
                    chr(0x03),
                    r'quit',
                    r'quit'
                ]
        }
        self.data = huawei
        return self.data

    def write_data(self, word):
        key_words = "interface"
        data = self.order_data()
        for i in data[word]:
            time.sleep(0.5)
            if key_words in i:
                a = i.split('interface', 1)
                if len(a[1]) == 0:
                    try:
                        i = "interface" + " " + self.box[-1]
                    except:
                        print(
                            """
                            ===========时间超时，请重新登录然后拔插模块========
                            """
                        )
                if len(a[1]) != 0:
                    try:
                        i = a[0] + "interface" + " " + self.box[-1] + a[1]
                    except:
                        print(
                            """
                            ===========时间超时，请重新登录然后拔插模块========
                            """
                        )
            print(i)
            self.ser.write((i + '\n').encode())

    def receive_data(self):
        self.time_now = datetime.datetime.now()
        all_time = self.time_now.strftime("%Y-%m-%d %H:%M:%S")
        self.res = [f"========up:AOC信息==={all_time}===Down:DDM信息========="]
        while len(self.res[-1]) != 0:
            data = self.ser.readline()
            self.res.append(data)
            print(self.res[-1])
        return self.res

    def back_box(self):
        key_words = "EntPhysicalName"
        data = self.res
        for i in data:
            if key_words in str(i):
                key_line = str(i)
                name_one = key_line.split(key_words, 1)[1].split(",", 1)[0].split("=", 1)[1]
                self.box.append(name_one)
                print(name_one)
        try:
            print(self.box[-1])
        except:
            print(
                """
                ===========时间超时，请重新登录然后拔插模块========
                """
            )

    def select_data(self):
        self.resS = ["Down:DDM信息"]
        data = self.res
        right_words = "Arista Networks"
        for i in data:
            print(i)
            if right_words in str(i):
                self.resS.append(i)
        return self.resS

    def position_data(self):
        data = self.res
        wrong_data = []
        wrong_words = 'unreachable'
        for i in data:
            if wrong_words in str(i):
                wrong_data.append(i)
        print('丢包数量:' + str(len(wrong_data)))

    def save_data(self):
        data = self.res  # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
        with open(f'C:\\Users\\Aphanda\\Desktop\\test\\{self.filedir}\\{self.file}.txt', mode='a+') as f:
            for j in data:
                f.write(str(j) + "\n")

    def send_data(self):
        self.open_port()
        data = self.order_data()
        if not self.ser.isOpen():
            print('端口未连接')
            quit
        while True:
            word = self.show_menu()
            if word == '1':
                self.write_data(word)
                self.receive_data()
            elif word == '2':
                self.write_data(word)
                self.receive_data()
                # self.select_data()
            elif word == '3':
                self.write_data(word)
                self.receive_data()
                # self.save_data()
            elif word == '4':
                self.write_data(word)
                self.receive_data()
                self.save_data()
            elif word == '5':
                self.filedir = input(
                    "请输入文件名：")  # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
                os.chdir("C:\\Users\\Aphanda\\Desktop\\test")
                if not os.path.exists(self.filedir):
                    os.makedirs(self.filedir)
                    os.chdir(self.filedir)
                else:
                    os.chdir(self.filedir)
            elif word == '6':
                self.file = input("请输入单号：")
            elif word == '7':
                self.receive_data()
                self.back_box()
            elif word == '8':
                self.write_data("7")
                self.receive_data()
            elif word == '0':
                if self.ser.isOpen:
                    self.close_port()
                    print("测试退出...")
                    print('退出完成...')
                    break
            else:
                print('输入错误 请正确输入')


def main():
    Port = Exchange()
    Port.send_data()


if __name__ == "__main__":
    main()