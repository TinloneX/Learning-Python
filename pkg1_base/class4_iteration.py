#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高级特性篇(2)
# 迭代（Iteration）     /       列表生成式

# for in 不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
# 此处迭代与Java中的迭代器不同，与fori、for-each类似

# 导包 3.7+版本推荐使用collections.abc
from collections.abc import Iterable
import os

# for in 遍历list 或 tuple  (均有下标)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
T = (96, 82, 88, 92, 80)

for name in L:
    print(name)

for score in T:
    print(score)

# for in 遍历字典 （java中的Map,无下标）
D = {'Michael': 96, 'Sarah': 82, 'Tracy': 88, 'Bob': 92, 'Jack': 80}

for key in D:  # 仅会遍历key
    print(key)

for value in D.values():  # 仅会遍历value
    print(value)

for k, v in D.items():  # 遍历键值对并对应 k,v
    print('%s的分数：%s' % (k, v))

# for in 遍历字符串
S = 'ABCD'

for char in S:  # char 并非保留字
    print(char)

# 判断一个对象是否是可迭代对象
print('字符串是否为可迭代对象:%s' % isinstance(S, Iterable))
print('元组是否为可迭代对象:%s' % isinstance(T, Iterable))
print('整数是否为可迭代对象:%s' % isinstance(1234, Iterable))

# 像Java一样使用索引遍历list 或 tuple
for i, value in enumerate(L):
    print(i, value)

# 扩展
LT = [(0, 0), (1, 1), (2, 2)]
LT2 = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]

for x in LT:
    print(x)  # 直接打印元组   (0, 0)

for x, y in LT:
    print(x, y)  # 打印元组内元素   0 0

for x, y, z in LT2:  # 尝试仅使用 x，y遍历会报错，使用此方法遍历需要变量数与内部嵌套的元素个数一致
    print(x, y, z)


# --------------------------------列表生成式--------------------------------
# 小写转换（判别是否为字符串）
def low(s):
    if isinstance(s, str):
        return s.lower()
    else:
        return s


print(list(range(10)))
print(list(range(1, 10)))
# 从1到9 生成平方 集合
print([x * x for x in range(1, 10)])
# 从1到9 生成偶数平方 集合
print([x * x for x in range(1, 10) if x % 2 == 0])
# 双层循环
print([m + n for m in 'ABC' for n in 'abc'])
# 以本目录下文件名生成集合
print([d for d in os.listdir('.')])
# 同时迭代多变量
print([k + ':' + str(v) for k, v in D.items()])  # '+'拼接字符串两端仅能使str类型，若为数字会报错，故使用str()转换
# 将集合字符转换为全小写
print([s.lower() for s in L])  # 如果list中既包含字符串又包含整数，非字符串类型没有lower()方法，列表生成式会报错
# 筛选符合型元素输出
Ln = ['Avas', 'AAcsa', 12, 'Adfs', None]
print([s.lower() for s in Ln if isinstance(s, str)])
# 保持元素型输出(仅对字符串执行小写，其余原样输出)
print([low(s) for s in Ln])
