import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patchM
import random
from matplotlib.animation import FuncAnimation  # 动图的核心函数
import seaborn as sns  # 美化图形的一个绘图包

class FiberArray(object):
    def __init__(self):
        pass

    def inition(self):
        self.fig = plt.subplot()
    

    def base_core(self):
        try:
            self.offset = int(input("请输入位置偏移量："))
            self.rotation = int(input("请输入旋转偏移量："))
        except Exception as e:
            print(e)
            self.base_core()

    def static_module(self):
        rect_XY = np.array([0, 0])
        rect = patchM.Rectangle(rect_XY, 2128, 350, facecolor="cyan",  edgecolor="darkcyan", alpha=0.5)
        self.fig.add_patch(rect)

        circle_XY_01 = [
            np.array([175, 175]), np.array([429, 175]), np.array([683, 175]), np.array([937, 175]),
            np.array([1191, 175]), np.array([1445, 175]), np.array([1699, 175]), np.array([1953, 175]),
        ]
        circle_XY_02 = [
            np.array([171.5, 175]), np.array([425.5, 175]), np.array([679.5, 175]), np.array([933.5, 175]),
            np.array([1187.5, 175]), np.array([1441.5, 175]), np.array([1695.5, 175]), np.array([1949.5, 175]),
        ]
        circle_XY_03 = [
            np.array([175, 171.5]), np.array([429, 171.5]), np.array([683, 171.5]), np.array([937, 171.5]),
            np.array([1191, 171.5]), np.array([1445, 171.5]), np.array([1699, 171.5]), np.array([1953, 171.5]),
        ]
        circle_XY_04 = [
            np.array([171.5, 171.5]), np.array([425.5, 171.5]), np.array([679.5, 171.5]), np.array([933.5, 171.5]),
            np.array([1187.5, 171.5]), np.array([1441.5, 171.5]), np.array([1695.5, 171.5]), np.array([1949.5, 171.5]),
        ]

        circle = [circle_XY_01, circle_XY_02, circle_XY_03, circle_XY_04]
        
        for i in circle_XY_04:
            rect_circle = patchM.Rectangle(i, 7, 7, color="b", alpha=0.5)
            self.fig.add_patch(rect_circle)
        
    def rotation_fuc(self, circle):
        X = circle[0]*np.cos(self.rotation*np.pi/180) + circle[1]*np.sin(self.rotation*np.pi/180) 
        Y = -circle[0]*np.sin(self.rotation*np.pi/180) + circle[1]*np.cos(self.rotation*np.pi/180)
        return [X, Y]

    def move_data(self, circle):
        random_X = random.randint(-self.offset, self.offset)
        random_Y = random.randint(-self.offset, self.offset)

        rectangle = [random_X + 1064*(1-np.cos(self.rotation*np.pi/180)), random_Y + 1064*np.sin(self.rotation*np.pi/180)]

        circles = []

        circle_XY = [
            [175, 175], [429, 175], [683, 175], [937, 175], [1191, 175], [1445, 175], [1699, 175], [1953, 175]
        ]
        for i in circle_XY:
            circles.append(np.array([
                self.rotation_fuc(i)[0]+ circle[0] + random_X + 1064*(1-np.cos(self.rotation*np.pi/180)), 
                self.rotation_fuc(i)[1] + circle[0] + random_Y + 1064*np.sin(self.rotation*np.pi/180)
                ]))
        print(circles)
        rect = patchM.Rectangle(rectangle, 2128, 350, facecolor="red", edgecolor="darkred", angle=-self.rotation, alpha=0.3)
        self.fig.add_patch(rect)
        for i in circles:
            circle_01 = patchM.Circle(i, 125, color="navy", alpha=0.2)
            circle_02 = patchM.Circle(i, 4.5, color="m", alpha=0.2)
            self.fig.add_patch(circle_01)
            self.fig.add_patch(circle_02)
 

def main():
    fiber = FiberArray()
    fiber.inition()

    fiber.base_core()
    fiber.static_module()

    circle = [0,0]
    fiber.move_data(circle)
    plt.axis('equal')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()
