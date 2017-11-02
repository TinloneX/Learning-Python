#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（9）
# 枚举 (enumerate)

# 快速打印
from util import p
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def test_enum():
    for name, member in Month.__members__.items():
        p(name, '=>', member, ',', member.value)
    day1 = Weekday.Sun
    p(day1)  # Weekday.Sun
    p(day1 == Weekday(0))  # True
    p(Weekday(6))  # Weekday.Sat
    p(Weekday['Tue'])  # Weekday.Tue
    p(Weekday['Tue'].value)  # 2


if __name__ == '__main__':
    test_enum()
