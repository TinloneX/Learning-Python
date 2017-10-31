#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 高级特性篇(2)
# 生成器（generator）

# 解决一次加载全部list浪费内存，使用生成器在循环的过程中不断推算出后续的元素
g = (x for x in range(100000))
print(g)
print(next(g))
for n in g:
    if n < 5:
        print(n)
    else:
        break


# 斐波拉契数列（Fibonacci）
def fib(m):
    s, a, b = 0, 0, 1
    while s < m:
        print(b)
        a, b = b, a + b  # 相当于t = (b, a + b)    a = t[0]    b = t[1]
        s = s + 1


# 生成长度为10的斐波拉契数列
fib(10)


# 斐波拉契数列（Fibonacci）
def fib2(m):
    s, a, b = 0, 0, 1
    while s < m:
        yield b  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        # 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
        # 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
        a, b = b, a + b  # 相当于t = (b, a + b)    a = t[0]    b = t[1]
        s = s + 1


gf = fib2(6)  # 类型为生成器
for x in gf:
    print(x)


def fib3(m):
    s, a, b = 0, 0, 1
    while s < m:
        yield b
        a, b = b, a + b  # 相当于t = (b, a + b)    a = t[0]    b = t[1]
        s = s + 1
    return 'dresult'  # 使用yield 的函数无法直接拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中


gf2 = fib3(3)
while True:
    try:
        x = next(gf2)
        print('g:', x)
    except StopIteration as e:
        print(e.value)
        break


# 设计实现杨辉三角(控制总阶数)（不安全）
def yh(step):
    result, temp, i, count = [1], [1], 0, 0  # 原始算法count从1起，为保证阶数与运算次数一致，更正为以0作为起始
    while count < step:  # 保证每阶运算执行
        yield result  # 设置运算起点
        while True:  # 保证循环，关循环由内部条件控制
            if i == count:  # 运算到最后一位，第n阶有n个元素
                temp.append(1)  # 保证第n为元素为1
                i = 0  # 循环标志清0
                result = temp  # 赋值保存
                temp = [1]  # 初始化 临时集合 ，并保证第一位为 1
                break
            else:
                # print('s',i,result[i])  # 调试查看当前元素
                # print(result[i-1])  # 调试查看上一元素-----错误，此在运算开始时系倒数第一个元素
                # print(result[i+1])  # 调试查看下一元素
                # 通过测试发现使用 集合1（上一元素+下一元素）系错误逻辑，应为 集合1（本位元素+下位元素）
                temp.insert(i + 1, result[i] + result[i + 1])
                # print(temp) 调试单步运算集合
                i += 1  # 运算标志+1，代表 第n阶的第 i 个元素
        count += 1  # 每阶运算完成后，count + 1


a = yh(7)  # 若使用next遍历超出后会报错，建议使用for in 循环
for w in a:
    print(w)


# 设计杨辉三角（无限运算）
def yhx():
    result = [1]
    while True:
        yield result
        # 算法解释：
        # 最后一位拼接0生成临时集合代表本位元素，并保证最后一位计算值为1
        # 第一位拼接0生成临时集合代表后位元素，并保证第一位计算值为1
        # i 自0 至 原集合长度+ 1，代表每阶长度增加1
        result = [(result + [0])[i] + ([0] + result)[i] for i in range(len(result) + 1)]


b = yhx()  # 若使用for in 循环遍历需注意为循环加阀，否则将无限制运算
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

