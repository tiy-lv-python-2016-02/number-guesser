# Create a version of the game that asks you to pick the number.
# The computer then takes guesses at what the number is.

### Add function for close call

chances = 5
max_number = 100

print("", "Please enter a number from 1 to {} for the computer to guess.".format(max_number), sep="\n")

# Run until user enters a valid secret number.
secret_number = ""

while not secret_number.isdigit() or int(secret_number) > max_number:
    secret_number = input("--> ")


def computer_version(secret_number, chances=5, max_number=100):
    low, high = 1, max_number

    for counter in range(chances):
        computer_guess = int((low + high) / 2)
        print("", "The computer has {} chances remaining".format(chances - counter), sep="\n")
        print("The computer guesses {}".format(computer_guess))

        if computer_guess == secret_number:
            print("The computer won!")
            return
        elif computer_guess > secret_number:
            high = computer_guess - 1
        else:
            low = computer_guess + 1
    print("The computer is out of guesses. You win!")

# Computer has range of possibilities
# Computer calcs the best guess
# gets feedback: too high/low, close
# re-calc possible range
