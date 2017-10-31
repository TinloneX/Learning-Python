#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（1）
# 类（Class）与实例(Object)

# -------- 面向对象(OOP)与面向过程(OPP) --------
std1 = {'name': 'Alex', 'score': 98}


def print_score(std):
    print(std['name'], ':', std['score'])


class Student(object):
    def __init__(self, name, score, grade):
        self.name = name  # 公开的变量
        self.score = score
        self.__grade = grade  # 私有的变量

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def tostring(self):
        print("%s : %s" % (self.name, self.score))

    def get_level(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'


print_score(std1)
std2 = Student('Bob', 86, 2)
std2.tostring()
std2.gender = 'boy'  # python相比于java，实例可以添加类中未定义的变量，
# 示例间也是相互独立的，两个不同的Student实例除却已初始定义的变量外，其他的变量均可不同
print(std2.gender)
print(std2.get_level())
print(std2.get_grade())  # 私有变量(一般)无法被外部直接访问(以下方式仍可访问，不建议)
print(std2._Student__grade)  # Python解释器对外把__name变量改成了_Student__name
std2.set_grade(3)  # 私有变量通过内定函数更改私有变量的值
print(std2.get_grade())

std3 = Student('Tom', 82, 3)
std3.__grade = 6  # 此时并不是更改Student中的私有变量__grade(因为它现在是_Student__grade)，而是新增了一个变量
print(std3.__grade)  # 6
print(std3.get_grade())  # 3
