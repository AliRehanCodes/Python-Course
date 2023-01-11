# class Person:
#     def __init__(self, first_name, last_name, age):
#         # isinstance varibles
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('Ali', 'Rehan', 22)
# print(p1.first_name)
        
# Exercise
# class Laptop:
#     def __init__(self, brand_naem, model, price):
#         # isinstance variable
#         self.brand_name = brand_naem
#         self.model = model
#         self.price = price
#         self.laptop_name = brand_naem + " " + model

# l1 = Laptop('Dell', 'E7470', 60000)
# print(l1.laptop_name) 

# practice

# class Person:
#     def __init__(self, first_name, last_name, age):
#         # isinstance variable
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def is_above_18(self):
#         return self.age > 18 

# p1 = Person('Ali', 'Rehan', 22)
# print(p1.is_above_18())

# Exercise

# class Laptop:
#     def __init__(self, brand, name, price):
#         # isinstance variable
#         self.brand = brand
#         self.name = name
#         self.price = price

#     def discount(self, n):
#         off_price = (n/100)*self.price
#         return self.price - off_price

# l1 = Laptop('dell', 'E7470', 63000)
# print(l1.discount(10))

# Class variable

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.r = radius

#     def calc_circumference(self):
#         return 2*Circle.pi*self.r

# c = Circle(4)
# print(c.calc_circumference())

# Practice

# class Laptop:
#     discount_var = 10
#     def __init__(self, brand, name, price):
#         # isinstance variable
#         self.brand = brand
#         self.name = name
#         self.price = price

#     def discount(self):
#         off_price = (self.discount_var/100)*self.price
#         return self.price - off_price

# l1 = Laptop('dell', 'E7470', 63000)
# # l1.discount_var = 20
# print(l1.discount())

# Exercise

# class Person:
#     count_instance = 0
#     def __init__(self,name):
#         Person.count_instance += 1
#         self.name = name

# p1 = Person("Ali")
# # p2 = Person()
# # p3 = Person()
# print(p1.name)

# Constructor

# class Person:
#     def __init__(self, f_name, l_name, age):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
    
#     @classmethod
#     def from_string(cls, string):
#         first, last, age = string.split(', ')
#         return cls(first,last,age)
    
# p1 = Person.from_string('ALi, Rehan, 22')
# print(p1.age)


# Getter & Setter

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = max(price,0)

#     @property           #Getter()
#     def specification(self):
#         return f'{self.brand} : {self.model} : {self.price}'
    
#     @property
#     def price(self):
#         return self.price

#     @price.setter       #setter
#     def price(self, new_price):
#         return max(new_price, 0)

# p1 = Phone('Nokia', '1100', -1000)
# p1.price = -500
# print(p1._price)
# # print(p1.specification)


# Ingeritance

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)

    @property
    def full_name(self):
        return f'{self.brand} {self.model}'
    
    def make_a_call(self, phone_number):
        return f'calling..... {phone_number}'

class Smart_Phone(Phone):
    def __init__(self, brand, model, price, RAM, camera):
        super().__init__(brand, model, price)
        self.RAM = RAM
        self.camera = camera

class FlagshipPhone(Smart_Phone):
    def __init__(self, brand, model, price, RAM, camera, snapdragon):
        super().__init__(brand, model, price, RAM, camera)
        self.snapdragon = snapdragon



phone1 = Phone('Nokia', '3310', 1000)
smart_phone1 = Smart_Phone('samsung', 'note 10', 30000, "6 GB", "20 MP") 
flagshipPhone = FlagshipPhone('Oneplus', '7pro', 50000, "8 GB", "30 MP", "855+")
# print(flagshipPhone.full_name + f" and ram is {flagshipPhone.RAM}") 
print(help(FlagshipPhone))