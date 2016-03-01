# Create a version of the game that asks you to pick the number.
# The computer then takes guesses at what the number is.

print("", "Please enter a number for the computer to guess.", sep="\n")


secret_number = ""
while not secret_number.isdigit() or int(secret_number) > 100:
    secret_number = input("--> ")

print("You number is {}".format(secret_number))
