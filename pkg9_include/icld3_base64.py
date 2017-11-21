#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(3)
# base64

# 快速打印
from util import p
import base64

# --- b64encode / b64decode
b1 = base64.b64encode(b'binary\x00string')
p('字符转base64', b1)
d1 = base64.b64decode(b1)
p('base64转字符', d1)

# --- urlsafe_b64encode
b2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
p('含+/的二进制数据b64', b2)
ub = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
p('含+/的urlsafe转b64', ub)
ud = base64.urlsafe_b64decode(ub)


def b64_eq_decode(s):  # 解析某种（去掉base64编码补位'='的）编码的算法
    ls = len(s)  # 获取长度待用，一般来说需要验证是否为0，此处未做
    if not ls % 4 == 0:  # 长度不能被4整除
        for x in range(4 - ls % 4):  # 计算需补位数
            s = s + b'='  # 遍历补位，此处为 b'='
    st = base64.b64decode(s)  # 解码
    p(st)  # 输出验证
    return st


# 验证有'='及去掉'='的解码结果
bo = b64_eq_decode(b'YWJjZA==') == b64_eq_decode(b'YWJjZA')
p(bo)

