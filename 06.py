#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Ask the user for a string and print out whether this string is a palindrome
# or not. (A palindrome is a string that reads the same forwards and backwards.)

sentence = str(raw_input("Give me a palindrome:"))
rvs = sentence[::-1]
if sentence == rvs:
    print("Correct " + sentence + " is a palindrome!")
else:
    print("No, " + sentence + " isn't a palindrome!")
