import serial
import time

data_A0 = {
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

data_A2 = {
    "0": "40",
    "40": "16",
    "56": "36",
    "92": "3",
    "95": "1",
    "96": "10",
    "106": "4",
    "110": "1",
    "111": "1",
    "112": "2",
    "114": "1",
    "115": "1",
    "116": "2",
    "118": "2",
    "120": "7",
    "127": "1",
    "128": "120",
    "248": "8",
    "126": "4",
    "130": "1",
    "131": "1",
    "132": "41",
    "173": "83"

}

try:
    ser = serial.Serial("COM8", 57600, timeout=0.5)
    ser.bytesize = 8
    ser.bytesize = serial.EIGHTBITS
except Exception as e:
    print("无法打开端口" + str(e))


def write_d(data):

    try:
        ser.write(data)
        print(data)
    except Exception as e:
        print(e)


def receive():
    try:
        receive_words = ser.readlines()
        print(receive_words)
        with open(r'D:\PythonCode\code\workplace\TestBoard\MaterialDeliveryMain\SFP_A2_02.txt', mode='a+') as f:
            f.write(str(receive_words) + '\n')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in data_A2:
        data = [0x23, 0x07, 0x06, 0xA2, int(i), int(data_A2[i]), 0x24]
        write_d(data)
        receive()


    # data = bytearray(6)
    #
    # data[0] = 0x23
    # data[1] = 0x06
    # data[2] = 0x81
    # data[3] = 0x00
    # data[4] = 0x93
    # data[5] = 0x24
    # data = b'\\0x23\\0x06\\0x81\\0x00\\0x93\\0x24'
    # aubUARTWriteBuf(0) = Asc("#")
    # 'Start Byte
    # aubUARTWriteBuf(1) = 7
    # 'Total Length
    # aubUARTWriteBuf(2) = 6
    # '读
    # aubUARTWriteBuf(3) = bIICDeviceAddress
    # 'IIC器件地址
    # aubUARTWriteBuf(4) = bIICDataStartAddress
    # '寄存器地址
    # aubUARTWriteBuf(5) = bIICReadDataLength
    # '读取长度
    # aubUARTWriteBuf(6) = Asc("$")