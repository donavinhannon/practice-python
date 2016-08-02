#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number. The
# function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
import random

rlist = sorted([random.randint(1,100) for i in range(20)])

print(rlist)
