class Tenty_four:
    def __init__(self, number: dict):
        self.result = {}
        self.number = number
        self.typeid = ['+', '-', '*', '/']
        self.basket_num = []
        self.basket_typ = []
        self.basket_new = []

    def digital(self):
        for i in self.number:
            for j in self.number:
                if j != i:
                    for m in self.number:
                        if m != i and m != j:
                            for n in self.number:
                                if n != i and n != j and n != m:
                                    a = [self.number[i], self.number[j], self.number[m], self.number[n]]
                                    self.basket_num.append(a)
        for item in self.basket_num:
            if item not in self.basket_new:
                self.basket_new.append(item)

    def operate(self):
        for i in self.typeid:
            for j in self.typeid:
                for k in self.typeid:
                    a = [i, j, k]
                    self.basket_typ.append(a)

    def bracket(self):
        k = ["(", ")"]
        for i in self.basket_new:
            for j in self.basket_typ:
                self.result = {
                    'A': "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(k[0], i[0], j[0], i[1], k[1], j[1], i[2], j[2], i[3]),
                    'B': "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(i[0], j[0], k[0], i[1], j[1], i[2], k[1], j[2], i[3]),
                    'C': "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(i[0], j[0], i[1], j[1], k[0], i[2], j[2], i[3], k[1]),
                    'D': "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(k[0], i[0], j[0], i[1], k[1], j[1], k[0], i[2], j[2], i[3], k[1]),
                    'E': "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(k[0], k[0], i[0], j[0], i[1], k[1], j[1], i[2], k[1], j[2], i[3]),
                    'F': "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(k[0], i[0], j[0], k[0], i[1], j[1], i[2], k[1], k[1], j[2], i[3]),
                    'G': "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(i[0], j[0], k[0], k[0], i[1], j[1], i[2], k[1], j[2], i[3], k[1]),
                    'H': "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(i[0], j[0], k[0], i[1], j[1], k[0], i[2], j[2], i[3], k[1], k[1]),
                    'J': "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(k[0], i[0], j[0], i[1], j[1], i[2], k[1], j[2], i[3]),
                    'K': "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(i[0], j[0], k[0], i[1], j[1], i[2], j[2], i[3], k[1]),
                }
                n = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
                for a in n:
                    try:
                        eval(self.result[a])
                    except Exception as e:
                        pass
                    finally:
                        if eval(self.result[a]) == 24:
                            print(self.result[a])


if __name__ == "__main__":
    print('--从小到大输入或者从大到小输入--')
    a = input("请输入第一个数:")
    b = input("请输入第二个数:")
    c = input("请输入第三个数:")
    d = input("请输入第四个数:")
    number = {'A': a, 'B': b, 'C': c, 'D': d}
    start = Tenty_four(number)
    start.digital()
    start.operate()
    start.bracket()




