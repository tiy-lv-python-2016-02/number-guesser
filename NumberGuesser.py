# Create a Python program that picks a number at random which you must guess within 5 chances.

import random

print("",
      "The computer has selected a number from 1 to 100. You have 5 tries to guess it",
      sep="\n"
      )

secret_number = random.randint(1, 100)
chances = 5


def game(chances, secret_number):
    """
    print statements include blank new lines for formatting.

    The player gets a warning when their guess is within 4.

    :param chances: The number of guesses allowed.
    :param secret_number: The number to be guessed.
    :return: Will return either a winning or losing message.
    """
    for counter in range(chances):
        print("You have {} guesses remaining".format(chances - counter), "", sep="\n")
        guess = ""

        while not guess.isdigit():
            guess = input("What is your guess? ")

        guess = int(guess)
        print("")

        if guess == secret_number:
            print("You win!")
            print("It took you {} tries".format(counter + 1))
            return
        elif guess < secret_number:
            print("You guessed too low")
        else:
            print("You guessed too high")

        if abs(guess - secret_number) < 5:
            print("You are close!")
    print("You have run out of guesses. The secret number was {}".format(secret_number))


game(chances, secret_number)
