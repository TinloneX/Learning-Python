#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（7）
# 多重继承 MaxIn (相比于java单继承多实现)

# 快速打印
from util import p


# Dog 狗 Bat 蝙蝠 Parrot 鹦鹉 Ostrich 鸵鸟
class Animal(object):  # java: 此处类可理解作--顶级父类Animal（动物）
    pass


class Runnable(object):  # java: 此处可理解作--接口：Runnable（可以跑的）
    pass                   # 实际上此处依旧是父类，以继承形式形成依赖关系


class Flyable(object):  # java: 此处可理解作--接口:Flyable（可以飞的）
    pass


class Mammal(Animal):  # java: 此处可理解作--父类--（哺乳动物）
    pass


class Bird(Animal):  # java: 此处可理解作--父类--（鸟类）
    pass


class Dog(Mammal, Runnable):  # java：Dog extends Mammal implements Runnable
    pass


class Bat(Mammal, Flyable):  #
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass
