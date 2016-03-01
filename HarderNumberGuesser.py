# Create a version of the game that asks you to pick the number.
# The computer then takes guesses at what the number is.

chances = 5
max_number = 100

print("", "Please enter a number from 1 to {} for the computer to guess.".format(max_number), sep="\n")


secret_number = ""

# Run until user enters a valid secret number.
while not secret_number.isdigit() or int(secret_number) > max_number:
    secret_number = input("--> ")

secret_number = int(secret_number)


def close_call(low, high, guess, guessed_high):
    if guessed_high:
        return max([guess - 3]), min([guess - 1, high])
    else:
        return max([guess + 1, low]), min([guess + 4, high])


def computer_version(secret_number, chances=5, max_number=100):
    low, high = 1, max_number

    for counter in range(chances):
        computer_guess = int((low + high) / 2 + 0.5)
        print("", "The computer has {} chances remaining".format(chances - counter), sep="\n")
        print("The computer guesses {}".format(computer_guess))

        if computer_guess == secret_number:
            print("The computer won!")
            return
        elif abs(computer_guess - secret_number) < 5:
            print("The computer is close!")
            low, high = close_call(low, high, computer_guess, computer_guess > secret_number)
        elif computer_guess > secret_number:
            high = computer_guess - 1
        else:
            low = computer_guess + 1
    print("The computer is out of guesses. You win!")


computer_version(secret_number)
