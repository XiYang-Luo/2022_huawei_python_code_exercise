# -*- coding:utf-8 -*-
"""
作者：xiyang
日期：2022年06月04日
功能解释：您还没有描述该文件的功能
"""
class Property:
    def __init__(self, function):
        print("function:",id(function))
        self.function = function
    def __get__(self, instance, owner):
        print("__get")
        return self.function(instance)
class Foo:
    prop = "1"
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def product(self):
        print('Calling...')
        return self._x * self._y

    def test1(self):
        print("test1...")
        return "test1"

    print("product",id(product))
    product = Property(product)

def t1():
    print("t1")

foo = Foo(10, 2)
#print(foo.product)
print("-=-=-=",Foo.test1 == foo.test1)
print("-=-=-=",id(Foo.test1),id( foo.test1),id(foo.product))
print("FOO",id(Foo))
print(foo.test1)
print("ssss",id(Foo.test1))
#del foo.test1
del t1
#del foo.product
#print(foo.product)