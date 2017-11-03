#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 错误调试测试（2）
# 单元测试（unit test）
# 快速打印
import time

from util import p
import unittest2


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
        p('Dict.__init__', time.time())

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest2.TestCase):
    def test_init(self):
        p('init', time.time())
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_attr(self):
        p('test_attr')
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key(self):
        p('test_key')
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        p('test_keyerror')
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        p('test_attrerror')
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):  # 调用测试方法前调用，（此处打印开始执行时间）
        p('setUP...', time.strftime('%Y-%m-%d %H:%M:%S %A', time.localtime(time.time())), time.time())

    def tearDown(self):
        p('tearDown...', time.time())  # 完成测试方法后调用


if __name__ == '__main__':
    unittest2.main()
