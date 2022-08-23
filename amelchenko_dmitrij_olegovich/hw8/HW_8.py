#1. Декоратор типов
# @typed(type=’str’)
# def add_two_symbols(a, b):
# return a + b
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
# return a + b + с
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001
def decorator(func):
    def typed(type:’str’):
        typed = func(arg1, arg2)

    return typed

@decorator(type:’str’)
def print_full_name():


print_full_name("3", 5)



#2. Расчет времени работы функции
import time

def my_fun_time(fun):

    def fun_time():

        start = time.perf_counter()
        fun()
        stop = time.perf_counter()

        return print(f'Function worked for <{stop - start:0.6f}> seconds')

    return fun_time

@my_fun_time
def generator():

    my_list = [1, 2, 3, 4, 5, 6]
    new_my_list = []

    for i in my_list:
        if i % 2:
            new_my_list.append(i)

    return new_my_list

generator()
