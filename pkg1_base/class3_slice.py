#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高级特性篇(1)
# 切片（Slice）

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 切片取集合元素  --示例1                                --> 运行结果
print(L[0:3])  # 取前三位（含首不含尾）                 --> ['Michael', 'Sarah', 'Tracy']
print(L[:3])  # 取前三位，即若切片起始位置为0则可省略   --> ['Michael', 'Sarah', 'Tracy']
print(L[1:3])  # 取第1-3位                              --> ['Sarah', 'Tracy']
print(L[-2:])  # 取倒数后两位（-2 ，-1 ，不含0）        --> ['Bob', 'Jack']
print(L[-2:-1])  # 取倒数第2位                          --> ['Bob']
print(L[:])  # 复制所有元素                             --> ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

S = list(range(100))

# 切片取集合元素  --示例2
print(S[:10])  # 取前10位（第0-9位）                    --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(S[10:20])  # 取11-20位                            --> [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(S[:10:2])  # 前10位每隔1位取一个                  --> [0, 2, 4, 6, 8]
print(S[::5])  # 所有元素每隔4位取一个                  --> [0, 5, 10, 15, 20, ... 80, 85, 90, 95]

T = tuple(range(10))

# 切片取元组元素
print(T[:3])  # 取元组前三位                            --> (0, 1, 2)

St = 'AaBbCcDdEeFf'

# 切片取字符串元素
print(St[:3])  # 取出前三位                            --> AaB
print(St[::2])  # 自第0位起隔1位取一个（取大写字母）   --> ABCDEF
print(St[1::2])  # 自第1位起隔1位取一个（取小写字母）  --> abcdef
