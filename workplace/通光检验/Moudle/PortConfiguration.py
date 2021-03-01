import serial
import serial.tools.list_ports
from ErrorConfiguration import Logits

class Port(object):
    def __init__(self):
       self.port_com = []


    def omron_bbc(self, value):
        """逐位异或校验"""
        try:
            res = 0
            for i in value:
                num = ord(i)
                res = res ^ num
            omron_res = value + hex(res)[-2:].upper()+ "*" + "\r" + "\n"
            return omron_res
        except Exception as e:
            print(e)

    def auto_search(self):
        """串口自动搜索"""
        try:
            port_com = []
            port_list = serial.tools.list_ports.comports()
            for i in port_list:
                name = str(i).split(" ", 1)[0]
                port_com.append(name)
                port_com = list(set(port_com))
            print(port_com)
            return port_com
        except Exception as e:
            print("auto_search-" + str(e))

    def open_port(self, value):
        """打开串口"""
        self.close_port()
        try:
            self.ser = serial.Serial(value, baudrate=115200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=0.1)
        except Exception as e:
            print("open_port" + str(e))

    def close_port(self):
        """关闭串口"""
        try:
            self.ser.close()
        except Exception as e:
            print("close_port-" + str(e))
    
    def judge_port(self):
        """判断串口状态"""
        try:
            if self.ser.is_open:
                print("True")
                return True
            return False
        except Exception as e:
            print("judge_port-" + str(e))

    def port_write(self, value):
        """串口写入/返回"""
        try:
            self.ser.write(self.omron_bbc(value).encode("UTF-8"))
            return self.ser.readline()
        except Exception as e:
            print("port_write-" + str(e))


if __name__ == "__main__":
    port = Port()
    com = port.auto_search()[0]
    port.open_port(com)
    port.judge_port()