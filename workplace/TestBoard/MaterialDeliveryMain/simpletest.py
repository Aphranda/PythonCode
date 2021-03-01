import serial
import time

try:
    ser = serial.Serial("COM6", 115200, timeout=0.5)
    ser_01 = serial.Serial("COM5", 115200, timeout=0.5)
    ser.bytesize = 8
    ser.bytesize = serial.EIGHTBITS
except Exception as e:
    print("无法打开端口" + str(e))


def write_d(data):

    try:
        ser.write(data)
        ser_01.write(data)
        print(data)
    except Exception as e:
        print(e)


def receive():
    try:
        receive_words = ser.readlines()
        print(len(receive_words[0]))
        print(receive_words)
        with open(r'D:\PythonCode\code\workplace\TestBoard\MaterialDeliveryMain\WM.txt', mode='a+') as f:
            f.write(str(receive_words) + '\n')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    i = 0
    data_Pattern_00 = [0x7e, 0x00, 0x7d, 0x5e, 0x00, 0x00, 0x7d, 0x5e, 0x7e]

    data_Pattern_01 = [0x7e, 0x10, 0x86, 0x00, 0x02, 0x01, 0x01, 0x9a, 0x7e]

    trans_data_Pattern = [0x7e, 0x0A, 0x00, 0x00, 0x00, 0xA, 0x7e]

    trans_data_open = [0x7e, 0x10, 0x80, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x93, 0x7e]

    try:
        write_d(data_Pattern_00)
        receive()
    except Exception as e:
        print(e)

   