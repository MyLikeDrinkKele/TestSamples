#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# """ a standard module """
#
# __author__ = 'zoubin'
#
# import sys
#
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print(args[0])
#     elif len(args) == 2:
#         print(args[1])
#     else:
#         print(args)
#
#
# if __name__ == '__main__':
#     test()


# def _private_1(name):
#     print('good name:' + name)
#
#
# def _private_2(name):
#     print('this is ok:' + name)
#
#
# def getName(name):
#     if len(name) == 2:
#         _private_1(name)
#     if len(name) == 3:
#         _private_2(name)
# import sys
#
# print(sys.path)
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def getGrade(self):
#         if self.age >= 18:
#             return 'old boy'
#         else:
#             return 'small boy'
#
#
# jack = Student('jack', 15)
# print(jack.age)
# print(jack.getGrade())


# class Animal(object):
#     def run(self):
#         print('暧昧')
#
#
# class Cat(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass
#
#
# dog1 = Dog()
# dog1.run()
# animal1 = Animal()
# print(isinstance(dog1, Animal))
# print(isinstance(animal1, Dog))


# class Dog(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def getName(self):
#         return self.__name
#
#     def getAge(self):
#         return self.__age
#
#     def setName(self, name):
#         self.__name = name
#
#     def setAge(self, age):
#         if 0 <= age <= 150:
#             self.__age = age
#         else:
#             print('错误的年龄')
#
#
# dog1 = Dog('yellow', 0)
# dog1.__name = 'new Name'
# print(dog1.__name)
# print(dog1.getName())
# print(dog1.getName())
# dog1.setName('big red')
# print(dog1.getName())
# dog1.setAge(0)


# class Animal(object):
#     def run(self):
#         print('魔力红')
#
#
# class Dog(Animal):
#     def run(self):
#         print('dog，魔力红')
#
#
# class Cat(Animal):
#     def run(self):
#         print('cat，魔力红')
#
#
# class Car(object):
#     def run(self):
#         print('car，魔力红')
#
#
# dog1 = Dog()
# dog1.run()
# cat1 = Cat()
# cat1.run()
# # True
# print(isinstance(dog1, Dog))
# # True
# print(isinstance(dog1, Animal))
#
#
# def printRun(animal):
#     animal.run()
#     animal.run()
#
#
# car1 = Car()
# printRun(car1)
#
# print(type(car1) == type(cat1))

# if type('str') == type('123'):
#     print('类型相等')
# import types
#
#
# def fu():
#     pass
#
#
# str1 = 'renshengrumeng'
# print(type(fu) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# str1 = 'test'
# print(dir(str1))
# print(len('abc'))
# print('abc'.__len__())


# class MyObject(object):
#     def __init__(self):
#         self.s = 9
#
#     def power(self):
#         return self.s * self.s
#
#
# m1 = MyObject()
# # 检查是否有s属性
# print(hasattr(m1, 's'))
# # 为对象临时设置一个属性，并赋值
# setattr(m1, 'w', '10')
# print(m1.w)
# m2 = MyObject()
# # True
# print(hasattr(m1, 'w'))
# # False
# print(hasattr(m2, 'w'))
# # 获取s的属性值
# print(getattr(m1, 's'))
# # 如果获取不存在的属性值，就会报错
# # print(getattr(m1, 'y'))
# # 防止报错可设置返回默认值
# print(getattr(m1, 'y', 404))
# # 获得对象的方法
# fu = getattr(m1, 'power')
# print(fu())


# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return '可以进行流操作'
#     return None

class Student(object):
    add = 0

    def __init__(self, name):
        self.name = name
        Student.add = Student.add + 1


s1 = Student('张三')
s2 = Student('李四')
s3 = Student('王五')
s4 = Student('赵六')
s4.add = 100
# 4
print(Student.add)
# 4
print(s3.add)
# 100
print(s4.add)
del s4.add
# 4
print(s4.add)
