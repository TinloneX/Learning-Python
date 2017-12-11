#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 TCP
# socket  - 请求响应端（服务端service）

# 快速打印
import threading

import time

from util import p
import socket

# 创建socket
service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
service.bind(('127.0.0.1', 9999))
service.listen(5)
p('Waiting for connection...')


def tcplink(sockt, addrs):
    p('Accept new connection from %s:%s...' % addrs)
    sockt.send(b'Welcome!')
    while True:
        data = sockt.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sockt.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sockt.close()
    p('Connection from %s:%s closed.' % addrs)


while True:
    sock, addr = service.accept()

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()




