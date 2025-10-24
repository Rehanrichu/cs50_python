import random

# Prompt user for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

# Generate random number between 1 and level
number = random.randint(1, level)

# Prompt user for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
