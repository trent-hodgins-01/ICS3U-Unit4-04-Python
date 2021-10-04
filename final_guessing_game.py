# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/04/2021
# This is a guessing game program
# The user enters in a number between 1 and 100


import random


def main():
    # this function checks to see if the user guessed the correct number
    random_number = random.randint(1, 100)
    # a number between 1 and 100

    # input process and output
    while True:
        number_as_string = input("Guess a number between 1 and 100: ")
        print("")
        try:
            number_as_integer = int(number_as_string)
            print("")
            if number_as_integer == random_number:
                print("You guessed correctly")
                break
            elif number_as_integer > random_number:
                print("Guess lower")
            else:
                print("Guess higher")

        except Exception:
            print("You didn’t enter in a positive integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
