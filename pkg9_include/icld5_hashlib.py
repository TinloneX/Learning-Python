#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(5)
# 摘要算法

import hashlib
import hmac
import random
# 快速打印
from util import p

# ----- MD5
mdv = hashlib.md5()
mdv.update('how to use md5 in python hashlib?'.encode('utf-8'))  # 直接全文md5编码
p(mdv.hexdigest())  # 获取MD5的值
mdv2 = hashlib.md5()
mdv2.update('how to use md5 '.encode('utf-8'))
mdv2.update('in python hashlib?'.encode('utf-8'))  # 分两（多）步md5编码
p('分步update与全文update相等吗？', mdv.hexdigest() == mdv2.hexdigest())  # 不论分多少步编码，只要内容不变，同一内容的md5编码相同

# ----- SHA1
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))  # 类似md5
p(sha1.hexdigest())

db = {  # 使用dict模仿数据库存储
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '1572bd5808d3cb30a3ccccd97a338c02',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, pwd):
    if db[user]:
        hs = hashlib.md5()
        # hs.update(user.encode('utf-8'))  # 建议在md5编码时加盐处理（此批数据未加盐），在解码时加盐验证
        hs.update(pwd.encode('utf-8'))
        p(hs.hexdigest())
        if db[user] == hs.hexdigest():
            return True
        else:
            return False
    else:
        return None


p(login('michael', '123456'))
p(login('bob', 'abc999'))
p(login('alice', 'alice2008'))
p(not login('michael', '1234567'))
p(not login('bob', '123456'))
p(not login('alice', 'Alice2008'))


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), digestmod='MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # self.password = get_md5(password + self.key)  # 自定义加盐操作
        self.password = hmac_md5(self.key, password)  # 标准化加盐操作（推荐）


db2 = {
    'michael': User('michael', '123456'),
    'alice': User('alice', 'alice123456'),
    'tom': User('tom', '4425as')
}


def login(username, password):
    if db2.__contains__(username):
        user = db2[username]
        return user.password == hmac_md5(user.key, password)
    else:
        return False


p(login('michael', '123456'))
p(login('bob', 'abc999'))
p(login('alice', 'alice123456'))
