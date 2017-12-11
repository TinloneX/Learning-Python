#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 UDP
# socket - 请求发起端（客户端client）

# 快速打印
import socket

from util import p

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9998))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()




