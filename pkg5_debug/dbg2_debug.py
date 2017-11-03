#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 错误调试测试（2）
# 调试（debug）
# 快速打印
from util import p
import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    p(n)  # 用print()把可能有问题的变量打印出来
    return 10 / n


def aoo(a):
    z = int(a)
    assert z != 0, 'n is zero'
    return 10 / z


def boo(b):
    y = int(b)
    logging.info('int = %s' % b)
    print(10 / y)


def main():  # 建议将参数改为'0'，并在此加断点，尝试使用debug运行方式step into
    foo('1')
    aoo('1')
    boo('1')


if __name__ == '__main__':
    main()
