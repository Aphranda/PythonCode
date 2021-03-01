import sqlite3

class MyTree(object):
    def __init__(self, path):
        file_path = path + "\\" + "DataBase.db"
        con = sqlite3.connect(file_path)
        self.cur = con


    def create_table(self, table):
        try:
            self.cur.execute(
                f"""CREATE TABLE IF NOT EXISTS {table}(
                    ID INTEGER PRIMARY KEY NOT NULL, 
                    ProductionSN TEXT,
                    ProductionPN TEXT,
                    BranchSN TEXT,
                    Polarity TEXT,
                    LightCheckResult TEXT,
                    LightCheckNum TEXT,
                    Operator TEXT,
                    Time TEXT,
                    ProductionNum TEXT,
                    ProductionItem TEXT,
                    ProductionCore TEXT,
                    is_exist bit default 1)""")
            self.cur.commit()
        except Exception as e:
            print(e)

 
    def add_data(self, table, value):
        try:
            self.cur.execute(f"""INSERT INTO {table} VALUES (Null,
                '{value[0]}', '{value[1]}', '{value[2]}', '{value[3]}', '{value[4]}', '{value[5]}',
                '{value[6]}', '{value[7]}', '{value[8]}', '{value[9]}', '{value[10]}', 1)""")
            self.cur.commit()
        except Exception as e:
            print(e)
    
    def delete_data(self, table, value):
        try:
            if len(value[0]) > 1:
                productionSN = f"ProductionSN='{value[0]}' AND"
            else:
                productionSN = ""

            if len(value[1]) > 1:
                productionPN = f"ProductionPN='{value[1]}' AND"
            else:
                productionPN = ""

            if len(value[2]) > 1:
                operator = f"Operator='{value[2]}' AND"
            else:
                operator = ""

            if len(value[3]) > 1:
                lightCheckResult = f"LightCheckResult='{value[3]}' AND"
            else:
                lightCheckResult = ""

            if len(value[4]) > 1:
                lightCheckNum = f"LightCheckNum='{value[4]}' AND"
            else:
                lightCheckNum = ""
            
            if len(value[5]) > 1:
                time = f"Time LIKE'{value[5]}%' AND"
            else:
                time = ""
            self.cur.execute(
                f"UPDATE {table} set is_exist=0 where {productionSN} {productionPN} {operator} {lightCheckResult} {lightCheckNum} {time} is_exist=1")
            self.cur.commit()
        except Exception as e:
            print(e)

    def search_data(self, table, value):
        try:
            box = []
            if len(value[0]) > 1:
                productionSN = f"ProductionSN='{value[0]}' AND"
            else:
                productionSN = ""

            if len(value[1]) > 1:
                productionPN = f"ProductionPN='{value[1]}' AND"
            else:
                productionPN = ""

            if len(value[2]) > 1:
                operator = f"Operator='{value[2]}' AND"
            else:
                operator = ""

            if len(value[3]) > 1:
                lightCheckResult = f"LightCheckResult='{value[3]}' AND"
            else:
                lightCheckResult = ""

            if len(value[4]) > 1:
                lightCheckNum = f"LightCheckNum='{value[4]}' AND"
            else:
                lightCheckNum = ""
            
            if len(value[5]) > 1:
                time = f"Time LIKE'{value[5]}%' AND"
            else:
                time = ""
            res = self.cur.execute(
                f"SELECT * FROM {table} where {productionSN} {productionPN} {operator} {lightCheckResult} {lightCheckNum} {time} is_exist=1")
            for i in res:
                box.append(i)
            return box
        except Exception as e:
            print(e)
      


# def main():
#     tree = MyTree(r"D:\PythonCode\PythonCode\workplace\通光检验\Moudle")
#     tree.create_table("beta")
#     tree.add_data("beta", ["SRCW2020101100", "1", "SRCW2020101100", "1-8", "1-1fail", "一次通光", "1", "2021-01-12 18:48:06", "4M 24F MTP/APC/PC", "12", "24", 1])
#     tree.search_data("beta", ['SRCW2020101100', "", "", "", "", "2021-01-12"])
#     # tree.delete_data("beta", ['SRCW2020101100', "", "", "", "", "2021-01-12"])
#     # tree.delete_data("beta", 'SRCW2020101100')

 


# if __name__ == '__main__':
#     main()
