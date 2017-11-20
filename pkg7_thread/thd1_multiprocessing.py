#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 多进程和多线程(1)
# 多进程 （multiprocessing）

# 快速打印
import random
from multiprocessing.pool import Pool

import os

import time

from util import p
from multiprocessing import Process, Queue

print('Process (%s) start...' % os.getpid())


# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#   print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#   print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def run_process(name):
    p('Run child process %s (%s)...' % (name, os.getpid()))


def proc1():
    p('Parent process %s.' % os.getpid())
    pro = Process(target=run_process, args=('test',))  # 创建一个Process实例
    p('Child process will start.')
    pro.start()  # start()方法启动
    pro.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p('Child process end.')


# ----- Pool -----


def long_time_task(name):
    p('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    p('Task %s runs %0.2f seconds.' % (name, (end - start)))


def propool():
    p('Parent process %s.' % os.getpid())
    po = Pool(4)
    for x in range(5):
        po.apply_async(long_time_task, args=(x,))
    p('Waiting for all subprocesses done...')
    po.close()
    po.join()
    p('All subprocesses done.')


# ----- 子进程 -----
import subprocess


def subproc():
    p('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    p('Exit code:', r)


def input_subproc():
    p('$ nslookup')
    sp = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = sp.communicate(b'set q=mx\npython.org\nexit\n')
    p(output.decode('utf-8', errors='ignore'))
    p('Exit code:', sp.returncode)


# 进程间通信


def write(q):
    p('Process to write :%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        p('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    p('Process to write: %s' % os.getpid())
    while True:
        value = q.get(True)
        p('Get %s from queue.' % value)


def que():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


if __name__ == '__main__':
    # 进程
    proc1()
    # 进程池
    propool()
    # 子进程
    subproc()
    input_subproc()
    que()
