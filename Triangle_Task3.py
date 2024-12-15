def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** + b ** 2 
    if b > a and a > c:
        return b ** 2 == a ** + c ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_triangle(5, 4, 3))
print(is_a_triangle(1, 3, 4))