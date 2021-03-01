import serial
import serial.tools.list_ports



class PlcPort(object):
    def __init__(self):
        self.flag = "@00RD00000001"

    def omron_bbc(self, value):
        """逐位异或校验"""
        res = 0
        for i in value:
            num = ord(i)
            res = res ^ num
        omron_res = value + hex(res)[-2:] + "*" + "\r"
        print(omron_res)
        return omron_res.upper()
    

    def search_port(self):
        try:
            print(".......端口搜索中....... " + "\n" + "......请稍等......")
            port_list = serial.tools.list_ports.comports()
            port_box = {}
            if len(port_list) == 0:
                print("无端口可用")
            else:
                n = 0
                for i in port_list:
                    n += 1
                    port_box[str(n)] = str(i)
                    print(str(n) + ":-----" + str(i) + "------")
            port_name = str(input('输入数字选择端口：'))
            final_com = port_box[port_name][0:4]
            return final_com
        except:
            print("\033[0;37;32m\t=======输入错误，请重新输入========\033[0m")

    def open_port(self):
        com = self.search_port()
        try:
            self.ser = serial.Serial(com, baudrate=115200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=0.5)
        except Exception as e:
            print(e)


    def read_data(self):
        while self.flag != self.omron_bbc("1"):
            self.flag = self.omron_bbc(input("请输入控制命令："))
            self.ser.write((self.flag + "\n").encode("UTF-8"))
            data = self.ser.readlines()
            with open ("Testdata.txt", mode="a+") as f:
                f.write(str(self.flag) + str(data) + "\n\r")
            print(data)
            

def main():
    Port = PlcPort()
    Port.open_port()
    Port.read_data()
    # key= ["1-8", "2-7", "3-6", "4-5", "5-4", "6-3", "7-2", "8-1"]
    # key= ["1-12", "2-11", "3-10", "4-9", "5-8", "6-7", "7-6", "8-5", "9-4","10-3", "11-2", "12-1"]


if __name__ == "__main__":
    main()