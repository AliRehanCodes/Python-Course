user_info = dict(
    name = 'ALi Rehan',
    age = 24,
    fav_movies = ['spiderman', 'ironman', 'moula jutt']
)

# print(user_info)

# _________________________________________________________________________________________________
# input

# user_info = dict()

# user_info['name'] = input("Please enter your name: ")
# user_info['age']  = int(input("Please enter your age: "))

# print(user_info)

# _________________________________________________________________________________________________
# if condition

# if 24 in user_info.values():
#     print('Present')
# else:
#     print("Not present")

# _________________________________________________________________________________________________
# iteration
# for key, value in user_info.items():
#     print(f"key is {key} and value is {value}")

# for i in user_info:
#     print(user_info[i])

# _________________________________________________________________________________________________

d = dict.fromkeys(range(1,11), None)
print(d)

# print(user_info.get('name'))

# if user_info.get('names'):
#     print("Yes")
# else:
#     print("No")

# _________________________________________________________________________________________________
# Exercise

# def cube_finder(n):
#     cube = {}
#     for i in range(1,n+1):
#         cube[i] = i**3
#     return cube        

# print(cube_finder(3))

# _________________________________________________________________________________________________
def name_counter(name):
    counter = {}
    for i in name:
        counter[i] = name.count(i)
    return counter

print(name_counter("ali Rehan"))

# _________________________________________________________________________________________________
# Exercise 02

# user_info2 = {}
# user_info2['name'] = input("Please enter your name: ")
# user_info2['age'] = int(input("Please enter your age: "))
# user_info2['fav_movies'] = input("Please enter your fav movies comma seperated: ").split(",")

# for key,value in user_info2.items():
#     print(f"{key} : {value}")

















































































