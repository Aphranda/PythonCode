import serial
import serial.tools.list_ports


class MyPort(object):
    def __init__(self):
        self.port_name = ["boardTA", "boardTB", "boardEA", "boardEB"]

    def port_sort(self):
        """打开并检测端口，依据返回值进行排序整合"""
        port_sign = []
        check_data = {
            b"#": [0x23, 0x07, 0x06, 0xA2, 0x00, 0x01, 0x24],
            b"7e": [0x7e, 0x10, 0x00, 0x00, 0x00, 0x10, 0x7e]
        }
        port_list = serial.tools.list_ports.comports()
        for i in port_list:
            name = str(i).split("-", 1)[0].replace(" ", "")
            port_sign.append(name)
        for j in port_sign:
            j = serial.Serial(j, baudrate=9600, bytesize=8, timeout=1)
            for k in check_data:
                j.write(check_data[k])
                receive = j.readlines()
                if k in receive:
                    globals()[self.port_name[0]] = k
                else:
                    globals()[self.port_name[3]] = k

    def port_check(self):
        """对四个端口进行独立判断，以确定端口状态"""
        pass

    def port_write(self):
        """向不同端口写入相应信息，并进行返回"""
        # 此处需要四个线程独立读写
        pass

    def port_read(self):
        """读取端口返回值，并以列表形式输出"""
        pass


def main():
    my_port = MyPort()
    my_port.port_sort()


if __name__ == '__main__':
    main()
