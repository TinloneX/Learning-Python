#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高阶函数篇（3）
# filter  / sort


def is_odd(n):
    return n % 2 == 1


l1 = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(l1)


def not_empty(s):
    return s and s.strip()


l2 = list(filter(not_empty, ['Alex', '', 'Bob', None, 'Cate']))
print(l2)


def _odd_iter():
    s = 1
    while True:
        s = s + 2
        yield s


def _not_divisible(o):
    return lambda x: x % o > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for i in primes():
    if i < 10:
        print(i)
    else:
        break

# -----------------------sort------------------------
L1 = [36, 5, -12, 9, -21]
print(sorted(L1))
print(sorted(L1, key=abs))
L2 = ['Alex', 'Bob', 'baby', 'cat', 'Devid']
print(sorted(L2))
print(sorted(L2, key=str.lower))
print(sorted(L2, key=str.lower, reverse=True))


def key1(t):
    return t[0]


def key2(t):
    return t[1]


L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L3, key=key1))
print(sorted(L3, key=key2))
