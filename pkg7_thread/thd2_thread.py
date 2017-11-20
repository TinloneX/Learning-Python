#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 多进程和多线程(2)
# 多线程 （threading）

# 快速打印
from util import p
import time
import threading


def loop():
    p('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        p('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(n)
    p('thread %s ended.' % threading.current_thread().name)


def test_th():
    p('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    p('thread %s ended.' % threading.current_thread().name)


# ----- lock -----
balance = 0
lock = threading.Lock()


def change(n):
    global balance
    balance = balance + n
    balance = balance - n


def run(n):
    for i in range(1000000):
        change(n)


def run_lock(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


def test_lock():
    # t1 = threading.Thread(target=run, args=(5,))
    t1 = threading.Thread(target=run_lock, args=(5,))
    # t2 = threading.Thread(target=run, args=(8,))
    t2 = threading.Thread(target=run_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    p(balance)


if __name__ == '__main__':
    test_th()
    test_lock()
    # 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
    # Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
