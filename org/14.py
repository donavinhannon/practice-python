#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.


import random

a = random.sample(range(100), random.randint(15,25))
b = random.sample(range(100), random.randint(15,25))

def new_list():
    return set([x for x in a if x in b])

# convert the set to a list to be sorted in ascending order
c = list(new_list())
c.sort()

print(c)
