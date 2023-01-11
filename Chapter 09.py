# l = list(range(1,11))
# print(l)

# names = ['ali', 'rehan', 'bilal']
# name_first_letter = [name[0] for name in names]
# print(name_first_letter)

# _________________________________________________________________________________________________

# def reverse_string(l):
#     return [i[::-1] for i in l]

# print(reverse_string(['abc', 'xyz']))

# _________________________________________________________________________________________________
# odd_nums = [i for i in range(1,11) if i%2 != 0]
# print(odd_nums)

# _________________________________________________________________________________________________

def func(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float )]
print(func([1,2,3.0]))