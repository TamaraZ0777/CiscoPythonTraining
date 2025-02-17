# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or a + c <= b:
#         return False
#     return True

#more compact way
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(is_a_triangle( 1, 1, 1))
print(is_a_triangle(1, 1, 3))

