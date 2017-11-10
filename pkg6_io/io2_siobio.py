#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 I/O编程 （2）
# StringIO / BytesIO

# 快速打印
from util import p
from io import StringIO, BytesIO

# ------- StringIO -------
f = StringIO()
p('写入hello,结果：', f.write('hello,'))
p('写入world结果：', f.write('world'))
p('取出内容：', f.getvalue())

f2 = StringIO('Sometime\nSomewhere\nSomeone\nSomething\nNothing')
while True:
    s = f2.readline()
    if s == '':
        break
    p(s.strip())

# ------- BytesIO -------
b = BytesIO()
b.write('lalalala啦啦啦啦'.encode('utf-8'))
p(b.getvalue())

b2 = BytesIO(b'lalalala\xe5\x95\xa6\xe5\x95\xa6\xe5\x95\xa6\xe5\x95\xa6')
p(b2.read())
