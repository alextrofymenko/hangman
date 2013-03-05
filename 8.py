# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *
import string

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    return len(set(secret_word)) == len(set(secret_word) & set(letters_guessed))



def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    word_guessed = []
    for let in secret_word:
        if (let in letters_guessed):
            word_guessed.append(let)
        else:
            word_guessed.append('-')
    print 'Word so far:', join(word_guessed, '')

    letters_remaining = list(string.lowercase)
    for i in range(0, len(letters_remaining)):
        if (letters_remaining[i] in letters_guessed):
            letters_remaining[i] = '-'

    print 'Letters remaining: ', join(letters_remaining, '')

def get_letter():
    guess = lower(raw_input('Please enter a letter:'))
    if (guess in letters_guessed):
        get_letter()

    letters_guessed.append(guess)
    return  guess

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    while (mistakes_made < MAX_GUESSES):
        guess = get_letter()

        if (guess in secret_word):
            if (word_guessed()):
                print "You won!"
                break
        else:
            mistakes_made += 1
            if (mistakes_made == MAX_GUESSES):
                print "You lost!"
                break

        print_hangman_image(mistakes_made)
        print_guessed()

    return None

    
play_hangman()