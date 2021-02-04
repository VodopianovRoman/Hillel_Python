# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат
# работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys,
# we got {}» остаток от деления.
import functools


# def decorator_remainder_of_division(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         res = 1
#         for i in args:
#             res *= i
#         res_remainder = 100 % res
#         if res_remainder == 0:
#             print('We are OK!')
#         else:
#             print(f'Bad news guys,we got {res_remainder}')
#     return wraper
#
#
#
# @decorator_remainder_of_division
# def multiplication(int_one, int_two):
#     return int_one * int_two
#
#
# multiplication(2, 3)

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который
# передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

# def decorator_check_for_number(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         for i in args:
#             if type(i) == int:
#                 func(i)
#             elif type(i) == str:
#                 raise ValueError('string type is not supported')
#
#     return wraper
#
#
# @decorator_check_for_number
# def number_function(int_arg):
#     print((int_arg * 100) / 20)


# number_function(2)

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы
# вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется,
# вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько
# эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение
# «Used cache with counter = {}» и
# количество раз обращений в cache.

# def decorator_fib(func):
#     cache = {}
#     @functools.wraps(func)
#     def wrap(*args):
#         if args in cache:
#             wrap.ccalls += 1
#             print(f'Used cache with counter = {fib.ccalls}')
#             return cache[args]
#         else:
#             cache[args] = func(*args)
#             wrap.ncalls += 1
#             print(f'Function executed with counter = {fib.ncalls}, function result = {func(*args)}')
#             return cache[args]
#
#
#     wrap.ccalls = 0
#     wrap.ncalls = 0
#     return wrap
#
#
# @decorator_fib
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)
#
# print('fib(20) =', fib(20))



# def decorator_multi(func):
#     cache = {}
#     @functools.wraps(func)
#     def wrap(*args):
#         if args in cache:
#             wrap.ccalls += 1
#             print(f'Used cache with counter = {wrap.ccalls}')
#             return cache[args]
#         else:
#             wrap.ncalls += 1
#             cache[args] = func(*args)
#             print(f'Function executed with counter = {wrap.ncalls}, function result = {func(*args)}')
#             return cache[args]
#
#     wrap.ccalls = 0
#     wrap.ncalls = 0
#     return wrap
#
#
# @decorator_multi
# def multi_bulti(int_n):
#     return int_n ** int_n
#
# multi_bulti(5)