my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)
print(type(my_list))
tup = tuple(my_list) #converts the list into tuple
print(tup)
print(type(tup))

#same way an iterable can be converted to a list
tup = 1, 2, 3
my_list = list(tup)
print(my_list)
print(type(my_list))

