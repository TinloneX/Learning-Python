#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 I/O编程 （3）
# 操作文件和目录（Operating files and directories）

# 快速打印
from util import p
import os
import shutil

p(os.name)  # 获取操作系统 /如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# p(os.uname())  # uname()函数在Windows上不提供,os模块的某些函数是跟操作系统相关的
p(os.environ)  # 操作系统中定义的环境变量
p(os.environ.get('PATH'))  # 要获取某个环境变量的值, 如PATH
p(os.environ.get('none', 'None'))  # 获取不确定环境变量的值，(建议)主动提供备选值

a = os.path.abspath
p(a('..'))  # 查看上级目录路径
b = os.path.join(a('..'), 'testdir')
p(b)  # 先表示出要创建的目录
if os.path.exists(b):  # 如果存在该目录
    os.rmdir(b)  # 删除该目录
    p(os.listdir(a('..')))  # 打印子目录列表

os.mkdir(b)  # 创建该目录
p(os.listdir(a('..')))  # 打印子目录列表

PATH_TXT = "../files/test_file.txt"
c = os.path.split(PATH_TXT)  # 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
p(c)
c2 = os.path.splitext(PATH_TXT)  # 合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

shutil.copyfile('io3_file2.py', '../files/io3_file2.py')  # 将此文件复制到files目录下
os.rename('../files/io3_file2.py', '../files/io3_copy.py')  # 重命名
os.remove('../files/io3_copy.py')  # 移除

drs = [x for x in os.listdir(a('.')) if os.path.isfile(x)]  # 列出当前目录下的所有文件
p(drs)
pys = [x for x in drs if os.path.splitext(x)[1] == '.py']  # 列出文件名以.py结束的文件
p(pys)


def __list(idr):
    lx = [x for x in os.listdir(idr)]
    j = os.path.join
    for d in lx:
        if os.path.isfile(j(idr, d)):
            p('<file>', d)
        elif os.path.isdir(j(idr, d)):
            p('<dir> ', d)
        else:
            p('      ', d)


idir = input('文件夹:')  # 示例：此处输入 D:\
if os.path.exists(idir) and os.path.isdir(idir):  # 判断输入文件夹路径是否存在
    __list(idir)  # # 类似于Win系统CMD中 dir /l ,其他系统中 dir -l
else:
    p('%s 目录不存在！' % idir)


def __filter(fx, flt):
    os.chdir(fx)  # 将os操作路径设置为fx
    j = os.path.join  # 拼接path函数
    for x in os.listdir(os.curdir):  # 遍历该目录下文件列表
        if os.path.isdir(j(os.curdir, x)):  # 若路径对应文件夹
            __filter(x, flt)  # 递归遍历子目录
            os.chdir(os.pardir)  # 子目录遍历完成后，操作目录还原为上级目录
        else:  # 若路径对应文件
            if flt in x:  # 若文件名中包含筛选字符串
                p(j(os.curdir, x))  # 打印它的相对路径，尝试：返回可迭代对象


fp = input('根目录：')
if os.path.exists(fp) and os.path.isdir(fp):
    _flt = input('筛选：')
    __filter(fp, _flt)
else:
    p('%s 目录不存在！' % fp)
