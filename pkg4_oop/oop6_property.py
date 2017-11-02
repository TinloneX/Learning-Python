#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（6）
# 使用@property

# 快速打印
from util import p


class Student(object):
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            self._score = 0
        if value < 0 or value > 150:
            raise ValueError('score must between 0 and 150')
        self._score = value


class Teacher(object):
    def __init__(self):
        self.__birth = 2017

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2017 - self.__birth


class Screen(object):
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__resolution = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height


if __name__ == '__main__':
    t = Teacher()
    t.birth = 1992
    p('birth = %s and age = %s ' % (t.birth, t.age))
    s = Screen()
    s.width = 720
    s.height = 1280
    p(s.resolution)
