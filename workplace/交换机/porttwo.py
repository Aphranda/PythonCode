import serial
import time
import threading


class Exchange(object):

    def __init__(self, com, data):
        self.com = com
        self.data = data
        pass

    @staticmethod
    def show_menu():
        print(
            """
        #========操作界面=========#
                               
             0.关闭端口退出界面  
             1.输出端口信息         
             2.开启环路拼包         
             3.ping指令，判断丢包率         
             4.读SFP端口DDM    
             5.读QSFP端口DDM   
                              
        #=========================#
            """
        )
        return input("请输入选择序号：")

    def open_port(self):
        self.ser = serial.Serial(self.com, 9600, timeout=0.5)

    def close_port(self):
        self.ser.close()

    def write_data(self, data, word):
        for i in data[word]:
            time.sleep(0.5)
            print(i)
            self.ser.write((i + '\n').encode())

    def receive_data(self):
        data = self.ser.readline()
        print(data)
        return data

    def position_data(self):
        pass

    def save_data(self):
        pass

    def send_data(self, data:dict):
        self.open_port()
        while True:
            word = self.show_menu()
            if word == '1':
                print(
                    self.ser.name
                )
            elif word == '2':
                print(data['2'])
                self.write_data(data, word)
            elif word == '3':
                print(data['3'])
                self.write_data(data, word)
            elif word == '4':
                print(data['4'])
                while True:
                    self.write_data(data, word)
                    self.receive_data()
            elif word == '5':
                print(data['5'])
                self.write_data(data, word)
                while True:
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
    com = 'COM7'
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
            r'display interface 25GE1/0/* transceiver verbose:'
        ],
        '5':
        [
            r'display interface 100GE1/0/* transceiver verbose:'
        ]
    }
    Port = Exchange(com, data)

    Port.send_data(data)


if __name__ == "__main__":
    main()