#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number. The
# function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
import random


def find(ordered_list, element_to_find):
    if element_to_find in ordered_list:
        return print("True")
    else:
        return print("False")

if __name__=="__main__":
    rlist = sorted([random.randint(1,100) for i in range(50)])
    num = random.randint(1,100)
    find(rlist,num)
