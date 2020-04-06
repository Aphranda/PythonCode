import sys
import serial
import xlrd, xlwt
import time
import threading


class UARTTOIIC():
    def __init__(self, value:str):
        self.uartComStr = value

    def portstart(self) -> bool:
        """打开串口"""
        try:
            self.communserialport = serial.Serial(self.uartComStr, 57600, timeout=0.5)
        except Exception as e:
            print('ERROR:' + e)
            return False
        else:
            return True

    def portclose(self) -> bool:
        """关闭串口"""
        try:
            self.communserialport.close()
        except Exception as e:
            print('ERROR:' + e)
            return False
        else:
            return True

    # 数据传输部分
    # 通讯协议复写
    def datatransmit(self, iicSpeed:int):
        uartWriteBuf_100 = bytearray(6)
        uartWriteBuf_200 = bytearray(6)
        uartWriteBuf_400 = bytearray(6)

        uartWriteBuf_100[0] = ord("#")
        uartWriteBuf_100[1] = 6
        uartWriteBuf_100[2] = 0x81
        uartWriteBuf_100[3] = 0x00
        uartWriteBuf_100[4] = 0x93
        uartWriteBuf_100[5] = ord("$")

        uartWriteBuf_200[0] = ord("#")
        uartWriteBuf_200[1] = 6
        uartWriteBuf_200[2] = 0x81
        uartWriteBuf_200[3] = 0x00
        uartWriteBuf_200[4] = 0xec
        uartWriteBuf_200[5] = ord("$")

        uartWriteBuf_400[0] = ord("#")
        uartWriteBuf_400[1] = 6
        uartWriteBuf_400[2] = 0x81
        uartWriteBuf_400[3] = 0x01
        uartWriteBuf_400[4] = 0xa1
        uartWriteBuf_400[5] = ord("$")

        if iicSpeed == 100:
            try:
                self.communserialport.write(uartWriteBuf_100)
            except Exception as e:
                print(e)
                return "串口链接断开"
        elif iicSpeed == 200: 
            try:
                self.communserialport.write(uartWriteBuf_200)
            except Exception as e:
                print(e)
                return "串口链接断开"
        elif iicSpeed == 400:
            try:
                self.communserialport.write(uartWriteBuf_400)
            except Exception as e:
                print(e)
                return "串口链接断开"
        else:
            try:
                self.communserialport.write(uartWriteBuf_100)
            except Exception as e:
                print(e)
                return "串口链接断开"

        
