import os


class File(object):
    def __init__(self):
        pass

    def create_file(self, path):
        """创建文件夹"""
        if not os.path.exists(path):
            os.mkdir(path)
  
    def back_file(self):
        """返回工作目录"""
        return os.getcwd()

    