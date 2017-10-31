#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（1）

a = abs(-10)
b = abs
c = b(-5)
print('a = %s, b = %s, c = %s' % (a, b, c))

# 函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 注：不要给已有python内建函数重新赋值，否则程序运行期间函数将已新值计算
# 注2：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10

# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


def add(x, y, f):
    return f(x) + f(y)


a = add(-10, 5, abs)  # 将求模函数传入add方法中
print(a)  # 15
