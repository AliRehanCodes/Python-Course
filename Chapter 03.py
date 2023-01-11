# # # # # # # if statement

# # # # # # age = int(input("Enter your age: "))
# # # # # # if age >= 18:
# # # # # #     print("You are adult")
# # # # # # else:
# # # # # #     print(f"Sorry your age is {age} you are not adult")

# # # # # # Exercise 01

# # # # # winnig_number = 45
# # # # # guess_number = int(input("Please guess a number between 0-100 : "))

# # # # # if guess_number == winnig_number:
# # # # #     print("Congrats you WIN!!!!!!")
# # # # # else:
# # # # #     if guess_number > winnig_number:
# # # # #         print("Too high")
# # # # #     else:
# # # # #         print("Too low")

# # # # # and, or condition 

# # # # name = "Ali"
# # # # age = 22
# # # # if name == "Ali" and age == 22:        Both should be True
# # # #     print("Condition True")
# # # # else:
# # # #     print("Condition False")

# # # # if name == "Ali" or age == 20:         One Should be True
# # # #     print("Condition True")
# # # # else:
# # # #     print("Condition False")

# # # # Exercise 02

# # # name = input("Please Enter your name: ")
# # # age = int(input("Enter your age: "))

# # # if age == 10 and (name[0] == "a" or name[0] == "A"):
# # #     print("You can watch COCO")
# # # else:
# # #     print("Sorry you can't watch movie")

# # # elif statment

# # age = int(input("Enter your age: "))

# # if age<0:
# #     print("You can't watch movie")
# # elif 0<age<=3:
# #     print("Ticket price: Free")
# # elif 4<age<=10:
# #     print("Ticket price: 150")
# # elif 11<age<=60:
# #     print("Ticket price: 250")
# # else:
# #     print("Ticket price: 200")


# # in keyword
# # name = "Ali Rehan"
# # if 'a' in name:
# #     print("a is present in name")
# # else:
# #     print("a is not present in name")

# name = input("Please enter your naem:")
# if name:
#     print(f"your name is {name}")
# else:
#     print("You didn't enter your name")


# # While loop
# i = 1
# while i<=10:
#     print(f"Hello world {i}")
#     i = i + 1

# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i+=1
# print(total)

# Exercise 03

# n = int(input("Please enter a number: "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i+=1
# print(total)

# Exercise 04

# number = input("Please enter digits: ")
# n = len(number)
# i = 0
# total = 0
# while i < n:
#     total += int(number[i])
#     i+=1
# print(total)

# Esercise 05
# name = input("Please enter your name:")
# n = len(name)
# name = name.lower()
# temp = ""
# i = 0 
# while i < n:
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i += 1

# for loop
# for i in range(1,11):
#     print(f"hello world : {i}")
#     print("\n")

# sum = 0 
# for i in range(1,11):
#     sum += i 
# print(sum)

# number = int(input("Enter the number: "))
# total = 0
# for i in range(1, number+1):
#     total += i 
# print(total)

# number = input("Enter a number: ")
# total = 0
# for i in range(len(number)):
#     total += int(number[i])
# print(total)

# name = input("Please enter your name: ")
# name = name.lower()
# temp = ""
# for i in range(len(name)):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# gussing number game

# import random
# winning_number = random.randint(1,100)
# guessing_number = int(input("Please guess a number between 1-100: "))
# attempt = 1
# game_over = False

# while not game_over:
#     if winning_number == guessing_number:
#         print(f"you win in {attempt} attempts")
#         game_over = True

#     else:
#         if winning_number < guessing_number:
#             print("Too high..!!")
#         else:
#             print("Too Low..!!")
#         attempt += 1
#         guessing_number = int(input("Guess again: "))

# Step argument

# for i in range(1,11,2):    #for even number
#     print(i)        



        

    































































