#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no
# divisors.). You can (and should!) use your answer to [Exercise 4]

number = int(raw_input("Pick a number to test if it is prime or not: "))
if number%2==0 or (number%3==0 and number!=3) or (number%5==0 and number!=5) or (number%7==0 and number!=7):
    print("This is not a prime number.")
else:
    print("This is a prime number!")

#Simplified
num = int(raw_input("Pick a number to test if it is prime or not: "))
a = [i for i in range(2,num) if num%i==0]
if len(a) > 1:
    print("Not Prime")
else:
    print("Prime")
