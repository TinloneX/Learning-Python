#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（10）
# 元类 metaclass / type()

# 快速打印
from util import p


def fn(self, name='world'):
    p('Hello,', name)


# -----------------------( type()创建类 )------------------------
def test_type():
    # 要创建一个class对象，type() 函数依次传入3个参数：
    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    Hello = type('Hello', (object,), dict(hello=fn))
    p(Hello)
    h = Hello()
    h.hello()
    p(h)
    p(type(h))


# -----------------------( metaclass1 )------------------------
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


def test_meta1():
    l = MyList()
    l.add(1)
    print(l)


# -----------------------( metaclass2 仅了解)------------------------
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        p('Found model:', name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                p('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, fields, params)
        print('SQL: %s' % sql)
        p('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


def test_model():
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()


if __name__ == '__main__':
    test_type()
    test_meta1()
    p('-----------------------------')
    test_model()
