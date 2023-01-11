# names = ['abc', 'def', 'ghi']
# def fun(l, target):
#     for i, name in enumerate(l):
#         if name == target:
#             return i
#     return -1

# print(fun(names, 'abc'))


# name_list = ['ali', 'rehan', 'hassan', 'faizan']

# def search_fuc(l, search_item):
#     for j, i in enumerate(l):
#         if i == search_item:
#             print (f'psotion : {j}')
        
#     print("Not Found...!!!")

# search_item = input("Please enter the item name: ")
# search_fuc(name_list, search_item)


# name_list = ['ali', 'rehan', 'hassan', 'faizan']

# output = list(map(lambda i: len(i), name_list))
# print(output)

# nums = [1,3,5,7,9,7,2,4,6,5]
# is_even = list(filter(lambda i: i%2 == 0, nums))
# print(is_even)


# name = ['Ali', 'Rehan', 'fazi']
# age = [22, 23, 21]

# output = dict(zip(name, age))
# for i,j in output.items():
#     print(f'{i} : {j}')

# l = [(1,2),(2,3), (3,4),(4,5)]
# l1, l2 = list(zip(*l))

# def average_finder(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3], [4,5,6], [7,8,9]))


# d = {
#  'Ali' : {'score' : 50, 'age' : 22},
#  'Bilal' : {'score' : 40, 'age' : 23},
#  'Abid' : {'score' : 30, 'age' : 22}
# }

# print(max(d, key= lambda item: d[item]['score']))























