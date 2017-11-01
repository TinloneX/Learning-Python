#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（3）
# 获取对象信息

import types

# 引入oop2_extends文件
from pkg4_oop import oop2_extends
# 快速打印
from util import p


# -------------------------type()--------------------------
p(type(123))  # type() 判断对象类型 <class 'int'>
p(type(p))  # <class 'function'>
p(type(oop2_extends.animal))
p('type(123) == type("abc") ?', type(123) == type('abc'))  # Warning 建议使用isinstance()替代==比较类型
p('type(dog) == type(animal)?', type(oop2_extends.dog) == type(oop2_extends.animal))
p('isinstance(dog,Animal)?', isinstance(oop2_extends.dog, oop2_extends.Animal))
p('is p(*args, **kw) be a function ?', type(p) == types.FunctionType)
p(type(lambda x: x) == types.LambdaType)  # True
p('LambdaType', isinstance(lambda x: x, types.LambdaType))  # True 验证 type.LambdaType 是Class类型
p('GeneratorType', isinstance((x for x in range(10)), types.GeneratorType))  # True
p(type((x for x in range(10))) == types.GeneratorType)  # True
p('haha is a Husky?', isinstance(oop2_extends.haha, oop2_extends.Husky))
p('haha is Dog?', isinstance(oop2_extends.haha, oop2_extends.Dog))
p('haha is Animal?', isinstance(oop2_extends.haha, oop2_extends.Animal))
p('dogs are Husky?', isinstance(oop2_extends.dog, oop2_extends.Husky))
p('haha is Dog or Cat?', isinstance(oop2_extends.haha, (oop2_extends.Dog, oop2_extends.Cat)))


# --------------------------dir()--------------------------


class TestObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

    def read(self):
        p('TestObject read')


def read_something(fp):
    if hasattr(fp, 'read'):
        return fp.read()
    return None


obj = TestObject()
obj2 = TestObject()
p(dir(oop2_extends.cat))  # 获得一个对象的所有属性和方法
p('obj(TestObject) has attr "x" ?', hasattr(obj, 'x'))  # 判断对象obj中是否有x属性（变量或方法）
p('obj.x =', obj.x)
p('obj(TestObject) has attr "y" ?', hasattr(obj, 'y'))
obj.y = 12  # 为obj对象（而非TestObject类）添加y变量
p('add attr "y" into obj')
p('obj(TestObject) has attr "y" ?', hasattr(obj, 'y'))  # obj有y变量
p('obj2(TestObject) has attr "y" ?', hasattr(obj2, 'y'))  # obj2 没有y变量
p('obj.y =', obj.y)
p('obj2.y =', getattr(obj2, 'y', None))  # 从obj2中取y（无），若无此属性则默认返回None
fn = getattr(obj, 'power')
p(type(fn))  # <class 'method'> 与types.FunctionType不同?
if type(fn) == types.FunctionType:
    p(fn())
else:
    p('type(fn) != types.FunctionType')

read_something(obj)  # 有read方法的对象
read_something(oop2_extends.haha)  # 无read方法的对象
