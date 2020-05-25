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
    "96": "10",
    "106": "4"

}

try:
    ser = serial.Serial("COM5", 115200, timeout=0.5)
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
        print(len(receive_words[0]))
        print(receive_words)
        with open(r'D:\PythonCode\code\workplace\TestBoard\MaterialDeliveryMain\WM.txt', mode='a+') as f:
            f.write(str(receive_words) + '\n')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    data_Pattern = [0x7e, 0x10, 0x82, 0x00, 0x03, 0x01, 0x01, 0x05, 0x9c, 0x7e]
    data_WM = [0x7e, 0x10, 0x00, 0x00, 0x00, 0x10, 0x7e]
    data_zf = [0x7e, 0x10, 0x06, 0x00, 0x00, 0x16, 0x7e]
    write_d(data_zf)
    receive()


   