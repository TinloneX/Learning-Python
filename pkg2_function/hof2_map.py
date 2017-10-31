#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（2）
# map / reduce
from functools import reduce


def n2(x, n=2):
    return x ** n


def n3(x, n):
    return n * x


L = [1, 2, 3, 4, 5, 6]
a = map(n2, L)  # 将L中元素依次传入n2中生成新的可迭代对象
print(a)
print(list(a))

b = reduce(n3, L)  # 将L中元素每两个传入n3中计算并累加为新值
print(b)


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def chartonum(o):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }[o]

    return reduce(fn, map(chartonum, s))


c = str2int('1231')
print(c)


# lambda 简化步骤
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }[s]


def str_int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


d = str_int('666')
print(d)


def uper(s):
    st = str(s)
    return st.replace(st[0], st[0].upper(), 1)


L2 = ['make', 'amada', 'alpha']
print(uper("sada"))
print(list(map(uper, L2)))

i = input('输入你的英文名字：')
print(uper(i))


def prod(ln):
    def fx(x, y):
        return x * y

    return reduce(fx, list(ln))


Lx = [1, 2, 3, 4, 5]
print(prod(Lx))


def str2float(s):
    l = str(s).split('.')
    if len(l) == 1:
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    else:
        return reduce(lambda x, y: x * 10 + y, map(char2num, l[0])) + reduce(lambda x, y: x * 10 + y,
                                                                             map(char2num, l[1])) / 10 ** len(l[1])


print(str2float('12.01'))
