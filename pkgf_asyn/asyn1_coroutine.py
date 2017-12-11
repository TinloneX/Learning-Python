#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
from util import p


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        p('[consumer] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        p('[producer] Producing %s...' % n)
        r = c.send(n)
        p('[producer] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
