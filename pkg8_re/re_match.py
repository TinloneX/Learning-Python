#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 正则表达式
# re模块

# 快速打印
from util import p
import re

m1 = re.match(r'^\d{3}-\d{3,8}$', '010-123456')
p(m1)

inp = input('请输入Email: ')
if re.match(r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+.com(.cn)?$', inp):
    p('it`s OK')
else:
    p('it`s not good')

# -------- 切分字符串 split
s = 'a b  c'
s2 = 'a, b,c  d'
p(s.split(' '))
p(re.split(r'\s+', s))
p(re.split(r'[\s,]+', s2))

# -------- 分组(group)
iqq = input('请输入QQ Email: ')
m = re.match(r'^([0-9]{6,11})@(qq.com)$', iqq)
if m:
    p('QQ:', m.group(1))
else:
    p('not qq email')

t = '19:05:30'
rt = '^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
mt = re.match(rt, t)
p('不匹配？', mt is None)

# -------- 贪婪匹配

n1 = re.match(r'^(\d+)(0*)$', '10230000').groups()
p(n1)
n2 = re.match(r'^(\d+?)(0*)$', '10230000').groups()
p(n2)

# -------- （预）编译

re_email = re.compile(r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+.com(.cn)?$')

A1 = '123@345.com'
A2 = '123@345.com.cn'
A3 = 'q123@.com'
A4 = 'q123@.345.com'
p(re_email.match(A1) is None)
p(re_email.match(A2) is None)
p(re_email.match(A3) is None)
p(re_email.match(A4) is None)
