import xlrd
import xlwt

class Excel(object):
    def __init__(self, path, name):
        self.path = path
        self.path = name

    def read_excel(self):
        self.data = xlrd.open_workbook(self.path)
        self.table = self.data.sheet_by_index(0)
        pass

    def process_excel(self):
        pass

    def write_excel(self):
        pass