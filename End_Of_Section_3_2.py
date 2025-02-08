# Task 1

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Task 2
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# Task 3
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

#Task 4
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
        