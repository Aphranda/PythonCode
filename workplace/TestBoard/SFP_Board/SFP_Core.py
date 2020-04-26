import threading
import math

cache02 = [
    [b'#\x03$'],
    [b'#\x04$'],
    [b'#\x07$'],
    [b'#\x10\x00\x00\x00\x00\x00\x00\x00$'],
    [b'#\x06$'],
    [b'#g$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x03$'],
    [b'#\x00$'],
    [b'#CISCO           $'],
    [b'#\x00$'],
    [b'#$\x00\x00$'],
    [b'#SFP-10G-AOC-03M $'],
    [b'#1.0 $'],
    [b'#R\x00$'],
    [b'#\x00$'],
    [b'#B$'],
    [b'#\n', b'\x1a$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#M181130         $'],
    [b'#181116  $'],
    [b'#h$'],
    [b'#\xf0$'],
    [b'#\x01$'],
    [b'#\x8a$'],
    [b'#\x00\x00\x11_"\xa4\x8b\xa3\\;[o\x81\xf2N@T\xe8{\x00\x00\x00\x00\x00\x00\x00\x00\x00gV\xcf\x00$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$']
]

cache01 = [
    [b'#_\x00\xce\x00U\x00\xf6\x00\x8d\xccrt\x88\xb8v\\\x1dL\x03\xe8\x17p\x05\xdcN \x03\xbbEv\x05\xeaN \x00\xe5Ev\x01k$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x80\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00$'],
    [b'#\x00\x00\x00$'],
    [b'#\x98$'],
    [b'#\x1c\x1c~\xe0\x0c\x86#\xf6\x00\x01$'],
    [b'#\x00\x00\x00\x00$'],
    [b'#\x02$'],
    [b'#\x00$'],
    [b'#\x00@$'],
    [b'#\x00$'],
    [b'#\x00$'],
    [b'#\x00@$'],
    [b'#\x00\x00$'],
    [b'#\x00\x00\x00\x00\x00\x00\x00$'],
    [b'#\x00$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\x00\x00\xff\xff$'],
    [b'#\xff$'],
    [b'#\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$'],
    [b'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff$']

]


