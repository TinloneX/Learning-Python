#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用第三方模块(3)
# chardet 检测编码 (pip install chardet)

# 快速打印
from util import p
import chardet

p(chardet.detect(b'Hello,World!'))
gbk1 = '离离原上草，室内赛'.encode('gbk')
p(chardet.detect(gbk1))
utf1 = '离离原上草'.encode('utf-8')
p(chardet.detect(utf1))
jpn1 = 'おかしな話だ'.encode('euc-jp')
p(chardet.detect(jpn1))


