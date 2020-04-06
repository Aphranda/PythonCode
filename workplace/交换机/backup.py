import serial
import serial.tools.list_ports
import time
import threading


# import tempfile,sys
# sys.stderr=tempfile.TemporaryFile()


class Exchange(object):

    def __init__(self, data):
        self.data = data
        pass

    @staticmethod
    def choice_switches():
        print(
            """
            ===========交换机选择===========

                     1.思科交换机
                        1.10G-25G 
                        2.40G-100G
                        3.4*10 25*4
                     2.华为交换机
                        1.10G 25G 100G
                     3.测试交换机

            ===========交换机选择===========
            """
        )
        return input('输入数字选择交换机：')

    @staticmethod
    def show_menu():
        print(
            """
        #========操作界面=========#

             0.关闭端口退出界面  
             1.输出端口信息         
             2.开启环路拼包         
             3.华为交换机25G拼包       
             4.读SFP端口DDM    
             5.读QSFP端口DDM
             6.登录并查询端口信息
             7.思科QSFP-4XSFP 40G端口DDM
             8.思科QSFP-4XSFP 100G端口DDM

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
        huawei = {
            "2":
                [
                    # 10G 环路拼包
                    r'system-view',
                    r'int 25ge1/0/*',
                    r'port mode 10G',
                    r'undo portswitch',
                    r'ip address 192.168.3.2.24',
                    r'commit',
                    r'ping -c 10000 192.168.x.x'
                ],
            "3":
                [
                    # 25G 环路拼包
                    r'int 25ge1/0/*',
                    r'undo portswitch',
                    r'ip address 192.168.3.2.24',
                    r'commit',
                    r'ping -c 10000 192.168.x.x'
                ],
            "4":
                [
                    r'display interface 25GE1/0/* transceiver verbose'
                ],
            "5":
                [
                    r'display interface 100GE1/0/* transceiver verbose'
                ],
            "6":
                [
                    r'/n',
                    r'system-view'
                ]
        }

        cisco_1025 = {
            "2":
                [
                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.1.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',
                    r'ping',
                    r'\n',
                    r'using default context',
                    r'1.1.1.6',
                    r'100000',
                    r'1000',
                    r'/n',
                    r'/n',
                    r'/n',
                    r'/n'

                ],
            "3":
                [
                    r'sh interface ethernet 1/* transceiver details'
                ],
            "4":
                [
                    r'sh interface transceiver details'
                ],
            "5":
                [],
            "6":
                [
                    r'admin',
                    r'admin',
                    r'admin',
                    r'TSn9koo1'
                ]
        }
        cisco_40100 = {
            "2":
                [
                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.1.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',

                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.2.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',

                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.3.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',

                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.4.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',

                    r'ping',
                    r'\n',
                    r'using default context',
                    r'1.1.1.6',
                    r'100000',
                    r'1000',
                    r'/n',
                    r'/n',
                    r'/n',
                    r'/n'
                ],
            "3":
                [],
            "4":
                [],
            "5":
                [
                    r'sh interface transceiver details'
                ],
            "6":
                [
                    r'admin',
                    r'admin',
                    r'admin',
                    r'TSn9koo1',
                    r'show inv',
                    r'config t',
                    r'int eth 1/*',
                    r'shutdown',
                ],
            "7":  # 打开QFSP-4XSFP 40-10
                [
                    r'config t'
                    r'interface breakout module 1 port 50 map 10g-4x',
                    r'interface breakout module 1 port 52 map 10g-4x'
                ],
            "8":
                [
                    r'config t'
                    r'interface breakout module 1 port 50 map 25g-4x',
                    r'interface breakout module 1 port 50 map 25g-4x'

                ]
        }
        cisco_test = {
            "2":
                [
                    r'config t',
                    r'int eth 1/*',
                    r'no sh',
                    r'ip address 1.1.1.6 255.255.255.0'
                    r'no sh',
                    r'exit',
                    r'exit',
                    r'ping',
                    r'\n',
                    r'using default context',
                    r'1.1.1.6',
                    r'100000',
                    r'1000',
                    r'/n',
                    r'/n',
                    r'/n',
                    r'/n'
                ],
            "3":
                [],
            "4":
                [
                    r'show inter ether 33 tran det',
                    r'show inter ether 34 tran det'
                ],
            "5":
                [],
            "6":
                [
                    r'admin',
                    r'admin',
                    r'admin',
                    r'abc123',
                    r'show inv'
                ]
        }
        choice = self.choice_switches()
        if choice == '11':
            self.data = cisco_1025
            return self.data
        elif choice == '12':
            self.data = cisco_40100
            return self.data
        elif choice == '13':
            return None
        elif choice == '21':
            self.data = huawei
            return self.data
        elif choice == '3':
            self.data = cisco_test
            return self.data

    def write_data(self, data, word):
        data = self.order_data()
        for i in data[word]:
            time.sleep(0.5)
            print(i)
            self.ser.write((i + '\n').encode())

    def receive_data(self):
        res = ["1", "2"]
        while True:
            data = self.ser.readline()
            res.append(data)
            if len(res[-1]) == 0:
                break
        for i in res:
            print(i)
        return res

    def position_data(self):
        pass

    def save_data(self):
        pass

    def send_data(self, data: dict):
        self.open_port()
        if not self.ser.isOpen():
            print('端口未连接')
            quit
        while True:
            word = self.show_menu()
            if word == '1':
                print('#==================' + self.ser.name + '==================#')
            elif word == '2':
                print(data['2'])
                self.write_data(data, word)
            elif word == '3':
                print(data['3'])
                self.write_data(data, word)
                self.receive_data()
            elif word == '4':
                print(data['4'])
                self.write_data(data, word)
                self.receive_data()
            elif word == '5':
                print(data['5'])
                self.write_data(data, word)
                self.receive_data()
            elif word == '6':
                print(data['6'])
                self.write_data(data, word)
                self.receive_data()
            elif word == '0':
                if self.ser.isOpen:
                    self.close_port()
                    print("测试退出中...")
                    time.sleep(0.5)
                    print('退出完成')
                    break
            else:
                print('请正确输入')


def main():
    data = {
        '2':
            [
                r'system-view',
                r'int 25ge1/0/*',
                r'port mode 10G',
                r'undo portswitch',
                r'ip address 192.168.3.2.24',
                r'commit'
            ],
        '3':
            [
                r'ping -c 10000 192.168.2.4'
            ],
        '4':
            [
                # r'display interface 25GE1/0/* transceiver verbose:'
                r'show inter ether 33 tran det',
                r'show inter ether 34 tran det',
            ],
        '5':
            [
                r'display interface 100GE1/0/* transceiver verbose:'
            ],
        '6':
            [
                r'admin',
                r'admin',
                r'admin',
                r'abc123',
                r'show inv'
            ]
    }
    Port = Exchange(data)
    Port.send_data(data)


if __name__ == "__main__":
    main()