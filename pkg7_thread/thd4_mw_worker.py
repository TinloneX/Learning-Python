#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 多进程和多线程(4)
# 分布式进程 （工作进程worker）

# 快速打印
from util import p
import time
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接master服务器，此处为本机IP
SERVER_ADDR = '127.0.0.1'
p('Connect to server %s...' % SERVER_ADDR)
# 端口和验证码注意保持与master的端口及验证码一致
m = QueueManager(address=(SERVER_ADDR, 5230), authkey=b'thd4')
# 从网络链接
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        p('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        p('task queue is empty.')

p('worker exit.')
