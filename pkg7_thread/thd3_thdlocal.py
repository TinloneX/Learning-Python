#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 多进程和多线程(3)
# ThreadLocal

# 快速打印
from util import p
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    std = local_school.student
    p('Hello,%s (in %s)' % (std, threading.current_thread().name))


def run(name):
    local_school.student = name
    process_student()


def test_local():
    t1 = threading.Thread(target=run, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=run, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    test_local()

