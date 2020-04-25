from PIL import ImageGrab, Image
from xlutils.copy import copy
import pytesseract
import xlwt
import xlrd

class Visual():
    def __init__(self):
        self.path = r'D:\PythonCode\code\workplace\截图识别\picture\3.14.png'
        self.date_file = r'D:\PythonCode\code\workplace\截图识别\data\data.xls'
        self.bbox = (135, 290, 200, 400)
        self.span = 8
        self.row = 1

    def screenshot(self):
        im = ImageGrab.grab(self.bbox)
        im.save(self.path)

    def identify(self):
        data = Image.open(self.path)
        print(data)
        text = pytesseract.image_to_string(data)
        self.txt = text.split("\n", self.span)

    def read_data(self):
        data = xlrd.open_workbook(self.date_file)
        excel = copy(data)
        table = excel.get_sheet(0)
        n = 0
        for i in self.txt:
            if len(i) != 0:
                table.write(self.row, n+1, str(i))
                n += 1
                print(i)
        excel.save(self.date_file)
