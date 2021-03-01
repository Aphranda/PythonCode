import configparser
from ErrorConfiguration import Logits
Logits = Logits()


class Configuration(object):
    def __init__(self):
        self.config = configparser.ConfigParser()

    def check_section(self, value):
        try:
            result = self.config.has_section(value[1])
            return result
        except Exception as e:
            print(e)

    def add_section(self, value):
        try:
            self.config.read(f"{value[0]}.ini", encoding="gbk")
            if self.check_section(value):
                receive = f"[{value[1]}]已经存在，请更换名称"
            else:
                self.config.add_section(f"{value[1]}")
                for i in value[2]:
                    self.config.set(value[1], i, value[2][i])
                receive = f"[{value[1]}]已经添加进入配置"
            self.write_config(value)
            return receive
        except Exception as e:
            print(e)

    def delete_section(self, value):
        try:
            self.config.read(f"{value[0]}.ini", encoding="gbk")
            self.config.remove_section(value[1])
            receive = f"[{value[1]}]已经删除"
            self.write_config(value)
            return receive
        except Exception as e:
            print(e)

    def modify_section(self, value):
        try:
            self.config.read(f"{value[0]}.ini", encoding="gbk")
            if self.check_section(value):
                for i in value[2]:
                    self.config.set(value[1], i, value[2][i])
                receive = f"[{value[1]}]修改完成"
            else:
                receive = f"[{value[1]}]不存在，请更换配置名称"
            self.write_config(value)
            return receive
        except Exception as e:
            print(e)

    def count_section(self, value):
        try:
            receive = {}
            self.config.read(f"{value}.ini", encoding="gbk")
            data = self.config.sections()
            for i in data:
                options = self.config.items(i)
                receive[i] = options
            return receive 
        except Exception as e:
            print(e)

    def search_option(self, value, section):
        try:
            self.config.read(f"{value}.ini", encoding="gbk")
            data = self.config.items(section)
            return data
        except Exception as e:
            print(e)

    def write_config(self, value):
        try:
            self.config.write(open(f"{value[0]}.ini", "w"))
        except Exception as e:
            print(e)

# def main():
#     data = ["111", "section", {"item01":"123", "item02":"456"}]
#     data01 = ["111", "section", {"item01":"1", "item02":"4"}]
#     con = Configuration()
#     con.add_section(data)

# if __name__ == "__main__":
#     main()
