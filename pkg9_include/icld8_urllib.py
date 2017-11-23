#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(8)
# urllib

# 快速打印

from util import p
from urllib import request, parse

p('Warnning, 此处使用个人本地搭载的服务器作为请求对象，其他人使用请自行替换url')


def parsex(response):
    data = response.read()
    p('Status:', response.status, response.reason)
    for k, v in response.getheaders():
        p('%s: %s' % (k, v))
    p('Data:', data.decode('utf-8'))
    p('---------------------------------------------')


# ------------------ Get请求
with request.urlopen('http://192.168.56.1:8080/api/user/preRegister?phone=10086') as f:
    parsex(f)

# 使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
req = request.Request('http://www.baidu.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, '
                             'like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    parsex(f)

# ---------------- Post 请求
p('本地服务器注册...')
email = input('电话号码:')
pwd = input('密码:')
login_date = parse.urlencode([
    ('phone', email),
    ('password', pwd),
    ('verificationCode', '6666')
])
rq_post = request.Request('http://192.168.56.1:8080/api/user/register')
# 若服务器需要验证文件头，则可添加对应文件头
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, '
#                             'like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(rq_post, data=login_date.encode('utf-8')) as f:
    parsex(f)

# ------------- Handler
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
