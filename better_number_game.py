#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program is the better number guessing game

import random


def main():
    # This function is the better number guessing game

    # Input
    guessed_number = int(input("Pick a number between 0-10: "))
    print("")

    # Process and Output
    if guessed_number == random.randint(0, 10):
        print("You guessed the correct number!")
    else:
        print("Incorrect, please run again.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
