# def function(x = 0):
#     return x

# value = function()
# print(value)

# value = function(3)
# print(value)

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
 
 
# print(f(3))

# def fun(x):
#     x += 1
#     return x
 
 
# x = 2
# x = fun(x + 1)
# print(x)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']
 
# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )
 
# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])

# def func_1(a):
#     return a ** a
 
 
# def func_2(a):
#     return func_1(a) * func_1(a)
 
 
# print(func_2(2))

# def any():
#     print(var + 1, end='')
 
 
# var = 1
# any()
# print(var)

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']
 
# for k in range(len(dictionary)):
#     v = dictionary[v]
 
# print(v)

# try:
#     value = input("Enter a value: ")
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

# my_list = ['Mary', 'had', 'a', 'little', 'lamb']
 
 
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
 
 
# print(my_list(my_list))

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# x = 1 // 5 + 1 / 5
# print(x)

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']
 
# for k in range(len(dct)):
#     v = dct[v]
 
# print(v)

# lst = [i for i in range(-1, -2)]
# print(lst)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
 
 
print(fun(0, 3))

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
 
for x in dct.keys():
    print(dct[x][1], end="")

lst = [[x for x in range(3)] for y in range(3)]
 
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

    