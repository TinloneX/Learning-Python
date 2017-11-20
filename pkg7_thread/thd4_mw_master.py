#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 多进程和多线程(4)
# 分布式进程 （主进程master）

# 快速打印
from util import p
import random
# import time
import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def tq():
    return task_queue


def rq():
    return result_queue


if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=tq)
    QueueManager.register('get_result_queue', callable=rq)
    #  绑定端口5000，设置验证码为‘thd4’
    manager = QueueManager(address=('127.0.0.1', 5230), authkey=b'thd4')
    manager.start()
    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        p('Put task %d...' % n)
        task.put(n)

    p('---- try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        p('Result:%s' % r)

    manager.shutdown()
    p('master exit.')
