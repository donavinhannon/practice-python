#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed
# too low, too high, or exactly right. (Hint: remember to use the user
# input lessons from the very first exercise)

import random

a = random.randint(1,50)
guess = 1
again = "y"

while again == "y" or again == "Y":
    b = int(raw_input("\nPick a number between 1 and 50:    "))

    if a == b:
        print("Correct! It took you " + str(guess) + " guesses.")
        again = raw_input("\nWant to play again?\nType (Y) for yes, and (N) for no:")
        a = random.randint(1,50)
        guess = 1

    elif a < b:
        print("Nope.. That guess was too high")
        guess += 1

    else:
        print("Nope.. That number is too low")
        guess += 1

# Keep the game going until the user types exit
# Keep track of how many guesses the user has taken,
# and when the game ends, print this out.
