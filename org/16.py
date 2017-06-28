#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# Write a password generator in Python. Be creative with how you generate
# passwords - strong passwords have a mix of lowercase letters, uppercase
# letters, numbers, and symbols. The passwords should be random, generating
# a new password every time the user asks for a new password. Include your
# run-time code in a main method.
#
# Extra: Ask the user how strong they want their password to be. For weak
# passwords, pick a word or two from a list.

import random

while True:
    strength = raw_input('Strong password or weak password?  ')
    if (strength == 'strong' or strength == 'Strong'):
        num = int(raw_input('Select the number of characters for your' +
                            'password: '))
        a = str('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                 '1234567890-=_+,.<>;:?|!@#$%^&*~`')
        a.split()
        passw = []
        for i in range(num):
            passw.append(random.choice(a))
        print ''.join(map(str, passw))
        break

    elif (strength == 'weak' or strength == 'Weak'):
        a = ['Dog', 'Cat', 'Mouse', 'Bird', 'Hippo']
        passw = [a[random.randint(0,4)], a[random.randint(0,4)]]
        print ''.join(map(str, passw))
        break

    else:
        strength = 0  # Give arbitrary value to strength to make loop restart
