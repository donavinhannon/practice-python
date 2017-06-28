#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they
# have a “cow”. For every digit the user guessed correctly in the wrong place
# is a “bull”. Every time the user makes a guess, tell them how many “cows”
# and “bulls” they have. Once the user guesses the correct number, the game is
# over. Keep track of the number of guesses the user makes throughout the game
# and tell the user at the end.
import random

num='0123456789'
code=''.join(random.sample(num,4))
attempt=10

def compare(guess,code):
    bullcow=[0,0]
    remaining_x=[]
    remaining_y=[]
    for x,y in zip(guess,code):
        if x==y:
            bullcow[0]+=1
        else:
            remaining_x.append(x)
            remaining_y.append(y)
    for x in remaining_x:
        if x in remaining_y:
            bullcow[1]+=1
            remaining_y.remove(x)
    return bullcow


while attempt>0:
    guess=input('Enter any four digits: ')
    if len(guess)==4:
        bullcow=compare(guess,code)
        if guess==code:
            print('Congrats, you cracked the code!')
            break
        else:
            print('You have %d cows and %d bulls' % (bullcow[0], bullcow[1]))
            attempt-=1
            print('You have %d attempts left' % attempt)
    else:
        print('Um, there aren\'t four digits in that entry...')
    if attempt==0:
        print('Sorry, the code you were looking for is ' + code)
