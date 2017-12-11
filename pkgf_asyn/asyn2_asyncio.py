#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
import threading

from util import p
import asyncio


@asyncio.coroutine
def hello():
    p('Hello world! (%s)' % threading.current_thread())
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    p('Hello again! (%s)' % threading.current_thread())


def test1():
    # 获取event_loop
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    # 执行coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


# -----------------


def wget(host):
    p('wget %s...' % host)
    conn = asyncio.open_connection(host, 80)
    reader, writer = yield  from conn
    header = 'GET / HTTP /1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == None or len(line) == 0 or line == b'\r\n':
            break
        p('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


def test2():
    loop2 = asyncio.get_event_loop()
    tasks2 = [wget(host) for host in ['www.sina.com.cn', 'www.souhu.com', 'www.163.com']]
    loop2.run_until_complete(asyncio.wait(tasks2))
    loop2.close()


# 对比｛asyn2_asyncio.py #hello()｝,尽在python3.5 + 可用
async def hello2():
    p('Hello world!')
    r = await asyncio.sleep(1)
    p('Hello again!')


if __name__ == '__main__':
    # test1()
    test2()
