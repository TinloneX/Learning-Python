#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（4）
# 返回函数（函数作为返回值）/ 匿名函数lambda


def lz_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s

    return sum


f1 = lz_sum(1, 2, 3, 4, 5, 6)
f2 = lz_sum(1, 2, 3, 4, 5, 6)
print(f1)
print('sum =', f1())
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f4, f5, f6 = count2()
print(f4(), f5(), f6())

# --------------------lambda---------------------
l1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(l1)

fx = lambda x: x * x
print(fx(5))


def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2)())
