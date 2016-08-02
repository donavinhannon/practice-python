#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don’t know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor
# of 26 because 26 / 13 has no remainder.)

num = int(raw_input("Pick a number:"))
a_list = list(range(1,num+1))
b_list = []
for x in a_list:
    if num%x == 0:
        b_list.append(x)
print(b_list)
