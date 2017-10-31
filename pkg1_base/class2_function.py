#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 函数篇
PI = 3.14159265359


def area_circle(r):
    radius = int(r)
    if radius >= 0:
        return PI * radius ** 2  # 同 PI * radius * radius
    else:
        return -1


def power(x):
    return x ** 2


def power(x, n):  # 并不存在java中狭义的方法重载，同名方法会被覆盖
    return x ** n


def power2(x, n=2):  # n=2 为默认参数的写法，即若只传 x ，则 n 默认为2
    return x ** n


def appd(L=[]):  # 默认参数为可变对象时，调用默认参数函数前会先将返回值计算并存储好，多次调用默认参数时，默认参数会变为上次使用默认参数时产生的值
    L.append('END')
    return L


def appdr(L=None):  # 解决上一方法出现的问题
    if L is None:
        L = []
    L.append('END')
    return L


def enroll(name, gender, age=6, city='beijing'):
    print("name = %s,gender = %s, age = %s, city = %s" % (name, gender, age, city))
    return


print(area_circle(6))
# print power(3) 会报错
#  File "F:/pythonDemo/test1/pkg1_base/class2_function.py", line 38, in <module>
#    print power(3)
# TypeError: power() takes exactly 2 arguments (1 given)
print(power(5, 3))
print(power2(3))
print(power2(5, 3))
print(appd())
print(appd())
print(appdr())
print(appdr())
enroll('张散', '男')
enroll('李思', '女', 7)
enroll('王舞', '女', city='tianjin')

# -----可变参函数------------------------------------------
A = [1, 2, 3, 5]


def addx(*numbers):  # 表示numbers 代表一个数组 ，*numbers 代表复制集合中所有元素作为一个元组tuple
    sumx = 0
    for num in numbers:
        sumx += num
    return sumx


def person(name, age, **kw):
    print('name:%s, age:%s, other:%s' % (name, age, kw))


def pmore(name, age, *, city='dali', job):
    person(name, age)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(addx(1, 2, 3))
print(addx(*A))  # *A代表复制集合中所有元素传入可变参函数
person("陈奇", 28)
person('赵柳', 20, city='wuhan')
dicc = {'city': 'jingzhou', 'job': 'Engineer'}
person('钱起', 25, **dicc)
pmore("tiny", 25, job='dancer')
print(fact(5))
