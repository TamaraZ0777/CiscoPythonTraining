def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(52.5, 1.65))
print(bmi(353, 1.65))
print(bmi(35, 2.65))
print(lb_to_kg(1))
print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6))
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

