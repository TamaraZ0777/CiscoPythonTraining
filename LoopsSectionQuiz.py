print("Task 1\n")
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

print("Task 2\n")
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
        
    x += 1

print("Task 3\n")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

print("Task 4\n")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end = "")
    
    