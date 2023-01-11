# # Function

# def add_two(a, b):
#     # return a + b
#     print(a+b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# total = add_two(a,b)
# # print(total)

# practice 01

# def last_char(a):
#     return a[-1]

# name = input("Please enter your name : ")
# char = last_char(name)
# print(f"last character of your name is : {char}")

# practice 02

# while True:
#     def odd_even(number):
#         if number%2 == 0:
#             return "Even number"
#         else:
#             return "Odd number"

#     number = int(input("Please enter a number: "))
#     output = odd_even(number)
#     print(output)

# practice 03

# def is_even(a):
#     return a%2 == 0

# print(is_even(3))

# exercise 01

# def greater_num(a,b):
#     if a>b:
#         return a
#     return b

# a = int(input("enter a number: "))
# b = int(input("Enter b number: "))

# output = greater_num(a,b)
# print(output)

# practice 03

# def greates(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     return c

# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# c = int(input("Enter c number: "))

# output = greates(a,b,c)
# print(f"{output} is the greatest number")

# Function into function

# def greater_num(a,b):
#     if a>b:
#         return a
#     return b
# def greatest(a,b,c):
#     bigger = greater_num(a,b)
#     return greater_num(bigger, c)

# Exersice 02

# def is_palendrom(char):
#     # revrse_char = char[:: -1]
#     # if char == revrse_char:
#     #     return True
#     # return False

# char = input("Enter a character: ")
# output = is_palendrom(char)
# print(output)

# Fibonacci Series

# def febonacci_seq(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2: 
#         print(a, b)
#     else:
#         print(a, b, end=" ")
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end=" ")
# n = int(input("Enter a number: "))
# febonacci_seq(n)

# Golobal vairable

# x = 5
# def variable():
#     global x
#     x = 7
#     print(7)
# print(x)
# variable()

































































































