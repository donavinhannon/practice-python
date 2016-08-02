#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use
# functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.

num = int(raw_input("How many Fibonnaci numbers do you want to generate??  "))
a = [1,1]

def fib():
    return a.append(a[-1] + a[-2])

for i in range(num-2):  # -2 to compensate for first two numbers in list.a
    fib()

print(a)
