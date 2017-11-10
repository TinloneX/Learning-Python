#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 I/O编程 （1）
# 文件读写

# 快速打印
from util import p

PATH_TXT = "../files/test_file.txt"
PATH_HARD = "../files/cnz_text.txt"
PATH_PNG = "../assets/icon_boy.png"

try:
    f = open(PATH_TXT, 'r')  # 打开文件（根据文件路径创建文件(流)）
    p(f.read())  # 将（所有）文件内容以String格式打印
except FileNotFoundError as e:  # 存在IO异常
    p(e)
finally:  # 无论是否正确打开文件，在文件使用完后都将关闭文件(流)
    f.close()

with open(PATH_TXT, 'r') as f:  # 简化try-finally->(close())文件使用完后会自行执行close操作
    p(f.read())

with open(PATH_TXT, 'r') as f:
    p(f.readline(20))  # file.readline(size) 读取size字节内容

with open(PATH_TXT, 'r') as f:
    p(f.readlines())  # file.readlines(index) 将文件按行读取生成集合，并取1~index个字节所包含的集合元素
    # 示例，取index = 0，20，50，100 分别对应"全部行"、"含第一行"、"含前两行"、"含前三行",大小与每行字节数有关

with open(PATH_TXT, 'r') as f:
    for line in f.readlines():  # 遍历所有行的集合
        p(line.strip())  # 不计每行末的换行符（'\n'）


# -------- file-like Object --------


class MyFileLike(object):
    def read(self):  # 类似open()方法返回的带有read()方法的对象均可称作file-like Object
        return 'I`m a file-like object !'


# -------- 二进制文件 --------
with open(PATH_PNG, 'rb')as f1:
    p(f1.read())

# -------- 字符编码 --------
with open(PATH_HARD, 'r', encoding='utf-8')as f2:  # 指定字符集
    p(f2.read())

with open(PATH_HARD, 'r', encoding='gbk', errors='ignore')as f3:  # 指定字符集并忽略字符集非法编码异常
    p(f3.read())  # 不符合gbk编码，失去解析意义

# -------- 写文件 --------
with open(PATH_TXT, 'w') as fw1:  # 默认编码写入
    fw1.write('this is one line which been write by code')

with open(PATH_HARD, 'w', encoding="utf-8") as fw2:  # 指定编码写入
    fw2.write('通过代码写入中文字符')

with open(PATH_HARD, 'w', encoding="gbk", errors='ignore') as fw2:  # 指定忽略错误编码写入
    fw2.write('error words :通过代码写入中文字符')

line_txt = ['line 1 :this is a test file\n', 'line 2 :file name -->test_file.txt\n', 'line 3 :Hellow,World!']
line_cnz = ['这是一行普通中文字：你好，世界！\n', '这是一行特殊中文字：厷厸厹厺厼厽厾叀叁参叄叅叆叇亝']


def __reset():
    with open(PATH_TXT, 'w', encoding='utf-8') as fr:
        fr.writelines(line_txt)  # 恢复原内容
    with open(PATH_HARD, 'w', encoding='utf-8') as frh:
        frh.writelines(line_cnz)  # 恢复原内容


m = {'Y': True, 'N': False}
b = input('是否回复文件内容（reset fils）？(y/n)')
t = str(b).upper()
if t == 'Y' or t == 'N':
    if m[t]:
        __reset()
else:
    p('错误，仅可输入Y或N（error:is sure "Y" or "N" ?）')
