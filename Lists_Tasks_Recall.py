numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)

numbers[0] = 111
print("Newal list content:", numbers)

numbers[1] = numbers[4]
print("Newest list content:", numbers)

print(len(numbers))

del numbers[1]
print(len(numbers))

