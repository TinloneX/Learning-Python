#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
class p(object):
    def __init__(self, *args, **kw):  # 恭喜你创建了一个p对象
        print(*args, **kw)  # 打印
        del self  # p对象过于劳累自杀了。。。
