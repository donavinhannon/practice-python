#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except
# with the words in backwards order. For example, say I type the string:
#     My name is Michele
# Then I would see the string:
#     Michele is name My

usr = str(raw_input("Give me a sentence and I'll reverse it for you: "))
rev = usr.split()
rev.reverse()

print(rev)
