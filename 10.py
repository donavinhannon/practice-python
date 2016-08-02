#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Take two lists, say for example these two:
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program
# works on two lists of different sizes. Write this in one line of Python
# using at least one list comprehension.

import random

a = [random.randint(1,100) for i in range(random.randint(10,25))]
b = [random.randint(1,100) for i in range(random.randint(10,25))]
c = set([x for x in a if x in b])

print(c)


# Simplified
w = random.sample(range(100), random.randint(10,25))
y = random.sample(range(100), random.randint(10,25))
z = set([x for x in w if x in y])

print(z)
