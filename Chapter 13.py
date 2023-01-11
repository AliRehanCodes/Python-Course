# pass function as perameter

# l = [1,2,3,4,5,6]

# def my_map(func, l):
#     my_list = []
#     for item in l:
#         my_list.append(func(item))
#     return my_list

# # print(my_map(lambda a: a**2, l))

# def my_map2(func, l):
#     return [func(item) for item in l]

# # print(my_map2(lambda a: a**2, l))

# return Function

# def outer_func(msg):
#     def inner_func():
#         print(f"the msg is {msg}")
#     return inner_func

# var = outer_func("Hi There !")
# var()

# Practice

# def outer_func(power):
#     def inner_func(number):
#         print(number**power)
#     return inner_func

# var = outer_func()
# var(4)

# Decorator

# def decorator_func(any_function):
#     def enhaced_func():
#         print('this is decorator function')
#         any_function()
#     return enhaced_func

# @decorator_func
# def func1():
#     print('this is function 01')

# @decorator_func
# def func2():
#     print('This is function 2')


# func1()
# func2()

# Complete decorator

# from functools import wraps

# def decorator_fun(any_function):
#     @wraps(any_function)
#     def enhanced_function(*args, **kwargs):
#         ''''This is wrap function'''
#         print('Decorator executed')
#         return any_function(*args, **kwargs)
#     return enhanced_function

# @decorator_fun
# def func(a,b):
#     '''This is add function'''
#     return a+b

# print(func.__doc__)

# Practice of decorators

# from functools import wraps

# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapped_function(*args, **kwargs):
#         print(f'you are calling {any_function.__name__} function')
#         print(f'{any_function.__doc__}')
#         return any_function(*args, **kwargs)
#     return wrapped_function

# @print_function_data
# def add(a,b):
#     '''this function takes two input as argument and return their sum'''
#     print(f'Sum of number is {a+b}')
        
# add(3,4)

# Exercise

# from functools import wraps
# import time

# def calcul_time(any_fun):
#     @wraps(any_fun)
#     def wrapper_func(*args, **kwargs):
#         t1 = time.time()
#         any_fun(*args, **kwargs)
#         t2 = time.time()
#         print(f'total time : {t1-t2}')
#     return wrapper_func

# @calcul_time
# def func1(a,b):
#     return a+b

# print(func1(1,2))

# Practice

# from functools import wraps

# def only_int_allowed(any_func):
#     @wraps(any_func)
#     def wrapper_func(*args, **kwargs):
#         data_types = []
#         for arg in args:
#             data_types.append(type(arg) == int)
#         if all(data_types):
#             return any_func(*args, **kwargs)
#         else:
#             print("only int data type allowed")
#     return wrapper_func
        


# @only_int_allowed
# def func1(*args):
#     total = 0
#     for i in args:
#         total += i
#     print(total)


# func1(1,2,3,4,5,'a')

# Practive
# from functools import wraps

# def only_int_allowed(any_func):
#     @wraps(any_func)
#     def wrapper_func(*args, **kwargs):
#         if all([type(arg) == int for arg in args]):
#             return any_func(*args, **kwargs)
#         print("only int data type allowed")
#     return wrapper_func
        


# @only_int_allowed
# def func1(*args):
#     total = 0
#     for i in args:
#         total += i
#     print(total)


# func1(1,2,3,4,5,'a')   


# Practice

from functools import wraps

def only_data_type_allowed(data_type):
    def decorator(any_func):
        @wraps(data_type)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return any_func(*args, **kwargs)
            return ("Invalid input")
        return wrapper
    return decorator

@only_data_type_allowed(int)
def func(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(func(1,2,3,4,5,6,'e'))


    









