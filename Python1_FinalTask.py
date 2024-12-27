# my_list = [1, 2]
 
# for v in range(2):
#     my_list.insert(-1, my_list[v])
 
# print(my_list)

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
 
print(x, y, z)
 
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
 
print(a, b)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
 
 
print(fun(fun(2)))

nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums)
print(vals)


