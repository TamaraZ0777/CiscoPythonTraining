my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list)

print(my_list[0][2])

t = [[3-i for i in range (3)] for j in range (3)]
print(t)

s = 0
for i in range(3):
    s += t[i][i]
print(s)
 

my_list = [i for i in range(-1, 2)]
print(my_list)


var = 1
while var < 10:
    print("#")
    var = var << 1

print(var)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)

my_list = [1, 2, 3, 4]
print(my_list[0:4])

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
