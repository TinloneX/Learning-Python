#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 错误调试测试（1）
# 错误（Exception）
# 快速打印
from util import p
import logging

try:
    r = 10 / 0
    p('result =', r)
except ZeroDivisionError as e:
    p('except :', e)
finally:
    p('finally')

try:
    re = 10 / 0
    p('result =', re)
except ZeroDivisionError as e:
    p('except :', e)

try:
    res = 10 / int('a')
    p('result:', res)
except ValueError as e:
    p('ValueError:', e)
except ZeroDivisionError as e:
    p('ZeroDivisionError:', e)

try:
    r = 10 / int('2')
    p('result:', r)
except ValueError as e:
    p('ValueError:', e)
except ZeroDivisionError as e:
    p('ZeroDivisionError:', e)
else:
    p('no error!')

try:
    resu = 10 / 0
    p(resu)
except ZeroDivisionError as e:
    logging.exception(e)

p('ZeroDivisionError end')


class E(ValueError):
    # 只有在必要的时候才定义我们自己的错误类型。
    # 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型
    pass


s = input('input int :')
try:
    i = int(s)
    p('result', i)
except ValueError as e:
    # raise E('he he he')
    p('error:9527', e)

# 思考，（PyCharm中）本文件代码多次执行，打印顺序不同，为什么~~
# 附： Python所有的错误都是从BaseException类派生的:
"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""
