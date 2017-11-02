#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（8）
# 定制类 （重写基类object方法）

# 快速打印
from util import p


# ------------------(__str__ / __repr__)-----------------


class Cat(object):
    def __init__(self):
        pass


class Dog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s is a dog' % self.name

    __repr__ = __str__


def test_str():
    p(Cat())
    p(Dog('Lucky'))


# ------------------(__iter__)-----------------'


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a


def test_iter():
    for n in Fib():
        p(n)


# ------------------(__getitem__)-----------------


class FibItem(Fib):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


def test_getitem():
    f = FibItem()
    for x in range(10):
        p(f[x])


# ------------------(__getitem__ slice)-----------------
class FibSlice(Fib):
    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0:
                raise ValueError('Index must be slice or positive int')
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            if start < 0:
                raise ValueError('The slice Start_Index must be positive int (include zero)')
            stop = item.stop
            if stop < 0 or stop < start:
                raise ValueError('The slice End_Index must be > Start_Index')
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


def test_slice():
    s = FibSlice()
    p(s[0:5])


# ------------------(__getattr__)-----------------
class UrlChain(object):
    IP = 'http://apis.baidu.com'

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return UrlChain('%s/%s' % (self._path, item))

    def __str__(self):
        return '%s%s' % (self.IP, self._path)


def test_getattr():
    url = UrlChain().apistore.iplookup.iplookup_paid
    p(url)


# ------------------(__getattr__)-----------------
class Url2Chain(UrlChain):
    IP = 'https://github.com'

    def __call__(self, param):
        return Url2Chain('%s/%s' % (self._path, param))


def test_call():
    # https://github.com/TinloneX/Learning-Python
    url = Url2Chain()('TinloneX')('Learning-Python')
    p(url)


if __name__ == '__main__':
    p('# -------------(__str__ / __repr__)-------------')
    test_str()
    p('# ------------------(__iter__)-----------------')
    test_iter()
    p('# ------------------(__getitem__)-----------------')
    test_getitem()
    p('-----------------(__getitem__ slice)----------------')
    test_slice()
    p('-----------------(__getattr__)----------------')
    test_getattr()
    p('-----------------(__call__)----------------')
    test_call()
