# -*- coding:utf-8 -*-
"""
作者：xiyang
日期：2022年06月04日
功能解释：您还没有描述该文件的功能
"""
class Property:
    def __init__(self, function):
        self.function = function
    def __get__(self, instance, owner):
        return self.function(instance)
class Foo:
    prop = "1"
    def __init__(self, x, y):
        print("------")
        self._x = x
        self._y = y
    def product(self):
        print('Calling...')
        return self._x * self._y

    def ac(self):
        print("AC")

    print("==", id(product))
    product = Property(product)
    print("--", id(product))

def t1():
    print("t1")

foo = Foo(10, 2)
print(foo.product)
print("xxxx", id(foo.product))
#del foo.ac
del t1
#del foo.product
print(foo.product)
# del Foo.prop
print(Foo.prop)