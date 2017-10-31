#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 模块 （1）
'模块--这里是文档注释'

__author__ = 'Tinlone'

import sys


def test():
    args = sys.argv  # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print('Hello,', args[0])
    elif len(args) == 2:
        print('Hello,', args[1])
    else:
        print('hello, Friend!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()


# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# 模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
