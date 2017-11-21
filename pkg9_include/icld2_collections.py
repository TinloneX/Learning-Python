#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(2)
# collections

# 快速打印
from util import p
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# ----- namedtuple
Point = namedtuple('Point', ['x', 'y'])  # 定义长度为二不可变的tuple
p1 = Point(1, 2)  # 创建对象
p('p1 = %s, p1.x = %s, p1.y = %s' % (p1, p1.x, p1.y))  # namedtuple允许使用属性访问元素
p('p1 is Point ?', isinstance(p1, Point))  # 验证类型1
p('p1 is tuple ?', isinstance(p1, tuple))  # 验证类型tuple

# ----- deque  双向列表
dq = deque(['a', 'b', 'c'])
dq.append('x')  # 后添加
dq.appendleft('0')  # 前添加
p(dq)
dq.pop()  # 后移除
p(dq)
dq.popleft()  # 前移除
p(dq)

# ----- defaultdict
dd = defaultdict(lambda: 'N/A')  # 定义若key不存在，调用函数返回默认值
dd['key1'] = 'abc'  # 新增k = key1, v = abc
p(dd['key1'])
p(dd['key2'])  # 无此key，返回默认值

# ----- OrderedDict
d = dict([('a', 1), ('o', 2), ('c', 3)])
p(d)  # 默认无序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
p(od)  # 有序（插入顺序）


# -- 使用OrderedDict实现一个先进先出的dict


class FIFOdict(OrderedDict):
    def __init__(self, capatity):
        super(FIFOdict, self).__init__()
        self._capatity = capatity  # 定义数量阀

    def __setitem__(self, key, value):
        contains = 1 if key in self else 0  # 若key存在则contains = 1，否则0
        if len(self) - contains >= self._capatity:  # 若key不存在且容量将大于数量阀
            last = self.popitem(last=False)  # 移除item
            p('remove:', last)
        if contains:  # 若1（True）
            del self[key]  # 移除[key]代表的原值引用
            p('set:', (key, value))
        else:  # 否0（False）
            p('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)  # 调用父类，有序添加键值对


# ----- Counter
c = Counter()
for ch in 'programming':  # 遍历字符
    c[ch] = c[ch] + 1  # 字符计数
p(c)  # 输出计数dict，（带序）数量+出现先后


