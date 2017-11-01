#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 面向对象编程（2）
# 继承（extends）


class Animal(object):  # 父类，基类，超类
    def run(self):
        print('Animal -- run...')


class Dog(Animal):  # 子类1
    def eat(self):  # 子类特有方法，父类无法直接访问到
        print('Dog eat dog-food')

    # def eat(self, food):  # python与java不同，没有重载的概念，只有完全的覆盖，故前一方法会报错
    #     print('Dog eat %s' % food)


class Cat(Animal):
    def eat(self):
        print('Cat eat cat-food')

    def run(self):  # 重写（覆盖）父类方法，该类对象调用run则执行此方法（而非父类run）
        print('Cat run & jump')  # 象形意义：猫跟（其他）动物跑的方式不一样


class Husky(Dog):
    def stare(self):
        print('Husky is staring at you...')


def someone_run(someone):
    someone.run()


animal = Animal()  # 供外部引用
dog = Dog()
cat = Cat()
haha = Husky()


if __name__ == '__main__':  # 仅本类测试执行
    animal.run()
    dog.run()
    cat.run()
    dog.eat()
    cat.eat()
    print('dog is Animal ?', isinstance(dog, Animal))
    print('animal is Dog ?', isinstance(animal, Dog))
    print('dog is Dog ?', isinstance(dog, Dog))
    print('dog is Cat ?', isinstance(dog, Cat))
    someone_run(animal)
    someone_run(dog)
    someone_run(cat)
