#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高级特性篇(2)
# 迭代器（Iterator）

from collections.abc import Iterator

a = isinstance((x for x in range(10)), Iterator)  # 生成器是迭代器
print(a)  # True
b = isinstance([], Iterator)  # 集合不是迭代器
print(b)  # False
c = isinstance("abc", Iterator)  # 字符串不是迭代器
print(c)  # False

d = isinstance(iter([]), Iterator)  # 使用iter（）方法可使Iterable对象转换为Iterator
print(d)  # True
e = isinstance(iter('abc'), Iterator)
print(e)  #True
print(iter('abc'))  # 对象地址
print(next(iter('abc')))  # a