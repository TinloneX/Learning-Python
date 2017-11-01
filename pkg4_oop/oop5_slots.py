#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（5）
# 类增加属性 与 限制类增加属性

# 快速打印
from util import p
from types import MethodType


class Human(object):
    pass


def set_age(self, age):
    self.age = age
    p('age = %s' % age)


def where(self, point):
    self.point = point
    p('this is someone in %s' % point)


def stand(self, bol):  # 此处注意，无论self有无用到，都需要存在（可以不写作self），
    # 即给类绑定的方法至少要有一个参数，因为在类（实例）中方法的方法被调用时会默认传递一个self对象
    if bol:
        p('someone stand')
    else:
        p('someone not stand')


h1 = Human()
h1.gender = 'man'
p(hasattr(h1, 'gender'))  # h1 添加了gender属性
h2 = Human()
p(hasattr(h2, 'gender'))  # h2 并没有gender属性
h1.set_age = MethodType(set_age, h1)  # 为h1添加方法
h1.set_age(23)
Human.where = where  # 为类绑定方法
h2.where('China')  # 即使是已经创建的实例也可访问绑定的方法
# h2.stand(True)  # 不能使用没有绑定的方法，即使之后绑定了，这也是不符合逻辑的
Human.stand = stand
h1.stand(True)


# ---------------------------__slots__----------------------------


class Plant(object):
    __slots__ = ('name', 'color')


class Tree(Plant):
    pass


class Flower(Plant):
    __slots__ = ('where', 'when')


p1 = Plant()
p(dir(p1))  # Plant类中实际已包含color 及 name 属性，且不允许增加其他属性
t1 = Tree()
p(dir(t1))  # Tree类亦已包含color 及 name 属性，允许增加其他属性
t1.hight = 12
p(t1.hight)
f = Flower()
p(dir(f))  # Flower中已包含color、name、where及when，不允许增加其他属性

