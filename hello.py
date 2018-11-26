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


class Dog(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age


dog1 = Dog('yellow', 98)
print(dog1.getName())
dog1.setName('big red')
print(dog1.getName())