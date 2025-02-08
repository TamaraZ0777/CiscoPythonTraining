hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter your number to put in the middle of the list: "))
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)
print(len(hat_list))

hat_list.insert(1, 333)
print(hat_list)

my_list = []
for i in range(10):
    my_list.append(i+1)

print(my_list)

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i
print(total)

for i in range(len(my_list)):
    total += my_list[i]

print(total)

