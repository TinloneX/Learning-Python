#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
class p(object):
    def __init__(self, *args, **kw):
        print(*args, **kw)
        del self
