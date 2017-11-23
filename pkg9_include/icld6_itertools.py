#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(6)
# itertools

# 快速打印
from util import p
import itertools
from functools import reduce

cut = itertools.count(1)  # count(）会创建一个无限迭代器
for n in cut:
    p(n)
    if n >= 3:  # 此处限制了迭代次数
        break

cyc = itertools.cycle('ab')  # cycle()会把传入的一个序列无限重复下去
for c in cyc:
    p(c)
    if c == 'b':  # 此处限制了迭代次数
        break

# ----- repeat() 负责把一个元素无限重复下去
rpt = itertools.repeat('a', 2)
# 若不提供限定重复次数（此处2）则无限重复
for r in rpt:
    p(r)

# ----- takewhile() 根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x: x <= 10, cut)
p(list(ns))  # 此处，cut迭代器先前已迭代至3，故自4起生成集合

# ----- chain() 将一组迭代对象串联起来，形成一个更大的迭代器
for ch in itertools.chain('abc', 'ok'):
    p(ch)

# ----- groupby() groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AABBBabb'):
    p(key, list(group))

# 挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key
for key, group in itertools.groupby('AaBbBaA', lambda c: c.upper()):
    p(key, list(group))


def pi(n):  # 计算近似PI值
    L = [x for x in range(1, 2 * n - 1, 2)]
    i = 0
    for pr in itertools.cycle((4, -4)):
        if i < len(L):
            L[i] = pr / L[i]
            i = i + 1
        else:
            break
    return reduce(lambda x, y: x + y, L)


p(pi(10000))  # 建议数值不要超过10**7
