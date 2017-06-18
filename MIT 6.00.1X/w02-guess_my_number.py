top = 100
bottom = 0
guess = 50
guess_text = 'Is your secret number ' + str(guess) + '?'
inn_text = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")

inn = str(input(inn_text))

while inn != 'c':
    if inn == 'h':
        top = int(guess)
        guess = int((top + bottom) / 2)
        print('Is your secret number ' + str(guess) + '?')
        inn = str(input(inn_text))
    elif inn == 'l':
        bottom = int(guess)
        guess = int((top + bottom) / 2)
        print('Is your secret number ' + str(guess) + '?')
        inn = str(input(inn_text))
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess) + '?')
        inn = str(input(inn_text))

print('Game over. Your secret number was: ' + str(guess))


# print("Please think of a number between 0 and 100!")
#
# # At the start the highest the number could be is 100 and the lowest is 0.
# hi = 100
# lo = 0
# guessed = False
#
# # Loop until we guess it correctly
# while not guessed:
#     # Bisection search: guess the midpoint between our current high and low guesses
#     guess = (hi + lo)//2
#     print("Is your secret number " + str(guess)+ "?")
#     user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
#
#     if user_inp == 'c':
#         # We got it right!
#         guessed = True
#     elif user_inp == 'h':
#         # Guess was too high. So make the current guess the highest possible guess.
#         hi = guess
#     elif user_inp == 'l':
#         # Guess was too low. So make the current guess the lowest possible guess.
#         lo = guess
#     else:
#         print("Sorry, I did not understand your input.")
#
# print('Game over. Your secret number was: ' + str(guess))
