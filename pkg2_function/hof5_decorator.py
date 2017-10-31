#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（5）
# Decorator
import time
import functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log
def now():
    print(time.strftime('%Y-%m-%d %A', time.localtime(time.time())))


@log2('a-execute')
def now2(n):
    print(n, time.strftime('%Y-%m-%d %A', time.localtime(time.time())))


now()
now2('Today is')
print(now.__name__)  # now 的名称变为wrapper，因为执行时实际返回的函数是wrapper
print(now2.__name__)


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return (func(*args, **kw), print('end call'))[0]

    return wrapper


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3
def now3():
    print(time.strftime('%Y-%m-%d %A', time.localtime(time.time())))


@log4('test')
def now4():
    print(time.strftime('%Y-%m-%d %A', time.localtime(time.time())))


now3()
now4()
print(now3.__name__)  # 使用@functools.wraps(func) 将log中wrapper函数签名替换为原函数签名
