numbers = [10, 5, 7, 2, 1]
print("Original list contains:", numbers)

numbers[0] = 111
print("\nNew list contains:", numbers)

numbers[1] = numbers[4]
print("Updated list contains:", numbers)

print("\nList length:", len(numbers))

print(numbers)

del numbers[1]

numbers.append(4)

print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(numbers)

