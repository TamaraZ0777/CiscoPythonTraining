c0 = int(input("Enter a number (please non-negative and not 0:"))

if c0 <= 0:
    print("Sorry, your number is 0 or smaller. It cannot be used for the task.")
else:
    counter = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        print(int(c0))
        counter += 1

print("steps = ", counter)