# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for l in lettersGuessed:
        count += secretWord.count(l)
    return len(secretWord) <= count



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = []
    for l in secretWord:
        if l in lettersGuessed:
            guessedWord.append(l)
        else:
            guessedWord.append('_')
    guessedWord = ''.join(guessedWord)
    return str(guessedWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    choices = []

    for l in string.ascii_lowercase:
        choices.append(l)

    for l in lettersGuessed:
        if l in choices:
            choices.remove(l)
        else:
            continue

    choices = ''.join(choices)
    return choices


def hangman(secretWord):
    '''
    param secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    guesses = 8

    while guesses != -1:
        if guesses == 0:
            print('-----------\nSorry, you ran out of guesses. The word was {}.'.format(secretWord))
            break

        print('-------------\nYou have {} guesses left.'.format(guesses))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = str(input('Please guess a letter: ')).lower()


        if guess not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('------------\nCongratulations, you won!')
                break
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            guesses -= 1


hangman('sea')

# print(getGuessedWord(secretWord, lettersGuessed))
# print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
