# Create a Python program that picks a number at random which you must guess within 5 chances.

import random

print("The computer has selected a number from 1 to 100. You have 5 tries to guess it")

secret_number = random.randint(1, 100)
chances = 5

for counter in range(chances):
    print("You have {} guesses remaining".format(chances))
    guess = ""

    while not guess.isdigit():
        guess = input("What is your guess? ")

    guess = int(guess)

    if guess == secret_number:
        print("You win!")
        print("It took you {} tries".format(counter + 1))
        break
    elif guess < secret_number:
        print("You guessed too low")
    else:
        print("You guessed too high")

# loop through chances
# feedback: chances left, high/low, (close)
#


# for _ in  range(chances):
# break if correct

# if chances too high, losing message


