secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("Enter your guess here:"))
while guess != secret_number:
    if guess != secret_number:
        print("No, not correct!")
        guess = int(input("Enter your gess here:"))
        
print("Yes, my secret number is", secret_number)
