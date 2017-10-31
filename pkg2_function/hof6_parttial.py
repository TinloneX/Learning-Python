#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（6）
# 偏函数（Partial function）
import functools


def int2(x):
    return int(x, base=2)


print(int('123'))  # 123
print(int('123', base=8))  # 83
print(int2('101'))  # 5

int3 = functools.partial(int, base=2)
print(int3('100001'))  # 33
print(int3('10001', base=4))  # 257
print(int3('100001'))  # 33

max1 = functools.partial(max, 10)
print(max1(1, 5, 7))  # 10
