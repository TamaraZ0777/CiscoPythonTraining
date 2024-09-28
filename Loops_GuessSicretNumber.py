secret_number = 129

number = 0

print(
"""
+===========================================+
|Welcome to my game, muggle!                |
|Enter an integer number and guess what     |
|number I've picked for you.                |
+===========================================+
""")

while number != secret_number:
    number = int(input("Guess secret number: "))

print("Right, the secret number is:", number)
