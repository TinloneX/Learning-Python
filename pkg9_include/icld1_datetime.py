#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(1)
# 日期和时间标准库 (datetime)

# 快速打印
from util import p
import re
from datetime import datetime, timedelta, timezone

# 当前时间
now = datetime.now()
p(now)
p(type(now))
# 指定时间创建datetime
p1 = datetime(2017, 12, 24, 00, 59)
p(p1)
# -------- datetime 转换为timestamp
pt1 = p1.timestamp()  # 将datetime转换为timestamp
p(pt1)
p(datetime.fromtimestamp(pt1))  # 将timestamp转换为datetime
p(datetime.utcfromtimestamp(pt1))  # 将timestamp转换为UTC时间
# -------- str转换为datetime
cd = datetime.strptime('2017-11-16 11:08:22', '%Y-%m-%d %H:%M:%S')
p(cd)
# -- datetime 转换为str
cs = cd.strftime('%a, %b %d %H:%M')
p(cs)
# ----- datetime加减
cdt = cd + timedelta(hours=5)  # 5 hours after
p(cdt)
cdp = cd - timedelta(days=2)  # 2 days before
p(cdp)
cdf = cd + timedelta(days=2, hours=5)  # 2d5h after
p(cdf)
# -----本地时间转UTC时间
now_utc8 = timezone(timedelta(hours=8))  # 东八区
tz_utc8 = now.replace(tzinfo=now_utc8)  # 替换时区为东八区
p(tz_utc8)
# -----时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 替换时区为0时区
p(utc_dt)
pk_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 将时区转换为北京时间
p('Peking time', pk_dt)
tky_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # 将时区转换为东京时间
p('Tokyo time', tky_dt)
k2p_dt = tky_dt.astimezone(timezone(timedelta(hours=8)))  # 将东京时间转为北京时间
p2k_dt = pk_dt.astimezone(timezone(timedelta(hours=9)))  # 将北京时间转为东京时间
p(p2k_dt.timestamp())  # 0时区时间秒值（任意"时刻"恒定）

idst = input('输入时间（%Y-%m-%d %H:%M:%S）:')  # 提示输入
try:
    idt = datetime.strptime(idst, '%Y-%m-%d %H:%M:%S')  # 转换时间
    i0dt = idt.replace(tzinfo=timezone.utc)  # 指定0时区
    time_mill = i0dt.timestamp()  # 取时间秒值作为基准待用
    itz = input('输入时区（UTC+5:00）:')  # 提示输入时区
    rex = re.compile(r'^UTC([+\-])(0?[0-9]|1[12]):00$')  # 东西12区正则截取
    mc = rex.match(itz)  # 验证输入
    if mc and mc.group(1) is '+':  # 匹配 且 为东12区
        utc_num = int(mc.group(2))  # 取时区值
        total = time_mill - utc_num * 60 * 60  # 0时区基准时间相对于utc_num时区为未来时间，故减去时区差时
        p('timezone = %d, timestamp = %s' % (utc_num, total))
    elif mc and mc.group(1) is '-':  # 匹配 且 为西12区
        utc_num = int(mc.group(2))  # 取时区值
        total = time_mill + utc_num * 60 * 60  # 0时区基准时间相对于utc_num时区为过去时间，故减去时区差时
        p('timezone = %d, timestamp = %s' % (utc_num, total))
    else:  # 不匹配
        p('时区输入有误')
except Exception as e:
    p(e)  # debug
