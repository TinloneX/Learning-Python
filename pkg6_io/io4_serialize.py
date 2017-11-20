#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 I/O编程 （4）
# 序列化（pickling / （java）Serialize）

# 快速打印
from util import p
import pickle
import json

PATH_DUMP = '../files/dump.txt'

d = dict(name='Bob', age=20, score=88)
p(pickle.dumps(d))  # 将字典d序列化为bytes

with open(PATH_DUMP, 'wb') as f:  # 准备文件输入为对象f
    pickle.dump(d, f)  # 将序列化对象写入文件

with open(PATH_DUMP, 'rb') as f:  # 读取文件输出为对象f
    d2 = pickle.load(f)  # 加载（还原bytes为）序列化对象
    p(d2)  # 输出对象d2
    p('比较内容：', d == d2)  # 比较对象内容  True
    p('比较地址：', id(d) == id(d2))  # 比较对象id（地址） False
    p('结论：这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已')

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# -------- json --------

j1 = json.dumps(d)
p('将dict转换为json：', j1)
dx = json.loads(j1)
p('将json反序列化：', dx)


# -------- json 进阶 --------


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        p(name, age, score)


def student2dict(std):  # 对象转dict的（回调）方法,dict可以更直接转json
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(di):  # # dict转对象的（回调）方法，dict可以更方便转对象
    return Student(di['name'], di['age'], di['score'])


s = Student('Tom', 22, 86)
j1 = json.dumps(s, default=student2dict)  # 对象转json,传入转换方法
p(j1)
j2 = json.dumps(s, default=lambda obj: obj.__dict__)  # 对象转json，传入对象的dict，定义了__slots__的class勿用
p(j2)

p(json.loads(j1, object_hook=dict2student))  # json转对象，传入dict转对象的方法
