# List

# number = [1,2,3,4,5]
# print(number)

# words = ['word1', 'word2', 'word3']
# print(words)

# words[0] = 1
# print(words)

# how to store data in list

# ___________________________________________________________________________________________________
# word1 = ['word1', 'word2']
# words.append('word4')
# print(words)
# word2 = ['word3', 'word4']
# word1.insert(1,'insert')       inster() method
# print(word1)
# word1.extend(word2)            extend() method
# print(word1)
# _________________________________________________________________________________________________
# word1.pop(1)                   pop() method
# print(word1)
# del word1[1]                   del statement
# print(word1)
# word1.remove('word2')          remove() method
# print(word1)

# append, extend, insert
# pop, remove, del
# _________________________________________________________________________________________________
# if 'word1' in word1:          in key word
#     print("Present")
# else:
#     print("NOt present")
# _________________________________________________________________________________________________
# useful methods

# count() method
# sort() method
# sorted() method
# clear() method
# reverse() method
# copy() method

# _________________________________________________________________________________________________

# user_info = 'AliRehan 22'.split(' ')
# print(user_info)

# user_info2 = ['Ali', '22']
# print(','.join(user_info2))

# _________________________________________________________________________________________________
# name = input("Please enter your name: ")
# age  = input("Please enter your age: ")

# user_info = []
# user_info.append(name)
# user_info.append(age)
# print(user_info)

# _________________________________________________________________________________________________

# word = ['word1', 'word2', 'word3', 'word4']
# for i in word:
#     print(i)

# _________________________________________________________________________________________________

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j)

# print(matrix[2][0])

# _________________________________________________________________________________________________

# def negative_value(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# output = negative_value([1,2,3,4,5,6,7,8,9,10])
# print(output)

# _________________________________________________________________________________________________

# Exercise 01
# def square(l):
#     square_list = []
#     for i in l:
#         square_list.append(i**2)
#     return square_list
# # l = list(input("Please enter a list"))
# output = square([1,2,3,4,5])
# print(output)

# _________________________________________________________________________________________________
# Exercise 02

# def reverse(l):
#     reverse_list = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         reverse_list.append(popped_item)
#     return reverse_list
# print(reverse([1,2,3,4,5]))

# _________________________________________________________________________________________________
# Exercise 03

# def reverse_string(l):
#     string = []
#     for i in l:
#         string.append(i[::-1])
#     return string

# print(reverse_string(['abc', 'xyz'])

# _________________________________________________________________________________________________

# Exercise 04

# def odd_even_filter(l):
#     odd = []
#     even = []
#     for i in l:
#         if i%2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return odd, even
# print(odd_even_filter([1,2,3,4,5,6,7,8,9]))

# _________________________________________________________________________________________________
# Exercise 05

# def filter_same(l1, l2):
#     same_value = []
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 same_value.append(i)
#     return same_value

# print(filter_same([1,2,3,4],[1,2,5,6]))

# _________________________________________________________________________________________________
# Exercise 06

def list_count(l):
    total_list = 0
    for i in l:
        if type(i) == list:
            total_list += 1
    return total_list

print(list_count([1,2,3]))



















































































