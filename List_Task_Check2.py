my_list = [8, 10, 6, 2, 4, 12, 0, -4, 198, 10, 0, 23, -23]
swapped = True

while swapped:
    swapped = False

    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i+1] = my_list[i + 1], my_list[i]

print(my_list)

