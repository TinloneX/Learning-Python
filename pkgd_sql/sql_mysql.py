#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 mysql
# mysql 相关基础学习历时近一周（https://www.imooc.com/learn/122）

import mysql.connector

from util import p

conn = mysql.connector.connect(user='root', password='password',database='test')
cursor = conn.cursor()

cursor.execute('create table if not exists puser (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into puser (id, name) values (%s, %s)', ['1', 'Michael'])

p(cursor.rowcount)
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from puser where id = %s', ('1',))
values = cursor.fetchall()
p(values)
cursor.close()
conn.close()

