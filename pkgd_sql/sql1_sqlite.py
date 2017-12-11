#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
from util import p
import sqlite3
import os

DB_PATH = '../database/test.db'
DB_PATH2 = '../database/score.db'
if os.path.isfile(DB_PATH):
    os.remove(DB_PATH)
    os.remove(DB_PATH2)


# 连接到sqlite数据库
# 数据库文件为test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect(DB_PATH)
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
p('test 行数', cursor.rowcount)
# 执行查询语句
cursor.execute('select * from user where id=?',('1',))
# 获得查询结果集
values = cursor.fetchall()
p('查询结果', values)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()

con2 = sqlite3.connect(DB_PATH2)
cursor2 = con2.cursor()
cursor2.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor2.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor2.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor2.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor2.close()
con2.commit()
con2.close()

def get_score_in(low, high):
    """返回指定分数区间的名字，按分数从低到高排序"""
    cnt = sqlite3.connect(DB_PATH2)
    cs = cnt.cursor()
    cs.execute('select name from user where score > ? and score <= ? order by score ASC', (low, high))
    resp = cs.fetchall()
    cs.close()
    cnt.close()
    result = []
    for name in resp:
        result.append(name[0])
    return result



# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

p('Pass')
