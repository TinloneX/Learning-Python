#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 UDP
# socket - 请求发起端（客户端client）

# 快速打印
import socket
import threading

import time

from util import p

service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

service.bind(('127.0.0.1', 9998))

p('Bind UDP on 9998')


while True:
    # 接收数据:
    data, addr = service.recvfrom(1024)
    print('Received from %s:%s.' % (data, addr))
    service.sendto(b'Hello, %s!' % data, addr)


