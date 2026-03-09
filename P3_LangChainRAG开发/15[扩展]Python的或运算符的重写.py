# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：15[扩展]Python的或运算符的重写.py
@Author  ：九成八
@Date    ：2026/3/7 21:27 
"""
class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)

    def __str__(self):
        return self.name


class MySequence(object):
    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for i in self.sequence:
            print(i)


if __name__ == '__main__':
    a = Test('a')
    b = Test('b')
    c = Test('c')
    e = Test('e')
    f = Test('f')
    g = Test('g')

    d = a | b | c | e | f | g  # a.__or__(b)
    d.run()
    print(type(d))