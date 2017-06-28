#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
# (using input), compare them, print out a message of congratulations to the
# winner, and ask if the players want to start a new game)

usr_1 = int(raw_input("Player 1, (0) Rock, (1) Paper, or (2) Scissors:"))
usr_2 = int(raw_input("Player 2, (0) Rock, (1) Paper, or (2) Scissors:"))

if usr_1 == usr_2:
    print("tie game")

elif usr_1 > 2:
    print("Wrong number Player 1, try again")

elif usr_2 > 2:
    print("Wrong number Player 2, try again")

elif usr_1 == 0:
    if usr_2 == 1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

elif usr_1 == 1:
    if usr_2 == 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

elif usr_1 == 2:
    if usr_2 == 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

else:
    print("WTF!")
