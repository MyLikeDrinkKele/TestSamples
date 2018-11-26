# print('\'1024 * 768= \'\n\t' + str(1024 * 768))
# print(r'\n')


# def normalize(name):
#     return str(name).capitalize()
#
#
# print(normalize('aouzbin'))
# from functools import reduce
#
#
# def mulati(x, y):
#     return x * y
#
#
# def prod(l):
#     return reduce(mulati, l);
#
#
# arr = [1, 2, 3, 4]
# print(prod(arr))


# def is_odd(n):
#     return n % 2 == 0
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(is_odd, arr)))


# def is_palindrome(n):
#     if str(n) == str(n)[::-1]:
#         return True
#
#
# print(list(filter(is_palindrome, range(0, 100))))


# 按绝对值大小排序
# arr = [-1, -99, 23, 89, -7]
# print(list(sorted(arr, key=abs)))

# 按字母表顺序反向排序
# arr = ['Zoubin', 'Rose', 'tom', 'jack']
# print(list(sorted(arr, key=str.lower, reverse=True)))

# 根据姓名或者分数排序
# def by_name(arr):
#     return str(arr[0]).lower()
#
#
# def by_score(t):
#     return 100 - t[1]
#
#
# L = [('aming', 55), ('Rose', 77), ('tom', 88), ('Zack', 99)]
# print(sorted(L, key=by_name))
# print(sorted(L, key=by_score))


# def lazy_sum(*args):
#     def sum():
#         a = 0
#         for n in args:
#             a += n
#         return a
#
#     return sum
#
#
# f = lazy_sum(1, 2, 3, 4)
# print(f())


# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))


# L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
# print(L)


# import time
#
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# import time
# import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('函数调用名:' + func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def now():
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#
#
# now()


# import functools
#
#
# def int2(x, base=2):
#     return int(x, base)
#
#
# # 2的7次方 64
# # print(int2('1000000'))
#
# int3 = functools.partial(int, base=2)
# print(int3('10000'))

# import hello
#
# hello.getName('江西省')

