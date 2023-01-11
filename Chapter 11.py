# def total(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(total(1,2,3,4,5,6,7,8))

# Exercise 01

# def fun(n, *args):
#     # output = []
#     # for i in args:
#     #     output.append(i ** n)
#     # return output
#     if args:
#         return [i**n for i in args]
#     else:
#         print("You didn't pass args")

# n = int(input("Please enter a number: "))
# arr = [1,2,3,4,5,6]
# print(fun(n, *arr))

# **kwargs

# def fun(num, **kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# d = {
#     'name' : 'Ali Rehan',
#     'age' : 24,
#     'Gender' : 'Male',
# }
# fun(3, **d)

# PADK
# Perameter
# *args
# default perameter
# **kwargs

# Exercise 02

# def fun(l, **kwargs):
#     if kwargs.get('Reverse_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]

# name = ['ali' , 'rehan']
# print(fun(name, Reverse_str = True))

# lambda function

# add = lambda a,b : a+b
# multiply = lambda a,b : a*b
# is_even = lambda n : n%2 == 0

# print(add(1,2))
# print(multiply(3,4))
# print(is_even(4))
























