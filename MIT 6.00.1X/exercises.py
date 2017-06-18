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