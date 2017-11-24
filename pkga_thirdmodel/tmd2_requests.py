#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用第三方模块(2)
# requests (安装：pip install requests)

# 快速打印
from util import p
import requests

r = requests.get('http://192.168.56.1:8080/api/user/preRegister?phone=10086')
p(r.status_code)  # 200
p(r.headers)
# {'Server': 'beegoServer:1.8.3', 'Date': 'Fri, 24 Nov 2017 07:08:23 GMT',
# 'Content-Length': '43', 'Content-Type': 'text/plain; charset=utf-8'}
p(r.text)  # {"state" : 0,"msg" : "success","data" : {}}

# requests 自动拼接参数
r2 = requests.get('http://192.168.56.1:8080/api/user/preRegister', params={'phone': '10086'}, timeout=2.5)
p(r2.url)
p('采用的编码', r2.encoding)  # 获取编码方式
p(r2.json())  # 自动提取json串

rp = requests.post('http://192.168.56.1:8080/api/user/register',
                   #  上传参数使用dict保存data
                   data={'phone': '10086', 'password': '100010', 'verificationCode': '6666'})
p(rp.status_code)
p(rp.json())  # 自动提取json串

# ------- file  /api/file/upload
upfile = {'file': open('../files/test_file.txt', 'rb')}  # 使用dict保存读取的文件
rpf = requests.post('http://192.168.56.1:8080/api/file/upload', files=upfile)  # 上传文件
