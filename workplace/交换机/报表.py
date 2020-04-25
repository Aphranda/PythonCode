



class Table(object):
    def __init__(self, order):
        self.people = {
            "1": "郭武荣",
            "2": "贺帅",
            "3": "李观豪",
            "4": "李琳",
            "5": "罗荣华",
            "6": "朱红卫",
            "7": "王先琴",
            "8": "李秋云",
            "9": "吴国军",
            "10": "徐记波",
            "11": "王艳",
            "12": "覃开贵",
            "13": "贾春红"
        }
        self.process = {
            "1": "点胶测试",
            "2": "组装工位",
            "3": "点位套胶",
            "4": "高温测试",
            "5": "交换机",
            "6": "包装工位"
        }
        self.order = []
        self.all_num = []
        self.all_time = []
        self.lose_time = []

    def order_input(self):
        while True:
            print("输入 '0' 退出单号输入")
            order_id = input("请输入订单号：")
            if order_id == "0":
                break
            self.order.append(order_id)
        while True:
            
