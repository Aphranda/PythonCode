import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patchM
from matplotlib.animation import FuncAnimation  # 动图的核心函数
import seaborn as sns  # 美化图形的一个绘图包

class FiberArray(object):
    def __init__(self):
        self.fig = plt.gca()
    

    def base_core(self):
        try:
            self.offset = int(input("请输入位置偏移量："))
            self.rotation = int(input("请输入旋转偏移量："))
        except Exception as e:
            print(e)
            self.base_core()

    def static_module(self):
        rect_XY = np.array([0, 0])

        circle_XY = [
            np.array([175, 175]),
            np.array([429, 175]),
            np.array([683, 175]),
            np.array([937, 175]),
            np.array([1191, 175]),
            np.array([1445, 175]),
            np.array([1699, 175]),
            np.array([1953, 175]),
        ]

        rect = patchM.Rectangle(rect_XY, 2128, 350, facecolor="cyan",  edgecolor="darkcyan", alpha=0.5)
        self.fig.add_patch(rect)
        for i in circle_XY:
            circle_01 = patchM.Circle(i, 125, color="c", alpha=0.5)
            circle_02 = patchM.Circle(i, 9, color="yellow", alpha=0.8)
            self.fig.add_patch(circle_01)
            self.fig.add_patch(circle_02)





def main():
    fiber = FiberArray()
    fiber.base_core()
    fiber.static_module()
    plt.axis('equal')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()
