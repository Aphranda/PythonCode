import serial
import serial.tools.list_ports
import time
import os
import datetime


class Exchange(object):

    def __init__(self):
        self.res = ["1"]
        self.file = "QC"
        self.filedir = 'QC' # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
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
             2.10G/25环路拼包
             3.40G/100G环路拼包                     
             4.读SFP端口DDM    
             5.读QSFP端口DDM
             6.文件名称创建
             7.订单单号输入
             8.退出拼包
             9.一分四拼包
                              
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
        return "COM6"


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
        cisco_1025 = {
            "1":
                [
                    '\n',
                    '\n',
                    r'admin',
                    r'TSn9k001',
                ],
            "2":
            [
                r'config t',
                r'int eth 1/7',
                r'no sh',
                r'no sw',
                r'ip address 1.1.1.6 255.255.255.0',
                r'no sh',
                r'exit',
                r'exit',
                r'ping',
                '',
                r'1.1.1.6',
                r'1000',
                r'1000',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'

                
            ],
            "4":
            [
                r'  sh interface ethernet 1/7 transceiver details',
                r'  sh interface ethernet 1/21 transceiver details'
            ],
            "5":
            [
                r'      sh interface ethernet 1/50 transceiver details',
                r'      sh interface ethernet 1/52 transceiver details',
            ],
            "8":
            [
                chr(0x03),
                r'quit',
                r'quit'
            ],
            "a":
            [
                r'config t',
                r'int eth 1/50/1',
                r'no sh',
                r'no sw',
                r'ip address 1.1.1.6 255.255.255.0',
                r'no sh',
                r'exit',
                r'exit',
                r'ping',
                '',
                r'1.1.1.6',
                r'100000',
                r'1000',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'

            ],
            "b":
            [
                r'config t',
                r'int eth 1/50/2',
                r'no sh',
                r'no sw',
                r'ip address 1.1.2.6 255.255.255.0',
                r'no sh',
                r'exit',
                r'exit',
                r'ping',
                '',
                r'1.1.1.6',
                r'100000',
                r'1000',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'

            ],
            "c":
            [
                r'config t',
                r'int eth 1/50/3',
                r'no sh',
                r'no sw',
                r'ip address 1.1.3.6 255.255.255.0',
                r'no sh',
                r'exit',
                r'exit',
                r'ping',
                '',
                r'1.1.1.6',
                r'100000',
                r'1000',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'

            ],
            "d":
            [
                r'config t',
                r'int eth 1/50/4',
                r'no sh',
                r'no sw',
                r'ip address 1.1.4.6 255.255.255.0',
                r'no sh',
                r'exit',
                r'exit',
                r'ping',
                '',
                r'1.1.1.6',
                r'100000',
                r'1000',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'
            ]

        }
        self.data = cisco_1025
        return self.data

    def write_data(self, word):
        data = self.order_data()
        for i in data[word]:
            time.sleep(0.5)
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
        data = self.resS + self.res # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
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
                # self.position_data()
            elif word == '5':
                self.write_data(word)
                self.receive_data()
            elif word == '8':
                self.write_data(word)
                self.receive_data()
            elif word == '6':
                self.filedir = input("请输入文件名：") # C:\\Users\\Aphanda\\Desktop\\test C:\\Users\\Administrator\\Desktop\\data
                os.chdir("C:\\Users\\Aphanda\\Desktop\\test")
                if not os.path.exists(self.filedir):
                    os.makedirs(self.filedir)
                    os.chdir(self.filedir)
                else:
                    os.chdir(self.filedir)
            elif word == '7':
                self.file = input("请输入单号：")
            elif word == "9":
                self.write_data("a")
                self.receive_data()
                time.sleep(60)
                self.write_data("8")
                self.write_data("b")
                self.receive_data()
                time.sleep(60)
                self.write_data("8")
                self.write_data("c")
                self.receive_data()
                time.sleep(60)
                self.write_data("8")
                self.write_data("d")
                self.receive_data()
            elif word == '0':
                if self.ser.isOpen:
                    self.close_port()
                    print("测试退出...")
                    time.sleep(0.5)
                    print('退出完成...')
                    break
            else:
                print('输入错误 请正确输入')


def main():
    Port = Exchange()
    Port.send_data()


if __name__ == "__main__":
    main()