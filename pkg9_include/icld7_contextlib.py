#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(7)
# contextlib

# 快速打印
from util import p
from contextlib import contextmanager, closing
from urllib.request import urlopen

# 使用with正确管理上下文对象
# 任何对象，只要正确实现了上下文管理，就可以用于with语句。


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        p('begin  --- __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            p('error, __exit__')
        else:
            p('end, __exit__ ')

    def query(self):
        p('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()


# -------------------- contextmanager


class Loox(object):  # 自身不重写enter和exit
    def __init__(self):
        self.task = []
        p('Loop prepare')

    def add_task(self, t):
        self.task.append(t)

    def loox(self):
        if len(self.task) >= 1:
            p('Loop loop task ', self.task[-1])


@contextmanager
def create_task(name):
    # @contextmanager这个decorator接受一个generator，
    # 用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
    p('prepare ...')
    lo = Loox()
    lo.add_task(name)
    yield lo
    p('end')


with create_task('task A') as ml:
    ml.loox()


@contextmanager
def tag(name):
    p("<%s>" % name)
    yield
    p("</%s>" % name)


with tag('h1'):
    p('hello,world')
    # 代码的执行顺序是：
    # with语句首先执行yield之前的语句，因此打印出<h1>；
    # yield调用会执行with语句内部的所有语句，因此打印出hello,world；
    # 最后执行yield之后的语句，打印出</h1>。

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        p(line)
