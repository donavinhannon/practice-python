#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?

number = int(raw_input("Pick a number, any number:"))
if number%4 == 0:
    print("Your number is divisble by 4.")
elif number%2 > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number
# to divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

num = int(raw_input("Pick a number to check:"))
check = int(raw_input("Pick a number to divide by:"))
if num%check > 0:
    print("Those numbers don't divide into each other evenly.")
else:
    print("Those numbers divide into each other evenly!")