class Core(object):
    def __init__(self):
        self.register_a0_sfp = {
            "0": "1",
            "1": "1",
            "2": "1",
            "3": "8",
            "11": "1",
            "12": "1",
            "13": "1",
            "14": "1",
            "15": "1",
            "16": "1",
            "17": "1",
            "18": "1",
            "19": "1",
            "20": "16",
            "36": "1",
            "37": "3",
            "40": "16",
            "56": "4",
            "61": "2",
            "62": "1",
            "63": "1",
            "64": "2",
            "66": "1",
            "67": "1",
            "68": "16",
            "84": "8",
            "92": "1",
            "93": "1",
            "94": "1",
            "95": "1",
            "96": "32",
            "128": "128"
        }
        self.register_a2_sfp = {
            "0": "40",
            "40": "16",
            "56": "36",
            "92": "3",
            "95": "1",
            "96": "10",
            "106": "4"
        }
        self.register_a0_qsfp = {}
        self.register_a2_qsfp = {}
        self.threshold_0_39 = []
        self.threshold_40_55 = []
        self.present_96_105 = []
        self.optional_106_109 = []
        self.threshold_dict = {}

    @staticmethod
    def scale_t(high, low):
        """-128/+128算法"""
        # 去掉0b，转换字符串
        bs_h = str(bin(high)).replace("0b", "")
        bs_l = str(bin(low)).replace("0b", "")
        # 高位补0
        bs_hl = 8 - len(bs_h)
        bs_ll = 8 - len(bs_l)
        bs_h = bs_hl*"0" + bs_h
        bs_l = bs_ll*"0" + bs_l
        # 数据计算
        res_h = int(bs_h[1])*64 + int(bs_h[2])*32 + int(bs_h[3])*16 + int(bs_h[4])*8 + int(bs_h[5])*4 + int(bs_h[6])*2 + int(bs_h[7])*1
        res_l = int(bs_l[7])/256 + int(bs_l[6])/128 + int(bs_l[5])/64 + int(bs_l[4])/32 + int(bs_l[3])/16 + int(bs_l[2])/8 + int(bs_l[1])/4 + int(bs_l[0])/2
        if bs_h[0] is "0":
            return res_h + res_l
        else:
            return -(res_h + res_l)
        
    @staticmethod
    def scale_v(high, low):
        """0/65535算法"""
        # 去掉0b，转换字符串
        bs_h = str(bin(high)).replace("0b", "")
        bs_l = str(bin(low)).replace("0b", "")
        # 高位补0
        bs_hl = 8 - len(bs_h)
        bs_ll = 8 - len(bs_l)
        bs_h = bs_hl*"0" + bs_h
        bs_l = bs_ll*"0" + bs_l
        # 数据计算
        res_h = int(bs_h[0])*32768 + int(bs_h[1])*16384 + int(bs_h[2])*8192 + int(bs_h[3])*4096 + int(bs_h[4])*2048 + int(bs_h[5])*1024 + int(bs_h[6])*512 + int(bs_h[7])*256
        res_l = int(bs_l[7])*128 + int(bs_l[6])*64 + int(bs_l[5])*32 + int(bs_l[4])*16 + int(bs_l[3])*8 + int(bs_l[2])*4 + int(bs_l[1])*2 + int(bs_l[0])*1
        return res_h + res_l

    @staticmethod
    def scale_e(high, low):
        """TEC算法"""
        # 去掉0b，转换字符串
        bs_h = str(bin(high)).replace("0b", "")
        bs_l = str(bin(low)).replace("0b", "")
        # 高位补0
        bs_hl = 8 - len(bs_h)
        bs_ll = 8 - len(bs_l)
        bs_h = bs_hl*"0" + bs_h
        bs_l = bs_ll*"0" + bs_l
        # 数据计算
        res_h = int(bs_h[1])*1638.4 + int(bs_h[2])*819.2 + int(bs_h[3])*409.6 + int(bs_h[4])*204.8 + int(bs_h[5])*102.4 + int(bs_h[6])*51.2 + int(bs_h[7])*25.6
        res_l = int(bs_l[7])*12.8 + int(bs_l[6])*6.4 + int(bs_l[5])*3.2 + int(bs_l[4])*1.6 + int(bs_l[3])*0.8 + int(bs_l[2])*0.4 + int(bs_l[1])*0.2 + int(bs_l[0])*0.1
        if bs_h[0] is "0":
            return res_h + res_l
        else:
            return -(res_h + res_l)

    @staticmethod
    def threshold_decode(data: list, box: list):
        """门限解码"""
        for i in data:
            for j in i:
                box.append(j)
        del box[0]
        del box[-1]
        return box

    def match_t(self, name: list, data: list, box: dict):
        """温度储存门限"""
        for i, n in enumerate(name):
            box[n] = self.scale_t(data[2*i], data[2*i+1])
        return box
    
    def match_v(self, name: list, data: list, box: dict):
        """电压储存门限"""
        for i, n in enumerate(name):
            box[n] = self.scale_v(data[2*i], data[2*i+1])/10000
        return box
    
    def match_c(self, name: list, data: list, box: dict):
        """电流储存门限"""
        for i, n in enumerate(name):
            box[n] = self.scale_v(data[2*i], data[2*i+1])/500
        return box

    def match_p(self, name: list, data: list, box: dict):
        """功率储存门限"""
        for i, n in enumerate(name):
            box[n] = math.log10(self.scale_v(data[2*i], data[2*i+1])/10000)*10
        return box
    
    def match_e(self, name: list, data: list, box: dict):
        """TEC储存门限"""
        for i, n in enumerate(name):
            box[n] = self.scale_e(data[2*i], data[2*i+1])/500
        return box

    def opposition_data(self, data):
        """解码公式"""
        # 数据名称
        aw_thresholds = ['Temp High Alarm', 'Temp Low Alarm', 'Temp High Warning', 'Temp Low Warning',
                         'Voltage High Alarm', 'Voltage Low Alarm', 'Voltage High Warning', 'Voltage Low Warning',
                         'Bias High Alarm', 'Bias Low Alarm', 'Bias High Warning', 'Bias Low Warning',
                         'TX Power High Alarm', 'TX Power Low Alarm', 'TX Power High Warning', 'TX Power Low Warning',
                         'RX Power High Alarm', 'RX Power Low Alarm', 'RX Power High Warning', 'RX Power Low Warning']
        optional_aw_thresholds = ['Optional Laser Temp High Alarm', 'Optional Laser Temp Low Alarm',
                                  'Optional Laser Temp High Warning', 'Optional Laser Temp Low Warning',
                                  'Optional TEC Current High Alarm', 'Optional TEC Current Low Alarm',
                                  'Optional TEC Current High Warning', 'Optional TEC Current Low Warning']
        present_name = ['Temperature', "Vcc", 'Bias', 'TX Power', 'RX Power']

        optional_name = ['OLT', 'OTC']

        # 0-39门限解码
        self.threshold_decode(data[0], self.threshold_0_39)
        # 40-55门限解码
        self.threshold_decode(data[1], self.threshold_40_55)
        # 96-105当前数据解码
        self.threshold_decode(data[5], self.present_96_105)
        # 105-109当前数据解码
        self.threshold_decode(data[6], self.optional_106_109)

        # 数据匹配提取
        # 温度数据匹配提取
        self.match_t(aw_thresholds[0:4], self.threshold_0_39[0:8], self.threshold_dict)
        # print(self.threshold_40_55[0:8])
        # 电压数据匹配提取
        self.match_v(aw_thresholds[4:8], self.threshold_0_39[8:16], self.threshold_dict)
        # 电流数据匹配提取
        self.match_c(aw_thresholds[8:12], self.threshold_0_39[16:24], self.threshold_dict)
        # 功率数据匹配提取
        self.match_p(aw_thresholds[12:20], self.threshold_0_39[24:40], self.threshold_dict)
        # print(self.threshold_0_39[24:40])
        # 激光器温度匹配提取
        self.match_t(optional_aw_thresholds[0:4], self.threshold_40_55[0:8], self.threshold_dict)
        # TEC电流匹配提取
        self.match_e(optional_aw_thresholds[4:8], self.threshold_40_55[8:16], self.threshold_dict)
        # print(self.threshold_0_39[16:24])
        
        # 实际温度匹配提取
        self.match_t(present_name[0:1], self.present_96_105[0:2], self.threshold_dict)
        # 实际电压匹配提取
        self.match_v(present_name[1:2], self.present_96_105[2:4], self.threshold_dict)
        # 实际电流匹配提取
        self.match_c(present_name[2:3], self.present_96_105[4:6], self.threshold_dict)
        # 实际功率匹配提取
        self.match_p(present_name[3:4], self.present_96_105[6:8], self.threshold_dict)
        self.match_p(present_name[4:5], self.present_96_105[8:10], self.threshold_dict)
        # print(self.present_96_105[6:8])
        # olt 匹配提取
        self.match_t(optional_name[0:1], self.optional_106_109[0:2], self.threshold_dict)
        # TEC电流匹配提取
        self.match_e(optional_name[1:2], self.optional_106_109[2:4], self.threshold_dict)
        # print(self.threshold_dict)
        # for i in self.threshold_dict:
        #     print(i + " : " + str(self.threshold_dict[i]))
        # print(self.threshold_dict["Temperature"])
        return self.threshold_dict

    # def clear_data(self):
    #     del self.threshold_0_39[:]
    #     del self.threshold_40_55[:]
    #     del self.present_96_105[:]
    #     del self.optional_106_109[:]
    #     print(self.threshold_dict)
    #     self.threshold_dict = {}
    #     print(self.threshold_dict)


# def main():
#     core = Core()
#     core.opposition_data(cache01)


# if __name__ == '__main__':
#     main()
