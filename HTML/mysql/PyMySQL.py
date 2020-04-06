from pymysql import *
import sys
import os


def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)


class JD(object):
    def __init__(self):
        self.con = connect(
            host='localhost', port=3306, user='root', password='password', database='jing_dong', charset='utf8'
        )
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def roll_back(self):
        self.con.rollback()

    def com_mit(self):
        self.con.commit()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for item in data:
            print(item)

    def insert_sql(self, sql):
        self.cursor.execute(sql)

    def show_all_goods(self):
        sql = "select * from goods"
        self.execute_sql(sql)

    def show_group(self):
        sql = "select name from goods_cates"
        self.execute_sql(sql)

    def show_brand_group(self):
        sql = "select name from goods_brands"
        self.execute_sql(sql)

    def add_brand_group(self):
        brand_name = input("输入新商品分类名称")
        sql = "insert into goods_cates (name) values ('%s')" % brand_name
        self.insert_sql(sql)

    @staticmethod
    def show_menu():
        print(
            """
            -------可查询项目-------
            0.退出界面
            1.查询所有的信息数据
            2.查询所有的分类数据
            3.查询所有的品牌分类
            4.增加商品分类 
           """
        )
        return input("请输入查询项目：")

    def look(self):
        while True:
            question = self.show_menu()
            if question[0] == "1":
                self.show_all_goods()
            elif question[0] == "2":
                self.show_group()
            elif question[0] == "3":
                self.show_brand_group()
            elif question[0] == '4':
                self.add_brand_group()
                res = input("确认输入1，取消输入0")
                if res == "1":
                    self.com_mit()
                elif res == "0":
                    self.roll_back()
                else:
                    print("输入有误")
            elif question[0] == '0':
                break
            else:
                print("请输入正确项目")


def main():
    jd = JD()

    jd.look()


if __name__ == '__main__':
    main()