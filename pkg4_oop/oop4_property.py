#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（4）
# 实例属性（对象调用变量）与类属性（类似java静态变量）
from util import p


class Circle(object):
    PI = 3.14  # 默认视作常量（static final）       代表圆周率
    perc = 0.5  # 定义一个常规可变类属性（static）       代表比例

    def __init__(self, radius):  # radius 半径
        self.radius = radius  # 定义一个实例属性

    def area(self):
        return self.perc * self.PI * (self.radius ** 2)  # 对应比例圆面积

    def area2(self):
        return Circle.perc * Circle.PI * (self.radius ** 2)


def __test():
    c1 = Circle(2)  # 定义一个半径为2的圆
    p(c1.area())  # 打印0.5个半径为2的圆的面积   6.28
    Circle.perc = 1  # 类直接访问并更改perc属性，设置比例为1
    p(c1.area())  # 打印1个半径为2的圆的面积   12.56
    p(c1.perc)  # 通过实例访问类属性
    c1.perc = 2  # 使用实例访问并更改类属性
    p(c1.area())  # 打印2个半径为2的圆面积    25.12
    c2 = Circle(2)  # 新定义一个半径为2的圆
    p(c2.area())  # 12.56  此处值与预想中的25.12不一样，故可判断在通过实例改变类属性时，实际并未改变类属性的值，
    # 仅是在该实例中创建了一个名称相同的新变量，在后续计算中使用的是新值，这个新值仅在当前对象中，类属性本身还是1，
    # 新建实例中perc值依旧是通过类直接改变生效的值（1），故此处计算值为12.56
    print(c1.area2())  # 12.56
    c1.perc = 2
    print(c1.area2())  # 12.56  # 故证实实例仅可访问类对象并不能真正更改类属性


if __name__ == '__main__':  # 仅本类测试执行
    __test()
