import pymssql
import _mssql
import decimal

decimal.__version__
_mssql.__version__

class MyServer(object):
    def __init__(self):
        self.con = pymssql.connect("192.168.0.100", "DL", "Dl", "OnlinePrint_MES")
        self.cur = self.con.cursor()


    def create_table(self, table):
        try:
            self.cur.execute(
                f"""CREATE TABLE LightInspection(
                    ID INT IDENTITY(1,1) PRIMARY KEY,
                    ProductionOrder varchar(25),
                    ProductionSN varchar(40),
                    ProductionPN varchar(40),
                    BranchSN varchar(40),
                    Polarity varchar(10),
                    LightCheckResult varchar(20),
                    LightCheckNum varchar(20),
                    Operator varchar(20),
                    Time varchar(30),
                    ProductionNum varchar(30),
                    ProductionItem varchar(10),
                    ProductionCore varchar(10),
                    PassInspectionOne bit default 0,
                    PassInspectionTwo bit default 0,
                    PassInspectionThree bit default 0,
                    PassINspectionFour bit default 0,
                    MacheineLocation varchar(20),
                    IsExist bit default 1)""")
            self.con.commit()
        except Exception as e:
            print(e)

 
    def add_data(self, value):
        try:
            self.cur.execute(f"""INSERT INTO LightInspection VALUES (
                '{value[0]}', '{value[1]}', '{value[2]}', '{value[3]}', '{value[4]}', '{value[5]}',
                '{value[6]}', '{value[7]}', '{value[8]}', '{value[9]}', '{value[10]}', '{value[11]}',
                '{value[12]}', '{value[13]}', '{value[14]}', '{value[15]}', '{value[16]}', 1)""")
            self.con.commit()
        except Exception as e:
            print(e)
    
    def delete_data(self, value):
        try:
            if len(value[0]) > 1:
                productionOrder = f"ProductionOrder='{value[0]}' AND"
            else:
                productionSN = ""

            if len(value[1]) > 1:
                productionSN = f"ProductionSN='{value[1]}' AND"
            else:
                productionSN = ""

            if len(value[2]) > 1:
                productionPN = f"ProductionPN='{value[2]}' AND"
            else:
                productionPN = ""

            if len(value[3]) > 1:
                operator = f"Operator='{value[3]}' AND"
            else:
                operator = ""

            if len(value[4]) > 1:
                lightCheckResult = f"LightCheckResult='{value[4]}' AND"
            else:
                lightCheckResult = ""

            if len(value[5]) > 1:
                lightCheckNum = f"LightCheckNum='{value[5]}' AND"
            else:
                lightCheckNum = ""
            
            if len(value[6]) > 1:
                time = f"Time LIKE'{value[6]}%' AND"
            else:
                time = ""
            self.cur.execute(
                f"UPDATE LightInspection set ISExist=0 where {productionOrder} {productionSN} {productionPN} {operator} {lightCheckResult} {lightCheckNum} {time} IsExist=1")
            self.con.commit()
        except Exception as e:
            print(e)

    def search_data(self, value):
        try:
            box = []
            if len(value[0]) > 1:
                productionOrder = f"ProductionOrder='{value[0]}' AND"
            else:
                productionOrder = ""

            if len(value[1]) > 1:
                productionSN = f"ProductionSN='{value[1]}' AND"
            else:
                productionSN = ""

            if len(value[2]) > 1:
                productionPN = f"ProductionPN='{value[2]}' AND"
            else:
                productionPN = ""

            if len(value[3]) > 1:
                operator = f"Operator='{value[3]}' AND"
            else:
                operator = ""

            if len(value[4]) > 1:
                lightCheckResult = f"LightCheckResult='{value[4]}' AND"
            else:
                lightCheckResult = ""

            if len(value[5]) > 1:
                lightCheckNum = f"LightCheckNum='{value[5]}' AND"
            else:
                lightCheckNum = ""
            
            if len(value[6]) > 1:
                time = f"Time LIKE'{value[6]}%' AND"
            else:
                time = ""

            self.cur.execute(
                f"SELECT * FROM LightInspection where {productionOrder} {productionSN} {productionPN} {operator} {lightCheckResult} {lightCheckNum} {time} IsExist=1")
            res = self.cur.fetchall()
            for i in res:
                print(i)
                box.append(i)
            return box
        except Exception as e:
            print(e)
      


def main():
    tree = MyServer()
    # tree.create_table("LightInspection")
    # tree.add_data(["SRCW2020101100", "2020101101", "1", "SRCW2020101100", "1-8", "1-1fail", "一次通光", "1", "2021-01-12 18:48:06", "4M 24F MTP/APC/PC", "12", "24","0", "0", "0", "0", "1"])
    tree.search_data(['SRCW2020101100', "", "", "", "", "", "2021-01-12"])
    # tree.delete_data(['SRCW2020101101', "", "", "", "", "", "2021-01-12"])
    # tree.delete_data("beta", 'SRCW2020101100')

 


if __name__ == '__main__':
    main()
