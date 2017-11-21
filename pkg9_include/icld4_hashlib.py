#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(5)
# 摘要算法

# 快速打印
from util import p
import hashlib

# ----- MD5
mdv = hashlib.md5()
mdv.update('how to use md5 in python hashlib?'.encode('utf-8'))
p(mdv.hexdigest())

# ----- SHA1
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
p(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '1572bd5808d3cb30a3ccccd97a338c02',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, pwd):
    if db[user]:
        hs = hashlib.md5()
        # hs.update(user.encode('utf-8'))
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
