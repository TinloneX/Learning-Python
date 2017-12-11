#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 TCP
# socket - 请求发起端（客户端client）

# 快速打印
from util import p
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
# 分离头部信息
header, html = data.split(b'\r\n\r\n', 1)
p(header.decode('utf-8'))
# 把接收的数据写入文件
with open('../files/sinal.html', 'wb') as f:
    f.write(html)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9999))

p(client.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Boby', b'Alix']:
    client.send(data)
    p(client.recv(1024).decode('utf-8'))
client.send(b'exit')
client.close()

