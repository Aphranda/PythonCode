import PIL
import os


class image_porcess(object):
    def read_picture(self):
        """读取图片"""
        path = r'E:\beauty\19120467'
        file_list = os.listdir(path)
        print(file_list)

    def corp_picture(self):
        """裁剪图片"""
        pass

    def process_picture(self):
        """处理图片,输出矩阵"""
        pass

    def compare_picture(self):
        """比较矩阵，输出结果"""
        pass

    def result_store(self):
        """结果储存"""
        pass

if __name__ == '__main__':
    pass
