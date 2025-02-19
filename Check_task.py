# tup = (1, ) + (1, )
# tup = tup + tup
# print(len(tup))

# first_prompt = input("1: ")
# a = len(first_prompt)
# second_prompt = input("2: ")
# b = len(second_prompt) * 2
# print(a/b)

# value = input("Enter a value: ")
# print(10/value)

# def fun(in=2, out=3):
#     return in * out

# print(fun(3))

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']
# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)

# my_list = ['Mary', 'had']
# def my_list(my_list):
#     del my_list[1]
#     my_list[0] = 'add'

# print(my_list(my_list))

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list)-1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

    